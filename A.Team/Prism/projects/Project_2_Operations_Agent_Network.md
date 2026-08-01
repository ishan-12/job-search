# Operations Agent Network — Decomposing an Enterprise Function

CruxOCM · Architect and owner · Vertex AI, FastAPI on Cloud Run, BigQuery vector RAG, Slack

**An orchestrator plus five specialist agents that finish the job with a deliverable, not a chat reply.**

---

## The business function

Pipeline operations troubleshooting was entirely human work: correlating Grafana and InfluxDB dashboards
against Kibana logs, reading signal trends and hydraulic behavior, searching Zendesk for prior occurrences,
checking docs, then hand-assembling an RFI workbook. Slow, shift-dependent — and safety-critical OT/SCADA,
where wrong-but-confident is not an acceptable failure mode.

## The decomposition — segment by evidence domain

Not one large agent with many tools. I cut the function along the lines it already breaks along: **each
source of evidence became an agent** with a bounded tool surface and a defined output contract, under an
orchestrator owning the mission end to end.

- **Orchestrator** — interprets the request, routes to the specialists it actually needs, reconciles what
  returns, produces the deliverable.
- **Dashboards** (Grafana, InfluxDB) · **Log analysis** (Kibana) · **Signal-trend and hydraulic analysis** ·
  **Ticket history** (Zendesk, so prior art surfaces) · **Docs and knowledge** — RAG over BigQuery vector
  embeddings of docs and tickets, so answers are grounded in the corpus, not model memory.

The ontology decision that made it work: **specialists are defined by the evidence they own, not the task
they perform** — so a new evidence domain is an addition, not a redesign of the mission logic.

## Engineering

- **Deliberate model tiering on Vertex AI** — Gemini 2.5 Flash for agent turns, Gemini 3 Pro for workbook
  generation; the tier follows the workload, not the hype.
- **Serverless, provisioned as code** — FastAPI on **Cloud Run services** (scale-to-zero, concurrency caps,
  VPC egress control, Secret Manager config, a service account per workload) plus **Cloud Run jobs** for
  async work — knowledge-base sync, ticket sync, pipeline runs — in Terraform/Terragrunt across ~17
  GCP/Azure projects. Driven from Slack, where operators already are.
- **Auto-generated RFI workbooks** — the service dispatches long-running generation to an async job instead
  of holding a request open; the mission ends in the artifact a human once assembled by hand. Governed
  through the AI control plane: scoped tools, short-lived credentials, Langfuse tracing.

## Why it maps to this mission

Exactly the motion the mission describes — take an enterprise business function, decompose it into agentic
workflows, define an ontology per agent, connect them to execute an end-to-end mission that produces real
output. Built in a safety-critical environment, which forced grounding, traceability, and bounded authority
in from day one.

*Related: a sibling agent in the same network authors Robot Framework suites against an OPC UA platform — output
that is executable software, closed by execution in a gated pipeline; regression went from days to <12 hours.*
