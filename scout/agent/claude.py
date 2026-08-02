"""
Everything that talks to the Claude CLI: the Pass 1 browser scrape (run_claude)
and the headless Pass 2/3 claude-backend call (_run_claude_headless), plus the
subprocess plumbing and model constants only they need.
"""

import functools
import json
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

from agent.llm_common import _add_usage, emit_log, log_model_call

BASE_DIR = Path(__file__).parent.parent

# Pass 1 (browser scrape) and Pass 2 (description cleaning) both run on Haiku —
# cheap and mechanical. Pass 3 (enrichment/scoring) runs on Sonnet — the
# classification, summarization, and fit judgment are the quality-sensitive steps.
SCRAPER_MODEL = "claude-haiku-4-5-20251001"
CLEAN_MODEL   = "claude-haiku-4-5-20251001"
ENRICH_MODEL  = "claude-sonnet-4-6"

# Which Claude model each headless pass uses when backend == "claude". On the
# api backend both passes use the single configured [llm.api] model.
_PASS_CLAUDE_MODEL = {"clean": CLEAN_MODEL, "enrich": ENRICH_MODEL}

# The clean/enrich calls are structured extraction against an explicit rubric;
# extended thinking adds ~1.5K billed-but-invisible output tokens per call
# without improving them, so it is disabled for those subprocesses. The browser
# scrape keeps thinking — it is an agentic multi-step task.
_NO_THINKING_ENV = {**os.environ, "MAX_THINKING_TOKENS": "0"}

# Hard wall-clock cap on each claude subprocess (the browser scrape and each
# enrichment call). Past this we kill the subprocess so a runaway or stuck agent
# can't hang the run indefinitely.
SUBPROCESS_TIMEOUT_S = 240  # 4 minutes

# The two Chrome tools Pass 1 actually needs (see scrape_prompt.md): navigate to
# the search URL, then run the fixed extraction JS.
#
# OBSERVED LIMITATION — this list is a statement of intent, NOT an enforced
# boundary. In a live run the sub-agent called tabs_context_mcp and computer
# (screenshot/wait), neither of which is listed here, and both executed. So
# --allowedTools does not currently gate the Chrome MCP tools the way it gates
# built-ins; the whole extension surface stays reachable, page readers included.
#
# It is kept because it costs nothing, documents the intended surface, and would
# take effect if the flag's enforcement is extended. But do not read it as a
# security control: the real blast-radius reduction here comes from --tools ""
# (drops every built-in) and --strict-mcp-config (drops the host's other MCP
# servers), both of which are verified to work. Restricting Chrome tools
# specifically is unsolved — --disallowedTools may or may not work and is
# untested.
SCRAPE_ALLOWED_TOOLS = (
    "mcp__claude-in-chrome__navigate",
    "mcp__claude-in-chrome__javascript_tool",
)


# ---------------------------------------------------------------------------
# Cross-platform subprocess helpers
# ---------------------------------------------------------------------------

