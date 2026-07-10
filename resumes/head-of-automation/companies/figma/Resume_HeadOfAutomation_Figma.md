# Ishan Shah

San Carlos, CA • +1-925-596-8956 • ishan.hash@gmail.com

**Engineering Leader │ AI Developer Tooling & Agent Platforms │ Developer Experience, MCP & Agentic Workflows**

---

## Summary

Engineering leader and hands-on builder with 15+ years across AI developer tooling, agent platforms, DevOps, and infrastructure. I build the AI-assisted workflows that make engineers more productive: standardized Cursor and Claude Code across the org, shipped MCP servers (including a published open-source MCP server) as reusable action surfaces, and put Claude Code + GitHub Copilot on automated PR review. Ship production cloud agents 0-to-1 on GCP ADK — including miniBOT, a Gemini multi-agent troubleshooting assistant grounded by RAG. Deep distributed-systems and production-infra foundations: tooling for AWS Redshift at massive scale and Kubernetes control planes across GCP and Azure at 99.99% reliability, on CI/CD and build platforms (GitHub Actions, Jenkins, Bazel). Hire, scale, and coach infra/platform/DevEx teams, set technical direction, and partner cross-functionally on high-leverage AI opportunities.

## Experience

### CruxOCM Inc. (AI + industrial-automation startup) — Head of Automation (reporting to the CTO) · Feb 2025 – Present

- **AI developer tooling & productivity:** Standardized Cursor and Claude Code as the team development environment and deployed Claude Code + GitHub Copilot for automated PR review — accelerating delivery and improving code-review consistency across the org.
- **MCP servers & agent-driven DevEx:** Shipped MCP servers as reusable action surfaces — a published open-source Lever MCP server and Slack-native MCP servers — plus GCP ADK agents for self-service ephemeral infrastructure and automated cost governance, eliminating manual ops tickets.
- **Production cloud agents (0-to-1):** Architected and shipped production agents on GCP ADK — miniBOT, a Gemini multi-agent troubleshooting assistant (FastAPI/Cloud Run, Slack) grounded by RAG over BigQuery embeddings, and a test-authoring agent that auto-generates test cases.
- **Build-vs-buy & enterprise rollout:** Assessed and standardized the org's AI tooling and models (Cursor, Claude Code, GitHub Copilot, Gemini Enterprise) and rolled out Gemini Enterprise org-wide across engineering, operations, and GTM.
- **Platform reliability & infrastructure:** Standardized Kubernetes as the control plane across GCP and Azure with GitOps-style governance; 99.99% uptime and >$200K saved on ~$2M cloud spend.
- **Observability & incident response:** Own platform observability on the Grafana LGTM stack (Loki/Grafana/Tempo/Mimir) and/or OpenObserve with PagerDuty — logs, metrics, traces, SLOs, and on-call/incident response.
- **Quality & delivery:** Built a Robot Framework test platform (integration/E2E/regression with pipeline gating) augmented by the in-house AI test-authoring agent — manual regression cut from days to <12 hours.
- **Team & technical direction:** Lead and grow a technical org spanning AI, platform, DevOps, infrastructure, security, and quality — hire, mentor, and coach engineers; set technical direction; and partner with the CEO/CTO and cross-functional teams on the AI and engineering roadmap and quarterly OKRs.

### Insulet Corporation — Sr. Cloud Engineering Manager · Dec 2022 – Feb 2025

- Managed cloud and data-product teams (25–30 engineers) across DevOps, **developer-productivity tools**, and performance engineering — hiring and growing the team through a high-growth phase and partnering with the VP of Engineering on FY2023–FY2024 roadmaps and quarterly OKRs.
- Owned end-to-end CI/CD (branching to one-button deploy) with Jenkins, Python, and Gradle; operated highly available Jenkins on EKS/EFS (99.9% uptime) and cut deployment errors 15%.
- Built a performance and load-testing framework (Locust, Python) on EKS/AWS driving a 25% improvement in cloud architecture performance.
- Implemented SBOM generation and merge automation across ~25 microservices.

### Amazon (AWS Redshift) — Lead Systems Engineer · Dec 2016 – Dec 2022

- Owned the build, CI/CD, release ecosystem, and test tooling for Redshift — one of AWS's largest-scale distributed data services — including the CI/CD servers and fully automated build/deploy across all AWS-supported regions.
- Led the team that designed and shipped a Bors-style automated merge queue, gating integration on the exact merge candidate (not just the feature branch) — eliminating broken-mainline incidents and unblocking developer velocity org-wide.
- Added metrics-driven reporting on pipeline health and developer productivity, making bottlenecks visible and driving continuous improvement across the developer workflow.

### Prosper Marketplace — Lead DevOps Engineer · Jan 2015 – Dec 2016

- Rolled out org-wide CI/CD with Jenkins and containerization with Docker; managed Artifactory for microservice versioning and SonarQube for static analysis; ran a Hadoop cluster on AWS (EMR).

### Pivotal Software — Member of Technical Staff · Sep 2011 – Jan 2015

- Managed CI infrastructure and agents; migrated Perforce to Git; automated Coverity and code-coverage integration; dynamic provisioning of Linux test environments on AWS and vCloud.

## Open Source

### UniClaw · [github.com/uniclaw-labs/uniclaw](https://github.com/uniclaw-labs/uniclaw)

- Architected and shipped UniClaw, an open-source AI agent platform for connected vehicle control — a multi-provider framework supporting 27+ vehicle brands (Tesla, BMW, Ford, Rivian) with natural language commands via 12 messaging channels (WhatsApp, Telegram, Slack) and voice assistants (Alexa, Google Home), built on Claude-powered agents, FastAPI, and a Tauri/React desktop app.
- Designed a security-first architecture for sensitive vehicle credentials: an OAuth2 authorization server with scoped JWTs, automatic Fernet encryption of secrets, constant-time token validation, and non-root containers.
- Delivered production-grade quality across a polyglot codebase (Python, TypeScript, Rust): 4,400+ automated tests, pluggable provider/channel adapters, Dockerized multi-service orchestration, and three AI backends (Anthropic API, local Ollama, zero-cost command mode).

## Education

- M.S., Software Engineering, San Jose State University (2011)
- B.E., Computer Engineering, Gujarat University (2009)

## Skills & Tools

- **AI Developer Tooling & Agents:** AI-augmented development (Cursor, Claude Code, GitHub Copilot); MCP servers & integrations (incl. published open-source MCP server); production AI agents & runtimes (GCP ADK); agent architectures & agentic workflows; enterprise LLM rollout (Gemini Enterprise); LLM-driven testing & PR review; build-vs-buy for AI tools & models
- **Developer Experience & Delivery:** CI/CD (GitHub Actions, Jenkins, Bazel, Gradle); build tools & monorepo workflows; self-service ephemeral infrastructure; test automation (Robot Framework, Python); performance engineering (Locust); SBOM
- **Distributed Systems & Infrastructure:** Distributed systems & large-scale data services; Kubernetes (GKE, EKS, AKS); Terraform; Docker; GitOps; AWS, GCP, Azure; observability (Grafana LGTM / OpenObserve, PagerDuty), SLOs & reliability (99.99%)
- **Leadership:** Hiring, scaling & coaching infra/platform/DevEx teams; technical direction & architecture; cross-functional alignment; roadmaps & quarterly OKRs; high-growth environments
- **Software & Data:** Python; Java/C/C#; Shell; API design; MySQL, PostgreSQL, Oracle, DynamoDB
