# Ishan Shah

San Carlos, CA • +1-925-596-8956 • ishan.hash@gmail.com

**Vice President, DevOps │ Platform Engineering, SRE & Cloud Operations │ AI-Enabled Infrastructure & AIOps**

> Tailored for Fiserv — Vice President, Dev Ops (Sunnyvale). Mirrors the JD order: enterprise DevOps/SRE/
> platform strategy → team building → CI/CD & IaC modernization → governance/standards → GenAI/AIOps applied
> to operations → SLOs & resilience → DevSecOps → budget/vendor/exec. Do not claim certifications, or years
> of Terraform/Kubernetes beyond what is real. Keep facts in sync with `profile/candidate-profile.md`.

---

## Summary

Technology leader with 15+ years across enterprise-scale engineering, infrastructure, and operations organizations, and 11+ years in lead and leadership roles spanning DevOps, platform engineering, cloud operations, and release engineering. I set and execute platform strategy end to end: Kubernetes standardized as the control plane across GCP and Azure with GitOps governance at 99.99% uptime; enterprise CI/CD modernization including fully automated build and deploy across every AWS region for AWS Redshift; observability, SLOs and PagerDuty-backed on-call and incident response; and DevSecOps with SBOM, vulnerability management and regulated change control embedded in the pipeline. I apply GenAI and AIOps to operations in production — agents for incident troubleshooting and root-cause analysis, self-service infrastructure provisioning, and automated cost governance — and I own the commercial side: a $2–3M budget including ~$2M of cloud spend, with >$200K in savings, plus vendor relationships and direct CEO/CTO partnership. Regulated-industry background across fintech, FDA-regulated medical devices, and safety-critical energy operations, with ISO/IEC 27001 and SOC 2 audit ownership.

## Experience

### CruxOCM Inc. — VP of Engineering / Head of Automation (reporting to the CTO) · Feb 2025 – Present

- **Enterprise platform strategy:** Own technology strategy across DevOps, Infrastructure, Web Services, Security, Quality, AI, and IT for an industrial automation platform in safety-critical, regulated energy environments; partner with the CEO and CTO on the multi-year roadmap and quarterly OKRs.
- **Cloud-native platform & cloud operations:** Architected and launched the platform from scratch; standardized **Kubernetes as the control plane across GCP and Azure** with GitOps-style governance, a **Kuma service mesh** (mTLS in-mesh), and **Terraform/Terragrunt** infrastructure as code covering every environment — **99.99% uptime**.
- **Reliability engineering & resilience:** Defined **SLOs**, alert severity and paging standards, service ownership, and incident response; observability on the **Grafana LGTM stack** (Loki, Grafana, Tempo, Mimir) and OpenObserve with **PagerDuty** on-call rotations, dashboards, and RCA discipline.
- **GenAI / AIOps applied to operations:** Shipped production agents that automate operational work — an AI troubleshooting agent that accelerates root-cause analysis and incident resolution, self-service ephemeral infrastructure provisioning through chat-native MCP servers, and automated cost governance (scheduled non-production shutdowns, reserved capacity) — eliminating manual operations tickets rather than routing them.
- **AI control plane (MLOps/LLMOps):** Architected and operate a production AI control plane on GKE — a gateway providing authentication, authorization, guardrails, service registration, path and model routing, per-tenant budgets and audit, fronting an orchestrator with a human-in-the-loop approval gate, with Langfuse for tracing, cost attribution, and model evaluation.
- **CI/CD & engineering standards:** Standardized CI/CD with pipeline gating and a Robot Framework test platform (integration/E2E/regression), augmented by an AI test-authoring agent — manual regression reduced from **days to under 12 hours**; established engineering standards and conventions for AI-assisted development across the org (Cursor, Claude Code, GitHub Copilot for automated PR review).
- **DevSecOps & compliance:** Partner with security leadership on automated controls, audit logging, and compliance in the SDLC; spearheaded **ISO/IEC 27001** and **SOC 2** programs and obtained audit reports for both.
- **Budget, vendors & executive partnership:** Own a **$2–3M** annual budget including **~$2M** of GCP and Azure spend; delivered **>$200K in savings** through right-sizing, ephemeral infrastructure, and reserved capacity, with spend attribution making tradeoffs visible to the executive team.
- **Team building:** Hire, coach, and develop engineers across DevOps, infrastructure, and quality in a distributed organization; set the performance bar and the standards the team works to.

