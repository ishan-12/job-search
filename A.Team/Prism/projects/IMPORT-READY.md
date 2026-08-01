# A.Team project imports — paste-ready

The three project PDFs would not import, so here is the same material in the shape A.Team's project
form actually takes: a description under 1,000 characters, an image, and metrics.

**Plain text on purpose** — no markdown, no bullets, no bold. Paste the description exactly as-is;
blank lines between paragraphs are the only formatting. Character counts are exact and verified.

---

## Project 1 — AI Control Plane: a governed agent network in production

**Title:** AI Control Plane — a governed agent network in production
**Image:** `Project_1_AI_Control_Plane.png` (1600x1200, ~45 KB) — or `Project_1_AI_Control_Plane.jpg` (same size, ~165 KB)
**Role / org:** Architect and owner · CruxOCM · Feb 2025 – present

**Description (987 characters):**

```
A production AI control plane on GKE where adding an agent is a registration, not a project.

Every agent declares a machine-readable contract: identity and auth, route, tool surface, egress allowlist, model tier, tenant budget, whether it needs human approval, and how it is evaluated. That declaration is the ontology — and it is the precondition for agents that create agents.

Four layers behind one URL. Agent Gateway: authn/authz, guardrails, agent and MCP registration, path and model routing, per-tenant budgets, audit. Control: a LangGraph supervisor orchestrator with a shared memory store and a human-in-the-loop approval gate. Execute: specialist agents and MCP backends, each with an egress allowlist and short-lived credentials. Observe: Langfuse for traces, tokens, cost and evaluations. Kuma service mesh, mTLS in-mesh.

It is the substrate for IAH, a commercial multi-tenant B2B SaaS AI platform I took 0-to-1 and that is sold to external customers across Azure and GCP.
```

**Metrics:**

| Label | Value |
|---|---|
| Platform uptime | 99.99% |
| Clouds | Azure + GCP (multi-tenant) |
| Compliance | ISO 27001 + SOC 2 |
| Agent onboarding | Registration via an 8-field contract |
| Cloud savings, agent-driven cost governance | >$200K on ~$2M spend |

---

## Project 2 — Operations Agent Network: an enterprise function, decomposed

**Title:** Operations Agent Network — an enterprise function, decomposed
**Image:** `Project_2_Operations_Agent_Network.png` (1600x1200, ~45 KB) — or `Project_2_Operations_Agent_Network.jpg` (same size, ~165 KB)
**Role / org:** Architect and owner · CruxOCM · safety-critical OT/SCADA

**Description (978 characters):**

```
A frontline operations support function was human work: correlating time-series dashboards against system logs, reading signal trends, searching past incident tickets, checking documentation, then hand-assembling the report the customer receives.

I did not build one large agent. I cut the function along the lines it already breaks along — each source of evidence became an agent with a bounded tool surface and a defined output contract, under an orchestrator owning the mission end to end. The ontology decision that made it work: specialists are defined by the evidence they own, not the task they perform, so a new evidence domain is an addition rather than a redesign.

Serverless and provisioned as code: FastAPI on Cloud Run services plus async jobs, in Terraform. Deliberate model tiering — a fast model for agent turns, a frontier model for document generation. Docs grounded by retrieval over vector embeddings. The mission ends in the deliverable, not a chat reply.
```

**Metrics:**

| Label | Value |
|---|---|
| Agents | 1 orchestrator + 5 specialists |
| Evidence domains covered | 5 (telemetry, logs, signal analysis, ticket history, documentation) |
| Model tiers | 2 — a fast model for agent turns, a frontier model for documents |
| Serverless footprint | 1 Cloud Run service + 3 Cloud Run jobs |
| Environments as code | Every environment, multi-cloud (Terraform/Terragrunt) |
| Output | Customer-facing report auto-generated (previously hand-assembled) |

---

## Project 3 — UniClaw: one contract, 27 vendor dialects

**Title:** UniClaw — one contract, 27 vendor dialects (open source)
**Image:** `Project_3_UniClaw.png` (1600x1200, ~45 KB) — or `Project_3_UniClaw.jpg` (same size, ~165 KB)
**Role / org:** Architect and maintainer · github.com/uniclaw-labs/uniclaw

**Description (989 characters):**

```
Open-source natural-language vehicle control. 27 vehicle brands expose incompatible surfaces: different auth models, different verbs, different state machines, different notions of what "locked" even means. The naive build is 27 special cases.

I defined the canonical capability contract first — what a vehicle is to the system, independent of vendor — then made every brand a provider adapter behind a pluggable registry mapping its dialect onto that contract. Adding a brand is registering an adapter; the agent reasons against the canonical model and never learns a vendor's quirks. Same pattern inbound: 12 messaging channels plus Alexa and Google Home normalised to one intake contract.

Three model modes, by what the request deserves: Claude Sonnet for open-ended intent, local Gemma via Ollama for private or offline use, and a zero-cost command menu for deterministic ones. 4,400+ automated tests across Python, TypeScript and Rust.

Link: https://github.com/uniclaw-labs/uniclaw
```

**Metrics:**

| Label | Value |
|---|---|
| Provider adapters | 27 vehicle brands behind one contract |
| Intake channels | 12 messaging + Alexa + Google Home |
| Automated tests | 4,400+ |
| Model modes | 3, including a zero-cost no-model path |
| License | Apache-2.0 / MIT (dropped from the prose to make room for the link) |

---

## Notes before you paste

- **The ">$200K" metric on Project 1** traces to right-sizing plus ephemeral infrastructure and the
  agent-driven cost-governance workflows registered in the control plane. If you'd rather keep the
  control-plane entry purely architectural, drop that row — the other four stand on their own.
- **Nothing here uses the unverified "94% reduction in manual ops"** figure for this project. Still open in
  `profile/candidate-profile.md`.
- **Both formats are in this folder, 1600x1200 (4:3).** Prefer the **PNG** — at ~45 KB it is roughly a
  quarter the size of the JPEG, because these are flat-colour diagrams and a palette compresses them far
  better than JPEG does. The **JPEG** (~165 KB, quality 90, 4:4:4 chroma so the text stays sharp) is there
  for any form that will not take a PNG.
- **PNG sizing:** kept small by quantising to a 128-colour palette — these
  are flat-colour diagrams, so it is visually lossless — then running `oxipng -o max`. The source HTML sits
  next to the PNGs (`img1-*.html`, `img2-*.html`, `img3-*.html`); edit the wording and re-shoot with:

  ```
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu \
    --hide-scrollbars --force-device-scale-factor=1 --window-size=1600,1200 \
    --screenshot=Project_1_AI_Control_Plane.png "file://$PWD/img1-control-plane.html"
  ```
- **The one-page PDFs are still in this folder** and remain the better artifact to attach to an email or
  hand to an interviewer; these blocks are purely for the A.Team form.
