# Job criteria — Ishan Shah

Preferences that sit outside the resume: what makes a role worth applying to,
independent of whether the resume matches it. Drives the `criteria_weight` share
of the final match score (`[scoring]` in config.toml); resume fit is scored
separately and should not be re-judged here.

**Sections marked `TODO` are not yet decided.** Ignore them entirely when
scoring — do not guess a preference, and do not penalise a job for saying
nothing about an undecided criterion. Score only against the filled sections
below.

---

## Level and scope

- Target level is **VP of Engineering**, or **Director / Senior Director** with
  real org scope — multiple teams, through managers, owning roadmap, headcount
  and budget.
- **Head of Automation / Head of Platform / Head of DevOps** are equally on
  target where the title fits the scope better than a VP label.
- A **Senior Engineering Manager** role counts when the scope is broad (multiple
  teams, or a team plus a platform mandate). A single small team is too narrow.
- Roles reporting to a CTO, CEO or GM are preferred over ones buried three
  levels down.

## Workplace

- **On-site, hybrid and remote are all acceptable.** On-site 4+ days a week is
  explicitly fine and must never be treated as a negative.
- Bay Area is home (San Carlos, CA). Roles in SF / Peninsula / South Bay need no
  relocation and should not be marked down for being on-site.
- Fully remote roles are fine. Remote roles scoped to a **non-US** timezone are
  a poor fit.
- A role requiring relocation outside the Bay Area is a significant negative,
  though not an automatic veto.

## Domain

Deep, genuinely differentiating experience — treat a role centred on any of
these as a strong positive:

- **AI platforms and agent engineering** — agent runtimes, MCP servers, agent
  orchestration and governance, RAG/retrieval infrastructure, LLMOps.
- **Cloud infrastructure and platform engineering** — Kubernetes across
  GCP/AWS/Azure, developer platform, observability, SRE.
- **Regulated / safety-critical environments** — energy and industrial OT/SCADA,
  FDA-regulated medical devices, fintech, ISO 27001 / SOC 2 ownership. Most
  candidates at this level have none of this; it is a moat, not a footnote.
- **Developer productivity and automation** — CI/CD at scale, test platforms,
  merge queues, build systems.

<!-- TODO: domains to actively AVOID. Nothing is currently ruled out. If any
     sector is a hard no (e.g. crypto/Web3, defence, gambling, ad tech), add it
     here — and mark it **DEALBREAKER**: if it is an automatic veto rather than
     a soft penalty. Note a Web3 infrastructure role currently scores 82/100
     purely on resume fit, so if that is not wanted, this is the file that
     fixes it. -->

## Compensation

<!-- TODO: not yet decided. Add a base and/or total-comp floor, e.g.
       - Base below $250K is a significant negative
       - **DEALBREAKER**: total compensation below $200K
     Until a number is here, compensation is not scored at all — a posting's
     stated salary has no effect on the criteria score, and dealbreaker_cap
     (30.0 in config.toml) can never fire. -->

## Company stage and size

<!-- TODO: not yet decided. Add preferences such as Series B-D vs public,
     headcount range, or "no pre-seed". -->

---

## How to score against this file

- Judge only what the posting actually states. A posting that is silent on a
  criterion is neutral, not negative.
- Reward matches on level, scope, workplace and domain in that order.
- `**DEALBREAKER**:` items — there are currently none — cap the final score at
  `dealbreaker_cap`. Only an item carrying that exact marker is a dealbreaker;
  never promote a soft preference into one.
