# GitHub Audit Actions - 2026-04-01

This file tracks GitHub account and repository governance work identified during the April 1, 2026 audit.

## Completed

- Added org-wide `CODEOWNERS` in `hummbl-dev/.github`
- Added org-wide pull request template in `hummbl-dev/.github`
- Added org-wide issue templates and routing in `hummbl-dev/.github`

## Remaining Actions

### 1. Normalize branch defaults

- Change `hummbl-dev/hummbl-tuples` default branch from `master` to `main`
- Verify no other repositories still use non-standard default branch names

### 2. Enforce branch protection / rulesets

Apply GitHub rulesets or branch protection to core repositories:

- `hummbl-governance`
- `base120`
- `mcp-server`
- `hummbl-agent`
- `hummbl-assurance`
- `hummbl-production`

Minimum target policy:

- Require pull request before merge
- Require status checks to pass
- Require at least one review for code changes
- Require CODEOWNER review on sensitive paths where repo-local CODEOWNERS exist
- Restrict force-push and branch deletion on default branches
- Choose one merge strategy standard for core repos

### 3. Reduce portfolio sprawl

Review low-signal or placeholder repositories and decide to archive, privatize, consolidate, or delete.

Examples surfaced in audit:

- Public: `bif`, `agent-governance-demo`, `arbiter`
- Private placeholders/stubs: `discovery`, `docs`, `god-mode`, `mirror-agent`, `rpbx`, `hummbl-gaas-platform`

### 4. Dependabot triage and batching

- Review open dependency PR queues in `mcp-server`, `hummbl-agent`, and `hummbl-production`
- Add repo-local batching, auto-merge, or stricter ignore rules where safe
- Keep noise low enough that real governance and product PRs stay visible

### 5. Repo-local ownership for critical repos

Add repo-local `CODEOWNERS` where ownership needs to be narrower than the org default.

Priority repos:

- `hummbl-production`
- `hummbl-agent`
- `mcp-server`
- `base120`
- `hummbl-governance`

### 6. Close known governance workflow debt

In `base120`, resolve and verify CI/governance issues surfaced by open issues:

- #33 Golden corpus determinism workflow reliability
- #35 Drift detection workflow comment posting bug

## Notes

The audit found strong direction and improving public coherence, but enforcement is still partly convention-driven. The next milestone is to convert conventions into platform-enforced GitHub policy.
