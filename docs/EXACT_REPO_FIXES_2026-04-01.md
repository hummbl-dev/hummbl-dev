# Exact Repo Fixes - 2026-04-01

This file contains exact replacement content for the remaining existing-file fixes identified in the audit.

## 1. `hummbl-governance/.github/dependabot.yml` ✅ APPLIED

**Status:** Already fixed in commit `c620ec4` (2026-04-01).

Current file is valid. Replacement was:

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

## 2. `hummbl-production/.github/CODEOWNERS` ✅ APPLIED

**Status:** Fixed in branch `fix/claude/gitops-cleanup-from-april-audit` (commit `763455b`, 2026-06-17).

Replaced stale `@rpbxbt` with `@hummbl-dev` + product surface rules. Replacement was:

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

## 3. `hummbl-production/README.md` ✅ ALREADY CLEAN

**Status:** No action needed. Current README already uses repo-relative links (`docs/fallback-ci.md`).

**Additional fixes applied (not in original audit):**
- `scripts/render_papers_as_content.py`: Replaced absolute `/Users/others/...` paths with repo-relative `Path(__file__).resolve().parents[1] / ...`
- `content/_BRAND_GUIDE.md`: Replaced two absolute `/Users/others/PROJECTS/hummbl-production/web/shared.css` references with repo-relative `web/shared.css`

## Suggested Commit Messages

- `hummbl-governance`: `chore: fix dependabot configuration`
- `hummbl-production`: `docs: fix ownership and README links`
