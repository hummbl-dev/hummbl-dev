# HUMMBL Whole-Codebase & Corpus Intelligence Benchmark v0.1

**Status: ADMITTED BENCHMARK PROGRAM — CANDIDATE ROUTING EVIDENCE — NO VENDOR WINNER PREDECLARED**

Issue: hummbl-dev/hummbl-dev#155
Master program index: hummbl-dev/hummbl-dev#153
Related portfolio scale work: hummbl-dev/hummbl-dev#154

## Purpose

Build a reproducible, HUMMBL-specific benchmark for evaluating frontier and open models on whole-repository understanding and massive-source intelligence tasks.

> Which model, tool scaffold, memory strategy, and routing configuration produces the most accurate, source-grounded, cost-effective understanding of real HUMMBL codebases and corpora?

Advertised context length and vendor benchmark claims are inputs, not conclusions.

## Initial model roster — verified official specifications as of 2026-07-10

| Model | Advertised input context | Max output | Official positioning |
|---|---:|---:|---|
| OpenAI GPT-5.6 Sol | 1.05M | 128K | Flagship for complex reasoning and coding |
| Anthropic Claude Fable 5 | 1M | 128K | Highest available capability; long-running agents |
| Anthropic Claude Opus 4.8 | 1M | 128K | Complex agentic coding and enterprise work |
| Anthropic Claude Sonnet 5 | 1M | 128K | Speed/intelligence balance |
| Google Gemini 3.1 Pro Preview | 1,048,576 | 65,536 | Software engineering, agentic workflows, precise tool use |
| Google Gemini 3.5 Flash | 1,048,576 | 65,536 | Sustained agentic/coding work at scale |
| xAI Grok 4.5 | 500K | provider-listed | Flagship for code and agentic tool calling |

Add open/local models only after exact version, context implementation, quantization, hardware, and serving configuration are declared.

## Benchmark targets

Use frozen commits and access-safe copies or worktrees for:

1. `founder-mode` — large operational, multi-agent, governance-heavy system
2. `hummbl-governance` — dense standards, schemas, validators, fixtures, and invariants
3. `hummbl-bibliography` — structured knowledge, source authority, identity, and provenance
4. `hummbl-production` — multi-stack product/deployment surface
5. one unfamiliar external repository with a compatible license and no privileged HUMMBL context

For corpus intelligence, include at least:

- a structured bibliography/source registry
- a multi-document research packet
- a long historical/OCR corpus sample
- a mixed-format packet containing text, PDF, table, and image evidence where permitted
- a globally distributed evidence task where no single chunk contains the answer

Private content must remain in approved execution environments. Public benchmark releases must use public-safe fixtures or derived redacted cases.

## Experimental conditions

Evaluate at least three context architectures:

```text
A. SINGLE_CONTEXT — pack the allowed repository/corpus into one model context where feasible
B. TOOL_NAVIGATED — model uses identical file/search/shell tools over the frozen source
C. MEMORY_AUGMENTED — deterministic inventory + structured intermediate records + retrieval + persistent evidence/claim graph
```

Optional fourth condition:

```text
D. MULTI_AGENT — bounded specialist agents with explicit task decomposition, shared evidence state, and synthesis review
```

Do not compare a bare model against a heavily engineered competing scaffold without reporting the difference.

## Core task families

### Repository understanding

- reconstruct architecture and major responsibility boundaries
- identify source-of-truth files and authority hierarchy
- produce a dependency and execution graph
- trace one invariant through code, tests, docs, and CI
- locate phantom or stale references
- detect contradictory claims across files
- identify generated/binary/vendor content that should be excluded
- explain one issue's likely root cause
- propose a bounded patch plan
- implement and validate one controlled issue where authorized
- cite exact file paths, symbols, commits, and line ranges

### Corpus intelligence

- entity/source identity resolution
- authority and evidence classification
- multi-hop synthesis across distant documents
- contradiction and correction detection
- temporal/version reasoning
- claim-to-source mapping
- uncertainty identification
- omission detection
- generation of a reproducible source-bounded report

### Governance and honesty

- distinguish verified facts, inference, proposal, and unknowns
- refuse unsupported novelty or completion claims
- identify privacy, licensing, and publication boundaries
- preserve negative results and unresolved ambiguity
- avoid treating proxy signals as authoritative state

## Ground truth and grading

Each task must have:

