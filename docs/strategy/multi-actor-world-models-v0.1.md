# Multi-Actor World Models v0.1

**Status: CANDIDATE — OPERATOR APPROVED 2026-07-10 — NON-CANON — EXTENDS #149**

Issue: hummbl-dev/hummbl-dev#151
Parent: hummbl-dev/hummbl-dev#149 (User-Driven World Model Generation)

## Decision

Extend the user-driven world-model program (#149) across three explicitly distinct actor regimes:

1. **User-first** — a human creates and owns model state with system assistance.
2. **User + agents** — a human principal delegates bounded epistemic and operational roles to one or more agents.
3. **Agent-only bounded operation** — agents operate without continuous human interaction but remain chartered by a human or organization, under explicit constitutions, resource limits, receipts, revalidation, and kill authority.

Self-authorizing agents with no human or organizational principal remain a research/simulation category and are not production-authorized.

## Core invariants

```text
agent inference != user belief
epistemic permission != durable-write permission
durable-write permission != action authority
agent count != independent evidence count
no human currently interacting != no human or organizational authority
```

The ability to observe, infer, propose, challenge, ratify, write durable state, execute, delegate, publish, revoke, and retire must remain separately permissioned.

## Actor regimes

### A. User-first

- Root principal: user
- Durable-model owner: user
- Contributors: user plus system-assisted compiler/critic/research roles
- Action authority: user or explicit bounded delegation

### B. User + agents

- Root principal: user
- Durable-model owner: user or a separately declared shared entity
- Contributors: user and delegated agents
- Required separation among:
  - user-approved model
  - agent-local working beliefs
  - shared operational state
  - external-world state
  - agent social/capability models
  - authority and consent state

### C. Organization + agent workforce

- Root principal: organization through declared human authority
- Durable-model owner: organization, project, or declared governed entity
- Contributors: authorized humans and agents
- Action authority: role-, policy-, quorum-, and delegation-bounded

### D. Bounded agent-only operation

- No continuous human interaction required
- Human or organization still defines mission, constitution, resources, legal authority, escalation, revalidation, and termination
- Suitable only for bounded contexts such as research, simulation, software operations, infrastructure monitoring, games, logistics, and internal workflows

### E. Agent-society research sandbox

- Simulated resources and environments only by default
- Explicit constitution and external operator
- Study coalition behavior, consensus failure, collusion, deception, ontology drift, emergent norms, and reward-path corruption
- No ambient production or open-world authority

## Non-collapsing world-model composition

```text
W_system = W_user_approved
         + W_shared_operational
         + sum(W_agent_local_i)
         + W_authority
         + W_policy
```

Every claim/model/state contribution must preserve:

- actor
- principal
- owner
- role
- delegation
- source/evidence lineage
- model/provider/tool independence lineage
- confidence or uncertainty posture
- scope and expiry
- visibility
- approval state
- durable-write posture
- action-authority posture

## Actor-neutral runtime primitives

```text
Principal
Actor
HumanActor
AgentActor
AgentVersion
Role
Delegation
Capability
EpistemicPermission
DurableWritePermission
ActionPermission
LocalBeliefState
SharedWorldState
AuthorityState
PolicyState
ModelFragment
Observation
Inference
Challenge
Dissent
Ratification
Rejection
MergeProposal
Fork
Prediction
Counterfactual
ActionProposal
Authorization
Execution
Outcome
CalibrationRecord
Receipt
Revocation
Quarantine
Retirement
```

The product interface remains user-first. The internal substrate must not hard-code that every observer, contributor, challenger, approver, or executor is human.

## Agent epistemic roles

Candidate roles:

- observer
- compiler
- translator
- critic
- researcher
- simulator
- planner
- executor
- historian
- consent steward
- arbiter

No single role should automatically combine observation, interpretation, approval, execution, and receipt authority.

## Multi-agent events

```text
AGENT_REGISTERED
AGENT_VERSION_CHANGED
AGENT_ROLE_ASSIGNED
DELEGATION_GRANTED
DELEGATION_REVOKED
AGENT_OBSERVATION
AGENT_INFERENCE
AGENT_MODEL_PROPOSAL
AGENT_CHALLENGE
AGENT_DISSENT
USER_RATIFICATION
USER_REJECTION
ORG_RATIFICATION
MODEL_MERGE_PROPOSAL
MODEL_FORK
HANDOFF_EVENT
TOOL_RESULT_PROPOSED
TOOL_RESULT_ADMITTED
ACTION_PROPOSED
ACTION_AUTHORIZED
ACTION_DENIED
AGENT_CALIBRATION_UPDATED
COALITION_FORMED
COALITION_DISSOLVED
AGENT_QUARANTINED
AGENT_ROLE_EXPIRED
```

Event attribution distinguishes:

```text
authored_by
represented_principal
approved_by
challenged_by
executed_by
receipted_by
```

## Local belief versus shared state

Do not force one global belief graph.

```text
W_collective = shared evidence/operational ledger
             + agent-local belief states
             + governance/authority state
```

Agents may retain conflicting conclusions while sharing the underlying observations, tests, unresolved questions, and decision state.

Consensus must not be treated as truth. Track independence across:

- foundation model/provider
- prompt and policy lineage
- source lineage
- retrieval path
- tool chain
- execution environment
- evaluator/judge lineage

Correlated agents repeating one source are one evidence lineage, not multiple independent confirmations.

## Agent calibration

Trust must be domain- and task-specific:

```text
agent_id
agent_version
domain
task_type
prediction_count
evaluated_count
calibration
error_profile
abstention_quality
correction_behavior
receipt_completeness
authority_violations
staleness
```

Do not create a universal scalar agent-reputation score.

## Agent-only constitution requirements

A bounded agent collective must have machine-readable rules for:

- mission and scope
- root principal and authority chain
- epistemic permissions
- durable-state admission
- action permissions
- resource and cost limits
- delegation and subagent limits
- evidence and consensus rules
- dissent and conflict resolution
- identity and attestation
- lifecycle, quarantine, and retirement
- external reporting and receipts
- periodic revalidation
- kill and recovery authority

## Priority failure modes

- authority laundering
- consensus laundering
- Sybil/correlated-agent inflation
- model/state poisoning
- self-confirming intervention loops
- coalition capture
- goal and ontology drift
- memory/version divergence
- delegation explosion
- reward-path corruption
- unsupported anthropomorphic claims

## Approved development progression

1. One user + one agent
2. One user + several specialized agents
3. One user + persistent calibrated agent team
4. Organization + agent workforce
5. Bounded agent-only operation
6. Agent-society research sandbox

Each phase must preserve prior governance and receipt gates and must not imply authorization for the next phase.

## Repository disposition

### Extend existing work

- `hummbl-models` — actor/principal/delegation envelope for candidate fragments
- `hummbl-tuples` — multi-actor epistemic and operational events
- `hummbl-admission-controlled-state` — agent and coalition admission/lifecycle
- `hummbl-eval` — multi-agent epistemic, calibration, collusion, and drift evals
- `agent-as-code` — versioned agent identity, roles, capabilities, permissions, and local-belief contracts
- `agent-handoffs` — belief-aware and authority-preserving handoffs
- `agent-control-plane-patterns` — local/shared state, dissent, merge/fork, and coalition control patterns
- `agent-runtime-governance` — bounded agent-only constitution and anti-authority-laundering controls
- `hummbl-repo-factory#5` — keep one private-first runtime; add actor-neutral internal boundaries

### Greenfield deferral

Do not create an agent epistemic network or agent-society repository yet. Extract only after the private runtime supports a second independent implementation/use case and the interface is grounded by working evidence.

## Acceptance criteria

- [x] Actor regimes and root-principal rules documented
- [x] Actor-neutral runtime primitives listed
- [x] Agent inference, user belief, durable state, and action authority separation documented
- [x] Agent-local beliefs and shared state separately representable
- [x] Dissent and contradiction remain first-class
- [x] Independence lineage prevents correlated-agent vote inflation
- [x] Agent calibration is domain/task specific
- [x] Agent-only operation requires human/organizational constitution and kill authority
- [x] Agent-society work remains sandboxed
- [x] No new repository created for this expansion during v0.1
- [ ] Child issues and receipts link back to this issue and #149

## Related

- `hummbl-dev/hummbl-dev#149` — user-driven world-model architecture
- `hummbl-dev/hummbl-dev#124` — Ownward voice runtime abstraction
- `hummbl-dev/hummbl-models#9` — candidate model fragment schema
- `hummbl-dev/hummbl-tuples#84` — world-model events
- `hummbl-dev/hummbl-eval#2` — user-model evaluation
- `hummbl-dev/hummbl-admission-controlled-state#23` — user-model admission
- `hummbl-dev/hummbl-repo-factory#5` — private-first runtime admission

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#151
- **Operator approval**: 2026-07-10
- **Actor regimes**: 5 (A-E)
- **Runtime primitives**: 35
- **Multi-agent events**: 27
- **Failure modes**: 11
- **Development progression**: 6 phases
- **Greenfield repos**: 0 (deferred)
- **Review status**: PENDING