### Insulet Corporation (FDA-regulated medical devices) — Sr. Cloud Engineering Manager · Dec 2022 – Feb 2025

- Built and led cloud infrastructure, DevOps, developer productivity, and performance engineering teams — **25–30 engineers** — for a connected medical-device platform; partnered with the VP of Engineering on roadmaps and quarterly OKRs.
- Drove **enterprise CI/CD modernization**: owned end-to-end delivery from branching to one-button deploy (Jenkins, Python, Gradle) and **reduced deployment errors 15%**; operated **highly available Jenkins on EKS with EFS at 99.9%**.
- Built a performance and load-testing framework (**Locust**, Python) on EKS/AWS that improved cloud architecture performance **25%**; established capacity and performance baselines.
- Implemented **SBOM** generation and merge automation across **~25 microservices** with CI/CD integration, supporting vulnerability management and regulatory requirements; automated regulated change control.

### Amazon (AWS Redshift) — Lead Systems Engineer · Dec 2016 – Dec 2022

- Owned the build, CI/CD, release ecosystem, and test tooling for Redshift — one of AWS's largest-scale distributed data services — including the CI/CD servers and **fully automated build and deploy across every AWS-supported region**: enterprise-wide CI/CD adoption and release management at global scale.
- **Led a team of 7 engineers** delivering a Bors-style automated merge queue that gated integration on the exact merge candidate rather than the feature branch — **eliminating broken-mainline incidents** and unblocking developer velocity org-wide.
- Established metrics-driven reporting on pipeline health and developer productivity, making bottlenecks visible and driving continuous operational improvement.

### Prosper Marketplace (regulated fintech) — Lead DevOps Engineer · Jan 2015 – Dec 2016

- Led org-wide CI/CD rollout with Jenkins and containerization with Docker; managed Artifactory versioning, SonarQube quality gates, and a Hadoop cluster on AWS (EMR) in a regulated financial-services environment.

### Pivotal Software — Member of Technical Staff · Sep 2011 – Jan 2015

- Owned CI infrastructure and its agents; migrated Perforce to Git with enforced branching and merge policy; automated static analysis and code-coverage aggregation; built dynamic provisioning of Linux environments on AWS and vCloud.

## Education

- M.S., Software Engineering, San Jose State University (2011)
- B.E., Computer Engineering, Gujarat University (2009)

## Skills & Tools

- **DevOps, Platform & Cloud Operations:** Enterprise DevOps and platform strategy; cloud-native platform design on **AWS, Azure, GCP**; **Kubernetes** (GKE, EKS, AKS) and containers; **Terraform/Terragrunt**, infrastructure as code; GitOps; service mesh (Kuma, mTLS); environment and release management; multi-region and multi-cloud architecture
- **CI/CD & Delivery Engineering:** Enterprise CI/CD adoption at scale (GitHub Actions, Jenkins, Bazel, Gradle); automated multi-region build and deploy; merge queues and pipeline gating; test automation (Robot Framework, Python); DORA metrics; developer productivity and internal platform tooling
- **SRE & Reliability:** SLOs/SLAs/KPIs; observability standards (**Grafana LGTM**, OpenObserve); **PagerDuty** on-call and incident response; RCA; disaster-recovery readiness and technology resilience; capacity and performance engineering (Locust); 99.99% uptime
- **AI, GenAI & AIOps:** GenAI and agent-based automation for incident troubleshooting/RCA, provisioning, and cost governance; MLOps/LLMOps (model routing, evaluation, tracing, cost attribution — Langfuse, Vertex AI, LangGraph, MCP); enterprise LLM rollout; AI-assisted development standards (Cursor, Claude Code, GitHub Copilot)
- **DevSecOps & Compliance:** Automated security controls and audit logging; SBOM and vulnerability management; regulated change control; **ISO/IEC 27001** and **SOC 2** audit ownership; FDA-regulated and safety-critical environments; security partnering
- **Leadership & Commercial:** Building and developing DevOps/SRE/platform teams; hiring, coaching and performance management; distributed teams; **$2–3M** budget and vendor management; executive and C-suite partnership; roadmapping and quarterly OKRs
- **Engineering:** Python; Java/C/C#; Shell; API design; PostgreSQL, MySQL, Oracle, DynamoDB
