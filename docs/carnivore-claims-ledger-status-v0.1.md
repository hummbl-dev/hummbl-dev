# Carnivore Claims Ledger: Status

**Status**: bootstrapped (repos exist, not yet populated)
**Date**: 2026-07-08
**Issue**: [hummbl-dev/hummbl-dev#52](https://github.com/hummbl-dev/hummbl-dev/issues/52)

## Canonical question

> Which carnivore claims are true, for whom, under what conditions, with what risks, and with what level of evidence?

## Repo state

Three repos exist and are bootstrapped with the structure from issue #52:

| Repo | Visibility | Purpose | Status |
|------|-----------|---------|--------|
| `hummbl-dev/ccl-workbench-private` | PRIVATE | Raw source discovery, transcript processing, extracted claims, unreviewed claims, internal notes, unsafe claim quarantine | Bootstrapped |
| `hummbl-dev/carnivore-claims-ledger` | PRIVATE | Private workbench: detailed analysis, internal reviews, red-team artifacts, protocol drafts | Bootstrapped |
| `hummbl-dev/carnivore-claims` | PUBLIC | Public-facing clean repo: sanitized reviewed claims, public-safe evidence summaries, claim family pages, methodology | Bootstrapped |

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

## Repo distinction clarified

Operator clarified 2026-07-08: keep both with careful distinction.

- `carnivore-claims` (PUBLIC) — public-facing clean repo for sanitized reviewed claims, public-safe evidence summaries, claim family pages, methodology
- `carnivore-claims-ledger` (PRIVATE) — private workbench for detailed analysis, internal reviews, red-team artifacts, protocol drafts
- `ccl-workbench-private` (PRIVATE) — raw source discovery, transcript processing, extracted claims, unreviewed claims, internal notes, unsafe claim quarantine

## Next steps

1. Populate P0 contributor stubs
2. Add issue templates
3. Add initial docs: methodology, risk taxonomy, evidence grading, source quality, protocol admission, public language policy, glossary
4. Add script stubs: validate_schema.py, export_public.py, dedupe_claims.py, check_receipts.py
5. Begin seed ingestion: 10 contributors x 5 sources x 10 claims each

## Non-canon notice

This status doc records the current state of CCL repos. It is not medical advice. The CCL project is not pro-carnivore and not anti-carnivore. It is a claim-first truth-seeking system.
