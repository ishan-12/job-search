# Skills & Experience — A.Team / The Prism (AI Architect)

> Paste-ready copy for the mission application. Two lengths below — use the **Full version** if the field
> caps at 3,000 *words*; use the **Short version** if it turns out to cap at 3,000 *characters*.
> Every fact traces to `profile/candidate-profile.md`. Word counts noted at the end of each version.

---

## FULL VERSION (~1,390 words)

**Ishan Shah — VP of Engineering / Head of Automation, CruxOCM · San Carlos, CA**

I design the layer beneath agent creation: the contract an agent declares, the registry it joins, the
routing that connects it to other agents, and the guarantees that make its output correct and repeatable.
That is the problem your posting describes, and it's what I do in production today.

### Why this mission specifically

Your framing — "code generation is no longer the constraint; the bottleneck is ensuring what gets produced
is semantically and syntactically correct, as well as reproducible and architecturally sound" — is a
restatement of the problem I've owned for 15 years, first for human-generated code and now for
model-generated work.

At Amazon I owned the build, CI/CD, release ecosystem, and test tooling for **AWS Redshift**: the CI/CD
servers and fully automated build and deploy across every AWS-supported region. I led seven engineers
building a Bors-style automated merge queue that gated integration on the *exact merge candidate* rather
than the feature branch — the difference between "this change passed" and "this change passed in the state
it will actually land in." That eliminated broken-mainline incidents outright and unblocked developer
velocity across the org, and I added metrics-driven reporting on pipeline health and developer productivity
so bottlenecks were visible rather than anecdotal.

That is the same job as agentic layering. A generator that produces plausible output faster than you can
verify it is a liability until you put a contract, a gate, and a trace around it. I've built that gate for
one kind of generator; I now build it for agents.

### Agent networks in production — what I own now

At CruxOCM I architected and operate a production-hardened **AI control plane** on GKE with a Kuma service
mesh (mTLS in-mesh). It has four layers:

- **Agent Gateway** — one URL fronting `/agents/*` and `/mcp/*`: authentication, authorization, guardrails,
  agent and MCP **registration**, path routing, **model routing**, per-tenant budgets, and gateway audit.
- **Control layer** — a **LangGraph supervisor orchestrator** performing intent routing to specialist
  agents, a shared memory store, and a **human-in-the-loop approval gate**, with an operator UI for
  approvals, config, and policy.
- **Execute layer** — specialist agents and **MCP backends** (ephemeral infrastructure, time-series and
  dashboard access, signal editor/composer, HMI, project config, CI/CD, a test-authoring agent), each
  registered with an **egress allowlist** and **short-lived credentials**.
- **Observe layer** — **Langfuse** in-cluster: prompts, traces, tokens, cost, evaluations, datasets.

The important part isn't the component list — it's that **adding an agent to the network is a registration,
not a project.** A new agent declares a machine-readable contract: identity and auth, the path it answers
on, the tool surface it may touch, its egress allowlist, its model tier, its tenant budget, whether it
requires human approval, and how it's evaluated. That declaration *is* the ontology. It's also what makes
agents-creating-agents tractable: a generating agent can emit a contract and a tool binding, and the
platform enforces the rest. You can't safely automate agent creation until agenthood is a schema.

This control plane is the substrate for **IAH**, a commercial multi-tenant B2B SaaS AI platform I architected
0→1 from concept to production and which is sold to external business customers — governed, agent-based AI
workloads at scale, hosted across Azure and GCP.

### Decomposing a business function into an agent network

**An operations agent network** is the clearest example. Frontline operations support was a human function:
someone correlating time-series dashboards against system logs, reading signal trends and equipment
behaviour, searching past incident tickets, checking documentation, then hand-assembling the report the
customer receives. I didn't build one large agent. I segmented the function by **evidence domain** — each
domain became an agent with a bounded tool surface and a defined output contract — and put an orchestrator
above them that owns the mission end to end: interpret the request, route to the right specialists,
reconcile what comes back, and **produce the deliverable**. Documentation and ticket Q&A is grounded by RAG
over vector embeddings. It runs as FastAPI on Cloud Run, driven from the chat tool the operators already
use, with deliberate model tiering — a fast model for agent turns, a frontier model for document
generation. The mission ends in an artifact, not a chat reply. The context is regulated and
safety-critical, so wrong-but-confident is not an acceptable failure mode — the design principle I work
from is "the model proposes, the system disposes."

**A test-authoring agent** is my closest analogue to an agent whose output is software: it drafts
executable test cases against an industrial control interface, registered in the control plane like any
other agent, and its generated suites run in the gated pipeline — so the generation loop is closed by
execution, not by review. Manual regression went from days to under 12 hours.

I've also shipped **chat-native MCP servers and GCP ADK agents** that took two real operational functions —
self-service ephemeral infrastructure and cloud cost governance — off the ticket queue entirely, contributing
to more than $200K saved against roughly $2M of GCP and Azure spend.

