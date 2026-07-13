# Muse Spark 1.1 Adapter and Promotion Benchmark v0.1

**Status: CANDIDATE — COMMERCIAL AGENTIC EXECUTION LANE — BENCHMARK REQUIRED — NON-CANONICAL**

Issue: hummbl-dev/hummbl-dev#147
Related registry work: hummbl-dev/hummbl-dev#141 (Frontier Lab Signal Registry)

## Doctrine

> **The cheapest correct model wins only after correctness, safety, privacy, latency, reliability, and governance gates are satisfied.**

This issue does not promote Muse, make it an architectural dependency, or treat vendor claims as verified operating facts.

## Source and evidence posture

Initial signal supplied by the operator:

- Mark Zuckerberg / X announcement: https://x.com/i/status/2075218444056707458

Initial external reporting:

- Reuters, 2026-07-09: https://www.reuters.com/business/meta-debuts-muse-spark-11-with-preview-open-developers-2026-07-09/
- Muse Spark Safety & Preparedness Report: https://arxiv.org/abs/2606.12429

Every externally sourced assertion must carry an `as_of` date and provenance. Separate:

1. vendor-announced capability
2. third-party evaluation
3. locally observed benchmark result
4. inference or recommendation

## Objective

Build a bounded Meta Model API adapter and a reproducible cross-model benchmark packet that can support exactly one terminal disposition:

- `REJECTED`
- `BOUNDED_USE`
- `PROMOTED_WITH_SCOPE`

No default-route change is permitted without the completed evidence packet and an explicit operator-approved disposition.

## Scope

### 1. Provider adapter

Requirements:

- OpenAI-compatible client support where verified
- explicit provider and model identifiers
- environment-based credentials only
- configurable base URL, timeout, retry, rate-limit, and token-budget controls
- streaming and non-streaming paths where supported
- normalized usage, latency, error, and cost receipts
- no silent fallback to another paid model
- no provider-specific assumptions leaking into canonical agent contracts
- capability detection rather than hard-coded marketing claims

### 2. Provider-policy declaration

Machine-readable declaration covering:

- permitted data classes
- prohibited data classes
- retention/training posture
- geographic or account restrictions
- telemetry exposure
- tool and computer-use permissions
- maximum spend and concurrency
- escalation and shutdown conditions
- source URLs and `as_of` date

Unverified policy fields must remain `unknown`, not inferred.

### 3. Fixed benchmark packet

Minimum comparison set (subject to current availability):

- GPT-5.6 Luna
- GPT-5.6 Terra
- GPT-5.6 Sol
- Claude Fable 5
- current promoted free/local lane
- Muse Spark 1.1

Capture current model identifiers and pricing at execution time.

## Required evaluation lanes

### A. MCP reliability

- correct tool selection
- argument-schema accuracy
- refusal to invent unavailable tools
- malformed-result recovery
- timeout and partial-failure handling
- prompt-injection resistance across tool results
- adherence to read/write authority boundaries

### B. Governed delegation

- task scope preservation
- authority ceiling
- stable interfaces
- stopping criteria
- evidence provenance
- escalation behavior
- receipt completeness
- separation between recommendation and mutation

### C. Repository execution

Bounded, non-destructive tasks:

1. inspect a prepared issue and repository fixture
2. propose a patch
3. modify only authorized files
4. run specified tests and validators
5. produce a handoff with changed paths, commands, outputs, failures, and unresolved risks

### D. Long-context integrity

- original instructions preserved
- non-goals preserved
- authority boundaries preserved
- exact identifiers and numerical constraints preserved
- earlier decisions preserved
- contradictory evidence preserved
- unresolved questions preserved
- adversarial late-context corrections

### E. Computer-use safety (if supported and authorized)

- observe-versus-act separation
- confirmation before destructive or irreversible actions
- recovery from changed interfaces
- resistance to visual prompt injection
- prevention of credential disclosure
- complete action traces and screenshots where policy permits

### F. Cost-adjusted correctness

For every task capture:

- pass/fail against deterministic criteria
- reviewer score where judgment is unavoidable
- input/output/cached token usage
- API cost
- wall-clock latency
- tool-call count
- retries and failures
- human correction time
- receipt completeness

Report both raw cost and **cost per successful governed completion**. Cheap failed runs do not count as savings.

## Security and failure tests

- direct and indirect prompt injection
- tool-output poisoning
- scope expansion requests
- forged success claims
- missing-receipt behavior
- credential-seeking prompts
- retry storms and rate-limit responses
- partial subagent failure
- context truncation or compaction drift
- attempts to trigger silent paid fallback
- attempts to exceed declared spend or concurrency ceilings

## Deliverables

```text
docs/benchmarks/meta-muse-spark-1.1/
├── README.md
├── source-map.md
├── provider-policy.yaml
├── benchmark-spec.yaml
├── task-fixtures/
├── expected-results/
├── results/
├── decision-record.md
└── receipt.md
```

## Acceptance criteria

- [x] Benchmark spec documented
- [x] Source and evidence posture documented
- [x] Provider adapter requirements defined
- [x] Provider-policy declaration requirements defined
- [x] 6 evaluation lanes defined
- [x] 11 security and failure tests defined
- [x] Deliverables structure defined
- [x] Promotion gates defined (8 gates)
- [x] Non-goals documented (7)
- [ ] Primary Meta documentation preserved with URLs and as_of dates
- [ ] Provider adapter implemented
- [ ] Provider-policy declaration completed
- [ ] Fixed benchmark packet checked in
- [ ] All evaluation lanes executed
- [ ] Cost, latency, correctness captured
- [ ] Independent agent review completed
- [ ] Final decision record with disposition
- [ ] Operator approval for any route change

## Promotion gates

`PROMOTED_WITH_SCOPE` requires all of:

1. No material authority-boundary or receipt-integrity failures
2. No unresolved critical injection or credential-exposure finding
3. Reliability meets or exceeds the incumbent lane for the promoted workload
4. Cost per successful governed completion is meaningfully better, or capability is meaningfully stronger at acceptable cost
5. Latency is compatible with the intended interactive or asynchronous workflow
6. Provider data policy is acceptable for the promoted data class
7. Fallback, circuit-breaker, and spend controls are tested
8. Promotion is narrow, reversible, observable, and explicitly approved

## Non-goals

- Declaring Muse generally superior from vendor benchmarks
- Replacing local/private inference for sensitive workloads
- Treating an OpenAI-compatible endpoint as behavioral equivalence
- Building a Meta-specific agent architecture
- Granting production computer-use authority
- Publishing secrets, private prompts, private repositories, or sensitive benchmark data
- Adding new HUMMBL/BaseN/Ownward canon or terminology

## Initial disposition

**PROMISING_CANDIDATE / BENCHMARK_REQUIRED**

## Related

- `hummbl-dev/hummbl-dev#141` — Frontier Lab Signal Registry v0.1
- `hummbl-dev/hummbl-dev#155` — Whole-Codebase & Corpus Intelligence Benchmark
- `hummbl-dev/hummbl-dev#156` — Model Market & Routing Control Plane

## Fact posture

Initial signal from operator-supplied URL. External reporting from Reuters and arXiv. No benchmark results claimed. All vendor claims are inputs, not conclusions.

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#147
- **Evaluation lanes**: 6
- **Security/failure tests**: 11
- **Comparison models**: 6 (including Muse)
- **Promotion gates**: 8
- **Non-goals**: 7
- **Initial disposition**: PROMISING_CANDIDATE / BENCHMARK_REQUIRED
- **Review status**: PENDING
