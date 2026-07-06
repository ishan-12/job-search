# Interview Prep

Personal command center for Ishan Shah's VP / Head-of-Automation interview process — resumes, application tracking, per-company prep, and study guides.

## Structure

```
Interview_Prep/
├── README.md                     ← you are here
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

Adapted from the [ai-job-search](https://github.com/MadsLorentzen/ai-job-search) drafter/reviewer pattern:

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

## What was borrowed from ai-job-search

Concepts only (that repo is Danish-market, LaTeX + scraper heavy): the CSV tracker, modular profile/STAR source files, the drafter→reviewer tailoring loop, and the per-company fit/prep dossier. Skipped: LaTeX toolchain, job-portal scrapers, Bun CLIs.
