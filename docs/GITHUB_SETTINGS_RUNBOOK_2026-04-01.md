# GitHub Settings Runbook - 2026-04-01

This runbook is the ordered admin pass for applying GitHub settings to HUMMBL core repositories.

## Sequence

Apply in this order:

1. `base120`
2. `hummbl-governance`
3. `mcp-server`
4. `hummbl-agent`
5. `hummbl-assurance`
6. `hummbl-production`
7. `hummbl-iac`
8. `hummbl-tuples` default-branch normalization

## Standard UI Path

For each repository:

- Open repository
- Open `Settings`
- Open `General` to review merge settings
- Open `Rules` or `Branches`
- Create or update default-branch protection for `main`

## Repo-By-Repo Steps

### 1. `base120`
- Confirm default branch is `main`
- Disable merge commits
- Disable rebase merge
- Keep squash merge enabled
- Require PR before merge
- Require 1 approval
- Require conversation resolution
- Require status checks:
  - `ci / test (3.11)`
  - `ci / test (3.12)`
  - `Governance Invariants / Golden Corpus Determinism`
  - `Semantic Drift Detection / detect-drift`
- Enable CODEOWNERS-required review

### 2. `hummbl-governance`
- Confirm default branch is `main`
- Fix `.github/dependabot.yml` first using `docs/EXACT_REPO_FIXES_2026-04-01.md`
- Disable merge commits
- Disable rebase merge
- Keep squash merge enabled
- Require PR before merge
- Require 1 approval
- Require conversation resolution
- Require status checks:
  - `ci / test (3.11)`
  - `ci / test (3.12)`
  - `ci / lint`
- Enable CODEOWNERS-required review after the repo-local CODEOWNERS file is confirmed

### 3. `mcp-server`
- Confirm default branch is `main`
- Disable merge commits
- Disable rebase merge
- Keep squash merge enabled
- Require PR before merge
- Require 1 approval
- Require conversation resolution
- Require the primary CI, typecheck, and test checks
- Enable CODEOWNERS-required review
- Review whether Dependabot PR count should be throttled further

### 4. `hummbl-agent`
- Confirm default branch is `main`
- Disable merge commits
- Disable rebase merge
- Keep squash merge enabled
- Require PR before merge
- Require 1 approval
- Require conversation resolution
- Require build, typecheck, test, and any policy-validation checks
- Enable CODEOWNERS-required review

### 5. `hummbl-assurance`
- Confirm default branch is `main`
- Disable merge commits
- Disable rebase merge
- Keep squash merge enabled
- Require PR before merge
- Require 1 approval
- Require conversation resolution
- Require verify or conformance workflow checks
- Enable CODEOWNERS-required review

### 6. `hummbl-production`
- Confirm default branch is `main`
- Update `.github/CODEOWNERS` and `README.md` first using `docs/EXACT_REPO_FIXES_2026-04-01.md`
- Disable merge commits
- Disable rebase merge
- Keep squash merge enabled
- Require PR before merge
- Require 1 approval
- Require conversation resolution
- Require main CI workflow
- Add alternate CI check only if stable and consistently present
- Enable CODEOWNERS-required review only after the stale owner is corrected

### 7. `hummbl-iac`
- Confirm default branch is `main`
- Disable merge commits
- Disable rebase merge
- Keep squash merge enabled
- Require PR before merge
- Require 1 approval
- Require conversation resolution
- Require workflow validation once CI exists or is expanded
- Enable CODEOWNERS-required review

### 8. `hummbl-tuples`
- Change default branch from `master` to `main`
- Update branch protection to target `main`
- Repoint any workflows or badges if needed

## Final Verification

After finishing all repos:

- Confirm no core repo still allows direct pushes to default branch
- Confirm merge strategy is consistent across core repos
- Confirm CODEOWNERS-required review is enabled only where repo-local ownership is correct
- Confirm all default branches are `main`
- Revisit public profile pins if needed after cleanup
