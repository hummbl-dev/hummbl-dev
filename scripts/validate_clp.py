#!/usr/bin/env python3
"""Validate a Conversation Lifecycle Protocol v0.1 JSON fixture."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "docs/conversation-lifecycle-protocol/v0.1/schema.json"

FIXTURES_DIR = Path(__file__).resolve().parents[1] / "docs/conversation-lifecycle-protocol/v0.1/fixtures"

VALID_FIXTURES = ["valid-end-chat", "valid-work-session", "interrupted-checkpoint"]
INVALID_FIXTURES = ["invalid-bad-state-transition"]

# Profile -> allowed terminal lifecycle states
PROFILE_TERMINAL_STATES = {
    "end-chat": {"CLOSED"},
    "end-work-session": {"CLOSED"},
    "session-checkpoint": {"INTERRUPTED"},
}

# Disposition constraints per profile
PROFILE_DISPOSITIONS = {
    "end-chat": {"READY_TO_RESUME", "READY_WITH_GAPS", "NOT_READY"},
    "end-work-session": {"READY_TO_RESUME", "READY_WITH_GAPS", "NOT_READY"},
    "session-checkpoint": {"CHECKPOINT_ONLY"},
}


class ValidationError(Exception):
    """Raised when a fixture does not match the v0.1 schema or protocol rules."""


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
        or (expected == "integer" and isinstance(value, int) and not isinstance(value, bool))
    )


def validate_schema(schema: dict[str, Any], value: Any, root: dict[str, Any], path: str = "$") -> None:
    schema = ref_schema(schema, root)
    if "const" in schema and value != schema["const"]:
        raise ValidationError(f"{path} must be {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        raise ValidationError(f"{path} must be one of {schema['enum']}")
    if "minimum" in schema and isinstance(value, (int, float)) and value < schema["minimum"]:
        raise ValidationError(f"{path} must be >= {schema['minimum']}")

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


def validate_capability_uniqueness(session: dict[str, Any]) -> None:
    """Each capability must be declared at most once."""
    caps = [c["capability"] for c in session.get("capabilities", [])]
    duplicates = sorted({cap for cap in caps if caps.count(cap) > 1})
    if duplicates:
        raise ValidationError(f"duplicate capability declaration(s): {', '.join(duplicates)}")


def validate_step_ordering(session: dict[str, Any]) -> None:
    """Steps must be ordered sequentially starting at 1 with no gaps."""
    orders = [s["order"] for s in session.get("steps", [])]
    expected = list(range(1, len(orders) + 1))
    if orders != expected:
        raise ValidationError(f"step orders must be sequential 1..N, got {orders}")


def validate_profile_state(session: dict[str, Any]) -> None:
    """Terminal lifecycle state must be consistent with the profile."""
    profile = session.get("profile")
    state = session.get("lifecycle_state")
    if profile in PROFILE_TERMINAL_STATES:
        allowed = PROFILE_TERMINAL_STATES[profile]
        if state not in allowed:
            raise ValidationError(
                f"profile '{profile}' requires terminal state in {sorted(allowed)}, "
                f"got '{state}'"
            )


def validate_profile_disposition(session: dict[str, Any]) -> None:
    """Disposition must be consistent with the profile."""
    profile = session.get("profile")
    disposition = session.get("disposition")
    if profile in PROFILE_DISPOSITIONS:
        allowed = PROFILE_DISPOSITIONS[profile]
        if disposition not in allowed:
            raise ValidationError(
                f"profile '{profile}' requires disposition in {sorted(allowed)}, "
                f"got '{disposition}'"
            )


def validate_fixture(path: Path, schema: dict[str, Any]) -> None:
    session = load_json(path)
    validate_schema(schema, session, schema)
    validate_capability_uniqueness(session)
    validate_step_ordering(session)
    validate_profile_state(session)
    validate_profile_disposition(session)


def main(argv: list[str]) -> int:
    if len(argv) == 1:
        # Self-test mode: validate all fixtures
        return _run_self_test(schema_data=None)

    if len(argv) != 2:
        print("Usage: python scripts/validate_clp.py <session.json>", file=sys.stderr)
        print("       python scripts/validate_clp.py --self-test", file=sys.stderr)
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

    session = load_json(fixture_path)
    print(
        f"VALIDATION PASSED: {session['session_id']} "
        f"(profile={session['profile']}, state={session['lifecycle_state']}, "
        f"disposition={session['disposition']}, {len(session['steps'])} steps)"
    )
    return 0


def _run_self_test(schema_data: dict[str, Any] | None) -> int:
    schema = schema_data or load_json(SCHEMA_PATH)
    failures = 0

    for name in VALID_FIXTURES:
        path = FIXTURES_DIR / name / "session.json"
        try:
            validate_fixture(path, schema)
            print(f"  PASS (valid):   {name}")
        except ValidationError as exc:
            print(f"  FAIL (valid):   {name} — {exc}", file=sys.stderr)
            failures += 1

    for name in INVALID_FIXTURES:
        path = FIXTURES_DIR / name / "session.json"
        try:
            validate_fixture(path, schema)
            print(f"  FAIL (invalid): {name} — expected validation error but passed", file=sys.stderr)
            failures += 1
        except ValidationError as exc:
            print(f"  PASS (invalid): {name} — correctly rejected: {exc}")

    if failures:
        print(f"\nSELF-TEST FAILED: {failures} failure(s)", file=sys.stderr)
        return 1

    total = len(VALID_FIXTURES) + len(INVALID_FIXTURES)
    print(f"\nSELF-TEST PASSED: {total}/{total} fixtures validated correctly")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
