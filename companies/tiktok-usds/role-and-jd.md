# TikTok US — USDS — Role & JD

- **Title:** Head of Infrastructure Engineering, TikTok US — USDS (TikTok USDS Joint Venture LLC)
- **Track to use:** VP of Engineering
- **JD link:** https://www.linkedin.com/jobs/view/4428660403/
- **Comp range (if known):** Not listed (executive; expect senior-exec band)
- **Location / remote:** San Jose, CA — fully in-person, up to 5 days/week

## Full JD (captured from LinkedIn guest endpoint)

**Org:** TikTok USDS Joint Venture — US data-security entity operating the apps under defined safeguards.

**Overview:** Own vision, execution, and operational excellence for the infrastructure powering a
mission-critical, revenue-generating platform and its supporting data and AI/ML platforms. Lead multiple
teams across **platform engineering, SRE, networking/traffic, storage & databases, data infrastructure,
and GPU/ML infrastructure**. Set strategy, drive cross-org alignment, deliver measurable outcomes in
availability, latency, efficiency, and security — at internet scale.

### Responsibilities
- **Strategy & Leadership:** multi-year infra roadmap; scale high-performing teams; leadership operating system; accountability-driven culture tying technical goals to business impact.
- **Platform & Distributed Systems:** architect & own reliability of global, multi-region distributed systems; fault isolation, automated recovery, resilience at internet scale.
- **Kubernetes at Scale:** production-grade multi-cluster K8s; multi-cluster networking & workload isolation; automation, self-service primitives, strict SLO governance.
- **Data, Storage & Databases:** global SQL/NoSQL fleets and lakehouse architectures; durability, high-QPS performance, cost-efficiency.
- **Networking & Edge Delivery:** global traffic engineering and CDN/Edge; deep network observability; routing, failover, multi-region connectivity.
- **AI/ML & GPU Infrastructure:** large-scale GPU clusters for distributed training/inference; hardware utilization; network fabric optimization.
- **SRE & Incident Management:** org-wide SLOs & observability; incident command; systemic remediation.

### Minimum Qualifications
- 6+ years infra/platform engineering; significant large-scale distributed systems in production.
- **6+ years leading leaders (managers of managers)** across multiple infra domains; scale orgs, deliver through others.
- Large production K8s at scale (multi-cluster, multi-region); hands-on networking, load balancing, global traffic management.
- **CDN/Edge delivery** & performance optimization for consumer-grade, high-traffic systems; large data/storage incl. **HDFS** (or equivalent) with durability/capacity discipline.
- SQL & NoSQL platforms at scale — HA/DR, replication, perf tuning, multi-tenant governance.
- **AI/ML infra on large GPU clusters** — distributed training/inference, multi-tenant scheduling.
- Strong executive communication (technical → business impact, investment, risk).

### Preferred
- Company-wide reliability/platform standardization (SLO governance, paved roads).
- Service mesh & multi-cluster traffic engineering.
- Infra portfolio budget & vendor strategy (cloud/hardware/network/CDN/database).
- Performance engineering for tail-latency reduction at global scale.

## My read — keyword & priority map

| JD theme / keyword | Do I have it? | Which resume bullet / story proves it |
|---|---|---|
| Infra/platform engineering leadership | ✅ | CruxOCM platform org; Insulet cloud; Amazon Redshift infra |
| Large-scale distributed systems in production | ✅ (adjacent scale) | AWS Redshift — one of AWS's largest distributed data platforms |
| Kubernetes multi-cluster / multi-region | ⚠️ partial | K8s control plane across GCP+Azure (multi-cloud, GitOps) — not internet-scale multi-cluster |
| SRE / SLO governance / observability | ✅ | 99.99% uptime; SLOs; observability; incident practices |
| Data / storage / HDFS | ✅ | Hadoop/HDFS on AWS EMR (Prosper); Redshift data platform |
| SQL & NoSQL at scale | ⚠️ partial | MySQL/PostgreSQL/Oracle/DynamoDB — not scaled HA/DR fleet ownership |
| Budget & vendor strategy | ✅ | $2–3M budget + vendor mgmt (smaller scale than TikTok) |
| Executive communication (→ business impact) | ✅ | C-suite partnership; OKRs; investment/risk framing |
| Multi-year roadmap; scaling orgs; accountability culture | ✅ | multi-year strategy; distributed org across domains |
| AI/ML platforms (not GPU) | ✅ platform / ❌ GPU | MLOps/LLMOps, Vertex AI, ADK — NOT GPU-cluster training/inference |
| 6+ yrs leading managers-of-managers | ❌ gap | VP ~1.5 yr + Sr Manager (Insulet); short of 6 yrs at manager-of-managers level |
| CDN/Edge delivery | ❌ gap | no CDN/edge experience |
| Global traffic engineering / networking / LB | ❌ gap | not a networking/traffic background |
| GPU/ML training infrastructure | ❌ gap | AI apps yes; GPU training/inference clusters no |
| Consumer internet-scale / high-QPS | ❌ gap | B2B/regulated (energy/medical/fintech/AWS-internal), not consumer internet-scale |
| Service mesh | ❌ gap | K8s/GitOps yes; service mesh not in profile |

## Gaps / stretch areas — READ BEFORE APPLYING
- **This is a reach.** Several *minimum* qualifications are not met: (1) 6+ yrs managing managers-of-managers,
  (2) CDN/Edge + global traffic engineering, (3) AI/ML on large GPU clusters (distributed training/inference),
  (4) consumer internet-scale operations. The resume makes the strongest honest case on the overlap
  (platform/infra leadership, distributed *data* platforms at AWS scale, K8s multi-cloud, SRE/SLOs, data/HDFS,
  MLOps/AI-ML platforms, budget/vendor, exec comms) and does **not** claim GPU/CDN/global-traffic/internet-scale.
- **Scale framing:** honest about multi-cloud/multi-region *data-platform* scale, not TikTok consumer scale.
- **Recommendation:** low-probability without a strong internal referral; if pursued, be transparent about the
  GPU/CDN/traffic gaps and lead with distributed-data-platform + SRE + org-leadership strengths. Onsite 5 days/wk San Jose.

## Tailoring checklist
- [x] Summary rewritten to lead with infra/platform/distributed-systems/SRE leadership + data & AI/ML platforms + exec comms
- [x] Bullets reframed toward infrastructure; Forward-Deployed dropped (irrelevant here)
- [x] Real matches surfaced (Redshift distributed data platform, Hadoop/HDFS, K8s, SLOs, budget/vendor)
- [x] GPU / CDN / global-traffic / internet-scale / managers-of-managers NOT overclaimed
- [x] PDF exported → ../../resumes/vp-engineering/companies/tiktok-usds/
