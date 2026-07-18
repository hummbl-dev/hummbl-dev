# User-Driven World Model Generation v0.1

**Status: CANDIDATE — OPERATOR APPROVED 2026-07-10 — NON-CANON — BROWNFIELD EXTENSION**

Issue: hummbl-dev/hummbl-dev#149

## Decision

Proceed with a user-driven world-model program that builds on the existing HUMMBL/BaseN/governance/evidence stack rather than recreating it.

```text
existing HUMMBL substrate
+ one private-first user-model runtime
+ later federation protocol after demonstrated interoperability need
```

## Core distinction

- **Mental models** are reasoning operators, heuristics, or interpretive lenses.
- **World models** are stateful, temporal, predictive representations of actors, environments, relationships, constraints, actions, and possible future states.
- Base120/BaseN are not themselves the world model. They operate on partial world models through inspectable, governed reasoning paths.

## Product thesis

A user should not need to understand ontology, graphs, schemas, or the phrase "world model."

The system should accept ordinary expression — voice, text, story, example, image, or measurement — and help the user create a bounded, inspectable, testable model fragment while preserving:

- the user's original language;
- the system's interpretation as a separate artifact;
- uncertainty and alternative interpretations;
- user approval before durable admission;
- ownership, privacy, consent, correction, deletion, and export;
- evidence and provenance;
- predictions, actions, outcomes, and revisions.

## Existing substrate to reuse

### Mental-model and reasoning layer

- `hummbl-dev/base120` — canonical Base120 mental-model substrate
- `hummbl-dev/hummbl-models` — registries, shared model schema, relationships, transformation maps, query/validation tooling
- `hummbl-dev/hummbl-tuples` — BaseN governed reasoning-path semantics, control modes, path events, and evidence layer
- `hummbl-dev/mcp-server` — public read-only access, lookup, search, problem-pattern search, and model recommendation

### Knowledge, evidence, and provenance layer

- `hummbl-dev/knowledge-as-code` — owner/authority, claims, source, interpretation, status, and accepted-state packet semantics
- `hummbl-dev/claim-evidence-ledger` — claim/evidence/confidence/adoption-state patterns
- `hummbl-dev/research-source-packets` — bounded source packets with provenance and caveats
- Evidence Graph v0.1 in `hummbl-dev/hummbl-dev` — fact posture, evidence grade, graph relationships, receipts, and supersession patterns

### State, governance, execution, and assurance layer

- `hummbl-dev/hummbl-admission-controlled-state` — candidate-to-durable state admission
- `hummbl-dev/hummbl-governance` — runtime authority, delegation, kill switches, circuit breakers, and policy primitives
- `hummbl-dev/hummbl-governance-kernel` — deterministic-first action gateway and receipt-bearing governance
- `hummbl-dev/execution-receipts` — action and workflow execution receipts
- `hummbl-dev/hummbl-assurance` — deterministic conformance, receipt verification, compatibility, and temporal revalidation
- `hummbl-dev/hummbl-eval` — evaluation harness to extend for fidelity, accessibility, fairness, safety, and calibration
- `hummbl-dev/hummbl-kernel-factory` and `hummbl-dev/hummbl-repo-factory` — implementation and repository bootstrapping

## Approved brownfield extensions

### 1. hummbl-models — candidate model fragment schema

Add a distinct, explicitly noncanonical candidate schema:

```text
schemas/candidate-model-fragment.v0.1.json
```

Minimum fields:

- fragment identifier and version
- original observation or expression reference
- context, population, and time boundary
- variables and proposed relationships
- mechanism posture
- prediction and time horizon
- confidence and uncertainty posture
- evidence references
- owner and consent state
- admission state
- supersession references

### 2. hummbl-tuples — world-model event semantics

Extend with events for model fragment lifecycle:

```text
MODEL_FRAGMENT_PROPOSED
MODEL_FRAGMENT_ADMITTED
MODEL_FRAGMENT_CHALLENGED
MODEL_FRAGMENT_REVISED
MODEL_FRAGMENT_SUPERSEDED
MODEL_FRAGMENT_RETIRED
MODEL_PREDICTION_MADE
MODEL_PREDICTION_RESOLVED
MODEL_ACTION_PROPOSED
MODEL_ACTION_EXECUTED
MODEL_OUTCOME_RECORDED
```

### 3. hummbl-admission-controlled-state — user-model admission

Extend admission to support:

- user-owned candidate fragments
- user approval before durable admission
- challenge and revision without data loss
- supersession chains
- retirement and export

### 4. hummbl-eval — model fragment evaluation

Extend evaluation to cover:

- fidelity (does the fragment match the user's intent?)
- predictive accuracy (do predictions resolve correctly?)
- calibration (are confidence and uncertainty honest?)
- accessibility (can the user understand and correct it?)
- privacy (does it preserve user ownership and consent?)
- safety (does it avoid harmful predictions or actions?)

### 5. hummbl-repo-factory — private-first runtime

Keep one private-first runtime. Add actor-neutral internal boundaries (extended in #151).

## Federation deferral

Do not build a federation protocol yet. Federation is deferred until:

- the private-first runtime has a working user-model admission cycle
- at least one independent implementation demonstrates interoperability need
- the interface is grounded by working evidence, not speculation

## User-model admission cycle

```text
1. User expresses (voice, text, image, measurement)
2. System proposes interpretation as candidate fragment
3. User reviews, corrects, or rejects
4. Approved fragment enters admission queue
5. Evidence and provenance attached
6. Fragment admitted to durable state (or challenged)
7. Predictions made from admitted fragments
8. Actions proposed and authorized
9. Outcomes recorded
10. Fragments revised or superseded based on outcomes
```

## Privacy and ownership

- User owns their model fragments
- System interpretation is a separate artifact, not the user's belief
- User can export, correct, or delete at any time
- No fragment is admitted without user approval
- No fragment is shared without explicit consent
- Federation requires explicit per-fragment sharing consent

## Non-goals

- Does not create a new repository
- Does not define federation protocol (deferred)
- Does not make Base120/BaseN into a world model
- Does not assume agent-only operation (see #151)
- Does not claim canonicality

## Acceptance criteria

- [x] Core distinction between mental models and world models documented
- [x] Product thesis documented (user does not need to understand "world model")
- [x] Existing substrate reuse map documented
- [x] Brownfield extensions identified for hummbl-models, hummbl-tuples, hummbl-admission-controlled-state, hummbl-eval, hummbl-repo-factory
- [x] Federation deferral rationale documented
- [x] User-model admission cycle documented
- [x] Privacy and ownership requirements documented
- [ ] Candidate model fragment schema implemented in hummbl-models
- [ ] World-model event semantics implemented in hummbl-tuples
- [ ] User-model admission implemented in hummbl-admission-controlled-state
- [ ] Model fragment evaluation implemented in hummbl-eval

## Related

- `hummbl-dev/hummbl-dev#151` — Multi-Actor World Models (extends this program)
- `hummbl-dev/hummbl-dev#124` — Ownward voice runtime abstraction
- `hummbl-dev/hummbl-models#9` — candidate model fragment schema
- `hummbl-dev/hummbl-tuples#84` — world-model events
- `hummbl-dev/hummbl-eval#2` — user-model evaluation
- `hummbl-dev/hummbl-admission-controlled-state#23` — user-model admission
- `hummbl-dev/hummbl-repo-factory#5` — private-first runtime admission

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#149
- **Operator approval**: 2026-07-10
- **Brownfield extensions**: 5 repos identified
- **Federation**: deferred
- **Review status**: PENDING
