# Medtronic — Role & JD

- **Title:** Senior Cloud Engineering Manager – Enterprise Cloud Platforms
- **Track to use:** Head of Automation
- **JD link:** none — received as a PDF document, not a live posting (see ⚠️ below)
- **Job ID (as stated):** MDT-CE-48291
- **Comp range (as stated):** $280,000 – $345,000 base, "depending on experience and qualifications"
- **Location:** San Francisco Bay Area, California, United States
- **Captured:** Aug 5, 2026

## ⚠️ Verify the posting before applying

This JD arrived as a standalone PDF, not a link to Medtronic's careers site, and
several details do not match how Medtronic actually posts:

- **Job ID format.** `MDT-CE-48291` is not Medtronic's Workday requisition
  format (theirs look like `R<digits>`).
- **Location granularity.** Real Medtronic reqs name a site (Santa Rosa,
  Sunnyvale, Minneapolis). "San Francisco Bay Area" is aggregator-style.
- **Comp band.** $280–345K base is high for a Medtronic manager-level cloud/IT
  role; their posted Bay Area bands for this level typically run well below that.
  This band is closer to Bay Area big-tech senior-manager comp.
- **Boilerplate.** "Collaborative work environment", "Application Process:
  Interested candidates should submit their resume for review" — generic filler,
  not Medtronic's careers-site copy.

