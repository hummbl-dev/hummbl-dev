# B0 Governance Propagation Factory — Receipt

**Date**: 2026-06-20  
**Agent**: devin  
**Scope**: hummbl-dev greenfield + near-greenfield repos  
**Mode**: B0 dry-run only (no mutations)  

---

## 1. What Was Done

Built an idempotent, operator-reviewable governance propagation mechanism consisting of:

1. **`manifest.json`** — 25 repo candidates (13 greenfield + 12 near-greenfield) with metadata
2. **`templates/`** — Canonical governance files copied from `hummbl-dev/hummbl-dev`:
   - `LICENSE` (Apache 2.0)
   - `SECURITY.md`
   - `CODEOWNERS`
   - `CONTRIBUTING.md`
   - `AGENTS.md`
   - `.github/PULL_REQUEST_TEMPLATE.md`
   - `.github/ISSUE_TEMPLATE/bug-report.md`
   - `.github/ISSUE_TEMPLATE/content-correction.md`
3. **`govern.py`** — Reusable dry-run script that:
   - Reads the manifest
   - Queries each repo via GitHub API for existing governance files
   - Compares against templates
   - Generates a markdown report
   - Default mode is `--dry-run`; `--apply` is blocked in B0
4. **`reports/dry-run-report.md`** — Full per-repo breakdown

---

## 2. Key Findings

| Metric | Value |
|--------|-------|
| Repos checked | 25 |
| Needs governance (missing required files) | 25 |
| Partial (optional files absent) | 0 |
| Complete | 0 |
| Missing/inaccessible | 0 |

**Universal gaps**: Every repo in the manifest is missing:
- `CODEOWNERS`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/bug-report.md`
- `.github/ISSUE_TEMPLATE/content-correction.md`

**Optional gaps**: ~20 repos also missing `AGENTS.md` (flagged as optional, not required)

**Existing files detected**: Many repos already have `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md` — the script correctly identifies these as present and does not flag them.

---

## 3. Assumptions

1. **Canonical source**: `hummbl-dev/hummbl-dev` is the governance template source of truth.
2. **License**: Apache 2.0 is the fleet-default and applies uniformly across hummbl-dev repos.
3. **CODEOWNERS**: `* reuben@hummbl.io` is the correct default for all repos.
4. **AGENTS.md is optional**: Not all repos need agent guidance (e.g., documentation-only repos).
5. **GitHub API access**: `gh` CLI is authenticated and has read access to all repos in the org.
6. **No README generation**: README is explicitly out of scope per operator directive (governance files only).

---

## 4. Constraints Honored

| Constraint | Status |
|------------|--------|
| Default mode is `--dry-run` | ✅ `govern.py` defaults to dry-run; `--apply` returns error in B0 |
| Do not mutate external repos | ✅ Zero mutations to any hummbl-dev repo |
| Do not create PRs | ✅ No PRs created |
| Do not commit directly to main | ✅ No commits made |
| Do not overwrite existing files | ✅ Script treats existing files as authoritative |
| Do not infer/change licenses without approval | ✅ License copied verbatim from canonical; no changes |
| Only governance files | ✅ Scope limited to LICENSE, SECURITY, CODEOWNERS, CONTRIBUTING, AGENTS, .github templates |
| Use manifest, not hardcoded logic | ✅ `manifest.json` is the single source of repo list |
| Treat existing governance as authoritative | ✅ Present files are skipped, not overwritten |

---

## 5. Next Steps (B1 → Operator Decision)

1. **Review the dry-run report** at `governance/batch-propagation/reports/dry-run-report.md`
2. **Decide on LICENSE**: The script assumes Apache 2.0 for all repos. If any repo needs a different license, flag it before application.
3. **Decide on AGENTS.md**: Should optional AGENTS.md be promoted to required? The script treats it as optional.
4. **Operator approval**: Once approved, the operator can:
   - Run `govern.py` with `--apply` (when implemented in B1)
   - Use the report to manually add files via GitHub UI
   - Run a separate script that uses `gh api` to create files
5. **Batch application strategy**: Suggest 3 batches:
   - Batch 1: Public high-impact repos (`hummbl-kernel-factory`, `founder-mode-showcase`, `evidence-gate`, `krineia`, `hummbl-skills`)
   - Batch 2: Public medium-impact repos
   - Batch 3: Private repos

---

## 6. Files Changed in Controlling Repo

All changes are within `hummbl-dev/hummbl-dev` (this repo):

```
governance/batch-propagation/
  manifest.json                              # 25-repo manifest
  govern.py                                  # Dry-run script
  RECEIPT.md                                 # This file
  templates/
    LICENSE                                  # Canonical Apache 2.0
    SECURITY.md                              # Canonical security policy
    CODEOWNERS                               # Canonical ownership
    CONTRIBUTING.md                          # Canonical contribution guide
    AGENTS.md                                # Canonical agent guidance
    .github/
      PULL_REQUEST_TEMPLATE.md             # Canonical PR template
      ISSUE_TEMPLATE/
        bug-report.md                        # Canonical bug template
        content-correction.md              # Canonical content template
  reports/
    dry-run-report.md                        # Generated report
```

---

**Receipt generated by**: devin  
**Receipt hash**: B0-2026-06-20-governance-propagation  
**Scope locked**: No external repo mutations performed  
**Bus receipt**: To be posted upon commit
