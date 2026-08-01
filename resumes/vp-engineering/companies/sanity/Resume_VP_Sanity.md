# Ishan Shah

San Carlos, CA • +1-925-596-8956 • ishan.hash@gmail.com

**Director, Cloud Infrastructure │ Platform & SRE Leadership │ Kubernetes, Multi-Cloud, Reliability, Cost & Trust at Scale**

> Tailored for Sanity — Director, Cloud Infrastructure (Product/SRE). Leads with platform foundations,
> reliability discipline, deployment golden paths, cost, and trust/compliance. Do not claim CDN/edge/Fastly,
> PCI/HIPAA, or a request-per-second figure. Keep facts in sync with `profile/candidate-profile.md`.

---

## Summary

Infrastructure and platform leader with 15+ years owning the foundations engineers build on: Kubernetes, multi-cloud, networking, CI/CD, observability, on-call, and incident response. I standardized Kubernetes as the control plane across GCP and Azure with GitOps-style governance and hold the platform at 99.99% uptime, with observability on the Grafana LGTM stack and PagerDuty-backed on-call. I make deployment boring — I owned the build, CI/CD, and release ecosystem for AWS Redshift, including fully automated build and deploy across every AWS region, and shipped self-service infrastructure that took provisioning off the ticket queue instead of into it. I own cloud cost discipline ($2–3M budget, ~$2M cloud, >$200K saved) and the trust requirements that make engineering quality visible (ISO 27001 and SOC 2 through third-party audit, FDA-regulated and safety-critical environments). I lead managers and senior engineers, partner directly with the C-suite, and stay in the codebase.

## Experience

### CruxOCM Inc. — VP of Engineering / Head of Automation (reporting to the CTO) · Feb 2025 – Present

- **Platform foundations:** Architected and launched the web-services platform from scratch and standardized **Kubernetes as the control plane across GCP and Azure** with GitOps-style governance, a **Kuma service mesh** (mTLS in-mesh), and infrastructure as code — **99.99% uptime** on a platform running safety-critical industrial workloads.
- **Reliability, on-call & incident response:** My team owns observability end to end on the **Grafana LGTM stack** (Loki, Grafana, Tempo, Mimir) and OpenObserve, with **PagerDuty** for alerting and on-call — logs, metrics, traces, dashboards, **SLOs**, paging standards, service ownership, and incident response.
- **Deployment golden paths:** Standardized CI/CD with pipeline gating and a Robot Framework test platform (integration/E2E/regression) so production readiness is part of shipping, not a separate step; manual regression cut from **days to under 12 hours** with an in-house test-authoring agent.
- **Platform vs. product-team ownership:** Shipped **self-service ephemeral infrastructure** through chat-native MCP servers and agents, plus automated cost governance — deliberately built as self-service so central platform work never became a ticket queue.
- **Cloud cost discipline:** Own a **$2–3M** annual budget including **~$2M** of GCP and Azure spend; drove **>$200K in savings** through right-sizing, ephemeral non-production infrastructure, scheduled shutdowns, and reserved instances, with spend attribution making tradeoffs visible.
- **Trust & compliance:** Spearheaded **ISO/IEC 27001** and **SOC 2** programs and obtained audit reports for both — controls, audit logging, and evidence that they operated, in a regulated, safety-critical environment.
- **Multi-cloud, multi-tenant delivery:** Architected **IAH** 0→1 — a commercial multi-tenant B2B SaaS platform sold to external business customers, hosted across **Azure and GCP** — including tenant isolation, per-tenant budgets, and the governance customers audit.
- **Org & strategy:** Lead a distributed organization spanning Infrastructure, DevOps, Web Services, Security, Quality, AI, and IT; partner with the CEO and CTO on the roadmap and quarterly OKRs; hire, coach, and stretch senior engineers and leads.
- **AI platform (differentiator):** Architected and operate a production AI control plane on GKE — a gateway doing authn/authz, guardrails, registration, path and model routing, per-tenant budgets and audit, in front of an orchestrator with a human-in-the-loop gate and Langfuse tracing, cost attribution and evaluations.

