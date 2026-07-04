# HUMMBL

Governance infrastructure for AI agents.

HUMMBL builds small, inspectable control-plane primitives for agentic systems: delegation tokens, append-only receipts, kill switches, circuit breakers, capability fences, source-verification gates, and review workflows that create evidence while the system runs.

This repository is the public HUMMBL profile, repo directory, agent coordination surface, and collaboration router for the `hummbl-dev` account.

The bias is explicit:

- **libraries over platforms** — controls should live in the execution path, not only in a dashboard after the fact
- **receipts over vibes** — every governance claim should leave an audit trail
- **stdlib-first primitives** — core safety controls should survive constrained, regulated, and air-gapped environments
- **human override preserved** — automation assists governance; it does not become the sovereign

```bash
pip install hummbl-governance
```

[![PyPI](https://img.shields.io/pypi/v/hummbl-governance)](https://pypi.org/project/hummbl-governance/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](LICENSE)
[![Runtime deps](https://img.shields.io/badge/runtime%20deps-zero-brightgreen)](https://pypi.org/project/hummbl-governance/)

---

## Start Here

| Need | Repository |
|---|---|
| Runtime governance primitives | [`hummbl-governance`](https://github.com/hummbl-dev/hummbl-governance) |
| Mental-model substrate | [`base120`](https://github.com/hummbl-dev/base120) |
| Source-verification gate | [`evidence-gate`](https://github.com/hummbl-dev/evidence-gate) |
| Code quality and governance scoring | [`arbiter`](https://github.com/hummbl-dev/arbiter) |
| MCP access to HUMMBL models and skills | [`mcp-server`](https://github.com/hummbl-dev/mcp-server) |
| Agent orchestration patterns | [`hummbl-agent`](https://github.com/hummbl-dev/hummbl-agent) |
| Research and citation corpus | [`hummbl-bibliography`](https://github.com/hummbl-dev/hummbl-bibliography) |
| Public profile, tools, and repo inventory | [`hummbl-dev`](https://github.com/hummbl-dev/hummbl-dev) |

New contributors should start with [`hummbl-governance`](https://github.com/hummbl-dev/hummbl-governance), [`base120`](https://github.com/hummbl-dev/base120), [`arbiter`](https://github.com/hummbl-dev/arbiter), [`mcp-server`](https://github.com/hummbl-dev/mcp-server), or [`hummbl-agent`](https://github.com/hummbl-dev/hummbl-agent), depending on whether they want runtime controls, mental-model infrastructure, code review automation, MCP interfaces, or orchestration patterns. Cross-repo proposals and public profile changes belong in this repo's issues.

For public collaboration routing, agent routing, and repo maturity tags, see:

- [Public Collaboration](docs/PUBLIC_COLLABORATION.md)
- [Agent Routing](docs/AGENT_ROUTING.md)
- [Repo Maturity Model](docs/REPO_MATURITY_MODEL.md)

---

## Repo Boundaries

This repository is the **public HUMMBL profile, static-tools, and documentation surface**.

It is **not** the source of truth for:

- internal operator workflow
- private repo governance
- live runtime or queue state
- draft cross-repo planning proposals

Some files are retained here as agent workflow scaffolding or dated planning artifacts. Treat them as internal or draft material unless they are explicitly linked from the public sections of this README or from [CONTRIBUTING.md](CONTRIBUTING.md).

Planning artifacts live under [`docs/plans/`](docs/plans/). They are useful for context, but they are not public commitments or adopted org-wide doctrine by default.

---

## Repository Directory

| Category | Repositories |
|---|---|
| Governance primitives | [`hummbl-governance`](https://github.com/hummbl-dev/hummbl-governance), [`agent-governance-demo`](https://github.com/hummbl-dev/agent-governance-demo), [`evidence-gate`](https://github.com/hummbl-dev/evidence-gate) |
| Agent systems | [`hummbl-agent`](https://github.com/hummbl-dev/hummbl-agent), [`mcp-server`](https://github.com/hummbl-dev/mcp-server), [`hummbl-iac`](https://github.com/hummbl-dev/hummbl-iac) |
| Review and quality | [`arbiter`](https://github.com/hummbl-dev/arbiter), source-verification rules, governed PR review workflows |
| Cognitive substrate | [`base120`](https://github.com/hummbl-dev/base120), [`hummbl-theory`](https://github.com/hummbl-dev/hummbl-theory), [`hummbl-bibliography`](https://github.com/hummbl-dev/hummbl-bibliography), [`arcana`](https://github.com/hummbl-dev/arcana) |
| Product and applied research | [`fractional-bench`](https://github.com/hummbl-dev/fractional-bench), `coaching`, `hummbl-production` |
| ML systems and benchmarking | _planned: local-inference-bench, agent-governance-harness, tiny-jax-transformer, kernel-harness, post-training-toolkit_ |
| Public tools and content | [`hummbl-dev`](https://github.com/hummbl-dev/hummbl-dev), static readiness tools, research essays, public profile assets |
| Experimental public repos | `autoresearch`, `governed-compression`, `sint-protocol`, `bif` |

Some repositories are private while they contain operator workflows, client-sensitive research, or active product work. Public repositories are the durable reference surface.

Contribution process and accepted contribution types are documented in [`CONTRIBUTING.md`](CONTRIBUTING.md). Some repositories are internal-only; open an issue in the target repo before submitting a PR.

### `*-as-code` Seed Family

`*-as-code` means treating an operational domain as version-controlled, reviewable, testable, auditable, and agent-operable source material. These repos are early public seeds and are not adopted HUMMBL canon unless later marked and audited.

| Status | Repository | Domain |
|---|---|---|
| `seed` | [`infrastructure-as-code`](https://github.com/hummbl-dev/infrastructure-as-code) | Cloud, local, network, runtime, and deployment infrastructure |
| `seed` | [`governance-as-code`](https://github.com/hummbl-dev/governance-as-code) | Decision rights, review gates, escalation paths, and operating constraints |
| `seed` | [`agent-as-code`](https://github.com/hummbl-dev/agent-as-code) | Agents, tools, permissions, prompts, evals, handoffs, and execution contracts |
| `seed` | [`policy-as-code`](https://github.com/hummbl-dev/policy-as-code) | Security, compliance, access, and operational policies |
| `seed` | [`security-as-code`](https://github.com/hummbl-dev/security-as-code) | Threat models, hardening baselines, detection rules, and secure defaults |
| `seed` | [`compliance-as-code`](https://github.com/hummbl-dev/compliance-as-code) | Controls, evidence, attestations, obligations, and audit packets |
| `seed` | [`protocol-as-code`](https://github.com/hummbl-dev/protocol-as-code) | Workflows, checklists, runbooks, playbooks, and safety procedures |
| `seed` | [`knowledge-as-code`](https://github.com/hummbl-dev/knowledge-as-code) | Definitions, source packets, vocabularies, claims, citations, and ledgers |
| `seed` | [`model-routing-as-code`](https://github.com/hummbl-dev/model-routing-as-code) | Model/provider selection, correctness gates, cost routing, fallback policy, and eval thresholds |
| `seed` | [`observability-as-code`](https://github.com/hummbl-dev/observability-as-code) | Dashboards, alerts, SLOs, traces, logs, metrics, runbooks, and visibility primitives |

---

## What HUMMBL Means by Governance

Governance is not a policy PDF. It is a runtime property:

1. **Who is acting?** Agent identity, trust tier, and delegation scope.
2. **What authority do they have?** Signed capability tokens and bounded tools.
3. **What happened?** Append-only receipts, bus messages, and evidence logs.
4. **What should stop the system?** Kill switches, circuit breakers, cost governors, and review gates.
5. **What can be audited later?** Source manifests, PR reviews, test evidence, and structured findings.

That is the spine across the org: small primitives that make governance observable, testable, and reviewable.

---

## By The Numbers

Inventory captured on 2026-07-04:

| Metric | Count |
|---|---:|
| Total repositories | 128 |
| Active public repositories | 25 |
| Active private repositories | 69 |
| Archived repositories | 34 |
| Primary language family | Python-heavy, with TypeScript, HTML, Shell, TeX, Go templates, Java |

Historical repo inventory: [`docs/GITHUB_REPO_INVENTORY_2026-05-08.md`](docs/GITHUB_REPO_INVENTORY_2026-05-08.md)

Latest branch cleanup audit: [`docs/BRANCH_CLEANUP_AUDIT_2026-05-08.md`](docs/BRANCH_CLEANUP_AUDIT_2026-05-08.md)

Current archive posture: [`docs/ARCHIVE_POSTURE_2026-05-13.md`](docs/ARCHIVE_POSTURE_2026-05-13.md)

Archived repo retention tracker: [`docs/ARCHIVED_REPO_RETENTION_2026-05-13.md`](docs/ARCHIVED_REPO_RETENTION_2026-05-13.md)

Merge queue issue-closure semantics: [`docs/MERGE_QUEUE_ISSUE_CLOSURE.md`](docs/MERGE_QUEUE_ISSUE_CLOSURE.md)

---

## Research

HUMMBL's public thesis is that AI governance will move from abstract policy to runtime evidence. The research corpus tracks:

- AI-generated code risk and liability
- agentic control-plane design
- source verification before publication
- governance receipts and audit trails
- mental-model infrastructure for agent reasoning
- practical compliance mapping across NIST AI RMF, ISO 42001, EU AI Act, OWASP, and related frameworks

Useful entry points:

- [AI slop crisis research corpus](docs/research/ai-slop-crisis/README.md)
- [Why libraries, not platforms](docs/research/ai-slop-crisis/essays/why-libraries-not-platforms.md)
- [Reasonable care in the age of AI agents](docs/research/ai-slop-crisis/essays/reasonable-care-age-of-agents.md)
- [The observability argument](docs/research/ai-slop-crisis/essays/the-observability-argument.md)

Before reusing public proof or research claims externally, read the repo-level [Proof and Research Evidence Posture](docs/PROOF_AND_RESEARCH_EVIDENCE_POSTURE.md).

---

## Tools

Free self-assessments and references:

| Tool | Purpose |
|---|---|
| [Tool index](index.html) | Landing page for the public tools in this repo |
| [EU AI Act readiness](eu-ai-act-readiness.html) | Governance posture check |
| [NIST AI RMF readiness](nist-ai-rmf-readiness.html) | Framework-aligned assessment |
| [ISO 42001 readiness](iso-42001-readiness.html) | AI management system checklist |
| [Singapore agentic AI readiness](singapore-agentic-readiness.html) | Agent governance architecture assessment |
| [Colorado AI Act readiness](colorado-ai-act-readiness.html) | State-level algorithmic decision compliance |
| [Compliance calendar](compliance-calendar.html) | AI governance timeline |
| [Governance crosswalk](governance-crosswalk.html) | Framework comparison |

---

## CI Posture

This repository is the HUMMBL organization profile, public documentation surface, and static tool portfolio. It does not currently run GitHub Actions because there is no build step, package release, or testable runtime in this repo.

Validation is manual for now:

- Review Markdown changes in rendered GitHub preview.
- Open changed HTML tools locally in a browser before publication.
- Keep executable code, packages, and service workflows in their dedicated project repositories, where CI is configured per repo.

If this repository gains generated assets, JavaScript modules, or release automation, add the smallest useful CI workflow for that surface.

---

## Work With HUMMBL

If you are building agentic systems and need runtime governance, source verification, auditability, or public/private agent workflow design, start with the repos above or contact reuben@hummbl.io.

---

## Contact

HUMMBL, LLC is founded by **Reuben Bowlby** in Atlanta, GA.

- Site: [hummbl.io](https://hummbl.io)
- Email: reuben@hummbl.io
- Package: [`hummbl-governance` on PyPI](https://pypi.org/project/hummbl-governance/)

*Governed agents need receipts, not slogans.*