# Give each claude subprocess its own process group so the watchdog can kill the
# whole tree (the browser agent spawns children). POSIX uses a new session;
# Windows uses CREATE_NEW_PROCESS_GROUP — the nearest equivalent.
if os.name == "nt":
    _NEW_GROUP_KWARGS = {"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP}
else:
    _NEW_GROUP_KWARGS = {"start_new_session": True}


def _kill_process_tree(proc: subprocess.Popen) -> None:
    """Hard-kill a subprocess and every child it spawned, cross-platform.

    POSIX SIGKILLs the process group; Windows has no group-signal equivalent,
    so ``taskkill /T`` walks and kills the tree. Best-effort — losing a race
    with a process that already exited is fine.
    """
    if os.name == "nt":
        subprocess.run(["taskkill", "/F", "/T", "/PID", str(proc.pid)],
                       capture_output=True)
    else:
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            pass


@functools.lru_cache(maxsize=None)
def _neutral_cwd() -> str:
    """An empty scratch directory to run every claude subprocess from.

    The CLI auto-discovers CLAUDE.md from its working directory and prepends it
    to the system prompt. Running from BASE_DIR (as this module used to) meant
    Scout's own ~8KB CLAUDE.md — instructions for editing Scout, of no use to a
    scraper or a JSON-emitting classifier — rode along on every single call.
    Measured at ~4.7K input tokens per call, on every job, in both headless
    passes.

    None of the passes read project files: Pass 1 works only through the
    browser, and Pass 2/3 are pure text in, JSON out. So the working directory
    has no purpose beyond that discovery, and an empty directory removes it.
    Created once per process and reused.
    """
    return tempfile.mkdtemp(prefix="scout-claude-cwd-")


def _write_system_prompt(system_prompt: str) -> str:
    """Write a system prompt to a temp file and return its path.

    Keeps large prompts off the command line, for two reasons.

    Security: the enrichment system prompt embeds the candidate's resume,
    profiles, and criteria. On argv that is world-readable through ``ps`` for
    the life of the call — every process on the machine can read it. A 0600
    temp file is visible only to the user.

    Robustness: argv has limits that vary by environment and are far below
    ARG_MAX in some of them. The prompts here run 6-11KB (enrichment plus a
    resume can exceed 20KB), and an over-long argv fails as a SIGKILL with no
    output at all, which surfaces confusingly as a JSON parse error rather
    than anything pointing at size.

    The caller is responsible for unlinking the path.
    """
    fd, path = tempfile.mkstemp(prefix="scout-sysprompt-", suffix=".md")
    with os.fdopen(fd, "w") as handle:
        handle.write(system_prompt)
    return path


@functools.lru_cache(maxsize=None)
def claude_executable() -> str:
    """Absolute path to the ``claude`` CLI, resolved once via PATH.

    Windows installs the CLI as a .cmd shim that ``subprocess`` can't find by
    bare name; ``shutil.which`` honors PATHEXT and returns the real path, which
    we hand to subprocess directly. Raises FileNotFoundError if it isn't
    installed / on PATH (validate_setup surfaces this as a clean startup error).
    """
    resolved = shutil.which("claude")
    if resolved is None:
        raise FileNotFoundError(
            "'claude' CLI not found on PATH. Install Claude Code and make sure "
            "the `claude` command is on your PATH, then re-run."
        )
    return resolved


# ---------------------------------------------------------------------------
# Headless call (Pass 2/3 claude backend)
# ---------------------------------------------------------------------------

def _run_claude_headless(model: str, system_prompt: str,
                         user_message: str) -> str | None:
    """Run one headless `claude --print --output-format json` call.

    The shared subprocess path for the clean and enrich passes: extended
    thinking off, no tools, no MCP servers, hard-capped at SUBPROCESS_TIMEOUT_S.
    Accumulates usage/cost into _tokens and returns the envelope's `result`
    text, or None on timeout / subprocess / parse failure.

    Both passes are pure text in, JSON out — they never call a tool — so the
    entire tool surface is dropped. That is worth real money as well as being
    the safe default, because tool *definitions* are billed as input on every
    call. Measured on a trivial prompt: 8,751 tokens as this used to run,
    294 with the flags below (~97% less), which on a 25-job run is roughly
    420K input tokens across the 50 clean+enrich calls.

    The two flags MUST travel together. ``--tools ""`` alone drops the built-ins
    but leaves whatever MCP servers the host has configured globally, and their
    definitions are then the only thing left in the prompt — measured at 86,641
    tokens, an order of magnitude WORSE than changing nothing. ``--strict-mcp-config``
    is what makes the saving real.

    (This replaces ``--exclude-dynamic-system-prompt-sections``, which the CLI
    no longer accepts — as of 2.1.81 it exits with "unknown option", so every
    pass failed outright. See _neutral_cwd for the other half of what that flag
    used to buy.)
    """
    # Neither large string goes on the command line (see _write_system_prompt):
    # the system prompt is handed over as a file and the job description on
    # stdin, so argv stays a couple of hundred bytes regardless of job size.
    prompt_path = _write_system_prompt(system_prompt)
    cmd = [
        claude_executable(),
        "--print",
        "--model", model,
        "--tools", "",
        "--strict-mcp-config",
        "--system-prompt-file", prompt_path,
        "--output-format", "json",
    ]
    try:
        proc = subprocess.run(
            cmd, input=user_message, cwd=_neutral_cwd(), capture_output=True,
            text=True, timeout=SUBPROCESS_TIMEOUT_S, env=_NO_THINKING_ENV,
        )
        envelope = json.loads(proc.stdout)
    except subprocess.TimeoutExpired:
        print(f"  claude {model} call timed out (> {SUBPROCESS_TIMEOUT_S}s)",
              file=sys.stderr)
        return None
    except (subprocess.SubprocessError, json.JSONDecodeError, ValueError) as exc:
        # stdout is empty on a killed subprocess, which surfaces here as a
        # JSONDecodeError; include the exit code and stderr so the cause is
        # visible instead of just "Expecting value: line 1 column 1".
        rc = locals().get("proc").returncode if "proc" in locals() else "?"
        err = (locals().get("proc").stderr or "")[:200] if "proc" in locals() else ""
        print(f"  claude {model} call failed (rc={rc}): {exc}"
              + (f" | stderr: {err}" if err.strip() else ""), file=sys.stderr)
        return None
    finally:
        try:
            os.unlink(prompt_path)
        except OSError:
            pass

    _add_usage(
        envelope.get("usage", {}),
        envelope.get("total_cost_usd", envelope.get("cost_usd", 0.0)),
    )
    return envelope.get("result", "")


# ---------------------------------------------------------------------------
# Pass 1 — browser scrape
# ---------------------------------------------------------------------------

def _build_scrape_cmd(system_prompt_file: Path, user_message: str) -> list[str]:
    """Read the scrape system prompt, log the call, and build the subprocess cmd.

    The tool surface is pinned to the minimum Pass 1 needs rather than bypassing
    permission checks outright, which is what `--dangerously-skip-permissions`
    used to do here. Three flags do that:

    - ``--tools ""`` drops every built-in tool. The scrape drives a browser and
      needs none of them; leaving them on handed a browser-driving agent Bash,
      Write, Read, and WebFetch for no benefit.
    - ``--strict-mcp-config`` ignores the user's own MCP servers. Without it the
      subprocess inherits whatever the machine has configured globally — in
      practice things like Gmail, Drive, and Slack — none of which Pass 1 has any
      business reaching.
    - ``--allowedTools`` names the Chrome tools the scrape intends to use. Note
      this one is NOT enforced for MCP tools in practice — see the comment on
      SCRAPE_ALLOWED_TOOLS. The first two flags are what actually shrink the
      surface; this one documents intent.

    ORDERING IS LOAD-BEARING: ``--tools`` and ``--allowedTools`` are variadic
    (``<tools...>``), so either one placed immediately before ``user_message``
    swallows it as another tool name and the CLI exits complaining that no
    prompt was given. Both are kept away from the tail of the list; the trailing
    ``--system-prompt``/``--output-format`` take exactly one value each.
    """
    system_prompt = system_prompt_file.read_text()
    log_model_call("scrape", SCRAPER_MODEL, system_prompt, user_message)
    # The prompt file is passed by path rather than by value (see
    # _write_system_prompt). Unlike the headless passes this one is not
    # unlinked here — the caller streams the subprocess and only knows the
    # command is finished later, so run_claude cleans it up.
    return [
        claude_executable(),
        "--print",
        "--model", SCRAPER_MODEL,
        "--verbose",
        "--chrome",
        "--tools", "",
        "--allowedTools", ",".join(SCRAPE_ALLOWED_TOOLS),
        "--strict-mcp-config",
        "--system-prompt-file", _write_system_prompt(system_prompt),
        "--output-format", "stream-json",
        user_message,
    ]


def _spawn_scrape_subprocess(cmd: list[str]) -> subprocess.Popen:
    """Launch the browser-scrape subprocess in its own process group."""
    return subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=_neutral_cwd(),  # keep Scout's own CLAUDE.md out of the prompt
        **_NEW_GROUP_KWARGS,  # own process group so we can kill the whole tree
    )


