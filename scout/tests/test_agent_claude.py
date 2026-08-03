"""Tests for agent/claude.py — the Claude-CLI-calling layer."""

import pytest
from pathlib import Path
from unittest.mock import MagicMock

import agent.claude as claude


@pytest.fixture
def scrape_cmd(tmp_path, monkeypatch):
    """Build a Pass 1 scrape command with the CLI path and prompt file stubbed."""
    monkeypatch.setattr(claude, "claude_executable", lambda: "/usr/local/bin/claude")
    prompt_file = tmp_path / "scrape_prompt.md"
    prompt_file.write_text("SYSTEM PROMPT BODY")
    return claude._build_scrape_cmd(prompt_file, "USER MESSAGE")


class TestBuildScrapeCmd:
    """Test the Pass 1 browser-scrape command's tool-surface restrictions.

    Pass 1 drives a real, logged-in Chrome session, so the blast radius of this
    subprocess is the security-sensitive part of the pipeline; these assertions
    pin it down rather than trusting the scrape prompt's own "hard rules", which
    are guidance to a model and not an enforced boundary.
    """

    def test_never_skips_permission_checks(self, scrape_cmd):
        """--dangerously-skip-permissions must not come back.

        It bypassed every permission check for a browser-driving agent that also
        inherited Bash, Write, and the machine's global MCP servers.
        """
        assert "--dangerously-skip-permissions" not in scrape_cmd
        assert "--permission-mode" not in scrape_cmd  # nor a bypassPermissions equivalent

    def test_drops_builtin_tools_and_foreign_mcp_servers(self, scrape_cmd):
        """Built-in tools are disabled and the user's own MCP servers ignored."""
        assert scrape_cmd[scrape_cmd.index("--tools") + 1] == ""
        assert "--strict-mcp-config" in scrape_cmd

    def test_allows_only_the_three_tools_the_scrape_needs(self, scrape_cmd):
        """Exactly the Chrome tools the scrape needs are granted, no more.

        tabs_context_mcp is required: without it the very first call is refused
        and the scrape returns 0 jobs. The refusal reads "Claude in Chrome
        requires permission", which looks like a browser problem rather than an
        allowlist one -- hence this test pinning the contents exactly.
        """
        allowed = scrape_cmd[scrape_cmd.index("--allowedTools") + 1].split(",")
        assert allowed == [
            "mcp__claude-in-chrome__tabs_context_mcp",
            "mcp__claude-in-chrome__navigate",
            "mcp__claude-in-chrome__javascript_tool",
        ]

    @pytest.mark.parametrize("denied", [
        "read_page", "get_page_text", "find",        # page readers → injection input
        "form_input", "computer", "shortcuts_execute",  # actors on the page
        "tabs_create_mcp", "upload_image",
    ])
    def test_page_readers_and_actors_stay_out(self, scrape_cmd, denied):
        """No page-reading or page-acting Chrome tool appears in the allowlist.

        The allowlist IS enforced for Chrome MCP tools -- verified live, same
        browser and moment, only the list differing. So withholding the page
        readers genuinely keeps untrusted posting text out of the model's
        context, and withholding the actors genuinely prevents clicking and
        typing. See the comment on SCRAPE_ALLOWED_TOOLS.
        """
        assert f"mcp__claude-in-chrome__{denied}" not in " ".join(scrape_cmd)

    def test_variadic_flags_are_not_last_before_the_prompt(self, scrape_cmd):
        """--tools/--allowedTools must never sit immediately before user_message.

        Both are variadic (<tools...>), so a flag placed at the tail eats the
        prompt as one more tool name and the CLI exits with "Input must be
        provided..." — a silent breakage that costs a whole run, and one that
        reordering this list could reintroduce at any time.
        """
        assert scrape_cmd[-1] == "USER MESSAGE"
        for flag in ("--tools", "--allowedTools"):
            # the value directly after each variadic flag must not be the prompt,
            # and the flag must be followed by a further flag, not the tail
            assert scrape_cmd.index(flag) + 2 < len(scrape_cmd)
            assert scrape_cmd[scrape_cmd.index(flag) + 2].startswith("--")

    def test_still_drives_chrome_with_the_scraper_model(self, scrape_cmd):
        """The hardening leaves the scrape itself intact."""
        assert "--chrome" in scrape_cmd
        assert scrape_cmd[scrape_cmd.index("--model") + 1] == claude.SCRAPER_MODEL
        assert scrape_cmd[scrape_cmd.index("--output-format") + 1] == "stream-json"

    def test_system_prompt_goes_via_file_not_argv(self, scrape_cmd):
        """The prompt is passed as a file path, and that file holds the prompt.

        Keeping it off argv matters for more than tidiness: the enrichment
        prompt embeds the candidate's resume, and argv is readable via ``ps`` by
        every process on the machine. An over-long argv also dies as a bare
        SIGKILL with no output, which is near-impossible to diagnose from the
        JSON parse error it surfaces as.
        """
        assert "--system-prompt" not in scrape_cmd
        path = scrape_cmd[scrape_cmd.index("--system-prompt-file") + 1]
        assert Path(path).read_text() == "SYSTEM PROMPT BODY"
        assert "SYSTEM PROMPT BODY" not in " ".join(scrape_cmd)

    def test_argv_stays_small_regardless_of_prompt_size(self, tmp_path, monkeypatch):
        """A large system prompt does not inflate argv."""
        monkeypatch.setattr(claude, "claude_executable", lambda: "/usr/local/bin/claude")
        big = tmp_path / "big.md"
        big.write_text("x" * 200_000)
        cmd = claude._build_scrape_cmd(big, "USER MESSAGE")
        assert sum(len(a) for a in cmd) < 2_000


