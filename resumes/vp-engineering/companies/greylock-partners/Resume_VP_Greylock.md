# Ishan Shah

San Carlos, CA • +1-925-596-8956 • ishan.hash@gmail.com

**Hands-On Engineering Leader │ AI Agents, RAG & Agent Platforms │ Backend, Platform & Distributed Infrastructure**

---

## Summary

Hands-on engineering leader with 15+ years building backend, infrastructure, and AI systems — and still in the code. Ship production AI agents 0-to-1: GCP ADK multi-agent runtimes (miniBOT — an orchestrator routing to specialized agents on FastAPI/Cloud Run) grounded by RAG on Vertex AI over operational docs and support tickets; MCP servers and agent frameworks for agentic workflows. Deep platform and distributed-systems foundations — from tooling for AWS Redshift at massive scale to Kubernetes control planes across GCP and Azure at 99.99% reliability. Lead small, highly technical teams: hire, mentor, set the engineering-quality bar, and make architectural calls under ambiguity in fast-moving, safety-critical environments.

## Experience

### CruxOCM Inc. (industrial-automation startup) — VP of Engineering / Head of Automation (reporting to the CTO) · Feb 2025 – Present

- **Production AI agents (0-to-1):** Architected and shipped production AI agents from scratch on GCP ADK — miniBOT, a Gemini-powered multi-agent troubleshooting assistant (FastAPI/Cloud Run, Slack) with an orchestrator routing to specialized agents for dashboards, logs, signal/hydraulic analysis, tickets, and docs Q&A; and a test-authoring agent that auto-generates Robot Framework tests.
- **Data ingestion & retrieval:** Built RAG/retrieval on Vertex AI — BigQuery vector embeddings over operational documentation and support tickets — to ground the agents, and rolled out Gemini Enterprise across the full application suite for org-wide AI access.
- **Agentic workflow frameworks:** Built the frameworks teams use to develop, configure, and govern agents at scale — MCP servers as reusable action surfaces (including a **published open-source Lever MCP server**), agent configuration conventions (CLAUDE.md / AGENTS.md) for multi-agent workflows, and prompt/skill versioning.
- **Backend & platform infrastructure:** Standardized Kubernetes as the control plane across GCP and Azure with GitOps-style governance; shipped Slack-native MCP servers and ADK agents for self-service ephemeral infrastructure and automated cost governance; 99.99% uptime, >$200K saved on ~$2M cloud spend.
- **Engineering-quality bar at startup pace:** Built a Robot Framework test platform (integration/E2E/regression with pipeline gating) augmented by the in-house AI test-authoring agent — manual regression cut from days to <12 hours; standardized Cursor and Claude Code and deployed automated PR review to hold a high quality bar without slowing execution.
- **Team & technical direction:** Lead a small, highly technical org spanning AI, backend/web services, DevOps, infrastructure, security, and quality — hire, mentor, and develop engineers; set technical direction and partner with the CEO/CTO on the AI and engineering roadmap; own compliance programs (ISO 27001, SOC 2) in a safety-critical, regulated environment.

### Insulet Corporation (FDA-regulated medical devices) — Sr. Cloud Engineering Manager · Dec 2022 – Feb 2025

- Managed cloud and data-product teams (25–30 engineers) across DevOps, developer productivity, and performance engineering for a connected medical-device (diabetes care) platform.
- Owned CI/CD end to end; operated highly available Jenkins on EKS/EFS (99.9% uptime) and cut deployment errors 15%.
- Built a performance and load-testing framework (Locust, Python) on EKS/AWS, running load and stress tests that drove a 25% improvement in cloud architecture performance.
- Automated SBOM generation and merge across ~25 microservices with CI/CD integration, and built a Python document-automation framework for regulated change control (ECO, SBR, PCO).

### Amazon (AWS Redshift) — Lead Systems Engineer · Dec 2016 – Dec 2022

- Owned the build, CI/CD, release ecosystem, and test tooling for Redshift — one of AWS's largest-scale distributed data services — including the CI/CD servers and fully automated build/deploy across all AWS-supported regions.
- Led the team that designed and shipped a Bors-style automated merge queue, gating integration on the exact merge candidate (not just the feature branch) — eliminating broken-mainline incidents and unblocking developer velocity org-wide.
- Added metrics-driven reporting on pipeline health and developer productivity, making bottlenecks visible and driving continuous improvement across the developer workflow.

### Prosper Marketplace (regulated fintech) — Lead DevOps Engineer · Jan 2015 – Dec 2016

- Rolled out org-wide CI/CD with Jenkins; implemented containerization with Docker; managed Artifactory, SonarQube, and a Hadoop cluster on AWS (EMR).

### Pivotal Software — Member of Technical Staff · Sep 2011 – Jan 2015

- Managed CI infrastructure; migrated Perforce to Git; automated Coverity and code-coverage integration; dynamic provisioning of Linux test environments on AWS and vCloud.

## Open Source

### UniClaw · [github.com/uniclaw-labs/uniclaw](https://github.com/uniclaw-labs/uniclaw)

- Architected and shipped UniClaw, an open-source AI agent platform for connected vehicle control — a multi-provider framework supporting 27+ vehicle brands (Tesla, BMW, Ford, Rivian) with natural language commands via 12 messaging channels (WhatsApp, Telegram, Slack) and voice assistants (Alexa, Google Home), built on Claude-powered agents, FastAPI, and a Tauri/React desktop app.
- Designed a security-first architecture for sensitive vehicle credentials: an OAuth2 authorization server with scoped JWTs, automatic Fernet encryption of secrets, constant-time token validation, and non-root containers — patterns transferable to SOC 2 / ISO 27001 environments.
- Delivered production-grade quality across a polyglot codebase (Python, TypeScript, Rust): 4,400+ automated tests, pluggable provider/channel adapters, Dockerized multi-service orchestration, and three AI backends (Anthropic API, local Ollama, zero-cost command mode).

## Education

- M.S., Software Engineering, San Jose State University (2011)
- B.E., Computer Engineering, Gujarat University (2009)

## Skills & Tools

- **AI & Agent Engineering:** Production AI agents & runtimes (GCP ADK) shipped 0-to-1; RAG/retrieval & data ingestion (Vertex AI, BigQuery embeddings); MCP servers & agentic workflow frameworks; multi-agent orchestration; prompt & agent-skill lifecycle; MLOps/LLMOps; enterprise LLM rollout (Gemini Enterprise); AI-augmented development (Cursor, Claude Code, GitHub Copilot)
- **Backend, Platform & Distributed Infrastructure:** AWS, GCP, Azure; Kubernetes (GKE, EKS, AKS); Terraform; Docker; GitOps; distributed systems & large-scale data services; observability (Grafana LGTM / OpenObserve, PagerDuty) & SLOs; 99.99% reliability
- **Delivery & Quality:** 0-to-1 product delivery; CI/CD (GitHub Actions, Jenkins, Bazel, Gradle); test automation (Robot Framework, Python); performance engineering (Locust); high engineering-quality bar at startup pace; SBOM
- **Leadership:** Hiring, mentoring & developing engineers; small, highly technical teams; technical direction & architecture under ambiguity; roadmaps & quarterly OKRs; C-suite partnership
- **Software & Data:** Python; Java/C/C#; Shell; API design; MySQL, PostgreSQL, Oracle, DynamoDB
- **Regulated & Complex-Data Domains:** Safety-critical OT/SCADA operational data; FDA-regulated medical devices; ISO/IEC 27001 & SOC 2 (audit ownership)
