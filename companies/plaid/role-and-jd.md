# Plaid — Role & JD

- **Title:** Engineering Manager, AI Applications
- **Team:** AI Applications — **team of 4 engineers**, mixed experience levels
- **Track to use:** VP of Engineering base (it carries the AI-agent framing), retitled for an EM role
- **Location:** San Francisco HQ
- **Comp:** **$216,000 – $367,200** + equity and/or commission
- **JD link:** https://plaid.com/careers/openings/engineering/san-francisco-hq/engineering-manager-ai-applications/
- **Captured:** Jul 29, 2026

## What the team does

- Define long-term strategy and drive execution with technical and product leadership
- Scale business relationships with major **AI customers and partners**, starting with personal finance apps
- **Develop integration patterns for Plaid with AI providers, including MCP Servers**
- Redesign consumer Link experiences for **conversational interfaces**
- **Build trust infrastructure for agentic commerce**
- Enhance the existing **customer support AI agent with multi-turn, multi-agent capabilities**
- Expand agentic systems into customer onboarding, product recommendations, upselling

## Requirements

**Must have**
- 8+ years industry experience, **including time as a Staff-level engineer before moving into management**
- 1+ years engineering management
- Hands-on LLM product development: **prompt engineering, fine-tuning, RAG, semantic search, agent orchestration, evaluation frameworks, GenAI UX patterns**
- User research and rapid experimentation
- Track record building high-performing engineering teams
- Exploratory *and* convergent thinking for 0→1
- Demonstrated passion for GenAI applications

**Nice to have**
- Training/serving ML models in production, or fine-tuning domain-specific LLMs
- Comfort in privacy-sensitive environments with compliance knowledge

## My read — the best-matched role in the pipeline

Four of their responsibilities are things Ishan has already shipped, and two of them are rare.

| Their ask | Fit | Proof |
|---|---|---|
| **Integration patterns with AI providers, including MCP Servers** | ✅ **rare bullseye** | Publishes an open-source **Lever MCP server**; built chat-native MCP servers; MCP backends registered in the control plane with egress allowlists and short-lived credentials; MCP tool governance. Very few EM candidates have shipped MCP in production |
| **Trust infrastructure for agentic commerce** | ✅ **rare bullseye** | The AI control plane *is* trust infrastructure for agents: authn/authz, guardrails, agent + tool registration, per-tenant budgets, egress allowlists, short-lived credentials, human-in-the-loop approval gate, full audit |
| **Customer support AI agent → multi-turn, multi-agent** | ✅ **direct** | Shipped exactly this: an orchestrator routing to specialist agents across telemetry, logs, signal analysis, ticket history and RAG-grounded docs, driven from chat, terminating in a generated deliverable |
| Agent orchestration | ✅ | LangGraph supervisor orchestrator with memory store and intent routing |
| Evaluation frameworks | ✅ | Langfuse in-cluster — traces, tokens, cost, evaluations, datasets |
| RAG + semantic search | ✅ | RAG over BigQuery vector embeddings of documentation and ticket history on Vertex AI |
| Prompt engineering | ✅ | Grounding context builders, anti-hallucination prompting, org-wide prompt/skill conventions |
| **Staff-level IC before management** | ✅ **matches the arc exactly** | Lead Systems Engineer at AWS (Redshift build/CI-CD/release, led 7), Lead DevOps at Prosper, MTS at Pivotal → then management at Insulet and CruxOCM |
| 1+ yr engineering management | ✅ | ~3.6 yrs formal; 25–30 engineers at Insulet |
| Building high-performing teams | ✅ | Hiring, coaching, performance across multiple orgs |
| 0→1, exploratory and convergent | ✅ | Commercial B2B SaaS AI platform 0→1, sold to external customers |
| **Privacy-sensitive + compliance** (nice-to-have) | ✅ **strong** | ISO 27001 + SOC 2 audit ownership, FDA-regulated medical devices, regulated fintech at Prosper |
| Passion for GenAI | ✅ | Open-source agent platform, MCP server, production agents |
| **Fine-tuning** | ❌ | Has a clear POV ("fine-tuning changes how a model behaves; RAG changes what it knows") but **no evidence of having fine-tuned a model.** Do not claim |
| **Training / serving ML models in production** | ❌ | Serves hosted LLMs; does not train or serve own models. Nice-to-have only |
| **User research** | ❌ | Not documented. Real gap against a stated must-have |
| **GenAI UX patterns** | ⚠️ partial | Chat-native agents, an operator UI, and UniClaw's three model modes including a **zero-cost command menu** — a genuine GenAI UX decision. But no consumer-facing conversational product |
| Consumer conversational experiences (Link redesign) | ⚠️ | Interfaces built for operators and engineers, not consumers |
| Fintech domain | ✅ adjacent | Prosper Marketplace (regulated fintech). Not banking-data or payments at Plaid's scale |

## Strategy

Lead with the two rare hits — **MCP integration patterns** and **trust infrastructure for agents** — because
almost nobody applying to an EM role has shipped either in production. Then the multi-agent support agent,
which is the JD's own example. Then the Staff-IC→manager arc, which they call out explicitly and which he
matches cleanly.

De-emphasize infrastructure craft. This is an **AI product** team; frame the control plane as *what makes
agents safe to put in front of customers*, not as a Kubernetes achievement.

## Gaps — do not claim

- Fine-tuning any model
- Training or serving self-hosted ML models
- User research as a practice
- Consumer product or consumer conversational UX
- Payments / banking-data domain depth

## Notes

- **Team of 4.** Smaller than anything he currently runs — the "why this scope" question will come up, and
  the comp ($216–367K) suggests they're paying for depth rather than span.
- SF HQ — commutable from San Carlos; on-site expectations not stated in the posting.