- frozen source SHA and manifest
- human-reviewed answer key or invariant set
- explicit acceptable alternatives
- hidden adversarial and omission checks
- severity-weighted error taxonomy
- source-citation verification
- blind or anonymized scoring where feasible

Grade separately:

```text
retrieval coverage
factual precision
architecture accuracy
cross-file reasoning
contradiction detection
uncertainty calibration
citation validity
patch correctness
validation completeness
privacy/authority compliance
latency
input/output tokens
monetary cost
human correction time
```

Do not collapse all results into one universal winner. Report role fitness and Pareto frontiers.

## Fairness controls

- Pin exact model IDs or snapshots where possible
- Record date, region, API/provider, reasoning level, temperature, tool access, rate limits, and retry policy
- Use materially equivalent source access and task instructions
- Cap tool calls, wall-clock time, and token/cost budget by declared condition
- Separate model capability from scaffold quality
- Repeat nondeterministic trials
- Preserve failures, timeouts, abstentions, and malformed outputs
- Do not use one tested model to author the final evaluation of itself without independent review
- Check for benchmark contamination and privileged repo familiarity

## External benchmark crosswalk

Map internal task families to, but do not substitute them with:

- RepoBench
- ExecRepoBench
- SWE-bench / SWE-bench Pro
- Terminal-Bench
- LongBench / long-context multi-hop evaluations
- corpus-level QA and memory-agent evaluations

Record benchmark versions, harnesses, and whether scores are provider-reported or independently reproduced.

## Required child workstreams

- Harness and reproducibility implementation in `autoresearch-pipeline`
- Source/corpus pack and authority manifest in `hummbl-bibliography` or the admitted corpus home
- Evidence-backed routing policy in `model-routing-as-code`
- Final benchmark report and publication-readiness decision under the research-integrity program

## Required outputs

1. Benchmark specification and threat model
2. Frozen source manifests
3. Public-safe and private benchmark partitions
4. Task schemas and fixtures
5. Runner adapters for each admitted model/provider
6. Raw run receipts and normalized result schema
7. Human correction/time log
8. Role-fitness scorecard and Pareto analysis
9. Reproducibility packet
10. Routing recommendations with reevaluation date
11. Public-claim and publication disposition

## Final dispositions

For each model × scaffold × workload class:

```text
REJECTED
DISCOVERY_ONLY
BOUNDED_READER
PRIMARY_READER_WITH_REVIEW
IMPLEMENTER_WITH_GATES
INDEPENDENT_REVIEWER
PROMOTED_WITH_SCOPE
```

## Acceptance criteria

- [x] Benchmark specification documented
- [x] Model roster with verified official specifications (7 models)
- [x] Benchmark targets identified (5 repos + 5 corpus types)
- [x] Experimental conditions defined (3 required + 1 optional)
- [x] Core task families documented (3 families, 25+ tasks)
- [x] Ground truth and grading framework documented (14 metrics)
- [x] Fairness controls documented (9 controls)
- [x] External benchmark crosswalk documented (6 benchmarks)
- [x] Required outputs listed (11 deliverables)
- [x] Final dispositions defined (7)
- [ ] Harness implementation in autoresearch-pipeline
- [ ] Frozen source manifests
- [ ] Task schemas and fixtures
- [ ] Runner adapters
- [ ] Raw run receipts
- [ ] Role-fitness scorecard
- [ ] Routing recommendations

## Non-goals

- Does not declare a vendor winner
- Does not substitute external benchmarks for internal evaluation
- Does not expose private repo material in public artifacts
- Does not collapse results into one universal winner
- Does not authorize routing changes without operator approval

## Related

- `hummbl-dev/hummbl-dev#153` — Research Integrity master program index
- `hummbl-dev/hummbl-dev#154` — Intentional Repository Scale & Responsibility Topology
- `hummbl-dev/hummbl-dev#156` — Model Market & Routing Control Plane
- `hummbl-dev/autoresearch-pipeline#31` — benchmark harness

## Fact posture

Model specifications were retrieved 2026-07-10 from official provider documentation. No benchmark results are claimed in this document. All model positioning is sourced from provider documentation, not independently verified by HUMMBL.

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#155
- **Model roster**: 7 (verified official specs as of 2026-07-10)
- **Benchmark targets**: 5 repos + 5 corpus types
- **Experimental conditions**: 3 required + 1 optional
- **Task families**: 3 (repository, corpus, governance)
- **Grading metrics**: 14
- **Fairness controls**: 9
- **Required outputs**: 11
- **Final dispositions**: 7
- **Review status**: PENDING
