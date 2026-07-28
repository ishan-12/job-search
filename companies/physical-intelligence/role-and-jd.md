# Physical Intelligence — Build & Release Engineer

- **Resume:** `resumes/head-of-automation/companies/physical-intelligence/Resume_HeadOfAutomation_PhysicalIntelligence.md` (HoA track, IC-tuned)
- **Track:** Head of Automation, **re-tuned for an IC build-release role** — leads with hands-on build/CI-CD/Bazel/
  K8s/Terraform expertise rather than people management.
- **Link:** https://jobs.ashbyhq.com/physicalintelligence/f70f9481-ea7e-48e4-9212-f9c10952a028
- **Location:** San Francisco, CA. **Comp:** not listed.
- **Company:** Physical Intelligence (π) — robot foundation models / AI robotics.

## ⚠️ Level note
This is an **individual-contributor** "Build & Release Engineer" role — a level below Ishan's VP / Head-of-Automation
titles. He can do this work in his sleep (it mirrors his Amazon Redshift build/release ownership), but it is an IC
hire. Resume is positioned around **hands-on build & release engineering**; leadership is present but not the lead.
Decide whether the level/company trade-off is worth it.

## The Role (from the JD)

Senior infrastructure role focused on **developer productivity and build-system reliability** — own GitHub-based
CI/CD, Bazel builds, cloud infra, and Kubernetes services supporting the engineering team.

**Key responsibilities:**
- Design/operate **GitHub-based CI/CD** (GitHub Actions, checks, workflows) — reliability + speed.
- Manage/evolve **Bazel-based build systems** across **C++, Python, Rust, TypeScript**.
- Build/maintain **Kubernetes** services and infra with **Terraform**.
- Replace manual workflows with **self-service GitHub-integrated systems**.
- Reduce build failures, deploy issues, and CI bottlenecks affecting velocity.
- Partner cross-functionally on build optimization.

**Required:** strong GitHub workflows at scale; deep CI/CD; **Bazel** (or similar large-scale build system); cloud
+ Kubernetes + Terraform; strong developer-experience instincts.
**Preferred:** CI throughput improvements for large teams; Bazel optimization; **security-focused infra
automation**; **internal developer platform** experience.

## My read — keyword / priority map

| Theme | Fit | Proof |
|---|---|---|
| **GitHub-based CI/CD (Actions, checks, workflows) at scale** | ✅ bullseye | CI/CD across GitHub Actions, Jenkins; pipeline gating; Amazon CI/CD servers + multi-region build/deploy |
| **Bazel monorepo build systems** | ✅ bullseye | Bazel monorepo at CruxOCM; owned Redshift build system (C++) |
| **Polyglot builds (C++, Python, Rust, TypeScript)** | ✅ | Redshift build (C++); UniClaw (Python/TypeScript/Rust); Python/Bash |
| **Kubernetes + Terraform infra** | ✅ | K8s (EKS/GKE/AKS) + Terraform; GitOps |
| Self-service, replace manual workflows | ✅ | Self-service ephemeral environments; MCP/agents eliminating manual ops |
| **Reduce build failures / CI bottlenecks (velocity)** | ✅ bullseye | Bors-style automated merge queue (eliminated broken-mainline); DORA; pipeline-health metrics |
| Developer-experience instincts / developer productivity | ✅ | Developer-productivity charter; paved roads; DORA |
| **Security-focused infra automation** (preferred) | ✅ | SBOM; static-analysis scanning; encrypted secrets |
| **Internal developer platform** (preferred) | ✅ | Built internal developer platform / self-service infra |
| **Robotics / ML domain** | ⚠️ n/a | Not required — role is internal eng build/release infra; not claimed |
| Hands-on C++/Rust authoring | ⚠️ | Owned C++ build (Redshift), Rust in UniClaw (Tauri) — builds/tooling, not primary app authoring; framed honestly |

## Gaps / stretch areas
- **Technically a bullseye** — every required and preferred qualification maps directly; the Amazon Redshift
  build/release + merge-queue work is the exact profile. No material technical gaps.
- **The real consideration is LEVEL** — this is an IC role vs Ishan's leadership trajectory (see level note).
- Not overclaimed: hands-on C++/Rust *authoring* (owned the C++ build and shipped Rust via UniClaw/Tauri, but not
  a primary C++/Rust application developer); robotics domain.

## Tailoring checklist
- [x] HoA track, IC-tuned — leads with hands-on build/release/CI-CD/Bazel/K8s/Terraform
- [x] Amazon build/release + Bors merge queue foregrounded (exact match); GitHub Actions + Bazel + polyglot surfaced
- [x] Security-focused automation + internal developer platform (preferred) surfaced
- [x] Level note flagged; C++/Rust authoring and robotics domain not overclaimed
- [x] PDF exported → resumes/head-of-automation/companies/physical-intelligence/
