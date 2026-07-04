# Prototype: Graph Retrieval Receipt Map v0.1

## Status

Prototype proposal. Not implemented.

## Goal

Create the smallest public-safe graph export that lets an agent answer with
citations, identify stale claims, and open correction issues without mutating
canon.

## Corpus

Start with public files and GitHub metadata from `hummbl-dev/hummbl-dev`:

- README and top-level doctrine docs,
- `docs/`,
- issues,
- PR metadata,
- merged PR receipts,
- ADRs and receipt files.

Exclude private repos, private customer data, raw chat logs, credentials, and
personal data.

## Output Format

JSONL nodes:

```json
{"id":"artifact:docs/repo-map.md","type":"Artifact","status":"public-safe","source":"docs/repo-map.md"}
{"id":"claim:repo-candidate-agent-receipts","type":"Claim","status":"candidate","source":"docs/repo-map.md"}
{"id":"receipt:pr-87","type":"Receipt","status":"reviewed","source":"https://github.com/hummbl-dev/hummbl-dev/pull/87"}
```

JSONL edges:

```json
{"from":"claim:repo-candidate-agent-receipts","to":"artifact:docs/repo-map.md","type":"cites"}
{"from":"receipt:pr-87","to":"artifact:docs/repo-map.md","type":"reviews"}
```

## Minimal Steps

1. Enumerate public Markdown files.
2. Pull issue and PR metadata through `gh`.
3. Extract candidate claims, decisions, tasks, and receipts with source paths.
4. Emit JSONL nodes and edges.
5. Generate stale-claim and contradiction reports.
6. Require source links in any agent answer.
7. Open issues or draft PRs for corrections; never mutate canon directly.

## Report Types

- missing receipt,
- stale claim,
- contradictory claim,
- uncited decision,
- candidate older than review SLA,
- private-boundary risk marker in public surface.

## Non-Goals

- embeddings,
- production vector database,
- private repo ingestion,
- automatic canon promotion,
- silent mutation by agents.

## Promotion Gate

This prototype can graduate only after:

- public/private boundary review,
- sample JSONL receipt,
- at least one stale-claim report,
- at least one correction issue or PR generated from the report,
- false-positive review.
