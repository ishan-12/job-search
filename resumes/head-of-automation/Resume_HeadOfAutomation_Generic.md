# Ishan Shah

San Carlos, CA • +1-925-596-8956 • ishan.hash@gmail.com

**Head of Automation │ AI Engineering, Platform & DevOps Leadership**

> Generic / base Head-of-Automation resume. Source of truth for the HoA track. Do not tailor this file —
> copy it into `companies/<company>/` and tailor there. Keep facts in sync with `profile/candidate-profile.md`.

---

## Summary

Engineering leader with 15+ years scaling high-impact teams across AI, Platform, Infrastructure, DevOps, and Quality. Track record of shipping production AI agents and platforms from scratch, owning multi-million dollar cloud budgets, and partnering directly with the C-suite to define AI strategy, OKRs, and operating cadences. Hands-on across AI-driven engineering workflows (Cursor, Claude Code, GitHub Copilot, Gemini Enterprise), AI agent frameworks (GCP ADK), AWS/GCP/Azure, Kubernetes, and CI/CD; now focused on AI engineering, org design, and cross-functional outcomes.

## Experience

### CruxOCM Inc. — Head of Automation (reporting to the CTO) · Feb 2025 – Present

- **Scope & org:** Oversee technology strategy across AI, Web Services, DevOps, Infrastructure, Security, Quality, and IT; partner directly with the CEO and CTO on the FY2025 and FY2026 AI and engineering roadmap and run quarterly OKRs.
- **AI strategy & enterprise rollout:** Defined and executed Crux's enterprise AI strategy in partnership with the CEO and CTO; rolled out Gemini Enterprise integrated with Crux's full application suite, providing org-wide AI access for engineering, operations, and GTM teams.
- **AI agents (production):** Architected and shipped two production agents on GCP ADK — a troubleshooting agent for the flagship pipebot (faster root-cause analysis, incident resolution) and a Robot Framework test-authoring agent that auto-generates test cases.
- **AI-driven engineering productivity:** Standardized Cursor and Claude Code as the team development environment; deployed Claude Code + GitHub Copilot for automated PR review, accelerating delivery and improving code-review consistency.
- **AI-driven DevOps (MCP + agents):** Shipped Slack-native MCP servers and GCP ADK agents for self-service ephemeral infrastructure and automated cost governance (scheduled non-prod shutdowns + reserved instances), eliminating manual ops tickets and driving cloud savings.
- **AI control plane (in build):** Architecting a production-hardened AI control plane on GKE with a Kuma service mesh (mTLS) — an Agent Gateway (AuthN/AuthZ, guardrails, agent/MCP registration, path & model routing, budgets, audit) fronting a LangGraph supervisor orchestrator with a human-in-the-loop approval gate, MCP backends with egress allow-listing and short-lived credentials, and Langfuse observability (traces, tokens, cost, evaluations).
- **Budget & cloud:** Own $2–3M annual team budget including ~$2M in GCP and Azure cloud spend; achieved >$200K in savings through right-sizing and ephemeral infrastructure.
- **Platform:** Architected and launched a web-services hybrid platform from scratch; standardized Kubernetes as the control plane across GCP & Azure with GitOps-style governance; uptime 99.99%.
- **Quality engineering:** Built a Robot Framework–based test platform enabling integration/E2E/regression packs with pipeline gating, now augmented by the in-house AI test-authoring agent; reduced manual regression from days to <12 hours.
- **Cost & compliance:** Spearheaded ISO and SOC 2 compliance efforts and obtained audit reports for both.

### Insulet Corporation — Sr. Cloud Engineering Manager · Dec 2022 – Feb 2025

- Managed cloud and data-product teams (25–30 engineers) across DevOps, developer productivity tools, and performance engineering, partnering with the VP of Engineering on FY2023 and FY2024 roadmap and run quarterly OKRs.
- Built a performance and load-testing framework (Locust, Python) on EKS that improved cloud architecture performance 25%.
- Operated highly available Jenkins on EKS with EFS (99.9% uptime) and reduced deployment errors by 15%.
- Owned end-to-end CI/CD (branching to one-button deploy) using Jenkins, Python, and Gradle.
- Developed a Python-based document automation framework (ECO, SBR, PCO).
- Implemented SBOM generation and merge automation across ~25 microservices with CI/CD integration.

### Amazon (AWS Redshift) — Lead Systems Engineer · Dec 2016 – Dec 2022

- Owned the build, CI/CD, release ecosystem, and test tooling for Redshift on AWS — including the CI/CD servers and fully automated build/deploy across all AWS-supported regions.
- Led the team that designed and shipped a Bors-style automated merge queue, gating integration on the exact merge candidate (not just the feature branch) — eliminating broken-mainline incidents and unblocking developer velocity org-wide.
- Added metrics-driven reporting on pipeline health and developer productivity, making bottlenecks visible and driving continuous improvement across the developer workflow.

### Prosper Marketplace — Lead DevOps Engineer · Jan 2015 – Dec 2016

- Rolled out org-wide CI/CD with Jenkins; implemented containerization with Docker and Docker registry.
- Managed Git, Bitbucket, and GitHub; set up Artifactory for microservice versioning and SonarQube for static analysis.
- Managed Hadoop Cluster on AWS (EMR & Ambari) for data processing.

### Pivotal Software — Member of Technical Staff · Sep 2011 – Jan 2015

- Managed and maintained the CI server (Pulse) and its agents.
- Administered Perforce and Git; migrated Perforce to Git with Jira-enforced hooks.
- Automated Coverity integration in CI; automated code-coverage aggregation for unit and functional tests.
- Worked on dynamic provisioning of Linux environments for test runs on AWS and vCloud.

## Education

- M.S., Software Engineering, San Jose State University (2011)
- B.E., Computer Engineering, Gujarat University (2009)

## Skills & Tools

- **AI Engineering:** AI agents & MCP servers (GCP ADK); Enterprise AI rollout (Gemini Enterprise); AI-augmented dev (Cursor, Claude Code, GitHub Copilot); LLM-driven testing & PR review
- **Leadership & Strategy:** Org design & hiring; Portfolio & roadmapping; Quarterly OKRs; KPI/DORA; Budget & vendor mgmt; Risk & compliance partnering
- **Platforms & Infrastructure:** Kubernetes (GKE, EKS, AKS), Terraform, Docker, GitOps patterns, AWS, GCP, Azure
- **Delivery & Quality:** CI/CD (GitHub Actions, Jenkins, Bazel, Gradle); Test automation (Robot Framework, Python); Performance engineering (Locust); SBOM
- **Software & Data:** Python; Java/C/C#; Shell; API design; Databases (MySQL, PostgreSQL, Oracle, DynamoDB); Observability (Grafana LGTM / OpenObserve, PagerDuty) & SLOs
