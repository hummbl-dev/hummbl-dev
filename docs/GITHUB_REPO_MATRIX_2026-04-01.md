# GitHub Repo Matrix - 2026-04-01

This matrix summarizes the core HUMMBL repositories reviewed in the repo-by-repo governance pass.

| Repo | README | SECURITY | CODEOWNERS | Dependabot | Notes |
|---|---|---|---|---|---|
| `base120` | Yes | Yes | Yes | Yes | Strongest governance posture; open CI/governance issues still need closure |
| `hummbl-governance` | Yes | Yes | Yes | Present but stale/broken | Repo-local CODEOWNERS added; existing Dependabot file still needs in-place correction |
| `mcp-server` | Yes | Yes | Yes | Yes | Healthy baseline; active dependency PR volume should be managed |
| `hummbl-agent` | Yes | Yes | Yes | Yes | Healthy baseline; strong repo-local security guidance |
| `hummbl-assurance` | Yes | Added | Added | Added | Core file gaps closed in this pass |
| `hummbl-production` | Yes | Yes | Yes but stale owner | Yes | README has workstation-local absolute links; CODEOWNERS should be corrected in place |
| `hummbl-iac` | Yes | Added | Added | Added | Core file gaps closed in this pass |
| `.github` | Yes | Yes | Added | No | Now provides org-level defaults for repos without local overrides |
| `hummbl-dev` | Yes | Inherits org default | Inherits org default | N/A | Tracks account-level audit actions and repo matrix |

## Remaining Manual or Settings-Level Work

### GitHub settings
- Apply branch protection or rulesets on core repos
- Normalize default branch names where still inconsistent
- Standardize merge strategy on core repos

### In-place file edits still needed
- `hummbl-governance/.github/dependabot.yml` should be replaced with a valid config
- `hummbl-production/.github/CODEOWNERS` should stop pointing at `@rpbxbt`
- `hummbl-production/README.md` should replace absolute local filesystem links with repo-relative links

### Portfolio cleanup
- Review low-signal repos for archival, privatization, or consolidation
- Keep the public account aligned with the canonical HUMMBL story in the profile repo
