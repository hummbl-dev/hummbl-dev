# Creation Packet: agent-receipts

## Status

Candidate. Public seed. Not yet authorized for creation.

## Namespace Receipt

Checked on 2026-07-04:

- `hummbl-dev/agent-receipts`: available under `hummbl-dev`.
- Public exact-name collisions exist outside the org, including
  `realalonw/agent-receipts` and other low-star repositories returned by GitHub
  search.

Risk: medium. The name is semantically useful but not unique. Use only if HUMMBL
scope/non-scope is explicit at creation.

## Scope

Portable receipts for agent work:

- work receipt,
- claim receipt,
- diff receipt,
- test receipt,
- review receipt,
- provenance receipt,
- promotion receipt.

## Non-Scope

- Not an external standard.
- Not a universal protocol.
- Not a runtime agent framework.
- Not a replacement for repo-specific audit logs.

## Public Boundary

Public-safe examples and schemas only. No private repo names, private customer
data, raw agent transcripts, credentials, or sensitive operational logs.

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

1. Define receipt object model, scope, non-scope, and public/private boundary.
2. Add first receipt schema and valid/invalid fixtures.
3. Run namespace/collision/public-claim audit before promotion.
