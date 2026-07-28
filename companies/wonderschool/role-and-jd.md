# Wonderschool — Head of AI Agent Systems

- **Resume:** `resumes/head-of-automation/companies/wonderschool/Resume_HeadOfAutomation_Wonderschool.md` (HoA track, hands-on-tuned)
- **Track:** Head of Automation, tuned **hands-on** — leads with multi-agent systems build/architecture + evaluation
  + reliability, not org-leadership (the JD explicitly says "not a traditional Head of Engineering").
- **Link:** https://job-boards.greenhouse.io/wonderschool/jobs/7710092003
- **Comp:** not specified. **Location:** San Francisco — **in-person 5–6 days/week** (Rincon Hill). Reports to CEO.
- **Company:** Wonderschool — Series B (a16z, Goldman), cash-flow positive; software for service businesses
  (childcare); deploying AI agents across product, ops, and support.

## ⚠️ Level / logistics notes
- **Hands-on + small team** (lead 2–3 engineers incl DevOps; direct codebase involvement). Explicitly **NOT** a
  traditional Head of Engineering, NOT large-team management, NOT research. Ishan is a VP/Head — this is a more
  hands-on, smaller-scope builder-leader role (deeply in his AI-agent wheelhouse). Decide if that suits.
- **5–6 days/week in-person in SF** — demanding commute from San Carlos; confirm willingness.

## The Role (from the JD)

Own the design and performance of Wonderschool's **multi-agent system** — transform a partially functional agent
platform into **production-grade infrastructure** tied to revenue (acquisition, onboarding, operations). Hands-on
while leading a small team.

**Responsibilities (condensed):**
- **Multi-agent architecture & performance** — own the system (OpenClaw, Claude Code, internal tools); fix
  coordination failures, memory loss, context limitations; raise output quality (minimize human correction).
- **Evaluation systems** — measure success rates, failure modes, task completion, human intervention; feedback loops.
- **Reliable execution** — validation layers, retry logic, agent-to-agent coordination, end-to-end reliability.
- **Company-wide adoption** — enable eng/product/design/ops to use agents; define standards; non-engineer usability.
- **Revenue/business impact** — tie agent metrics to outcomes; conversion, onboarding, provider revenue, cost
  automation, fraud/compliance.
- **Team** — lead 2–3 engineers; hire/develop agent-systems engineers; balance hands-on with leadership.

**Required:** strong engineering + production systems; AI/LLMs/automation in real environments; debugging complex
systems & improving reliability; direct code + architecture; fast-paced high-ownership.
**Preferred:** multi-agent systems; workflow automation / internal platform; regulated/compliance-heavy; founder/
early-stage startup engineer.

## My read — keyword / priority map

| Theme | Fit | Proof |
|---|---|---|
| **Multi-agent system architecture** (coordination, memory, context) | ✅ bullseye | AI control plane: LangGraph supervisor orchestration, memory store, agent-to-agent routing; miniBOT multi-agent |
| Partially-functional → **production-grade** hardening | ✅ | Production-hardened AI control plane on GKE/Kuma; reliability engineering |
| **Evaluation systems** (success rates, failure modes, feedback loops) | ✅ bullseye | Langfuse model evaluations, traces, cost; DORA/metrics; feedback loops |
| **Reliable execution** (validation, retry, reliability) | ✅ | HITL/guardrails, retry/validation patterns; 99.99%; blameless RCA |
| Agent output quality / minimize human correction | ✅ | Guardrails + HITL approval gate; TestBOT auto-generated tests |
| **Company-wide agent adoption + standards + non-engineer usability** | ✅ | Gemini Enterprise rollout org-wide; standardized Claude Code/Cursor; Slack-native agents; agent frameworks |
| **Claude Code** (named) | ✅ | Standardized Claude Code across the org |
| Hands-on in code + lead small team + hire | ✅ | Hands-on Python/FastAPI; hire/mentor engineers incl DevOps |
| Business/revenue impact; cost automation; compliance | ✅ (partial) | IAH B2B SaaS (revenue); AI→cost automation (>$200K); ISO/SOC2; **fraud detection not done** |
| Regulated/compliance-heavy (preferred) | ✅ | ISO 27001/SOC 2; FDA medical; energy OT; fintech |
| Workflow automation / internal platform (preferred) | ✅ | Automation frameworks; internal developer platform; MCP |
| **Founder / early-stage startup engineer** (preferred) | ⚠️ | CruxOCM startup (VP), Prosper/Pivotal growth-stage — not a founder |
| **Direct revenue-conversion/onboarding agents; fraud detection** | ⚠️ | Ties AI to productivity/cost + platform revenue (IAH); not sales-conversion agents or fraud detection specifically |

## Gaps / stretch areas
- **Content bullseye** — multi-agent systems, evaluation, reliability, adoption, Claude Code, hands-on + small team,
  regulated — all his exact recent work (control plane + agents + Langfuse evals + UniClaw).
- **Honest softer spots (not overclaimed):** founder background (startup VP, not founder); direct revenue-conversion/
  onboarding agents and fraud detection (frames as tying agent metrics to business outcomes + cost automation).
- **The real considerations are level (hands-on/small-team) and location (SF 5–6 days in-person)** — see notes.
- Priority H (fit); decide on hands-on level + onsite.

## Tailoring checklist
- [x] HoA track, hands-on-tuned — leads with multi-agent systems + evaluation + reliability + adoption
- [x] AI control plane (orchestration/memory/guardrails/HITL) + Langfuse evals + Claude Code surfaced; UniClaw foregrounded
- [x] Founder gap, revenue-conversion/fraud not overclaimed; level + onsite flagged
- [x] PDF exported → resumes/head-of-automation/companies/wonderschool/
