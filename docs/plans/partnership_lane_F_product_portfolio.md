# Lane F — Product Portfolio & Revenue-Attribution Brief
**Entities:** HUMMBL LLC (Reuben) + Dan's S-Corp
**Date:** 2026-04-05
**Status:** DRAFT — operator review required

---

## 1. Product Categorization

| Bucket | Products | Rationale |
|---|---|---|
| **Wholly-Reuben (HUMMBL LLC 100%)** | Founder Mode, hummbl-governance (PyPI), Base120 + mental models | Built solo by Reuben, 14,400+ tests, pre-partnership IP |
| **Wholly-Dan (S-Corp 100%)** | JSR original concept/brand, Dan-originated BD frameworks | Dan conceived and seeded; Reuben engineered but as contracted work |
| **Joint (co-owned via umbrella/contract)** | Peptide Checker, HUMMBL Grade family (as a suite), future co-built products | Genuine co-creation, shared risk, split domain expertise |
| **Cross-contributed (one owner + rev-share)** | JSR (Dan owns, Reuben rev-share for engineering), Founder Mode (Reuben owns, Dan rev-share for BD/sales) | One-sided build, two-sided value realization |
| **Reference / OSS (brand-only)** | hummbl-governance PyPI, Base120 mental models (public), open skills/rules | Brand-building, recruiting, credibility lever |

---

## 2. Per-Product Ownership Proposals

### Founder Mode
- **Legal owner:** HUMMBL LLC (100%)
- **Primary maintainer:** Reuben
- **Revenue share:** Dan gets 15–25% of net revenue attributable to BD/sales/promotion he sources; 0% on organic/inbound
- **Exit treatment:** Reuben retains IP on dissolution; Dan receives tail revenue (12 months) on deals he closed
- **Publication rights:** Reuben authors technical; Dan authors GTM/positioning with attribution

### Peptide Checker
- **Legal owner:** Umbrella entity (preferred) OR 50/50 JV contract between HUMMBL LLC and Dan S-Corp
- **Primary maintainer:** TBD by domain split — Reuben (platform/API), Dan (regulatory/clinical/BD)
- **Revenue share:** 50/50 net of direct costs, with carve-out for disproportionate regulatory spend
- **Exit treatment:** Right of first refusal to buy out at trailing-12-month-revenue × 2.5x
- **Publication rights:** Joint authorship default; either party can publish solo with 30-day review window

### JSR (Jargon-to-Substance Ratio)
- **Legal owner:** Dan's S-Corp (trademark + concept)
- **Primary maintainer:** Dan (product), Reuben (engineering)
- **Revenue share:** Reuben gets 20–30% of JSR-attributed revenue as long as he maintains the codebase; drops to 10% royalty if he hands off
- **Exit treatment:** Reuben retains right to fork engineering work under different name if partnership dissolves and JSR remains with Dan
- **Publication rights:** Dan owns brand voice; Reuben publishes engineering write-ups with Dan's sign-off

### HUMMBL Grade Family (Code Grade, Namespace Audit, JSR-as-component)
- **Legal owner:** HUMMBL LLC owns "HUMMBL Grade" trademark and suite; Dan's S-Corp licenses JSR into the suite
- **Primary maintainer:** Reuben (suite), Dan (JSR component)
- **Revenue share:** Suite revenue split 70/30 Reuben/Dan when sold as bundle; individual component revenue flows to component owner
- **Exit treatment:** JSR extractable; HUMMBL Grade suite minus JSR stays with HUMMBL LLC
- **Publication rights:** Co-branded under HUMMBL Grade

### hummbl-governance (PyPI)
- **Legal owner:** HUMMBL LLC (100%)
- **Maintainer:** Reuben
- **Revenue:** None direct (OSS); brand + consulting lead-gen
- **Publication:** Reuben sole

### Base120 + Mental Models
- **Legal owner:** HUMMBL LLC
- **Maintainer:** Reuben
- **Revenue:** Licensed into consulting engagements at flat per-use fee; potential book/course future
- **Publication:** Reuben sole; Dan cites with attribution

---

## 3. Revenue Attribution Rules

**Consulting:**
- Entity that sources the client invoices the client
- If the other entity provides >20% of delivery hours, cross-entity invoice at agreed rate (see §4)
- Default delivery rate: $225/hr Reuben, $275/hr Dan (operator-adjust)

**Product revenue:**
- Revenue lands in owning entity's account first
- Cost allocation: infrastructure costs borne by owner; marketing costs shared per revenue-share ratio
- Royalty payments made quarterly within 30 days of quarter-end

**Licensing:**
- Joint products license through umbrella (when formed); until then, through whichever entity owns the primary trademark
- Wholly-owned products license entity-direct

