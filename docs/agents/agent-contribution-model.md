# Agent Contribution Model

## Principle

Agents may assist with work, but humans remain accountable for authority-bearing decisions.

## Work lifecycle

1. Human intent
2. Issue or handoff
3. Agent execution
4. Receipt preservation
5. PR or proposed patch
6. Review
7. Merge or release
8. Canon/state update only when approved

## Required receipts

- Source links for claims and assertions
- Commands run
- Files changed
- Tests run
- Known limitations
- Open questions
- Authority boundary

## Prohibited behavior

- Silent canon changes
- Unreviewed release claims
- Invented file/repo state
- Direct `main` mutation without permission
- Treating generated output as verified fact

## Review gates

- Correctness
- Security
- Provenance
- Reversibility
- Public/private boundary
- Release impact

## Memory and canon discipline

- Ideas are not doctrine.
- Candidates are not approved truth.
- Sources are evidence, not conclusions.
- Canon exists only after authority review and merge/release approval.

## Fast-path for first contribution

1. Claim one issue, then open a PR with the smallest valid edit.
2. Link the issue and include the expected packet shape in the PR body.
3. Attach receipts for commands, checks, and scope assumptions.
4. Mark status as `seed` or `v0.1-draft` until adoption is explicit.
