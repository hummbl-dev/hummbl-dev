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
{"id":"artifact:docs/repo-map.md","type":"Artifact","lifecycle":"reviewed","visibility":"public-safe","source":"docs/repo-map.md","source_location":"docs/repo-map.md","provenance_confidence":"high"}
{"id":"claim:repo-candidate-agent-receipts","type":"Claim","lifecycle":"candidate","visibility":"public-safe","source":"docs/repo-map.md","source_location":"docs/repo-map.md#candidate-repo-admission-queue","provenance_confidence":"medium"}
{"id":"receipt:pr-87","type":"Receipt","lifecycle":"reviewed","visibility":"public-safe","source":"https://github.com/hummbl-dev/hummbl-dev/pull/87","source_location":"pull_request:87","provenance_confidence":"high"}
```

JSONL edges:

```json
{"from":"claim:repo-candidate-agent-receipts","to":"artifact:docs/repo-map.md","type":"cites","source_location":"docs/repo-map.md#candidate-repo-admission-queue","provenance_confidence":"medium"}
{"from":"receipt:pr-87","to":"artifact:docs/repo-map.md","type":"reviewed_by","source_location":"pull_request:87","provenance_confidence":"high"}
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
