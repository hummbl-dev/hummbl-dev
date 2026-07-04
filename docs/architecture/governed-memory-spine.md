# Governed Memory Spine

## Status

Candidate architecture. Not canon.

## Layer Model

```text
Source Corpus -> Extraction -> Typed Graph -> Retrieval -> Governance -> Agent Runtime -> Receipts
```

## Layers

### Source Corpus

Inputs may include public-safe README files, docs, issues, PR metadata,
discussion records, release notes, receipts, ADRs, and artifacts.

Do not ingest private repos, credentials, raw personal data, or private customer
records without a separate private-boundary packet.

### Extraction

Extract typed objects:

- claim,
- decision,
- task,
- source,
- receipt,
- artifact,
- person/team/agent,
- repo,
- canon candidate,
- deprecated item.

Extraction must preserve source location and confidence. It must not rewrite
source meaning into stronger claims.

### Typed Graph

Candidate node types:

- `Artifact`
- `Claim`
- `Decision`
- `Receipt`
- `Task`
- `Repo`
- `Agent`
- `Source`
- `Status`

Candidate relations:

- `cites`
- `supports`
- `contradicts`
- `supersedes`
- `blocks`
- `implements`
- `reviewed_by`
- `promoted_to`
- `deprecated_by`

### Retrieval

Retrieval should combine:

- full-text search,
- metadata filters,
- graph traversal,
- recency/freshness ranking,
- citation requirement,
- permission filter.

No agent answer should cite memory without a source pointer.

### Governance

Memory status must be explicit:

- raw,
- candidate,
- reviewed,
- canon,
- deprecated,
- contradicted,
- private,
- public-safe.

Promotion requires receipt-bearing review. Deprecation should preserve the old
object and point to the superseding object.

### Agent Runtime

Allowed actions:

- read,
- cite,
- summarize,
- report stale or contradictory claims,
- open issues,
- draft PRs.

Forbidden without explicit approval:

- silently mutate canon,
- erase contradictions,
- promote candidates,
- cross public/private boundaries,
- answer without citations when claiming institutional state.

## BaseN Mapping

BaseN can be treated as transformation machinery over memory objects:

- extract claim from artifact,
- collapse duplicate claims,
- compare novelty distance,
- route contradiction,
- promote candidate to reviewed.

This is a candidate mapping, not a mystical or canonical "brain" claim.