class TestClaudeExecutable:
    """Test cross-platform resolution of the claude CLI."""

    def test_resolves_via_which(self, monkeypatch):
        """Returns the absolute path shutil.which finds."""
        claude.claude_executable.cache_clear()
        monkeypatch.setattr(claude.shutil, "which", lambda name: "/usr/local/bin/claude")
        try:
            assert claude.claude_executable() == "/usr/local/bin/claude"
        finally:
            claude.claude_executable.cache_clear()

    def test_raises_when_missing(self, monkeypatch):
        """Raises FileNotFoundError when claude isn't on PATH."""
        claude.claude_executable.cache_clear()
        monkeypatch.setattr(claude.shutil, "which", lambda name: None)
        try:
            with pytest.raises(FileNotFoundError, match="claude"):
                claude.claude_executable()
        finally:
            claude.claude_executable.cache_clear()


class TestKillProcessTree:
    """Test cross-platform subprocess-tree kill."""

    def test_posix_kills_process_group(self, monkeypatch):
        """On POSIX, SIGKILL is sent to the child's process group."""
        killed = {}
        monkeypatch.setattr(claude.os, "name", "posix")
        monkeypatch.setattr(claude.os, "getpgid", lambda pid: 4242)
        monkeypatch.setattr(claude.os, "killpg",
                            lambda pgid, sig: killed.update(pgid=pgid, sig=sig))
        proc = MagicMock()
        proc.pid = 999

        claude._kill_process_tree(proc)

        assert killed == {"pgid": 4242, "sig": claude.signal.SIGKILL}

    def test_posix_swallows_already_dead(self, monkeypatch):
        """A process that already exited doesn't raise out of the kill."""
        monkeypatch.setattr(claude.os, "name", "posix")

        def _gone(pid):
            raise ProcessLookupError()

        monkeypatch.setattr(claude.os, "getpgid", _gone)
        proc = MagicMock()
        proc.pid = 1

        claude._kill_process_tree(proc)  # must not raise

    def test_windows_uses_taskkill(self, monkeypatch):
        """On Windows, taskkill /T is invoked to walk the tree."""
        calls = {}
        monkeypatch.setattr(claude.os, "name", "nt")
        monkeypatch.setattr(claude.subprocess, "run",
                            lambda cmd, **kw: calls.update(cmd=cmd))
        proc = MagicMock()
        proc.pid = 4321

        claude._kill_process_tree(proc)

        assert calls["cmd"] == ["taskkill", "/F", "/T", "/PID", "4321"]
