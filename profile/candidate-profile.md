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
- **IAH platform (CruxOCM)** — a commercial, **multi-tenant B2B SaaS AI platform**, architected 0→1 (concept → production) and **sold to external business customers**; hosted (multi-tenant) on CruxOCM's own ecosystem across **Azure + GCP**. It's the cloud-native substrate on which customers run **governed, agent-based AI workloads at scale** — built on the AI control plane (agent gateway, multi-model routing, orchestration, tool/MCP governance, and end-to-end observability). (Resume framing: describe at the *platform* level — do NOT enumerate individual services like RFI/Trainer/TestBOT; those are internal components, not the pitch.) **Hosted SaaS model** — runs on our ecosystem rather than deploying AI into customers' own environments. (Supersedes the earlier inaccurate "forward-deployed Fortune-50" framing.) → real **0→1 B2B SaaS** proof.
- **AI Control Plane (CruxOCM)** — a production-hardened AI control plane on **GKE** with a **Kuma service mesh** (in-mesh **mTLS** everywhere; GKE cluster boundary). Components:
  - **Agent Gateway** — single URL for `/agents/*` and `/mcp/*`: **AuthN**, **AuthZ**, **guardrails**, agent + MCP **registration**, **path routing**, **model routing**, per-tenant **budgets**, and **gateway audit**.
  - **Control layer** — a **LangGraph supervisor orchestrator** doing intent routing to specialist agents, a **memory store**, and a **human-in-the-loop (HITL) approval gate**; optional operator UI (dashboard, approvals, config & policies).
  - **Execute/tools** — specialist agents + **MCP backends** (ephemeral, InfluxDB, Grafana, signal-editor/composer, HMI, project-config, CI/CD, TestBOT), each **registered** with an **egress allowlist** and **short-lived credentials**.
  - **Observe** — **Langfuse** in-cluster: prompts, traces, tokens, **cost**, **evaluations**, datasets.
  - NOTE: this covers capabilities previously flagged as not-done and now real/delivered: MCP allow-listing (egress allowlist), multi-model (model routing), model eval (Langfuse evaluations), monitoring (Langfuse), HITL gate, LangGraph — claimable as delivered.
- **Serverless / event-driven experience (cross-company)** — *(added Jul 28, 2026)*
  - **CruxOCM (GCP):** **Cloud Run v2** in production, provisioned as code in `crux-tf-infra` (Terraform + Terragrunt, YAML-config-driven, GCP + Azure, ~17 project environments across dev/qa/uat/prod/iac). miniBOT runs as a Cloud Run **service** (`slack-agent-bot`: scale-to-zero/min-instances, concurrency caps, VPC access with egress control, Secret Manager–backed env, dedicated per-workload service accounts) plus Cloud Run **jobs** for async/batch work (`minibot-pipeline`, `kb-sync-manager` 24h timeout, `zendesk-bq-sync`); the service **dispatches long-running work to an async job** (RFI workbook generation) rather than holding a request open.
  - **Insulet (AWS):** the service estate ran **serverless** — **ECS** for services and **AWS Lambda** for event-driven / short-lived jobs.
  - **Framing:** claim serverless/event-driven architecture broadly (Cloud Run ≈ Lambda-class managed compute; same cold-start, concurrency, timeout, IAM-per-workload, and idempotency questions). Do **not** claim deep Lambda/Step Functions specialization.
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
