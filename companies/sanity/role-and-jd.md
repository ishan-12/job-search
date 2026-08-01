# Sanity — Role & JD

- **Title:** Director, Cloud Infrastructure
- **Track to use:** VP of Engineering (Director-level infra/platform leadership)
- **JD link:** https://jobs.ashbyhq.com/sanity/2bd22c35-4801-44bd-8487-8a280d4aba14
- **Location:** **London, UK** — `isRemote: true`, but `addressCountry: United Kingdom` and **no secondary
  locations**. Read as *remote within the UK*, not globally remote.
- **Department / team:** Product → **SRE**
- **Comp:** not published ("competitive stock options and location-based salary")
- **Captured:** Jul 28, 2026 (via Ashby posting API — the web page is JS-rendered and returns title only)
- **Recruiter tag in the JD:** `#LI-ST`
- **Company:** ~200 people. AI Content Operating System. Raised **$85M Series C** led by GP Bullhound;
  backed by ICONIQ Growth, Threshold, Heavybit, Shopify, and founders from Vercel, WP Engine, Twitter,
  Mux, Netlify, Heroku. Customers: SKIMS, Figma, Riot Games, Anthropic, Nordstrom, COMPLEX, Morning Brew.

## The mandate (their words, condensed)

> "Sanity's infrastructure is entering a new stage. The next layer is clearer ownership, stronger platform
> foundations, better operational discipline, and an architecture that can carry the company through the
> next few stages of growth."

Owns: cloud infrastructure, Kubernetes, networking, routing, observability, CI/CD, deployment paths,
incident response, and the standards that make production ownership work across product teams.

**Scale stated:** Content Lake handles ~**75,000 requests/second** (~4.5M/minute). Critical paths across
CDN, edge, gateway, caching, object storage, and **GCP**.

**Work already in motion:** moving **Varnish and Mead onto Fastly**, tightening observability, finishing
the **developer on-call rollout**, making production readiness a normal part of shipping.

## What they want

- Infrastructure strategy + roadmap across cloud, reliability, deployment, observability, security, cost, DX
- Lead teams owning GCP projects/clusters, K8s, networking, service discovery, routing, gateways, CI/CD, IaC, observability
- **Draw a clean line between Platform and SRE** — central foundations vs. enabling product teams,
  "without creating a ticket queue that everyone resents"
- Raise the reliability bar: dashboards, alert severity, paging standards, service ownership, on-call readiness, incident response
- **"Make deployment boring in the best way"** — golden paths, production readiness checks, safe rollouts
- **Own cloud cost discipline** — know where the money goes, make tradeoffs visible
- Longer-term architecture for multi-region, DR, **data residency**, and trust requirements: **SOC 2, ISO 27001, PCI, HIPAA**
- **Hire, coach, stretch infra leaders**; has **managed managers or senior technical leads**
- Deep enough to debate architecture with senior infra engineers, practical enough to call it

## My read — fit map

| Their criterion | Fit | Proof |
|---|---|---|
| Platform foundations: K8s, multi-cloud, IaC, GitOps | ✅ strong | Standardized Kubernetes as the control plane across **GCP + Azure** with GitOps-style governance; platform launched 0→1; **99.99% uptime** |
| Observability + on-call + incident response | ✅ **bullseye** | Team owns observability on **Grafana LGTM** (Loki/Grafana/Tempo/Mimir) / OpenObserve with **PagerDuty** for alerting and on-call — logs, metrics, traces, dashboards, SLOs, incident response |
| CI/CD + deployment golden paths, "make deployment boring" | ✅ **bullseye** | Owned build/CI-CD/release for **AWS Redshift** incl. fully automated build + deploy **across every AWS region**; merge queue gating on the exact merge candidate ended broken-mainline incidents; HA Jenkins on EKS/EFS at 99.9%, one-button deploy, −15% deploy errors |
| Platform vs product-team ownership, no ticket queue | ✅ strong | Shipped **self-service ephemeral infrastructure** via chat-native MCP servers + agents — took provisioning off the ticket queue entirely. Exactly their stated anti-goal |
| Cloud cost discipline | ✅ **bullseye** | **>$200K saved on ~$2M** GCP + Azure spend via right-sizing, ephemeral infra, scheduled non-prod shutdowns, reserved instances; owns a **$2–3M** budget |
| Trust requirements — SOC 2, ISO 27001 | ✅ **bullseye** | Owns both programs through third-party audit; plus FDA-regulated medical devices and safety-critical energy operations |
| Multi-region architecture | ✅ | Redshift build/deploy automation across all AWS-supported regions; IAH hosted across Azure + GCP |
| Managed managers / senior technical leads | ✅ | 25–30 engineers across cloud + data-product teams at Insulet; 7 engineers at Amazon; multi-function org at CruxOCM reporting to the CTO |
| Scaling SaaS / developer-tools company | ✅ | IAH is commercial multi-tenant B2B SaaS, 0→1, sold to external customers; 6 yrs inside AWS |
| Deep technically, still hands-on | ✅ | In the codebase daily (Python/FastAPI) |
| Exec + cross-functional communication | ✅ | Direct CEO/CTO partnership, quarterly OKRs, vendor + budget ownership |
| **75k req/s request volume** | ⚠️ **not matched by a stated number** | Redshift is one of AWS's largest distributed data services, but his role was the build/release ecosystem. **Do not imply he ran a 75k req/s serving path.** Anchor on uptime, on-call and incident discipline instead |
| **CDN / edge / Fastly / Varnish** | ❌ **gap** | Not in the profile. The in-flight project is literally a Fastly migration. Don't claim it; be curious about it |
| **PCI / HIPAA** | ❌ | Has ISO 27001 + SOC 2 + FDA-regulated device software. Claim those, not PCI/HIPAA |
| Service discovery / API gateways | ✅ (adjacent) | **Kuma service mesh** with mTLS; an agent/MCP **gateway** doing authn/authz, path + model routing, budgets, audit |
| **UK-based** | ❌ **the blocker** | Bay Area (San Carlos). See below |

## The location problem — and the honest argument

The role is **London / remote-in-UK** and Ishan is in **San Carlos, CA** (PT, 8 hours behind London).
That has to be raised by him, not discovered.

What makes the ask reasonable rather than presumptuous — all verifiable from Sanity's own job board
(25 open postings, captured Jul 28, 2026):

- **17 of 25 postings are US/Canada-based**, including two **San Francisco Bay Area** roles:
  *Software Engineering Manager, Web* and *Director, People Operations*.
- The **SRE org already hires in North America**: *Senior Site Reliability Engineer — Remote in the
  United States or Canada (East Coast/ET)*. Same team this role would lead.

So the honest question isn't "will you bend the rules for me" — it's **"is UK a hard requirement here for
EU coverage and on-call follow-the-sun reasons, or is it where you happened to open the req?"** The ET
preference on the SRE posting suggests overlap with London matters, so he should pre-empt it: commit to
early-PT mornings (London afternoons) and say so unprompted.

## Gaps summary — do not claim

- CDN / edge / Fastly / Varnish operating experience
- PCI or HIPAA
- A specific request-per-second figure on a serving path
- UK work authorization / residency

## Angle for the resume

Lead with **platform foundations + reliability discipline + cost + trust**, in that order — those are four
direct hits. Keep the AI-platform work present but compact: Sanity is an AI content company and it's a
differentiator, but this req is an infrastructure leadership role reporting into Product/SRE, not an AI role.
