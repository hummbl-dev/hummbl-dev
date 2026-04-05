# HUMMBL Partnership Synthesis — Reuben + Dan
### 7-lane brainstorm unified into decision document
### Date: 2026-04-05

> Parallel agent team (legal architecture, IP ownership, equity+comp, operating
> model, meeting prep, product portfolio, institute fit) converged on a
> consistent recommendation. This doc is the synthesis — what to do, what to
> decide in the meeting, and what needs attorney review.

---

## TL;DR — the recommended structure

| Layer | Recommendation |
|-------|---------------|
| **Legal entity** | New Georgia **Umbrella LLC** as holding company (Option A) — owned by Reuben + Dan, neither existing entity dissolves |
| **Interim (6-12 mo)** | **Joint Venture contract** between HUMMBL LLC and Dan's S-Corp as bridge before umbrella |
| **Equity split** | **75% Reuben / 25% Dan** with ±10% dynamic adjustment band, freezes at $250K revenue or Dec 31 2027 |
| **Vesting** | 1-year cliff, milestone-based ($50K/$150K/$300K BD-sourced revenue) + tenure |
| **Comp** | Hybrid: cross-entity invoicing (Reuben $225/hr, Dan $200/hr) + 15% BD revenue share for Dan |
| **Back-pay** | **Document Reuben's deferred-comp ledger BEFORE any equity issuance to Dan** — non-negotiable |
| **Operating model** | Domain vetoes + joint sign-off on shared products + standing external advisor for deadlocks |
| **Institute analog** | Santa Fe Institute + AI2 hybrid — Director (Reuben) + EVP (Dan) is standard |

---

## Cross-lane convergence (where all 7 agreed)

1. **Umbrella LLC is the destination, JV is the bridge.** All lanes point to eventual holding-company structure, but don't form umbrella prematurely.

2. **IP needs immediate formal assignment — before anything else.** Reuben's pre-existing IP (Founder Mode, governance primitives, methodologies, 300+ docs) must be carved out explicitly as owned by HUMMBL LLC before Dan gets any equity in a shared entity. Without this, Dan's equity grant could dilute Reuben's sweat equity.

3. **Reuben's underpayment is a structural liability, not a grievance.** Back-pay must be a balance-sheet line item with dollar value and vesting BEFORE equity conversations close. Every lane independently flagged this.

4. **Director + EVP is the right role split.** Reuben holds scientific/research authority, Dan holds organizational/BD authority. This is standard in the 8+ research institutes surveyed (SFI, AI2, FAR AI, RAND, MIRI, etc.)

5. **Bidirectional SSH work is fine — it doesn't confer IP.** Hosting infrastructure doesn't create co-ownership. Reuben working on Dan's machine engineering JSR does not make HUMMBL a JSR owner. Reuben's contributions = license + contributor credit, not ownership.

6. **75/25 is the defensible split.** Reuben's pre-partnership IP floor (14,400+ tests, 300+ research docs, ~2 years solo work, shipped PyPI package) sets the baseline. 70-80% for the solo-builder predecessor is the standard in multi-entity research partnerships. Dan's 25% vests on BD-sourced revenue, not pure tenure.

7. **Publication velocity is the institute's existential metric.** 2-principal research institutes fail when research output drops. Without a publication calendar + delivery discipline, the institute drifts back to startup-mode or dissolves.

---

## Points of tension between lanes

### Tension 1: When to form the umbrella LLC

- **Lane A (Legal)**: form it as the primary structure, $1-3K setup
- **Lane F (Product Portfolio)**: "form only when joint ARR exceeds ~$150K" — delay it

**Resolution**: Form the JV contract NOW (cheap, fast, establishes IP baseline). Upgrade to umbrella LLC when EITHER (a) joint product ARR crosses $150K, OR (b) first institutional sponsor demands single-counterparty contracting, OR (c) Reuben+Dan agree timing is right. Not a sequencing question — a trigger-based upgrade.

### Tension 2: JSR ownership

- **Lane B (IP)**: Dan owns IP (he originated), Reuben gets perpetual license + contributor credit
- **Lane F (Products)**: Dan's S-Corp owns trademark/brand, Reuben holds 20-30% rev-share while maintaining

**Resolution**: These are compatible — IP ownership (Dan) + revenue-share agreement (Reuben 20-30%) is one arrangement expressed two ways. Reuben's license to his own engineering contributions is implicit in the rev-share contract.

### Tension 3: How to treat Reuben's Claude-code-harness engineering

- **Lane B**: infrastructure hosting doesn't confer IP — Reuben's harness on Dan's machine still belongs to Reuben/HUMMBL
- **Lane D**: SSH access is mutual and documented via per-repo `authorized_keys` manifests

