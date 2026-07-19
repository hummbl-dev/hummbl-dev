# Permanent Issues — Do Not Close

These issues are **permanent**. They must remain open indefinitely as standing
program indexes and portfolio ledgers. No agent may close, auto-resolve, or
mark any of these issues as done unless the operator (Reuben) closes them
personally with explicit written intent.

If an agent believes one of these issues should be closed, it must **stop and
ask the operator** rather than closing it. Silently closing a permanent issue
is a guardrail violation.

## Criteria for inclusion

An issue belongs on this list if its body explicitly declares it as:
- "APPROVED STANDING PORTFOLIO LEDGER... Keep this issue open", or
- a "durable navigation surface" with no close condition, or
- otherwise has no close condition and serves as a durable program index.

## Permanent issue registry

All permanent issues in this repository:

| # | Title | Body signal |
|---|---|---|
| [#153](https://github.com/hummbl-dev/hummbl-dev/issues/153) | HUMMBL Research Integrity, LLL, and Constitutional Systems — master program index | "ACTIVE CROSS-REPO PROGRAM INDEX — COORDINATION ONLY"; durable navigation surface, no close condition in body |
| [#194](https://github.com/hummbl-dev/hummbl-dev/issues/194) | Public Repository Cross-Repo Contract Coverage Ledger v0.1 | "APPROVED STANDING PORTFOLIO LEDGER... Keep this issue open as the portfolio index" |

## Maintenance

- **Adding an issue:** the operator confirms in writing that an issue is
  permanent. A PR should update this file in the same change set.
- **Removing an issue:** only the operator may remove an issue from this list,
  by closing the issue personally and updating this file in the same commit.
- **Audit:** agents performing issue triage, inbox-zero, or stale-issue scans
  must skip every issue listed here and report the skip in their receipt.
