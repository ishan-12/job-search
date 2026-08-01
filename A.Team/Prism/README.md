# A.Team — The Prism · AI Architect

Application package for the A.Team mission with **The Prism** (stealth enterprise AI company) for an
**AI Architect** — designing agents that create, orchestrate, and evolve other agents ("agentic layering").

**Captured:** Jul 28, 2026 · **Rate band:** $85–106/hr ($11,797–18,433/mo) · **Availability asked:** 40 hrs/wk

## Contents

| File | What it is |
|---|---|
| [role-and-jd.md](role-and-jd.md) | The mission posting, terms, and my read on how to position |
| [skills-and-experience.md](skills-and-experience.md) | Paste-ready **Skills & Experience** section — full (~1,390 words) + short (~270 words) |
| [projects/](projects/) | Three one-page project references (`.md` source + generated `.pdf`) |

## The three project references

| # | Project | The point it makes |
|---|---|---|
| 1 | **AI Control Plane** (CruxOCM) | The layer *beneath* agent creation — agenthood as a declared contract, so adding an agent is a registration, not a project. Directly answers "define the ontology and structure of new agents." |
| 2 | **Operations Agent Network** (CruxOCM) | Decomposing a real enterprise business function into an orchestrator + specialist agents that execute an end-to-end mission and emit a deliverable. Answers "break enterprise functions into agentic workflows." |
| 3 | **UniClaw** (open source) | Ontology-and-registry discipline done in public — 27 vendor adapters normalized to one canonical contract, multi-model cost tiering, 4,400+ tests. Answers the open-source (soofi.xyz) and reproducibility asks. |

PDFs are generated artifacts — edit the `.md`, never the PDF:

```bash
docker compose run --rm pdf "A.Team/Prism/projects/Project_1_AI_Control_Plane.md" \
                           "A.Team/Prism/projects/Ishan_Shah_Project_AI_Control_Plane.pdf"
```

(An explicit output path is required here — without it the generator writes `Resume_Ishan_Shah.pdf`.)

## Positioning summary

Lead with **ontology + registration + governed orchestration**, not "I built agents." Their stated
bottleneck — semantic correctness, reproducibility, architectural soundness of generated output — is the
same problem as owning build/CI/CD/release gating for AWS Redshift, which is 6 years of Ishan's résumé.
The "Architectural Operator" framing is the bridge: systems that produce software, not code written by hand.

## Open items before submitting

- **AWS Lambda (their one listed required skill) — claimed at a high level, per Ishan (Jul 28, 2026).**
  Basis: at Insulet the service estate ran serverless on AWS — ECS for services, **Lambda for event-driven
  and short-lived jobs**; today the agent estate runs on **Cloud Run** (Lambda-class managed compute) —
  services *and* async jobs — provisioned as code in `crux-tf-infra` (Terraform/Terragrunt, ~17 GCP/Azure
  project environments). The copy claims *serverless/event-driven architecture*, not deep Lambda or Step
  Functions specialization, and leans on their own line that the serverless layer is already encoded in
  existing agents. **If asked to go deep on Lambda internals, pivot to the Cloud Run equivalents** —
  cold starts, concurrency, timeouts, per-workload IAM, request-vs-job split, idempotency.
- **Availability (40 hrs/wk)** is deliberately not addressed in the written copy — currently VP of
  Engineering at CruxOCM. Decide how to answer before submitting.
- **Enterprise domains they name** are insurance and capital markets. Closest real credentials: regulated
  fintech (Prosper), FDA-regulated medical devices (Insulet), safety-critical energy/SCADA (CruxOCM),
  ISO 27001 + SOC 2 audit ownership. Framed as "regulated enterprise," not as insurance/capital markets.
- **"94% reduction in manual ops"** (the operations agent network) is unverified in the profile and is **not** used anywhere here.
