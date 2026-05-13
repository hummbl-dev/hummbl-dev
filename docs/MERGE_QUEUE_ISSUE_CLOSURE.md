# Merge Queue Issue-Closure Semantics

## Purpose

Prevent completed work from leaving accepted issues open because a PR used
non-closing language such as "Addresses #123" when the PR actually satisfied
the issue.

## Required Merge Check

Before merging a PR that references an issue, classify the reference:

| Reference | Meaning | Merge action |
|---|---|---|
| `Closes #N`, `Fixes #N`, `Resolves #N` | PR fully satisfies the issue acceptance criteria. | Merge normally; confirm the issue closes after merge. |
| `Addresses #N` | PR materially advances the issue but may not complete all acceptance criteria. | Merge only if the issue should remain open or update the PR/body before merge. |
| `Refs #N`, `Related #N` | Context only. | Do not expect issue closure. |

## Reviewer Checklist

- Identify every issue reference in the PR title, body, and final merge message.
- Compare the PR diff against the issue acceptance criteria.
- If the PR fully satisfies the issue, require closing language before merge.
- If the PR is partial, keep `Addresses`/`Refs` and leave a comment naming the
  remaining acceptance criteria.
- After merge, verify that the expected issue state matches the reference type.

## Examples From 2026-05-13 Sweep

- `crab#7` completed `crab#5` but needed manual closure because the PR used
  non-closing language.
- `autoresearch-reports#4` completed `autoresearch-reports#1` but needed manual
  closure after merge.
- `claude-config#3` intentionally did not close `claude-config#1` because the
  legacy skill-frontmatter migration remained open and was tracked separately.

## Default Rule

If the merge captain is unsure whether a PR completes the issue, keep the issue
open and add a comment that names the unresolved criteria. Do not silently rely
on "Addresses" to mean "done."