**Action before submitting:** find this role on `medtronic.com/careers` (or
Medtronic's Workday) and apply through the official req. If it doesn't exist
there, treat this as a reposter/aggregator listing or a fabricated posting and do
not send a resume to whatever address accompanied the PDF. **Do not set `Date
Applied` until it has been submitted through a verified Medtronic channel.**

The resume itself is worth having either way — the title match is exact, so it is
reusable for any real Medtronic or medtech cloud-platform req.

## Full JD (pasted verbatim)

> **Job Title:** Senior Cloud Engineering Manager – Enterprise Cloud Platforms
> **Location:** San Francisco Bay Area, California, United States
> **Job ID:** MDT-CE-48291
>
> ### About the Role
>
> Medtronic is seeking a Senior Cloud Engineering Manager to lead the design,
> development, and optimization of scalable cloud platforms that support
> enterprise technology initiatives across the organization. This role will focus
> on driving cloud engineering excellence, improving platform reliability, and
> enabling secure, high-performing solutions across complex technology
> environments.
>
> The ideal candidate will bring strong experience in cloud infrastructure,
> DevOps practices, engineering leadership, and automation. This individual will
> work closely with cross-functional technology teams to establish modern
> engineering practices, improve operational efficiency, and deliver solutions
> that support digital transformation initiatives.
>
> This position requires a hands-on technology leader who can guide engineering
> teams, influence technical strategy, and build reliable cloud capabilities that
> align with business objectives and regulated healthcare technology
> environments.
>
> ### Key Responsibilities
>
> - Lead and mentor cloud engineering teams responsible for designing, building,
>   and maintaining scalable cloud platforms and infrastructure solutions.
> - Define and execute cloud engineering strategies focused on reliability,
>   automation, security, and operational excellence.
> - Drive adoption of modern DevOps practices, including infrastructure-as-code,
>   continuous integration, continuous delivery, and automated testing
>   frameworks.
> - Partner with software engineering, cybersecurity, architecture, and business
>   teams to deliver enterprise cloud solutions.
> - Improve cloud platform performance, availability, monitoring, and incident
>   response capabilities.
> - Establish engineering standards, best practices, and technical guidelines
>   across cloud environments.
> - Provide technical leadership for AWS-based platforms, containerized
>   applications, and Kubernetes-driven infrastructure.
> - Evaluate emerging cloud technologies and recommend solutions that enhance
>   scalability and business value.
>
> ### Qualifications
>
> - Bachelor's degree in Computer Engineering, Computer Science, Information
>   Technology, or a related technical discipline.
> - 8+ years of experience in software engineering, cloud engineering, DevOps, or
>   infrastructure engineering roles.
> - Proven experience leading engineering teams and delivering complex technology
>   solutions.
> - Strong hands-on experience with cloud platforms such as Amazon Web Services
>   (AWS).
> - Experience with Kubernetes, Docker, Terraform, Jenkins, and automation
>   frameworks.
> - Strong programming and scripting experience with languages such as Python and
>   Bash.
> - Experience designing and supporting highly available, scalable, and secure
>   technology platforms.
> - Strong communication skills with the ability to collaborate across technical
>   and business stakeholders.
>
> ### Preferred Qualifications
>
> - Experience supporting healthcare, medical technology, or other highly
>   regulated industries.
> - Experience managing enterprise-scale cloud transformation initiatives.
> - Knowledge of cloud security practices, compliance frameworks, and
>   infrastructure governance.
> - Experience improving engineering processes through automation, performance
>   optimization, and operational maturity.
> - Advanced degree in Computer Science, Engineering, or a related technical
>   field.
>
> ### Compensation
>
> - Target salary range: $280,000 – $345,000 USD depending on experience and
>   qualifications.
> - Performance-based bonuses and additional incentives where applicable.
>
> ### Benefits
>
> - Comprehensive benefits package. Professional development opportunities.
>   Collaborative work environment. Opportunities to contribute to innovative
>   healthcare technology solutions. Employee resources supporting career growth.
>
> ### Application Process
>
> Interested candidates should submit their resume for review. Qualified
> candidates will be contacted for next steps.

## My read — keyword & priority map

**The headline fact: the title is an exact match to a role Ishan already held.**
Insulet, Dec 2022 – Feb 2025, *Sr. Cloud Engineering Manager* — at an
FDA-regulated medical device company, on AWS, running Jenkins on EKS. This is
the rare posting where the strongest evidence is the previous job title itself.
Lead with Insulet, not CruxOCM.

### Stated requirements → proof

| JD theme / keyword | Do I have it? | Which resume bullet / story proves it |
|---|---|---|
| Title: Sr. Cloud Engineering Manager | **Exact** | Insulet, *Sr. Cloud Engineering Manager*, Dec 2022 – Feb 2025 |
| Lead & mentor cloud engineering teams | Yes | Insulet: 25–30 engineers across DevOps, dev-productivity, perf engineering; Amazon: led 7 on merge-queue; CruxOCM: AI/WebSvcs/DevOps/Infra/Security/Quality/IT |
| Define & execute cloud engineering strategy | Yes | CruxOCM: own technology strategy + FY25/FY26 roadmap with CEO/CTO, quarterly OKRs; Insulet: FY23/FY24 roadmap with VP Eng |
| Reliability / availability | Yes | 99.99% platform uptime (CruxOCM K8s); Jenkins on EKS + EFS at 99.9% (Insulet) |
| Automation | Yes | Robot Framework test platform, regression days → <12h; Slack-native MCP + ADK agents for self-service ephemeral infra; Python doc-automation framework (ECO/SBR/PCO) |
| Security | Yes | ISO/IEC 27001 + SOC 2 (audit ownership); SBOM across ~25 microservices; static analysis; egress allow-listing + short-lived credentials |
| Operational excellence | Yes | Bors-style merge queue eliminated broken-mainline incidents; deployment errors −15% |
| Infrastructure-as-code | Yes | Terraform + Terragrunt in `crux-tf-infra`, YAML-config-driven, ~17 project environments across dev/qa/uat/prod/iac, GCP + Azure |
| Continuous integration / delivery | Yes | Insulet: end-to-end CI/CD, branching → one-button deploy (Jenkins, Python, Gradle); Amazon: fully automated multi-region build/deploy; Prosper: org-wide Jenkins rollout |
| Automated testing frameworks | Yes | Robot Framework integration/E2E/regression packs with pipeline gating + AI test-authoring agent; Locust performance/load framework |
| Partner w/ software eng, cybersecurity, architecture, business | Yes | ISO 27001/SOC 2 programs run with security; C-suite stakeholder management (CEO/CTO); Insulet partnered with VP Eng |
| Platform performance | Yes | Locust (Python) framework on EKS → **25%** cloud architecture performance improvement (Insulet) |
| Monitoring | Yes | Grafana LGTM stack (Loki/Grafana/Tempo/Mimir) and OpenObserve — logs, metrics, traces, dashboards, SLOs |
| Incident response | Yes | PagerDuty alerting + on-call owned by the platform team (CruxOCM) |
| Engineering standards & best practices | Yes | Amazon: owned Redshift build/CI-CD/release ecosystem + test tooling org-wide; metrics-driven pipeline-health & developer-productivity reporting |
| **AWS-based platforms** | Yes — 8 yrs | **Amazon (AWS Redshift) Dec 2016 – Dec 2022**; Insulet: EKS, ECS, Lambda, EFS; Prosper: EMR/Ambari on AWS |
| Containerized applications | Yes | Docker from Prosper (2015) forward; non-root containers (UniClaw); Docker Compose |
| Kubernetes-driven infrastructure | Yes | EKS (Insulet), GKE + AKS (CruxOCM); standardized K8s as control plane across GCP & Azure with GitOps governance |
| Evaluate emerging cloud technologies | Yes | AI control plane on GKE (Kuma mesh, Agent Gateway, LangGraph, Langfuse); Gemini Enterprise rollout; MCP servers |
| Bachelor's CE/CS/IT | Yes | B.E. Computer Engineering, Gujarat University (2009) |
| 8+ years | Yes — 15+ | career total |
| Hands-on Kubernetes, Docker, Terraform, **Jenkins**, automation | Yes | Jenkins across four companies: Pivotal (Pulse CI), Prosper (org-wide rollout), Amazon (CI/CD servers), Insulet (HA Jenkins on EKS) |
| Python and Bash | Yes | Python: FastAPI, Locust, Robot Framework, doc automation, `google-genai`; Shell/Bash scripting |
| HA, scalable, secure platforms | Yes | 99.99% uptime + ISO 27001/SOC 2 + multi-tenant IAH platform 0→1 |
| Communication across technical + business | Yes | C-suite partnering; quarterly OKRs; stakeholder management across the C-suite |

### Preferred requirements → proof

| Preferred | Do I have it? | Proof |
|---|---|---|
| **Healthcare / medical technology / regulated** | **Bullseye** | **Insulet — FDA-regulated medical devices** (Dec 2022 – Feb 2025); plus safety-critical energy OT/SCADA (CruxOCM), regulated fintech (Prosper), ISO 27001 + SOC 2 |
| Enterprise-scale cloud transformation | Yes | Amazon: automated build/deploy across all AWS-supported regions; CruxOCM: K8s standardization across GCP + Azure, ~17 project environments as code |
| Cloud security, compliance frameworks, infra governance | **Strong** | ISO/IEC 27001 + SOC 2 audit ownership; SBOM + static analysis; access-control standards; per-tenant budgets, egress allowlists, short-lived credentials |
| Improving eng processes via automation / perf / operational maturity | **Strong** | Merge queue killed broken-mainline incidents; regression days → <12h; perf +25%; deploy errors −15%; >$200K cloud savings |
| Advanced degree | Yes | M.S., Software Engineering, San Jose State University (2011) |

## Gaps / stretch areas

Honest list. Every stated requirement above is matched; these are the real soft
spots, and none of them should be papered over in the resume.

1. **No medical-device software QMS / validation experience by name.** Insulet
   was FDA-regulated, but the profile does not record 21 CFR Part 11, IEC 62304,
   GxP, or computer-system-validation (CSV) work. Medtronic will care. *How I'll
   address it:* claim FDA-regulated **environment** experience (true) and ISO
   27001/SOC 2 **audit ownership** (true) — never claim QMS or CSV ownership. Ask
   on the first call how much of this role is validated-system work.
2. **AWS is deep but not current.** AWS spans Dec 2016 – Feb 2025 (Amazon +
   Insulet), but the last 18 months at CruxOCM are GCP/Azure-primary. *How I'll
   address it:* lead the Insulet and Amazon AWS work prominently rather than
   burying it under recent GCP work; be ready to say plainly that current
   day-to-day is GCP/Azure and that the primitives transfer.
3. **"Enterprise technology initiatives" = internal enterprise IT platform.**
   Ishan's platform work is *product* platform (customer-facing SaaS), not
   internal corporate IT. *How I'll address it:* the Insulet role was internal
   cloud/data platform serving product teams, which is the closest analogue —
   frame around internal-platform-as-a-service to engineering customers.
4. **Bash named explicitly; Ishan's scripting story is Python-forward.** Minor —
   Shell is real and long-standing, just not the headline. Keep both named.
5. **Org size at Medtronic scale is unknown.** ~95K employees; the JD never says
   how many engineers this role manages, or whether it owns budget. Ask.

## Tailoring checklist
- [x] Summary rewritten to mirror JD's top 3 priorities (cloud platform leadership, DevOps/IaC/automation, regulated healthcare)
- [x] Top bullets reordered to lead with their language
- [x] Metrics that match their scale surfaced (25–30 engineers, 99.99%/99.9%, +25% perf, −15% deploy errors)
- [x] Insulet promoted above CruxOCM in emphasis — exact title + FDA-regulated + AWS
- [x] Reviewed against JD (nothing generic / buried)
- [x] PDF exported → `resumes/head-of-automation/companies/medtronic/`
- [ ] **Posting verified on Medtronic's own careers site** ← blocking, see ⚠️ above
- [ ] Submitted; `Date Applied` set in the tracker
