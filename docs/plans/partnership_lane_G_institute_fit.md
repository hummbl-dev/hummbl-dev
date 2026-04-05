# Partnership Lane G: Institute-Fit Assessment

**Subject:** HUMMBL as a 2-principal "research institute that ships software"
**Date:** 2026-04-05
**Principals:** Reuben Bowlby (PI / internal), Daniel Matha (EVP / external)

---

## 1. Comparable Institute Structures

| Institute | Leadership | Revenue Model | IP Handling |
|---|---|---|---|
| **RAND Corporation** | President + board; domain VPs | FFRDC contracts, sponsored research, philanthropic grants (~$350M ARR) | Most work published; client-specific reports can be restricted. Non-profit, open-citation norm. |
| **MITRE** | CEO + FFRDC directors | Federal FFRDC contracts (DoD, IRS, FAA) (~$2B ARR) | Government-funded work is public-domain or US-gov owned. No commercial licensing. |
| **Allen Institute for AI (AI2)** | CEO + research directors under Allen Family Foundation | Foundation-funded (Paul Allen estate); minimal earned revenue | Aggressively OSS (OLMo, Semantic Scholar, AllenNLP). IP released under permissive licenses. |
| **Redwood Research** | Small exec team; research-lead-driven | Philanthropic grants (Open Philanthropy, SFF) | Publishes results openly; no commercial arm. ~20 FTE. |
| **FAR AI** | Executive Director + research leads | Philanthropic grants, some sponsored research | Open publication; occasional proprietary alignment contracts. ~15 FTE. |
| **MIRI** | Executive Director + research staff | Individual donors, foundation grants | Publication-first; technical reports, decision-theory papers. Pivoted to advocacy 2024. |
| **Santa Fe Institute** | President + VP Science + external faculty | Memberships ($50K-$500K), sponsored research, individual giving | Open publication; interdisciplinary working papers. External-faculty model. |
| **Distill (defunct)** | Editorial collective | Volunteer + Google sponsorship | Publication house only; CC-BY articles. Hiatus since 2021. |

---

## 2. HUMMBL's Closest Structural Analog(s)

**Primary analog: Santa Fe Institute + AI2 hybrid.**

- **Santa Fe Institute match:** small principal core, external-faculty orbit, interdisciplinary methodology focus (HUMMBL's 7 methodologies + 3 protocols parallel SFI's complexity-science frameworks), memberships + sponsored research revenue.
- **AI2 match:** aggressive OSS shipping (361 skills, 16 repos, PyPI governance primitives) resembles AI2's OLMo/AllenNLP posture.
- **Secondary: FAR AI.** Small principal team, methodology/safety orientation, mix of grants + sponsored contracts.

**Not a match:** RAND/MITRE (FFRDC requires federal charter, scale, decades of contract history). Redwood/MIRI (single-thesis; HUMMBL is methodology-pluralistic). Distill (publication-only; HUMMBL ships runnable software).

**Net:** HUMMBL is a **micro-SFI that ships code** — methodology institute with an OSS distribution arm.

---

## 3. Director + EVP Pattern in Research Institutes

The **PI-Director + External-EVP split is a standard and well-worn institute pattern.**

- SFI: President (currently David Krakauer, science-facing) + VP for Applied Complexity (external/industry-facing).
- AI2: CEO (Ali Farhadi, research) + COO/business development.
- FAR AI: Executive Director + separate research leads.
- RAND: President + division VPs handle client relations.

**Operating rhythm (typical):**
- PI-Director owns research agenda, publication pipeline, hiring, scientific direction.
- EVP owns fundraising, sponsor relations, client intake, partnerships, communications.
- Weekly sync on pipeline; monthly on strategy; quarterly on budget/roadmap.

**Decision authority split:**
- Research scope, methodology, publication: PI-Director (Reuben) has final say.
- Revenue deals, pricing, external commitments: EVP (Dan) leads; PI-Director has veto on scope-creep.
- Hiring, org structure, IP policy: joint; tie broken by PI-Director for research roles, EVP for commercial roles.
- Strategic pivots: joint, documented (ADR-style decision log).

**Fit for Reuben/Dan:** strong. Reuben's stated preference (lab over pitching) maps cleanly to PI-Director. Dan's external disposition maps to EVP. This is the most common stable 2-principal institute topology.

---

## 4. Partnership Viability in Institute Mode

**Are 2-principal research institutes viable?** Yes, but only at **pre-scale / incubation stage** (year 0-3). Examples:
- Distill launched with ~2 core editors + volunteers.
- Redwood Research launched 2021 with ~3 principals; now ~20.
- FAR AI launched ~2022 with 2-3 principals; now ~15.

**Critical-mass threshold:** ~3-5 FTE sustained. Below this, the institute is "2 principals + contractors/collaborators." Publication velocity caps at ~1 substantive output per principal per quarter without research staff.

