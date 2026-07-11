# Migration Contract Template

Status: `v0.1-draft` — candidate template, not admitted canon.

Parent issue: [#125](https://github.com/hummbl-dev/hummbl-dev/issues/125)
Part of: [Migration Assurance Protocol](README.md)

---

## How to use this template

Copy this file into your migration working directory. Fill in every section before any agent writes code. Sections marked **[REQUIRED]** must be completed. Sections marked **[OPTIONAL]** may be omitted with an explicit "N/A — reason" note.

This contract is the shared reference that keeps parallel agent instances coherent. Without it, each agent makes independent assumptions about what must stay identical and what may change.

---

## 1. Source system / target system [REQUIRED]

| Field | Value |
|---|---|
| Source language | |
| Target language | |
| Source codebase size (approx lines) | |
| Target codebase structure (new/existing) | |
| Source repo / path | |
| Target repo / path | |

## 2. Why migration is being considered [REQUIRED]

State the motivating problem in 2-3 sentences. Do not justify the choice of target language here — state the problem the migration is meant to solve.

> Example: "The source codebase has a class of memory-safety bugs (use-after-free, double-free) that are endemic to the source language's manual memory management interacting with a garbage-collected runtime. The target language's ownership model makes these bug classes compiler errors."

## 3. Behavior invariants [REQUIRED]

List everything that must stay behaviorally identical between source and target. These are the contract the test suite validates.

- [ ] Public API surface unchanged
- [ ] CLI commands and flags unchanged
- [ ] Output format (stdout/stderr/exit codes) unchanged
- [ ] Error messages: byte-for-byte identical, OR explicitly documented exceptions approved by a human (list each exception below)
- [ ] Performance: no regression beyond `TBD%` on benchmark `TBD`
- [ ] File formats: read/write compatibility maintained
- [ ] Protocol compatibility (HTTP, WebSocket, etc.): unchanged
- [ ] Other: ___

## 4. Non-goals [REQUIRED]

Explicitly state what this migration will NOT do. This prevents scope creep.

- [ ] No new features
- [ ] No API additions
- [ ] No performance optimization beyond parity
- [ ] No dependency upgrades
- [ ] No naming/idiom changes beyond mechanical translation
- [ ] Other: ___

## 5. Allowed mechanical transformations [REQUIRED]

List the transformations agents may perform without additional review:

- [ ] Language syntax translation (e.g., `defer` → `Drop`)
- [ ] Type annotation addition required by target language
- [ ] Import/module system adaptation
- [ ] Memory management idiom translation (e.g., manual free → RAII)
- [ ] Error handling idiom translation (e.g., error codes → `Result`)
- [ ] Other: ___

## 6. Disallowed transformations [REQUIRED]

List transformations that require explicit human approval. Any transformation not listed in §5 (allowed) is disallowed by default and must be added here with human approval before execution.

- [ ] Changing function signatures (parameter order, arity)
- [ ] Splitting or merging modules/files
- [ ] Renaming public symbols
- [ ] Changing control flow (loops → iterators, callbacks → async)
- [ ] Introducing new abstractions not present in source
- [ ] Removing code the agent "believes is dead" without verification
- [ ] Adding comments that explain or justify a workaround (flag for review — workarounds indicate the migration is not mechanical)
- [ ] Other: ___

## 7. Compatibility expectations [REQUIRED]

| Expectation | Requirement |
|---|---|
| Binary/API compatibility | |
| File format compatibility | |
| Network protocol compatibility | |
| Configuration compatibility | |
| Plugin/extension compatibility | |

## 8. Performance-sensitive areas [OPTIONAL]

List areas where the migration must be especially careful about performance. Agents should not change the algorithm or data structure in these areas.

| Area | File(s) | Concern | Constraint |
|---|---|---|---|

## 9. Security/safety-sensitive areas [REQUIRED]

List areas where incorrect migration could create security vulnerabilities.

| Area | File(s) | Risk | Constraint |
|---|---|---|---|

## 10. Human-owned decisions [REQUIRED]

List decisions that must be made by a human, not an agent:

- [ ] Whether to merge the migration
- [ ] Whether to release the migration
- [ ] Whether to change public API
- [ ] Whether to introduce new dependencies
- [ ] Whether to change build system
- [ ] Other: ___

## 11. Test/evidence contract [REQUIRED]

The primary test suite must be independent of source/target language to validate behavioral equivalence. Supplemental source-native or target-native tests may be added to cover language-specific behavior, but cannot replace the independent suite as the migration gate.

| Field | Value |
|---|---|
| Test suite location | |
| Test suite language (must be independent of source/target) | |
| Supplemental source-native tests (if any) | |
| Supplemental target-native tests (if any) | |
| Test runner command | |
| Exact test outcomes before migration (pass count / fail count / skip count) | |
| Exact test outcomes after migration (must match before counts) | |
| Platforms to validate | |
| Coverage requirement | |
| Fuzzing requirement (if any) | |

## 12. Rollback / abort criteria [REQUIRED]

Define when to abort the migration rather than continue:

- [ ] Abort if test pass rate drops below `TBD%` after `TBD` rounds
- [ ] Abort if more than `TBD` regressions are introduced
- [ ] Abort if migration exceeds `TBD` days of wall-clock time
- [ ] Abort if cost exceeds `$TBD`
- [ ] Abort if a security vulnerability is introduced that cannot be fixed within `TBD` hours
- [ ] Other: ___

Rollback procedure:

> Describe the steps to revert to the pre-migration state. Include branch name, tag, and any state that must be restored.

## 13. Receipt requirements [REQUIRED]

Every PR in the migration must include:

- [ ] Link to this contract
- [ ] List of files changed
- [ ] Test results (pass/fail counts, platform)
- [ ] Adversarial review results (reviewer context, findings, fixes applied)
- [ ] Any deviations from the contract (with justification)
- [ ] Process patches (if the workflow prompt was modified)

## 14. Source/evidence posture [REQUIRED]

| Field | Value |
|---|---|
| Is this migration based on a published case study? | yes / no |
| If yes, source URL | |
| Source posture (self-report / independent / verified) | |
| Are performance/cost figures independently verified? | yes / no |
| Is the target language choice evidence-based or preference-based? | |

---

## Guard against feature expansion

**Hard rule:** No new features, no API additions, no behavioral changes beyond mechanical translation. If an agent proposes a "small improvement" during the migration, it must be filed as a separate issue, not included in the migration PR.

If you need a paragraph-long comment to justify why a workaround is OK, the code is wrong — fix the code.
