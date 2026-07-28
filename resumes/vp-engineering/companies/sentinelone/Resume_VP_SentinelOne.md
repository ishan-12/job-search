# Ishan Shah

San Carlos, CA • +1-925-596-8956 • ishan.hash@gmail.com

**AI Platform & Developer-Experience Engineering Leader │ Agents, MCP & Multi-Model Gateways │ AI-Driven CI/CD, Internal Developer Platforms & Security**

---

## Summary

Engineering leader with 15+ years building AI platforms and the developer platforms they run on. I've built the enterprise AI foundation — a Gemini multi-agent assistant (miniBOT) grounded by RAG on Vertex AI, reusable MCP servers, an org-wide Gemini Enterprise rollout, and an open-source multi-model AI gateway (OAuth2 authorization, scoped JWTs, multi-model routing) on Python/FastAPI + React/TypeScript — and I'm now architecting a production-hardened AI control plane (Agent Gateway, LangGraph supervisor, MCP allow-listing, model evaluations). I've also used AI to transform how engineering ships: AI-driven CI/CD with AI-assisted code generation, an agent that auto-generates test suites, and contextual PR review, on an internal developer platform with self-service infrastructure. I own security and compliance end to end (ISO 27001, SOC 2), assess build-vs-buy across model providers and vendors, partner cross-functionally with Product, Security, and Finance, and hire, mentor, and technically lead distributed engineering teams.

## Experience

### CruxOCM Inc. — VP of Engineering / Head of Automation (reporting to the CTO) · Feb 2025 – Present

- **Scope & leadership:** Lead a distributed engineering org (AI, platform, DevOps, infrastructure, security, quality); partner with the CEO/CTO and cross-functionally with product and security; hire, mentor, and technically lead engineers and leads; set architecture standards and own roadmap and quarterly OKRs.
- **Enterprise AI platform & agents:** Architected miniBOT, a Gemini-powered multi-agent assistant (FastAPI on Cloud Run) grounded by RAG over BigQuery vector embeddings on Vertex AI; built reusable MCP servers as action surfaces (a published open-source Lever MCP server + Slack-native); ran an org-wide Gemini Enterprise rollout with access/policy controls and build-vs-buy vendor assessment.
- **AI control plane (Gateway + Harness), in build:** Architecting a production-hardened AI control plane on GKE (Kuma service mesh, mTLS everywhere) — an **Agent Gateway** providing centralized AuthN/AuthZ, content guardrails, agent/MCP registration, **multi-model routing**, per-tenant **budgets**, and a full request **audit trail** across a single `/agents/*` and `/mcp/*` surface; a **LangGraph supervisor** orchestrator with a memory store and a **human-in-the-loop approval gate**; MCP backends governed by **egress allow-listing** and short-lived credentials; and **Langfuse** observability with **model evaluations**, traces, tokens, and cost.
- **AI-driven CI/CD:** Turned the pipeline into an AI-assisted system — Cursor/Claude Code for AI-assisted code generation, TestBOT (a Gemini agent on GCP ADK) that auto-generates test suites, and Claude Code + Copilot for contextual PR review — cutting manual regression from days to under 12 hours.
- **Internal developer platform:** Architected a web-services platform from scratch; standardized Kubernetes across GCP and Azure with GitOps and Terraform; shipped self-service ephemeral environments that eliminate manual ops toil; drive developer productivity as DORA metrics.
- **Reliability, observability & cost:** Own platform observability on the Grafana LGTM stack (Loki/Grafana/Tempo/Mimir) and/or OpenObserve with PagerDuty — logs, metrics, traces, SLOs, and blameless incident response at 99.99% uptime; own ~$2M cloud spend with >$200K saved.
- **Security, governance & compliance:** Spearheaded ISO 27001 and SOC 2 programs (audit ownership); SBOM and static-analysis security scanning; partnered across engineering, security, and operations on shared standards for a safety-critical, regulated environment.

### Insulet Corporation (FDA-regulated medical devices) — Sr. Cloud Engineering Manager · Dec 2022 – Feb 2025

- Led cloud and data-product teams (25–30 engineers) across DevOps, developer productivity, and performance engineering; partnered with the VP of Engineering on multi-year roadmaps and quarterly OKRs.
- Owned end-to-end CI/CD with centralized policy and gating; operated highly available Jenkins on EKS/EFS (99.9% uptime) and cut deployment errors 15%.
- Built a performance and load-testing framework (Locust, Python) on EKS/AWS (25% improvement); implemented SBOM generation and security automation across ~25 microservices in CI/CD.

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

- Architected and shipped UniClaw, an open-source multi-model AI gateway — routes natural-language requests across three model backends (Anthropic, local Ollama, command mode) via a pluggable provider/tool registry (27+ integrations) with per-request auth, on FastAPI (Python) + React/TypeScript; an OAuth2 authorization server with scoped JWTs, rate limiting, Fernet-encrypted secrets, and non-root containers — the auth, policy, and routing patterns an enterprise AI gateway requires; 4,400+ tests (Python, TypeScript, Rust). Also publish an open-source Lever MCP server.

## Education

- M.S., Software Engineering, San Jose State University (2011)
- B.E., Computer Engineering, Gujarat University (2009)

## Skills & Tools

- **AI Platform & Agent Engineering:** Multi-agent orchestration & agentic workflows; RAG/retrieval (Vertex AI, BigQuery embeddings); MCP servers & action surfaces (incl. published open-source MCP server); AI gateway patterns (centralized auth, scoped JWTs, rate limiting, multi-model routing); enterprise LLM rollout & administration (Gemini Enterprise)
- **AI-Driven Development & DevEx:** AI-assisted code generation (Cursor, Claude Code); automated test generation (AI agents, GCP ADK); AI-assisted PR review (Claude Code, GitHub Copilot); internal developer platforms & self-service infrastructure; developer productivity & DORA metrics
- **Providers & Stack:** Anthropic (Claude) & Google (Gemini, Vertex AI); multi-model routing; Python / FastAPI; React / TypeScript; pydantic; REST / API design
- **Platform, CI/CD & Cloud:** AWS, GCP, Azure; Kubernetes (GKE/EKS/AKS); Terraform; Docker; GitOps; CI/CD (GitHub Actions, Jenkins, Bazel monorepo, Gradle); merge-queue & release governance
- **Reliability & Security:** Observability (Grafana LGTM / OpenObserve, PagerDuty), SLOs & 99.99% reliability; OAuth2 / scoped JWTs; secrets encryption; SBOM & static-analysis scanning; ISO/IEC 27001 & SOC 2 (audit ownership)
- **Leadership & Strategy:** Hiring, mentoring & technically leading engineering teams; architecture standards & review; build-vs-buy & vendor assessment; cross-org partnership (Product, Security, Finance, Infosec); roadmaps & OKRs; executive communication
