# SentinelOne — Roles & JDs (TWO roles, ONE resume)

Two SentinelOne roles, served by **one shared resume on the VP track** (per request):

| # | Role | Dept | Resume |
|---|---|---|---|
| 1 | **Engineering Director, Developer Experience** | R&D | `resumes/vp-engineering/companies/sentinelone/Resume_VP_SentinelOne.md` (shared) |
| 2 | **Sr. Director, Enterprise AI Platform Engineering** | InfoSec & IT | `resumes/vp-engineering/companies/sentinelone/Resume_VP_SentinelOne.md` (shared) |

- **Track:** VP of Engineering for both. The shared resume bridges the two — AI platform / agents / MCP /
  multi-model gateway / Gemini (role 2) **and** AI-driven CI/CD / internal developer platform / developer
  productivity (role 1) — plus security/compliance and leadership common to both.

- **Location:** United States — Remote (both).
- **All claims fact-checked.** UPDATE: the **AI control plane now IN BUILD** legitimizes several capabilities as
  IN-PROGRESS (claimed as *being built*, not long-shipped): **model evaluation** (Langfuse evals), **MCP
  allow-listing** (egress allowlist + short-lived creds), **multi-model routing**, **LangGraph** supervisor, **HITL
  gate**, request **audit**, per-tenant **budgets**, and content **guardrails** — on GKE + Kuma (mTLS). This makes
  the resume a much closer match to the Gateway/Harness JD. STILL NOT claimed: **AWS Bedrock, OpenAI, Kong AI
  Gateway, pydantic.ai** by name, and **Go**.

---

## Role 1 — Engineering Director, Developer Experience (R&D)
- **Link:** https://www.sentinelone.com/jobs/?gh_jid=7775027003
- **Track:** VP of Engineering (shared resume). Positioned via the AI-driven-CI/CD + internal-developer-platform +
  developer-productivity bullets, which carry the DevEx weight for this role.
