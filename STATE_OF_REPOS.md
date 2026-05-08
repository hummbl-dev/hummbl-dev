# State of Repos | 2026-05-08

This file is the short current summary. The detailed generated inventory lives in:

- [`docs/GITHUB_REPO_INVENTORY_2026-05-08.md`](docs/GITHUB_REPO_INVENTORY_2026-05-08.md)
- [`docs/BRANCH_CLEANUP_AUDIT_2026-05-08.md`](docs/BRANCH_CLEANUP_AUDIT_2026-05-08.md)

## Summary

| Metric | Count |
|---|---:|
| Total `hummbl-dev` repositories | 54 |
| Active public repositories | 35 |
| Active private repositories | 17 |
| Archived repositories | 2 |
| Branch audit records | 263 |
| Deletion candidates by graph shape | 31 |
| Stale low-ahead review branches | 119 |
| Branches with open PRs | 5 |

## Current Public Spine

| Repo | Role |
|---|---|
| [`hummbl-governance`](https://github.com/hummbl-dev/hummbl-governance) | Runtime governance primitives |
| [`base120`](https://github.com/hummbl-dev/base120) | Mental-model substrate |
| [`evidence-gate`](https://github.com/hummbl-dev/evidence-gate) | Source-verification rule library |
| [`arbiter`](https://github.com/hummbl-dev/arbiter) | Repository quality and governance scoring |
| [`mcp-server`](https://github.com/hummbl-dev/mcp-server) | MCP interface for HUMMBL skills and models |
| [`hummbl-agent`](https://github.com/hummbl-dev/hummbl-agent) | Agent orchestration patterns |
| [`hummbl-bibliography`](https://github.com/hummbl-dev/hummbl-bibliography) | Bibliography and citation corpus |
| [`hummbl-dev`](https://github.com/hummbl-dev/hummbl-dev) | Public profile, tools, and repo inventory |

## Private Active Spine

| Repo | Role |
|---|---|
| `founder-mode` | Internal agent coordination and operator workflows |
| `fractional-bench` | Productized fractional-services methodology bench |
| `hummbl-production` | Production Cloudflare Workers and public site stack |
| `arcana` | Multi-lens governance and political-philosophy analysis pipeline |
| `claude-config` | Agent profile config and runtime rules |
| `hummbl-iac` | Fleet infrastructure-as-code |

## Cleanup Posture

No branch deletion was performed in the 2026-05-08 audit.

Deletion candidates are only graph-shape candidates: non-default branches with zero commits ahead of default and no open PR. They still require explicit operator approval before any destructive action.

High-confidence next pass:

1. Review the 31 `delete_candidate_merged_or_empty` branches.
2. Separate HUMMBL-owned branches from inherited upstream/fork branches in repos such as `paramiko`, `rich`, and `vllm`.
3. Delete only approved HUMMBL-owned branches first.
4. Leave stale low-ahead branches for separate salvage/close decisions.
