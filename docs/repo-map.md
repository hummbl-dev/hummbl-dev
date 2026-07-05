# HUMMBL Public Repo Map

Updated 2026-07-04 after the Fleet Bootstrap wave. See [`receipts/fleet-bootstrap-2026-07-04.md`](../receipts/fleet-bootstrap-2026-07-04.md) for the wave receipt and [`docs/REPO_MATURITY_MODEL.md`](REPO_MATURITY_MODEL.md) for maturity level definitions.

## How to read this map

Each repo is classified by:

- **Maturity** — `seed`, `v0.1-packet`, `active`, `canonical-candidate`, `canonical`, `hold` (see maturity model)
- **Surface type** — `implementation-bearing`, `pattern/reference`, `docs-first`, `distribution`, `profile`
- **Contributor readiness** — `open`, `scoped`, `closed`

## Core profile

| Repo | Maturity | Surface type | Contributor readiness | Role |
|---|---|---|---|---|
| [hummbl-dev/hummbl-dev](https://github.com/hummbl-dev/hummbl-dev) | active | profile | scoped | Public profile, repo inventory, fleet governance docs |
| [.github](https://github.com/hummbl-dev/.github) | active | profile | scoped | Shared contribution workflow and governance defaults |

## Implementation-bearing repos (code ships)

| Repo | Maturity | Surface type | Contributor readiness | Role |
|---|---|---|---|---|
| [hummbl-governance](https://github.com/hummbl-dev/hummbl-governance) | canonical | implementation-bearing | scoped | Governance runtime primitives (kill switch, circuit breaker, cost governor, delegation tokens) — on PyPI |
| [base120](https://github.com/hummbl-dev/base120) | canonical | implementation-bearing | scoped | Base120 mental-model substrate — v1.0.0 reference implementation |
| [arbiter](https://github.com/hummbl-dev/arbiter) | active | implementation-bearing | scoped | Agent-aware code quality scoring |
| [hummbl-agent](https://github.com/hummbl-dev/hummbl-agent) | active | implementation-bearing | scoped | TypeScript agent orchestration runtime |
| [mcp-server](https://github.com/hummbl-dev/mcp-server) | active | implementation-bearing | scoped | HUMMBL MCP Server |
| [hummbl-toolkit](https://github.com/hummbl-dev/hummbl-toolkit) | active | implementation-bearing | scoped | Supplementary tooling (evidence-gate, batch ingestion) |
| [bif](https://github.com/hummbl-dev/bif) | active | implementation-bearing | scoped | Batch Ingestion Framework |
| [governed-compression](https://github.com/hummbl-dev/governed-compression) | active | implementation-bearing | scoped | Governed vector/KV-cache compression research |
| [compendium-as-code](https://github.com/hummbl-dev/compendium-as-code) | active | implementation-bearing | scoped | Source-adapter for Compendium of Physical Activities |

## Research and reference repos

| Repo | Maturity | Surface type | Contributor readiness | Role |
|---|---|---|---|---|
| [hummbl-bibliography](https://github.com/hummbl-dev/hummbl-bibliography) | active | pattern/reference | open | Bibliography and citation corpus |
| [hummbl-papers](https://github.com/hummbl-dev/hummbl-papers) | active | pattern/reference | open | Research papers and reproducibility artifacts |
| [docs](https://github.com/hummbl-dev/docs) | active | docs-first | scoped | Public documentation surface |

## `*-as-code` pattern family (v0.1 packets)

All repos in this section received v0.1 packets during the 2026-07-04 Fleet Bootstrap. Each has: `docs/v0.1-boundary.md`, `docs/prior-art.md`, a JSON schema, valid/invalid fixtures, and a receipt. All are `seed`/`v0.1-packet` maturity — non-canon until explicitly adopted.

| Repo | Maturity | Surface type | Role |
|---|---|---|---|
| [infrastructure-as-code](https://github.com/hummbl-dev/infrastructure-as-code) | v0.1-packet | pattern/reference | Cloud/local/network/deployment infrastructure as code |
| [policy-as-code](https://github.com/hummbl-dev/policy-as-code) | v0.1-packet | pattern/reference | Security/compliance/access policies in executable form |
| [model-routing-as-code](https://github.com/hummbl-dev/model-routing-as-code) | v0.1-packet | pattern/reference | Model/provider selection rules, cost routing, fallback policy |
| [agent-as-code](https://github.com/hummbl-dev/agent-as-code) | v0.1-packet | pattern/reference | Agents, tools, permissions, prompts as auditable code |
| [observability-as-code](https://github.com/hummbl-dev/observability-as-code) | v0.1-packet | pattern/reference | Dashboards, alerts, SLOs, traces, logs as versioned artifacts |
| [governance-as-code](https://github.com/hummbl-dev/governance-as-code) | v0.1-packet | pattern/reference | Decision rights, review gates, escalation paths as code |
| [protocol-as-code](https://github.com/hummbl-dev/protocol-as-code) | v0.1-packet | pattern/reference | Workflows, checklists, runbooks as reusable protocol artifacts |
| [compliance-as-code](https://github.com/hummbl-dev/compliance-as-code) | v0.1-packet | pattern/reference | Controls, evidence, attestations, audit packets as code |
| [knowledge-as-code](https://github.com/hummbl-dev/knowledge-as-code) | v0.1-packet | pattern/reference | Definitions, source packets, vocabularies as versioned knowledge |
| [security-as-code](https://github.com/hummbl-dev/security-as-code) | v0.1-packet | pattern/reference | Threat models, hardening baselines, detection rules as code |

## Agent pattern repos (v0.1 packets)

All repos in this section received v0.1 packets during the 2026-07-04 Fleet Bootstrap. All are `seed`/`v0.1-packet` maturity — non-canon.

| Repo | Maturity | Surface type | Role |
|---|---|---|---|
| [agent-evaluation-patterns](https://github.com/hummbl-dev/agent-evaluation-patterns) | v0.1-packet | pattern/reference | Eval suites, rubrics, judge models, regression testing patterns |
| [agent-handoffs](https://github.com/hummbl-dev/agent-handoffs) | v0.1-packet | pattern/reference | Context transfer, delegation, session continuity patterns |
| [agent-control-plane-patterns](https://github.com/hummbl-dev/agent-control-plane-patterns) | v0.1-packet | pattern/reference | Control loops, reconciliation, desired-state patterns |
| [agent-instruction-format](https://github.com/hummbl-dev/agent-instruction-format) | v0.1-packet | pattern/reference | System prompts, instruction hierarchy, override rules |
| [agent-runtime-governance](https://github.com/hummbl-dev/agent-runtime-governance) | v0.1-packet | pattern/reference | Kill switches, circuit breakers, guardrails, admission control |
| [agentic-eng-patterns](https://github.com/hummbl-dev/agentic-eng-patterns) | v0.1-packet | pattern/reference | Agent loops, planning, memory, delegation, HITL patterns |
| [ai-source-verification](https://github.com/hummbl-dev/ai-source-verification) | v0.1-packet | pattern/reference | C2PA, provenance, content authenticity, tamper detection |
| [execution-receipts](https://github.com/hummbl-dev/execution-receipts) | v0.1-packet | pattern/reference | Execution records, input/output hashing, audit trails |
| [claim-evidence-ledger](https://github.com/hummbl-dev/claim-evidence-ledger) | v0.1-packet | pattern/reference | Append-only claim-evidence ledgers, provenance chains |
| [research-source-packets](https://github.com/hummbl-dev/research-source-packets) | v0.1-packet | pattern/reference | Source metadata, citation graphs, evidence grading |

## Package distribution spine

| Repo | Maturity | Surface type | Role |
|---|---|---|---|
| [packages](https://github.com/hummbl-dev/packages) | v0.1-packet | distribution | Canonical release index — identity, artifacts, checksums, SBOM, provenance |
| [homebrew-tap](https://github.com/hummbl-dev/homebrew-tap) | v0.1-packet | distribution | Downstream generated Homebrew tap (from packages) |
| [scoop-bucket](https://github.com/hummbl-dev/scoop-bucket) | v0.1-packet | distribution | Downstream generated Scoop bucket (from packages) |
| [winget-manifests](https://github.com/hummbl-dev/winget-manifests) | v0.1-packet | distribution | Downstream generated winget manifests (from packages) |
| [nix](https://github.com/hummbl-dev/nix) | v0.1-packet | distribution | Downstream generated Nix flakes/overlays/devShells (from packages) |

## Pending decision surfaces

These repos have open decision issues requiring operator authority. Do not extend without explicit decision.

| Repo | Issue | Decision needed |
|---|---|---|
| [homebrew-hummbl](https://github.com/hummbl-dev/homebrew-hummbl) | #3 | Choose canonical Homebrew tap surface (homebrew-hummbl vs homebrew-tap) |
| [mintlify-docs](https://github.com/hummbl-dev/mintlify-docs) | #3 | Choose canonical docs source-of-record (docs vs mintlify-docs) |

## Dependency graph

```text
packages (canonical identity + receipts)
  ├── homebrew-tap (generated)
  ├── scoop-bucket (generated)
  ├── winget-manifests (generated)
  └── nix (generated)

hummbl-governance (canonical primitives)
  └── referenced by: agent-runtime-governance, governance-as-code, arbiter

base120 (canonical substrate)
  └── referenced by: hummbl-agent, hummbl-bibliography

*-as-code family (pattern/reference, non-canon)
  └── no downstream dependencies yet

agent pattern repos (pattern/reference, non-canon)
  └── no downstream dependencies yet
```

## How contributors should route work

1. Check this map for repo maturity and surface type.
2. `seed` / `v0.1-packet` repos accept docs/schema/fixture contributions only — no runtime changes.
3. `active` / `canonical` repos have scoped contribution paths — read their CONTRIBUTING.md.
4. `hold` repos are frozen pending operator decision — do not extend.
5. Start with an issue. Preserve receipts. Propose changes as PRs.

## First five minutes for new contributors

1. Read this repo map.
2. Pick a repo matching your interest and check its maturity level.
3. Open the linked repo and read its `docs/v0.1-boundary.md` (if v0.1-packet) or README.
4. Check open issues and PRs before starting work.
5. Follow issue-first workflow with receipts.

## Candidate Repo Admission Queue

Issue `hummbl-dev#86` is the current planning packet for next-wave repo candidates. Candidate names are not authorization to create repos. Each accepted repo still needs a namespace check, public/private boundary, non-scope, status posture, and receipt-bearing scaffold before creation or promotion.

### Hard Gates

- Run exact GitHub namespace/collision checks immediately before creation.
- Classify the repo as public, private, or private-first/public-later.
- Write initial README scope and non-scope before promotion.
- Mark experimental surfaces as candidate/non-canonical.
- Avoid names that imply official standardization, medical authority, universal adoption, or category ownership without receipts.
- Seed accepted repos with contribution, security, status, receipt, and ADR scaffolding.

### Explicit Deferrals

- `ownward-dogfood` and `hummbl-behavior-change` stay private or private-first.
- `hummbl-cli` waits until command scope and package boundaries are smaller.
- `basen-lab` requires non-canonical status language before public creation.
- `agentic-arbitrage` and `model-arbitrage` require public-claim review before naming or launch.
- Names implying external standard status, universal protocols, or medical authority remain rejected unless a later receipt changes the risk posture.
