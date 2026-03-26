# State of Repos | 2026-03-26

**Orgs**: hummbl-dev (26 active + 37 archived = 63), foundermode-ai (3 private)
**Total**: 66 repos (29 active, 37 archived)

## Summary

| Metric | Value |
|--------|-------|
| Active repos | 29 (26 hummbl-dev + 3 foundermode-ai) |
| Archived repos | 37 (all hummbl-dev) |
| CI green | 20/29 active |
| CI failing | 3 (governed-iac-reference, mcp-server Node 18, hummbl-production alerts only) |
| Open PRs | 2 active + 30 on archived repos |
| Dependabot alerts | 13 (11 hummbl-production, 2 founder-mode) |
| Repos with branch protection | 10 (all Tier 1) |

---

## Tier 1: Core Product (10 repos)

These repos are actively developed, have CI, and are standardized with branch protection + Dependabot + secret scanning.

| Repo | Visibility | CI | PRs | Alerts | Arbiter | Notes |
|------|:----------:|:--:|:---:|:------:|:-------:|-------|
| **founder-mode** | Private | GREEN | 1 | 2 | - | v0.3.0-dev. 7,700+ tests, 14 workflows. The platform. PR #230 (convergence suite). |
| **foundermode-app** | Private | GREEN | 0 | 0 | - | iOS coaching app. SENSE→Body/Mind/Drive/Fuel. Apr 2 TestFlight deadline. |
| **hummbl-production** | Private | GREEN | 0 | 11 | - | Cloudflare Pages + Workers. hummbl.io live with brand v2. 26 pages + API. Alerts are new (just enabled Dependabot). |
| **hummbl-governance** | Public | GREEN | 0 | 0 | A (99.5) | PyPI published. 20 modules, 476 tests, stdlib-only. Lint fixed today. |
| **hummbl-agent** | Public | GREEN | 0 | 0 | A (95.4) | Agent orchestration. 195 skills, 37-step CI. OpenClaw→HUMMBL migration done today. |
| **base120** | Public | GREEN | 0 | 0 | - | v1.0.0 reference. 120 mental models. 11 governance workflows. |
| **mcp-server** | Public | FAIL | 0 | 0 | A (100) | npm @hummbl/mcp-server. TypeScript strict. 195 tests. Node 18 CI matrix fails (`styleText` requires Node 22+). Node 20+ passes. |
| **arbiter** | Public | GREEN | 0 | 0 | A (98.0) | Code quality scoring. Report generator merged today. |
| **governed-iac-reference** | Public | FAIL | 0 | 0 | - | IaC reference. Dependabot Updates workflow failing (not main CI). Checkov/Trivy dep bumps merged today. |
| **hummbl-assurance** | Public | GREEN | 0 | 0 | - | Governance assurance. AAA→HUMMBL rebrand merged today. |

### Tier 1 Actions Needed
- [ ] Fix mcp-server Node 18 CI failure (drop Node 18 from matrix or pin dep)
- [ ] Fix governed-iac-reference Dependabot Updates workflow
- [ ] Address 11 new Dependabot alerts on hummbl-production
- [ ] Address 2 Dependabot alerts on founder-mode
- [ ] Merge or close founder-mode PR #230 (convergence suite — may have conflicts)

---

## Tier 2: Supporting Repos (8 repos)

Active, public, serve a specific purpose but not core product. No CI governance standardization yet.

| Repo | Visibility | CI | PRs | Last Updated | Purpose |
|------|:----------:|:--:|:---:|:------------:|---------|
| **HUMMBL-Unified-Tier-Framework** | Public | GREEN | 0 | Mar 25 | Problem complexity classification (5 tiers). Standardized today. |
| **agent-governance-demo** | Public | GREEN | 0 | Mar 25 | Standalone demo of hummbl-governance. 58 tests. |
| **bif** | Public | - | 0 | Mar 25 | Batch Ingestion Framework. Knowledge acquisition methodology. |
| **hummbl-bibliography** | Public | GREEN | 1 | Mar 24 | Research bibliography. 1 open PR. |
| **autoresearch-reports** | Public | - | 0 | Mar 24 | Research pipeline outputs. |
| **swarm-test** (foundermode-ai) | Private | - | 0 | Mar 25 | 15 experiments, tmux dispatch, Crucible-aware. |
| **hummbl-dev** | Public | - | 0 | Mar 24 | Org profile + dashboard + governance tools. Rebranded today. |
| **hummbl-cca-f** | Private | - | 0 | Mar 25 | CCA-F certification prep. |

### Tier 2 Actions Needed
- [ ] Merge hummbl-bibliography PR
- [ ] Consider archiving bif and autoresearch-reports if no longer active

