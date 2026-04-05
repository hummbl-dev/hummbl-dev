# AI Slop Crisis Research Corpus

**Purpose**: Evidence backbone for HUMMBL's market positioning, pitch materials, and sales conversations.

**Scope**: 5 research rounds, 12 parallel lanes, ~440K tokens of primary source analysis. Every claim is cited.

**Period**: April 2026

---

## Start here

- **For executive summary**: `06_round5_synthesis.md` (most recent, absorbs prior 4 rounds)
- **For pitch**: `capability_brief.md`, `one_pager_defense_federal.md`
- **For narrative hook**: `01_round1_37k_lines_of_slop.md`
- **For hard numbers**: `03_round3_hard_data_sweep.md`

---

## Full index

### Rounds 1-3: Foundational research (external authorship, synthesized)

| # | Doc | Role | Key content |
|---|-----|------|-------------|
| 01 | `01_round1_37k_lines_of_slop.md` | Narrative hook | 10-insight qualitative breakdown of the Scott / Ishwar Jha / GStack critique |
| 02 | `02_round2_crisis_synthesis.md` | Qualitative argument | 10 sources, tragedy-of-commons, skill atrophy, market convergence |
| 03 | `03_round3_hard_data_sweep.md` | Quantitative evidence | 14 stats, 5 named CVEs, EU AI Act specifics |

### Round 4: Self-identified gap closure (Claude Code swarm, 6 lanes)

| # | Doc | Lane |
|---|-----|------|
| 04 | `04_round4_synthesis.md` | Master synthesis |
| 04a | `04a_round4_us_regulatory.md` | US federal + state + sector + insurance |
| 04b | `04b_round4_competitive_intel.md` | 10 governance vendors + white space |
| 04c | `04c_round4_incident_harvest.md` | 17 new verified incidents + taxonomy |
| 04d | `04d_round4_devsecops_analogue.md` | Historical timing pattern |
| 04e | `04e_round4_mcp_wedge.md` | MCP governance wedge validation |
| 04f | `04f_round4_enterprise_spend.md` | TAM + pricing + buyers |

### Round 5: Reviewer-identified gap closure (Sonnet-flagged, 6 lanes)

| # | Doc | Lane |
|---|-----|------|
| 05a | `05a_round5_primary_sources.md` | METR, Baltes, Stanford, Apiiro, Sonar verified |
| 05b | `05b_round5_steelman_roi.md` | Pro-AI case + anti-governance steelman |
| 05c | `05c_round5_legal_liability.md` | Liability chain + Moffatt + Mobley |
| 05d | `05d_round5_observability_analogue.md` | Pre-Datadog → post-Datadog fully developed |
| 05e | `05e_round5_regulated_verticals.md` | Healthcare + finance + defense compound |
| 05f | `05f_round5_buyer_hiring_benchmarks.md` | CTO/CISO voice + labor shifts + SWE-bench inversion |
| 06 | `06_round5_synthesis.md` | Master synthesis |

### Derived artifacts

| Doc | Purpose |
|-----|---------|
| `capability_brief.md` | HUMMBL capability brief — single-doc pitch reference |
| `one_pager_defense_federal.md` | Positioning one-pager for defense / federal buyers (primary wedge) |

---

## Top 10 cite-ready findings

1. **42% of code is AI-generated** (Sonar 2026 survey, n=1,100+)
2. **AI code is 2.74× more vulnerable** than human-written (Veracode 2025)
3. **Security pass rate stuck at ~55% for 2 years** despite model improvement (Veracode Spring 2026)
4. **25.1% of AI code samples had confirmed vulnerabilities** (AppSec Santa, 6 LLMs, 534 samples)
5. **SWE-bench is inverted**: Claude Opus 4.6 = 79.3% Verified but 29.2% vulnerable; GPT-5.2 = 19.1% vulnerable
6. **METR RCT**: experienced devs 19% SLOWER with AI, believe they're 20% faster (arxiv 2507.09089)
7. **Moffatt v. Air Canada**: deploying company eats AI chatbot liability
8. **Mobley v. Workday**: vendor-as-agent liability theory certified July 2025
9. **EU AI Act Aug 2 2026**: €35M / 7% global revenue penalties, enforcement live in Finland since Jan 2026
10. **Berkley absolute AI exclusions**: no D&O/E&O coverage for AI-related claims → insurance as de-facto enforcement

---

## Strongest single positioning lines

**For ROI skeptics**: *"Concede the 40-60% greenfield/junior gain. Governance is about what an agent is allowed to do, not whether it codes correctly. A perfectly-aligned agent with unlimited authority is still a catastrophic-blast-radius risk."*

**For legal/GC**: *"Signed delegation tokens and append-only audit logs are a Caremark affirmative defense, a NIST AI RMF conformance record, and a reasonable-care evidence pack, generated at runtime, not reconstructed after the breach."*

**For defense/federal CISOs**: *"Commercial AI governance SaaS cannot touch IL4/IL5. HUMMBL deploys where your classified workloads deploy — stdlib-only, air-gap capable, contract-driven, and readable by your CMMC assessor."*

**For pitch decks**: *"AI generation is commoditizing. Every vendor will have it. Differentiation accrues to the layer that governs output quality, enforces policy, tracks provenance, and maintains accountability. This is the observability argument applied to AI."*

---

## Methodology notes

- All primary-source citations verified in Round 5 Lane G
- 2 citations corrected in Rounds 1-3 based on verification (see `06_round5_synthesis.md` Part I)
- Research production: Claude Opus 4.6 (Claude Code) orchestrating 12 parallel general-purpose research agents
- Research authorship: Claude Sonnet 4.6 extended (via claude.ai browser) for Rounds 1-3; Claude Opus 4.6 with swarm agents for Rounds 4-5

---

*Last updated: 2026-04-05. Next review: quarterly, or when EU AI Act Aug 2 2026 enforcement begins.*
