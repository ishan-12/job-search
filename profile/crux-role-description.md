# CruxOCM role description — application profile field

Paste-ready for the "role description" field on application profiles (Workday, Wellfound, Greenhouse).
Plain text, no markdown; the bullet is a literal bullet character. Facts trace to `candidate-profile.md`.

Deliberately reusable across the VP Eng / DevOps / platform / AI-infrastructure roles in the pipeline, so it
leads with scope and platform rather than tuning to one JD. Product codenames omitted.

## 1924 / 2,000 characters

```
VP of Engineering / Head of Automation, reporting to the CTO. Own technology strategy across AI, Web Services, DevOps, Infrastructure, Security, Quality and IT for an industrial automation platform operating in safety-critical, regulated energy environments.

• Platform: architected and launched the platform from scratch; standardized Kubernetes as the control plane across GCP and Azure with GitOps governance, a Kuma service mesh (mTLS in-mesh) and Terraform/Terragrunt infrastructure as code. 99.99% uptime.
• Reliability: defined SLOs, alert severity and paging standards, service ownership and incident response; observability on the Grafana LGTM stack and OpenObserve with PagerDuty on-call rotations.
• AI in production: shipped agents that automate operational work — incident troubleshooting and root-cause analysis, self-service ephemeral infrastructure, automated cost governance — plus an AI control plane on GKE: a gateway handling authn/authz, guardrails, registration, model routing, per-tenant budgets and audit, fronting an orchestrator with a human-in-the-loop approval gate, with tracing, cost attribution and model evaluation.
• Delivery: CI/CD with pipeline gating and a Robot Framework test platform augmented by an AI test-authoring agent — manual regression cut from days to under 12 hours; standardized Cursor and Claude Code with AI-assisted PR review.
• Product: architected a commercial multi-tenant B2B SaaS AI platform 0-to-1, sold to external business customers and hosted across Azure and GCP.
• Commercial: own a $2-3M annual budget including ~$2M of cloud spend; delivered >$200K in savings through right-sizing, ephemeral infrastructure and reserved capacity.
• Compliance: spearheaded ISO/IEC 27001 and SOC 2 and obtained audit reports for both.
• Team: hire, coach and develop engineers across a distributed organization; partner with the CEO and CTO on the roadmap and quarterly OKRs.
```

## Notes

- Traceable numbers: 99.99% uptime, $2-3M budget, ~$2M cloud, >$200K saved, days to under 12h regression,
  ISO 27001 + SOC 2. The unverified "94% reduction in manual ops" figure is not used.
- If a field is tighter than 2,000, cut in this order: Team, Compliance, Product. The Platform, Reliability
  and AI bullets are the load-bearing three for every role currently in play.
- If a role is DevOps/SRE-weighted (e.g. Fiserv), move the AI bullet below Delivery so Platform and
  Reliability lead. If it's AI-platform-weighted, leave as is.