**Resolution**: Both. Reuben retains IP in his harness. Operational access is mutual and documented. These are orthogonal concerns (ownership vs access).

---

## What MUST be decided in the Reuben+Dan meeting

Per Lane E, these are the 5 must-decide-today items with anti-postponement mechanisms:

| # | Decision | Default if stuck | Time-box |
|---|----------|-----------------|----------|
| 1 | **Equity split percentage** (75/25 recommended, ±10%) | Provisional 75/25 for 90 days, revisit Jul 5 | 30 min |
| 2 | **Monthly comp floor** for each principal | $5K/mo Reuben, $X/mo Dan (Dan states) | 20 min |
| 3 | **IP rule** for pre-partnership work (carve-out) | All pre-2026-04-05 IP carved out by owner entity | 15 min |
| 4 | **Tiebreaker mechanism** for deadlocks | External advisor (attorney or fractional CFO) | 15 min |
| 5 | **Entity direction** — JV contract now or Umbrella LLC now? | JV contract, $1-3K, 2 weeks | 20 min |

**Second-tier decisions** (defer ≤14 days if not resolvable):
- Dan's specific title (EVP, CBO, Co-Director, President?)
- Exact BD-revenue-share percentage (15% vs 10% vs 20%)
- Product-by-product ownership for current + future products
- Standing advisor identity and retainer

**Third-tier decisions** (defer to Q2-Q3 2026):
- 501(c)(3) conversion path
- Sponsored-research formal structure
- Institutional membership pricing

---

## The top 5 reverse-prompts for the meeting (from Lane E)

1. *"List every piece of IP you personally brought into this partnership. Don't edit."* (Paired with *"List what the OTHER person brought in. Be generous."*) — forces factual baseline before negotiation.

2. *"What's the minimum monthly comp you need to stop subsidizing this company personally?"* — names the underpayment without grievance framing.

3. *"What equity split feels fair to you right now? Say the number. Explain the reasoning."* — forces both to commit a number simultaneously.

4. *"If we don't agree on equity today, what's our fallback mechanism?"* — prevents meeting from becoming another postponement.

5. *"What's the thing you've been holding back saying about our partnership?"* — surfaces resentment early.

**Biggest emotional landmine to disarm first**: Reuben's underpayment frustration colliding with Dan's pre-existing JSR ownership. Name both facts in the opening, treat Reuben's back-pay as a line item (not a moral claim), disclose JSR's status as a factual baseline (not a judgment).

---

## Non-negotiable deal breakers (from Lane C)

These clauses MUST be in whatever agreement is signed:

1. **Pre-partnership IP carve-out with explicit exclusion dated 2026-04-05** — All Reuben's existing IP (Founder Mode, governance primitives, methodologies, research corpus) explicitly excluded from any assignment to a new entity. Without this, Dan could later claim rights to pre-existing HUMMBL platform.

2. **Documented deferred-comp ledger BEFORE equity issuance to Dan** — Reuben's accrued underpayment (hours × $225 − cash received since 2024) must be a signed, balance-sheet liability before Dan's equity grants. Otherwise Dan's equity dilutes Reuben's unrecovered contribution.

3. **"Anything we build together" language must be bounded** — replace with per-product one-page term sheets before work begins. Future-IP assignment with no scope is court-disfavored.

---

## Attorney consultation prep

**Top 3 questions for Georgia business attorney**:

1. Can Dan hold Umbrella LLC membership interest individually vs through his S-Corp — what are the tax and passive-income consequences of each path?

2. Draft a **profits-interest grant** (Rev. Proc. 93-27 safe harbor) for Dan in the Umbrella LLC, plus a mutual IP assignment covering prior joint work (Peptide Checker, JSR, Founder Mode) without triggering §721 contribution issues.

3. For research-institute mode, can the Umbrella LLC enter sponsored research agreements, hold publication rights, and spawn a 501(c)(3) affiliate for grant eligibility without tainting the LLC?

**Critical prerequisites for attorney**:
- Dan's state of residence + S-Corp state of domicile
- Documented back-pay ledger (amount + time period)
- Preliminary equity split (75/25)
- List of existing IP assets by entity

**Estimated legal cost**: $2-5K for Operating Agreement + IP assignments + profits-interest grant + JV contract.

---

## Next actions

### This week (no lawyer needed)