def _run_scrape_watchdog(proc: subprocess.Popen) -> tuple[threading.Timer, threading.Event]:
    """Start the hard-kill-on-timeout guard for a scrape subprocess.

    Returns the started (not yet cancelled) timer and the event it sets, so
    the caller can check whether it fired and cancel it once the subprocess
    finishes normally.
    """
    timed_out = threading.Event()

    def _kill_on_timeout() -> None:
        timed_out.set()
        _kill_process_tree(proc)

    watchdog = threading.Timer(SUBPROCESS_TIMEOUT_S, _kill_on_timeout)
    watchdog.start()
    return watchdog, timed_out


def _stream_scrape_events(proc: subprocess.Popen) -> tuple[str, dict]:
    """Read and print the scrape subprocess's streamed JSON events live.

    Prints a formatted line per event type (assistant text/tool_use,
    tool_result, system) as they arrive; raw non-JSON lines are printed
    as-is. Returns (text_output, envelope) from the terminal "result" event.
    """
    text_output = ""
    envelope = {}
    for line in proc.stdout:
        line = line.rstrip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            print(f"[raw] {line}", flush=True)
            continue

        event_type = event.get("type", "")

        if event_type == "assistant":
            # Print each content block as it arrives
            for block in event.get("message", {}).get("content", []):
                if block.get("type") == "text":
                    print(f"[agent] {block['text'][:200]}", flush=True)
                elif block.get("type") == "tool_use":
                    print(f"[tool_use] {block.get('name')} — input: {str(block.get('input',''))[:150]}", flush=True)
        elif event_type == "user":
            # Tool results arrive as content blocks inside a "user" event, NOT as
            # a top-level {"type": "tool_result"} event -- which is what this used
            # to match, so a tool result was never printed at all. That made a
            # failing scrape unreadable: the log showed only the sub-agent's
            # narration ("I need you to grant permission") with no sign of the
            # actual error behind it ("Claude in Chrome requires permission"), and
            # those two are not always the same thing. Errors print in full;
            # successes stay truncated because a Voyager payload is megabytes.
            for block in event.get("message", {}).get("content", []):
                if block.get("type") != "tool_result":
                    continue
                content = block.get("content", "")
                if isinstance(content, list):
                    content = " ".join(b.get("text", "") for b in content
                                       if isinstance(b, dict) and b.get("type") == "text")
                if block.get("is_error"):
                    print(f"[tool_error] {str(content)[:500]}", flush=True)
                else:
                    print(f"[tool_result] {str(content)[:200]}", flush=True)
        elif event_type == "result":
            envelope = event
            text_output = event.get("result", "")
        elif event_type == "system":
            print(f"[system] {event.get('subtype','')} — {str(event)[:150]}", flush=True)

    return text_output, envelope


