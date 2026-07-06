# Integrity Check Catalog v0.1

**Status**: candidate (not canon)
**Date**: 2026-07-06
**Issue**: [hummbl-dev/hummbl-dev#109](https://github.com/hummbl-dev/hummbl-dev/issues/109)
**Composes with**: [Autoresearch Packet v0.1](../../autoresearch-packet/v0.1/schema.json) (#108)

## Purpose

Each integrity check (IC) is a deterministic, stdlib-verifiable rule that gates whether a keep/discard verdict can be trusted before it feeds the next iteration. A check that fails hard-rejects the verdict.

## Source taxonomy

The five checks below map to documented failure modes in the autoresearch literature:

| # | Failure mode | Source | Source class |
|---|-------------|--------|-------------|
| IC-1 | Post-hoc selection bias / seed luck | arXiv:2509.08713, arXiv:2407.01502 | [PRIM], [SEC] |
| IC-2 | Evaluator tampering | arXiv:2603.11337 | [SEC] |
| IC-3 | Train/test (holdout) leakage | arXiv:2603.11337, arXiv:2509.08713 | [SEC], [PRIM] |
| IC-4 | Metric misuse / naive decision rule | karpathy/autoresearch README | [PRIM] |
| IC-5 | Silent failure | HUMMBL autoresearch-pipeline 2026-07-06 batch | [OBS] |

**Source class legend**: `[PRIM]` = primary source verified, `[SEC]` = secondary (search-surfaced, arXiv ID cited), `[OBS]` = direct HUMMBL observation, `[INF]` = inferred.

---

## IC-1: Seed variance gate

**Failure mode**: Post-hoc selection bias / seed luck. A single-seed run that beats baseline within the noise floor is kept, optimizing luck rather than the objective.

**HUMMBL manifestation**: `results.tsv` records one `val_bpb` per run with no seed, no variance, no reseeded verification.

**Check**:
- `n_seeds >= k` (default k=3) for any keep verdict
- `noise_floor` = measured baseline seed variance (std dev across ≥3 baseline seeds)
- `delta` = candidate_mean − baseline_mean (signed)
- `metric_direction` = "minimize" or "maximize"
- **Reject keep if improvement is within noise floor:**
  - For `minimize`: reject if `delta >= -noise_floor` (improvement is `delta < 0`; must exceed noise)
  - For `maximize`: reject if `delta <= noise_floor` (improvement is `delta > 0`; must exceed noise)
- `per_seed_metric[]` must have exactly `n_seeds` entries

**Inputs**: `n_seeds`, `per_seed_metric[]`, `noise_floor`, `metric_direction`, `delta` (candidate mean − baseline mean)

**Pass condition**: `n_seeds >= k` AND `len(per_seed_metric) == n_seeds` AND (for minimize: `delta < -noise_floor`; for maximize: `delta > noise_floor`)

**Fail condition**: `n_seeds < k` OR `len(per_seed_metric) != n_seeds` OR (for minimize: `delta >= -noise_floor`; for maximize: `delta <= noise_floor`)

---

## IC-2: Evaluator integrity

**Failure mode**: Evaluator tampering. The scored diff edits the evaluator/metric path, not just the training code, inflating the metric without real improvement.

**HUMMBL manifestation**: Agent could modify `prepare.py::evaluate_bpb` to return a lower value without changing the model.

**Check**:
- `evaluator_hash` = SHA256 of the measurement entrypoint file at scoring time
- `baseline_evaluator_hash` = SHA256 of the same file at baseline
- **Reject if `evaluator_hash != baseline_evaluator_hash`** (the evaluator was modified by the scored diff)

**Inputs**: `evaluator_hash`, `baseline_evaluator_hash`

**Pass condition**: `evaluator_hash == baseline_evaluator_hash`

**Fail condition**: `evaluator_hash != baseline_evaluator_hash`

---

## IC-3: Holdout provenance

**Failure mode**: Train/test leakage. The held-out validation set is reachable or editable during training, allowing the model to memorize eval data.

**HUMMBL manifestation**: `VAL_SHARD` is a fixed data shard; if the training data loader can read it, leakage is possible.

**Check**:
- `holdout_provenance` must be declared (non-empty string describing the holdout source)
- `holdout_path` must be declared (the path the eval step reads)
- `train_paths[]` must be declared (paths the train step reads)
- **Reject if `holdout_path` is in `train_paths[]`** (the train step can read the holdout)

**Inputs**: `holdout_provenance`, `holdout_path`, `train_paths[]`

**Pass condition**: `holdout_provenance` non-empty AND `holdout_path` not in `train_paths`

**Fail condition**: `holdout_provenance` empty OR `holdout_path` in `train_paths`

---

## IC-4: Decision rule explicitness

**Failure mode**: Metric misuse / naive decision rule. A raw "did it improve?" check with no threshold, no variance accounting, and no reseeded verification.

**HUMMBL manifestation**: karpathy/autoresearch decides by "checks if the result improved, keeps or discards" — no noise floor, no reseed. [PRIM, verified 2026-07-06]

**Check**:
- `decision_rule` must be declared (non-empty string, e.g., "threshold_vs_noise_floor")
- `decision_rule` must not be "naive_improve" (the ungoverned default)
- If `decision_rule` includes "reseeded_verification", then `reseeded_verification.ran` must be true and `reseeded_verification.delta` must be present

**Inputs**: `decision_rule`, `reseeded_verification{ran, delta}`

**Pass condition**: `decision_rule` non-empty AND `decision_rule != "naive_improve"` AND (if reseeded_verification referenced, `ran == true` and `delta` present)

**Fail condition**: `decision_rule` empty OR `decision_rule == "naive_improve"` OR (reseeded referenced but `ran != true` or `delta` missing)

---

## IC-5: Failure receipt completeness

**Failure mode**: Silent failure. A receipt records `status=failed` but no error code, making the failure un diagnosable and un-auditable.

**HUMMBL manifestation**: 2026-07-06 automated batch produced receipts with `status=failed, val_bpb=null, error_code=null`.

**Check**:
- If `status == "failed"` or `status == "crash"`, then `error_code` must be non-null and non-empty
- If `status == "keep"` or `status == "discard"`, IC-5 does not apply (other ICs gate the verdict)

**Inputs**: `status`, `error_code`

**Pass condition**: `status` in ("keep", "discard") OR (`status` in ("failed", "crash") AND `error_code` non-empty)

**Fail condition**: `status` in ("failed", "crash") AND (`error_code` is null or empty)

---

## Check severity

| Check | Severity | Rationale |
|-------|----------|-----------|
| IC-1 | hard | Seed luck is the primary drift source over long search horizons |
| IC-2 | hard | Evaluator tampering invalidates all downstream results |
| IC-3 | hard | Holdout leakage invalidates the metric itself |
| IC-4 | hard | Naive decision rule is the root cause of ungoverned keep/discard |
| IC-5 | hard | Silent failures break auditability |

All checks are hard-fail. A soft-fail tier may be introduced in v0.2.
