# Creation Packet: source-candidate-registry

## Status

Candidate. Public seed. Not yet authorized for creation.

## Namespace Receipt

Checked on 2026-07-04:

- `hummbl-dev/source-candidate-registry`: available under `hummbl-dev`.
- No exact public search result found in the bounded check.

Risk: medium. The name should not imply that listed sources are accepted,
validated, or canonical.

## Scope

Source candidates before promotion:

- source identity,
- provenance,
- retrieval date,
- license or terms notes,
- freshness,
- claim relation,
- admissibility status,
- promotion/deprecation receipts.

## Non-Scope

- Not a bibliography of approved sources.
- Not a canon source registry.
- Not a scraper warehouse.
- Not a place for private, paid, or copyrighted full-text dumps.

## Public Boundary

Public source metadata only. No paid content, private reports, long copyrighted
excerpts, credentials, or private research notes.

## Initial Scaffold

```text
README.md
CONTRIBUTING.md
SECURITY.md
LICENSE
hummbl.repo.yaml
docs/status.md
docs/receipts/
schemas/
examples/
fixtures/valid/
fixtures/invalid/
sources/
.github/ISSUE_TEMPLATE/
.github/pull_request_template.md
```

## Seed Issues

1. Define source-candidate status ladder and public/private boundary.
2. Add v0.1 source-candidate schema and fixtures.
3. Add promotion receipt from candidate source to accepted/canon-bearing source.
