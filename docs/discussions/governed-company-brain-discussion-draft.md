# Discussion Draft: Governed Company Brain

## Prompt

What would make a company memory system trustworthy enough for agents to use?

## Context

Recent social chatter about an alleged Anthropic "Obsidian brain" appears
unverified, but the metaphor is sticky because many teams feel the same pain:
institutional memory is scattered across docs, issues, PRs, chats, decisions,
and people's heads.

Obsidian graphs and RAG search are useful, but neither is enough by itself.

## Proposed Frame

A real company brain is governed institutional memory:

- claims have sources,
- decisions have receipts,
- stale claims are visible,
- contradictions are first-class,
- permissions are enforced,
- agents cite before acting,
- canon promotion requires review.

## Questions For Review

1. Which memory objects should HUMMBL model first: claims, decisions, tasks, or receipts?
2. What should be the first public-safe corpus: README/docs, issues, PR metadata, or receipts?
3. What status ladder is useful without becoming bureaucracy?
4. What should agents be allowed to do with memory by default?
5. What should always require a human gate?

## Candidate Prototype

Start with `hummbl-dev/hummbl-dev` public-safe data only:

- ingest README/docs/issues/PR metadata,
- emit JSONL nodes and edges,
- classify claim/decision/task/source/receipt objects,
- require source citations,
- report contradictions and stale claims,
- draft issues or PRs for corrections.

## Non-Goals

- no private repo ingestion,
- no production graph system,
- no viral-claim laundering,
- no new canon term without review.
