# Comparative Agent Runtime Program v0.1 — OpenClaw × Hermes Pilot

**Status: CANDIDATE — RESEARCH PROGRAM — NON-CANON**

Issue: hummbl-dev/hummbl-dev#152

## Purpose

Establish a governed comparative-analysis program for agent runtimes, using OpenClaw × Hermes Agent as the pilot campaign.

This is not a generic feature comparison. The program must reconstruct development lineage, normalize functional phases, separate implementation evidence from project positioning, run bounded comparative benchmarks, and produce decision-bearing outputs for HUMMBL, BaseN, Ownward, Founder Mode, fleet architecture, runtime governance, and model/runtime routing.

## Strategic questions

1. What are the structural differences between agent runtimes that matter for HUMMBL's fleet?
2. Which runtime properties are measurable, and which are only claimable?
3. How do development lineage and project maturity affect runtime trust?
4. What runtime properties are invariant across workloads, and which are workload-dependent?
5. How do governance, safety, and control surfaces differ across runtimes?
6. What can HUMMBL adopt from each runtime without coupling to its ecosystem?
7. Where do OpenClaw and Hermes overlap, diverge, and complement each other?

## Program structure

### Phase 1: Lineage reconstruction

- Document the development history of each runtime
- Identify founders, contributors, funding, and organizational context
- Trace major architectural decisions and their rationale
- Classify project posture (research, commercial, open-source, hybrid)
- Identify canonical sources vs. marketing claims

### Phase 2: Functional normalization

- Define a common functional taxonomy for agent runtimes
- Map each runtime's features to the common taxonomy
- Identify features that are unique, overlapping, and absent
- Separate implementation evidence from project positioning
- Note where features are claimed but not demonstrated

### Phase 3: Comparative benchmark

- Define workload scenarios that exercise the runtime properties that matter to HUMMBL
- Run bounded comparative tests where possible
- Use HUMMBL's own benchmark harness (autoresearch-pipeline#31)
- Record results with fact posture and evidence grade
- No vendor winner is predeclared

### Phase 4: Decision-bearing output

- Produce a comparative analysis report
- Generate adoption recommendations (adopt, adapt, avoid)
- Identify governance and safety implications
- Feed results into fleet architecture and runtime routing decisions
- Produce evidence pack for governance review

## Common functional taxonomy (candidate)

```text
Agent identity and versioning
Role and capability declaration
Delegation and authority chain
Tool invocation and sandboxing
Memory and state management
Handoff and session continuity
Receipt and audit logging
Kill switch and circuit breaker
Cost governance
Multi-agent coordination
Observability and telemetry
Failure modes and recovery
Constitution and policy enforcement
Calibration and evaluation
```

## OpenClaw posture

- Open-source agent runtime
- Active on nodezero
- Gateway + ACP + signal-cli components
- Temurin JDK 21
- Planned second node on Anvil via NVIDIA NemoClaw + WSL2

## Hermes Agent posture

- To be documented during Phase 1
- Development lineage to be reconstructed
- Project positioning to be separated from implementation evidence

## Evidence requirements

- All claims must be sourced and posture-classified
- Implementation evidence (code, tests, docs) is primary
- Project positioning (marketing, announcements) is secondary
- Benchmark results must be reproducible or marked as single-run
- No claim about one runtime may be made without comparable evidence for the other

## Non-goals

- Does not declare a runtime winner
- Does not replace HUMMBL's own runtime governance
- Does not couple HUMMBL to either runtime's ecosystem
- Does not publish claims that cannot be sourced
- Does not assume feature parity where it has not been demonstrated

## Acceptance criteria

- [x] Program structure documented (4 phases)
- [x] Common functional taxonomy proposed (14 categories)
- [x] OpenClaw posture documented (from existing fleet context)
- [ ] Hermes Agent posture documented (Phase 1)
- [ ] Lineage reconstruction for both runtimes (Phase 1)
- [ ] Functional normalization mapping (Phase 2)
- [ ] Comparative benchmark results (Phase 3)
- [ ] Decision-bearing output report (Phase 4)
- [ ] Adoption recommendations (adopt, adapt, avoid)

## Related

- `hummbl-dev/agent-runtime-governance#10` — OpenClaw × Hermes runtime governance crosswalk (draft PR #18)
- `hummbl-dev/hummbl-dev#155` — Whole-Codebase & Corpus Intelligence Benchmark
- `hummbl-dev/hummbl-dev#156` — Model Market & Routing Control Plane
- `hummbl-dev/autoresearch-pipeline#31` — benchmark harness

## Fact posture

This document is a research program proposal. OpenClaw posture is sourced from existing fleet context. Hermes Agent posture is pending Phase 1 research. No comparative claims are made yet.

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#152
- **Pilot campaign**: OpenClaw × Hermes Agent
- **Program phases**: 4
- **Functional taxonomy**: 14 categories
- **Evidence requirement**: all claims sourced and posture-classified
- **Review status**: PENDING
