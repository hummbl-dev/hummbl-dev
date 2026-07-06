# Ecosystem Audit — 2026-07-06

**Status**: candidate (not canon)
**Date**: 2026-07-06
**Issue**: [hummbl-dev/hummbl-dev#103](https://github.com/hummbl-dev/hummbl-dev/issues/103)
**Method**: `gh repo list hummbl-dev --limit 200` against live org state.

## Summary

Most items from #103 have already been resolved. Of 20 repos flagged in the original issue, 14 no longer exist (deleted or never created), 1 is archived, and 5 exist as active repos (some under different names than flagged).

**No destructive actions taken.** This is a read-only audit with recommendations.

---

## Duplicates to clarify

| Flagged pair | Current state | Recommendation |
|-------------|---------------|----------------|
| arbiter-new vs arbiter | `arbiter-new` does not exist. `arbiter` exists (active, PUBLIC, updated 2026-07-04). | **Resolved.** No action. |
| hummbl-bus-continue vs hummbl-bus | `hummbl-bus-continue` does not exist. `hummbl-bus` exists (active, PRIVATE, updated 2026-07-03). | **Resolved.** No action. |
| founder-mode-mdo-tuple vs founder-mode | `founder-mode-mdo-tuple` does not exist. `founder-mode` exists (active, PRIVATE, updated 2026-07-05). | **Resolved.** No action. |
| Whether vs whether-book | `Whether` does not exist. `whether-book` exists (active, PUBLIC, updated 2026-06-25). | **Resolved.** No action. |

**Verdict**: All duplicate pairs show only one repo present in the live snapshot. The `-new`, `-continue`, `-mdo-tuple`, and bare `Whether` repos are not present in the current org state; whether they were deleted, never created, or renamed cannot be determined from a snapshot alone.

---

## Empty repos to delete or document

| Repo | Current state | Recommendation |
|------|---------------|----------------|
| hummbl-prompt-engineering | Does not exist. | **Resolved.** Not present in live snapshot. |
| hummbl-engineering | Does not exist. | **Resolved.** Not present in live snapshot. |

**Verdict**: Both empty repos are not present in the live snapshot. Whether they were deleted or never created cannot be determined from a snapshot alone.

---

## Stale repos to review

| Flagged repo | Current state | Recommendation |
|-------------|---------------|----------------|
| hummbl-fractional-bench | Does not exist. `fractional-bench` exists (active, PRIVATE, updated 2026-06-25, has description). | **Resolved (renamed).** `fractional-bench` is the canonical name. Active — keep. |
| hummbl-iac | Exists (active, PRIVATE, updated 2026-06-25, has description: "Infrastructure-as-Code for the HUMMBL dev fleet"). | **Not stale.** Active with description. Keep. |
| hummbl-kernel-forge | Does not exist. `hummbl-kernel-factory` exists (active, PRIVATE, updated 2026-06-25, has description: "Meta-kernel factory"). | **Resolved (renamed).** `hummbl-kernel-factory` is the canonical name. Active — keep. |
| hummbl-rubric-templates | Does not exist. | **Resolved.** Not present in live snapshot. |

**Verdict**: All stale repos are either not present in the live snapshot or exist under a different name. No stale repos remain under the flagged names.

---

## Missing READMEs

| Repo | Current state | Recommendation |
|------|---------------|----------------|
| governed-counterpart | Does not exist. | **Resolved.** Not present in live snapshot. |
| ops-secrets | Does not exist. | **Resolved.** Not present in live snapshot. |
| data | Does not exist. | **Resolved.** Not present in live snapshot. |
| industry-watch | Does not exist. | **Resolved.** Not present in live snapshot. |
| reubenbowlby-site | Does not exist. | **Resolved.** Not present in live snapshot. |

**Verdict**: All repos flagged for missing READMEs are not present in the live snapshot. No action needed.

---

## Missing repo

| Repo | Current state | Recommendation |
|------|---------------|----------------|
| NATURALIS-FUTURA | Exists but **archived** (archived=true, PUBLIC, updated 2026-06-22, description: "latent encyclopedia"). | **Found.** Already archived. No action needed. |

**Verdict**: NATURALIS-FUTURA was not missing — it was archived. It appears in the org repo list with `archived=true` status.

---

## Additional findings

### Archived external forks

The org has ~30 archived repos, most of which are forks of external projects (vllm, rich, paramiko, markitdown, httpie-cli, etc.). These are archived and do not need action. They are retained for reference.

### Active repo count

As of 2026-07-06, the `hummbl-dev` org has approximately 120 repos:
- ~90 active (not archived)
- ~30 archived

### `-as-code` repo family

The org has a family of 10 `-as-code` repos (governance-as-code, protocol-as-code, observability-as-code, agent-as-code, model-routing-as-code, policy-as-code, infrastructure-as-code, knowledge-as-code, compliance-as-code, security-as-code). All are active and have descriptions. No duplicates or staleness detected.

---

## Recommendations

1. **No destructive actions needed.** All flagged items are either resolved, renamed, or archived.
2. **Close #103.** The audit is complete; no remaining action items.
3. **Periodic re-audit.** Recommend re-running this audit quarterly to catch new duplicates or stale repos.

## Non-canon notice

This audit is a point-in-time snapshot (2026-07-06). Repo states will change. All findings are based on `gh repo list` output and are classified as local execution facts.
