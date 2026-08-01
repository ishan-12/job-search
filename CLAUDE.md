# CLAUDE.md — Working guide for this repo

Personal job-search command center for **Ishan Shah** (VP of Engineering / Head of Automation job search): role discovery and scoring, resumes, application tracking, per-company prep, and study guides.

## ⛔ Most important rules

1. **NEVER add "Co-Authored-By: Claude" (or any Claude/AI attribution) to commits, PRs, or commit messages.** No `🤖 Generated with Claude Code` trailers either. Commits must look authored by Ishan alone.
2. **This repo is private career data.** Do not push it anywhere, share it, or send its contents to external services unless Ishan explicitly asks.
3. **Never invent resume facts, metrics, dates, or achievements.** Every number must trace to `profile/candidate-profile.md`. If something isn't there, ask — don't fabricate.

## 🎯 The one metric

**`Date Applied` in `tracking/interview_tracker_master.csv`.**

Work that does not move a row from *tailored* to *applied* is deferred. This repo
has repeatedly out-produced its own submission rate — tailored resumes and
drafted outreach accumulating while the applied count stays flat. Preparation is
the comfortable work; submitting is the work that gets interviews. When choosing
between building something here and sending something out, send it out.

## Repo map

```
profile/candidate-profile.md   Single source of truth for facts/metrics — edit numbers HERE first
profile/*-profile.md           Paste-ready, character-counted copy per platform
behavioral/star-stories.md     STAR answer bank for behavioral rounds
resumes/
  head-of-automation/          HoA track: generic .md + companies/<co>/ tailored variants
  vp-engineering/              VP track:  generic .md + companies/<co>/ tailored variants
companies/<co>/                Prep dossier per org (research, JD, interviewers, notes, outreach)
tracking/
  interview_tracker_master.csv Parent sheet — one row per application
  org-sheets/<co>.csv          Sub-sheet — one row per interview round
prep-guide/                    Study guides (attached to a Claude Project)
scout/                         Job discovery: scrapes LinkedIn, scores roles against the resume
.claude/skills/                Repo skills (apply, outreach)
tools/ + docker-compose.yml    Dockerized resume PDF generator
```

**`profile/` vs `scout/profiles/`** — one letter apart, different jobs.
`profile/` (singular) is canonical career facts. `scout/profiles/` (plural) is
Scout's scoring inputs: its config, criteria, and a symlink to the canonical
resume. **"The profile" always means `profile/candidate-profile.md`.**

## ⚠️ Frozen layout

**Never nest `tools/` or `resumes/`, and never rename them.** Two things depend
on them being exactly where they are, and both fail *silently*:

- `.githooks/pre-commit` triggers the PDF tests on a root-anchored regex
  (`^(tools/md-to-pdf\.(mjs|test\.mjs)|tools/Dockerfile|resumes/.*\.md)$`).
  Move either directory and the tests simply stop running — no error.
- `tools/md-to-pdf.mjs` computes `REPO_ROOT` as the script's parent and renders
  everything under `REPO_ROOT/resumes`.

Renaming the repository directory itself is safe; nesting is not.

## Conventions

- **Resume source of truth is Markdown.** `.md` files are edited; PDFs are generated artifacts — never hand-edit a PDF.
- **PDF output is always `Resume_Ishan_Shah.pdf`** (recruiter-facing name), one per folder. The `.md` keeps a descriptive name (`Resume_VP_<Company>.md`).
- **Generate PDFs with Docker only** (no local Node/Chrome): `docker compose run --rm pdf` (all) or `docker compose run --rm pdf <path/to/Resume.md>` (one).
- **Run tests with Docker only** — `docker compose run --rm test`. Never run the suite with local
  `node`; macOS Chrome is flaky for batch renders and results must match the production image.
- **Don't tailor the generic resumes.** Copy a generic into `resumes/<track>/companies/<company>/` and tailor the copy.
- **Company folder names:** lowercase-kebab (`acme-robotics`), identical under `resumes/*/companies/` and `companies/`.
- **Dates:** always absolute ("Feb 2025"), never relative ("last year").
- **Two resume tracks:** default to **VP of Engineering** for VP roles; use **Head of Automation** where the title/scope fits better.

## Tailoring workflow (drafter → reviewer)

1. Copy generic `.md` into `resumes/<track>/companies/<company>/`, rename descriptively.
2. **Draft:** rewrite summary + reorder/reword bullets to mirror the JD (`companies/<company>/role-and-jd.md`).
3. **Review:** critique the draft against the JD (missing / buried / generic), then revise.
4. `docker compose run --rm pdf <that .md>` → `Resume_Ishan_Shah.pdf`.
5. Log the version + status in `tracking/interview_tracker_master.csv`.

