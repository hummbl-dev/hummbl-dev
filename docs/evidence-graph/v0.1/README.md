# Evidence Graph v0.1

Evidence Graph v0.1 is a minimal representation of a completed cross-repo
evidence batch. It links bibliography, source packets, research grounding,
paper artifacts, receipts, and implementation issues into one auditable
structure.

This is not a claim compiler, dashboard, registry, database, crawler,
release pipeline, public website integration, or generalized ontology. The
v0.1 goal is to validate one known batch before generalizing.

## First fixture

The first fixture is intentionally narrow. It represents only the completed
scientific-grounding batch and its paired next lane:

```text
hummbl-bibliography#75
  to research-source-packets#7
  to hummbl-papers#13
  to hummbl-research#42
  to hummbl-research#44
  to hummbl-papers#15
  to hummbl-dev#104
  to hummbl-dev#105
```

It also records the paired lane:

```text
hummbl-papers#14 pairs_with research-source-packets#8
```

No other HUMMBL repos or claims are scanned.

## Fact posture

`public_source_fact` means the fixture is pointing at a public GitHub PR,
issue, merge state, or receipt that can be independently inspected.

`local_execution_fact` means the fact came from a local command, such as
running `gh pr view` or this validator. Local execution facts should not be
promoted as public claims unless a durable public receipt records them.

`user_reported_fact` captures scope or context supplied by the operator.
`derived_synthesis` marks a bounded inference across source-linked artifacts.

## Files

- `schema.json` defines the minimal Evidence Graph v0.1 document shape.
- `fixtures/valid-cross-repo-batch.json` encodes the exact batch.
- `fixtures/invalid-missing-fact-posture.json` must fail validation.
- `../../../scripts/validate_evidence_graph.py` validates a fixture locally.

## Validate

Run from the repository root:

```bash
python scripts/validate_evidence_graph.py docs/evidence-graph/v0.1/fixtures/valid-cross-repo-batch.json
python scripts/validate_evidence_graph.py docs/evidence-graph/v0.1/fixtures/invalid-missing-fact-posture.json
```

The first command should pass. The second should exit nonzero and report that
the node is missing `fact_posture`.

## Links

- `hummbl-dev#104`: canonical meta-thread for the Evidence Graph v0.1 slice.
- `hummbl-dev#105`: implementation issue for this minimal schema and validator.
- `hummbl-papers#15`: batch receipt anchor for the completed cross-repo batch.
