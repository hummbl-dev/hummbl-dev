# Frontier Lab Classification v0.1 — Archetypes, Capability Tiers, Assurance Grades

**Status: CANDIDATE RESEARCH/GOVERNANCE PACKET — NON-CANONICAL**

Issue: hummbl-dev/hummbl-dev#140

## Context

A defensible way to categorize "frontier labs" without collapsing model capability, specialization, infrastructure power, safety maturity, reputation, and commercial scale into one prestige leaderboard.

## Candidate classification model

> **Archetype × Frontier Capability Tier × Assurance Grade**, with optional modifiers, trajectory, evidence posture, and an `as_of` date.

Example: `FM/AGT – F1 – A2 – C,D – stable – as of 2026-07-10`

### 1. Archetype (10)

| Code | Archetype | Primary output |
|---|---|---|
| `FM` | General Frontier Model Lab | General-purpose foundation models |
| `OW` | Open-Weight Frontier Lab | Openly distributed models |
| `SV` | Sovereign Frontier Lab | National/state-backed capability |
| `INF` | Frontier Infrastructure Lab | Chips, training, inference, data |
| `AGT` | Agentic Systems Lab | Autonomous systems, orchestration |
| `EMB` | Embodied Intelligence Lab | Robotics, physical-world models |
| `SCI` | AI-for-Science Lab | Scientific discovery |
| `BIO` | AI-Biology Lab | Genomics, proteins, drug discovery |
| `SAFE` | Safety and Assurance Lab | Evals, interpretability, alignment |
| `APP` | Applied Frontier Lab | Bounded industry application |

### 2. Frontier capability tier (7)

- **F0** — Frontier-Setting
- **F1** — Frontier-Competitive
- **F2** — Near-Frontier Challenger
- **F3** — Specialized Frontier
- **F4** — Frontier-Enabling
- **F5** — Emerging Frontier Candidate
- **N** — Not Currently Frontier

### 3. Assurance grade (5)

- **A0** — Opaque or materially unassessable
- **A1** — Minimal voluntary safety claims
- **A2** — Documented internal controls and evaluations
- **A3** — Strong evaluation regime, external testing
- **A4** — Independently auditable assurance system

### 4. Optional modifiers (8)

- `O` — open-weight/open-source
- `C` — closed/proprietary
- `S` — sovereign/state-backed
- `I` — infrastructure-dependent
- `D` — deployment-scale operator
- `R` — research-first
- `P` — product-first
- `X` — classification uncertain

### 5. Trajectory (4)

- `rising`
- `stable`
- `declining`
- `uncertain`

## Candidate packet layout

```text
docs/research/frontier-labs/
├── README.md
├── methodology.md
├── taxonomy.md
├── scoring-and-gates.md
├── evidence-policy.md
├── registry.json
├── frontier-lab-classification.schema.json
└── fixtures/
    ├── valid-minimal.json
    ├── valid-full.json
    ├── invalid-missing-as-of.json
    ├── invalid-tier-without-gates.json
    └── invalid-unsupported-enum.json
```

## Acceptance criteria

- [x] 10 archetypes documented
- [x] 7 capability tiers documented
- [x] 5 assurance grades documented
- [x] 8 modifiers documented
- [x] 4 trajectory values documented
- [x] Packet layout documented
- [ ] Methodology and taxonomy docs
- [ ] Scoring gates and evidence policy
- [ ] Schema and validator
- [ ] Registry with evidence-backed entries
- [ ] Valid/invalid fixtures
- [ ] Independent review

## Non-goals

- Collapsing dimensions into one prestige leaderboard
- Using valuation, hype, or reputation as primary signal
- Benchmark cherry-picking
- Presenting candidate terminology as canon

## Fact posture

This is a candidate research/governance packet derived from issue #140. All terminology is candidate until reviewed and explicitly adopted.

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#140
- **Archetypes**: 10
- **Capability tiers**: 7
- **Assurance grades**: 5
- **Modifiers**: 8
- **Trajectory values**: 4
- **Review status**: PENDING
