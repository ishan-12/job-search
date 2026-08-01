# Plaid — Outreach to Ellen D

Role: **Engineering Manager, AI Applications** · SF HQ · team of 4 · **$216,000–$367,200** + equity
Contact: **Ellen D. — Senior Technical Recruiter @ Plaid** (LinkedIn `ellen-d-569375b6`, she/her), started
April 2026. Four years at Lyft before that recruiting Product Management, Mobile, **Infra**, **Engineering
Managers** and Data across US/Canada; four years at Happy Money before that. **FinTech** is one of her
three listed top skills. Certifications include "Recruiting for the Future: AI Talent Tactics", and her
Lyft tooling list included Claude and Gemini — she is AI-literate, so the AI content lands without
translation.

*(Her profile is not reachable programmatically — public web 404s, and Composio's LinkedIn toolkit returns
403 on third-party lookup. Details confirmed from a manually exported profile PDF, Jul 30 2026.)*

**Strategy — driven by the JD, bullet by bullet.** Every line in the message maps to a stated requirement or
responsibility; nothing is shaped around the reader's preferences. Order follows what they weight: the
Staff-IC-before-management must-have first (it is the most specific and most checkable), then LLM product work
shipped to real users, then the two responsibilities almost nobody has built — MCP integration patterns and
trust infrastructure for agentic commerce — then 0→1, then privacy/compliance.

**The message states only what has been done.** It does not volunteer gaps. That is a different thing from
claiming them — the do-not-claim list below still stands, and applies to conversation as much as to writing. Most EM candidates applying to an AI role can talk about prompts
and RAG. Very few have shipped **MCP servers in production** or built **trust infrastructure for agents** —
and those are two of Plaid's own listed responsibilities, including "build trust infrastructure for agentic
commerce." Those go first, before the general AI credentials.

Then the **Staff-IC → manager arc**, because the JD calls it out explicitly ("8+ years… that includes time as
a Staff-level engineer before transitioning into management") and Ishan matches it cleanly.

**Do not claim:** fine-tuning, training or serving self-hosted ML models, user research as a practice,
consumer conversational product experience, or payments/banking-data domain depth.

---

## Message (~250 words, resume attached)

```
Hi Ellen,

I'm applying for the Engineering Manager, AI Applications role. Mapping to what you've asked for:

• Staff-level IC before management — a decade as a Lead/Staff engineer owning AWS Redshift's build, CI/CD and release ecosystem across every AWS region, leading a team of 7 there. Then into management: 25-30 engineers across cloud and data-product teams at Insulet, and today I run engineering at CruxOCM.

• LLM products shipped and iterated with real users — a multi-agent assistant in daily use by operations teams: an orchestrator routing to specialist agents by evidence domain, RAG and semantic search over vector embeddings for grounding, prompt and context design throughout, and model tiering chosen by what each workload deserves.

• Two things from your JD I've already built. MCP servers as governed integrations — each backend registers a declared tool surface, egress allowlist and short-lived credentials. And trust infrastructure for agents: a gateway doing authn/authz, guardrails and agent/tool registration, a LangGraph supervisor with a human-in-the-loop approval gate, per-tenant budgets, and Langfuse in-cluster for traces, cost attribution and evaluations. That's your "trust infrastructure for agentic commerce" line, running in production today.

• 0-to-1 — architected a commercial multi-tenant B2B SaaS AI platform from concept to production, now sold to external customers. Outside work I maintain an open-source agent platform and publish an open-source MCP server.

• Privacy and compliance — ISO 27001 and SOC 2 through third-party audit, and regulated fintech at Prosper Marketplace.

Resume attached — happy to talk whenever works for you.

Ishan Shah
ishan.hash@gmail.com · +1-925-596-8956 · San Carlos, CA
```

---

## Notes before sending

- **Keep the two systems separate. They are not the same thing.**
  - *The operations assistant* — orchestrator + specialist agents, RAG/semantic search, prompt and context
    design, model tiering. Runs on Cloud Run. **No Langfuse.**
  - *The AI control plane* — gateway (authn/authz, guardrails, registration, routing, budgets, audit),
    LangGraph supervisor, human-in-the-loop gate, **Langfuse** for traces/cost/evaluations. Runs on GKE.
  - An earlier draft attached Langfuse to the assistant. That would not have survived "walk me through the
    eval set for that assistant." Corrected.

- **Role confirmed: recruiter**, so the message is already in requirement-list form. No further trimming needed.
- **She came from Happy Money and lists FinTech as a top skill** — the Prosper Marketplace line is real
  common ground and is deliberately kept in. Don't reference her background directly; just let it land.
- **Comp is strong** ($216–367K + equity) and the band is wide, which usually means level is negotiable.
- **Expect "why a team of 4?"** He currently runs a multi-function org. The honest answer is depth over
  span — this is the exact problem space he's been building in, and the band suggests Plaid is paying for
  depth too.
- **The one stated must-have he genuinely lacks is user research** — *"Ability to deeply understand customer
  and user needs through user research and rapid experimentation — be your own technical PM."* Not volunteered
  in the message, but **expect it in the first call.** Honest answer: the agents were built from watching how
  operators actually worked and iterating with them, and he sets roadmap directly with the CEO and CTO — but
  formal user research is not his background. Do not invent it.
- **Fine-tuning is only an example, not a requirement.** The JD says *"including but not limited to: Prompt
  engineering, Fine-tuning, RAG…"* — a non-exhaustive list. It appears separately as a nice-to-have. Earlier
  drafts conceded it unprompted; that was over-conceding and it's now out.
- **Also in that list and not claimable: Streaming and SSE**, and *"common UX and design patterns for
  GenAI-powered products."* Don't raise them; don't claim them if asked.
- Resume: `resumes/vp-engineering/companies/plaid/Resume_Ishan_Shah.pdf`
