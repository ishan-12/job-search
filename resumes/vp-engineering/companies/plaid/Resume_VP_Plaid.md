# Ishan Shah

San Carlos, CA • +1-925-596-8956 • ishan.hash@gmail.com

**Engineering Manager, AI Applications │ LLM Product Development │ Agent Orchestration, MCP & Trust Infrastructure**

> Tailored for Plaid — Engineering Manager, AI Applications (SF HQ). Leads with shipped LLM product work in
> their order: MCP integration patterns, trust infrastructure for agents, multi-agent support, RAG/semantic
> search, evaluation. Then the Staff-IC → manager arc they ask for. Do NOT claim fine-tuning, training or
> serving own ML models, user research, or consumer conversational UX. Keep facts in sync with
> `profile/candidate-profile.md`.

---

## Summary

Engineering leader who ships LLM products, not just LLM demos. I build and lead teams that put agents in front of real users: a multi-agent support assistant with an orchestrator routing to specialist agents, MCP servers as governed integration surfaces (including a published open-source one), RAG and semantic search over vector embeddings, and the evaluation and tracing layer that tells us whether any of it is working. I also built the trust infrastructure that makes agents safe to expose — authentication and authorization, guardrails, tool registration with egress allowlists and short-lived credentials, per-tenant budgets, a human-in-the-loop approval gate, and end-to-end audit. My arc is the one this role describes: Staff-level engineer for a decade — build, CI/CD and release for AWS Redshift — then into management, leading teams of up to 25–30 across cloud and data-product engineering. I take 0→1 products from exploration to production, including a commercial multi-tenant B2B SaaS AI platform now sold to external customers, and I work natively in privacy-sensitive, regulated environments (ISO/IEC 27001, SOC 2, FDA-regulated medical devices, regulated fintech).

## Experience

### CruxOCM Inc. — VP of Engineering / Head of Automation (reporting to the CTO) · Feb 2025 – Present

- **Multi-turn, multi-agent product:** Shipped a production support and troubleshooting assistant — an orchestrator interprets a request, routes to specialist agents across telemetry, log analysis, signal analysis, ticket history and documentation, reconciles what returns, and produces the finished deliverable. Driven from chat, where the users already work.
- **MCP servers as integration patterns:** Built MCP servers as reusable, governed action surfaces for internal and third-party systems, and **published an open-source Lever MCP server**. MCP backends register with a declared tool surface, an egress allowlist and short-lived credentials — integration as a contract rather than a bespoke wiring job.
- **Trust infrastructure for agents:** Architected and operate an AI control plane that makes agents safe to expose: a gateway handling authentication, authorization, guardrails, agent and tool registration, path and model routing, per-tenant budgets and audit, fronting a **LangGraph supervisor orchestrator** with a shared memory store and a **human-in-the-loop approval gate** for consequential actions.
- **Evaluation and observability for LLM systems:** Langfuse in-cluster for prompts, traces, tokens, **cost attribution, evaluations and datasets** — plus an admission gate for AI-generated artifacts built on the principle that a model never certifies its own output.
- **RAG and semantic search:** Grounded agents with retrieval over BigQuery vector embeddings of documentation and support history on Vertex AI, with deliberate model tiering — a fast model for agent turns, a frontier model for document generation.
- **0→1 product:** Architected a commercial multi-tenant B2B SaaS AI platform from concept to production, **sold to external business customers** across Azure and GCP — the substrate on which customers run governed, agent-based AI workloads.
- **Team leadership and AI-native engineering:** Lead and grow a distributed engineering organization; standardized **Cursor and Claude Code** as the team development environment with Claude Code and GitHub Copilot for automated PR review, and wrote the conventions the team codes against — how to prompt with real repository context, what must be verified before AI output ships, and where to stop trusting it.
- **Privacy and compliance:** Own **ISO/IEC 27001** and **SOC 2** programs through third-party audit — controls, audit logging, and evidence that they operated — in a safety-critical, regulated environment.

### Insulet Corporation (FDA-regulated medical devices) — Sr. Cloud Engineering Manager · Dec 2022 – Feb 2025

