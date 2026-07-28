# Ishan Shah

San Carlos, CA • +1-925-596-8956 • ishan.hash@gmail.com

**VP of Engineering │ AI Platforms & Agent Engineering │ MLOps, Cloud Infrastructure & Regulated Industries**

> Generic / base VP resume. Source of truth for the VP track. Do not tailor this file — copy it into
> `companies/<company>/` and tailor there. Keep facts in sync with `profile/candidate-profile.md`.

---

## Summary

Engineering leader with 15+ years building and scaling engineering organizations across AI platforms, agent engineering, infrastructure, DevOps, and quality. Shipped production AI agents and agent platforms from scratch — GCP ADK agent runtimes, MCP servers, agent skills/configuration frameworks, RAG and retrieval pipelines, and org-wide enterprise LLM rollouts — with MLOps/LLMOps, observability, and 99.99% platform reliability built in. Architected IAH 0→1, a multi-tenant B2B SaaS platform (Azure and GCP) sold to external business customers — unifying AI agents for troubleshooting and information, automated test generation, an RFI (request-for-information) tool, and a trainer. Deep regulated-industry experience: safety-critical energy operations (pipeline SCADA/OT), FDA-regulated medical devices, and ISO 27001 / SOC 2 compliance ownership. Own $2–3M budgets and partner directly with the C-suite on AI strategy, roadmaps, and quarterly OKRs.

## Experience

### CruxOCM Inc. — VP of Engineering / Head of Automation (reporting to the CTO) · Feb 2025 – Present

- **Scope & org:** Lead a distributed engineering organization spanning AI, Web Services, DevOps, Infrastructure, Security, Quality, and IT for an industrial automation platform operating in safety-critical, highly regulated energy environments; partner with the CEO and CTO on the FY2025–FY2026 AI and engineering roadmap and quarterly OKRs.
- **Agent platforms (production):** Architected and shipped production AI agents on GCP ADK — miniBOT, a Gemini-powered multi-agent troubleshooting assistant (FastAPI/Cloud Run, driven from Slack) with an orchestrator routing to specialized agents for dashboards, logs, signal/hydraulic analysis, tickets, and docs Q&A; and a test-authoring agent that auto-generates Robot Framework test cases.
- **Agent skills & lifecycle management:** Built the frameworks that let teams develop, configure, and govern agents at scale: MCP servers as reusable action surfaces (including a published open-source Lever MCP server), agent configuration conventions (CLAUDE.md / AGENTS.md) for multi-agent workflows, and prompt/skill versioning practices across the org.
- **AI & data architecture:** Built RAG/retrieval on Vertex AI — BigQuery vector embeddings over operational documentation and support tickets — to ground the agents; rolled out Gemini Enterprise integrated with the full application suite, delivering org-wide AI access for engineering, operations, and GTM.
- **AI platform (IAH) — 0→1 B2B SaaS:** Architected and lead IAH — a commercial multi-tenant B2B SaaS platform on Azure and GCP whose services are sold to external business customers — spanning an RFI (request-for-information) tool, a Trainer, TestBOT (automated test generation), ephemeral-infrastructure automation, and troubleshooting and informational assistants; built from concept to production.
- **MLOps / platform engineering:** Standardized Kubernetes as the control plane across GCP and Azure with GitOps-style governance; shipped Slack-native MCP servers and ADK agents for self-service ephemeral infrastructure and automated cost governance; 99.99% uptime; >$200K cloud savings on ~$2M spend.
- **AI-driven engineering productivity:** Standardized Cursor and Claude Code as the team development environment; deployed Claude Code + GitHub Copilot for automated PR review, accelerating delivery and improving review consistency.
- **Quality & compliance:** Built a Robot Framework test platform (integration/E2E/regression with pipeline gating), augmented by the in-house AI test-authoring agent — manual regression cut from days to <12 hours; spearheaded ISO 27001 and SOC 2 programs and obtained audit reports for both.

### Insulet Corporation (FDA-regulated medical devices) — Sr. Cloud Engineering Manager · Dec 2022 – Feb 2025

- Managed cloud and data-product teams (25–30 engineers) across DevOps, developer productivity, and performance engineering for a connected medical-device (diabetes care) platform; partnered with the VP of Engineering on FY2023–FY2024 roadmaps and quarterly OKRs.
- Built a performance and load-testing framework (Locust, Python) on EKS/AWS that improved cloud architecture performance 25%.
- Operated highly available Jenkins on EKS with EFS (99.9% uptime); reduced deployment errors by 15%; owned end-to-end CI/CD from branching to one-button deploy.
- Implemented SBOM generation and merge automation across ~25 microservices with CI/CD integration, supporting security and regulatory requirements; built a Python-based document automation framework for regulated change control (ECO, SBR, PCO).

### Amazon (AWS Redshift) — Lead Systems Engineer · Dec 2016 – Dec 2022

- Owned the build, CI/CD, release ecosystem, and test tooling for Redshift — one of AWS's largest-scale distributed data services — including the CI/CD servers and fully automated build/deploy across all AWS-supported regions.
- Led the team that designed and shipped a Bors-style automated merge queue, gating integration on the exact merge candidate (not just the feature branch) — eliminating broken-mainline incidents and unblocking developer velocity org-wide.
- Added metrics-driven reporting on pipeline health and developer productivity, making bottlenecks visible and driving continuous improvement across the developer workflow.

### Prosper Marketplace (regulated fintech) — Lead DevOps Engineer · Jan 2015 – Dec 2016

- Rolled out org-wide CI/CD with Jenkins; implemented containerization with Docker; managed Artifactory, SonarQube, and a Hadoop cluster on AWS (EMR).

### Pivotal Software — Member of Technical Staff · Sep 2011 – Jan 2015

- Managed CI infrastructure; migrated Perforce to Git; automated Coverity and code-coverage integration; dynamic provisioning of Linux test environments on AWS and vCloud.

## Education

- M.S., Software Engineering, San Jose State University (2011)
- B.E., Computer Engineering, Gujarat University (2009)

## Skills & Tools

- **AI & Agent Engineering:** Agent platforms & runtimes (GCP ADK); MCP servers & action frameworks; multi-agent orchestration; RAG/retrieval & semantic architectures (Vertex AI); prompt & agent-skill lifecycle management; MLOps/LLMOps; enterprise LLM rollout (Gemini Enterprise); AI-augmented development (Cursor, Claude Code, GitHub Copilot); LLM-driven testing & PR review
- **Leadership & Strategy:** Org design & hiring; distributed teams; portfolio & roadmapping; quarterly OKRs; KPI/DORA; $2–3M budget & vendor management; C-suite partnership; multi-tenant AI platform delivery
- **Platforms & Infrastructure:** AWS, GCP, Azure; Kubernetes (GKE, EKS, AKS); Terraform; Docker; GitOps; distributed systems; observability (Grafana LGTM / OpenObserve, PagerDuty) & SLOs
- **Delivery & Quality:** CI/CD (GitHub Actions, Jenkins, Bazel, Gradle); test automation (Robot Framework, Python); performance engineering (Locust); SBOM
- **Compliance & Regulated Industries:** ISO/IEC 27001, SOC 2 (audit ownership); FDA-regulated medical device software; safety-critical OT/SCADA environments; security partnering
- **Software & Data:** Python; Java/C/C#; Shell; API design; MySQL, PostgreSQL, Oracle, DynamoDB
