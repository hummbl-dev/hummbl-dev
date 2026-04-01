# Exact Repo Fixes - 2026-04-01

This file contains exact replacement content for the remaining existing-file fixes identified in the audit.

## 1. `hummbl-governance/.github/dependabot.yml`

Replace the current placeholder file with:

```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
    commit-message:
      prefix: "chore(deps)"

  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
    commit-message:
      prefix: "chore(ci)"
```

## 2. `hummbl-production/.github/CODEOWNERS`

Replace the current file with:

```text
# Default ownership
* @hummbl-dev

# Product surfaces
/api/ @hummbl-dev
/web/ @hummbl-dev
/.github/ @hummbl-dev
/docs/ @hummbl-dev
/README.md @hummbl-dev
/SECURITY.md @hummbl-dev
```

## 3. `hummbl-production/README.md`

Under the `Fallback CI` section, replace the two workstation-local absolute links with repo-relative links.

### Replace this line:

```md
More detail: [docs/fallback-ci.md](/Users/others/PROJECTS/hummbl-production/docs/fallback-ci.md)
```

### With this:

```md
More detail: [docs/fallback-ci.md](docs/fallback-ci.md)
```

### Replace this line:

```md
An external-hosted fallback is also scaffolded via [`.circleci/config.yml`](/Users/others/PROJECTS/hummbl-production/.circleci/config.yml) so the same checks can run even while GitHub Actions billing is locked.
```

### With this:

```md
An external-hosted fallback is also scaffolded via [`.circleci/config.yml`](.circleci/config.yml) so the same checks can run even while GitHub Actions billing is locked.
```

## Suggested Commit Messages

- `hummbl-governance`: `chore: fix dependabot configuration`
- `hummbl-production`: `docs: fix ownership and README links`
