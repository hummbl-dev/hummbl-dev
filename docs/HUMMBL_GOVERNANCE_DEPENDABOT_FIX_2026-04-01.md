# Exact Fix: `hummbl-governance/.github/dependabot.yml` (2026-04-01)

## Problem

The current file is a placeholder generated from the default Dependabot template and is visibly invalid:

```yaml
version: 2
updates:
  - package-ecosystem: ""
    directory: "/hummbl-governance"
    schedule:
      interval: "weekly"
```

This harms the public maintenance signal of a canonical HUMMBL repository.

## Recommended Replacement

Replace the entire file with:

```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5

  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 3
```

## Why This Replacement

- `package-ecosystem` is valid
- `directory` points to the actual repo root
- Python dependency updates are enabled for the package itself
- GitHub Actions updates are enabled for workflow maintenance
- pull-request limits prevent queue spam

## Expected Outcome

Once replaced, `hummbl-governance` should move up materially in the active public fleet ranking and stop carrying a visible governance contradiction.
