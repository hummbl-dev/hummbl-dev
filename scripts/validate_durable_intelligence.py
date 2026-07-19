#!/usr/bin/env python3
"""Validate an Agent Session Receipt v0.1 JSON fixture.

Implements the Durable Intelligence Doctrine operational adoption per issue #162:
  - Schema validation (JSON Schema draft 2020-12 subset)
  - Mutation truthfulness: mutations_made is mandatory and every record
    must have a boolean 'created' field
  - Environment capability disclosure: tools_available must declare at
    least one tool category
  - Claim posture validation: every claim must have an explicit posture
  - Re-entry verification guidance: receipt_destination must be a durable
    sink (not chat-only)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "docs/durable-intelligence-doctrine/v0.1/schema.json"

FIXTURES_DIR = Path(__file__).resolve().parents[1] / "docs/durable-intelligence-doctrine/v0.1/fixtures"

VALID_FIXTURES = ["valid-session-receipt"]
INVALID_FIXTURES = ["invalid-missing-mutations"]

# Durable sinks per the doctrine — chat-only is not acceptable
DURABLE_SINKS = {
    "github_issue",
    "github_pr_comment",
    "receipt_directory",
    "claim_evidence_ledger",
    "task_registry",
    "handoff_index",
}


class ValidationError(Exception):
    """Raised when a receipt does not match the v0.1 schema or doctrine rules."""


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


def ref_schema(schema: dict[str, Any], root: dict[str, Any]) -> dict[str, Any]:
    ref = schema.get("$ref")
    if not ref:
        return schema
    prefix = "#/$defs/"
    if not isinstance(ref, str) or not ref.startswith(prefix):
        raise ValidationError(f"unsupported schema ref: {ref}")
    name = ref.removeprefix(prefix)
    try:
        return root["$defs"][name]
    except KeyError as exc:
        raise ValidationError(f"unknown schema ref: {ref}") from exc


def type_ok(expected: str, value: Any) -> bool:
    return (
        (expected == "object" and isinstance(value, dict))
        or (expected == "array" and isinstance(value, list))
        or (expected == "string" and isinstance(value, str))
        or (expected == "boolean" and isinstance(value, bool))
        or (expected == "integer" and isinstance(value, int) and not isinstance(value, bool))
    )


def validate_schema(schema: dict[str, Any], value: Any, root: dict[str, Any], path: str = "$") -> None:
    schema = ref_schema(schema, root)
    if "const" in schema and value != schema["const"]:
        raise ValidationError(f"{path} must be {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        raise ValidationError(f"{path} must be one of {schema['enum']}")

    expected_type = schema.get("type")
    if expected_type:
        if not type_ok(expected_type, value):
            raise ValidationError(f"{path} must be a {expected_type}")
        if expected_type == "object":
            validate_object(schema, value, root, path)
        elif expected_type == "array":
            validate_array(schema, value, root, path)
        elif expected_type == "string" and len(value) < schema.get("minLength", 0):
            raise ValidationError(f"{path} must not be empty")


def validate_object(schema: dict[str, Any], value: dict[str, Any], root: dict[str, Any], path: str) -> None:
    properties = schema.get("properties", {})
    for key in schema.get("required", []):
        if key not in value:
            raise ValidationError(f"{path} missing required property: {key}")
    if schema.get("additionalProperties") is False:
        extra = sorted(set(value) - set(properties))
        if extra:
            raise ValidationError(f"{path} has unexpected properties: {', '.join(extra)}")
    for key, child_schema in properties.items():
        if key in value:
            validate_schema(child_schema, value[key], root, f"{path}.{key}")


def validate_array(schema: dict[str, Any], value: list[Any], root: dict[str, Any], path: str) -> None:
    min_items = schema.get("minItems")
    if min_items is not None and len(value) < min_items:
        raise ValidationError(f"{path} must contain at least {min_items} item(s)")
    item_schema = schema.get("items")
    if item_schema:
        for index, item in enumerate(value):
            validate_schema(item_schema, item, root, f"{path}[{index}]")


# ---------------------------------------------------------------------------
# Doctrine-specific validation rules
# ---------------------------------------------------------------------------

def validate_mutation_truthfulness(receipt: dict[str, Any]) -> None:
    """Every receipt must explicitly state whether mutations were made.

    Mutation truthfulness is mandatory. A receipt without mutations_made
    is invalid — no artifact may be implied without a confirmed identifier.
    """
    mutations = receipt.get("mutations_made")
    if mutations is None:
        raise ValidationError("mutations_made is required — mutation truthfulness is mandatory")

    records = mutations.get("records", []) if isinstance(mutations, dict) else []
    for i, record in enumerate(records):
        if "created" not in record:
            raise ValidationError(
                f"mutations_made.records[{i}] missing 'created' field — "
                f"every mutation record must explicitly state whether it was created"
            )


def validate_durable_sink(receipt: dict[str, Any]) -> None:
    """Receipt destination must be a durable, discoverable sink.

    Chat-only preservation is insufficient for operational continuity.
    """
    dest = receipt.get("receipt_destination", {})
    dest_type = dest.get("type", "")
    if dest_type and dest_type not in DURABLE_SINKS:
        raise ValidationError(
            f"receipt_destination type '{dest_type}' is not a durable sink — "
            f"chat-only preservation is insufficient; approved sinks: {sorted(DURABLE_SINKS)}"
        )


def validate_claim_postures(receipt: dict[str, Any]) -> None:
    """Every claim must have an explicit posture from the doctrine vocabulary.

    Agents must not infer that review implies mutation, discussion implies
    verification, or a previous verdict implies independent confirmation.
    """
    claims = receipt.get("claims", [])
    for i, claim in enumerate(claims):
        if "posture" not in claim:
            raise ValidationError(
                f"claims[{i}] missing 'posture' — claim posture must be explicit"
            )


def validate_fixture(path: Path, schema: dict[str, Any]) -> None:
    receipt = load_json(path)
    validate_schema(schema, receipt, schema)
    validate_mutation_truthfulness(receipt)
    validate_durable_sink(receipt)
    validate_claim_postures(receipt)


def main(argv: list[str]) -> int:
    if len(argv) == 1:
        return _run_self_test(schema_data=None)

    if len(argv) != 2:
        print("Usage: python scripts/validate_durable_intelligence.py <receipt.json>", file=sys.stderr)
        print("       python scripts/validate_durable_intelligence.py --self-test", file=sys.stderr)
        return 2

    if argv[1] == "--self-test":
        return _run_self_test(schema_data=None)

    fixture_path = Path(argv[1])
    try:
        schema = load_json(SCHEMA_PATH)
        validate_fixture(fixture_path, schema)
    except ValidationError as exc:
        print(f"VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1

    receipt = load_json(fixture_path)
    print(
        f"VALIDATION PASSED: {receipt['session_id']} "
        f"(agent={receipt['source_agent']}, status={receipt['completion_status']}, "
        f"{len(receipt.get('claims', []))} claims, "
        f"{len(receipt.get('negative_knowledge', []))} negative-knowledge items)"
    )
    return 0


def _run_self_test(schema_data: dict[str, Any] | None) -> int:
    schema = schema_data or load_json(SCHEMA_PATH)
    failures = 0

    for name in VALID_FIXTURES:
        path = FIXTURES_DIR / name / "receipt.json"
        try:
            validate_fixture(path, schema)
            print(f"  PASS (valid):   {name}")
        except ValidationError as exc:
            print(f"  FAIL (valid):   {name} -- {exc}", file=sys.stderr)
            failures += 1

    for name in INVALID_FIXTURES:
        path = FIXTURES_DIR / name / "receipt.json"
        try:
            validate_fixture(path, schema)
            print(f"  FAIL (invalid): {name} -- expected validation error but passed", file=sys.stderr)
            failures += 1
        except ValidationError as exc:
            print(f"  PASS (invalid): {name} -- correctly rejected: {exc}")

    if failures:
        print(f"\nSELF-TEST FAILED: {failures} failure(s)", file=sys.stderr)
        return 1

    total = len(VALID_FIXTURES) + len(INVALID_FIXTURES)
    print(f"\nSELF-TEST PASSED: {total}/{total} fixtures validated correctly")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
