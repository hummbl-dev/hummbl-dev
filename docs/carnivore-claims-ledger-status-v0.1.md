# Carnivore Claims Ledger: Status

**Status**: bootstrapped (repos exist, not yet populated)
**Date**: 2026-07-08
**Issue**: [hummbl-dev/hummbl-dev#52](https://github.com/hummbl-dev/hummbl-dev/issues/52)

## Canonical question

> Which carnivore claims are true, for whom, under what conditions, with what risks, and with what level of evidence?

## Repo state

Three repos already exist and are bootstrapped with the structure from issue #52:

| Repo | Visibility | Purpose | Status |
|------|-----------|---------|--------|
| `hummbl-dev/ccl-workbench-private` | PRIVATE | Raw source discovery, transcript processing, extracted claims, unreviewed claims, internal notes, unsafe claim quarantine | Bootstrapped |
| `hummbl-dev/carnivore-claims-ledger` | PRIVATE | Public-bound clean repo: sanitized reviewed claims, public-safe evidence summaries, claim family pages, methodology | Bootstrapped |
| `hummbl-dev/carnivore-claims` | PRIVATE | Appears to be a third repo (possibly a duplicate or earlier name) | Bootstrapped |

All three repos contain: README, CANONICAL_QUESTION, GOVERNANCE, SAFETY, schema/, data/, claim_families/, contributors/, reviews/, docs/, scripts/, tests/.

## What's done

- [x] Create `ccl-workbench-private` repo
- [x] Create `carnivore-claims-ledger` repo
- [x] Add README, CANONICAL_QUESTION, GOVERNANCE, SAFETY, RELEASE_CRITERIA to workbench
- [x] Add README, CANONICAL_QUESTION, METHODOLOGY, SAFETY, GOVERNANCE, LIMITATIONS to public-bound repo
- [x] Add schema directory
- [x] Add data directory with empty CSVs
- [x] Add claim_families directory
- [x] Add contributors directory
- [x] Add reviews directory
- [x] Add docs directory
- [x] Add scripts directory

## What's not done

- [ ] Populate contributor stubs for P0 source nodes (Bart Kay, Shawn Baker, etc.)
- [ ] Populate claim-family template pages
- [ ] Add issue templates for source ingestion, claim extraction, evidence review
- [ ] Add initial docs: methodology, risk taxonomy, evidence grading, source quality, protocol admission, public language policy, glossary
- [ ] Add script stubs: validate_schema.py, export_public.py, dedupe_claims.py, check_receipts.py
- [ ] Begin manual seed ingestion: 10 contributors x 5 sources x 10 claims each
- [ ] Clarify relationship between `carnivore-claims` and `carnivore-claims-ledger` (possible duplicate)

## Possible duplicate

Three repos exist where the issue specifies two. `carnivore-claims` may be an earlier name or duplicate of `carnivore-claims-ledger`. Operator should clarify whether to:
1. Archive `carnivore-claims` and use `carnivore-claims-ledger` as the public-bound repo
2. Merge `carnivore-claims` into `carnivore-claims-ledger`
3. Keep all three with distinct purposes

## Next steps

1. Operator clarifies `carnivore-claims` vs `carnivore-claims-ledger`
2. Populate P0 contributor stubs
3. Add issue templates
4. Begin seed ingestion

## Non-canon notice

This status doc records the current state of CCL repos. It is not medical advice. The CCL project is not pro-carnivore and not anti-carnivore. It is a claim-first truth-seeking system.
