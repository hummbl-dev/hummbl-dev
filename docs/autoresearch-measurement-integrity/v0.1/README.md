# Autoresearch Measurement Integrity v0.1

**Status**: candidate (not canon)
**Date**: 2026-07-06
**Issue**: [hummbl-dev/hummbl-dev#109](https://github.com/hummbl-dev/hummbl-dev/issues/109)
**Composes with**: [Autoresearch Packet v0.1](../../autoresearch-packet/v0.1/README.md) (#108)

## What this is

A **candidate spec** for the governance layer of the measure → keep/discard step in an agent-driven experiment loop. Where #108 governs *what an experiment declares*, this governs *whether a keep/discard verdict can be trusted*.

```text
#108  packet.declare   →   #109  decision.verify   →   next iteration
      (what ran)               (is the verdict real?)
```

## What it is not

- **Not canon.** Candidate spec for operator review.
- **Not a runtime.** Schema, checks, and validator — not executable infrastructure.
- **Not a benchmark claim.** No performance or adoption claim about any referenced system.
- **Not a live-substrate change.** Docs-first only; no `autoresearch-pipeline` modifications.

## Why this exists

An autonomous loop that keeps on naive improvement will, over a long search horizon, optimize noise and its own evaluator rather than the objective. The 2026 literature documents this failure class directly:

- **Seed luck**: single-seed keeps within noise floor [PRIM, arXiv:2509.08713]
- **Evaluator tampering**: patching the metric code [SEC, arXiv:2603.11337]
- **Holdout leakage**: training on eval data [SEC, arXiv:2603.11337]
- **Naive decision rule**: raw improve-check with no threshold [PRIM, karpathy/autoresearch]
- **Silent failure**: failed receipts with no error code [OBS, HUMMBL 2026-07-06]

## Integrity checks

Five deterministic checks (IC-1 through IC-5), all hard-fail:

| IC | Failure mode | Check |
|----|-------------|-------|
| IC-1 | Seed luck | `n_seeds >= 3` AND `delta > noise_floor` |
| IC-2 | Evaluator tampering | `evaluator_hash == baseline_evaluator_hash` |
| IC-3 | Holdout leakage | `holdout_path` not in `train_paths` |
| IC-4 | Naive decision rule | `decision_rule != "naive_improve"` + reseed verification |
| IC-5 | Silent failure | `error_code` non-empty for failed/crash receipts |

See [integrity-checks.md](integrity-checks.md) for full definitions.

## Schema additions

Extends #108's experiment/receipt schema with: `n_seeds`, `per_seed_metric[]`, `noise_floor`, `delta`, `evaluator_hash`, `baseline_evaluator_hash`, `holdout_provenance`, `holdout_path`, `train_paths[]`, `decision_rule`, `reseeded_verification{ran, delta}`, `error_code`.

See [schema-additions.json](schema-additions.json).

## Files

```text
docs/autoresearch-measurement-integrity/v0.1/
├── README.md                          # this file
├── integrity-checks.md                # IC-1..IC-5 catalog
├── schema-additions.json              # fields extending #108
├── crosswalk-public-systems.md        # 7-system IC coverage crosswalk
└── fixtures/
    ├── valid-verified-keep/
    │   └── receipt.json               # valid: 3 seeds, delta > noise, hashes match
    ├── invalid-within-noise-floor/
    │   └── receipt.json               # invalid: delta within noise floor
    ├── invalid-evaluator-modified/
    │   └── receipt.json               # invalid: evaluator_hash mismatch
    └── invalid-holdout-leak/
        └── receipt.json               # invalid: holdout_path in train_paths

scripts/
└── validate_measurement_integrity.py  # stdlib-only IC-1..IC-5 validator
```

## Validation

```bash
# Valid fixture (should pass)
python scripts/validate_measurement_integrity.py \
    docs/autoresearch-measurement-integrity/v0.1/fixtures/valid-verified-keep/receipt.json

# Invalid fixtures (should fail)
python scripts/validate_measurement_integrity.py \
    docs/autoresearch-measurement-integrity/v0.1/fixtures/invalid-within-noise-floor/receipt.json
python scripts/validate_measurement_integrity.py \
    docs/autoresearch-measurement-integrity/v0.1/fixtures/invalid-evaluator-modified/receipt.json
python scripts/validate_measurement_integrity.py \
    docs/autoresearch-measurement-integrity/v0.1/fixtures/invalid-holdout-leak/receipt.json
```

## Non-canon notice

This spec is a **candidate**. It has not been adopted as HUMMBL canon. All claims about public repos carry source-class marks (`[PRIM]`/`[SEC]`/`[OBS]`/`[INF]`). No benchmark, performance, or adoption claim is made without evidence.
