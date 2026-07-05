# Contributor Paths

Detailed routing for each contributor type listed in [`START_HERE.md`](../START_HERE.md). Pick the path that matches your interest, read the first-read list, then open an issue before submitting a PR.

## Agent engineer

- **What you'd work on** — runtime guardrails, handoff contracts, control-plane loops for agent systems.
- **Repos** — [`agent-runtime-governance`](https://github.com/hummbl-dev/agent-runtime-governance), [`agent-handoffs`](https://github.com/hummbl-dev/agent-handoffs), [`agent-control-plane-patterns`](https://github.com/hummbl-dev/agent-control-plane-patterns), [`hummbl-agent`](https://github.com/hummbl-dev/hummbl-agent).
- **Skills that help** — TypeScript/Python, agent runtimes, control-loop design, HITL patterns.
- **Read first** — the repo's `docs/v0.1-boundary.md`, then [`docs/repo-map.md`](repo-map.md).
- **Good first contributions** — fixture additions for handoff schemas, edge-case examples in `agent-control-plane-patterns`, doc clarifications on kill-switch semantics.

## Governance / policy person

- **What you'd work on** — decision rights, review gates, escalation paths, compliance controls as versioned code.
- **Repos** — [`governance-as-code`](https://github.com/hummbl-dev/governance-as-code), [`policy-as-code`](https://github.com/hummbl-dev/policy-as-code), [`compliance-as-code`](https://github.com/hummbl-dev/compliance-as-code), [`security-as-code`](https://github.com/hummbl-dev/security-as-code).
- **Skills that help** — policy frameworks (NIST AI RMF, ISO 42001, EU AI Act), control mapping, audit evidence.
- **Read first** — `docs/v0.1-boundary.md` and `docs/prior-art.md` in each repo.
- **Good first contributions** — schema fixtures mapping a control to evidence, prior-art additions, glossary terms in `knowledge-as-code`.

## Package / release engineer

- **What you'd work on** — canonical release index, generated downstream taps, provenance and SBOM posture.
- **Repos** — [`packages`](https://github.com/hummbl-dev/packages), [`homebrew-tap`](https://github.com/hummbl-dev/homebrew-tap), [`scoop-bucket`](https://github.com/hummbl-dev/scoop-bucket), [`winget-manifests`](https://github.com/hummbl-dev/winget-manifests), [`nix`](https://github.com/hummbl-dev/nix).
- **Skills that help** — Homebrew/Scoop/winget/Nix packaging, SBOM, provenance, release automation.
- **Read first** — `packages` README and the dependency graph in [`docs/repo-map.md`](repo-map.md). Note: `homebrew-hummbl` vs `homebrew-tap` is an open decision — do not extend either without operator sign-off.
- **Good first contributions** — fixture manifests, validation rule docs, checksum schema examples.

## Evidence / research person

- **What you'd work on** — append-only ledgers, source provenance, citation graphs, content authenticity.
- **Repos** — [`claim-evidence-ledger`](https://github.com/hummbl-dev/claim-evidence-ledger), [`research-source-packets`](https://github.com/hummbl-dev/research-source-packets), [`ai-source-verification`](https://github.com/hummbl-dev/ai-source-verification), [`hummbl-bibliography`](https://github.com/hummbl-dev/hummbl-bibliography).
- **Skills that help** — C2PA/provenance, evidence grading, bibliographic metadata.
- **Read first** — `docs/v0.1-boundary.md` in each repo, then [`docs/PROOF_AND_RESEARCH_EVIDENCE_POSTURE.md`](PROOF_AND_RESEARCH_EVIDENCE_POSTURE.md).
- **Good first contributions** — source-packet fixtures, evidence-grading examples, citation-graph schema cases.

## Pattern designer

- **What you'd work on** — reusable agentic engineering patterns, instruction formats, execution receipts.
- **Repos** — [`agentic-eng-patterns`](https://github.com/hummbl-dev/agentic-eng-patterns), [`agent-instruction-format`](https://github.com/hummbl-dev/agent-instruction-format), [`execution-receipts`](https://github.com/hummbl-dev/execution-receipts), [`agent-evaluation-patterns`](https://github.com/hummbl-dev/agent-evaluation-patterns).
- **Skills that help** — pattern-language writing, schema design, eval rubrics.
- **Read first** — `docs/v0.1-boundary.md` and existing fixtures in each repo.
- **Good first contributions** — new pattern fixtures, edge-case examples for instruction hierarchy, receipt schema variants.

## Tool builder

- **What you'd work on** — runtime primitives, mental-model substrate, code quality scoring, MCP interfaces.
- **Repos** — [`hummbl-governance`](https://github.com/hummbl-dev/hummbl-governance), [`base120`](https://github.com/hummbl-dev/base120), [`arbiter`](https://github.com/hummbl-dev/arbiter), [`mcp-server`](https://github.com/hummbl-dev/mcp-server).
- **Skills that help** — Python, TypeScript, MCP protocol, scoring/rule design.
- **Read first** — each repo's CONTRIBUTING.md and README. These are `canonical` or `active` — scoped contributions with review gates.
- **Good first contributions** — tests, bug fixes, rule additions in `arbiter`, MCP tool implementations in `mcp-server`.

## What agents can and cannot do

- **Agents can** work on docs, schema, and fixture contributions in `v0.1-packet` repos. Agents can open issues, draft PRs, and surface blockers.
- **Agents cannot** make canonical decisions, promote repos, close decision issues, or extend `hold` repos. Operator-authority issues (see Bucket 1 in [`FLEET_REMAINING_ISSUES_2026-07-04.md`](FLEET_REMAINING_ISSUES_2026-07-04.md)) must not be auto-completed.
- **Agents must** preserve receipts: link the issue, cite prior art, and document the boundary of the change. If a task touches operator authority, stop and surface the blocker instead of proceeding.

## Cross-repo proposals

Changes that span multiple public HUMMBL repos belong in `hummbl-dev` as a cross-repo proposal issue, not as scattered PRs across repos. State the target repos, the expected user or maintainer benefit, and link public evidence for any factual claim. Separate adopted behavior from exploratory ideas.

## Triage

Open issues across the fleet are classified in [`docs/FLEET_REMAINING_ISSUES_2026-07-04.md`](FLEET_REMAINING_ISSUES_2026-07-04.md) into buckets:

- **Bucket 1: Operator authority** — decision issues requiring explicit operator sign-off. Agents must not auto-complete these.
- **Bucket 2: Business/personal ops** — operator-owned work, not agent-actionable without explicit delegation.
- **Bucket 3+: Agent-actionable** — docs, schema, fixture, and code contributions open to contributors.

Check the triage doc before starting work to avoid picking up an operator-authority or business-ops issue.

## General rules for every path

- **Issue first** — open an issue describing the change before submitting a PR.
- **One concern per PR** — keep diffs small and focused (target < 300 lines changed).
- **Receipts** — link the issue, cite prior art, and preserve evidence in the PR body.
- **Maturity gates** — `seed` / `v0.1-packet` repos accept docs/schema/fixture contributions only. `active` / `canonical` repos have scoped contribution paths with review gates — read their CONTRIBUTING.md.
- **No canonical decisions from agents** — promotions, demotions, and decision issues require operator authority.
- **Security** — never report vulnerabilities in public issues. Use the private reporting path in `SECURITY.md`.