**Sponsored research:**
- Institutional grants/contracts flow to whichever entity best matches the sponsor's compliance posture (S-Corp for commercial sponsors, LLC for foundation/academic)
- 10% overhead retained by the receiving entity for admin

---

## 4. Cross-Entity Invoicing Model

- **HUMMBL LLC → Dan S-Corp:** for Reuben's engineering work on Dan's products (JSR maintenance, platform build-outs)
- **Dan S-Corp → HUMMBL LLC:** for Dan's BD, pitch work, client sourcing for Founder Mode or HUMMBL Grade
- **Cadence:** Monthly invoicing, quarterly reconciliation. Monthly keeps cash flow honest; quarterly trues up revenue-share accruals
- **Transfer pricing:** Use market rate for comparable work ($225–$275/hr) documented in a one-page intercompany services agreement. Below-market rates invite IRS reclassification; above-market invites partner friction
- **Net settlement:** If both sides owe, net the amounts and settle the difference
- **Documentation:** Each invoice cites the product, hours, and rate; retained 7 years

---

## 5. Product-Specific Deep Dives

### Founder Mode
Reuben built it (14,400+ tests, 7 adapters live, Phase 2 underway). Dan's rev-share must be **performance-contingent, not equity-like**, because Reuben carries all build risk and ongoing maintenance cost. Mechanism: **attribution-tracked BD commission.** Dan closes a deal → Dan gets 20% of net ARR year one, 15% year two, 10% year three, 0% thereafter. Uses standard sales-attribution rules (first-touch or closed-won credit, agreed in writing). If Dan never sources a deal, Dan earns $0 on Founder Mode — this is fair because Reuben bears 100% of engineering cost.

### Peptide Checker
Stage: concept/early-prototype (operator confirm). Contributions: Reuben = platform, data pipeline, API; Dan = regulatory knowledge, clinical relationships, market access. **HIPAA:** likely required if handling PHI; design for BAA-eligible infra (AWS BAA, Vanta-ready). **FDA:** if classified as CDS (Clinical Decision Support) software and not merely informational, could trigger 510(k) or De Novo pathway — budget 6–18 months regulatory runway. **Recommendation:** keep v1 strictly as informational reference tool (non-device) to avoid FDA scope; seek regulatory counsel before any diagnostic claim.

### JSR
Dan built concept and initial; Reuben engineered via SSH. **Ownership:** Dan's S-Corp keeps trademark and brand. Reuben holds rev-share as long as he maintains. If Reuben stops maintaining, he converts to a fixed 10% royalty on JSR revenue for 24 months, then sunsets. Protects both parties: Dan isn't locked in perpetually to a non-contributor, Reuben isn't stripped for his engineering work.

### HUMMBL Grade Family
If JSR joins the HUMMBL Grade suite, it's licensed in under a revenue-share, not sold or assigned. HUMMBL LLC owns the suite; JSR remains Dan's. Suite bundle revenue: 70/30 Reuben/Dan to reflect that HUMMBL Grade = 2+ components Reuben owns plus JSR. Individual component sales flow to component owner. Keeps incentives aligned: both parties want the suite to win, but neither loses individual product equity.

---

## 6. Revenue Forecasting (Illustrative, 12-Month Institute Model)

| Channel | % of Revenue | Primary Attributor |
|---|---|---|
| Consulting (governance, audits) | 45% | Split ~60/40 Reuben/Dan |
| Licensing (Founder Mode, HUMMBL Grade) | 20% | Reuben-weighted (80/20) |
| Subscriptions (API tiers, support) | 15% | Reuben-weighted (75/25) |
| Sponsored research / grants | 12% | Dan-weighted (60/40) |
| Institutional memberships | 5% | Joint (50/50) |
| Hardware (Peptide Checker) | 3% | Joint (50/50) |

**Per-principal attribution (illustrative):** Reuben ≈ 55% of revenue flows through HUMMBL LLC; Dan ≈ 45% through S-Corp. Reconciles quarterly via §4 intercompany invoicing.

---

## 7. Umbrella Entity Implications

Products that **benefit most** from umbrella ownership:
- **Peptide Checker** — joint build, regulated domain, needs single compliance posture
- **HUMMBL Grade suite** — multi-component bundle, licensing clarity matters
- **Institutional memberships** — single-entity counterparty preferred by institutions

Products that should **stay entity-direct:**
- Founder Mode (Reuben's IP, no reason to dilute)
- JSR (Dan's brand)
- hummbl-governance, Base120 (Reuben's brand-building, no revenue)
- Individual consulting engagements (use sourcing entity, avoid umbrella overhead)

**Recommendation:** Form umbrella only when (a) joint product revenue exceeds ~$150K ARR, (b) an institutional buyer requires single-counterparty contracting, or (c) tax efficiency clearly favors consolidation. Until then, JV contracts are cheaper and faster.

---

*End of brief. Operator review required before execution.*
