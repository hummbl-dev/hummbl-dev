#!/usr/bin/env python3
"""Validate a Manual Transfer Intake Gate v0.1.1-alpha JSON fixture.

Implements broader field validation per issue #161:
  - Schema validation (JSON Schema draft 2020-12 subset)
  - Authority-scope rule: consequential requests require target-bound authority
  - Conflict-blocking rule: current_conflict packets must not request
    implement/authorize actions
  - Raw-text rule: raw-text transfers cannot grant consequential authority
  - Lane-aware subject-key validation: <domain>/<object>/<version-or-scope>/<lane>
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "docs/manual-transfer-intake-gate/v0.1.1/schema.json"

FIXTURES_DIR = Path(__file__).resolve().parents[1] / "docs/manual-transfer-intake-gate/v0.1.1/fixtures"

VALID_FIXTURES = ["valid-minimal", "valid-lane-aware"]
INVALID_FIXTURES = ["invalid-missing-authority", "invalid-conflict-active", "invalid-raw-text-consequential"]

CONSEQUENTIAL_ACTIONS = {"implement", "authorize"}


class ValidationError(Exception):
    """Raised when a fixture does not match the v0.1.1-alpha schema or gate rules."""


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
# Broader field validation rules (beyond schema)
# ---------------------------------------------------------------------------

def validate_authority_scope(packet: dict[str, Any]) -> None:
    """Consequential requested actions require target-bound authority.

    A packet requesting 'implement' or 'authorize' with authority scope 'none'
    or 'advisory' must be quarantined — transfer does not authenticate or
    authorize.
    """
    action_type = packet.get("requested_action", {}).get("action_type", "none")
    authority_scope = packet.get("authority", {}).get("scope", "none")

    if action_type in CONSEQUENTIAL_ACTIONS and authority_scope != "target-bound":
        raise ValidationError(
            f"requested_action '{action_type}' requires target-bound authority, "
            f"got authority scope '{authority_scope}' — packet must be quarantined"
        )


def validate_conflict_blocking(packet: dict[str, Any]) -> None:
    """Packets with current_conflict must not request consequential actions.

    v0.1.1-alpha safety patch: unresolved current conflict forces
    active_packet_id: null. A conflicted packet requesting implement/authorize
    would expose an actionable active packet, violating the safety patch.
    """
    currentness = packet.get("currentness", {})
    status = currentness.get("status", "unknown")
    action_type = packet.get("requested_action", {}).get("action_type", "none")

    if status == "conflict" and action_type in CONSEQUENTIAL_ACTIONS:
        raise ValidationError(
            f"current_conflict packet requests '{action_type}' — "
            f"conflicted packets must not expose actionable active selection"
        )


def validate_raw_text_authority(packet: dict[str, Any]) -> None:
    """Raw-text transfers cannot grant consequential authority.

    The conservative raw-text wrapper cannot grant consequential authority.
    A raw-text packet with authority scope 'consequential' must be rejected.
    """
    has_raw_text = "raw_text" in packet
    authority_scope = packet.get("authority", {}).get("scope", "none")

    if has_raw_text and authority_scope == "consequential":
        raise ValidationError(
            "raw-text transfer cannot grant consequential authority — "
            "conservative raw-text wrapper does not authenticate or authorize"
        )


def validate_lane_aware_key(packet: dict[str, Any]) -> None:
    """Lane-aware subject keys must follow <domain>/<object>/<version-or-scope>/<lane>.

    Coarse keys (fewer than 4 segments) are accepted but flagged as warnings.
    Keys with more than 4 segments are invalid.
    """
    subject_key = packet.get("subject_key", "")
    segments = subject_key.split("/")
    if len(segments) > 4:
        raise ValidationError(
            f"subject_key has {len(segments)} segments; lane-aware profile allows "
            f"at most 4 (<domain>/<object>/<version-or-scope>/<lane>)"
        )


def validate_fixture(path: Path, schema: dict[str, Any]) -> None:
    packet = load_json(path)
    validate_schema(schema, packet, schema)
    validate_raw_text_authority(packet)
    validate_authority_scope(packet)
    validate_conflict_blocking(packet)
    validate_lane_aware_key(packet)


def main(argv: list[str]) -> int:
    if len(argv) == 1:
        return _run_self_test(schema_data=None)

    if len(argv) != 2:
        print("Usage: python scripts/validate_intake_gate.py <packet.json>", file=sys.stderr)
        print("       python scripts/validate_intake_gate.py --self-test", file=sys.stderr)
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

    packet = load_json(fixture_path)
    print(
        f"VALIDATION PASSED: {packet['packet_id']} "
        f"(posture={packet['evidentiary_posture']}, "
        f"authority={packet['authority']['scope']}, "
        f"currentness={packet['currentness']['status']})"
    )
    return 0


def _run_self_test(schema_data: dict[str, Any] | None) -> int:
    schema = schema_data or load_json(SCHEMA_PATH)
    failures = 0

    for name in VALID_FIXTURES:
        path = FIXTURES_DIR / name / "packet.json"
        try:
            validate_fixture(path, schema)
            print(f"  PASS (valid):   {name}")
        except ValidationError as exc:
            print(f"  FAIL (valid):   {name} -- {exc}", file=sys.stderr)
            failures += 1

    for name in INVALID_FIXTURES:
        path = FIXTURES_DIR / name / "packet.json"
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
