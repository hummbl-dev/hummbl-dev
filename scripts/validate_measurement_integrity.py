#!/usr/bin/env python3
"""Validate an Autoresearch Measurement Integrity v0.1 receipt.

Runs IC-1 through IC-5 over a receipt JSON. Stdlib-only.

Usage:
    python scripts/validate_measurement_integrity.py <receipt.json>
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

SCHEMA_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs/autoresearch-measurement-integrity/v0.1/schema-additions.json"
)

DEFAULT_MIN_SEEDS = 3


class ValidationError(Exception):
    """Raised when a receipt fails an integrity check."""


def load_json(path: Path) -> dict[str, Any]:
    try:
        with path.open(encoding="utf-8") as handle:
            data = json.load(handle)
    except OSError as exc:
        raise ValidationError(f"cannot read {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValidationError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValidationError(f"{path} must contain a JSON object")
    return data


def check_required_fields(receipt: dict[str, Any]) -> None:
    """Check that all required fields are present (schema-level)."""
    required = [
        "integrity_version",
        "n_seeds",
        "per_seed_metric",
        "noise_floor",
        "evaluator_hash",
        "baseline_evaluator_hash",
        "holdout_provenance",
        "holdout_path",
        "train_paths",
        "decision_rule",
        "reseeded_verification",
        "status",
        "error_code",
    ]
    for field in required:
        if field not in receipt:
            raise ValidationError(f"missing required field: {field}")


def ic1_seed_variance(receipt: dict[str, Any], min_seeds: int = DEFAULT_MIN_SEEDS) -> None:
    """IC-1: Reject keep if delta < noise_floor or n_seeds < k."""
    status = receipt.get("status", "")
    if status not in ("keep", "discard"):
        return  # IC-1 only gates keep/discard verdicts

    n_seeds = receipt.get("n_seeds", 0)
    per_seed = receipt.get("per_seed_metric", [])
    noise_floor = receipt.get("noise_floor", 0)
    delta = receipt.get("delta", 0)

    if n_seeds < min_seeds:
        raise ValidationError(
            f"IC-1 FAIL: n_seeds={n_seeds} < minimum {min_seeds}"
        )
    if len(per_seed) != n_seeds:
        raise ValidationError(
            f"IC-1 FAIL: per_seed_metric has {len(per_seed)} entries, "
            f"expected {n_seeds}"
        )
    if status == "keep" and abs(delta) <= noise_floor:
        raise ValidationError(
            f"IC-1 FAIL: delta={delta} within noise_floor={noise_floor} "
            "(improvement is seed luck, not real)"
        )


def ic2_evaluator_integrity(receipt: dict[str, Any]) -> None:
    """IC-2: Reject if evaluator_hash != baseline_evaluator_hash."""
    eval_hash = receipt.get("evaluator_hash", "")
    baseline_hash = receipt.get("baseline_evaluator_hash", "")
    if eval_hash != baseline_hash:
        raise ValidationError(
            f"IC-2 FAIL: evaluator_hash={eval_hash} != "
            f"baseline={baseline_hash} (evaluator was modified)"
        )


def ic3_holdout_provenance(receipt: dict[str, Any]) -> None:
    """IC-3: Reject if holdout_path is in train_paths or provenance empty."""
    provenance = receipt.get("holdout_provenance", "")
    holdout_path = receipt.get("holdout_path", "")
    train_paths = receipt.get("train_paths", [])

    if not provenance:
        raise ValidationError(
            "IC-3 FAIL: holdout_provenance is empty"
        )
    if holdout_path in train_paths:
        raise ValidationError(
            f"IC-3 FAIL: holdout_path '{holdout_path}' is in train_paths "
            "(holdout leakage)"
        )


def ic4_decision_rule(receipt: dict[str, Any]) -> None:
    """IC-4: Reject naive_improve or missing reseeded_verification."""
    rule = receipt.get("decision_rule", "")
    if not rule:
        raise ValidationError(
            "IC-4 FAIL: decision_rule is empty"
        )
    if rule == "naive_improve":
        raise ValidationError(
            "IC-4 FAIL: decision_rule='naive_improve' is not governed"
        )
    if "reseeded" in rule:
        rv = receipt.get("reseeded_verification", {})
        if not rv.get("ran"):
            raise ValidationError(
                "IC-4 FAIL: decision_rule references reseeded_verification "
                "but ran is not true"
            )
        if "delta" not in rv:
            raise ValidationError(
                "IC-4 FAIL: decision_rule references reseeded_verification "
                "but delta is missing"
            )


def ic5_failure_receipt(receipt: dict[str, Any]) -> None:
    """IC-5: Reject failed/crash receipts without error_code."""
    status = receipt.get("status", "")
    if status in ("failed", "crash"):
        error_code = receipt.get("error_code")
        if not error_code:
            raise ValidationError(
                f"IC-5 FAIL: status={status} but error_code is null/empty "
                "(silent failure)"
            )


def validate_receipt(receipt: dict[str, Any]) -> list[str]:
    """Run all IC checks. Returns list of check names that passed."""
    check_required_fields(receipt)
    checks = [
        ("IC-1", ic1_seed_variance),
        ("IC-2", ic2_evaluator_integrity),
        ("IC-3", ic3_holdout_provenance),
        ("IC-4", ic4_decision_rule),
        ("IC-5", ic5_failure_receipt),
    ]
    passed = []
    for name, check in checks:
        check(receipt)
        passed.append(name)
    return passed


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(
            "Usage: python scripts/validate_measurement_integrity.py <receipt.json>",
            file=sys.stderr,
        )
        return 2

    fixture_path = Path(argv[1])
    try:
        receipt = load_json(fixture_path)
        passed = validate_receipt(receipt)
    except ValidationError as exc:
        print(f"VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1

    print(
        f"VALIDATION PASSED: {passed} "
        f"(status={receipt['status']}, n_seeds={receipt['n_seeds']}, "
        f"decision_rule={receipt['decision_rule']})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