- **The DevEx org** (from SentinelOne's sibling Developer-Platform postings): partner with engineering teams to
  accelerate software-delivery velocity through innovation + standardization.
  - **Internal Developer Platform (IDP):** a "Golden Path" serving ~1,000 engineers — safe, fast PoC → production.
  - **AI-driven CI/CD:** pipelines where AI assists **code generation**, **auto-generates test suites**, and does
    **initial PR reviews** with contextual understanding.
  - **Infra & tooling:** modern deploys (Canary, Blue/Green); **ArgoCD, GitHub Actions**.
  - **Scale:** 15,000 enterprise clients, 9+ PB/day, 80+ Kubernetes clusters.
  - **Stack:** Go, Python, Kubernetes, Docker, AWS, GCP, GitHub Actions, ArgoCD, Kafka, REST/GraphQL/gRPC,
    Postgres/Mongo/Redis/ClickHouse, Prometheus/Thanos.
  - **Wants:** Go/Python + full SDLC; AWS/GCP + K8s; CI/CD + GitOps at scale; IaC (Terraform/Pulumi); SQL/NoSQL;
    cross-team influence; **passion for integrating LLMs & AI agents into developer workflows**; (Director level =
    lead the org, set strategy, mentor, partner cross-functionally).

### Role 1 — keyword / priority map
| Theme | Fit | Proof |
|---|---|---|
| **AI-driven CI/CD (AI code-gen, auto test-gen, AI PR review)** | ✅ bullseye | Cursor/Claude Code (code-gen); **TestBOT** auto-generates tests; Claude Code + Copilot automated PR review |
| Developer Experience / productivity leadership | ✅ strong | DevEx/dev-productivity charter; DORA; Bors-style merge queue (Amazon) |
| Internal Developer Platform / golden path / self-service | ✅ | Web-services platform from scratch; self-service ephemeral environments; K8s control plane |
| CI/CD + GitOps at scale | ✅ | GitHub Actions, Jenkins, Bazel monorepo, Gradle; GitOps governance; release gating |
| Kubernetes, AWS, GCP, Docker, Terraform | ✅ | K8s (GKE/EKS/AKS); AWS (Redshift/EKS); GCP; Docker; Terraform |
| Integrate LLMs & AI agents into dev workflows | ✅ bullseye | Production AI agents (GCP ADK), MCP servers; Gemini Enterprise; Cursor/Claude Code |
| Reduce friction / eliminate toil via automation | ✅ | Self-service infra + MCP/agents eliminating manual ops; automation frameworks |
| Cross-functional (Product, Security, Finance) | ✅ | CEO/CTO + cross-functional; budget/cost (Finance-adjacent); security/compliance |
| Leadership / mentorship / org strategy | ✅ | VP over multi-function org; Insulet 25–30 eng; Amazon team |
| **Go** | ❌ minor | Python/Bash yes; Go no |
| **ArgoCD / Prometheus / Thanos / Kafka / ClickHouse / Pulumi** by name | ⚠️ | GitOps (not ArgoCD by name); Grafana LGTM/Mimir (Prometheus-compatible); Terraform (not Pulumi) |
| Cybersecurity product domain | ⚠️ | Security/compliance depth (ISO/SOC2) but not a security-product builder |
| ~1,000-engineer / 80+-cluster scale | ⚠️ | Operated large-scale (Redshift org-wide; 25–30 direct) — bigger org scale is a stretch |

---

## Role 2 — Sr. Director, Enterprise AI Platform Engineering (InfoSec & IT)
- **Link:** https://www.sentinelone.com/jobs/?gh_jid=7782516003
- **Track:** VP of Engineering. **Comp:** $198,750–$298,000 base + RSUs + ESPP.
- **Mission:** Build the AI foundation every internal AI use case runs on — the control plane through which all AI
  activity is governed, observed, secured, and scaled (custom apps + vendor AI: Claude Enterprise, Gemini Enterprise).

### What you'll do
- Own the roadmap for the enterprise AI platform — **Gateway, Harness, and Semantic Layers** — direct-to-LLM → a
  governed, multi-model control plane.
- Build the **AI Gateway**: centralized identity & AuthN/Z, token budgeting, **DLP & content guardrails**,
  **multi-model routing & failover**, **MCP allow-listing**, full **audit trail** on every AI request.
- Build/operate the **Harness**: agent orchestration (**LangGraph or equivalent**), prompt/context management,
  memory & state, model abstraction across Anthropic/OpenAI/Google via **AWS Bedrock and Vertex**, MCP/tool wiring.
- Own the **Claude & Gemini Enterprise plugin framework**; partner with Infosec; govern all agents through one policy.
- Hire, mentor, technically lead; set standards; review architecture; communicate to executives.

### What they want
- Built ≥1 production platform enforcing centralized policy across consumers (auth/AuthN-Z, rate limiting,
  observability, audit). AI/LLM-gateway a bonus.
- Hands-on agent orchestration (**LangGraph or equivalent**); routing to **Bedrock/Vertex**; context/memory/tool-calling.
- Designed/implemented an **AI gateway** (auth, rate limiting, DLP, observability, audit). **Kong AI Gateway** a plus.
- Built/owned a **model evaluation framework**. Familiarity with **MCP** + governing tool access securely.
- Hands-on **Claude Enterprise & Gemini Enterprise** admin/policy. **Python 3.11+/FastAPI, React 18+/TS, pydantic.ai**.
- **Build/buy/assemble** evaluation; vendor/TCO. **7+ yrs SWE, 3+ yrs eng leadership, 1+ yr AI/ML infra in prod.**

### Role 2 — keyword / priority map
| JD theme | Do I have it? | Proof |
|---|---|---|
| Enterprise AI platform / control plane | ✅ strong | CruxOCM AI platform, agent runtimes, MCP frameworks |
| AI gateway (auth, routing, audit, guardrails) | ✅ (via UniClaw) | UniClaw: OAuth2 authz server, multi-model routing, scoped JWTs, rate limiting |
| Multi-model routing & failover | ✅ | UniClaw (Anthropic/Ollama/command); **model routing in the AI control plane gateway (in build)**; Vertex; Gemini |
| MCP familiarity & secure tool access | ✅ | Published open-source Lever MCP server; Slack-native MCP; agent/skill frameworks |
| Agent orchestration (LangGraph or equivalent) | ✅ | GCP ADK today; **LangGraph supervisor orchestrator in the AI control plane (in build)** — now LangGraph by name |
| Gemini Enterprise administration/policy | ✅ direct | Org-wide Gemini Enterprise rollout (access, policy, integration) |
| Python/FastAPI + React/TypeScript stack | ✅ direct | UniClaw: FastAPI (Python) + React/TypeScript |
| Build-vs-buy / vendor / TCO | ✅ | Evaluated & standardized AI tools/models; vendor mgmt |
| Security / governance / Infosec partnering | ✅ strong | ISO 27001 + SOC 2 (audit ownership); UniClaw security-first |
| Hire/mentor/lead; architecture; exec comms | ✅ | VP/HoA leading multi-domain org |
| **Model evaluation framework** | ✅ in build | **Langfuse evaluations** in the AI control plane (in build) — claim as in-progress |
| **MCP allow-listing** | ✅ in build | MCP backends with **egress allow-listing** + short-lived creds in the control plane (in build) |
| **AWS Bedrock / OpenAI / Kong / pydantic.ai** by name | ❌/⚠️ | Vertex+Anthropic+Google; not those named tools — don't claim (LangGraph IS now used — see above) |
| Claude Enterprise admin depth | ⚠️ | Strong on Gemini admin; Claude used org-wide, less admin depth — frame honestly |

## Gaps / stretch summary
- **Role 1 (DevEx Director):** bullseye on AI-driven CI/CD + developer productivity; gaps = Go, ArgoCD/Prometheus/
  Kafka/Pulumi by name, cybersecurity-product domain, ~1,000-eng org scale. Priority H.
- **Role 2 (AI Platform):** now an even stronger fit — the **AI control plane in build** (Agent Gateway, LangGraph
  supervisor, MCP allow-listing, multi-model routing, HITL, model evaluations, audit, budgets, guardrails on
  GKE/Kuma) maps almost 1:1 to the Gateway/Harness JD, framed as in-progress. Remaining named-tool gaps:
  Bedrock/OpenAI/Kong/pydantic.ai (not used); Claude Enterprise admin depth (frame honestly). Priority H.

## Tailoring checklist
- [x] ONE shared VP resume covering both roles — bridges AI platform/gateway/MCP/multi-model/Gemini (role 2)
      and AI-driven CI/CD / internal developer platform / developer productivity (role 1)
- [x] AI control plane (in build) surfaced — Gateway/LangGraph/MCP allow-listing/multi-model/HITL/model-eval as IN-PROGRESS
- [x] No fabricated claims — still NOT claimed: Bedrock, OpenAI, Kong, pydantic.ai by name, Go; control-plane items marked "in build"
- [x] PDF exported → resumes/vp-engineering/companies/sentinelone/
