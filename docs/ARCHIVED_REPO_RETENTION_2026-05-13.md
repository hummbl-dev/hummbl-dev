# Archived Repository Retention Tracker

Date: 2026-05-13

This tracker records archived repositories that were intentionally skipped by the
2026-05-13 untouched-repo issue pass. It does not unarchive or edit archived
repositories.

## Retention Queue

| Repository | Archived | Last updated | Current signal | Required decision |
|---|---:|---|---|---|
| `hummbl-dev/hummbl-asi` | yes | 2025-12-06 | Description: "HUMMBL Artificial Super Intelligence Framework" | Confirm whether this is historical research, superseded by another HUMMBL repo, or should be revived with a concrete owner. |
| `hummbl-dev/hummbl-assurance` | yes | 2026-04-18 | Description says EAL merged into `hummbl-governance` PR #12; vendor scorecards retained for reference. | Keep archived if `hummbl-governance` is confirmed source of truth; add archive note only after retention decision. |

## Operating Rules

- Do not unarchive either repository without an explicit revival decision.
- Do not edit archived repositories from this tracking pass.
- If retained, add archive notes in the archived repo or successor repo only
  after the retention rationale is approved.
- If revived, open a revival plan before changing archive state.

## Recommended Next Step

Prioritize `hummbl-assurance` first because its description already names a
successor source of truth. `hummbl-asi` needs a human/product decision before
any source-of-truth statement is safe.
