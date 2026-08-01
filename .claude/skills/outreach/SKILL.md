---
name: outreach
description: Draft outreach to a named contact at a target company, or find who to contact. Use when Ishan asks for a LinkedIn note, InMail, recruiter message, referral ask, or application note. Drafts only — never sends.
---

# Outreach for one role

Codifies the pattern already in the nine `companies/*/outreach.md` files. A cold
application is a lottery ticket; an application with a warm note attached is a
conversation.

**Draft only. Never send anything, ever.** Output is text for Ishan to paste
after reading it.

---

## Step 1 — Find who to contact

If a contact isn't already known, produce **links for a human to open** — never
scrape, never automate a lookup, never use stored credentials:

```
https://www.linkedin.com/search/results/people/?keywords=<company>%20recruiter
https://www.linkedin.com/search/results/people/?keywords=<company>%20engineering%20manager
```

LinkedIn blocks automated profile lookups, and several existing files record
exactly that ("role not verified — LinkedIn blocks automated lookups"). **Say
what is unverified rather than guessing a title.** A message that works for
either a recruiter or a hiring leader is better than one addressed to the wrong
role with false confidence.

## Step 2 — Find the angle

This is the whole job, and it is the step most drafts skip.

Read `companies/<co>/role-and-jd.md` and find **the one requirement where Ishan
is not merely qualified but unusual**. Then state what the generic candidate
answer would be, and why his is different. From the Dealpath file:

> The JD is unusually insistent on AI-assisted development. Most candidates will
> answer that with "I use Cursor." Ishan rolled it out to an org and set the
> review discipline — that's the differentiator, so it leads.

Write that reasoning down in the file above the drafts. It is what makes the
message specific, and it is what you check the drafts against.

Good angles are usually: the regulated-industry moat, org-scale evidence
(headcount, budget, uptime), or a named system he built that maps onto what the
JD says it needs. Weak angles are enthusiasm, culture fit, and years of
experience.

## Step 3 — Write per-channel versions

Channels have hard limits and different context. Write the ones that apply,
**each in a fenced block, ready to paste**, with the character count in the
heading where a limit exists:

| Channel | Limit | Notes |
|---|---|---|
| LinkedIn connection note | **300 chars** | Count it. Put the count in the heading. |
| LinkedIn DM / InMail | ~120–150 words | Room for one concrete artifact |
| Application note (Wellfound, Greenhouse) | ~150–160 words | Resume is already attached — don't repeat it |
| Referral ask (someone known) | ~100 words | Ask for the intro, make it easy to forward |

**The versions are not the same text trimmed.** An application note is sent
*with* the resume, so "I'm reaching out rather than applying" is wrong there and
the background compresses to one line. A connection note has no attachment, so it
carries the hook alone. Note the difference in the file, as the existing files do.

## Step 4 — Check before handing it over

- Every claim traces to `profile/candidate-profile.md` (rule 3). Outreach is
  where overclaiming is most tempting and least recoverable.
- Location stated early and plainly when the role isn't local. Discovering it
  later "reads as either careless or evasive; leading with it reads as respectful
  of their time."
- Character counts actually counted, not estimated.
- Contact's name spelled as they spell it.
- No private third-party data beyond a public handle — no personal emails or
  phone numbers in a committed file.

## Step 5 — Record

Save to `companies/<co>/outreach.md`. Note in
`tracking/interview_tracker_master.csv` when it is **sent** — not when drafted.

Nine drafted, unsent outreach messages are currently sitting in this repo. A
draft is not outreach.

---

## Follow-up policy

Recorded here so it exists before there is anything to follow up on:

- **Max two follow-ups** per application, then stop.
- First follow-up no earlier than **10 days** after `Date Applied`.
- 60–120 words. Add one new, relevant fact — never just "checking in".
- **Never a claim that wasn't in the submitted materials.**
- Draft only; Ishan sends.
- A short thank-you after each completed interview stage is separate from this
  cap and always appropriate.
