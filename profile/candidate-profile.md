# Candidate Profile — Ishan Shah

Single source of truth for reusable facts, metrics, and narrative. **Edit a number here first**, then propagate to resume variants so nothing drifts.

## Identity

- **Name:** Ishan Shah
- **Location:** San Carlos, CA
- **Phone:** +1-925-596-8956
- **Email (resume):** ishan.hash@gmail.com
- **Current title:** VP of Engineering / Head of Automation, CruxOCM (reporting to CTO)
- **Targeting:** VP of Engineering / Head of Automation (AI platforms, agent engineering, platform/DevOps leadership)

## Headline metrics (reusable, keep exact)

| Metric | Value | Where it comes from |
|---|---|---|
| Experience | 15+ years | career total |
| Team budget owned | $2–3M annual | CruxOCM |
| Cloud spend owned | ~$2M (GCP + Azure) | CruxOCM |
| Cloud savings | >$200K | right-sizing + ephemeral infra |
| Platform uptime | 99.99% | CruxOCM K8s platform |
| Regression cycle | days → <12 hours | Robot Framework + AI test agent |
| Production agents shipped | 2 on GCP ADK | troubleshooting + test-authoring |
| Insulet team size | 25–30 engineers | Insulet |
| Insulet perf improvement | 25% | cloud architecture |
| Insulet deploy-error reduction | 15% | Jenkins on EKS |
| Amazon team led | 7 engineers | Redshift merge-gating system (Bors-style merge queue) |
| Microservices (SBOM) | ~25 | Insulet |

## Career timeline

| Company | Title | Dates |
|---|---|---|
| CruxOCM | VP of Engineering / Head of Automation | Feb 2025 – Present |
| Insulet (FDA-regulated med devices) | Sr. Cloud Engineering Manager | Dec 2022 – Feb 2025 |
| Amazon (AWS Redshift) | Lead Systems Engineer | Dec 2016 – Dec 2022 |
| Prosper Marketplace (regulated fintech) | Lead DevOps Engineer | Jan 2015 – Dec 2016 |
| Pivotal Software | Member of Technical Staff | Sep 2011 – Jan 2015 |

## Education

- M.S., Software Engineering, San Jose State University (2011)
- B.E., Computer Engineering, Gujarat University (2009)

## Signature projects (for stories & resume bullets)

- **miniBOT** — Gemini-powered multi-agent troubleshooting/support assistant (FastAPI on Cloud Run, driven from Slack); orchestrator + specialized agents (Grafana/InfluxDB dashboards, Kibana log analysis, signal-trend & hydraulic analysis, Zendesk ticket lookup, docs Q&A); **RAG over BigQuery vector embeddings** (documentation + support tickets); **Vertex AI** (Gemini 2.5 Flash for agents, Gemini 3 Pro for workbooks); auto-generates RFI workbooks. Safety-critical OT/SCADA pipeline context. ("94% reduction in manual ops" — unverified; see TODO.)
- **TestBOT** — Robot Framework + OPC UA test-automation platform with a **Gemini agent** (`google-genai`) that auto-generates Robot Framework test cases; cut manual regression from days to <12h.
- **UniClaw** ([github.com/uniclaw-labs/uniclaw](https://github.com/uniclaw-labs/uniclaw)) — open-source natural-language vehicle-control platform. Tauri v2 + **React 19 / TypeScript** desktop app on a **FastAPI (Python)** backend; AI agent with three modes (Claude Sonnet / local Gemma via Ollama / zero-cost command menu). **27 vehicle-brand provider adapters** via a pluggable registry; **12 messaging channels** + Alexa/Google Home; **OAuth2 + scoped JWTs**, Fernet-encrypted credentials, non-root containers; **4,400+ automated tests**; Docker Compose. Apache-2.0 / MIT. (Rust ~3% via Tauri.)
- **Lever MCP server** — published open-source MCP server (reusable action surface).
- **Gemini Enterprise rollout** — org-wide LLM access integrated with full app suite; hard part was tenancy/governance.
- **Slack-native MCP + ADK agents** — self-service ephemeral infra + automated cost governance.
- **Platform observability (CruxOCM)** — team owns observability on the **Grafana LGTM stack** (Loki, Grafana, Tempo, Mimir) and/or **OpenObserve**, with **PagerDuty** for alerting and on-call: logs, metrics, traces, dashboards, SLOs, and incident response. (Distinct from miniBOT's agentic access to pipeline Grafana/InfluxDB/Kibana signals.)
- **Forward-deployed delivery** — Fortune-50 energy customer pilot → expansion.
- **Redshift developer productivity (Amazon)** — owned the build/CI-CD/release ecosystem and test tooling for Redshift (CI/CD servers, fully automated multi-region build/deploy); led 7 engineers building a Bors-style automated merge queue that gated integration on the exact merge candidate (not just the feature branch); added metrics-driven reporting on pipeline health + developer productivity. Eliminated broken-mainline incidents; unblocked developer velocity org-wide.

## Domain / regulated-industry credentials

- Safety-critical energy operations (pipeline SCADA/OT)
- FDA-regulated medical devices (Insulet)
- ISO/IEC 27001 + SOC 2 (audit ownership)
- Regulated fintech (Prosper)

## Positioning one-liners

- "Fine-tuning changes how a model behaves; RAG changes what it knows; prompting is how you get 80% of the value before spending on either."
- "The question is never which model is best, it's which tier does this workload deserve — hybrid is almost always the real answer."
- "The model proposes, the system disposes." (agent safety design principle)

## Open questions / TODO for me

- [ ] Confirm exact "94% manual ops reduction" phrasing and source before quoting in interviews.
- [ ] Decide default track per target company (VP vs. HoA).
- [ ] Add compensation expectations / geographic constraints.
