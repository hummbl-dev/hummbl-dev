# Ownership & Lifetime Ledger Template

Status: `v0.1-draft` — candidate template, not admitted canon.

Parent issue: [#125](https://github.com/hummbl-dev/hummbl-dev/issues/125)
Part of: [Migration Assurance Protocol](README.md)
Companion to: [Migration Contract Template](MIGRATION_CONTRACT_TEMPLATE.md)

---

## How to use this template

Before any agent writes migration code, fill out a ledger entry for every component where resource ownership, cleanup, references, handles, state lifetimes, async callbacks, or external resources could become correctness hazards.

The ledger makes ownership assumptions explicit before code generation. Adversarial reviewers use it to challenge those assumptions. Without it, each agent instance silently assumes its own ownership model.

Two formats are provided:

- **Markdown table** (below) — for human-readable review and inline discussion
- **TSV** (`OWNERSHIP_LIFETIME_LEDGER_TEMPLATE.tsv`) — for machine-readable consumption by agent workflows

Fill in both if your workflow uses automated tooling. Use the Markdown format alone for smaller migrations.

---

## Ledger fields

| Field | Description |
|---|---|
| **component** | File, module, or symbol being tracked |
| **resource** | The resource or state being owned (memory, file handle, socket, lock, callback, etc.) |
| **current_owner** | Who/what currently owns the resource lifecycle in the source system |
| **borrower** | Who/what borrows, consumes, or references the resource (including async continuations and callbacks) |
| **cleanup** | How and when the resource is cleaned up in the source system |
| **escape_risk** | Can the resource escape its intended scope? (callback capture, async continuation, global registry, etc.) |
| **concurrency_risk** | Is the resource accessed concurrently? (threads, event loop reentrance, GC marker thread, etc.) |
| **target_representation** | How the resource will be represented in the target system (ownership type, lifetime annotation, guard object, etc.) |
| **reviewer_notes** | Adversarial reviewer's challenge or confirmation |
| **evidence** | Test or assertion that validates the ownership/cleanup behavior |
| **status** | `unreviewed` / `reviewed` / `blocked` / `superseded` |

---

## Example ledger (Markdown)

> This example is illustrative only. It uses generic names, not any specific codebase.

| component | resource | current_owner | borrower | cleanup | escape_risk | concurrency_risk | target_representation | reviewer_notes | evidence | status |
|---|---|---|---|---|---|---|---|---|---|---|
| `net/socket.c` | TCP socket handle | Socket object | Event loop, close callback | `defer socket.close()` at call site | High: close callback fires after object may be freed | Medium: event loop reentrance during close | `Owned<Socket>` with `Drop` | "Drop runs automatically — but verify async close callback doesn't outlive the owner" | `test/socket_close_test.ts` | unreviewed |
| `runtime/buffer.c` | ArrayBuffer reference | Buffer wrapper | JS GC, valueOf callback | Manual unpin before GC | High: valueOf can detach mid-operation | Low (single-threaded) | `PinnedBuffer` with `Drop` unpin | "Check: does Drop unpin happen before or after the last JS callback?" | `test/buffer_detach_test.ts` | unreviewed |
| `http/parser.c` | Parser state arena | Arena allocator | All parser functions in scope | Arena freed at function exit | Low: arena doesn't escape function | Low | `Arena` with scoped lifetime | "Confirmed: arena is function-local, no escape paths" | `test/parser_stress_test.ts` | reviewed |

---

## Review protocol

1. **Before code generation**: Fill in the ledger for every risky component. Mark all entries `unreviewed`.
2. **Adversarial review**: A reviewer in a separate context window (see [Split-Context Adversarial Review Protocol](#), issue #129) challenges each entry:
   - Is the `current_owner` correct?
   - Are all `borrower` paths accounted for, including async/callback paths?
   - Is the `escape_risk` assessment accurate?
   - Is the `concurrency_risk` assessment accurate?
   - Does the `target_representation` actually solve the identified risk?
3. **After review**: Update `reviewer_notes` and `status` for each entry.
4. **Blocked entries**: Entries marked `blocked` must be resolved before the corresponding code is migrated. Do not migrate a blocked component.
5. **Superseded entries**: If a component is removed or restructured during migration, mark `superseded` with a note pointing to the replacement.

---

## Linking

- This ledger must link to the [Migration Contract](MIGRATION_CONTRACT_TEMPLATE.md) for the same migration.
- The Migration Contract's "Behavior invariants" section should reference ledger entries that validate those invariants.
- The Split-Context Adversarial Review Protocol (#129) should reference this ledger as input for the reviewer.
