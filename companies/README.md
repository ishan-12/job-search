# Companies

Deep prep dossier per org — the intel a resume can't hold. One folder per company, copied from `_TEMPLATE/`.

```
companies/
├── _TEMPLATE/
│   ├── company-research.md    Business, product, funding, culture, why-them
│   ├── role-and-jd.md         Pasted JD + your read on it (drives resume tailoring)
│   ├── interviewers.md        Who you're meeting, backgrounds, likely angles
│   └── prep-notes.md          Round-by-round notes, questions to ask, 30/60/90
└── <company>/                 cp -r _TEMPLATE <company>
```

## Workflow

1. `cp -r _TEMPLATE <company>` (lowercase-kebab name, same as under `resumes/*/companies/`).
2. Fill `role-and-jd.md` first — it drives the tailored resume.
3. Build `company-research.md` and `interviewers.md` before the first real round.
4. Use `prep-notes.md` as your live scratchpad through the process.
5. Mirror status into `../tracking/`.

Related, kept separate on purpose: the **tailored resume** lives under `../resumes/<track>/companies/<company>/`; the **round schedule** lives in `../tracking/org-sheets/<company>.csv`.
