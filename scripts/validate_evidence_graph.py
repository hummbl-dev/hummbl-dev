#!/usr/bin/env python3
"""Validate an Evidence Graph v0.1 JSON fixture."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "docs/evidence-graph/v0.1/schema.json"


class ValidationError(Exception):
    """Raised when a fixture does not match the v0.1 schema."""


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


def validate_edge_endpoints(graph: dict[str, Any]) -> None:
    node_ids = [node["id"] for node in graph["nodes"]]
    duplicates = sorted({node_id for node_id in node_ids if node_ids.count(node_id) > 1})
    if duplicates:
        raise ValidationError(f"duplicate node id(s): {', '.join(duplicates)}")

    known = set(node_ids)
    for index, edge in enumerate(graph["edges"]):
        for endpoint in ("from", "to"):
            node_id = edge[endpoint]
            if node_id not in known:
                raise ValidationError(f"$.edges[{index}].{endpoint} references unknown node id: {node_id}")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python scripts/validate_evidence_graph.py <graph.json>", file=sys.stderr)
        return 2

    fixture_path = Path(argv[1])
    try:
        schema = load_json(SCHEMA_PATH)
        graph = load_json(fixture_path)
        validate_schema(schema, graph, schema)
        validate_edge_endpoints(graph)
    except ValidationError as exc:
        print(f"VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1

    print(
        "VALIDATION PASSED: "
        f"{graph['graph_id']} ({len(graph['nodes'])} nodes, {len(graph['edges'])} edges, "
        f"{len(graph['receipts'])} receipts)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
