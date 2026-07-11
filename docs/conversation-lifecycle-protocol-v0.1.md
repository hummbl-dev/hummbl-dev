# HUMMBL Conversation Lifecycle Protocol v0.1 — Cross-Platform Chat and Work-Session Closeout

**Status: CANDIDATE COMPANY PROTOCOL — CROSS-PLATFORM — NON-CANON UNTIL REVIEWED**

Issue: hummbl-dev/hummbl-dev#159

## Decision context

HUMMBL already has strong platform-specific session bookends in `claude-config` and `apex-nexus`, especially `/start-session`, `/end-session`, and `/session-metrics`. Those skills assume capabilities such as:

- a local repository root
- shell and Git access
- a coordination bus
- writable local memory
- agent identity and filesystem state

ChatGPT chats and connected work sessions may have a different and variable capability surface. HUMMBL therefore needs a provider-neutral protocol core with capability-aware adapters rather than a copy of the Claude procedure.

## Objective

Define a reusable Conversation Lifecycle Protocol (CLP) whose initial v0.1 profile closes ChatGPT chats and multi-tool work sessions safely, preserves durable value, produces a resumable handoff, and records what could and could not be verified.

> If this chat became unavailable now, could a human or another authorized agent recover the decisions, evidence, artifacts, constraints, open work, and next action without reconstructing the entire transcript?

## Repository responsibility map

### `protocol-as-code`
- lifecycle states
- capability declarations
- ordered closeout procedure
- step outcomes and stop conditions
- completion contract
- platform-adapter requirements
- valid, invalid, and interrupted-session fixtures

### `agent-handoffs`
- objective and achieved outcomes
- decisions and claim posture
- artifacts and confirmed locations
- open work and blockers
- authority and constraints
- evidence and provenance references
- next recommended action
- receiver acknowledgment and expiry

### `execution-receipts`
- invoked mode and protocol version
- declared/observed capabilities
- checks attempted and outcomes
- preservation writes confirmed
- artifacts created or updated

## Acceptance criteria

- [x] Decision context documented
- [x] Objective documented
- [x] Repository responsibility map documented (3 repos)
- [ ] Lifecycle states defined
- [ ] Capability declarations schema
- [ ] Ordered closeout procedure
- [ ] Platform-adapter requirements
- [ ] Valid/invalid/interrupted fixtures
- [ ] Independent review

## Non-goals

- Copying the Claude procedure
- Assuming capabilities that ChatGPT lacks
- Canonizing before review

## Cross-repo dependencies

- `hummbl-dev/protocol-as-code#7` — lifecycle protocol profile
- `hummbl-dev/agent-handoffs#9` — session handoff profile
- `hummbl-dev/execution-receipts#10` — closeout receipt profile

## Fact posture

This is a candidate company protocol derived from issue #159. Non-canon until reviewed. All states, procedures, and fixtures are candidate until implemented.

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#159
- **Repository responsibilities**: 3
- **Cross-repo deps**: 3
- **Review status**: PENDING
