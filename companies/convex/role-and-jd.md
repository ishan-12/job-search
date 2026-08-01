# Convex — Role & JD

- **Title:** Engineering Manager, Infra/Systems
- **Track to use:** VP of Engineering (hands-on EM framing, not VP scope — see notes)
- **Comp:** $280K – $280K (single point, not a range)
- **Location:** San Francisco — **in-person**, hires primarily in SF ("a few experienced folks remote in certain situations")
- **Captured:** Jul 28, 2026 · posted ~Jul 21, 2026; recruiter recently active
- **CEO:** James Turner

## The pitch (their framing)

> "Application demands are rapidly changing while the experience to design and operate infrastructure is
> rapidly diminishing. A new platform abstraction is needed to support **agentic development, agentic
> applications, and an entirely new set of application workloads.**"

Team owns **the database, the sync layer**, and newer primitives (**branching, analytics**). Explicitly
"no playbook — we're the ones writing it."

## What they want

- Deep distributed systems + operating infra at scale; owning systems through major scale transitions, or
  building core infrastructure from scratch
- Track record of **growing engineers**, not just shipping software
- Strong systems judgment — simplicity vs. justified complexity
- Fast-moving, under-specified problems
- In-person SF; high-quality code (**Rust a plus**)
- **"We generally weigh experience on OLTP databases over OLAP or offline systems"** — live-site,
  user-facing mindset
- Still an engineer: architecture, code review, works directly with the CTO

## My read — fit map

| Their criterion | Fit | Proof |
|---|---|---|
| Agentic workloads as the thing the platform must serve | ✅ **differentiator** | Built the AI control plane + agent network that Convex's abstraction is *for* — he is the customer persona and an infra leader at once |
| Operating infra at scale, live-site | ✅ | 99.99% platform uptime, K8s control plane across GCP + Azure, observability (Grafana LGTM / OpenObserve) + PagerDuty on-call |
| Large-scale distributed data service | ✅ (adjacent) | 6 yrs inside AWS Redshift — but on the build/CI-CD/release/test ecosystem, **not** the storage or query engine |
| Growing engineers / building teams | ✅ strong | 7 engineers on the Redshift merge queue; 25–30 across cloud + data-product teams at Insulet; hiring and mentoring at CruxOCM |
| Hands-on EM, still an engineer | ✅ | In the codebase daily (Python/FastAPI) while running the function |
| Fast-moving, under-specified | ✅ | 0→1 platform at CruxOCM; stealth-stage churn |
| Systems judgment / simplicity | ✅ | Merge queue gating on the exact merge candidate; "the model proposes, the system disposes" |
| Building core infra from scratch | ✅ (platform, not database) | Web-services hybrid platform 0→1; AI control plane 0→1 |
| In-person SF | ✅ | San Carlos — commutable, no relocation needed |
| **OLTP database internals** | ❌ **the real gap** | Redshift is **OLAP**, and his role was developer infrastructure around it. No storage-engine, sync-protocol, or transaction-layer authorship |
| **Rust** | ❌ | ~3% of UniClaw via Tauri. JD says "you'll figure it out," so survivable — do not claim it |
| Sync layer / branching primitives | ❌ | Not built. Nothing comparable to claim |

## Gaps / how to handle

- **OLAP vs OLTP is called out explicitly in the JD.** Do not paper over it. Naming it first is the
  strongest move available — the JD has a whole section on trust and integrity, and a candidate who
  self-reports the mismatch reads as senior. Then pivot to the live-site weight he *has* carried
  (99.99%, on-call, incident response) and the team-growing record.
- **Scope mismatch is the other risk:** he's a VP/Head-of-function; this is a hands-on EM over one team.
  Frame it as deliberate — he wants to be closer to the systems, not further away — or the read is
  "overqualified, will be bored, will leave."
- **Comp is a flat $280K.** Below his likely VP band. Decide before engaging.
- **Rust:** don't claim it. The JD already forgives it.

## The angle that makes this note worth sending

Convex is betting the company on **agentic workloads**. Ishan has spent the last 18 months building
exactly those workloads — an agent gateway, orchestrator, per-tenant budgets, tool governance — on top of
infrastructure that wasn't designed for them. He has felt precisely which primitives are missing. That is
a perspective their infra team does not have in-house, and it is not something a database specialist can
fake. Lead with it.
