# LinkedIn profile — Ishan Shah

Paste-ready copy for the LinkedIn **Experience → CruxOCM** description. Plain text, no markdown; the
bullet is a literal bullet character. Facts trace to `candidate-profile.md`.

Public profile, so internal product codenames (miniBOT, TestBOT) are **omitted** — same rule as
`wellfound-profile.md`. IAH stays because Ishan already names it publicly.

---

## Experience — CruxOCM (VP of Engineering / Head of Automation, Feb 2025 – Present)

### Recommended — 1,691 / 2,000 characters

```
Lead a technology mandate spanning AI engineering, platform, infrastructure, quality engineering, and compliance — reporting to the CTO and driving the technical strategy behind CruxOCM's enterprise growth in pipeline automation.

• Led the creation of Industrial Automation Hub (IAH), a multi-tenant agentic AI platform for deploying, validating, and managing control applications — cutting deployment time by 50% and compressing release cycles from months to weeks.

• Agentic AI in production: shipped two agents into safety-critical operations — a multi-agent troubleshooting assistant (Gemini on Vertex AI, RAG over BigQuery vector embeddings, Slack-native) doing root-cause analysis across telemetry, logs, and support history, and a test-authoring agent that generates Robot Framework/OPC UA suites, cutting manual regression from days to under 12 hours.

• AI Control Plane (MLOps/LLMOps): built the platform that makes agentic workflows governable and observable — an agent/MCP gateway on GKE handling authn/authz, guardrails, multi-model routing, per-tenant budgets, and audit; a LangGraph supervisor orchestrator with a human-in-the-loop approval gate; and end-to-end tracing, token/cost attribution, evaluations, and prompt/dataset versioning.

• Direct multi-cloud platform, infrastructure, and AIOps strategy across GCP and Azure — Kubernetes control plane, GitOps, Terraform/Terragrunt IaC, SLO-driven observability on the Grafana LGTM stack with PagerDuty on-call, and AI agents embedded in incident response — achieving 99.99% uptime and $200K+ in cost savings.

• Own ISO 27001 and SOC 2 audit completion, unblocking enterprise procurement with supermajor energy customers.
```

### Compact alternative — 1,111 / 2,000 characters

Use if five bullets read long against the rest of the profile. Folds the two agents into the control-plane
bullet and keeps the original two-bullet spine.

```
Lead a technology mandate spanning AI engineering, platform, infrastructure, quality engineering, and compliance — reporting to the CTO and driving the technical strategy behind CruxOCM's enterprise growth in pipeline automation.

• Led the creation of Industrial Automation Hub (IAH), a multi-tenant agentic AI platform for deploying, validating, and managing control applications — cutting deployment time by 50% and compressing release cycles from months to weeks.

• Built the AI Control Plane behind it — agent/MCP gateway (authn/authz, guardrails, multi-model routing, per-tenant budgets, audit), LangGraph orchestration with human-in-the-loop approval, and MLOps/LLMOps observability for traces, cost, and evaluations — running two production agents: AI troubleshooting/root-cause analysis and AI test authoring (regression cut from days to under 12 hours).

• Direct multi-cloud platform, infrastructure, and AIOps strategy across GCP and Azure — achieving 99.99% uptime, $200K+ in cost savings, and ISO 27001/SOC 2 audit completion that unblocks enterprise procurement with supermajor energy customers.
```

---

## Supporting changes elsewhere on the profile

- **Skills** (LinkedIn keyword-matches recruiter search against these, not just prose): add **MLOps**,
  **AIOps**, **LLMOps**, **Agentic AI**, **AI Agents**, **LangGraph**, **Vertex AI**, **RAG**,
  **Model Evaluation**, **AI Governance**. Pin them to the CruxOCM role so they show under it.
- **Headline** option if the current one is platform-only:
  `VP of Engineering | AI Platforms & Agentic Systems | MLOps / AIOps | Multi-Cloud Infrastructure`
- **About** section: mirror one line of the control-plane language so the term "MLOps" appears above the
  fold as well as inside Experience.

## Notes

- Traceable numbers only: 50% deployment-time cut, months → weeks, days → under 12h regression,
  99.99% uptime, $200K+ savings, ISO 27001 + SOC 2, two production agents. The unverified
  "94% reduction in manual ops" figure is **not** used.
- "Multi-tenant" replaces nothing in the original IAH line — it's added because
  `candidate-profile.md` supports it and it signals real SaaS scope.
- "Sub-12-hour regression cycles" moved out of the infrastructure bullet and into the agent bullet,
  where it's attributable to the AI test agent rather than to platform work.
