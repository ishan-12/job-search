# Ishan Shah

San Carlos, CA • +1-925-596-8956 • ishan.hash@gmail.com

**Engineering Leader │ AI-Native Product Engineering & Multi-Tenant SaaS Platforms │ Agentic AI Control Planes, LLM/GenAI Integration, Cloud & Security (SOC 2)**

---

## Summary

Engineering leader with 15+ years leading engineering strategy, architecture, and delivery — and building AI-native, multi-tenant products. I architected IAH from concept to production (0→1) — a commercial, multi-tenant B2B SaaS AI platform on Azure and GCP, sold to external business customers, on which they run governed, agent-based AI workloads at scale. That platform runs on an AI control plane I architected and operate — an Agent Gateway providing AuthN/AuthZ, guardrails, model routing, per-tenant budgets and audit; a LangGraph supervisor orchestrator with a memory store and a human-in-the-loop approval gate; and Langfuse evaluations, cost and trace observability. I integrate AI/ML, LLMs, and GenAI directly into production applications, including multi-agent assistants grounded by RAG on Vertex AI, on a Python/FastAPI stack. I build and scale high-performing engineering teams across onshore and offshore, own architecture and technical roadmaps, and establish the best practices that keep delivery fast and safe: CI/CD, testing, observability, and security across AWS, GCP, and Azure with Kubernetes, Docker, and Terraform. I own ISO 27001 and SOC 2 (audit ownership), partner closely with Product on quality releases, and thrive in high-growth startups.

## Experience

### CruxOCM Inc. — VP of Engineering / Head of Automation (reporting to the CTO) · Feb 2025 – Present

