# SentinelOne — Role & JD

- **Title:** Sr. Director, Enterprise AI Platform Engineering (InfoSec & IT)
- **Track to use:** VP of Engineering (Sr. Director / exec-level AI platform leadership)
- **JD link:** https://www.sentinelone.com/jobs/?gh_jid=7782516003
- **Comp range (if known):** $198,750–$298,000 base + RSUs + ESPP + benefits
- **Location / remote:** United States — Remote

## Full JD (captured via Greenhouse API)

**Mission:** Build the AI foundation every internal AI use case runs on — the control plane through which
all AI activity at SentinelOne is governed, observed, secured, and scaled, serving both custom-built AI
apps and vendor AI (Claude Enterprise, Gemini Enterprise).

### What you'll do
- Own the roadmap for the enterprise AI platform — **Gateway, Harness, and Semantic Layers** — moving from direct-to-LLM to a governed, multi-model control plane.
- Build the **AI Gateway**: centralized identity & AuthN/Z, token budgeting, **DLP & content guardrails**, **multi-model routing & failover**, **MCP allow-listing**, and a full **audit trail** on every AI request.
- Build/operate the **Harness**: agent orchestration (**LangGraph or equivalent**), prompt/context management, memory & state, model abstraction across Anthropic/OpenAI/Google via **AWS Bedrock and Vertex**, MCP/tool wiring.
- Own the **Claude & Gemini Enterprise plugin framework** — role-based skills/agents; secure authoring, testing, deployment; output quality/reliability.
- Partner with Enterprise Data, Apps, Product Dev, and **Infosec**; shared architectural contracts.
- Govern how all agents (user-instantiated, engineered, SaaS-embedded, external) pass the same policy controls.
- Hire, mentor, technically lead engineers; set standards; review architecture; communicate to executives.

### What they want
- Built ≥1 production platform enforcing centralized policy across consumers (auth/AuthN-Z, rate limiting, observability, audit). AI/LLM-gateway a bonus; API/data/developer-platform backgrounds welcome.
- Hands-on agent orchestration (**LangGraph or equivalent**); routing to **Bedrock/Vertex**; real grasp of context windows/memory/tool-calling.
- Designed/implemented an **AI gateway** (auth, rate limiting, DLP, observability, audit across providers). **Kong AI Gateway** a plus.
- Built/owned a **model evaluation framework** — closing the loop to drive model selection, prompt tuning, routing.
- Familiarity with **MCP** and governing tool access securely.
- Hands-on with **Claude Enterprise & Gemini Enterprise** administration/policy.
- Strong SWE background; **Python 3.11+ / FastAPI, React 18+ / TypeScript, pydantic.ai** stack.
- Cross-org collaboration; shared architectural contracts.
- **Build/buy/assemble** evaluation; vendor assessment; TCO; don't over-engineer.
- **7+ yrs SWE, 3+ yrs eng leadership, 1+ yr leading a team building AI/ML infra in production enterprise.**

## My read — keyword & priority map

| JD theme / keyword | Do I have it? | Proof |
|---|---|---|
| Enterprise AI platform / control plane | ✅ strong | CruxOCM AI platform, agent runtimes, MCP frameworks |
| MCP governance / allow-listing / tool access | ✅ strong | Published open-source Lever MCP server; Slack-native MCP; agent/skill frameworks |
| AI gateway (auth, routing, audit, guardrails) | ✅ (via UniClaw) | UniClaw: OAuth2 authz server, multi-model routing, scoped JWTs, audit — plus platform auth/observability |
| Multi-model routing (Anthropic/Google) | ✅ | UniClaw (Anthropic/Ollama/command); Vertex AI; Gemini Enterprise |
| Agent orchestration (LangGraph or equivalent) | ✅ equivalent | GCP ADK multi-agent orchestration (LangGraph not by name) |
| Model evaluation framework (closed loop) | ✅ | eval + monitoring in runtime (quality/cost/impact) driving model/prompt decisions |
| Gemini Enterprise administration/policy | ✅ direct | Org-wide Gemini Enterprise rollout (access, policy, integration) |
| Claude (enterprise) usage | ✅ partial | Standardized Claude/Claude Code org-wide (admin depth less than Gemini) |
| Python/FastAPI + React/TypeScript stack | ✅ direct (UniClaw) | UniClaw: FastAPI (Python) + React/TypeScript |
| Build-vs-buy / vendor / TCO | ✅ | Evaluated & standardized AI tools/models; vendor mgmt; ~$2M cloud + savings |
| Security / governance / Infosec partnering | ✅ strong | ISO 27001 + SOC 2 (audit ownership); safety-critical; UniClaw security-first |
| Cross-org partnership / shared contracts | ✅ | CEO/CTO + cross-functional; org-wide standards |
| Hire/mentor/lead; architecture review; exec comms | ✅ | VP/HoA leading multi-domain org |
| 7+ SWE / 3+ leadership / 1+ AI-infra team | ✅ | 15+ yrs; VP/HoA leading AI platform |
| AWS Bedrock | ❌ gap | Uses Vertex + Anthropic; not Bedrock — don't claim |
| OpenAI models | ❌ gap | Uses Anthropic/Google; not OpenAI — don't claim |
| LangGraph (specifically) | ⚠️ | Orchestration via ADK; not LangGraph by name |
| Kong AI Gateway / pydantic.ai (specifically) | ⚠️/❌ | "plus" items; FastAPI/pydantic yes, not Kong or pydantic.ai by name |

## Gaps / stretch areas
- **Name-level gaps, not competency gaps:** AWS Bedrock, OpenAI, LangGraph, Kong AI Gateway, pydantic.ai. Underlying skills (multi-model routing, agent orchestration, AI gateway auth/audit, FastAPI/pydantic) are all present via Vertex/Anthropic/Google, ADK, and UniClaw — lead with those; don't claim the specific named tools.
- **Claude Enterprise admin:** strong on Gemini Enterprise admin; Claude used org-wide but less admin depth — frame honestly.
- Overall: this is a **genuine strong fit** (not a stretch) — priority H.

## Tailoring checklist
- [x] Summary leads with control plane / AI gateway / MCP governance / multi-model + evaluation
- [x] UniClaw tailored as a governed multi-model AI gateway on the exact stack (FastAPI/React/TS)
- [x] Gemini Enterprise rollout + build-vs-buy + security/compliance surfaced
- [x] Named-tool gaps (Bedrock/OpenAI/LangGraph/Kong/pydantic.ai) not overclaimed
- [x] PDF exported → ../../resumes/vp-engineering/companies/sentinelone/