def _check_scrape_result(proc: subprocess.Popen, timed_out: threading.Event,
                         elapsed: float) -> None:
    """Raise on a watchdog kill, else report the exit code/stderr.

    Called after proc.wait() so proc.returncode and proc.stderr are final.
    """
    if timed_out.is_set():
        print(f"[ERROR] browser scrape exceeded {SUBPROCESS_TIMEOUT_S}s "
              f"({elapsed:.0f}s) — subprocess group killed.", file=sys.stderr)
        raise TimeoutError(
            f"browser scrape exceeded {SUBPROCESS_TIMEOUT_S // 60} min and was killed"
        )

    stderr_out = proc.stderr.read()
    if proc.returncode != 0:
        print(f"Scrape agent exited with error (code {proc.returncode}):\n{stderr_out}", file=sys.stderr)
    elif stderr_out.strip():
        print(f"stderr: {stderr_out[:300]}", file=sys.stderr)


def _report_scrape_usage(envelope: dict, elapsed: float) -> None:
    """Accumulate the scrape's usage/cost and print the summary line."""
    usage = envelope.get("usage", {})
    cost = envelope.get("total_cost_usd", envelope.get("cost_usd", 0.0))
    _add_usage(usage, cost)
    in_tok = usage.get("input_tokens", 0)
    out_tok = usage.get("output_tokens", 0)
    cache_r = usage.get("cache_read_input_tokens", 0)
    print(
        f"Scrape done in {elapsed:.0f}s — "
        f"in={in_tok:,} out={out_tok:,} cache_read={cache_r:,} cost=${cost:.4f}",
        flush=True,
    )


def run_claude(system_prompt_file: Path, user_message: str) -> str:
    """
    Invoke the browser scrape subprocess: `claude --print --chrome` on the
    scraper model with the given system prompt and user message. Streams each
    output event to stdout in real time. Token usage is accumulated into _tokens.
    """
    print("Starting browser scrape subprocess...", flush=True)
    t0 = time.monotonic()
    cmd = _build_scrape_cmd(system_prompt_file, user_message)
    try:
        proc = _spawn_scrape_subprocess(cmd)
        watchdog, timed_out = _run_scrape_watchdog(proc)
        text_output, envelope = _stream_scrape_events(proc)
        proc.wait()
        watchdog.cancel()
        elapsed = time.monotonic() - t0
        _check_scrape_result(proc, timed_out, elapsed)
        _report_scrape_usage(envelope, elapsed)
        return text_output
    finally:
        # Remove the temp system-prompt file _build_scrape_cmd created; the
        # path is the argument right after the flag.
        try:
            os.unlink(cmd[cmd.index("--system-prompt-file") + 1])
        except (ValueError, IndexError, OSError):
            pass