---

## Tier 3: Utility / Inactive (11 active, not archived)

These repos exist but aren't actively developed. Candidates for archival.

| Repo | Visibility | Last Updated | Status | Recommendation |
|------|:----------:|:------------:|--------|----------------|
| agent-os | Public | Mar 22 | No description | **Archive** |
| autoresearch-pipeline | Private | Mar 17 | NemoClaw research | **Archive** (superseded by research-pipeline) |
| autoresearch-win-rtx | Public | Mar 24 | GPU research runner | **Keep** if Windows desktop active |
| base120-corpus-validator | Public | Mar 11 | Declaration only | **Archive** |
| caes-tools | Private | Mar 23 | No description | **Archive** or merge into governance |
| claude-code-folder | Private | Mar 24 | Claude workspace | **Keep** (active config) |
| codex-agent-folder | Public | Feb 8 | Stale | **Archive** |
| hummbl-agent-federation | Public | Feb 15 | Stale | **Archive** |
| hummbl-claude-skills | Public | Mar 7 | Superseded by .claude/skills | **Archive** |
| hummbl-infra | Public | Feb 7 | Stale | **Archive** |
| meeting-archive | Private | Mar 25 | Meeting transcripts | **Keep** (private records) |

### Tier 3 Actions Needed
- [ ] Archive 7 stale repos: agent-os, autoresearch-pipeline, base120-corpus-validator, caes-tools, codex-agent-folder, hummbl-agent-federation, hummbl-claude-skills
- [ ] Review hummbl-infra — archive if unused

---

## Tier 4: Archived (37 repos)

Already archived. No action needed. Notable archived repos with stale open PRs:

| Repo | Open PRs | Notes |
|------|:--------:|-------|
| hummbl-monorepo | 16 | Legacy monorepo. PRs are stale dependabot. |
| engine-ops | 10 | Engine optimization. Stale PRs. |
| hummbl-research | 1 | Research repo. CI failing. |
| shared-hummbl-space | 1 | Shared agent space. |
| gastown | 1 | Multi-agent workspace. |
| games | 1 | Logic games. |
| sys-arch-testing | 1 | Architecture testing. |
| claude-code-infrastructure-showcase | 1 | Showcase repo. |
| OpenAgent | 1 | Web3 AI agent (private). |

*Archived repos with open PRs cannot be merged — PRs should be closed if the repo is archived.*

---

## foundermode-ai Org (3 repos)

| Repo | Visibility | CI | PRs | Alerts | Notes |
|------|:----------:|:--:|:---:|:------:|-------|
| **founder-mode** | Private | GREEN | 1 | 2 | Main platform. Listed in Tier 1 above. |
| **foundermode-app** | Private | GREEN | 0 | 0 | iOS app. Dan's active project. |
| **swarm-test** | Private | - | 0 | 0 | Experiment platform. |

---

## Governance Tooling Status

| Feature | Tier 1 (10) | Tier 2 (8) | Tier 3 (11) |
|---------|:-----------:|:----------:|:-----------:|
| Branch protection | 10/10 | 0/8 | 0/11 |
| Dependabot alerts | 10/10 | 1/8 | 0/11 |
| Secret scanning | 9/10 | varies | varies |
| Push protection | 9/10 | varies | varies |
| CodeQL | 0/10 (removed) | 0/8 | 0/11 |
| CI workflows | 10/10 | 3/8 | 0/11 |

---

## Brand v2 Status

| Asset | Status |
|-------|--------|
| hummbl.io (30 pages) | LIVE — brand v2 deployed |
| hummbl-dev/dashboard.html | Rebranded, committed |
| hummbl-dev governance tools (7 HTML) | Rebranded, committed |
| PRINT_PACKAGE.html | Rebranded, committed |
| Newsletter/Linktree specs | Updated |
| Frontend skill CSS tokens | Updated |
| Old colors (#0a0a0a, #00ff88) | Zero references remaining |

---

## Priority Actions (next session)

1. **Fix mcp-server CI** — drop Node 18 from matrix (EOL Oct 2025, `styleText` requires 22+)
2. **Fix governed-iac-reference** — Dependabot Updates workflow failing
3. **Address 13 Dependabot alerts** (11 hummbl-production, 2 founder-mode)
4. **Archive 7+ stale Tier 3 repos** — reduce maintenance surface from 29 to ~22 active
5. **Close 30 stale PRs on archived repos** — can't merge on archived repos, just close
6. **Resolve founder-mode PR #230** — convergence suite, may need rebase or close+re-land

---

*Generated by Claude Opus 4.6 (apex) | 2026-03-26T14:30Z*
