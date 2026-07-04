# `*-as-code` PR Checklist (v0.1)

Use this before submitting PRs in the `*-as-code` repos.

- [ ] PR body links the issue spine and required shared issue/PR chain.
- [ ] Directory contract is present: `docs/`, `schemas/`, `examples/`, `fixtures/valid/`, `fixtures/invalid/`, `receipts/`.
- [ ] Status uses one of: `seed`, `v0.1-draft`, `validated-example`, `v0.1-packet`.
- [ ] Boundary document exists and includes explicit non-canon statement.
- [ ] At least one schema artifact is added.
- [ ] At least one valid example and one invalid fixture are added.
- [ ] Required receipt artifacts are present and explicit.
- [ ] Adjacent repo links are explicit when boundaries are crossed.

## PR close condition

- Do not merge as canonical before explicit review/approval.
- Treat all `seed`/draft state as public non-canon until adopted.
