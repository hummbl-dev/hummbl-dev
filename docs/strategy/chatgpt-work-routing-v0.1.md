# ChatGPT Work Platform Signal — Routing Distinction v0.1

**Status: SOURCE-GROUNDED — NON-CANON — RE-CHECK REQUIRED BEFORE MERGE**

Issue: hummbl-dev/hummbl-dev#139
Observation date: 2026-07-10

## Purpose

OpenAI's ChatGPT Work announcement is a meaningful platform signal for HUMMBL / Ownward / Codex routing. This document preserves the signal as a bounded operational distinction so agents can reason from it without turning OpenAI's product surface into an architectural dependency.

## Source inputs

Official OpenAI sources observed on 2026-07-10:

- ChatGPT Work announcement: https://openai.com/index/chatgpt-for-your-most-ambitious-work/
- ChatGPT Work product page: https://openai.com/chatgpt-work/
- GPT-5.6 announcement / model family context: https://openai.com/index/gpt-5-6/
- ChatGPT Projects help page: https://help.openai.com/en/articles/10169521-projects-in-chatgpt
- Apps in ChatGPT help page: https://help.openai.com/en/articles/11487775-connectors-in-chatgpt
- Related OpenAI agent background: https://openai.com/index/introducing-chatgpt-agent/

These are source inputs, not canon. Re-check before merging because OpenAI product surfaces are volatile.

## Surface distinction

| Surface | What it is | HUMMBL posture |
|---------|-----------|----------------|
| ChatGPT Chat | Conversational interface for general Q&A, drafting, analysis | Useful for research, drafting, exploration — not for governed execution |
| ChatGPT Projects | Context surface: persistent context, files, instructions per project | Useful for organizing research sessions — not a runtime architecture |
| ChatGPT Apps/Connectors | Tool/data surface: third-party integrations for data access | Useful for signal gathering — not a governance boundary |
| ChatGPT Work | Delegated execution surface: longer-horizon, multi-step work with tool use | Candidate for bounded task delegation — not a replacement for governed agents |
| Codex | Repo/change implementation agent surface: code changes, PRs, tests | Useful for implementation tasks — operates within HUMMBL governance when used |
| HUMMBL/Ownward | Governed product/runtime architecture: contracts, receipts, guardrails, bus | The authoritative runtime; vendor surfaces are inputs, not authorities |

## Architectural principle

**Be ChatGPT Work-ready, not ChatGPT Work-bound.**

- Preserve vendor-neutral abstractions and receipts.
- Avoid making OpenAI product behavior a hard architectural premise.
- Treat vendor surfaces as candidate execution lanes, not as governance authority.
- HUMMBL governance (contracts, receipts, guardrails, bus) remains the authoritative layer regardless of which vendor surface executes the work.

## Routing table

| Task type | Recommended lane | Why |
|-----------|-----------------|-----|
| Research exploration, source gathering | ChatGPT Chat or Projects | Fast, conversational, good for synthesis |
| Drafting docs, proposals, analysis | ChatGPT Projects | Persistent context helps coherence |
| Bounded multi-step task with tool use | ChatGPT Work (candidate) | Delegated execution — but require HUMMBL receipt on completion |
| Code changes, PRs, tests | Codex | Repo-aware implementation agent |
| Governed execution with contracts and receipts | HUMMBL/Ownward runtime | Authoritative governance layer |
| Voice-first coaching | Ownward | Voice runtime — not a ChatGPT surface |
| Cross-agent coordination | HUMMBL bus | Coordination protocol — vendor-independent |

## Codex/operator routing guidance

When deciding where a task belongs:

1. **Is it a code change to a HUMMBL repo?** → Codex (with HUMMBL governance)
2. **Is it research or drafting?** → ChatGPT Chat/Projects (then ingest into HUMMBL via receipts)
3. **Is it a bounded multi-step task needing tool use?** → ChatGPT Work (candidate) — require a HUMMBL receipt on completion
4. **Is it governed execution requiring contracts, guardrails, or bus coordination?** → HUMMBL/Ownward runtime
5. **Is it voice-first coaching?** → Ownward (see #124)

## Non-goals

- Do not adopt ChatGPT Work as a dependency.
- Do not introduce new canon terminology.
- Do not rewrite the public README unless a small link is clearly warranted.
- Do not claim private access to ChatGPT Work behavior beyond official public sources and user-observed UI.
- Do not make commitments about OpenAI roadmap, pricing, availability, or private team data.

## Related work

- #124 — Ownward Voice Runtime Abstraction v0.1 / GPT-Live readiness
- #141 — Frontier Lab Signal Registry v0.1 (generalizes this pattern)

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#139
- **Observation date**: 2026-07-10
- **Source posture**: official OpenAI public pages, re-check before merge
- **Architecture posture**: vendor-neutral; GPT/OpenAI surfaces are candidates/signals, not dependencies
- **Canonical status**: non-canon
- **Review status**: PENDING — re-check sources before merge
