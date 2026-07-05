# HUMMBL Glossary

Definitions for terms already used across HUMMBL public repos. This glossary stabilizes comprehension — it does not introduce new terminology.

## Governance concepts

**Governed agentic work** — AI agent execution where every action has identity, authority, receipts, rollback, and audit. Operators stay accountable; automation assists, it does not replace review.

**Operator authority** — Decisions that require a human operator. Agents cannot make these decisions autonomously. Examples: promoting a repo to canonical, approving Phase 1 deployments, closing operator-authority issues.

**Execution receipt** — A structured record proving that a specific command or action ran, with inputs, outputs, environment, exit status, and verification chain. Stored as append-only evidence.

**Claim-evidence ledger** — An append-only ledger linking claims to their supporting evidence with provenance chains. Each entry records what was claimed, what evidence supports it, and where the evidence came from.

**Kill switch** — A governance primitive with 4 modes: DISENGAGED → HALT_NONCRITICAL → HALT_ALL → EMERGENCY. Stops agent execution at escalating severity levels.

**Circuit breaker** — A governance primitive with 3 states: CLOSED → HALF_OPEN → OPEN. Wraps external service calls and trips on repeated failures to prevent cascading damage.

**Delegation token** — An HMAC-SHA256 signed capability token that bounds what an agent can do: scope, expiry, and chain-depth. Agents present tokens to prove authority for specific actions.

**Governance bus** — An append-only audit log (JSONL) recording all delegation events. Provides the durable evidence trail for agent actions.

## Repo maturity

**v0.1-packet** — A repo that has a v0.1 boundary document, prior art survey, JSON schema, valid/invalid fixtures, and a receipt. The minimal coherent unit for a pattern/reference repo. Open for docs/schema/fixture contributions. Non-canon.

**Canonical** — A repo that has been audited, approved, and explicitly adopted as HUMMBL authority. Changes require operator authority and receipts. Current canonical repos: `hummbl-governance`, `base120`.

**Canonical-candidate** — A repo proposed for canonical status. Under audit. Not yet canon.

**Seed** — A repo with concept framing, README, license, and initial issues, but no v0.1 packet yet. Expect change. Not ready for outside contributors.

**Hold** — A repo frozen pending operator decision. Do not extend.

## Repo types

**Implementation-bearing repo** — Ships runnable code. Has tests, builds, releases. Examples: `hummbl-governance`, `base120`, `arbiter`, `mcp-server`.

**Pattern/reference repo** — Contains docs, schemas, fixtures, and prior art. No runtime code. Examples: all `*-as-code` repos, all agent pattern repos.

**Distribution repo** — A generated or policy-validated install surface downstream from `packages`. Examples: `homebrew-tap`, `scoop-bucket`, `winget-manifests`, `nix`.

**Distribution spine** — The canonical package identity, artifact receipt, and release pipeline defined in `hummbl-dev/packages`. Downstream repos (Homebrew, Scoop, winget, Nix) generate their manifests from this spine.

## Agent routing

**Agent-safe** — An issue or task that is safe for autonomous agent execution. No operator authority required, no canon impact, no new terminology.

**Agent-hold** — An issue or task blocked for agent execution. Requires operator decision or human review before an agent can proceed.

**External-collab-ready** — A repo or issue ready for outside contributor participation. Has clear scope, contribution guidance, and bounded acceptance criteria.

**Decision-required** — An issue requiring human decision before proceeding. Agents must escalate, not auto-complete.

**Evidence-needed** — An issue or PR that needs evidence or receipts before closure.

## Posture

**Non-canon** — Content marked as exploratory, candidate, or draft. Not adopted as HUMMBL authority. May be useful without being authoritative.

**Receipt** — A structured record documenting what was done, why, and with what evidence. Required for governance-bearing changes. Stored in `receipts/` or `_receipts/`.

**Provenance** — The origin trail for a piece of content, data, or evidence. Records where something came from and how it was verified.
