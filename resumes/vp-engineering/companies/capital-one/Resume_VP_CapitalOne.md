# Ishan Shah

San Carlos, CA • +1-925-596-8956 • ishan.hash@gmail.com

**Senior AI Engineering Leader │ Agentic AI Platforms & Control Planes │ LLM Inference, RAG/Vector Search, Guardrails, Memory & Model Evaluation — Responsible & Governed**

---

## Summary

AI engineering leader who builds agentic AI platforms and the control planes that make them safe, governed, and scalable. I architected and operate a production-hardened AI control plane — an Agent Gateway (model routing / LLM inference, content guardrails, budgets, and audit), a LangGraph supervisor orchestrator with a memory store and human-in-the-loop approval, MCP tool governance, and Langfuse model evaluation — and shipped production multi-agent systems grounded by RAG over vector embeddings. I make build-vs-buy decisions across open-source and SaaS AI, deploy scalable AI across AWS, GCP, and Azure, and lead responsible AI in regulated environments (ISO 27001, SOC 2; financial services). I set technical vision and roadmap for foundational AI systems, partner with engineers, scientists, and product managers, and mentor, coach, and attract top engineering talent — atop 15+ years of large-scale distributed-systems and platform leadership.

## Experience

### CruxOCM Inc. — VP of Engineering / Head of Automation (reporting to the CTO) · Feb 2025 – Present

- **AI engineering leadership & vision:** Set the technical vision and roadmap for foundational AI systems; lead a distributed org across AI, platform, and infrastructure; partner cross-functionally with engineers, product, and operations; and mentor, coach, and attract top talent.
- **Agentic AI platform & control plane:** Architected and operate a production-hardened AI control plane on GKE (Kuma service mesh, mTLS) — an Agent Gateway providing model routing / LLM inference, content guardrails, per-tenant budgets, and full audit; a LangGraph supervisor orchestrator with a memory store and a human-in-the-loop approval gate; MCP tool governance with egress allow-listing; and Langfuse model evaluation, tracing, and cost.
- **LLM inference, similarity search & agents:** Architected miniBOT, a Gemini multi-agent assistant grounded by RAG over BigQuery vector embeddings (VectorDB / similarity search) on Vertex AI; delivered LLM-powered products and an org-wide Gemini Enterprise rollout.
- **Build-vs-buy & AI platform (IAH):** Make build-vs-buy decisions across open-source and SaaS AI technologies and vendors; architected IAH, a commercial multi-tenant B2B SaaS AI platform (Azure and GCP) sold to external business customers, built from concept to production.
- **Responsible AI, security & compliance:** Govern AI with guardrails, human-in-the-loop, and audit; own ISO 27001 and SOC 2 (audit ownership) and security scanning for a safety-critical, regulated environment.
- **Scalable AI on cloud & reliability:** Deploy scalable AI across AWS, GCP, and Azure on Kubernetes at 99.99% reliability with observability and SLOs; own ~$2M cloud spend with >$200K saved.

### Amazon (AWS Redshift) — Lead Systems Engineer · Dec 2016 – Dec 2022

- Owned the build, CI/CD, release ecosystem, and test tooling for Redshift — one of AWS's largest-scale distributed data services — including the CI/CD servers and fully automated build/deploy across all AWS-supported regions.
- Led the team that designed and shipped a Bors-style automated merge queue, gating integration on the exact merge candidate (not just the feature branch) — eliminating broken-mainline incidents and unblocking developer velocity org-wide.
- Added metrics-driven reporting on pipeline health and developer productivity, making bottlenecks visible and driving continuous improvement across the developer workflow.

### Insulet Corporation (FDA-regulated medical devices) — Sr. Cloud Engineering Manager · Dec 2022 – Feb 2025

- Led cloud and data-product teams (25–30 engineers) across platform, DevOps, developer productivity, and performance engineering; partnered with the VP of Engineering on multi-year roadmaps and quarterly OKRs.
- Built a performance and load-testing framework (Locust, Python) on EKS/AWS (25% improvement); operated highly available Jenkins on EKS/EFS (99.9% uptime) and cut deployment errors 15%.
- Owned end-to-end CI/CD with gating and one-button deploy (Jenkins, Python, Gradle); implemented SBOM generation and regulated change control for data integrity and supply-chain security.

### Prosper Marketplace (regulated fintech / financial services) — Lead DevOps Engineer · Jan 2015 – Dec 2016

- Rolled out org-wide CI/CD with Jenkins and containerization with Docker for a regulated consumer-lending platform; managed Artifactory artifact/versioning, SonarQube static-analysis quality gates, and a Hadoop cluster on AWS (EMR).

### Pivotal Software — Member of Technical Staff · Sep 2011 – Jan 2015

- Managed CI infrastructure and agents; migrated Perforce to Git with enforced branching/merge policy; automated static analysis and code-coverage; built dynamic provisioning of Linux environments on AWS and vCloud.

## Open Source

### UniClaw · [github.com/uniclaw-labs/uniclaw](https://github.com/uniclaw-labs/uniclaw)

- Architected and shipped UniClaw, an open-source multi-model AI agent platform — a governed gateway routing natural-language requests across model backends (Anthropic, local Ollama, command mode) via a pluggable provider/tool registry (27+ integrations) with per-request auth, on FastAPI (Python) + React/TypeScript; OAuth2 with scoped JWTs, encrypted secrets, non-root containers; 4,400+ automated tests (Python, TypeScript, Rust). Also publish an open-source Lever MCP server.

## Education

- M.S., Software Engineering, San Jose State University (2011)
- B.E., Computer Engineering, Gujarat University (2009)

## Skills & Tools

- **Agentic AI & Platforms:** Agentic AI platforms; AI control plane (Agent Gateway, LangGraph supervisor, memory, HITL) on GKE/Kuma; multi-agent orchestration; MCP tool governance; enterprise LLM rollout (Gemini Enterprise)
- **LLM & AI/ML Technologies:** LLM inference & model routing; RAG / retrieval & VectorDBs (Vertex AI, BigQuery embeddings) / similarity search; content guardrails; memory; model evaluation (Langfuse); MLOps/LLMOps
- **Build-vs-Buy & Providers:** Build-vs-buy across open-source & SaaS AI; Anthropic (Claude), Google (Gemini, Vertex AI); vendor & TCO assessment
- **Cloud & Reliability:** AWS, GCP, Azure; Kubernetes (EKS/GKE/AKS); Terraform; Docker; observability (Grafana LGTM / OpenObserve, PagerDuty), SLOs & 99.99% reliability; scalable AI deployment
- **Responsible AI, Security & Compliance:** Guardrails, human-in-the-loop, audit & governance; ISO 27001 / SOC 2 (audit ownership); regulated financial-services & healthcare
- **Leadership:** Technical vision & roadmap for foundational AI systems; hiring, mentoring, coaching & attracting talent; cross-functional partnership (engineers, scientists, product); executive communication; Python / FastAPI
