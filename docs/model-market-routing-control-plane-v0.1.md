# HUMMBL Model Market & Routing Control Plane v0.1 — Cross-Repo Implementation Plan

**Status: APPROVED PLAN — NO GREENFIELD REPO — IMPLEMENT THROUGH EXISTING REPOSITORIES**

Issue: hummbl-dev/hummbl-dev#156

## Decision

HUMMBL, LLC will not create a new repository for model-market intelligence or cheapest-correct-model routing at this stage.

Canonical policy and schema home: `hummbl-dev/model-routing-as-code`

## Architecture

```text
Work request
  -> task/runtime route
  -> model-routing-as-code policy
  -> provider/model adapter
  -> bounded execution
  -> execution receipt
  -> evidence graph / observability / reevaluation
```

## Doctrine

> Cheapest correct model wins only after runtime, correctness, safety, privacy, authority, latency, reliability, reproducibility, and governance gates pass.

## Objectives (6)

1. Establish one authoritative model-routing policy surface
2. Separate runtime selection from model/provider selection
3. Measure total cost per accepted governed outcome
4. Convert real HUMMBL workflows into reusable benchmark evidence
5. Preserve provider portability
6. Allow Ownward and future products to consume without defining

## Repository responsibility map

### `model-routing-as-code` — canonical policy and schema authority
- provider/model capability registry contract
- task/workload class registry
- route manifests and decision schema
- hard gates and soft-ranking rules
- cost ceilings and fallback chains
- promotion lifecycle and expiry
- benchmark-import contract
- deterministic validator and fixtures

### `autoresearch-pipeline` — benchmark harness
- reproducible runs, frozen task fixtures
- candidate configuration
- latency, token, tool, retry, outcome collection
- comparison output for routing policy import

### `execution-receipts` — execution and economic evidence
- selected runtime/provider/model/version
- route-decision reference
- input, output, reasoning, cache usage
- external-tool costs, retries, fallbacks
- reviewer cost, human-review effort
- accepted/rejected/partial outcome
- total cost per accepted outcome

### Evidence Graph / claim-evidence infrastructure
- provider price claim → source and verification date
- benchmark claim → fixture, harness, run, receipt
- model promotion → supporting evidence
- route decision → execution outcome

### `observability-as-code`
- spend by provider/model/task class
- cost per accepted task
- escalation and retry rate
- acceptance and rollback rate
- latency distributions
- provider concentration
- stale promotion evidence
- route drift and budget breaches

### `hummbl-dev/hummbl-dev`
- cross-repo coordination
- company-level decisions
- milestone tracking
- product-consumer mapping
- final readiness and transition receipts

## Scope decision (#7)

**Layered shared envelope** with independent runtime and model decisions. Runtime route resolves first; model route resolves within the approved runtime envelope.

**Invariant:** A cheaper model cannot override an unsafe runtime, prohibited data boundary, missing authority, or required human-review gate.

## Work plan (8 phases)

### Phase 0 — Boundary and decision closure
- Resolve #7 with layered architecture
- Record definitions (task, runtime, backend, provider, model, scaffold, reviewer, human route)
- **Gate:** reviewed scope decision before schema changes

### Phase 1 — Minimal policy packet
- 9 schemas (task-runtime envelope through price snapshot)
- Deterministic validator
- 9 invalid fixtures
- **Gate:** schemas validate, invalid fixtures fail correctly

### Phase 2 — HUMMBL task-class registry (15 classes)
- REPO_INVENTORY through CALENDAR_CONFLICT_RESOLUTION
- Per class: source profile, consequence level, privacy, authority, correctness threshold, citation requirements, latency, cost ceiling, scaffolds, review, expiry
- **Gate:** no class promoted without fixture and acceptance criteria

### Phase 3 — Benchmark and cost instrumentation
- 8 initial benchmarks (governed issue through multi-agent handoff)
- 12 measurement dimensions
- **Gate:** benchmark results imported, not manually copied

