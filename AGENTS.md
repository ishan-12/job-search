# AGENTS.md

Guidance for any AI coding agent (Claude Code, Cursor, Copilot, Codex, etc.) working in this repo.

**The full guide lives in [`CLAUDE.md`](CLAUDE.md) — read it and follow it.** This file restates only the non-negotiable rules so they're visible to tools that read `AGENTS.md` first.

## ⛔ Non-negotiable rules

1. **NEVER add "Co-Authored-By: Claude" or any AI/agent attribution** to commits, commit messages, or PRs. No `🤖 Generated with …` trailers. Commits must look authored by Ishan alone.
2. **Private career data** — do not push, share, or send repo contents to external services unless Ishan explicitly asks.
3. **Never fabricate resume facts, metrics, or dates.** Everything traces to `profile/candidate-profile.md`; if it's not there, ask.

## Quick facts

- Resume source of truth = Markdown; PDFs are generated (`docker compose run --rm pdf`), always named `Resume_Ishan_Shah.pdf`.
- **Generate PDFs and run tests with Docker only** — `docker compose run --rm pdf` / `docker compose run --rm test`. Never use local `node`/Chrome.
- Don't tailor the generic resumes — copy into `resumes/<track>/companies/<company>/` and tailor there.
- Company folders: lowercase-kebab; dates: always absolute.
- **The metric that matters is `Date Applied`** in `tracking/interview_tracker_master.csv`. Work that doesn't move a row from tailored to applied is deferred.
- `profile/` (singular) = canonical career facts. `scout/profiles/` (plural) = Scout's scoring inputs. **"The profile" always means `profile/candidate-profile.md`** — never write facts into `scout/profiles/`.
- `scout/` has its own `CLAUDE.md`; **the three rules above still win.** All its commands run from inside `scout/`.
- Never nest or rename `tools/` or `resumes/` — the pre-commit test trigger and the PDF renderer are both anchored to those exact paths and fail silently if moved.

See [`CLAUDE.md`](CLAUDE.md) for the full structure, conventions, and workflows.
