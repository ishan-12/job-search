# Resumes

Two tracks, each with a generic base and per-company tailored variants.

```
resumes/
├── head-of-automation/
│   ├── Resume_HeadOfAutomation_Generic.md   ← base (don't tailor)
│   └── companies/<company>/                  ← tailored variant + exported PDF
├── vp-engineering/
│   ├── Resume_VP_Generic.md                  ← base (don't tailor)
│   └── companies/<company>/                  ← tailored variant + exported PDF
```

## Which track to use

- **VP of Engineering** — default for VP-titled roles; leads with AI platforms, agent engineering, MLOps, regulated industries, and org leadership.
- **Head of Automation** — use where the title/scope maps to automation, platform, DevOps, and quality leadership.

Both are current as of the last edit. Facts live in [`../profile/candidate-profile.md`](../profile/candidate-profile.md) — change a metric there first, then update both generic resumes.

## Tailoring a resume for a company

1. `cp -r <track>/companies/_TEMPLATE <track>/companies/<company>` (or copy the generic `.md` in).
2. Rename the `.md` to `Resume_<Track>_<Company>.md` (descriptive source name).
3. **Draft:** rewrite the summary and reorder/reword bullets to match the JD's language and priorities. Pull the JD from [`../companies/<company>/role-and-jd.md`](../companies/).
4. **Review:** critique the draft against the JD (what's missing/buried/generic), then revise.
5. Generate the PDF (below) and log the version in [`../tracking/interview_tracker_master.csv`](../tracking/interview_tracker_master.csv).

## Exporting Markdown → PDF

The `.md` files are the source of truth; PDFs are generated from them via Docker (no local Node/Chrome needed — just Docker running):

```bash
docker compose run --rm pdf                                          # rebuild every resume PDF
docker compose run --rm pdf resumes/vp-engineering/companies/<co>/Resume_VP_<Co>.md   # rebuild one
```

The output PDF is **always `Resume_Ishan_Shah.pdf`** (the recruiter-facing filename), written next to its `.md`. Each folder holds one resume, so the fixed name never collides. Editorial `> notes` in the `.md` are dropped from the PDF. Both resumes are tuned to fit 2 pages. Fonts render in Carlito (Calibri-compatible), baked into the image for consistent output on any machine.