## Editing facts

Change a metric in `profile/candidate-profile.md` **first**, then propagate to both generic resumes and any affected tailored variants so numbers never drift.

## Git

- Branch off `main` for nontrivial work; commit/push only when Ishan asks.
- Commit messages: concise, factual, **no AI attribution / no Co-Authored-By trailer** (see rule 1).
- Don't commit anything with credentials or private third-party info.

## Git hooks & secret scanning (already set up — keep it this way)

- Run `bash tools/setup-hooks.sh` once per clone to enable hooks (`core.hooksPath=.githooks`).
- **pre-commit:** gitleaks secret scan (staged), sensitive-filename block, 2 MB large-file guard,
  and PDF-generation tests when `tools/` or a resume `.md` changes.
- **commit-msg:** every line ≤ 80 chars; blocks AI/agent attribution (enforces rule 1).
- **Tests:** run **only** via Docker — `docker compose run --rm test` (never local `node`), so
  results match the production image. They assert every resume + hostile edge cases render to a
  valid PDF.
- **CI:** `security.yml` (gitleaks) and `ci.yml` (PDF tests) — local hooks can be bypassed
  with `--no-verify`, CI cannot. Actions pinned by SHA.
- **Dependabot** (`.github/dependabot.yml`): weekly updates for the Docker base image + Actions.
- Never weaken these or commit with `--no-verify` to skip the secret scan.

## PDF generator security (already set up — keep it this way)

The generator image is built from the **official Alpine base (pinned by digest)** + Alpine-signed packages, and runs with `network_mode: none`, `read_only: true`, and an in-memory `tmpfs: /tmp`. Don't loosen these without reason.

## First thing in any session

```bash
git config --get core.hooksPath      # must print .githooks
```

`core.hooksPath` is local git config, not committed state, so a fresh clone has
**no hooks** — the only mechanical enforcement of rules 1 and 2 is silently off
until someone runs `bash tools/setup-hooks.sh`. Check before committing.

## scout/ — job discovery

A Python app that scrapes configured LinkedIn searches, cleans each posting, and
scores it against the resume and `scout/profiles/criteria.md`. Survivors land in
a local DuckDB browsed through a small web UI.

**Every command runs from inside `scout/`:**

```bash
cd scout && pipenv run python -m agent.runner            # all configured searches
cd scout && pipenv run python -m agent.runner --url URL  # one ad-hoc URL or job id
cd scout && pipenv run uvicorn app.main:app --reload     # triage UI
docker compose run --rm scout-test                       # its test suite
```

- **Always `cd scout` first.** Run `pytest` from the repo root and it misses
  `scout/pytest.ini`, loses `testpaths`, and collects `scout/scripts/*` as tests.
- `scout/` keeps its own `CLAUDE.md` describing the three-pass pipeline. **The
  three rules at the top of this file still win** wherever they conflict.
- Scout is a file copy of `abraham-jacob/scout` (MIT, see `.claude/NOTICE.md`)
  with local fixes. There is no upstream remote and no automatic sync.

### Scout handles pre-decision candidates; the tracker handles decisions

Scout's `jobs` table is a raw candidate pool — tens of roles per run, most of
which get dismissed. `tracking/interview_tracker_master.csv` is hand-curated
rows for roles you have decided to pursue. **They are not the same schema and
must not be merged.** The handoff is a promotion: a triaged job becomes a new
tracker row with Company Folder and Resume Version Used filled in.

### Where Scout writes career data outside git's reach

Worth knowing, because gitleaks and the pre-commit guards reach none of it:

- `~/Downloads/scout_<run_id>.json` — every scraped description in cleartext.
  Deleted on a successful run; **survives a failed one**.
- Temp system-prompt files under `/tmp` contain the resume; the cleanup is
  skipped if the run's watchdog kills the process.
- `scout/logs/model_calls.log` — only with `--log-model-calls`, but it writes
  the *entire* enrichment prompt (resume + criteria) per call, kept 30 days.
  Never point `[logging] dir` at a path outside the repo.

### Two Scout behaviours that look like micro-optimisations and are not

Do not "simplify" either:

- `agent/claude.py::_neutral_cwd()` runs every subprocess from an empty temp
  directory. The CLI auto-discovers `CLAUDE.md` from its working directory, so
  without this, **this file** and `.claude/settings.json` would be prepended to
  roughly a hundred LLM calls per run. It is a privacy control.
- `tools/md-to-pdf.mjs` scopes its search to `REPO_ROOT/resumes`, which is why
  nothing under `scout/` can ever enter the PDF render set.