1. **Reuben reads this synthesis + all 7 lane briefs** (in `~/Downloads/partnership_lane_*.md`)
2. **Reuben computes back-pay ledger**: hours worked on HUMMBL × $225/hr − cash received since entity formation. This is a concrete dollar number.
3. **Reuben schedules 2-hour meeting with Dan** — use Lane E framework
4. **Dan reads synthesis before meeting** (share this doc)
5. **Pre-meeting: Reuben + Dan each write** their IP contribution list independently

### In-meeting (2 hours, Reuben + Dan)

6. **Execute Lane E framework** — reverse-prompting facilitated session
7. **Decide 5 must-decide items** (equity split, comp floor, IP rule, tiebreaker, JV vs Umbrella)
8. **Name decisions in writing** — each principal signs meeting summary
9. **Schedule attorney consultation** within 14 days

### Week 2-3 (professional support)

10. **Attorney consultation** (~2 hours, $500-1K) with top-3 questions
11. **Draft JV contract** (if JV-first) or **Umbrella LLC Operating Agreement** (if umbrella-first)
12. **IP assignment documents** signed between entities
13. **Deferred-comp ledger** formalized and signed

### Month 2+ (ops + sustain)

14. **Begin monthly partner ops review** (per Lane D)
15. **Quarterly partnership review** with external advisor
16. **Publication calendar committed** (institute velocity = existential)
17. **Revenue diversification tracked** — no single source >50% of revenue

---

## Paradigm fit check (from Lane G)

**HUMMBL closest analog**: Santa Fe Institute + Allen Institute for AI hybrid.
- SFI match: methodology-pluralistic micro-institute with external-faculty orbit
- AI2 match: ship-code-openly, OSS-distribution-first posture
- FAR AI match: closest 2-principal-stage living peer

**Director + EVP pattern**: standard, well-worn in SFI/AI2/FAR AI/RAND.

**Institute-mode viability**: 2-principal research institutes are viable at early stage. Critical-mass threshold: ~3-4 principals OR $500K ARR. Hire first research FTE when sponsored pipeline > $300-500K committed.

**Target by month 12**: $250-400K ARR — 60% consulting + 25% sponsored research + 15% licensing. 4 published artifacts minimum. First sponsored-research agreement signed.

**Top 2 paradigm risks**:
1. **Publication velocity collapse** — delivery work drowns out synthesis
2. **Revenue concentration + paradigm drift back to startup mode**

---

## What didn't get brainstormed (deferred to future sessions)

- Dan's S-Corp state of domicile (affects legal options — answer before attorney meeting)
- Specific insurance structure (D&O, E&O, cyber — Berkley AI exclusions research done but not applied here)
- Founder Mode pricing model details (beyond institute-tier recommendations)
- Peptide Checker medical regulatory path (HIPAA / FDA device classification — requires specialist)
- Hiring plan beyond 2 principals (when, who, budget)
- International tax implications (if sponsored research crosses borders)

---

## Lane briefs — files for deep reference

| Lane | Focus | File |
|------|-------|------|
| A | Legal Architecture | `~/Downloads/partnership_lane_A_legal_architecture.md` |
| B | IP Ownership Mapping | `~/Downloads/partnership_lane_B_ip_ownership.md` |
| C | Equity + Compensation | `~/Downloads/partnership_lane_C_equity_comp.md` |
| D | Operating Model | `~/Downloads/partnership_lane_D_operating_model.md` |
| E | Meeting Prep + Reverse-Prompts | `~/Downloads/partnership_lane_E_meeting_prep.md` |
| F | Product Portfolio + Revenue | `~/Downloads/partnership_lane_F_product_portfolio.md` |
| G | Institute Fit | `~/Downloads/partnership_lane_G_institute_fit.md` |

---

## The single strategic observation

**Reuben + Dan have a real partnership.** It's operated informally for months, produced real output (JSR, cross-contributed Founder Mode improvements, Peptide Checker in development, Reuben's engineering on Dan's machine). It's financially unsustainable for Reuben as currently structured ($230/mo net).

**The path forward is not complicated**:
1. Meet for 2 hours using Lane E framework
2. Decide the 5 must-decide items
3. See an attorney for $2-5K of formal paperwork
4. Start operating with documented structure
5. Ship the institute

**The block is emotional/conversational, not strategic.** The 7-lane team converged on a consistent recommendation across every dimension. The recommendation is defensible, standard in research institutes, and respects both principals' contributions. What remains is the conversation.

---

*Synthesis produced 2026-04-05 from 7 parallel research agents, ~400K total tokens. Each lane delivered a standalone brief + 250-word exec summary. Full briefs in `~/Downloads/partnership_lane_*.md`.*

*Disclaimer: educational/research input only, not legal or financial advice. Retain a Georgia business attorney and CPA before executing.*
