# ChatGPT Session-Closeout Adapter v0.1

**Status: CANDIDATE — NON-CANON — ADAPTER PROFILE**

Issue: hummbl-dev/hummbl-dev#160
Parent: hummbl-dev/hummbl-dev#159 (Conversation Lifecycle Protocol)
Dependencies (now with reviewable drafts):
- protocol-as-code#7 — Conversation Lifecycle Protocol profile
- agent-handoffs#9 — Conversation/work-session handoff profile (draft PR #10)
- execution-receipts#10 — Conversation closeout receipt profile (draft PR #11)

## Mission

Define a ChatGPT-specific adapter for the provider-neutral closeout protocol. The adapter closes both ordinary chats and connected work sessions using only capabilities actually available in the current ChatGPT session, while preserving honest `UNAVAILABLE` outcomes for local or platform-specific checks it cannot perform.

This adapter does not assume ChatGPT exposes native custom slash commands. Candidate trigger phrases may be represented in instructions, a custom-agent profile, or natural language.

## Adapter modes

| Mode | When to use |
|------|-------------|
| `CHAT_CLOSEOUT` | Analysis, strategy, research, or planning chats without meaningful external mutations |
| `WORK_SESSION_CLOSEOUT` | ChatGPT accessed or mutated connected systems (GitHub, Gmail, Calendar, Drive, Slack, Notion, Teams, Dropbox, other connectors) |
| `SESSION_CHECKPOINT` | Interruption or planned pause without asserting completion |
| `NO_CLOSEOUT_REQUIRED` | Trivial or casual sessions where durable preservation would add noise |

## Candidate natural-language triggers

```text
End this chat cleanly.
Close this work session.
Run the HUMMBL session closeout.
Checkpoint this session.
Close this session with an AAR.
```

Trigger wording is adapter-level and non-canonical. The operator may bind any phrase to the procedure.

## ChatGPT capability mapping

At invocation, map the current tool surface into the protocol capability contract. At minimum distinguish:

| Capability | ChatGPT availability |
|------------|---------------------|
| conversation context | available (in-context window) |
| connected source read/write tools | depends on session connectors |
| specific connector destinations | depends on session connectors |
| artifact creation/update/verification | depends on connectors |
| internet verification | depends on connector |
| local filesystem or sandbox | unavailable |
| local Git repository access | unavailable |
| shell | unavailable |
| coordination bus | unavailable |
| durable memory write | unavailable (ChatGPT memory is not governed memory) |
| automation creation | unavailable |

**Never infer availability from prior sessions or user claims.** Mark unavailable capabilities explicitly with `UNAVAILABLE` and do not mark them `PASS` or `used: true`.

## Required procedure

1. **Enter closeout freeze**: no new substantive implementation after closeout begins.
2. **Select profile** based on actual session activity (chat vs work session vs checkpoint vs trivial).
3. **Build session objective and outcome ledger** from visible context.
4. **Reconcile every external write** using connector/tool results already returned or fresh read-back where necessary.
5. **Search for existing canonical artifacts** before creating new ones.
6. **Identify material unpreserved session value**.
7. **Classify candidate preservation destinations** as public/private/internal/chat-only.
8. **Perform only bounded preservation actions** that are authorized and clearly housed.
9. **Emit compatible handoff and receipt artifacts** (agent-handoffs#9 and execution-receipts#10 profiles).
10. **Return categorical readiness disposition** and first next action.

## Preservation policy

### Preferred

- comment/update an existing issue or document;
- create a bounded issue only when the work is material, actionable, scoped, non-duplicate, and has a clear repo;
- preserve confirmed artifact links;
- provide an in-chat handoff when no safe durable sink exists.

### Prohibited

- full-transcript publication by default;
- automatic public issue creation from private/personal content;
- invented file paths, issue numbers, receipts, or memory writes;
- claims that local Git, bus, shell, or filesystem were checked when inaccessible;
- autonomous future continuation;
- hidden-reasoning disclosure or use as evidence;
- starting new implementation after closeout begins.

## Output requirements

### Human closeout (concise)

```text
Disposition: READY_TO_RESUME | READY_WITH_GAPS | NOT_READY | CHECKPOINT_ONLY | NO_CLOSEOUT_REQUIRED
Preserved: <confirmed artifacts or in-chat-only>
Open: <material unfinished work>
Unavailable/failed: <checks or writes>
First next action: <one bounded action>
```

### Machine/structured artifacts

- handoff profile compatible with `agent-handoffs#9`;
- receipt compatible with `execution-receipts#10`;
- protocol step outcomes compatible with `protocol-as-code#7`.

## Idempotency behavior

Before creating a durable artifact:

- search current session outputs and target repo/source for an existing closeout or coordination artifact;
- update existing canonical artifacts where safe;
- otherwise create one superseding artifact with links;
- retain failed attempts;
- do not create duplicate issues because the user invokes closeout twice.

## Dry-run matrix

The adapter must be validated against at least these 10 scenarios:

1. chat-only strategy session;
2. GitHub-connected work session with confirmed issue creation;
3. session with failed connector write;
4. mixed private/public context with public minimal-disclosure output;
5. repeated closeout invocation;
6. checkpoint after interruption;
7. no-closeout-required trivial session;
8. session where Git/shell/bus/memory are unavailable;
9. session with an ambiguous canonical destination;
10. session requiring human approval before preservation.

## Capability-aware fallback table

| Capability unavailable | Adapter behavior |
|------------------------|-----------------|
| local Git | Mark `UNAVAILABLE`; do not claim commits, branches, or status were checked |
| shell | Mark `UNAVAILABLE`; do not claim command output as evidence |
| coordination bus | Mark `UNAVAILABLE`; no bus STATUS posted; note in receipt `materialMissingChecks` |
| durable memory | Mark `UNAVAILABLE`; do not claim memory writes; preserve in-chat or in-handoff only |
| filesystem | Mark `UNAVAILABLE`; do not claim file creation; use connector-based artifacts only |
| GitHub connector | If work session required writes, disposition drops to `NOT_READY` or `READY_WITH_GAPS` |

## Cross-adapter compatibility

This adapter produces artifacts compatible with:

- **agent-handoffs#9** handoff profile (handoff packet schema)
- **execution-receipts#10** closeout receipt profile (receipt schema)
- **protocol-as-code#7** conversation lifecycle protocol (step outcomes)

A different adapter (e.g., Claude Code, Codex) consuming the handoff and receipt produced by this adapter must be able to resume work without ChatGPT-specific knowledge.

## Primary acceptance test

Close one real HUMMBL ChatGPT work session and give the handoff plus referenced artifacts to a different authorized agent/session. The receiving agent must be able to resume without asking the original ChatGPT session for clarification.

## Non-goals

- Does not define the protocol (see protocol-as-code#7)
- Does not define the handoff schema (see agent-handoffs#9)
- Does not define the receipt schema (see execution-receipts#10)
- Does not modify ChatGPT platform behavior
- Does not assume native slash command support

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#160
- **Dependencies**: protocol-as-code#7 (draft), agent-handoffs#9 (draft PR #10), execution-receipts#10 (draft PR #11)
- **Adapter modes**: 4 (CHAT_CLOSEOUT, WORK_SESSION_CLOSEOUT, SESSION_CHECKPOINT, NO_CLOSEOUT_REQUIRED)
- **Capability mappings**: 11
- **Dry-run scenarios**: 10
- **Preservation prohibitions**: 7
- **Review status**: PENDING
