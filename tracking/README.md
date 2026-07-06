# Tracking

Two-level tracking, CSV-based so it drops straight into Google Sheets / Drive.

```
tracking/
├── interview_tracker_master.csv     Parent sheet — one row per application (pipeline overview)
└── org-sheets/
    ├── _TEMPLATE_org_tracker.csv     Copy this per active company
    └── <company>.csv                 One row per interview round for that company
```

## Master sheet (`interview_tracker_master.csv`)

One row per company/application. Columns:

`Company, Role Title, Track (VP / HoA), Priority (H/M/L), Status, Source / Referral, Recruiter / Contact, Date Applied, Comp Range, Location / Remote, Resume Version Used, JD Link, Company Folder, Next Step, Next Date, Notes`

**Status values (suggested):** `Researching → Applied → Recruiter Screen → HM Screen → Onsite/Panel → Final → Offer → Accepted / Rejected / Withdrawn / On Hold`.

## Org sub-sheet (`org-sheets/<company>.csv`)

One row per interview round. Copy `_TEMPLATE_org_tracker.csv` to `<company>.csv` when a process becomes active. Columns:

`Round #, Stage, Date, Time (PT), Format, Interviewer, Title / Role, LinkedIn, Focus Area, Prep Status, Outcome, Feedback / Notes, Thank-You Sent`

## Connecting to Google Drive / Sheets

**Option A — manual (simplest):** Upload both CSVs to a Drive folder; open each with Google Sheets (right-click → Open with → Google Sheets). Re-import when you edit locally.

**Option B — one live workbook (recommended):** Create one Google Sheet named `Interview Tracker`. Make the first tab `Master` (import `interview_tracker_master.csv`), then add one tab per company (import each `org-sheets/<company>.csv`). This matches the "parent sheet + sub-sheet per org" model in one file. Link a master-sheet row to its tab with a hyperlink in the `Company` cell.

**Option C — automated sync:** This repo has Google Drive tools available in-session. Ask Claude to "push the tracking CSVs to my Drive folder X" and it can create/update the files for you.

## Keeping master ↔ org sheets in sync

When you add a round to an org sheet, update the master row's `Status` / `Next Step` / `Next Date`. The master is your at-a-glance pipeline; org sheets are the detail.
