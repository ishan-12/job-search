# Convex — Outreach to James Turner (CEO)

Role: **Engineering Manager, Infra/Systems** · $280K · SF in-person

**Strategy:** lead with the one thing their infra team can't hire for internally — someone who has been
*building the agentic workloads Convex wants to abstract for*, and who has run infrastructure and grown
engineers. Then name the OLAP/OLTP gap before they find it. The JD has an entire section on trust; a
candidate who self-reports the mismatch is demonstrating the trait rather than claiming it.

**Do not:** claim Rust, claim database-internals work, or imply the Redshift years were on the engine.

---

## Version A — LinkedIn DM (~120 words, fits the connection-note follow-up)

```
James — your framing of the problem is why I'm writing: application demands changing while the
experience to design and operate infrastructure thins out.

I've spent the last 18 months on the other side of that gap, architecting and operating a production
AI control plane — agent gateway, orchestrator, per-tenant budgets, tool governance — on infrastructure
that was never designed for those workloads. I know exactly which primitives are missing, because I've
worked around their absence.

Before that: six years inside AWS Redshift, and cloud/data teams of 25–30 at Insulet. Still in the
codebase daily.

Straight up — Redshift is OLAP and my work there was the build and release ecosystem, not the storage
engine. Happy to talk about where that helps and where it doesn't.

Worth 20 minutes?

Ishan
```

## Version B — Email (~220 words)

**Subject:** Infra EM — I've been building the agentic workloads you're abstracting for

```
James,

Your framing is what got my attention: application demands changing fast while the experience to design
and operate infrastructure gets thinner. I've spent the last 18 months living on the wrong side of that
gap.

At CruxOCM I architected and operate a production AI control plane on GKE — an agent gateway doing
authn/authz, registration, model routing and per-tenant budgets, a supervisor orchestrator with a
human-in-the-loop gate, tool backends with egress allowlists and short-lived credentials, full tracing
and cost attribution. All of it built on infrastructure that was never designed for agentic workloads.
I have a very concrete list of the primitives that should have existed and didn't. That's the
perspective I'd bring to the abstraction you're defining.

The rest of the background: six years inside AWS Redshift, where I owned the build, CI/CD and release
ecosystem and led seven engineers on an automated merge queue that ended broken-mainline incidents;
25–30 engineers across cloud and data-product teams at Insulet; a platform I now run at 99.99% with
on-call and incident response. Still in the codebase daily.

One thing I'd rather say up front than have you find: Redshift is OLAP, and my work there was developer
infrastructure around the engine, not the storage layer itself. You weight OLTP for good reasons. What I
can point at is live-site weight I've actually carried and a decade of growing engineers into owning
hard problems.

I'm in San Carlos, so the SF office is easy.

Worth 20 minutes? And yes — I'll be fine with being asked whether there's a simpler solution. It's
usually the right question.

Ishan Shah
ishan.hash@gmail.com · +1-925-596-8956
```

---

## Notes before sending

- **Confirm the name.** The JD refers to "James"; Convex's founder is often listed as **Jamie Turner**.
  Check LinkedIn and match whatever he uses publicly before you hit send.
- **Decide on comp first.** $280K flat is likely below his VP band. If it's a non-starter, don't open
  the conversation.
- **Have the scope answer ready.** "You're a VP — why an EM role over one team?" The honest answer is
  that he wants to be closer to the systems; rehearse it, because it's the first thing they'll wonder.
- The closing line about a simpler solution is a callback to the JD's own joke. Keep it only if the
  tone feels right — cut it if the email reads long.
