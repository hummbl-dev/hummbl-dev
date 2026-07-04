# Creation Packet: claim-as-code

## Status

Candidate. Public seed. Not yet authorized for creation.

## Namespace Receipt

Checked on 2026-07-04:

- `hummbl-dev/claim-as-code`: available under `hummbl-dev`.
- No exact public search result found in the bounded check.

Risk: medium because the repo name could imply truth authority. README must
state that it models claims and evidence state; it does not canonize claims.

## Scope

Machine-checkable claims:

- claim text,
- source/provenance,
- evidence state,
- confidence or maturity,
- public-surface status,
- deprecation and contradiction markers.

## Non-Scope

- Not a truth oracle.
- Not medical, legal, or financial authority.
- Not a source-ingestion warehouse.
- Not a public claim publisher without review gates.

## Public Boundary

Public-safe schemas, examples, and fixtures. No private claims, customer
material, unreleased strategy, or sensitive protocol content.

## Initial Scaffold

```text
README.md
CONTRIBUTING.md
SECURITY.md
LICENSE
hummbl.repo.yaml
docs/status.md
docs/receipts/
docs/adr/
schemas/
examples/
fixtures/valid/
fixtures/invalid/
.github/ISSUE_TEMPLATE/
.github/pull_request_template.md
```

## Seed Issues

1. Define claim-as-code scope, non-scope, and public/private boundary.
2. Add v0.1 claim schema with valid/invalid fixtures.
3. Add overclaim and canon-contamination review checklist.
