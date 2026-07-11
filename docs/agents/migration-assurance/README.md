# Migration Assurance Protocol

Status: `v0.1-draft` — candidate protocol packet, not admitted canon.

Parent issue: [#125](https://github.com/hummbl-dev/hummbl-dev/issues/125)

---

## What this packet is for

This packet provides reusable patterns for governing large-scale agentic code migrations — rewrites, ports, or major refactors where an AI agent writes most of the code and a human reviews before merge.

It is grounded in a single public case study ([Bun Rust rewrite](case-studies/bun-rust-rewrite.md)) and extracted into vendor-neutral templates and protocols.

## When to use it

- Rewriting a codebase from one language to another with agent assistance
- Large-scale refactors where parallel agent instances produce code simultaneously
- Migrations where the test suite is language-independent (can validate the target without trusting the agent)
- Any project where the diff is too large for a single human to review line-by-line

## When not to use it

- Small patches or single-file changes — normal PR review suffices
- Migrations where no test suite exists to validate correctness
- Projects where the agent cannot be constrained from mutating git state
- Greenfield projects (no source to port from — different assurance model)

## Source posture note

The Bun Rust rewrite case study is a **first-party public self-report** by Bun's author, who works at Anthropic (which acquired Bun and makes the model used). It is useful case-study material but:

- Not independently verified by HUMMBL
- Not a benchmark for any model's capability
- Not an endorsement of Anthropic, Claude, Bun, Rust, or Zig
- A success story — failed agentic rewrites are not published

See the [source packet](case-studies/bun-rust-rewrite.md) for the full claims table with posture classification.

## Recommended agent workflow

The sequence below is the recommended order of operations for a governed agentic migration:

```
1. Migration Contract (#127)
   ├── Porting guide: source→target pattern mapping
   └── Reviewed adversarially before any code is written

2. Ownership & Lifetime Ledger (#128)
   ├── Trace ownership/lifetime of every struct field
   └── Reviewed adversarially, serialized to a reference file

3. Implementation
   ├── Parallel agent instances write code per the contract
   ├── Each file: 1 implementer + 2 adversarial reviewers + 1 fixer
   └── No git mutation during implementation (commit only)

4. Split-Context Adversarial Review (#129)
   ├── Reviewer gets only the diff, not the implementer's reasoning
   ├── Reviewer is told to assume the code is wrong
   └── Implementer does not review; reviewer does not implement

5. Failure Queue (#130)
   ├── Compiler errors → batched into a work queue, not fixed one-by-one
   ├── Test failures → saved to file, grouped, distributed to agents
   └── CI failures → loop until green, per platform

6. Mutation Discipline (#131)
   ├── No git stash, git reset, or destructive git ops
   ├── Shard agents across separate worktrees
   └── No slow commands inside the workflow loop

7. Process-Patch Log (#132)
   ├── When a class of error recurs, fix the workflow prompt
   └── Log the patch so future migrations learn from it

8. Resource Isolation (#133)
   ├── cgroups / systemd-run for memory and CPU limits
   ├── PID namespace isolation per workflow shard
   └── Monitor disk exhaustion

9. Final Validation
   ├── 100% test suite passing on all platforms
   ├── Manually verify tests are running, not being skipped
   └── Human presses merge
```

## Child docs/templates map

| Issue | Document | Status |
|---|---|---|
| [#126](https://github.com/hummbl-dev/hummbl-dev/issues/126) | [Bun Rust rewrite source packet](case-studies/bun-rust-rewrite.md) | Draft (PR #135) |
| [#127](https://github.com/hummbl-dev/hummbl-dev/issues/127) | Migration Contract template | Pending |
| [#128](https://github.com/hummbl-dev/hummbl-dev/issues/128) | Ownership & lifetime ledger template | Pending |
| [#129](https://github.com/hummbl-dev/hummbl-dev/issues/129) | Split-context adversarial review protocol | Pending |
| [#130](https://github.com/hummbl-dev/hummbl-dev/issues/130) | Failure queue protocol | Pending |
| [#131](https://github.com/hummbl-dev/hummbl-dev/issues/131) | Agent mutation discipline guardrails | Pending |
| [#132](https://github.com/hummbl-dev/hummbl-dev/issues/132) | Process-patch log template | Pending |
| [#133](https://github.com/hummbl-dev/hummbl-dev/issues/133) | Resource isolation boundaries | Pending |

## PR boundary guidance

- **One issue → one PR** unless the PR remains very small and clearly related.
- Each PR should link back to #125 and the specific child issue it addresses.
- Use `Refs #issue` for partial work. Use `Closes #issue` only when all acceptance criteria are met.
- Leave #125 open until all child docs are linked and this README is coherent.

## Review/validation guidance

- Every PR in this packet is docs-only — no code changes, no CI workflow changes, no governance policy changes.
- Review for: claim accuracy, source posture, vendor neutrality, public/private boundary.
- Reject: unsupported performance claims, canon terminology not yet admitted, private repo assumptions.
- Markdown and repo docs checks must pass.

## Claim-safety warnings

- Do not cite Bun's numbers (cost, lines, time, speed) as benchmarks — they are source-reported, not independently verified.
- Do not claim HUMMBL has operationalized these patterns — they are candidate patterns, not admitted canon.
- Do not name Anthropic, Claude, Fable, Bun, Rust, or Zig as architectural dependencies — they are source context only.
- Do not promote these patterns to canon without authority review and merge/release approval.

## Entry point

This README is reachable from `docs/agents/` in the `hummbl-dev/hummbl-dev` repository. The agent contribution model (`docs/agents/agent-contribution-model.md`) governs general agent work; this packet governs migration-specific work.
