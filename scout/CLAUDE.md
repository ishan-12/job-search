# CLAUDE.md — scout/

> **The three rules in the repo-root `CLAUDE.md` win wherever they conflict with
> anything here**: no AI attribution in commits, this is private career data, and
> never invent resume facts. This file describes only how Scout's pipeline works.
>
> Scout is a file copy of [abraham-jacob/scout](https://github.com/abraham-jacob/scout)
> (MIT — see `../.claude/NOTICE.md` and `LICENSE`), imported without git history
> and since modified locally. There is no upstream remote; nothing here syncs.
>
> **Every command below runs from inside `scout/`.** Running pytest from the repo
> root misses `pytest.ini`, loses `testpaths`, and collects `scripts/*` as tests.

## What Scout is

Scout scrapes the LinkedIn saved-search URLs configured under
`[[linkedin_searches]]`, extracts the jobs behind them, classifies and summarizes
each one with Claude, and stores the survivors in a local DuckDB database that a
small FastAPI + HTMX web UI browses. It is a single-user local app (the run state
lives in memory, not the DB) for one job seeker. Scout is open source under MIT.

## Commands

Dependencies are managed with **pipenv** (Python 3.12). Prefix runtime commands with
`pipenv run`.

```bash
pipenv install --dev                       # install deps

# Web UI (FastAPI). Serves the job list and the "Run Scout" button.
pipenv run uvicorn app.main:app --reload

# Run the agent pipeline directly (the web UI shells out to this same command):
pipenv run python -m agent.runner                  # scrape every configured [[linkedin_searches]] entry
pipenv run python -m agent.runner --url <linkedin_url>   # scrape one ad-hoc URL, ignoring config

# Initialise / inspect the DuckDB schema
pipenv run python -m app.database

# Tests (pytest, config in pytest.ini — testpaths=tests, asyncio_mode=auto)
pipenv run pytest                          # all tests
pipenv run pytest tests/test_agent_runner.py           # one file
pipenv run pytest tests/test_agent_runner.py::TestName::test_case   # one test
pipenv run pytest -m unit                  # by marker (unit / integration)
pipenv run unit-tests                      # full suite with junit + HTML coverage
```

## Architecture

The system is **three passes orchestrated by `agent/runner.py`** — a browser
scrape (Pass 1) and two headless passes, description cleaning (Pass 2) and
per-job enrichment/scoring (Pass 3) — launched as a subprocess by the web UI.
Read `agent/runner.py`'s module docstring first — it is the map for the whole
pipeline, and its Pass 1/2/3 numbering is authoritative.

### Pass 1 — browser scrape (Haiku), `agent/scrape_prompt.md` / `agent/scrape_single_prompt.md`
`runner.py` spawns `claude --print --chrome` on Haiku with `scrape_prompt.md`. That
sub-agent does **no filtering**: it hits LinkedIn's internal **Voyager job-postings
API** via `javascript_tool` (not the accessibility tree, not card-clicking) to pull
every field for every job on page 1, including virtualized cards that never render.
A single LinkedIn job URL (a `/jobs/view/<id>` link, or a search URL's
`currentJobId` toggled to "just this job" in the UI) is detected by
`runner.extract_single_job_id()` and routed to `scrape_single_prompt.md`
instead — the same Voyager fetch for one job ID directly, skipping the
search-results DOM discovery entirely since the job ID is already known.

The critical constraint: each job description is 5–13 KB, and the Chrome extension's
**privacy filter blocks large `javascript_tool` return values**. So the sub-agent
writes the whole batch to `window.__jobs` and blob-**downloads** it as
`scout_<run_id>.json` to the browser's Downloads folder. Only a one-line status
comes back through the extension. `runner.py::load_downloaded_jobs` then polls the
Downloads folder (`download_dir()`, config-overridable) for that file, reads it, and
deletes it. The blob download is load-bearing; do not try to route descriptions back
through the tool return value. There is deliberately **no shell step** — the sub-agent
does not move the file — so the handoff works identically on Windows/macOS/Linux
(the poll replaces the wait-loop the agent used to run in bash).

### Between passes — deterministic filters
`apply_deterministic_filters()` cheaply drops jobs before spending any LLM call:
scrape errors, jobs already in the DB, already-applied, closed (`jobState != LISTED`),
jobs with no company name, and companies in the config's `[filters]
exclude_companies` (also enforced again in `save_jobs`).

### Pass 2 — description cleaning (Haiku, parallel), `agent/clean_prompt.md`
For each survivor, one headless call (`run_headless("clean", …)`) strips non-role
boilerplate from the raw description — EEO/DEI statements, legal disclaimers,
generic culture/benefits marketing, "About [Company]" fluff — and returns a single
`{"description_clean": "..."}` JSON field. Runs `MAX_WORKERS`-wide via a
`ThreadPoolExecutor`. A failed call falls back to the raw description so Pass 3
always has something to work with. On the Claude backend this is Haiku
(`CLEAN_MODEL`); on the api backend it's the configured `[llm.api] model`.

### Pass 3 — per-job enrichment (Sonnet, parallel), `agent/enrichment_prompt.md`
For each survivor, one headless `claude --print` Sonnet call classifies the role into
one of the **user-configured role types** (or `Other`), writes a 2–4 sentence
summary, tags the job, and scores it against the candidate's resume/profiles/criteria.
`enrichment_prompt.md` is a single file covering classification, summary, tags, and
scoring instructions. Runs `MAX_WORKERS`-wide via a `ThreadPoolExecutor`. Jobs classified `Other`
(or that fail to enrich) are dropped; the rest are saved via `agent/tools.py::save_jobs`,
which also does repost detection and unwraps LinkedIn safety-redirect apply URLs.

All user configuration lives in `profiles/config.toml` (loaded and validated by
`app/config.py::load_config`). The file is **required**, with six required
sections and no in-code defaults: `[[roles]]` (≥1 role type),
`[[linkedin_searches]]` (≥1 named saved-search URL, scraped every run —
`name` is the alias shown in the UI/logs in place of the raw URL),
`[filters]` (exclude_companies, may be empty), `[scoring]` (fit/criteria
weights summing to 1, plus dealbreaker_cap used by `compute_match_score`),
`[logging]` (dir for the daily app log and the opt-in model-call log; see
`app/logging_setup.py`), and `[llm]` (`backend` + `max_workers`, below). One
optional section, `[scrape]`, carries `download_dir` — where the browser saves
the scrape blob; it defaults to `~/Downloads` (correct on Windows/macOS/Linux)
and `runner.download_dir()` expands it, so it's the only config path with a
cross-platform default rather than failing loudly. `[llm]` carries `backend`
(required, `"claude"` or `"api"` — no default, so the config always states
which one) which selects the backend for the two **headless** passes —
description cleaning and enrichment/scoring — via `agent/llm.py::run_headless()`, and
`max_workers` (required, the Pass 2/3 pool width, tuned per backend). `"api"`
routes both passes (together, never split) to any OpenAI-compatible endpoint
(e.g. Ollama, local or remote) configured under `[llm.api]` (`base_url`, `model`,
optional `api_key`/`timeout`). Two optional per-pass sub-tables, `[llm.api.clean]`
and `[llm.api.enrich]`, carry request parameters (e.g. `temperature`,
`reasoning_effort`) merged verbatim into that pass's chat-completion JSON by
`agent/llm_api.py::_run_api_llm`; values must be scalars and may not set the
pipeline-owned `model`/`messages`/`stream` keys (validated in
`config._parse_api_params`). The browser scrape always runs on Claude.
Each role carries the classification definition injected into the prompt's
`{{ROLE_DEFINITIONS}}`/`{{ROLE_ENUM}}` placeholders, an optional per-role profile
file for scoring, and drives the UI filter buttons and chip colors. `jobs.role_type`
stores the role's `name` verbatim. `runner.validate_setup()` fails fast at pipeline
start: the roles config must load, `profiles/resume.md` must exist, and a role's
referenced profile file must exist (roles may omit `profile` to score on the resume
alone).

### Progress events → web UI
`runner.py` emits `SCOUT_PROGRESS <json>` sentinel lines on stdout. `app/main.py`
reads the subprocess stdout line by line and folds those events into the in-memory
`_run` dict (`_apply_event`), which renders the live "run drawer" partial that HTMX
polls at `GET /scout/status`. Event `key`s in `runner.py`'s `emit()` calls must stay
in sync with `GLOBAL_STEPS` / `SEARCH_STEPS` in `app/main.py`.

### Data layer
`app/database.py` — DuckDB at `data/scout.duckdb`, two tables (`scrape_runs`, `jobs`).
`role_type` is per-job (derived from the title/description at enrichment), not per-run.
`scrape_runs.search_name` holds the configured search's `name` alias (from the
`[[linkedin_searches]]` redesign, which replaced the earlier Gmail-derived
`email_subject`/`email_date` columns — the one-time migration off that schema,
`_migrate_scrape_runs_schema()`, was retired once no pre-migration databases
remained).

### `agent/tools.py`
Plain Python DB helpers (`create_scrape_run`, `get_existing_job_ids`, `save_jobs`,
etc.) called directly by `runner.py`.

### The LLM-calling layer (`agent/llm_common.py`, `agent/claude.py`, `agent/llm_api.py`, `agent/llm.py`)
`runner.py` holds only pipeline orchestration; every function that actually talks to
a backend lives in one of four small modules, one-directional
(`runner.py` → `llm.py` → {`claude.py`, `llm_api.py`} → `llm_common.py`, never the
reverse — this is what keeps the import graph acyclic):
- `agent/llm_common.py` — cross-cutting plumbing only, no backend logic: progress
  events (`emit`/`emit_log`/`PROGRESS_SENTINEL`), `log_model_call()`, token/cost
  accounting (`_add_usage`/`print_token_summary`/`_tokens`), and `SetupError` (raised
  by both `runner.py`'s `check_setup` and `llm_api.py`'s `_verify_api_llm` — neither
  owns the other, so it lives in the shared leaf module).
- `agent/claude.py` — everything that talks to the Claude CLI: `run_claude` (Pass 1
  browser scrape), `_run_claude_headless` (Pass 2/3 claude backend), `claude_executable`,
  `_kill_process_tree`, and the `SCRAPER_MODEL`/`CLEAN_MODEL`/`ENRICH_MODEL` constants.
- `agent/llm_api.py` — everything that talks to the OpenAI-compatible endpoint:
  `_run_api_llm`, `_verify_api_llm`, `_warm_api_llm`, `_api_endpoint`.
- `agent/llm.py` — the thin router: `run_headless()` dispatches to `claude.py` or
  `llm_api.py` based on `config.llm_backend`.

`runner.py` imports directly from whichever module owns a given name (e.g.
`CLEAN_MODEL`/`ENRICH_MODEL` come straight from `agent.claude`, not funneled through
`agent.llm`) — only the actual Pass 2/3 backend *dispatch* goes through `llm.py`.
Tests mirror this: `tests/test_agent_llm_common.py`, `tests/test_agent_claude.py`,
`tests/test_agent_llm_api.py`, `tests/test_agent_llm.py`.

## LinkedIn scraping notes (in `scrape_prompt.md`)

Two page structures exist and the Step-1 JS handles both: `/search-results/` uses the
`componentkey` attribute; `/search/` (and `/comm/jobs/search` redirects) uses
`data-occludable-job-id`. The Voyager API is the sole data source — salary is not in
the API and is regex-parsed out of the description text.
