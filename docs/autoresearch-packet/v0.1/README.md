# Autoresearch Packet v0.1

**Status**: candidate (not canon)
**Date**: 2026-07-06
**Issue**: [hummbl-dev/hummbl-dev#108](https://github.com/hummbl-dev/hummbl-dev/issues/108)

## What this is

A **candidate spec** for a minimal, auditable packet format for agent-driven experiment loops: modify, measure, keep/discard, repeat.

This packet models the common denominator across public autoresearch-style systems (Karpathy, Sakana, Microsoft, Vector Institute, and others) plus HUMMBL's governance layer (fact posture, receipts, safety bounds).

## What it is not

- **Not canon.** This is a candidate spec for operator review. It has not been adopted as a HUMMBL standard.
- **Not a runtime.** This is a schema and documentation artifact, not executable infrastructure.
- **Not a benchmark claim.** No performance, adoption, or superiority claim is made about any system referenced here.
- **Not a replacement for existing governance.** It complements existing HUMMBL evidence/receipt work; it does not supersede it.

## Why this packet exists

Public autoresearch systems share a common pattern: an agent modifies code, runs a measurement, decides keep/discard, and repeats. Each system implements this differently, but the common denominator is small and reusable:

- A named metric with a direction (minimize/maximize)
- A measurement command that produces the metric
- An editable scope (what the agent can change)
- A budget (time, steps, or cost)
- An append-only experiment ledger
- A keep/discard decision rule
- Safety bounds on agent autonomy

This packet formalizes that common denominator so that:
1. Experiment loops can be audited independently of the agent that ran them
2. Results from different systems can be compared on a common frame
3. HUMMBL governance (fact posture, receipts) can be applied to any autoresearch-style loop

## How it differs from ungoverned autonomous experimentation

| Dimension | Ungoverned | Packet v0.1 |
|-----------|-----------|-------------|
| Fact posture | implicit | explicit (public-source, local, candidate, derived) |
| Receipts | ad hoc | required, structured |
| Safety bounds | informal | explicit (autonomy level, rollback, scope) |
| Auditability | git history only | git + ledger + receipts + review |
| Claim/evidence | unseparated | separate ledgers for experiments and claims |

## How it relates to existing HUMMBL work

- **Evidence Graph v0.1**: The packet's `receipts` and `fact_posture` fields use the same enum values as the evidence graph schema.
- **hummbl-tuples**: The packet's `safety.autonomy_level` aligns with IDP tuple governance tiers.
- **autoresearch-pipeline**: The pipeline is the primary consumer candidate. Its `experiment.json`, `results.tsv`, and receipt files already implement most packet fields.

## What is intentionally out of scope

- Agent implementation (how the agent decides what to try next)
- Specific ML frameworks or training code
- Cloud GPU orchestration
- Multi-agent coordination protocols
- Publication-quality paper generation
- Benchmark dataset management

## Files

```
docs/autoresearch-packet/v0.1/
├── README.md                          # this file
├── schema.json                        # candidate JSON schema
├── fixtures/
│   ├── valid-minimal-packet/
│   │   └── packet.json                # valid fixture
│   └── invalid-missing-measurement/
│       └── packet.json                # invalid (empty measurement command)
└── crosswalks/
    └── public-autoresearch-repos.md   # 7-repo crosswalk

scripts/
└── validate_autoresearch_packet.py    # stdlib-only validator
```

## Validation

```bash
# Valid fixture (should pass)
python scripts/validate_autoresearch_packet.py \
    docs/autoresearch-packet/v0.1/fixtures/valid-minimal-packet/packet.json

# Invalid fixture (should fail)
python scripts/validate_autoresearch_packet.py \
    docs/autoresearch-packet/v0.1/fixtures/invalid-missing-measurement/packet.json
```

## Schema overview

Required fields:

| Field | Purpose |
|-------|---------|
| `packet_version` | Schema version (currently "0.1") |
| `packet_id` | Unique identifier for this packet |
| `title` | Human-readable name |
| `status` | candidate, active, deprecated, superseded |
| `objective` | Metric name, direction, description |
| `measurement` | Command, determinism, extraction method |
| `scope` | Editable, readonly, immutable paths |
| `budget` | Type (time/steps/cost/combined), value, safety margin |
| `ledgers` | Experiments path+format, claims path+format |
| `safety` | Autonomy level, auto-rollback, scope limits |
| `fact_posture` | Evidence classification for this packet |

Optional fields: `receipts`, `review`, `crosswalk_refs`

## Non-canon notice

This packet is a **candidate spec**. It has not been adopted as HUMMBL canon. All claims about public repos in the crosswalk are bounded public-source facts. No benchmark, performance, or adoption claim is made without evidence.
