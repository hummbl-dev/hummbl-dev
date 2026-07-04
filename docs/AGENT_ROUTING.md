# Agent Routing

Agents should read `AGENTS.md` before making changes. Cross-repo or org-level work should be coordinated through issues in this repo. Repo-specific changes should happen in the target repo unless the task is explicitly about public profile, inventory, templates, or cross-repo governance.

## Routing Rules

| Work type | Route |
|---|---|
| Repo-specific code or docs | Target repo branch and PR. |
| Public profile README, static tools, or repo inventory | This repo. |
| Cross-repo proposal or coordination issue | This repo. |
| Agent task assignment | `agent-handoff` issue template. |
| Security-sensitive work | Follow `SECURITY.md` and repo-specific security instructions. |

## Evidence

Agent changes should leave reviewable evidence:

- Issue or PR link for the task.
- Files changed and validation run.
- Known gaps or follow-up work.
- Explicit boundary when content is exploratory rather than adopted canon.

For cross-repo public-surface work, use the Agent Command Center board spec in
[`docs/agent-command-center.md`](agent-command-center.md).
