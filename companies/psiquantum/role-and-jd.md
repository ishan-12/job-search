# PsiQuantum — Director, Compute Platforms & AI

- **Resume:** `resumes/head-of-automation/companies/psiquantum/Resume_HeadOfAutomation_PsiQuantum.md` (HoA track)
- **Track:** Head of Automation — the role is compute-platform strategy + **dev infrastructure (CI/CD, artifact
  mgmt)** + **observability** + **generative-AI tool adoption/enablement** + infra standards + team leadership.
  That is the HoA track's core ("AI Engineering, Platform & DevOps Leadership") — a better fit than the VP
  "agent-platform builder" framing, even though it's a Director-level leadership role.
- **Link:** https://www.psiquantum.com/apply?gh_jid=7730800003 (Greenhouse; board token `psiquantum`)
- **Comp:** Bay Area $215,000–$255,000 (US range $185,000–$215,000).
- **Location:** Milpitas, CA. **Department:** IT. **Reports to:** Chief Information & Security Officer (CISO).

## The Role (from the JD)

Lead compute-platform strategy across **cloud, on-premises, and HPC** environments. Combines strategic oversight
with hands-on technical engagement.

**Key responsibilities:**
- Define/drive strategy for compute platforms spanning **AWS, Azure, and on-prem/HPC** systems.
- Lead **evaluation and adoption of generative AI tools** across engineering and business workflows.
- Oversee cloud + HPC capabilities incl. **development infrastructure and observability**.
- Drive **performance optimization, capacity planning, and operational excellence**.
- Lead complex system issue **resolution and remediation**.
- Establish **infrastructure standards and best practices** across teams.
- Provide **technical leadership and mentorship**.

**Required:**
- **10+ yrs** designing, building, operating complex infrastructure systems.
- Strong **development infrastructure (CI/CD, artifact management)** expertise.
- Deep **observability** (metrics, logging, tracing, alerting).
- Hands-on **Linux, networking, storage, distributed systems**.
- Leading complex technical initiatives across teams; building high-performing teams in demanding environments.

**Preferred:**
- Evaluating/implementing **generative AI tools** in enterprise; operational/**security/cost** considerations
  for AI adoption; strong comms with technical + executive stakeholders.

## My read — keyword / priority map

| Theme | Fit | Proof |
|---|---|---|
| Compute-platform strategy across cloud (AWS/Azure) | ✅ | AWS (Redshift/EKS), K8s across GCP/Azure, hybrid web-services platform; Terraform |
| **Dev infrastructure — CI/CD + artifact management** | ✅ bullseye | CI/CD (GHA, Jenkins, Bazel, Gradle) + Artifactory + Bors-style merge queue + release governance |
| **Deep observability (metrics/logs/traces/alerting)** | ✅ | Grafana LGTM (metrics/Mimir, logs/Loki, traces/Tempo) / OpenObserve + PagerDuty alerting |
| **Generative-AI tool evaluation & enterprise adoption** | ✅ bullseye | Gemini Enterprise org-wide; standardized Cursor/Claude Code + Copilot PR review; build-vs-buy |
| Operational/security/cost of AI adoption | ✅ | Cost governance (>$200K saved / ~$2M); ISO 27001 / SOC 2; SBOM + static analysis |
| Performance optimization, capacity planning, ops excellence | ✅ | Locust perf framework (25%); 99.99%; SLOs; capacity/right-sizing |
| Complex issue resolution & remediation | ✅ | Blameless incident management/RCA; troubleshooting AI agent (miniBOT) |
| Infrastructure standards & best practices | ✅ | GitOps governance; coding/DevOps standards; DORA |
| Linux / distributed systems | ✅ | Linux; AWS Redshift (large-scale distributed data service); Hadoop/EMR |
| Technical leadership & mentorship; high-performing teams | ✅ | VP over multi-function org; Insulet 25–30 eng; Amazon team |
| Executive stakeholders (CISO / C-suite) | ✅ | CEO/CTO partnership; security & compliance program ownership |
| **HPC (supercomputing: schedulers/MPI/GPU clusters)** | ❌ gap | Large-scale distributed *data*/cloud compute — not HPC/supercomputing. Not claimed. |
| **On-prem data-center operations** | ⚠️ | Mostly cloud + hybrid (GCP/Azure) + early vCloud/on-prem; not a data-center/on-prem-HPC operator. Light. |
| Networking / storage depth | ⚠️ | Linux strong; storage (EFS/S3) and networking fundamentals — not a network/storage specialist |
| Quantum-computing domain | n/a | Not required (role is IT/compute-platforms, not quantum physics) |

## Gaps / stretch areas
- **HPC / supercomputing** is the real gap — Ishan's scale is large-scale *distributed cloud/data* systems
  (Redshift, Hadoop/EMR, K8s), not HPC schedulers/MPI/GPU clusters. Positioned as adjacent (large-scale
  distributed + cloud compute); HPC **not** claimed.
- **On-prem / data-center operations** — light (cloud + hybrid + early vCloud); framed honestly as hybrid, not
  as a data-center operator.
- Everything else is a strong-to-bullseye match, especially **dev infrastructure + observability + generative-AI
  adoption**, which are the JD's center of gravity.

## Tailoring checklist
- [x] HoA track — copied generic, tailored (compute-platforms + gen-AI-adoption + dev-infra/observability leader)
- [x] Lead with compute platforms, dev infrastructure (CI/CD + artifact mgmt), observability, gen-AI adoption
- [x] Operational excellence / performance / capacity / incident-remediation surfaced
- [x] Exec/CISO + security/cost framing surfaced
- [x] Gaps (HPC/supercomputing, on-prem data-center depth, quantum) NOT claimed
- [x] PDF exported → resumes/head-of-automation/companies/psiquantum/
