# GitHub Ruleset UI Checklist - 2026-04-01

Use this checklist when applying branch protection or rulesets manually in the GitHub UI.

## Apply First To

1. `base120`
2. `hummbl-governance`
3. `mcp-server`
4. `hummbl-agent`
5. `hummbl-assurance`
6. `hummbl-production`
7. `hummbl-iac`

## UI Path

For each repository:

- Open `Settings`
- Open `Rules` or `Branches`
- Create a new ruleset for the default branch, or update branch protection for `main`

## Checklist

### Branch target
- [ ] Target branch is `main`
- [ ] If repo still uses another default branch, normalize that first

### Pull request protection
- [ ] Require a pull request before merging
- [ ] Require at least 1 approval
- [ ] Dismiss stale approvals when new commits are pushed
- [ ] Require all conversations to be resolved before merge

### Status checks
- [ ] Require status checks before merging
- [ ] Require branch to be up to date before merging where it does not create excessive churn
- [ ] Add the repo’s primary CI checks explicitly

### Branch safety
- [ ] Block force pushes
- [ ] Block branch deletion
- [ ] Restrict direct pushes to default branch

### Ownership
- [ ] Enable required CODEOWNERS review if repo-local `CODEOWNERS` is valid
- [ ] Skip this temporarily if repo-local ownership is known to be stale

### Merge strategy
Recommended on core repos:
- [ ] Squash merge enabled
- [ ] Rebase merge disabled
- [ ] Merge commits disabled
- [ ] Auto-merge disabled until checks are stable, then optionally enabled

## Suggested Status Checks

### `base120`
- [ ] `ci / test (3.11)`
- [ ] `ci / test (3.12)`
- [ ] `Governance Invariants / Golden Corpus Determinism`
- [ ] `Semantic Drift Detection / detect-drift`

### `hummbl-governance`
- [ ] `ci / test (3.11)`
- [ ] `ci / test (3.12)`
- [ ] `ci / lint`

### `mcp-server`
- [ ] main CI workflow
- [ ] typecheck
- [ ] test

### `hummbl-agent`
- [ ] main CI workflow
- [ ] build
- [ ] typecheck
- [ ] test
- [ ] policy or governance validation jobs if present

### `hummbl-assurance`
- [ ] verify or conformance workflow
- [ ] protection audit job if present

### `hummbl-production`
- [ ] main test workflow
- [ ] fallback CI or alternate hosted CI if used as merge gate

### `hummbl-iac`
- [ ] syntax or render validation workflow if added
- [ ] GitHub Actions validation if present

## Known Exceptions Before Enabling CODEOWNERS Requirement

- `hummbl-production` has stale ownership in `.github/CODEOWNERS`
- Any repo without a repo-local `CODEOWNERS` can inherit org defaults, but repo-local ownership is preferable for sensitive codebases