### Phase 4 — Initial candidate lanes (8)
- Deterministic through human-review
- 12 scoped dispositions (REJECTED through RETIRED)
- **Gate:** no provider becomes company-wide default

### Phase 5 — Receipts and observability integration
- Route-decision receipt before execution
- Execution/economic receipt after execution
- Evidence linking
- Dashboard and alert contracts
- **Gate:** one end-to-end trace from request through cost

### Phase 6 — Adapter and runtime integration
- Normalized provider-adapter interfaces
- Smallest viable adapters
- Provider-native features behind capability declarations
- **Gate:** 2+ providers + 1 local/free route execute same task contract

### Phase 7 — Product consumption
- Ownward consumes task-class, route decisions, adapters, telemetry
- Products retain domain policy, safety, memory, user state
- **Gate:** product integration is adapter-based and removable

## Greenfield-repo trigger (4 conditions)

1. Deployable routing service with independent API, auth, SLA
2. Commercial product boundary with independent ownership
3. Runtime implementation overwhelms spec repository boundary
4. Distinct task/runtime router becomes governed production system

## Success criteria for v0.1 (11)

- [ ] #7 resolved with reviewed boundary
- [ ] 7 schemas exist (provider/model, task-class, route-decision, benchmark-import, promotion, price-snapshot)
- [ ] Deterministic validator and adversarial fixtures exist
- [ ] 5+ real HUMMBL task classes have reproducible benchmarks
- [ ] 2+ hosted providers + 1 local/free lane compared
- [ ] Cost per accepted governed outcome calculated
- [ ] Route decisions record why cheaper candidates rejected
- [ ] One end-to-end trace links route, execution, review, acceptance, evidence, economics
- [ ] No production route changes without operator approval and transition receipt
- [ ] Ownward represented as future consumer, not platform owner
- [ ] No new repo created absent documented trigger decision

## Acceptance criteria

- [x] Decision documented (no greenfield repo)
- [x] Architecture documented
- [x] 6 objectives documented
- [x] Repository responsibility map documented (6 repos)
- [x] Scope decision documented (layered envelope)
- [x] 8 phases documented with gates
- [x] 15 task classes listed
- [x] 8 benchmarks listed
- [x] 12 measurement dimensions listed
- [x] 8 candidate lanes listed
- [x] 12 scoped dispositions listed
- [x] 4 greenfield triggers documented
- [x] 11 success criteria documented
- [ ] All success criteria met (execution)

## Non-goals

- Universal best-model ranking
- Production default change
- Provider dependency
- Product-specific private state in public registries
- New HUMMBL/BaseN terminology canonization
- Competing policy authority

## Cross-repo dependencies

- `hummbl-dev/model-routing-as-code#7` — scope decision
- `hummbl-dev/model-routing-as-code#8` — policy implementation
- `hummbl-dev/model-routing-as-code#9` — execution packet
- `hummbl-dev/autoresearch-pipeline#29` — benchmark harness
- `hummbl-dev/autoresearch-pipeline#31` — routing benchmark
- `hummbl-dev/execution-receipts#9` — economic receipt
- `hummbl-dev/observability-as-code#7` — observability
- `hummbl-dev/hummbl-dev#158` — vertical slice

## Fact posture

This is an approved plan derived from issue #156. No greenfield repo. Provider prices are volatile external facts requiring source URLs and verification timestamps. Benchmark results are local execution evidence. Promotions are bounded HUMMBL operating decisions.

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#156
- **Objectives**: 6
- **Repository responsibilities**: 6
- **Phases**: 8 (with gates)
- **Task classes**: 15
- **Benchmarks**: 8
- **Measurement dimensions**: 12
- **Candidate lanes**: 8
- **Scoped dispositions**: 12
- **Greenfield triggers**: 4
- **Success criteria**: 11
- **Cross-repo deps**: 8
- **Review status**: PENDING