### Insulet Corporation (FDA-regulated medical devices) — Sr. Cloud Engineering Manager · Dec 2022 – Feb 2025

- Led **25–30 engineers** across cloud infrastructure, DevOps, developer productivity, and performance engineering for a connected medical-device platform; partnered with the VP of Engineering on roadmaps and quarterly OKRs.
- Operated **highly available Jenkins on EKS with EFS at 99.9%**; owned end-to-end CI/CD from branching to one-button deploy (Jenkins, Python, Gradle) and **reduced deployment errors 15%**.
- Built a performance and load-testing framework (**Locust**, Python) on EKS that improved cloud architecture performance **25%**.
- Implemented **SBOM** generation and merge automation across **~25 microservices** with CI/CD integration, plus automation for regulated change control — security and audit evidence as part of the pipeline.

### Amazon (AWS Redshift) — Lead Systems Engineer · Dec 2016 – Dec 2022

- Owned the build, CI/CD, release ecosystem, and test tooling for Redshift — one of AWS's largest-scale distributed data services — including the CI/CD servers and **fully automated build and deploy across every AWS-supported region**.
- **Led 7 engineers** building a Bors-style automated merge queue that gated integration on the exact merge candidate rather than the feature branch — **eliminating broken-mainline incidents** and unblocking developer velocity org-wide.
- Added metrics-driven reporting on pipeline health and developer productivity, making bottlenecks visible instead of anecdotal.

### Prosper Marketplace (regulated fintech) — Lead DevOps Engineer · Jan 2015 – Dec 2016

- Rolled out org-wide CI/CD with Jenkins and containerization with Docker; managed Artifactory versioning, SonarQube quality gates, and a Hadoop cluster on AWS (EMR).

### Pivotal Software — Member of Technical Staff · Sep 2011 – Jan 2015

- Owned CI infrastructure; migrated Perforce to Git with enforced branching policy; automated static analysis and coverage; built dynamic provisioning of Linux environments on AWS and vCloud.

## Education

- M.S., Software Engineering, San Jose State University (2011)
- B.E., Computer Engineering, Gujarat University (2009)

## Skills & Tools

- **Cloud & Platform:** GCP, AWS, Azure; Kubernetes (GKE, EKS, AKS); Terraform / infrastructure as code; Docker; GitOps; service mesh (Kuma, mTLS); gateways & routing; multi-region and multi-cloud architecture; multi-tenant SaaS
- **Reliability & Observability:** Grafana LGTM (Loki, Grafana, Tempo, Mimir), OpenObserve; PagerDuty on-call & paging standards; SLOs and error budgets; dashboards & alert severity; incident response and RCA; 99.99% uptime; performance & load engineering (Locust)
- **Delivery & Developer Experience:** CI/CD at scale (GitHub Actions, Jenkins, Bazel, Gradle); automated multi-region build/deploy; merge queues & pipeline gating; production-readiness checks; self-service platform tooling; test automation (Robot Framework, Python); SBOM; DORA metrics
- **Cost & Trust:** Cloud cost ownership and attribution ($2–3M budget, ~$2M cloud, >$200K saved); right-sizing, ephemeral infrastructure, reserved capacity; **ISO/IEC 27001** and **SOC 2** audit ownership; FDA-regulated and safety-critical environments; security partnering
- **Leadership:** Leading managers and senior technical leads; hiring, coaching and performance; distributed teams across time zones; C-suite partnership; roadmapping and quarterly OKRs; vendor management
- **Engineering:** Python; Java/C/C#; Shell; API design; PostgreSQL, MySQL, Oracle, DynamoDB; AI/agent platforms (LangGraph, MCP, Vertex AI) and AI-augmented development (Cursor, Claude Code)
