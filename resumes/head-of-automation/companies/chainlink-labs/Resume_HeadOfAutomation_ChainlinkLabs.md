# Ishan Shah

San Carlos, CA • +1-925-596-8956 • ishan.hash@gmail.com

**Engineering Leader │ Internal Infrastructure Platforms & Kubernetes at Scale │ CI/CD, Reliability (SLOs) & SOC 2 / ISO 27001 Compliance**

---

## Summary

Infrastructure and platform leader with 15+ years building and operating the internal infrastructure platforms that power engineering velocity. I've built Kubernetes-based platforms from the ground up on public cloud (AWS, GCP, Azure), delivered self-service provisioning that takes teams from idea to production faster without sacrificing control, and held the line at 99.99% reliability with SLOs and blameless incident response. I own security and compliance end to end — ISO 27001 and SOC 2 (audit ownership) — with access-control and provisioning standards, and secure CI/CD foundations built on encrypted secrets, artifact management, and supply-chain scanning. I've done this in lean, high-ambiguity startup environments, leading distributed, remote-first teams that I hire, develop, and retain.

## Experience

### CruxOCM Inc. — Head of Automation (reporting to the CTO) · Feb 2025 – Present

- **Infrastructure platform & team leadership:** Lead a distributed, remote-first engineering org across platform, infrastructure, DevOps, security, and quality in a lean startup environment; hire, develop, and retain engineers and leads, set the technical bar, and own strategy and OKRs amid ambiguity.
- **Kubernetes-based internal platform (built ground-up):** Architected a web-services platform from scratch and standardized Kubernetes as the control plane across GCP and Azure — multi-tenant, GitOps-governed clusters with Terraform infrastructure-as-code — plus self-service, ephemeral environments ("paved roads") that let teams provision and operate efficiently, speeding idea → production and measured as DORA metrics.
- **Observability & incident response:** Own platform observability on the Grafana LGTM stack (Loki/Grafana/Tempo/Mimir) and/or OpenObserve with PagerDuty — logs, metrics, traces, SLOs, and blameless on-call/incident response and RCA at 99.99% uptime; own ~$2M cloud spend with >$200K saved.
- **Secure CI/CD & compliance:** Own CI/CD across GitHub Actions, Jenkins, Bazel (monorepo), and Gradle with pipeline gating, artifact management, and encrypted secrets; drove ISO 27001 and SOC 2 programs (audit ownership) with access-control and provisioning standards, SBOM, and static-analysis scanning to minimize operational and supply-chain risk.
- **AI agents & platform:** Shipped production AI agents on GCP ADK — miniBOT, a Gemini multi-agent assistant grounded by RAG over BigQuery vector embeddings on Vertex AI, and TestBOT, which auto-generates tests — plus reusable MCP servers (a published open-source Lever MCP server + Slack-native) as action surfaces on the platform.
- **AI-driven engineering productivity:** Rolled out Gemini Enterprise across the org and standardized Cursor/Claude Code + GitHub Copilot for automated PR review, applying AI to accelerate delivery, with build-vs-buy vendor assessment.

### Insulet Corporation (FDA-regulated medical devices) — Sr. Cloud Engineering Manager · Dec 2022 – Feb 2025

- Led cloud and data-product teams (25–30 engineers) across platform, DevOps, developer productivity, and performance engineering; partnered with the VP of Engineering on multi-year roadmaps and quarterly OKRs.
- Owned end-to-end CI/CD with gating and one-button deploy (Jenkins, Python, Gradle); operated highly available Jenkins on EKS/EFS (99.9% uptime) and cut deployment errors 15%.
- Built a performance and load-testing framework (Locust, Python) on EKS/AWS (25% improvement); implemented SBOM generation and regulated change control for data integrity and supply-chain security.

### Amazon (AWS Redshift) — Lead Systems Engineer · Dec 2016 – Dec 2022

- Owned the build, CI/CD, release ecosystem, and test tooling for Redshift — one of AWS's largest-scale distributed data services — including the CI/CD servers and fully automated build/deploy across all AWS-supported regions.
- Led the team that designed and shipped a Bors-style automated merge queue, gating integration on the exact merge candidate (not just the feature branch) — eliminating broken-mainline incidents and unblocking developer velocity org-wide.
- Added metrics-driven reporting on pipeline health and developer productivity, making bottlenecks visible and driving continuous improvement across the developer workflow.

### Prosper Marketplace (regulated fintech) — Lead DevOps Engineer · Jan 2015 – Dec 2016

- Rolled out org-wide CI/CD with Jenkins and containerization with Docker; managed Artifactory artifact/versioning, SonarQube static-analysis quality gates, and a Hadoop cluster on AWS (EMR).

### Pivotal Software — Member of Technical Staff · Sep 2011 – Jan 2015

- Managed CI infrastructure and agents; migrated Perforce to Git with enforced branching/merge policy; automated Coverity static analysis and code-coverage; built dynamic provisioning of Linux environments across AWS and vCloud.

## Open Source

### UniClaw · [github.com/uniclaw-labs/uniclaw](https://github.com/uniclaw-labs/uniclaw)

- Architected and shipped UniClaw, an open-source AI agent platform — a multi-provider framework on a FastAPI (Python) backend and a React / TypeScript app, with a security-first design: OAuth2 authorization server with scoped JWTs, rate limiting, Fernet-encrypted secrets, and non-root containers; 4,400+ automated tests across a polyglot codebase (Python, TypeScript, Rust) with Dockerized orchestration. Also publish an open-source Lever MCP server.

## Education

- M.S., Software Engineering, San Jose State University (2011)
- B.E., Computer Engineering, Gujarat University (2009)

## Skills & Tools

- **Infrastructure Platforms & Cloud:** Internal infrastructure / developer platforms; Kubernetes (EKS, GKE, AKS) built ground-up; multi-tenant clusters; AWS, GCP, Azure; Docker; Terraform (IaC); self-service provisioning
- **CI/CD & Delivery:** GitHub Actions, Jenkins, Bazel (monorepo), Gradle; GitOps; merge-queue & release governance; CI runners; secrets management; secure artifact management (Artifactory)
- **Reliability & Operations:** Observability (Grafana LGTM / OpenObserve, PagerDuty); SLOs; incident management & blameless RCA; 99.99% reliability; cloud networking; capacity & cost efficiency
- **Security & Compliance:** ISO 27001 & SOC 2 / SOC 2 Type 2 (audit ownership); access control & provisioning standards; SBOM & static-analysis scanning; encrypted secrets; supply-chain security
- **AI & Automation:** AI agents (GCP ADK) & MCP servers; RAG / retrieval (Vertex AI); enterprise AI rollout (Gemini Enterprise); AI-assisted development (Cursor, Claude Code, GitHub Copilot)
- **Leadership:** Building, hiring, developing & retaining distributed remote-first teams; startup / high-ambiguity delivery; standards & architecture review; roadmaps & OKRs; ~$2–3M budget & vendor management
- **Software & Data:** Python; Java/C/C#; Bash; SQL/NoSQL (MySQL, PostgreSQL, Oracle, DynamoDB); API design