- **Engineering leadership & roadmap:** Lead engineering strategy, architecture, and the technical roadmap for a distributed org spanning platform, AI, DevOps, infrastructure, security, and quality; build and scale high-performing teams (onshore and offshore), partner with Product on timely, quality releases, and manage stakeholders across the C-suite.
- **AI/ML & LLM integration into products:** Integrate AI/ML, LLMs, and GenAI into production — miniBOT, a Gemini multi-agent assistant grounded by RAG over BigQuery vector embeddings on Vertex AI; TestBOT, which auto-generates tests; reusable MCP servers; and an org-wide Gemini Enterprise rollout.
- **AI control plane — governed agents in a multi-tenant product:** Architected and operate a production-hardened AI control plane on GKE with a Kuma service mesh (mTLS everywhere) — an Agent Gateway (single URL for /agents/* and /mcp/*) with AuthN/AuthZ, guardrails, agent and MCP registration, path and model routing, **per-tenant budgets**, and gateway audit; a **LangGraph** supervisor orchestrator doing intent routing to specialist agents, with a memory store and a **human-in-the-loop approval gate** for actions requiring sign-off; MCP backends registered with egress allow-listing and short-lived credentials; and **Langfuse** observability across prompts, traces, tokens, cost, and evaluations.
- **Multi-tenant B2B SaaS platform (IAH), 0→1:** Architected and shipped IAH from concept to production — a secure, scalable, commercial multi-tenant B2B SaaS AI platform on Azure and GCP, **sold to external business customers**, providing the cloud-native substrate on which they run governed, agent-based AI workloads at scale.
- **Cloud, Kubernetes & best practices:** Standardized Kubernetes across GCP and Azure with Docker, Terraform (IaC), and GitOps; established engineering best practices — CI/CD (GitHub Actions, Jenkins, Bazel monorepo, Gradle), testing, and observability (Grafana LGTM / OpenObserve, PagerDuty) at 99.99% reliability.
- **Security & compliance:** Spearheaded ISO 27001 and SOC 2 programs (audit ownership) with SBOM and static-analysis scanning and access-control standards; own ~$2M cloud spend with >$200K saved.
- **Stack:** Python / FastAPI, PostgreSQL, REST APIs, and distributed systems across the platform.

### Insulet Corporation (FDA-regulated medical devices) — Sr. Cloud Engineering Manager · Dec 2022 – Feb 2025

- Led cloud and data-product teams (25–30 engineers) across DevOps, developer productivity, and performance engineering; partnered with the VP of Engineering on multi-year roadmaps and quarterly OKRs.
- Built a performance and load-testing framework (Locust, Python) on EKS/AWS (25% improvement); operated highly available Jenkins on EKS/EFS (99.9% uptime) and cut deployment errors 15%.
- Owned end-to-end CI/CD with gating and one-button deploy (Jenkins, Python, Gradle); implemented SBOM generation and regulated change control for data integrity and supply-chain security.

### Amazon (AWS Redshift) — Lead Systems Engineer · Dec 2016 – Dec 2022

- Owned the build, CI/CD, release ecosystem, and test tooling for Redshift — one of AWS's largest-scale distributed data services — including the CI/CD servers and fully automated build/deploy across all AWS-supported regions.
- Led the team that designed and shipped a Bors-style automated merge queue, gating integration on the exact merge candidate (not just the feature branch) — eliminating broken-mainline incidents and unblocking developer velocity org-wide.
- Added metrics-driven reporting on pipeline health and developer productivity, making bottlenecks visible and driving continuous improvement across the developer workflow.

### Prosper Marketplace (regulated fintech) — Lead DevOps Engineer · Jan 2015 – Dec 2016

- Rolled out org-wide CI/CD with Jenkins and containerization with Docker; managed Artifactory artifact/versioning, SonarQube static-analysis quality gates, and a Hadoop cluster on AWS (EMR).

### Pivotal Software — Member of Technical Staff · Sep 2011 – Jan 2015

- Managed CI infrastructure and agents; migrated Perforce to Git with enforced branching/merge policy; automated Coverity static analysis and code-coverage; built dynamic provisioning of Linux environments on AWS and vCloud.

## Open Source

### UniClaw · [github.com/uniclaw-labs/uniclaw](https://github.com/uniclaw-labs/uniclaw)

- Architected and shipped UniClaw end to end (concept to production), an open-source AI agent platform — Claude-powered agents on a **FastAPI (Python)** backend and a **React / TypeScript** app, with a pluggable provider/tool registry (27+ integrations), **OAuth2 authorization server with scoped JWTs**, rate limiting, Fernet-encrypted secrets, and non-root containers; 4,400+ automated tests across a polyglot codebase (Python, TypeScript, Rust). Also publish an open-source Lever MCP server.

## Education

- M.S., Software Engineering, San Jose State University (2011)
- B.E., Computer Engineering, Gujarat University (2009)

## Skills & Tools

- **AI/ML & LLM Integration:** Integrating AI/ML, LLMs & GenAI into production applications; multi-agent systems; agent orchestration (**LangGraph** supervisor, intent routing, memory, human-in-the-loop approval); AI control plane & agent gateway (AuthN/AuthZ, guardrails, model routing, per-tenant budgets, audit); RAG / retrieval (Vertex AI, BigQuery embeddings); MCP servers & agent frameworks with egress allow-listing; LLM observability & evaluation (**Langfuse** — prompts, traces, tokens, cost, evaluations); enterprise LLM rollout (Gemini Enterprise); AI-assisted development (Cursor, Claude Code, GitHub Copilot)
- **Product & Platform Architecture:** Secure, scalable multi-tenant SaaS platforms (single-tenant & on-prem-capable); end-to-end product engineering; technical roadmap & architecture; API design
- **Backend & Data:** Python (FastAPI); PostgreSQL; REST APIs; distributed systems at scale; SQL/NoSQL (MySQL, Oracle, DynamoDB)
- **Cloud & Delivery:** AWS, GCP, Azure; Kubernetes (EKS/GKE/AKS); Docker; Terraform; CI/CD (GitHub Actions, Jenkins, Bazel monorepo, Gradle); testing & release governance; observability (Grafana LGTM / OpenObserve, PagerDuty), SLOs & 99.99% reliability
- **Security & Compliance:** ISO 27001 / SOC 2 (audit ownership); cloud security; SBOM & static-analysis scanning; access control & encrypted secrets
- **Leadership:** Building & scaling onshore/offshore engineering teams; Agile delivery; stakeholder management; roadmaps & OKRs; ~$2–3M budget & vendor management; startup rapid-growth leadership
