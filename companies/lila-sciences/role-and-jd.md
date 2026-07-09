# Lila Sciences — Role & JD

- **Title:** Senior Director, Software Development, Test Automation (Systems) — reports to VP of Engineering
- **Track to use:** Head of Automation (test-automation / quality / CI-CD wheelhouse)
- **JD link:** https://job-boards.greenhouse.io/lilasciences/jobs/4294875009
- **Comp range (if known):** $260,000–$390,000 base + bonus + early-stage equity
- **Location / remote:** San Francisco, CA

## Full JD (captured via Greenhouse API)

**Company:** Lila Sciences — "Scientific Superintelligence"; AI models + AI Science Factory instruments,
an OS for science that runs the scientific method autonomously (medicine, materials, energy).

**Role:** Builder-leader. Own the **test automation platform, CI/CD test infra, AI-driven test tooling,
and the eval discipline** across the SDLC. Federated model — you own platform/standards/metrics; teams
own test execution; you scale via tooling + influence. Also stand up the **lab-automation QC framework**
(validation patterns, harnesses, contracts) with **ALCOA+ / data-integrity** foundations. Lead a small
(3–5) team.

### What you'll do
- **Architect & ship the test automation platform** — frameworks, fixtures, golden datasets, orchestration, reporting; standards across unit/integration/contract/E2E/regression/performance/chaos for backend, frontend monorepo, and data pipelines; treat adoption, flake rate, time-to-signal as first-class metrics.
- **Build-vs-buy with conviction** — test infra, eval platforms, browser/device clouds, observability, lab QC; justify by TCO / signal quality / integration cost; buy commodity, build differentiators.
- **Modernize CI/CD** — parallelization, caching, hermetic envs, ephemeral preview envs, affected-only test selection across an **Nx monorepo/microservices**; retry/quarantine/impact-analysis; drive change-failure rate, MTTR, pipeline efficiency, coverage, PR-to-prod lead time.
- **AI-driven test automation** — LLMs across the lifecycle: **test generation from specs/PRs**, self-healing UI tests, visual regression with vision models, AI-assisted triage; **validate every AI-generated test through evals**.
- **Quality metrics system** — SLOs and adoption metrics; dashboards PR→exec; apply Google SRE practices.
- **Lab-automation QC (mid-long term)** — validation framework/harnesses/contracts; embed **ALCOA+** (data integrity, audit trails, sample→instrument→output lineage).
- **Lead & coach** a 3–5 person platform team; coach other teams on test design/adoption.

### Required
- 10+ yrs SWE; 5+ yrs leading test automation / quality eng / platform-SRE-adjacent.
- 3+ yrs managing engineers, incl. building/scaling a team.
- Strong architect/engineer; **Python and/or TypeScript** hands-on.
- **Deep CI/CD** — GitHub Actions at scale, monorepo build/test orchestration (**Nx/Turborepo/Bazel**), parallelization/caching, hermetic + ephemeral envs, flake quarantine, test impact analysis.
- **Build-vs-buy judgment** (TCO / signal trade-offs).
- **Hands-on AI-driven test automation** — LLMs to generate/maintain/triage tests in production, **with rigorous eval validation; fluency with eval frameworks.**
- Track record standing up an adopted test-automation platform.
- Working knowledge of **Google SRE practices**.
- Metrics-driven; leverage & influence, not gatekeeping; customer/UX-first.

### Nice to have
- **GxP-regulated / scientific data integrity**; lab automation / **LIMS** / instrument-driven systems; multi-tenant SaaS at scale; event-driven / agent orchestration / **MCP**; performance/load or chaos engineering.

## My read — keyword & priority map

| JD theme | Fit | Proof |
|---|---|---|
| Test automation platform (adopted by default) | ✅ strong | Robot Framework platform (integration/E2E/regression + gating), cut regression days→<12h |
| AI-driven **test generation** | ✅ strong | TestBOT — Gemini agent auto-generates Robot Framework tests from specs |
| Deep CI/CD; monorepo (Bazel) | ✅ | GitHub Actions, Jenkins, **Bazel** (monorepo/hermetic), Gradle; pipeline gating |
| Build-vs-buy (TCO/signal) | ✅ (light) | Assessed/standardized AI tooling + models; vendor assessment |
| Quality metrics / SLOs / SRE | ✅ | observability & SLOs, 99.99%, DORA (KPI/DORA) |
| Performance/load testing | ✅ | Locust performance framework (Insulet), +25% |
| Lead small team; coach; influence | ✅ | led teams (7, 25–30); hire/mentor/coach |
| Python / TypeScript hands-on | ✅ | Python (strong); TypeScript via UniClaw (React/TS) |
| Regulated data integrity / ALCOA+-adjacent | ✅ adjacent | FDA-regulated med device (Insulet); regulated change control (ECO/SBR/PCO) + audit trails; ISO/SOC2 |
| Instrument-driven systems (LIMS-adjacent) | ✅ adjacent | TestBOT tests **OPC UA** industrial control systems; SCADA/OT |
| MCP / agent orchestration (nice-to-have) | ✅ | Lever + Slack-native MCP; miniBOT multi-agent |
| Static analysis / quality gates | ✅ | SonarQube, Coverity; pre-integration validation (Amazon) |
| **Eval discipline / eval frameworks** (REQUIRED) | ❌ **gap** | Has AI test-*generation* (TestBOT) but **no eval-validation discipline / eval frameworks** — NOT claimed |
| Nx / Turborepo | ⚠️ | Bazel monorepo yes; Nx/Turborepo not by name |
| Self-healing UI tests / visual-regression / flake-quarantine / affected-only / test-impact-analysis | ❌ | not built — don't claim; can discuss |
| Chaos engineering; browser/device clouds; multi-tenant SaaS | ❌ | not his background |

## Gaps / stretch areas
- **Eval discipline (the key gap).** This is a *required* qual and a core JD theme. Ishan has done the AI
  test-*generation* half (TestBOT) but not eval-validation / eval frameworks. Resume claims generation only;
  eval is the honest growth area. JD explicitly invites applicants who don't meet every qual — worth applying,
  but expect this to be probed. Prep a POV on eval (golden datasets, rubrics, regression suites, offline/online).
- **CI/CD-test-infra specifics** (flake quarantine, affected-only selection, test-impact analysis, Nx) — not
  built by name; Bazel/hermetic/gating/ephemeral are the honest anchors. Don't claim the rest.
- **Not built:** self-healing UI tests, visual regression (vision models), chaos engineering, browser/device
  clouds, multi-tenant SaaS. Kept out.
- Overall: **strong fit** on the platform + AI-test-generation + CI/CD + regulated-quality axes; one real
  required-qual gap (eval). Priority H.

## Tailoring checklist
- [x] Summary leads with test-automation platform + AI test generation (TestBOT) + CI/CD + regulated quality
- [x] TestBOT / Robot Framework platform surfaced as adopted-by-default platform work
- [x] OPC UA instrument testing surfaced (lab/instrument-driven adjacency); FDA/ALCOA+-adjacent surfaced
- [x] Eval NOT claimed; other not-built items (self-healing/visual/chaos) kept out
- [x] PDF exported → ../../resumes/head-of-automation/companies/lila-sciences/
