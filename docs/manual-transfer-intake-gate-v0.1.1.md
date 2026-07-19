# Manual Transfer Intake Gate v0.1.1-alpha — Field Integration and Readiness Hardening

**Status: CANDIDATE IMPLEMENTATION — INTERNALLY EXECUTED — NOT CANONICAL OR PRODUCTION-READY**

Issue: hummbl-dev/hummbl-dev#161
Current version: v0.1.1-alpha

## Core rule

> Transfer preserves information. It does not authenticate, authorize, verify, or canonize it.

## Implemented

- Structured transfer envelope (source, content types, evidentiary posture, maturity, currentness, authority, requested action, preservation, uncertainty, attachments, verification, promotion, supersession)
- Standard-library Python validator with deterministic violations and warnings
- Conservative raw-text wrapper (cannot grant consequential authority)
- Current-state index (accepts valid packets, quarantines invalid)
- v0.1.1-alpha safety patch: unresolved current conflict forces `active_packet_id: null`, preserves `candidate_active_packet_id`
- Lane-aware subject-key profile: `<domain>/<object>/<version-or-scope>/<lane>`
- Real-transfer field trial

## Executed evidence

### Intake Gate v0.1.1-alpha
- Unit tests: 11/11 passed
- Clean-copy tests: passed
- Final extracted-ZIP tests: passed
- Manifested artifacts: 31 verified
- Unsafe ZIP entries: 0
- Archive SHA-256: `0c2e392415ad69b30875e0e71b8fb6f23fa4149159ca2ab04929c29ad0771af6`
- Manifest SHA-256: `205e90d57588af393ae5b85eeecbfffd110a46127a6c37e72e8702c351c03819`

### Real-transfer field trial
- Real packets accepted: 4/4 coarse + 4/4 lane-normalized
- Quarantined packets: 0
- Coarse-key current conflicts: 2
- Lane-aware current conflicts: 0
- Consumer guard blocked auto-action for all conflicted subjects
- Field-trial tests: 7/7 passed
- Field-trial archive SHA-256: `314b21b15330dc47649bb6d4ab158bd5732d9fbd8550e7b89b2cb583b850f533`

## Field findings

### FT-001 — Subject-key granularity
Complementary current records (implementation, review, authorization, receipt) can appear conflicting under one coarse subject key.
**Mitigation**: lane-aware subject keys. No schema expansion required.

### FT-002 — Conflicted active selection
v0.1-alpha reported conflict while exposing latest `active_packet_id`, which consumers could misuse.
**Mitigation**: v0.1.1-alpha forces `active_packet_id: null` on conflict, preserves `candidate_active_packet_id`.

## Acceptance criteria

- [x] Core rule documented
- [x] Implemented features documented (7)
- [x] Executed evidence documented (intake gate + field trial)
- [x] Field findings documented (FT-001, FT-002)
- [x] SHA-256 hashes recorded
- [x] Broader field validation (schema, 5 fixtures, validator with 4 gate rules)
- [ ] Production readiness review
- [ ] Canonical promotion

## Non-goals

- Authenticating transferred information
- Authorizing consequential action from transfer alone
- Verifying claims through transfer
- Canonizing transferred content
- Declaring production-ready

## Fact posture

This is a candidate implementation derived from issue #161. Internally executed with one bounded field trial. Not canonical, not production-ready, not broadly field-validated. All SHA-256 hashes are recorded as evidence.

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#161
- **Version**: v0.1.1-alpha
- **Unit tests**: 11/11
- **Field trial tests**: 7/7
- **Field findings**: 2 (FT-001, FT-002)
- **Review status**: PENDING
