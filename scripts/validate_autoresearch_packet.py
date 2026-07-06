#!/usr/bin/env python3
"""Validate an Autoresearch Packet v0.1 JSON fixture.

Stdlib-only. Validates against the candidate schema at
docs/autoresearch-packet/v0.1/schema.json.

Usage:
    python scripts/validate_autoresearch_packet.py <packet.json>
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

SCHEMA_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs/autoresearch-packet/v0.1/schema.json"
)


class ValidationError(Exception):
    """Raised when a packet does not match the v0.1 schema."""


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
        or (expected == "boolean" and isinstance(value, bool))
        or (expected == "number" and isinstance(value, (int, float)) and not isinstance(value, bool))
    )


def validate_schema(
    schema: dict[str, Any], value: Any, root: dict[str, Any], path: str = "$"
) -> None:
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
        elif expected_type == "string":
            min_len = schema.get("minLength", 0)
            if len(value) < min_len:
                raise ValidationError(f"{path} must not be empty")
        elif expected_type in ("integer", "number"):
            minimum = schema.get("minimum")
            if minimum is not None and value < minimum:
                raise ValidationError(f"{path} must be >= {minimum}")


def validate_object(
    schema: dict[str, Any], value: dict[str, Any], root: dict[str, Any], path: str
) -> None:
    properties = schema.get("properties", {})
    for key in schema.get("required", []):
        if key not in value:
            raise ValidationError(f"{path} missing required property: {key}")
    if schema.get("additionalProperties") is False:
        extra = sorted(set(value) - set(properties))
        if extra:
            raise ValidationError(
                f"{path} has unexpected properties: {', '.join(extra)}"
            )
    for key, child_schema in properties.items():
        if key in value:
            validate_schema(child_schema, value[key], root, f"{path}.{key}")


def validate_array(
    schema: dict[str, Any], value: list[Any], root: dict[str, Any], path: str
) -> None:
    min_items = schema.get("minItems")
    if min_items is not None and len(value) < min_items:
        raise ValidationError(f"{path} must contain at least {min_items} item(s)")
    # Validate items whenever the "items" key is present, even if schema is {}
    if "items" in schema:
        item_schema = schema["items"]
        for index, item in enumerate(value):
            validate_schema(item_schema, item, root, f"{path}[{index}]")


def validate_measurement_command(packet: dict[str, Any]) -> None:
    """Ensure measurement.command is non-empty (semantic check beyond schema)."""
    cmd = packet.get("measurement", {}).get("command", "")
    if not cmd.strip():
        raise ValidationError(
            "$.measurement.command must be a non-empty string "
            "(the measurement entrypoint is required)"
        )


def validate_budget_conditional(packet: dict[str, Any]) -> None:
    """Enforce if/then conditional constraints on budget.type (schema allOf).

    - time_seconds: requires time_budget_seconds
    - step_count: requires step_budget
    - combined: requires both step_budget and time_budget_seconds
    """
    budget = packet.get("budget", {})
    btype = budget.get("type")
    if btype == "time_seconds" and "time_budget_seconds" not in budget:
        raise ValidationError(
            "$.budget.type='time_seconds' requires time_budget_seconds"
        )
    elif btype == "step_count" and "step_budget" not in budget:
        raise ValidationError(
            "$.budget.type='step_count' requires step_budget"
        )
    elif btype == "combined":
        missing = []
        if "step_budget" not in budget:
            missing.append("step_budget")
        if "time_budget_seconds" not in budget:
            missing.append("time_budget_seconds")
        if missing:
            raise ValidationError(
                "$.budget.type='combined' requires "
                f"{', '.join(missing)}"
            )


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(
            "Usage: python scripts/validate_autoresearch_packet.py <packet.json>",
            file=sys.stderr,
        )
        return 2

    fixture_path = Path(argv[1])
    try:
        schema = load_json(SCHEMA_PATH)
        packet = load_json(fixture_path)
        validate_schema(schema, packet, schema)
        validate_measurement_command(packet)
        validate_budget_conditional(packet)
    except ValidationError as exc:
        print(f"VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1

    print(
        "VALIDATION PASSED: "
        f"{packet['packet_id']} (status={packet['status']}, "
        f"metric={packet['objective']['metric_name']}, "
        f"direction={packet['objective']['metric_direction']})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