**When to hire beyond principals:**
- **First research hire** when sponsored-research pipeline exceeds principal capacity (typically $300-500K committed funding).
- **First ops hire** (part-time) when admin/contracts exceed ~10 hrs/week for EVP.
- **Editorial/publication hire** when shipping cadence exceeds 1 major artifact per month.
- HUMMBL trigger: when Dan's pitch pipeline + Reuben's research pipeline both exceed ~60% of their time for 2 consecutive quarters.

**Viability verdict:** 2-principal institute is **viable for 18-36 months** with HUMMBL's IP base, contingent on reaching ~$250-400K ARR to justify principals' opportunity cost.

---

## 5. Revenue Model Feasibility (2-Principal HUMMBL)

Assumptions: Reuben 70% research / 30% delivery; Dan 70% business-dev / 30% delivery. ~1,500 billable hours/yr combined at institute-blend rate.

| Model | Mechanics | Feasibility ARR | Ranking |
|---|---|---|---|
| **Consulting (governance assessments, methodology engagements)** | $250-400/hr blended, 800 hrs billable | $200-320K | **1 (highest near-term)** |
| **Sponsored research (foundations, corporate R&D)** | 1-2 sponsors @ $75-150K each | $100-300K | **2 (highest upside)** |
| **Licensing (HUMMBL methodologies, protocols, governance primitives)** | 3-8 licensees @ $10-40K/yr | $50-200K | **3 (slow ramp, compounds)** |
| **Institutional memberships** (SFI model) | 2-5 corp members @ $25-75K | $75-250K | **4 (requires reputation moat; 18-24mo lead time)** |
| **Publication subscriptions** | Paid research reports, Substack-premium | $15-50K | **6 (low; audience-building)** |
| **Training (workshops, cohorts)** | 4-6 cohorts/yr @ $10-25K gross | $40-120K | **5 (scalable, founder-time-intensive)** |

**Recommended blend (Year 1):** Consulting (60%) + sponsored research (25%) + licensing (15%) = **$250-400K ARR target.** This matches Santa Fe / FAR AI early-stage profiles.

---

## 6. Paradigm Risks

**Top risks that kill research institutes at HUMMBL's stage:**

1. **Revenue concentration (single-sponsor risk).** If >50% of revenue comes from one client/grant, institute is one renewal away from collapse. MIRI, Redwood, and early AI2 all navigated this.
2. **Publication velocity drop.** Institutes live and die by shipped artifacts (papers, OSS, reports). Principals drowning in delivery work = zero publications = reputation decay = sponsor loss. **This is the #1 2-principal killer.**
3. **Paradigm drift back to startup mode.** Pressure to "just raise" reappears at every cash-flow pinch. Without explicit governance (written charter, board, or covenant), the institute reverts to VC-mode defaults.
4. **Founder departure.** 2-principal institutes have no redundancy. Reuben or Dan leaving = institute ends or halves. Mitigation: documented IP, external advisor bench.
5. **Grant/sponsor loss without pipeline.** EVP must maintain 3-5 active sponsor conversations at all times; single-pitch dependence is fatal.
6. **Over-indexing on shipping vs. synthesizing.** HUMMBL ships code aggressively (good); must also synthesize into citable artifacts (papers, reports) for institute credibility.

---

## 7. Transition Plan (Informal → Institute)

### What needs to change structurally
- Written **charter** declaring institute paradigm, research agenda, publication cadence.
- **Decision-rights matrix** (per Section 3 above).
- **Publication pipeline**: quarterly technical report, monthly working paper, continuous OSS.
- **Sponsor CRM** and pipeline discipline (Dan owns).
- **Revenue diversification target** (no source >50% by month 12).
- **IP policy**: default open-publication with commercial-license carve-out for governance primitives.

### What stays the same
- Stdlib-only engineering discipline.
- Multi-agent coordination bus and governance-first posture.
- OSS-default shipping (361 skills, PyPI primitives).
- LLC structure initially.

### 6-month milestones
- Charter + decision-rights doc signed.
- First institute-branded publication shipped (methodology whitepaper).
- 2 paying consulting engagements live.
- 1 sponsored-research conversation in stage-2+.
- Advisor bench of 3 named external collaborators.

### 12-month milestones
- $250K+ ARR across ≥2 revenue sources.
- 4 published artifacts (papers/reports).
- 1 signed sponsored-research agreement.
- First licensing deal closed.
- Decision on 501(c)(3) conversion (see below).

### 501(c)(3) vs stay LLC
- **Stay LLC** if: consulting + licensing dominate, <$200K grants, principals want flexibility and distributable earnings.
- **Convert to 501(c)(3)** if: sponsored research + foundation grants exceed 40% of revenue, or a major foundation requires nonprofit status. Typical trigger: first $100K+ foundation grant conditional on nonprofit status.
- **Hybrid**: LLC now; spin up 501(c)(3) affiliate at month 18-24 if grant pipeline warrants. SFI and AI2 both use foundation/nonprofit structures; FAR AI is 501(c)(3) from inception.

**Recommendation:** LLC through month 12, evaluate conversion at month 12-18 based on grant pipeline.

---

*End of assessment.*
