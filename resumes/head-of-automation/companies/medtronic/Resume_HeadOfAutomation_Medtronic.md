# Ishan Shah

San Carlos, CA • +1-925-596-8956 • ishan.hash@gmail.com

**Cloud & Platform Engineering Leader │ Enterprise Cloud Platforms, DevOps & Automation │ AWS · Kubernetes · Terraform · FDA-Regulated Environments**

---

## Summary

Hands-on engineering leader with 15+ years building and running scalable cloud platforms — including over two years as a **Sr. Cloud Engineering Manager inside an FDA-regulated medical device company**, leading 25–30 engineers across DevOps, developer productivity, and performance engineering on AWS. I define and execute cloud engineering strategy around reliability, automation, security, and operational excellence: infrastructure-as-code with Terraform, end-to-end CI/CD, automated testing frameworks, and the monitoring and incident response that hold platforms at 99.99% uptime. Eight years of hands-on AWS — Amazon's Redshift build and release ecosystem, then EKS, ECS, and Lambda at Insulet — plus Kubernetes and Docker across EKS, GKE, and AKS. I own ISO/IEC 27001 and SOC 2 audit programs, manage multi-million-dollar cloud budgets, mentor engineers, and partner across software engineering, security, and architecture to set the standards that make delivery faster and safer.

## Experience

### CruxOCM Inc. — Head of Automation (reporting to the CTO) · Feb 2025 – Present

- **Scope & leadership:** Own technology strategy across Web Services, DevOps, Infrastructure, Security, Quality, AI, and IT; lead and mentor a distributed engineering org, partner with the CEO and CTO on the FY2025–FY2026 roadmap, and run quarterly OKRs. Safety-critical energy operations (pipeline SCADA/OT).
- **Cloud platform & Kubernetes:** Architected and launched a hybrid web-services platform from scratch and led the transformation that standardized **Kubernetes** as the control plane across **GCP and Azure** (GKE, AKS) with Docker and GitOps-style governance, sustaining **99.99% uptime**.
- **Infrastructure-as-code:** Provision the estate as code with **Terraform and Terragrunt** — a YAML-config-driven repository covering roughly **17 project environments** across dev, QA, UAT, prod, and IaC, spanning GCP and Azure, with per-workload service accounts and secret-manager-backed configuration.
- **CI/CD & engineering standards:** Own CI/CD and release governance across **GitHub Actions, Jenkins, a Bazel monorepo, and Gradle**; set the engineering standards, code-review practices, and technical guidelines the org builds against.
- **Reliability, monitoring & incident response:** Team owns observability on the **Grafana LGTM stack** (Loki, Grafana, Tempo, Mimir) and OpenObserve — logs, metrics, traces, dashboards, and SLOs — with **PagerDuty** alerting and an on-call rotation driving incident response.
- **Automated testing:** Built a **Robot Framework** test platform for integration, E2E, and regression packs with pipeline gating, augmented by an in-house test-authoring agent — cut manual regression from days to **under 12 hours**.
- **Security & compliance:** Spearheaded **ISO/IEC 27001 and SOC 2** programs and obtained audit reports for both, partnering with security, architecture, and business stakeholders across the company; drove SBOM generation, static-analysis scanning, and access-control standards.
- **Budget & cost optimization:** Own a **$2–3M** annual team budget including **~$2M** in GCP and Azure cloud spend; delivered **>$200K** in savings through right-sizing, reserved instances, and automated shutdown of ephemeral non-production infrastructure.
- **Evaluating emerging cloud technology:** Put a governed AI platform layer into production on GKE — service mesh with mTLS, a gateway enforcing authN/authZ and per-tenant budgets, egress allow-listing with short-lived credentials, and full trace and cost observability — plus Slack-based self-service infrastructure automation.

### Insulet Corporation — Sr. Cloud Engineering Manager · Dec 2022 – Feb 2025

*FDA-regulated medical device manufacturer (insulin delivery systems).*

