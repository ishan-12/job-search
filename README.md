# job-search

Personal job-search command center for Ishan Shah (VP of Engineering / Head of
Automation): role discovery and scoring, resumes, application tracking,
per-company prep, and study guides.

**The metric this repo optimises is `Date Applied`** in
`tracking/interview_tracker_master.csv`. Work that does not move a row from
tailored to applied is deferred.

## Structure

```
job-search/
├── README.md                     ← you are here
├── scout/                        Job discovery — scrapes LinkedIn, scores roles vs the resume
│                                 (own CLAUDE.md; all commands run from inside scout/)
├── .claude/skills/               Repo skills: apply, outreach
├── profile/                      Single source of truth for facts, metrics, career narrative
│   └── candidate-profile.md      Reuse these numbers/bullets across every resume variant
├── behavioral/                   Interview answer banks
│   └── star-stories.md           STAR stories mapped to common leadership questions
├── resumes/                      All resume documents (source-of-truth in Markdown; drop PDFs alongside)
│   ├── head-of-automation/
│   │   ├── Resume_HeadOfAutomation_Generic.md
│   │   └── companies/<company>/  Tailored variant per org
│   └── vp-engineering/
│       ├── Resume_VP_Generic.md
│       └── companies/<company>/  Tailored variant per org
├── companies/                    Deep prep dossier per org (research, JD, interviewers, notes)
│   └── <company>/                Copy from companies/_TEMPLATE/
├── tracking/                     Application + interview tracking (CSV → Google Sheets)
│   ├── interview_tracker_master.csv   Parent sheet: one row per application
│   └── org-sheets/<company>.csv       Sub-sheet: one row per interview round
├── prep-guide/                   Study guides (used as a Claude Project)
│   └── 01-llm-fundamentals.md
├── tools/                        Resume PDF generator (Dockerized)
│   ├── md-to-pdf.mjs
│   └── Dockerfile
└── docker-compose.yml            `docker compose run --rm pdf` → regenerate PDFs
```

## Generating resume PDFs

`.md` is the source of truth; PDFs are generated (all named `Resume_Ishan_Shah.pdf`). Requires only Docker running — no local Node/Chrome:

```bash
docker compose run --rm pdf                      # rebuild every resume PDF
docker compose run --rm pdf <path/to/Resume.md>  # rebuild one
```

## How the pieces fit together

1. **`profile/candidate-profile.md`** holds every reusable fact — metrics, dates, one-liners. Edit facts *here* first, then propagate to resume variants so numbers never drift.
2. **`resumes/<track>/Resume_*_Generic.md`** is the base resume for each track (Head of Automation vs. VP of Engineering). Keep these polished and current.
3. When applying to a company, run the **tailoring workflow** below to produce `resumes/<track>/companies/<company>/`.
4. **`companies/<company>/`** holds the intel that resume can't: company research, the actual JD, interviewer bios, and round-by-round prep notes.
5. **`tracking/`** is the operational layer — master sheet for pipeline overview, one org sub-sheet per active process.
6. **`prep-guide/`** is your study material (attach the whole folder to a Claude Project).

## Resume tailoring workflow (drafter → reviewer)

Encoded as a skill in `.claude/skills/apply/SKILL.md`, which adds the honesty
checks (requirement coverage, the interview backtrack test) and the PDF
verification step:

1. Copy the generic resume into `resumes/<track>/companies/<company>/`.
2. **Draft:** rewrite the summary + reorder/reword bullets to mirror the JD's language and priorities.
3. **Review:** critique the draft against the JD — what's missing, what's buried, what reads generic — then revise.
4. Export to PDF, drop the PDF in the same folder, log it in the tracker.

## Conventions

- **Company folder name:** lowercase-kebab (`acme-robotics`), used identically under `resumes/*/companies/` and `companies/`.
- **Resume source (`.md`):** descriptive name — `Resume_<Track>_<Company>.md`; generic = `Resume_<Track>_Generic.md`.
- **Resume output (`.pdf`):** always `Resume_Ishan_Shah.pdf` (recruiter-facing name), generated next to the `.md` via `docker compose run --rm pdf`. One resume per folder, so the fixed PDF name never collides.
- **Track chooser:** default to the **VP of Engineering** resume for VP roles; use **Head of Automation** where the title/scope matches better. See both under `resumes/`.
- **Dates:** always absolute (e.g. "Feb 2025"), never "last year".

## Provenance

- `scout/` is a copy of [abraham-jacob/scout](https://github.com/abraham-jacob/scout)
  (MIT), imported without git history and modified since. Its `LICENSE` is retained.
- `.claude/skills/` is authored here. A small number of written rules are
  derived from [ai-job-search](https://github.com/MadsLorentzen/ai-job-search)
  (MIT) — the untrusted-posting trust boundary, the interview backtrack test,
  relevance-weighted cutting, and an interview question bank. `tools/verify_pdf.py`
  is the only file taken from it. Not a tracked fork; there is no upstream remote,
  deliberately, because this repo is private career data.

See `.claude/NOTICE.md` for the licence texts.

