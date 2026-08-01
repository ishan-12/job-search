# Zipline — Role & JD

- **Title:** Director of Engineering, Marketplace
- **Track to use:** VP of Engineering (Director-level, **product-org framing** — not the infra framing)
- **Location:** not stated in the posting. Zipline HQ is South San Francisco — **confirm on-site expectations**
- **Comp:** not stated
- **Captured:** Jul 29, 2026

## What the org owns

The consumer side of a drone delivery network:

- **The Zipline consumer app** — ordering meals, groceries, home essentials
- **Partner tools** — restaurant kitchen integrations, retailer catalog connections, on-demand fulfillment
  powering checkout-to-delivery in as little as 10 minutes
- **Customer support tooling**
- **Services** — pricing, prioritization, growth optimization
- **Developer tooling** to enable high-velocity engineering for the team

## What they want

- Track record leading and scaling **product engineering** teams shipping **operationally-complex software**
- Strong technical judgment; guide architecture so a lean team gets a lot done
- Building organizations, developing leaders, attracting exceptional technical talent
- **Excellent product sense**, prioritization, cross-functional partnership
- Comfort in ambiguity
- *Nice to have:* marketplace, e-commerce, pricing, or two-sided-platform products
- *Nice to have:* **thought leadership on the AI-driven way of building software**

## My read — the honest fit picture

This is a **weaker fit than Fiserv or Sanity**, and the weakness is on one specific axis. Worth applying
(the JD explicitly invites imperfect fits) but go in clear-eyed.

| Their criterion | Fit | Notes |
|---|---|---|
| **Operationally-complex software** | ✅ **strongest angle** | Career spent on software that drives or observes physical systems where failure is visible: pipeline SCADA/OT control, FDA-regulated medical devices, industrial automation. Zipline is the same genre of consequence — kitchens, fulfillment, 10-minute promises |
| **Developer tooling for high-velocity engineering** | ✅ **explicit JD line, deep match** | Literally the Amazon job: owned Redshift's build/CI-CD/release, led 7 on a merge queue that ended broken-mainline incidents. Plus CI/CD + test platform at CruxOCM cutting regression days → <12h |
| Leading and scaling teams; developing leaders | ✅ | 25–30 engineers at Insulet across multiple teams; 7 at Amazon; multi-function org at CruxOCM; hires and coaches |
| **AI-driven way of building software** (nice-to-have) | ✅ **bullseye** | Standardized Cursor + Claude Code as the team environment, AI PR review, wrote the org's conventions, shipped production agents. Genuine thought leadership, and it's a differentiator most Director candidates won't have |
| Comfort in ambiguity; lean team, high output | ✅ | 0→1 platform and 0→1 commercial SaaS at a startup, reporting to the CTO |
| Technical judgment / architecture | ✅ | Multi-cloud platform architecture, 99.99%, AI control plane |
| Cross-functional partnership | ✅ | CEO/CTO, product, operations, GTM |
| **Product engineering teams** | ⚠️ **partial** | Teams led have been infra, DevOps, platform, quality, and **cloud + data-product** at Insulet. Not consumer product engineering. The "operationally-complex" half is strong; the "product engineering" half is the stretch |
| **Excellent product sense** | ⚠️ **the real gap** | Core requirement. Closest genuine credential: architected a commercial multi-tenant B2B SaaS platform 0→1 that is **sold to external customers** — real product ownership, but B2B and enterprise, not consumer |
| **Consumer-facing product** | ❌ | None. Zipline's app is consumer food/grocery delivery. Entire background is B2B, industrial, medical, fintech infra |
| Marketplace / e-commerce / pricing / two-sided platforms | ❌ | Not present. It is a nice-to-have, but combined with the consumer gap it's the likely screen-out |
| Growth optimization | ❌ | Not his background |

## Strategy

**Lead with genre, not domain.** He cannot claim consumer marketplace experience. What he can claim, credibly
and distinctively, is a career building software where **the physical world is the failure mode** — and that
is exactly what makes Zipline's marketplace hard. A checkout that succeeds while the kitchen can't fulfil, or
a 10-minute promise the network can't keep, is an operations problem wearing a product interface.

Three pillars, in this order:
1. **Operationally-complex software leadership** — the genre match
2. **Engineering velocity** — their explicit ask, his deepest expertise
3. **AI-native engineering** — their nice-to-have, his standout

**De-emphasize** infrastructure minutiae (service mesh, IaC internals). This is a product org; reliability and
platform should be framed as customer experience and team velocity, not as infra craft.

## Gaps — do not claim

- Consumer product or consumer app experience
- Marketplace, two-sided platform, pricing, or e-commerce products
- Growth optimization / experimentation
- "Product sense" as a proven track record — frame it as B2B product ownership (0→1, sold to customers)

## Open questions

- **Location and on-site expectations** are not in the posting. Zipline HQ is South San Francisco, which is
  close to San Carlos — likely a non-issue, but confirm.
- **Comp is not stated.** Director at a late-stage startup; ask early.
