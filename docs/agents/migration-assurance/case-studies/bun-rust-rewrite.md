# Bun Rust Rewrite — Source Packet

Parent: [#125 — Bun Rust Rewrite Case Study](https://github.com/hummbl-dev/hummbl-dev/issues/125)
Source: [Rewriting Bun in Rust](https://bun.com/blog/bun-in-rust) — Jarred Sumner, July 8, 2026

Status: `v0.1-draft` — candidate case-study material, not admitted canon.

---

## Source posture

| Field | Value |
|---|---|
| **Source type** | First-party public blog post by Bun (Jarred Sumner) |
| **Evidence posture** | Public-source self-report. Useful case-study material. Not independent benchmark verification. |
| **Disclosure** | Bun was acquired by Anthropic in December 2025. Author used a pre-release version of Claude Fable 5. |
| **Do not claim** | HUMMBL reproduced the migration, verified cost numbers, verified model capability, or audited Bun internals. |
| **Do extract** | Workflow structure, review separation, failure-queue design, mutation guardrails, test-suite behavior contract, and process repair pattern. |

---

## Context

Bun is a JavaScript/TypeScript runtime, bundler, package manager, and test runner originally written in Zig (~535,000 lines). The post describes an 11-day rewrite of the entire codebase from Zig to Rust using ~64 concurrent Claude instances in Claude Code dynamic workflows, resulting in a +1,009,272 line diff across 6,778 commits.

The rewrite was motivated by a class of memory-safety bugs (use-after-free, double-free, memory leaks) that are endemic to manually-managed languages interacting with a garbage-collected runtime (JavaScriptCore). Rust's ownership model and `Drop` trait make these bug classes compiler errors rather than style-guide enforcement problems.

---

## Why this matters for governed agentic work

This post is one of the few public first-party accounts of a large-scale agentic code rewrite. It describes concrete operational patterns — not just "AI wrote code" — for:

1. **Pre-migration documentation** (`PORTING.md`, `LIFETIMES.tsv`) as a shared contract between agent instances.
2. **Split-context adversarial review** — separate implementer and reviewer agents with deliberately different context windows.
3. **Compiler/test failures as work queues** — automated error-to-task pipelines.
4. **Git/worktree mutation discipline** — constraining agent filesystem and git operations.
5. **Resource isolation** for heavy parallel workflows (cgroups, worktree sharding).

These map directly to HUMMBL governance primitives (delegation tokens, circuit breakers, audit logs, identity registry) and to the migration-assurance protocol packet being built in #125–#134.

---

## Claims table with source posture

| Claim | Source posture | Notes |
|---|---|---|
| 535,496 lines of Zig rewritten to Rust | Source-reported | Author states line count; not independently verified. |
| 11 days, 6,778 commits, 64 concurrent Claudes | Source-reported | Author provides commit log visualization; raw data not independently audited. |
| ~$165,000 in API costs (5.9B uncached input tokens, 690M output tokens) | Source-reported | Author's own cost accounting; not independently verified. |
| +1,009,272 line diff landed | Source-reported | Author states final diff size. |
| 128 bugs fixed in v1.4.0 that reproduce in v1.3.14 | Source-reported | Author's bug count; not independently verified. |
| 19 known regressions introduced, all fixed | Source-reported | Author discloses regressions with issue links. |
| 0 tests skipped or deleted | Source-reported | Author states this explicitly; verified manually by author. |
| ~4% of Rust code in `unsafe` blocks (~13,000 keywords) | Source-reported | Author provides current snapshot. |
| 100 billion fuzzer executions, ~15 PRs from fuzzing | Source-reported | Post-merge fuzzing results; ongoing. |
| "Peak 1,300 lines of code per minute" | Source-reported | Includes rewrites; not a sustained rate. |
| Binary size reduced ~20% on Linux & Windows | Source-reported | Author provides before/after table. |
| Memory usage: `Bun.build()` leak fixed (6,745 MB → 609 MB at 2,000 builds) | Source-reported | Author provides measurement table. |
| Would have taken 3 engineers ~1 year by hand | Author's estimate | Speculative; not verifiable. |

---

## Reusable vendor-neutral patterns

These are the workflow patterns extractable from the post, stripped of vendor-specific context. Each is a candidate for a dedicated protocol/template issue (#127–#133).

### 1. Pre-migration contract documents

Before any agent writes code, produce two documents:

- **Porting guide** — maps source-language patterns to target-language patterns. Acts as a shared reference for all agent instances.
- **Lifetime/ownership ledger** — traces the ownership and lifetime of every struct field in the codebase. Reviewed adversarially before code generation begins.

These documents are the contract that keeps parallel agent instances coherent. Without them, each agent makes independent assumptions about idioms and ownership.

### 2. Split-context adversarial review

Separate the implementer and reviewer into different context windows with different instructions:

- **Implementer**: has the original source, the porting guide, and its own reasoning. Goal: produce code.
- **Adversarial reviewer**: has only the diff. Goal: find bugs and reasons the code does not work. Told to assume the code is wrong.

Ratio: 1 implementer, 2+ reviewers. The implementer does not review. The reviewer does not implement. A fixer applies review feedback.

This prevents the "author wants to merge" bias that occurs when the same context both writes and reviews code.

### 3. Failure queues (compiler, test, CI)

Instead of fixing errors one at a time, batch them into a work queue:

1. Run the checker (`cargo check`, test suite, CI).
2. Save all errors to a file, grouped by module/crate/file.
3. Distribute errors across parallel agent instances.
4. Each agent fixes its assigned errors, gets adversarial review, and commits.
5. Re-run the checker. Repeat until green.

This turns a 16,000-error backlog into a parallelizable work queue rather than a sequential debugging session.

### 4. Git/worktree mutation discipline

Agents in parallel workflows can destroy each other's work if they share a working directory. The post describes false starts where agents ran `git stash`, `git reset --hard`, and `git stash pop` in shared state.

Discipline rules extracted:

- No `git stash`, `git reset`, or any git command that doesn't commit a specific file.
- No `cargo` or slow commands inside the workflow loop.
- Shard agents across separate worktrees (4 worktrees, 16 agents each).
- `cargo check` runs only at the start of each crate cycle, not during fixes.

### 5. Resource isolation for heavy parallel workflows

Running 64 concurrent agents with compilation and test suites requires resource isolation:

- Use `systemd-run` (cgroups) to limit memory and CPU per workflow shard.
- Isolate PID namespaces to prevent process interference.
- Shard test files across worktrees by folder to avoid contention.
- Watch for disk exhaustion — the machine crashed several times from disk space.

### 6. Process repair over hand-fixing

When a class of error keeps recurring (e.g., agents stubbing out functions to pass compilation, agents adding long justification comments), fix the workflow prompt rather than hand-fixing each instance.

Example rule added to adversarial reviewers: "If you need a paragraph-long comment to justify why the workaround is OK, the code is wrong — fix the code."

---

## Non-portable / vendor-specific details

These aspects of the post are specific to Bun's context and should not be treated as generalizable patterns:

- **Zig → Rust specifically**: The memory-safety bug class (GC + manual management) is specific to Bun's Zig + JavaScriptCore architecture. Most migrations do not involve this exact language pair.
- **Claude Fable 5 (pre-release)**: The model used was a pre-release Anthropic model. Results are not reproducible with currently available public models and should not be cited as a capability claim for any specific model.
- **535K lines, 64 agents, $165K**: These numbers are specific to Bun's scale and budget. They are not targets or benchmarks.
- **Claude Code dynamic workflows**: The orchestration harness is Anthropic-specific. The patterns (parallelism, review separation, failure queues) are portable; the specific tool is not.
- **JavaScriptCore embedding**: Bun's C++ interop requirements (and the resulting `unsafe` usage) are specific to its architecture.

---

## Risks and unknowns

| Risk | Description |
|---|---|
| **Self-report bias** | The post is written by the person who did the rewrite and who works at the company that makes the model used. Positive framing is expected. |
| **No independent verification** | No third party has verified the commit count, test pass rate, cost figures, or bug counts. |
| **Survivorship bias** | This is a success story. Failed large-scale agentic rewrites are not published. |
| **Pre-release model** | Results depend on a model not publicly available. Cannot be reproduced or benchmarked. |
| **Scale assumption** | Patterns that worked at 64 concurrent agents on EC2 may not translate to smaller-scale agent workflows. |
| **Regression disclosure** | 19 regressions were disclosed, but the post does not claim this is exhaustive. |
| **Ongoing maintenance** | The post describes the merge, not long-term maintenance of LLM-authored code at scale. |

---

## Follow-up child issues / PR pointers

| Issue | Pattern extracted | Status |
|---|---|---|
| [#127](https://github.com/hummbl-dev/hummbl-dev/issues/127) | Migration Contract template (porting guide + lifetime ledger) | Open |
| [#128](https://github.com/hummbl-dev/hummbl-dev/issues/128) | Ownership and lifetime ledger template | Open |
| [#129](https://github.com/hummbl-dev/hummbl-dev/issues/129) | Split-context adversarial review protocol | Open |
| [#130](https://github.com/hummbl-dev/hummbl-dev/issues/130) | Failure queue protocol (compiler/test/CI) | Open |
| [#131](https://github.com/hummbl-dev/hummbl-dev/issues/131) | Agent mutation discipline guardrails | Open |
| [#132](https://github.com/hummbl-dev/hummbl-dev/issues/132) | Process-patch log for workflow failures | Open |
| [#133](https://github.com/hummbl-dev/hummbl-dev/issues/133) | Resource isolation boundaries | Open |
| [#134](https://github.com/hummbl-dev/hummbl-dev/issues/134) | Docs spine README and PR routing map | Open |

---

## Receipt

- Source URL: https://bun.com/blog/bun-in-rust
- Source author: Jarred Sumner (Bun, acquired by Anthropic December 2025)
- Source date: July 8, 2026
- Packet created: 2026-07-09
- Packet author: devin
- Parent issue: #125
- This PR: refs #126
