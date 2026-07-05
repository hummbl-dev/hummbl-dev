# Click-Path Audit — 2026-07-04

Simulated first-time visitor click path through the HUMMBL public fleet.

## Click path tested

1. GitHub org profile → `profile/README.md`
2. `hummbl-dev/hummbl-dev` → `README.md`
3. `START_HERE.md`
4. `docs/contributor-paths.md`
5. `docs/repo-map.md`
6. `docs/REPO_MATURITY_MODEL.md`
7. `.github/CONTRIBUTING.md` (org-level)
8. v0.1-packet repo (`agent-runtime-governance`) → `README.md` → `docs/v0.1-boundary.md`
9. Starter issue (`agent-runtime-governance#5`)

## Results

### Step 1: GitHub org profile — PASS

Org profile README is clear, explains HUMMBL, lists canonical projects, has FAQ. Test count verified at 2027. Links to PyPI and hummbl.io.

### Step 2: hummbl-dev/hummbl-dev README — PASS

90-second overview is clear. Start Here table routes by need. Repository Directory matches repo-map.md. Pending decisions section visible. 41 active public repos count is accurate.

### Step 3: START_HERE.md — PASS

90-second pitch is concise. Pick-your-path table covers 6 contributor types. What-not-to-touch section calls out pending decisions. All internal links verified working.

### Step 4: docs/contributor-paths.md — PASS

Expanded contributor type routing with good first contributions per path. Agent CAN/CANNOT section is clear. Triage link works.

### Step 5: docs/repo-map.md — PASS

Full fleet classification with maturity, surface type, contributor readiness. Dependency graph is accurate. Pending decision surfaces called out.

### Step 6: docs/REPO_MATURITY_MODEL.md — PASS

Maturity levels, surface types, contributor readiness, promotion path all defined. Clear and self-consistent.

### Step 7: .github/CONTRIBUTING.md — PASS

Expanded with contributor type table, repo maturity, agent CAN/CANNOT lists, operator authority section, receipts section. Links to FLEET_LABELS.md.

### Step 8: v0.1-packet repo (agent-runtime-governance) — FAIL

**Issue found:** README.md contains `$(System.Collections.Hashtable.Name)` — a PowerShell template artifact that was never resolved. This appears as literal broken text to visitors.

**Scope:** 10 of 13 v0.1-packet repos have this broken token:
- agent-control-plane-patterns
- agent-instruction-format
- agent-runtime-governance
- agentic-eng-patterns
- ai-source-verification
- execution-receipts
- agent-evaluation-patterns
- agent-handoffs
- claim-evidence-ledger
- research-source-packets

**Fix:** PRs created to replace the token with proper display names.

The `docs/v0.1-boundary.md` file is clean and well-structured.

### Step 9: Starter issue (agent-runtime-governance#5) — PASS

Issue is labeled `good-first-issue`, `external-collab-ready`, `agent-safe`. Definition of done includes the required constraints (no canon, no new terminology, no operator-authority changes, receipt required). Links to CONTRIBUTING.md.

## Link integrity

All internal links in START_HERE.md, README.md, and contributor-paths.md verified via GitHub API. All repo links resolve to existing repos. One directory link (`docs/plans/`) resolves to a valid directory.

## Jargon cliffs

| Term | Where | Risk level | Recommendation |
|---|---|---|---|
| `$(System.Collections.Hashtable.Name)` | 10 repo READMEs | HIGH — broken text | Fix in progress (PRs created) |
| "governance primitives" | README, START_HERE | LOW — explained in context | OK |
| "mental-model substrate" | README, START_HERE | LOW — explained in context | OK |
| "v0.1-packet" | START_HERE, repo-map, maturity model | LOW — defined in REPO_MATURITY_MODEL.md | OK |
| "non-canon posture" | v0.1-boundary docs | LOW — explained in context | OK |

## Authority boundaries

- CONTRIBUTING.md clearly states what agents CAN and CANNOT do
- START_HERE.md "What not to touch yet" section calls out pending decisions
- FLEET_REMAINING_ISSUES_2026-07-04.md triages all open issues by bucket
- Starter issues include "Does not modify operator-authority surfaces" in definition of done

## Overall verdict

**NEEDS ONE FIX** — The broken PowerShell template token in 10 repo READMEs is the only blocking issue. PRs are being created to fix this. Once merged, the fleet is **READY** for external collaboration.

## Recommendations

1. **Fix the broken template tokens** (in progress)
2. **Enable Discussions on more repos** — only 5 of 41 repos have Discussions enabled
3. **Add `good-first-issue` label to org-level defaults** — currently created per-repo
4. **Consider a glossary** — terms like "governance primitives" are explained in context but a central glossary would help
5. **Monitor the 5 Discussions** — respond to first comments promptly to set the tone
