# Ishan Shah

San Carlos, CA • +1-925-596-8956 • ishan.hash@gmail.com

**AI Platform & Agent Engineering Leader │ Multi-Agent Systems, RAG & MCP │ Multi-Model Gateways, Security & Enterprise LLM Rollout**

---

## Summary

AI platform and agent engineering leader with 15+ years building the platforms, agents, and infrastructure that let organizations adopt AI at scale. At CruxOCM I architected miniBOT — a Gemini-powered multi-agent assistant on FastAPI/Cloud Run — grounded by RAG over BigQuery vector embeddings on Vertex AI; built reusable MCP servers (a published open-source server plus Slack-native); and ran an org-wide Gemini Enterprise rollout with access and policy controls. My open-source UniClaw project is a governed multi-model gateway — OAuth2 authorization server, scoped JWTs, rate limiting, multi-model routing — on Python/FastAPI + React/TypeScript, the exact patterns this role's Gateway and Harness layers need. I own security and compliance end to end (ISO 27001, SOC 2), assess build-vs-buy across model providers and vendors, partner cross-functionally, and hire, mentor, and technically lead engineering teams.

## Experience

### CruxOCM Inc. — VP of Engineering / Head of Automation (reporting to the CTO) · Feb 2025 – Present

- **Multi-agent orchestration & RAG:** Architected miniBOT, a Gemini-powered multi-agent troubleshooting assistant (FastAPI on Cloud Run, driven from Slack) — an orchestrator routing to specialized agents for dashboards, log analysis, signal/hydraulic analysis, ticket lookup, and documentation Q&A — grounded by RAG over BigQuery vector embeddings on Vertex AI; plus TestBOT, a Gemini agent that auto-generates Robot Framework tests.
- **MCP servers & agent frameworks:** Built reusable MCP servers as action surfaces — a published open-source Lever MCP server and Slack-native MCP servers — plus agent configuration/skill conventions and prompt/skill lifecycle practices across the org.
- **Enterprise LLM rollout & vendor strategy:** Rolled out Gemini Enterprise across the org — access, policy, and integration with the full application suite — and assessed and standardized AI tooling and models (Claude, Cursor, GitHub Copilot) with build-vs-buy and vendor assessment.
- **Platform foundations:** Standardized Kubernetes control planes across GCP and Azure with GitOps governance and SLOs; 99.99% uptime; owned ~$2M cloud spend and vendor strategy with >$200K saved.
- **Observability & incident response:** Own platform observability on the Grafana LGTM stack (Loki/Grafana/Tempo/Mimir) and/or OpenObserve with PagerDuty — logs, metrics, traces, SLOs, and on-call/incident response.
- **Security, compliance & cross-org partnership:** Spearheaded ISO 27001 and SOC 2 programs (audit ownership) and partnered across engineering, security, and operations on shared standards for a safety-critical, regulated environment.
- **Team & technical leadership:** Hire, mentor, and technically lead a distributed engineering org (AI, platform, DevOps, infrastructure, security, quality); set architecture standards and review key decisions; partner with the CEO/CTO on roadmap and quarterly OKRs.

### Insulet Corporation (FDA-regulated medical devices) — Sr. Cloud Engineering Manager · Dec 2022 – Feb 2025

- Led cloud and data-product teams (25–30 engineers) across DevOps, developer productivity, and performance engineering; partnered with the VP of Engineering on multi-year roadmaps and quarterly OKRs.
- Owned end-to-end CI/CD with centralized policy and gating; operated highly available Jenkins on EKS/EFS (99.9% uptime) and cut deployment errors 15%.
- Built a performance and load-testing framework (Locust, Python) on EKS/AWS driving a 25% improvement in cloud architecture performance.
- Implemented SBOM generation and security automation across ~25 microservices in CI/CD, supporting security and regulatory requirements.

### Amazon (AWS Redshift) — Lead Systems Engineer · Dec 2016 – Dec 2022

- Owned the build, CI/CD, release ecosystem, and test tooling for Redshift — one of AWS's largest-scale distributed data services — including the CI/CD servers and fully automated build/deploy across all AWS-supported regions.
- Led the team that designed and shipped a Bors-style automated merge queue, gating integration on the exact merge candidate (not just the feature branch) — eliminating broken-mainline incidents and unblocking developer velocity org-wide.
- Added metrics-driven reporting on pipeline health and developer productivity, making bottlenecks visible and driving continuous improvement across the developer workflow.

### Prosper Marketplace (regulated fintech) — Lead DevOps Engineer · Jan 2015 – Dec 2016

- Rolled out org-wide CI/CD with Jenkins and containerization with Docker; managed microservice versioning (Artifactory) and static-analysis security scanning (SonarQube); ran a Hadoop/HDFS cluster on AWS (EMR).

### Pivotal Software — Member of Technical Staff · Sep 2011 – Jan 2015

- Managed CI infrastructure; migrated Perforce to Git; automated static analysis and code-coverage; built dynamic provisioning of Linux environments on AWS and vCloud.

## Open Source

### UniClaw · [github.com/uniclaw-labs/uniclaw](https://github.com/uniclaw-labs/uniclaw)

- Architected and shipped UniClaw, an open-source multi-model AI agent platform — a governed gateway that routes natural-language requests across three model backends (Anthropic API, local Ollama, zero-cost command mode) through a pluggable provider/tool registry (27+ integrations) with per-request auth, on a FastAPI (Python) backend and a React / TypeScript app.
- Built the security control plane: an OAuth2 authorization server with scoped JWTs, rate limiting, Fernet-encrypted secrets, constant-time token validation, and non-root containers — the auth, policy, and routing patterns an enterprise AI gateway requires.
- Delivered production-grade quality across a polyglot codebase (Python, TypeScript, Rust): 4,400+ automated tests, model-mode selection, and Dockerized multi-service orchestration.

## Education

- M.S., Software Engineering, San Jose State University (2011)
- B.E., Computer Engineering, Gujarat University (2009)

## Skills & Tools

- **AI Platform & Agent Engineering:** Multi-agent orchestration & agentic workflows; RAG/retrieval (Vertex AI, BigQuery embeddings); MCP servers & action surfaces (incl. published open-source MCP server); AI gateway patterns (centralized auth, scoped JWTs, rate limiting, multi-model routing); enterprise LLM rollout & administration (Gemini Enterprise); AI-assisted development (Cursor, Claude Code)
- **Providers & Stack:** Anthropic (Claude) & Google (Gemini, Vertex AI); multi-model routing; Python / FastAPI; React / TypeScript; pydantic; REST / API design
- **Platform & Infrastructure:** AWS, GCP, Azure; Kubernetes (GKE/EKS/AKS); Terraform; Docker; GitOps; observability (Grafana LGTM / OpenObserve, PagerDuty), SLOs & reliability (99.99%)
- **Security, Governance & Compliance:** OAuth2 / scoped JWTs; secrets encryption; ISO/IEC 27001 & SOC 2 (audit ownership); security partnering
- **Leadership & Strategy:** Hiring, mentoring & technically leading engineering teams; architecture standards & review; build-vs-buy & vendor assessment; cross-org partnership (Data, Apps, Product, Infosec); roadmaps & OKRs; executive communication
