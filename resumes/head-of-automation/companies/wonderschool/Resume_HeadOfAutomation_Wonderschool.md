# Ishan Shah

San Carlos, CA • +1-925-596-8956 • ishan.hash@gmail.com

**Engineering Leader │ Multi-Agent AI Systems in Production │ Agent Orchestration, Evaluation & Reliability │ Hands-On + Team Leadership**

---

## Summary

Hands-on AI-agent-systems leader who turns partially functional agent platforms into production-grade infrastructure. I architected and operate a production AI control plane — a LangGraph supervisor orchestrating specialist agents with a memory store, agent-to-agent coordination, content guardrails, and a human-in-the-loop gate — directly addressing the coordination failures, memory loss, and context limits that break multi-agent systems. I design the evaluation systems that measure agent success rates and failure modes (Langfuse), build reliable end-to-end execution with validation and retry, and drive company-wide agent adoption (standardized Claude Code and Cursor, agent standards, non-engineer usability). I stay in the codebase (Python/FastAPI) while leading and hiring small, high-accountability teams, and I tie agent performance to business outcomes. Deep regulated/compliance background (ISO 27001, SOC 2; fintech, healthcare).

## Experience

### CruxOCM Inc. — VP of Engineering / Head of Automation (reporting to the CTO) · Feb 2025 – Present

- **Multi-agent system architecture:** Architected and operate a production-hardened AI control plane — a LangGraph supervisor orchestrator routing to specialist agents, with a memory store, agent-to-agent coordination, content guardrails, and a human-in-the-loop approval gate on GKE (Kuma mesh) — hardening a partially functional agent stack into reliable production infrastructure and directly tackling coordination failures, memory loss, and context limits.
- **Evaluation systems & performance reporting:** Designed agent evaluation and observability with Langfuse — success rates, failure modes, traces, tokens, and cost — with feedback loops that raise output quality and minimize human correction, tracking every agent across the system.
- **Reliable execution & production agents:** Built reliable end-to-end execution with validation and retry logic; shipped production agents on GCP ADK — miniBOT, a Gemini multi-agent assistant grounded by RAG, and TestBOT, which auto-generates tests — plus reusable MCP servers as governed tool surfaces.
- **Company-wide agent adoption & standards:** Drove org-wide agent adoption — an enterprise Gemini rollout, standardized Cursor/Claude Code + GitHub Copilot, Slack-native agents for non-engineers, and standards/conventions for agent-based workflows that reduce reliance on manual processes.
- **Business impact:** Tie agent and automation metrics to business outcomes — shipped IAH, a commercial multi-tenant B2B SaaS AI platform sold to external customers (revenue), and automated cost-reducing workflows (>$200K saved on ~$2M); ISO 27001 and SOC 2 for compliance.
- **Hands-on + team leadership:** Stay hands-on in the codebase (Python/FastAPI) while hiring, developing, and leading engineers (including DevOps) to high performance and accountability.

### Amazon (AWS Redshift) — Lead Systems Engineer · Dec 2016 – Dec 2022

- Owned the build, CI/CD, release ecosystem, and test tooling for Redshift — one of AWS's largest-scale distributed data services — including CI/CD servers and fully automated build/deploy across all AWS-supported regions.
- Designed and shipped a Bors-style automated merge queue, gating integration on the exact merge candidate — eliminating broken-mainline incidents and improving reliability org-wide.
- Added metrics-driven reporting on pipeline health and developer productivity, driving continuous improvement.

### Insulet Corporation (FDA-regulated medical devices) — Sr. Cloud Engineering Manager · Dec 2022 – Feb 2025

- Led cloud and data-product teams (25–30 engineers) across DevOps, developer productivity, and performance engineering; partnered with the VP of Engineering on roadmaps and OKRs.
- Owned end-to-end CI/CD with gating and one-button deploy (Jenkins, Python, Gradle); operated highly available Jenkins on EKS/EFS (99.9% uptime); cut deployment errors 15%.
- Built a performance and load-testing framework (Locust, Python) on EKS/AWS (25% improvement); implemented SBOM and regulated change control.

### Prosper Marketplace (regulated fintech) — Lead DevOps Engineer · Jan 2015 – Dec 2016

- Rolled out org-wide CI/CD with Jenkins and containerization with Docker; managed Artifactory versioning, SonarQube quality gates, and a Hadoop cluster on AWS (EMR).

### Pivotal Software — Member of Technical Staff · Sep 2011 – Jan 2015

- Managed CI infrastructure; migrated Perforce to Git with enforced branching/merge policy; automated static analysis and code-coverage; built dynamic provisioning of Linux environments on AWS and vCloud.

## Open Source

### UniClaw · [github.com/uniclaw-labs/uniclaw](https://github.com/uniclaw-labs/uniclaw)

- Architected and shipped UniClaw, an open-source multi-agent AI platform — Claude-powered agents routed across model backends through a pluggable provider/tool registry (27+ integrations) with per-request auth, on a FastAPI (Python) backend and a React/TypeScript app; OAuth2 with scoped JWTs, encrypted secrets, non-root containers; 4,400+ automated tests across a polyglot codebase (Python, TypeScript, Rust). Also publish an open-source Lever MCP server.

## Education

- M.S., Software Engineering, San Jose State University (2011)
- B.E., Computer Engineering, Gujarat University (2009)

## Skills & Tools

- **Multi-Agent AI Systems:** Multi-agent architecture & orchestration (LangGraph supervisor); agent-to-agent coordination; memory; content guardrails; human-in-the-loop; MCP tool governance; production AI agents (GCP ADK); Claude Code, Cursor
- **Evaluation & Reliability:** Agent evaluation systems (Langfuse) — success rates, failure modes, feedback loops; validation & retry; observability (Grafana LGTM / OpenObserve, PagerDuty); SLOs; 99.99% reliability; debugging complex systems
- **Adoption & Automation:** Company-wide agent adoption & standards; non-engineer usability (Slack-native agents); workflow automation; internal developer platform; enterprise LLM rollout (Gemini Enterprise); RAG / retrieval (Vertex AI)
- **Hands-On Engineering:** Python / FastAPI; system architecture; production systems; AWS, GCP, Azure; Kubernetes; Docker; CI/CD
- **Business & Compliance:** Tie agent metrics to business outcomes; cost-reducing automation; commercial B2B SaaS AI platform (IAH); ISO 27001 / SOC 2; regulated (fintech, healthcare)
- **Leadership:** Hands-on + leading and hiring small high-accountability teams (incl. DevOps); fast-paced, high-ownership startup delivery
