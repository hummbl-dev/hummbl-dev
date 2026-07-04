# Governed Company Brain v0.1

## Status

Research packet. Candidate architecture. Not canon.

## Executive Read

A viral claim asserted that Anthropic had an internal "Obsidian brain" or
company knowledge graph leak. Public search found social chatter and derivative
posts about Claude Code, Obsidian, leaked code, and second-brain workflows, but
did not find a credible public artifact proving an Anthropic internal Obsidian
vault leak.

The useful signal is not the viral claim. The useful signal is market appetite
for an agent-readable institutional memory layer.

## Claim Provenance Disposition

| Item | Current status | Treatment |
| --- | --- | --- |
| Anthropic has an internal Obsidian company brain | unsupported public claim | Do not cite as fact. |
| Anthropic/Claude Code leak discourse exists | public discourse exists | Treat as context, not proof of the Obsidian-vault claim. |
| Obsidian + Claude Code / second-brain workflows are popular | supported by public posts, repos, and plugin ecosystem | Treat as market signal. |
| Company brain as governed memory | HUMMBL candidate architecture | Evaluate on primitives, not hype. |

Public context checked on 2026-07-04.

Search queries:

- `Anthropic Obsidian brain company knowledge graph leak`
- `"Anthropic" "Obsidian" "brain" leak`
- `site:x.com Anthropic Obsidian brain leak`
- `Anthropic internal Obsidian vault knowledge graph`

Surfaced results and disposition:

- X post result titled "23 PAGES. 10 ANTHROPIC TEAMS..." surfaced in search, but
  the surfaced snippet did not establish a repo, vault, archive, hash, or source
  package.
- Search surfaced Medium/Substack/LinkedIn-style posts discussing Claude Code
  leaks, Obsidian, and second-brain patterns. These are derivative narratives,
  not source packages for the specific Anthropic/Obsidian-vault claim.
- Search surfaced public GitHub and Obsidian-plugin examples for graph-backed
  personal knowledge workflows. These support market-interest analysis, not the
  Anthropic internal-vault claim.
- No archive or snapshot identifier was found or used in this pass.

Reference surfaces checked:

- `https://x.com/de1lymoon/status/2072050181181255934/photo/1`
- `https://github.com/eugeniughelbur/obsidian-second-brain`
- `https://community.obsidian.md/plugins/graph-context-for-claude-code`
- `https://blog.fsck.com/agent-blog/2026/03/20/knowledge-graph/`

## Market Metaphor Analysis

Resonant terms:

- company brain,
- second brain,
- knowledge graph,
- operating memory,
- institutional intelligence,
- AI wiki,
- graph RAG,
- agent memory.

Audiences:

- founders and operators who want continuity,
- research teams who want less repeated context,
- agencies and services teams who want reusable work receipts,
- engineering teams that want issue/PR/docs memory,
- PKM users who understand Obsidian-style graph metaphors.

Emotional hook:

- fewer repeated decisions,
- faster onboarding,
- retained institutional context,
- less context loss between agents and humans,
- agent autonomy with traceable citations.

## Competitive Landscape

| Category | Representative systems | Useful primitive | Gap |
| --- | --- | --- | --- |
| PKM / graph notes | Obsidian, Logseq, Roam, Tana | local notes, backlinks, graph views | weak authority, permissions, freshness, receipts |
| Team knowledge bases | Notion, Confluence, Slab, Guru | shared docs and search | often doc-centric, not claim/decision-centric |
| Enterprise AI search / RAG | Glean, Hebbia, Dust, Sana, Writer, Atlassian Rovo | retrieval across corpora | provenance and action boundaries vary |
| Agent workspaces | Claude Code, Cursor, Devin, Codex, Linear/GitHub agents | task execution and code/doc mutation | memory often session/tool-specific |
| Governance/provenance systems | policy-as-code, data catalogs, model cards, eval ledgers | typed controls and receipts | not usually packaged as operational memory |

## HUMMBL Candidate

A governed company brain is not an Obsidian vault and not RAG over docs. It is
governed institutional memory:

- every claim has provenance,
- every decision has a receipt,
- stale claims are detectable,
- contradictions are preserved and routed,
- permissions are explicit,
- canon/candidate/deprecated state is machine-readable,
- agents can cite, propose, and open PRs, but cannot silently mutate canon.

## Non-Goals

- Do not build a production graph system in this packet.
- Do not ingest private repos or private user data.
- Do not present the viral Anthropic/Obsidian claim as fact.
- Do not promote "company brain" or BaseN memory terms into canon.
