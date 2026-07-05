# HUMMBL

HUMMBL builds governance and release infrastructure for agentic work.

AI agents can increasingly do real work. But real work requires authority, review, receipts, rollback, provenance, memory discipline, and human accountability to stay trustworthy.

Our first mission is to make agentic engineering reliable for teams actually shipping with agents.

This repository is the public HUMMBL profile, repo directory, agent coordination surface, and collaboration router for the `hummbl-dev` account.

The bias is explicit:

- **governance over hype** — controls should preserve reviewability before and after execution
- **receipts over vibes** — every governance claim leaves append-only evidence
- **small primitives over platforms** — controls run in execution paths, not only dashboards
- **human accountability preserved** — automation assists operators, it does not replace review

## 90-second overview

- **What HUMMBL is** — governance and release infrastructure for agentic work. Small primitives (kill switches, circuit breakers, cost governors, delegation tokens, execution receipts) that make agent work inspectable, reviewable, and shippable.
- **What Base120 is** — the mental-model substrate behind HUMMBL reasoning and routing. A v1.0.0 reference implementation lives in [`base120`](https://github.com/hummbl-dev/base120).
- **What governed agentic work means** — every action has identity, authority, receipts, rollback, and audit. Governance is a runtime property, not a policy PDF.
- **Which repos are canonical** — [`hummbl-governance`](https://github.com/hummbl-dev/hummbl-governance) and [`base120`](https://github.com/hummbl-dev/base120) are canonical. Everything else is `active`, `v0.1-packet`, `seed`, or `hold` until explicitly promoted.
- **Where new contributors should begin** — [`START_HERE.md`](START_HERE.md) routes you by contributor type. Pick a repo matching your interest, check its maturity in [`docs/repo-map.md`](docs/repo-map.md), open an issue first.
- **What not to touch yet** — `homebrew-hummbl` and `mintlify-docs` have open decision issues. Any repo marked `hold` is frozen. `seed` / `v0.1-packet` repos accept docs/schema/fixture contributions only — no runtime changes.

## Public positioning

**HUMMBL makes agentic work trustworthy, inspectable, and shippable.**

Ownward is an applied product for founder-operators using this governance layer.

BaseN is the reasoning and routing substrate behind the system.

First buyers: engineering leaders and founder-led technical teams adopting AI agents who need review, provenance, release risk management, and accountable delegation.

```bash
pip install hummbl-governance
```

[![PyPI](https://img.shields.io/pypi/v/hummbl-governance)](https://pypi.org/project/hummbl-governance/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](LICENSE)
[![Runtime deps](https://img.shields.io/badge/runtime%20deps-zero-brightgreen)](https://pypi.org/project/hummbl-governance/)

---

## Start Here

New visitors: start with [`START_HERE.md`](START_HERE.md). The table below maps the v0.1-packet fleet categories to entry repos.

| Need | Repository |
|---|---|
| Runtime governance primitives (canonical) | [`hummbl-governance`](https://github.com/hummbl-dev/hummbl-governance) |
| Mental-model substrate (canonical) | [`base120`](https://github.com/hummbl-dev/base120) |
| Code quality and governance scoring | [`arbiter`](https://github.com/hummbl-dev/arbiter) |
| MCP access to HUMMBL models and skills | [`mcp-server`](https://github.com/hummbl-dev/mcp-server) |
| Agent orchestration runtime | [`hummbl-agent`](https://github.com/hummbl-dev/hummbl-agent) |
| Agent pattern repos (v0.1-packet) | [`agent-runtime-governance`](https://github.com/hummbl-dev/agent-runtime-governance), [`agent-handoffs`](https://github.com/hummbl-dev/agent-handoffs), [`agentic-eng-patterns`](https://github.com/hummbl-dev/agentic-eng-patterns) |
| `*-as-code` family (v0.1-packet) | [`governance-as-code`](https://github.com/hummbl-dev/governance-as-code), [`policy-as-code`](https://github.com/hummbl-dev/policy-as-code), [`compliance-as-code`](https://github.com/hummbl-dev/compliance-as-code) |
| Package distribution spine (v0.1-packet) | [`packages`](https://github.com/hummbl-dev/packages), [`homebrew-tap`](https://github.com/hummbl-dev/homebrew-tap), [`nix`](https://github.com/hummbl-dev/nix) |
| Research and citation corpus | [`hummbl-bibliography`](https://github.com/hummbl-dev/hummbl-bibliography) |
| Public profile, tools, and repo inventory | [`hummbl-dev`](https://github.com/hummbl-dev/hummbl-dev) |

For public collaboration routing, agent routing, and repo maturity tags, see:

- [Start Here](START_HERE.md)
- [Contributor Paths](docs/contributor-paths.md)
- [Public Collaboration](docs/PUBLIC_COLLABORATION.md)
- [Repo Map](docs/repo-map.md)
- [Repo Maturity Model](docs/REPO_MATURITY_MODEL.md)

---

## Repo Boundaries

This repository is the **public HUMMBL profile, static-tools, and documentation surface**. It is not the source of truth for internal operator workflow, private repo governance, live runtime or queue state, or draft cross-repo planning proposals.

Some files are retained here as agent workflow scaffolding or dated planning artifacts. Treat them as internal or draft material unless explicitly linked from the public sections of this README or from [CONTRIBUTING.md](CONTRIBUTING.md). Planning artifacts live under [`docs/plans/`](docs/plans/) — useful for context, not public commitments.

---

## Repository Directory

Categories match [`docs/repo-map.md`](docs/repo-map.md). Maturity tags are defined in [`docs/REPO_MATURITY_MODEL.md`](docs/REPO_MATURITY_MODEL.md).

### Implementation-bearing (code ships)

| Repo | Maturity | Role |
|---|---|---|
| [`hummbl-governance`](https://github.com/hummbl-dev/hummbl-governance) | canonical | Governance runtime primitives — on PyPI |
| [`base120`](https://github.com/hummbl-dev/base120) | canonical | Base120 mental-model substrate — v1.0.0 |
| [`arbiter`](https://github.com/hummbl-dev/arbiter) | active | Agent-aware code quality scoring |
| [`hummbl-agent`](https://github.com/hummbl-dev/hummbl-agent) | active | TypeScript agent orchestration runtime |
| [`mcp-server`](https://github.com/hummbl-dev/mcp-server) | active | HUMMBL MCP Server |
| [`hummbl-toolkit`](https://github.com/hummbl-dev/hummbl-toolkit) | active | Supplementary tooling |
| [`bif`](https://github.com/hummbl-dev/bif) | active | Batch Ingestion Framework |
| [`governed-compression`](https://github.com/hummbl-dev/governed-compression) | active | Governed vector/KV-cache compression research |
| [`compendium-as-code`](https://github.com/hummbl-dev/compendium-as-code) | active | Source-adapter for Compendium of Physical Activities |

### Pattern / reference

| Repo | Maturity | Role |
|---|---|---|
| [`hummbl-bibliography`](https://github.com/hummbl-dev/hummbl-bibliography) | active | Bibliography and citation corpus |
| [`hummbl-papers`](https://github.com/hummbl-dev/hummbl-papers) | active | Research papers and reproducibility artifacts |

### Distribution

| Repo | Maturity | Role |
|---|---|---|
| [`packages`](https://github.com/hummbl-dev/packages) | v0.1-packet | Canonical release index — identity, artifacts, checksums, SBOM, provenance |
| [`homebrew-tap`](https://github.com/hummbl-dev/homebrew-tap) | v0.1-packet | Generated Homebrew tap (from packages) |
| [`scoop-bucket`](https://github.com/hummbl-dev/scoop-bucket) | v0.1-packet | Generated Scoop bucket (from packages) |
| [`winget-manifests`](https://github.com/hummbl-dev/winget-manifests) | v0.1-packet | Generated winget manifests (from packages) |
| [`nix`](https://github.com/hummbl-dev/nix) | v0.1-packet | Generated Nix flakes/overlays/devShells (from packages) |

### Profile

| Repo | Maturity | Role |
|---|---|---|
| [`hummbl-dev`](https://github.com/hummbl-dev/hummbl-dev) | active | Public profile, repo inventory, fleet governance docs |
| [`.github`](https://github.com/hummbl-dev/.github) | active | Shared contribution workflow and governance defaults |

Some repositories are private while they contain operator workflows, client-sensitive research, or active product work. Public repositories are the durable reference surface.

Contribution process and accepted contribution types are documented in [`CONTRIBUTING.md`](CONTRIBUTING.md). Some repositories are internal-only; open an issue in the target repo before submitting a PR.

### `*-as-code` pattern family (v0.1 packets)

`*-as-code` means treating an operational domain as version-controlled, reviewable, testable, auditable, and agent-operable source material. All repos below received v0.1 packets during the 2026-07-04 Fleet Bootstrap and are non-canon until explicitly adopted.

| Status | Repository | Domain |
|---|---|---|
| `v0.1-packet` | [`infrastructure-as-code`](https://github.com/hummbl-dev/infrastructure-as-code) | Cloud, local, network, runtime, and deployment infrastructure |
| `v0.1-packet` | [`governance-as-code`](https://github.com/hummbl-dev/governance-as-code) | Decision rights, review gates, escalation paths, and operating constraints |
| `v0.1-packet` | [`agent-as-code`](https://github.com/hummbl-dev/agent-as-code) | Agents, tools, permissions, prompts, evals, handoffs, and execution contracts |
| `v0.1-packet` | [`policy-as-code`](https://github.com/hummbl-dev/policy-as-code) | Security, compliance, access, and operational policies |
| `v0.1-packet` | [`security-as-code`](https://github.com/hummbl-dev/security-as-code) | Threat models, hardening baselines, detection rules, and secure defaults |
| `v0.1-packet` | [`compliance-as-code`](https://github.com/hummbl-dev/compliance-as-code) | Controls, evidence, attestations, obligations, and audit packets |
| `v0.1-packet` | [`protocol-as-code`](https://github.com/hummbl-dev/protocol-as-code) | Workflows, checklists, runbooks, playbooks, and safety procedures |
| `v0.1-packet` | [`knowledge-as-code`](https://github.com/hummbl-dev/knowledge-as-code) | Definitions, source packets, vocabularies, claims, citations, and ledgers |
| `v0.1-packet` | [`model-routing-as-code`](https://github.com/hummbl-dev/model-routing-as-code) | Model/provider selection, correctness gates, cost routing, fallback policy |
| `v0.1-packet` | [`observability-as-code`](https://github.com/hummbl-dev/observability-as-code) | Dashboards, alerts, SLOs, traces, logs, metrics, runbooks, and visibility primitives |

### Agent pattern repos (v0.1 packets)

All repos below received v0.1 packets during the 2026-07-04 Fleet Bootstrap. All are non-canon.

| Repo | Role |
|---|---|
| [`agent-evaluation-patterns`](https://github.com/hummbl-dev/agent-evaluation-patterns) | Eval suites, rubrics, judge models, regression testing patterns |
| [`agent-handoffs`](https://github.com/hummbl-dev/agent-handoffs) | Context transfer, delegation, session continuity patterns |
| [`agent-control-plane-patterns`](https://github.com/hummbl-dev/agent-control-plane-patterns) | Control loops, reconciliation, desired-state patterns |
| [`agent-instruction-format`](https://github.com/hummbl-dev/agent-instruction-format) | System prompts, instruction hierarchy, override rules |
| [`agent-runtime-governance`](https://github.com/hummbl-dev/agent-runtime-governance) | Kill switches, circuit breakers, guardrails, admission control |
| [`agentic-eng-patterns`](https://github.com/hummbl-dev/agentic-eng-patterns) | Agent loops, planning, memory, delegation, HITL patterns |
| [`ai-source-verification`](https://github.com/hummbl-dev/ai-source-verification) | C2PA, provenance, content authenticity, tamper detection |
| [`execution-receipts`](https://github.com/hummbl-dev/execution-receipts) | Execution records, input/output hashing, audit trails |
| [`claim-evidence-ledger`](https://github.com/hummbl-dev/claim-evidence-ledger) | Append-only claim-evidence ledgers, provenance chains |
| [`research-source-packets`](https://github.com/hummbl-dev/research-source-packets) | Source metadata, citation graphs, evidence grading |

### Pending decisions

These repos have open decision issues requiring operator authority. Do not extend without explicit decision.

| Repo | Issue | Decision needed |
|---|---|---|
| [`homebrew-hummbl`](https://github.com/hummbl-dev/homebrew-hummbl) | #3 | Choose canonical Homebrew tap surface (homebrew-hummbl vs homebrew-tap) |
| [`mintlify-docs`](https://github.com/hummbl-dev/mintlify-docs) | #3 | Choose canonical docs source-of-record (docs vs mintlify-docs) |

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

Inventory captured on 2026-07-04. Public-safe snapshot: [`docs/GITHUB_REPO_INVENTORY_2026-07-04.md`](docs/GITHUB_REPO_INVENTORY_2026-07-04.md)

| Metric | Count |
|---|---:|
| Total repositories | 128 |
| Active public repositories | 41 |
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

HUMMBL's public thesis is that AI governance will move from abstract policy to runtime evidence. The research corpus tracks AI-generated code risk, agentic control-plane design, source verification, governance receipts, mental-model infrastructure, and practical compliance mapping (NIST AI RMF, ISO 42001, EU AI Act, OWASP).

Useful entry points:

- [AI slop crisis research corpus](docs/research/ai-slop-crisis/README.md)
- [Why libraries, not platforms](docs/research/ai-slop-crisis/essays/why-libraries-not-platforms.md)
- [Reasonable care in the age of AI agents](docs/research/ai-slop-crisis/essays/reasonable-care-age-of-agents.md)
- [The observability argument](docs/research/ai-slop-crisis/essays/the-observability-argument.md)

Before reusing public proof or research claims externally, read [Proof and Research Evidence Posture](docs/PROOF_AND_RESEARCH_EVIDENCE_POSTURE.md).

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

This repository has no build step, package release, or testable runtime, so it does not run GitHub Actions. Validation is manual: review Markdown in rendered GitHub preview, open changed HTML tools locally before publication, and keep executable code in its dedicated project repo where CI is configured per repo. If this repo gains generated assets or release automation, add the smallest useful CI workflow for that surface.

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