- **Team & scope:** Managed cloud and data-product teams of **25–30 engineers** across DevOps, developer-productivity tooling, and performance engineering; partnered with the VP of Engineering on the FY2023 and FY2024 roadmap and ran quarterly OKRs.
- **AWS platform:** Ran the service estate on **AWS** — **EKS** for containerized workloads, **ECS** for services, and **Lambda** for event-driven and short-lived jobs — designing for high availability, scalability, and security in a regulated environment.
- **CI/CD & operational maturity:** Owned end-to-end CI/CD from branching strategy to one-button deploy using **Jenkins, Python, and Gradle**, operating highly available **Jenkins on EKS with EFS at 99.9% uptime** and cutting deployment errors by **15%**.
- **Performance engineering:** Built a performance and load-testing framework (**Locust**, Python) on EKS that improved cloud architecture performance by **25%**.
- **Supply-chain security & automation:** Implemented **SBOM** generation and merge automation across roughly **25 microservices**, integrated into CI/CD.
- **Change-control automation:** Developed a Python framework automating engineering change documentation (ECO, SBR, PCO) within the company's regulated change-control process.

### Amazon (AWS Redshift) — Lead Systems Engineer · Dec 2016 – Dec 2022

- Owned the build, CI/CD, release ecosystem, and test tooling for **Redshift on AWS** — including the CI/CD servers and fully automated build and deploy across **all AWS-supported regions**, at enterprise scale.
- **Led a team of 7 engineers** that designed and shipped a Bors-style automated **merge queue**, gating integration on the exact merge candidate rather than the feature branch — eliminating broken-mainline incidents and unblocking developer velocity org-wide.
- Added metrics-driven reporting on pipeline health and developer productivity, making bottlenecks visible and driving continuous improvement across the developer workflow.

### Prosper Marketplace — Lead DevOps Engineer · Jan 2015 – Dec 2016

*Regulated consumer-lending fintech.*

- Rolled out org-wide CI/CD with **Jenkins**; implemented containerization with **Docker** and a private registry; stood up Artifactory for microservice versioning and SonarQube for static analysis.
- Managed a Hadoop cluster on AWS (EMR, Ambari) for data processing.

### Pivotal Software — Member of Technical Staff · Sep 2011 – Jan 2015

- Managed the CI server and its agents; migrated Perforce to Git with Jira-enforced hooks; automated Coverity static analysis and code-coverage aggregation in CI; provisioned Linux test environments dynamically on AWS and vCloud.

## Education

- M.S., Software Engineering, San Jose State University (2011)
- B.E., Computer Engineering, Gujarat University (2009)

## Skills & Tools

- **Cloud & Containers:** **AWS** (EKS, ECS, Lambda, EFS, EMR, Redshift), GCP, Azure; **Kubernetes** (EKS, GKE, AKS), **Docker**, service mesh (mTLS), GitOps; hybrid/multi-cloud, highly available and secure platform design
- **Infrastructure-as-Code & CI/CD:** **Terraform**, Terragrunt, **Jenkins**, GitHub Actions, Bazel monorepo, Gradle; branching strategy through one-button deploy; release governance
- **Automation & Quality:** Test-automation frameworks (**Robot Framework**, Python); performance and load testing (Locust); SBOM generation; merge-queue and change-control automation; AI-augmented development (Cursor, Claude Code, GitHub Copilot)
- **Reliability & Operations:** Observability on the Grafana LGTM stack (Loki, Grafana, Tempo, Mimir) and OpenObserve; SLOs, dashboards, alerting; **PagerDuty** on-call and incident response; 99.99% uptime
- **Security, Compliance & Regulated Environments:** **ISO/IEC 27001 and SOC 2** (audit ownership); static-analysis scanning; access-control standards; infrastructure governance, egress allow-listing, short-lived credentials; **FDA-regulated medical devices** (Insulet), safety-critical energy OT/SCADA (CruxOCM), regulated fintech (Prosper)
- **Programming & Data:** **Python** (FastAPI, Locust, automation tooling), **Bash**/Shell, Java, C/C#; API design; PostgreSQL, MySQL, Oracle, DynamoDB
- **Leadership:** Org design, hiring, and mentoring; technical strategy and roadmapping; quarterly OKRs; KPI/DORA metrics; multi-million-dollar budget ownership; cross-functional partnering with security, architecture, product, and the C-suite
