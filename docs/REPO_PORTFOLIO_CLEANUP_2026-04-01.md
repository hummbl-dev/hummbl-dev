# Repo Portfolio Cleanup Plan - 2026-04-01

This file converts the GitHub audit into a portfolio cleanup shortlist.

## Keep As Canonical Public Spine

These repos clearly support the current HUMMBL story and should remain visible and well-maintained:

- `hummbl-dev` (profile repo)
- `.github`
- `base120`
- `hummbl-governance`
- `mcp-server`
- `hummbl-agent`
- `hummbl-assurance`
- `HUMMBL-Unified-Tier-Framework`
- `hummbl-bibliography`

## Keep But Govern More Tightly

These look active or strategically relevant, but should have stronger repo-level governance and clearer positioning:

- `hummbl-production`
- `hummbl-iac`
- `hummbl-tuples`
- `governed-iac-reference`

## Review For Archive / Privatize / Consolidate

These surfaced as low-signal, placeholder, demo, or ambiguous repos in the audit. Review each and make an explicit decision.

### Public review set
- `bif`
- `agent-governance-demo`
- `arbiter`
- `agentic-patterns`
- `hummbl-mobile`

### Private review set
- `discovery`
- `docs`
- `god-mode`
- `mirror-agent`
- `rpbx`
- `hummbl-gaas-platform`
- `games`
- `sys-arch-testing`
- `autoresearch-pipeline`
- `hummbl-prototype`
- `hummbl-asi`
- `hummbl-gpts`
- `forge`
- `init-system`
- `ci-governance`
- `hummbl-v2`
- `hummbl-old-version`
- `hummbl`

## Review Criteria

For each repo, choose one state:

- Keep active
- Keep private
- Archive public
- Merge into another repo
- Delete

Use these questions:

- Does it support the current public HUMMBL narrative?
- Is it actively maintained?
- Does it duplicate another repo’s purpose?
- Does it contain historical but still useful reference material?
- Is the name likely to confuse partners, users, or reviewers?

## Immediate Hygiene Tasks

1. Change `hummbl-tuples` default branch from `master` to `main`.
2. Correct stale ownership in `hummbl-production`.
3. Replace workstation-local links in `hummbl-production/README.md`.
4. Fix broken placeholder Dependabot config in `hummbl-governance`.

## Suggested Execution Order

1. Fix branch and ownership inconsistencies.
2. Clean up public-facing low-signal repos.
3. Audit private placeholder repos for deletion or archive.
4. Re-pin profile/projects after cleanup if needed.
