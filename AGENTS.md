# AGENTS.md

Guidance for any AI coding agent (Claude Code, Cursor, Copilot, Codex, etc.) working in this repo.

**The full guide lives in [`CLAUDE.md`](CLAUDE.md) — read it and follow it.** This file restates only the non-negotiable rules so they're visible to tools that read `AGENTS.md` first.

## ⛔ Non-negotiable rules

1. **NEVER add "Co-Authored-By: Claude" or any AI/agent attribution** to commits, commit messages, or PRs. No `🤖 Generated with …` trailers. Commits must look authored by Ishan alone.
2. **Private career data** — do not push, share, or send repo contents to external services unless Ishan explicitly asks.
3. **Never fabricate resume facts, metrics, or dates.** Everything traces to `profile/candidate-profile.md`; if it's not there, ask.

## Quick facts

- Resume source of truth = Markdown; PDFs are generated (`docker compose run --rm pdf`), always named `Resume_Ishan_Shah.pdf`.
- Don't tailor the generic resumes — copy into `resumes/<track>/companies/<company>/` and tailor there.
- Company folders: lowercase-kebab; dates: always absolute.

See [`CLAUDE.md`](CLAUDE.md) for the full structure, conventions, and workflows.
