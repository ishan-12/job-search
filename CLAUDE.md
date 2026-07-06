# CLAUDE.md — Working guide for this repo

Personal interview-prep command center for **Ishan Shah** (VP of Engineering / Head of Automation job search): resumes, application tracking, per-company prep, and study guides.

## ⛔ Most important rules

1. **NEVER add "Co-Authored-By: Claude" (or any Claude/AI attribution) to commits, PRs, or commit messages.** No `🤖 Generated with Claude Code` trailers either. Commits must look authored by Ishan alone.
2. **This repo is private career data.** Do not push it anywhere, share it, or send its contents to external services unless Ishan explicitly asks.
3. **Never invent resume facts, metrics, dates, or achievements.** Every number must trace to `profile/candidate-profile.md`. If something isn't there, ask — don't fabricate.

## Repo map

```
profile/candidate-profile.md   Single source of truth for facts/metrics — edit numbers HERE first
behavioral/star-stories.md     STAR answer bank for behavioral rounds
resumes/
  head-of-automation/          HoA track: generic .md + companies/<co>/ tailored variants
  vp-engineering/              VP track:  generic .md + companies/<co>/ tailored variants
companies/<co>/                Prep dossier per org (research, JD, interviewers, notes)
tracking/
  interview_tracker_master.csv Parent sheet — one row per application
  org-sheets/<co>.csv          Sub-sheet — one row per interview round
prep-guide/                    Study guides (attached to a Claude Project)
tools/ + docker-compose.yml    Dockerized resume PDF generator
```

## Conventions

- **Resume source of truth is Markdown.** `.md` files are edited; PDFs are generated artifacts — never hand-edit a PDF.
- **PDF output is always `Resume_Ishan_Shah.pdf`** (recruiter-facing name), one per folder. The `.md` keeps a descriptive name (`Resume_VP_<Company>.md`).
- **Generate PDFs with Docker only** (no local Node/Chrome): `docker compose run --rm pdf` (all) or `docker compose run --rm pdf <path/to/Resume.md>` (one).
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
- **pre-commit:** gitleaks secret scan (staged), sensitive-filename block, 2 MB large-file guard.
- **commit-msg:** every line ≤ 80 chars; blocks AI/agent attribution (enforces rule 1).
- **CI** (`.github/workflows/security.yml`): authoritative gitleaks scan — local hooks can be
  bypassed with `--no-verify`, CI cannot. Actions pinned by SHA.
- **Dependabot** (`.github/dependabot.yml`): weekly updates for the Docker base image + Actions.
- Never weaken these or commit with `--no-verify` to skip the secret scan.

## PDF generator security (already set up — keep it this way)

The generator image is built from the **official Alpine base (pinned by digest)** + Alpine-signed packages, and runs with `network_mode: none`, `read_only: true`, and an in-memory `tmpfs: /tmp`. Don't loosen these without reason.
