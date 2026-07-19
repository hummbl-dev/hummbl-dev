# Durable Intelligence Doctrine v0.1 — Operational Adoption Guidelines

**Status: CANDIDATE — NON-CANONICAL**

Issue: hummbl-dev/hummbl-dev#162

## Purpose

Operationalize the Durable Intelligence Doctrine v0.1 so that every meaningful agent session leaves behind a compact, durable state transition. This document defines the adoption path, approved durable sinks, re-entry verification requirements, and the agent-session receipt schema.

## Agent-session receipt schema

A versioned JSON schema is defined at `docs/durable-intelligence-doctrine/v0.1/schema.json`.

### Required fields

| Field | Purpose |
|---|---|
| `schema_version` | Receipt schema version (currently `0.1`) |
| `session_id` | Unique session identifier |
| `source_agent` | Agent or human that produced the receipt |
| `environment` | Execution environment description |
| `tools_available` | Environment capability disclosure (mandatory) |
| `repository_or_system_scope` | Target repository or system |
| `starting_state` | State at session start |
| `actions_attempted` | What the agent tried to do |
| `mutations_made` | Mutation truthfulness — what was actually created (mandatory) |
| `claims[]` | Claims with explicit posture and evidence |
| `decisions[]` | Decisions made during the session |
| `negative_knowledge[]` | What did not happen and what is not established |
| `open_questions[]` | Unresolved questions |
| `next_actions[]` | Next bounded actions with disposition |
| `authority_boundaries` | Scope and constraints on agent authority |
| `receipt_destination` | Where the receipt is durably stored |
| `completion_status` | Session completion state |

### Claim posture vocabulary

Reused from existing HUMMBL governance work:

- `observed` — directly witnessed by the agent
- `source-reported` — reported by a source but not independently verified
- `inferred` — derived from available evidence
- `provisional` — candidate, not yet confirmed or refuted
- `verified` — independently confirmed
- `refuted` — shown to be false
- `unresolved` — insufficient evidence to determine

### Handoff dispositions

Where a session ends on a candidate defect or unresolved claim:

- `CONFIRMED` — verified independently
- `REFUTED` — shown to be false
- `INCONCLUSIVE` — insufficient evidence
- `BLOCKED_MISSING_AUTHORITY` — cannot proceed without additional authorization
- `SUPERSEDED` — replaced by a newer finding or action

## Approved durable sinks

Receipts must be preserved in durable, discoverable sinks. Chat-only preservation is insufficient.

| Sink | Use case |
|---|---|
| `github_issue` | Issue comments for ongoing work |
| `github_pr_comment` | PR review handoffs |
| `receipt_directory` | Governed receipt directories in repos |
| `claim_evidence_ledger` | Claim-evidence ledgers for cross-session patterns |
| `task_registry` | Task registries for bounded work items |
| `handoff_index` | Canonical handoff indexes for cross-agent coordination |

## Re-entry verification

Incoming agents must verify live state before trusting stale handoffs. At minimum:

1. **Confirm current branch/HEAD** — `git branch --show-current` and `git log --oneline -1`
2. **Confirm active issue/PR state** — `gh issue view` or `gh pr view` for referenced artifacts
3. **Confirm relevant file contents** — read files referenced in the receipt before acting
4. **Confirm authoritative source versions** — check for superseding commits, merged PRs, or closed issues

If live state contradicts the receipt, the receipt is stale. Do not act on stale receipts without re-verification.

## Validation path

A standard-library Python validator is provided at `scripts/validate_durable_intelligence.py`.

```bash
# Validate a single receipt
python scripts/validate_durable_intelligence.py receipt.json

# Run self-test on all fixtures
python scripts/validate_durable_intelligence.py --self-test
```

The validator enforces:
- Schema compliance (required fields, enum values, type checks)
- Mutation truthfulness (every mutation record must have a `created` boolean)
- Durable sink requirement (receipt_destination must be a durable sink, not chat-only)
- Claim posture explicitness (every claim must have an explicit posture)

## Fixture

A valid fixture converting the seed example (`hummbl-dev/hummbl-production#747`) into the receipt format is at `docs/durable-intelligence-doctrine/v0.1/fixtures/valid-session-receipt/receipt.json`.

This fixture demonstrates:
- A tool-limited cloud review session with explicit capability disclosure
- Mutation truthfulness: all mutation records have `created: false`
- Negative knowledge: 5 items including "no code changed" and "defect not confirmed"
- Provisional claim posture with evidence
- Bounded next action with `INCONCLUSIVE` disposition
- Advisory-only authority boundaries

## Adoption checklist

- [x] Versioned agent-session receipt schema drafted
- [x] Claim-posture vocabulary reused from existing governance work
- [x] Mutation-truthfulness and environment-capability fields mandatory
- [x] One existing handoff converted into the proposed format as a fixture
- [x] Validation path defined (machine-checkable, stdlib-first)
- [x] Guidance identifies approved durable sinks and re-entry verification requirements
- [ ] Doctrine adopted as operational practice across all agent workflows
- [ ] Independent review