### Systems thinking, AWS, and serverless

Six years inside AWS on Redshift. At Insulet the service estate ran serverless on AWS — ECS for services
and **Lambda** for event-driven and short-lived jobs — alongside EKS, highly available Jenkins on EKS/EFS at
99.9%, a Locust performance framework, SBOM across ~25 microservices, a 25% architecture performance
improvement, and 15% fewer deploy errors. Today the agent estate at CruxOCM runs on **Cloud Run** —
Lambda-class managed compute — provisioned as code in a Terraform/Terragrunt repo covering roughly 17
project environments across GCP and Azure: agent-facing Cloud Run **services** with scale-to-zero,
concurrency caps, VPC egress control, Secret Manager–backed configuration, and a dedicated service account
per workload, plus Cloud Run **jobs** for async and batch work, where the service dispatches long-running
generation to a job instead of holding a request open. That request/job split, per-workload IAM, timeouts,
idempotency, and cold-start economics are the same design questions Lambda, Step Functions, and DynamoDB
pose — and your posting notes that layer is already encoded into your existing agents. Where I add value on
day one is above it: how a business function is cut into agents, what each agent is allowed to touch, and
how their outputs compose into a mission.

### Prompt engineering, frameworks, and AI-assisted delivery

I work with existing frameworks rather than rebuilding them — LangGraph, MCP, GCP ADK, Vertex AI. I
standardized Cursor and Claude Code as the team development environment and deployed Claude Code with
GitHub Copilot for automated PR review, and I codify recurring solutions as reusable skills and MCP servers
instead of one-off scripts. My working position on prompting: "fine-tuning changes how a model behaves, RAG
changes what it knows, prompting is how you get 80% of the value before spending on either" — and the
follow-on, "the question is never which model is best, it's which tier this workload deserves." Both of
those show up as concrete routing and cost decisions in the systems above.

### Open source

**UniClaw** ([github.com/uniclaw-labs/uniclaw](https://github.com/uniclaw-labs/uniclaw), Apache-2.0/MIT) — an
open-source natural-language vehicle-control platform: a FastAPI backend and Tauri/React 19 desktop app, an
agent with three model modes (Claude Sonnet, local Gemma via Ollama, zero-cost command menu), **27
vehicle-brand provider adapters** behind a pluggable registry, 12 messaging channels plus Alexa and Google
Home, OAuth2 with scoped JWTs, Fernet-encrypted credentials, non-root containers, and **4,400+ automated
tests**. The adapter registry is ontology work: 27 vendors with incompatible semantics normalized to one
contract so a new brand is a plugin, not a fork. I also publish an open-source **Lever MCP server**. I'd
contribute to soofi.xyz the same way I run these repos.

### Enterprise and regulated environments

Safety-critical industrial operations at CruxOCM, FDA-regulated medical devices at Insulet,
regulated fintech at Prosper, and I own ISO/IEC 27001 and SOC 2 audit reports. Enterprises don't adopt agent
networks because the demo was good; they adopt them when the audit trail, the approval gate, and the blast
radius are answerable. I build for that by default.

### How I work

Systems thinker first, hands-on second — I'm still in the codebase in Python/FastAPI while running the
function. I'm comfortable with ambiguity and stealth-stage churn, I ship daily against stories rather than
quarter-long specs, and I've worked distributed teams across time zones for most of my career.

*(~1,390 words)*

---

## SHORT VERSION (~270 words / ~1,790 characters)

I design the layer beneath agent creation: the contract an agent declares, the registry it joins, the
routing that connects it, and the guarantees that make its output correct and repeatable.

At CruxOCM I architected and operate a production AI control plane on GKE — an Agent Gateway (authn/authz,
guardrails, agent + MCP registration, path and model routing, per-tenant budgets, audit) fronting a
LangGraph supervisor orchestrator with a memory store and a human-in-the-loop gate, MCP backends with
egress allowlists and short-lived credentials, and Langfuse for traces, cost, and evaluations. Adding an
agent is a registration, not a project: it declares identity, tool surface, egress, model tier, budget,
approval requirement, and eval set. That declaration is the ontology — and it's the precondition for agents
that create agents. It's also the substrate for IAH, a multi-tenant B2B SaaS AI platform I took 0→1 and
that's sold to external customers.

I decompose functions before building them. An operations agent network segmented frontline support by evidence
domain — dashboards, logs, signal analysis, ticket history, RAG-grounded docs — under an orchestrator that
produces the finished customer report, not a chat answer. A sibling agent authors executable test suites;
regression went from days to under 12 hours.

Your stated bottleneck — semantic correctness, reproducibility, architectural soundness — is the job I did
for six years at AWS owning Redshift's build, CI/CD, release, and merge-gating systems. Serverless
throughout: Lambda and ECS at Insulet, Cloud Run services and async jobs for the agent estate today, all
provisioned as code. Open source: UniClaw (27-adapter registry, 4,400+ tests) and a Lever MCP server.

*(~270 words)*
