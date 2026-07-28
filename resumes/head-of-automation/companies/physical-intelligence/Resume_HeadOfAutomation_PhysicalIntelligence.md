# Ishan Shah

San Carlos, CA • +1-925-596-8956 • ishan.hash@gmail.com

**Build & Release / DevOps Engineering │ CI/CD (GitHub Actions), Bazel Monorepo Builds, Kubernetes & Terraform │ Developer Productivity at Scale**

---

## Summary

Build, release, and developer-productivity engineer with 15+ years designing and operating CI/CD and build systems at scale. I own GitHub-based CI/CD (GitHub Actions, checks, workflows) and Bazel monorepo builds across polyglot codebases (C++, Python, Rust, TypeScript), run Kubernetes services and infrastructure with Terraform, and replace manual workflows with self-service, GitHub-integrated automation. I have a track record of reducing build failures, deploy issues, and CI bottlenecks that slow teams down — including designing an automated merge queue for one of AWS's largest distributed services — with strong developer-experience instincts and an internal-developer-platform mindset. Hands-on and security-minded, I keep pipelines fast, reliable, and safe.

## Experience

### CruxOCM Inc. — VP of Engineering / Head of Automation (reporting to the CTO) · Feb 2025 – Present

- **CI/CD & build systems:** Own CI/CD across GitHub Actions (checks, workflows), Jenkins, Bazel (monorepo), and Gradle — pipeline gating, reliability, and speed — and manage and evolve the Bazel-based build system supporting a polyglot codebase (Python, TypeScript, Rust).
- **Kubernetes & Terraform:** Build and maintain Kubernetes services and infrastructure with Terraform (IaC) across GCP and Azure, with GitOps governance and self-service, GitHub-integrated ephemeral environments that replace manual workflows.
- **Developer productivity:** Reduce build failures, deploy issues, and CI bottlenecks that affect team velocity — pipeline-health and DORA metrics with dashboards, plus merge-gating discipline — and partner with engineers across the stack on build optimization.
- **Security-focused automation:** Bake security into the pipeline — SBOM generation, static-analysis scanning, and encrypted secrets — and drove ISO 27001 and SOC 2 (audit ownership).
- **Automation & AI tooling:** Build automation that eliminates manual toil, including production AI agents (GCP ADK) and MCP servers, plus standardized Cursor/Claude Code + GitHub Copilot for automated PR review.
- **Team:** Hire and mentor engineers and partner cross-functionally with product and security.

### Amazon (AWS Redshift) — Lead Systems Engineer · Dec 2016 – Dec 2022

- Owned the build, CI/CD, release ecosystem, and test tooling for Redshift — one of AWS's largest-scale distributed data services (C++ codebase) — including the CI/CD servers and fully automated build/deploy across all AWS-supported regions.
- Designed and shipped a Bors-style automated merge queue, gating integration on the exact merge candidate (not just the feature branch) — eliminating broken-mainline incidents and build failures and unblocking developer velocity org-wide.
- Added metrics-driven reporting on pipeline health and developer productivity, making build/CI bottlenecks visible and driving continuous improvement across the developer workflow.

### Insulet Corporation (FDA-regulated medical devices) — Sr. Cloud Engineering Manager · Dec 2022 – Feb 2025

- Owned end-to-end CI/CD with gating and one-button deploy (Jenkins, Python, Gradle); operated highly available Jenkins on EKS/EFS (99.9% uptime) and cut deployment errors 15%.
- Built a performance and load-testing framework (Locust, Python) on EKS/AWS (25% improvement); implemented SBOM generation and regulated change control for supply-chain security.
- Led cloud and data-product teams (25–30 engineers) across DevOps, developer productivity, and performance engineering.

### Prosper Marketplace (regulated fintech) — Lead DevOps Engineer · Jan 2015 – Dec 2016

- Rolled out org-wide CI/CD with Jenkins and containerization with Docker; managed Artifactory artifact/versioning and SonarQube static-analysis quality gates on AWS.

### Pivotal Software — Member of Technical Staff · Sep 2011 – Jan 2015

- Managed CI infrastructure and agents; migrated Perforce to Git with enforced branching/merge policy; automated static analysis and code-coverage; built dynamic provisioning of Linux build/test environments on AWS and vCloud.

## Open Source

### UniClaw · [github.com/uniclaw-labs/uniclaw](https://github.com/uniclaw-labs/uniclaw)

- Architected and shipped UniClaw, an open-source AI agent platform across a **polyglot codebase (Python, TypeScript, Rust)** — a FastAPI (Python) backend and a Tauri (Rust) + React/TypeScript desktop app — with **4,400+ automated tests**, Dockerized multi-service orchestration, and a security-first design (OAuth2 with scoped JWTs, Fernet-encrypted secrets, non-root containers). Also publish an open-source Lever MCP server.

## Education

- M.S., Software Engineering, San Jose State University (2011)
- B.E., Computer Engineering, Gujarat University (2009)

## Skills & Tools

- **CI/CD & Build Systems:** GitHub Actions (checks, workflows), Jenkins; **Bazel (monorepo)**, Gradle; build optimization & caching; merge-queue & release governance; artifact management (Artifactory); reproducible builds
- **Cloud, Kubernetes & IaC:** Kubernetes (EKS, GKE, AKS); **Terraform**; Docker; GitOps; AWS, GCP, Azure; self-service ephemeral environments
- **Developer Productivity & Platform:** Internal developer platforms; developer-experience tooling; DORA metrics & pipeline-health dashboards; reducing build failures & CI bottlenecks; automation of manual workflows
- **Languages (polyglot builds):** C++, Python, Rust, TypeScript, Java, Bash — build/release across mixed-language codebases
- **Security & Reliability:** Security-focused infra automation (SBOM, static-analysis scanning, encrypted secrets); ISO 27001 / SOC 2; observability (Grafana LGTM / OpenObserve, PagerDuty); SLOs; 99.99% reliability
- **AI & Automation:** AI agents (GCP ADK) & MCP servers; AI-assisted development (Cursor, Claude Code, GitHub Copilot)
