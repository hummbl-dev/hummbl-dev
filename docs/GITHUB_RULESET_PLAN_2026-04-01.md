# GitHub Ruleset Plan - 2026-04-01

This file defines the recommended GitHub branch protection / ruleset baseline for HUMMBL core repositories.

## Core Repositories

Apply the following baseline to:

- `base120`
- `hummbl-governance`
- `mcp-server`
- `hummbl-agent`
- `hummbl-assurance`
- `hummbl-production`
- `hummbl-iac`

## Default Branch Policy

Target branch: `main`

Required protections:

- Require a pull request before merging
- Require at least 1 approval before merge
- Dismiss stale approvals on new commits
- Require conversation resolution before merge
- Require status checks to pass before merge
- Require branch to be up to date before merge where practical
- Block force pushes to default branch
- Block branch deletion on default branch
- Restrict direct pushes to admins only if emergency access is needed, otherwise block all direct pushes

## Merge Strategy Standard

Recommended default for core repos:

- Allow squash merge: `enabled`
- Allow rebase merge: `disabled`
- Allow merge commits: `disabled`
- Auto-merge: `enabled` only after checks + review policy are stable

Rationale:

- Squash merges keep history legible
- Rebase and merge-commit combinations weaken audit readability in small teams
- Auto-merge is useful only after status checks and ownership rules are trustworthy

## Required Status Checks By Repo

### `base120`
- `ci / test (3.11)`
- `ci / test (3.12)`
- `Governance Invariants / Golden Corpus Determinism`
- `Semantic Drift Detection / detect-drift`

### `hummbl-governance`
- `ci / test (3.11)`
- `ci / test (3.12)`
- `ci / lint`

### `mcp-server`
- require primary CI workflow(s)
- require typecheck and test jobs if split
- require dependency/security checks if already wired

### `hummbl-agent`
- require primary CI workflow(s)
- require build/test/typecheck jobs for package changes
- require policy/governance validation jobs if present

### `hummbl-assurance`
- require verify / conformance workflow(s)
- require release/protection audit jobs if already defined

### `hummbl-production`
- require main test workflow
- require fallback CI or equivalent hosted CI when GitHub Actions is unavailable
- require preview/deploy checks only if deterministic and stable

### `hummbl-iac`
- require syntax/render validation if added
- require workflow validation if CI exists

## CODEOWNERS Review Policy

- Enable CODEOWNERS review requirement for repos with repo-local `CODEOWNERS`
- Start with these repos first:
  - `base120`
  - `mcp-server`
  - `hummbl-agent`
  - `hummbl-assurance`
  - `hummbl-iac`

## Manual Follow-Up

1. Normalize default branches first.
2. Clean up stale repo-local ownership files before enabling CODEOWNERS-required review.
3. Add rulesets on the public core repos first.
4. Extend to private operational repos once status checks are stable.
