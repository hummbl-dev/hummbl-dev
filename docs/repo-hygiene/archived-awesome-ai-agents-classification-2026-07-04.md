# Archived `awesome-ai-agents*` Classification - 2026-07-04

Issue: [#41](https://github.com/hummbl-dev/hummbl-dev/issues/41)

This memo classifies the archived public `awesome-ai-agents*` cluster so searched public repo inventory surfaces and agents do not treat duplicate imports as active HUMMBL-maintained projects.

## Summary

| Repository | Disposition | Public-surface treatment |
|---|---|---|
| [`awesome-ai-agents`](https://github.com/hummbl-dev/awesome-ai-agents) | Archived upstream fork/import evidence archive | Do not list as active HUMMBL product. Retain only as archived public reference unless separately reviewed. |
| [`awesome-ai-agents-2026`](https://github.com/hummbl-dev/awesome-ai-agents-2026) | Archived upstream fork/import evidence archive | Do not list as active HUMMBL product. Retain only as archived public reference unless separately reviewed. |
| [`awesome-ai-agents-1`](https://github.com/hummbl-dev/awesome-ai-agents-1) | Archived upstream fork/import evidence archive | Do not list as active HUMMBL product. Retain only as archived public reference unless separately reviewed. |

## Evidence

Live GitHub metadata checked on 2026-07-04:

| Repository | Visibility | Archived | Fork | Default branch | Disk usage | Description signal |
|---|---|---:|---:|---|---:|---|
| `hummbl-dev/awesome-ai-agents` | public | yes | yes | `main` | 117632 KB | "A list of AI autonomous agents"; homepage points to `e2b.dev/docs`. |
| `hummbl-dev/awesome-ai-agents-2026` | public | yes | yes | `main` | 63 KB | "The most comprehensive list of AI agents, frameworks & tools in 2026"; homepage points to `github.com/caramaschiHG/awesome-ai-agents-2026`. |
| `hummbl-dev/awesome-ai-agents-1` | public | yes | yes | `main` | 29537 KB | "Awesome AI Agents for 2026"; README links contributor flow to `ARUNAGIRINATHAN-K/awesome-ai-agents`. |

Repository README excerpts show upstream/list-corpus positioning rather than HUMMBL product, governance primitive, or maintained public collaboration surface positioning.

Search result in this repository:

```text
rg -n "awesome-ai-agents|awesome-ai-agents-2026|awesome-ai-agents-1" README.md docs .github governance -S
```

Within the searched surfaces, only the issue-promotion packet for #41 referenced the cluster. No searched README, public routing, governance, or template surface linked these repos as active HUMMBL work.

## Decision

Classify all three repos as archived public fork/import evidence archives.

They should not be linked from active-product lists, public "Start Here" surfaces, or agent task routing surfaces. If they remain visible in an inventory, use `archived` and `fork/import` boundary language.

## Agent Routing

Agents should not file active AI-agent-list corpus work in these archived repos by default.

Use one of these routes instead:

- Public profile or inventory hygiene: `hummbl-dev/hummbl-dev`.
- Active HUMMBL agent runtime work: `hummbl-dev/hummbl-agent`.
- Cross-repo public-surface proposal: `hummbl-dev/hummbl-dev` using the cross-repo proposal template.

## Follow-Up

- If these archived forks are retained long term, a future fork-boundary sweep can add minimal archived-repo boundary notes inside each fork.
- No archive/delete/rename action is recommended from this memo alone.