- Led **25–30 engineers** across cloud, DevOps, developer productivity and **data-product** teams for a connected medical-device platform; hired, coached and developed engineers and leads; partnered with the VP of Engineering on roadmaps and quarterly OKRs.
- Owned end-to-end CI/CD from branching to one-button deploy; **reduced deployment errors 15%**; operated highly available Jenkins on EKS/EFS at 99.9%.
- Built a performance and load-testing framework (Locust, Python) that improved cloud architecture performance **25%**; implemented SBOM and automated regulated change control across ~25 microservices.

### Amazon (AWS Redshift) — Lead Systems Engineer · Dec 2016 – Dec 2022

- Staff-level individual contributor and technical lead: owned the build, CI/CD, release ecosystem and test tooling for Redshift — one of AWS's largest-scale distributed data services — including fully automated build and deploy across every AWS-supported region.
- **Led a team of 7 engineers** delivering a Bors-style automated merge queue that gated integration on the exact merge candidate — eliminating broken-mainline incidents and unblocking developer velocity org-wide.
- Added metrics-driven reporting on pipeline health and developer productivity, making bottlenecks visible rather than anecdotal.

### Prosper Marketplace (regulated fintech) — Lead DevOps Engineer · Jan 2015 – Dec 2016

- Rolled out org-wide CI/CD with Jenkins and containerization with Docker; managed Artifactory versioning, SonarQube quality gates, and a Hadoop cluster on AWS (EMR) in a regulated consumer-lending environment.

### Pivotal Software — Member of Technical Staff · Sep 2011 – Jan 2015

- Owned CI infrastructure; migrated Perforce to Git with enforced policy; automated static analysis and coverage; built dynamic provisioning of Linux test environments on AWS and vCloud.

## Open Source

### UniClaw · [github.com/uniclaw-labs/uniclaw](https://github.com/uniclaw-labs/uniclaw) · Apache-2.0 / MIT

- Open-source natural-language control platform: a FastAPI backend and React 19 / TypeScript desktop app, with an agent running **three model modes chosen by what the request deserves** — Claude Sonnet for open-ended intent, local Gemma via Ollama for private or offline use, and a zero-cost command menu for deterministic requests. **27 provider adapters** normalized behind one canonical contract, 12 messaging channels, OAuth2 with scoped JWTs, and **4,400+ automated tests**. Also publish an open-source **Lever MCP server**.

## Education

- M.S., Software Engineering, San Jose State University (2011)
- B.E., Computer Engineering, Gujarat University (2009)

## Skills & Tools

- **LLM Product Development:** Prompt engineering and grounding context design; **RAG and semantic search** (vector embeddings, Vertex AI); **agent orchestration** (LangGraph supervisor, multi-agent routing, memory); **MCP** servers and tool governance; **evaluation frameworks** (Langfuse — traces, cost, evaluations, datasets); multi-model routing and cost tiering; GCP ADK
- **Trust & Safety for Agents:** AuthN/AuthZ for agent and tool access; guardrails; egress allowlists and short-lived credentials; human-in-the-loop approval gates; per-tenant budgets; end-to-end audit; admission gates for AI-generated artifacts
- **Product & Delivery:** 0→1 exploration to production; commercial multi-tenant B2B SaaS; rapid iteration with engineering and product partners; A/B-ready instrumentation and cost/quality tradeoffs
- **Leadership:** Staff-level IC before management; leading and growing teams (7 at Amazon, 25–30 at Insulet, multi-function org at CruxOCM); hiring, coaching, performance; AI-native engineering standards (Cursor, Claude Code, GitHub Copilot)
- **Privacy & Compliance:** ISO/IEC 27001 and SOC 2 audit ownership; FDA-regulated medical device software; regulated fintech; data-handling and audit-trail design
- **Engineering:** Python / FastAPI; TypeScript / React; Java/C/C#; Shell; API design; PostgreSQL, MySQL, DynamoDB, BigQuery; AWS, GCP, Azure; Kubernetes; Docker; CI/CD
