# Partnership Lane C — Equity & Compensation Framework

**Subject:** Reuben Bowlby (HUMMBL LLC, Director & PI) + Daniel Matha (S-Corp, EVP/BD)
**Model:** Self-funded research institute, no VC raise, revenue from consulting + licensing + sponsored research
**Date:** 2026-04-05
**Disclaimer:** Educational/research input only. **Not legal or financial advice.** Engage a startup attorney (Delaware/Georgia) and CPA before executing any of the below.

---

## 1. Equity Split Options

### 1.1 100/0 with Profit-Share Contract
- Reuben retains 100% of HUMMBL LLC (or NewCo). Dan operates as independent contractor via his S-Corp under a profit-share agreement.
- **Pros:** Cleanest cap table; no dilution; Reuben retains full IP control; avoids securities/§83(b) complexity; easiest to unwind.
- **Cons:** Dan has no upside lock-in; weaker BD motivation; Dan may defect if better offer appears.
- **Best when:** IP is the overwhelming value driver and BD is replaceable.

### 1.2 80/20, 70/30, 60/40 with Vesting
- Fixed split with time-based or milestone vesting on Dan's stake.
- **Vesting:** Standard 4-year vest, 1-year cliff (25% at 12 months, then 1/48th monthly). Milestone variant: 25% at signed service contract, 25% at $100k ARR, 25% at $250k ARR, 25% at $500k ARR.
- **Acceleration triggers:** Double-trigger (change of control + termination without cause) is standard. Single-trigger on death/disability.
- **Buy-out provisions:** Right of first refusal (ROFR); formula-based buyback at book value or trailing 12-mo revenue multiple (typically 1-2x) if Dan departs or is terminated for cause.
- **Pros:** Recognizes Reuben's pre-partnership IP contribution; gives Dan real skin in the game; industry-standard.
- **Cons:** Requires 409A valuation for tax-safe option grants; dilution is permanent absent buyback.

### 1.3 50/50 with Decision-Tiebreak Mechanism
- Equal split. Requires explicit deadlock clause: independent board seat, rotating CEO, coin flip, or shotgun clause (Texas shootout).
- **Pros:** Signals true partnership; strong co-founder motivation.
- **Cons:** Ignores pre-existing IP asymmetry; deadlocks are existential risk; research shows 50/50 co-founder splits have highest dissolution rate (Noam Wasserman, *Founder's Dilemmas*).
- **Best when:** Contributions are genuinely symmetric going forward AND pre-existing IP is separately licensed.

### 1.4 Dynamic Equity (Slicing Pie / Grunt Fund)
- Equity is not fixed upfront. Each hour worked, dollar invested, and asset contributed earns "slices" at pre-agreed rates (e.g., Reuben's time @ $250/hr = 250 slices/hr; cash @ 4x slices/dollar; pre-existing IP valued upfront as fixed slice block).
- Recalculated until a "freeze event" (first outside raise, $1M revenue, or defined milestone date).
- **Pros:** Fair by construction; adjusts automatically if one party disengages; Mike Moyer's framework is well-documented.
- **Cons:** Admin overhead (weekly time logs); can feel transactional; attorneys unfamiliar with it charge premium; not well-suited to LLC conversions.
- **Best when:** Both parties' future contributions are uncertain and you want self-correcting fairness.

### 1.5 Phantom Equity / Profit Units
- Dan receives contractual right to % of profits or exit proceeds WITHOUT legal equity. No dilution of HUMMBL LLC cap table.
- Typical structure: Profit interest units (PIUs) in LLC (tax-advantaged if structured per Rev. Proc. 93-27 / 2001-43), OR phantom stock plan with vesting.
- **Pros:** No §83(b) election anxiety; Reuben retains voting control; easy to terminate on breach; no securities registration.
- **Cons:** Dan has no voting rights; harder to explain to Dan's CPA; PIUs require capital account accounting.
- **Best when:** You want to reward Dan like an owner without making him one.

---

## 2. Comp Structure Options (Separate From Equity)

| Model | Mechanics | Best For |
|---|---|---|
| **Salary-only (institute)** | W-2 from HUMMBL LLC (requires LLC to elect S-corp or have payroll). Predictable. | Post-revenue stability. |
| **Salary + equity** | Below-market cash + vesting equity. Classic startup. | Bridging to Series A (N/A here). |
| **Revenue share** | Fixed % of specific product line revenue (e.g., Dan gets 15% of BD-sourced consulting revenue for life of client). | Aligning BD incentives. |
| **Billable-hours** | Market rate ($200-$300/hr Reuben; $150-$250/hr Dan) invoiced to NewCo or direct clients. | Early, irregular revenue. |
| **Cross-entity invoicing** | HUMMBL LLC invoices Dan's S-Corp for Reuben's technical work; S-Corp invoices HUMMBL LLC for BD. Nets to profit distribution. | Legal separation of entities; tax optimization. **Requires arm's-length pricing** or IRS will recharacterize. |
| **Hybrid + milestone bonuses** | Base retainer ($2-5k/mo) + hourly overage + quarterly bonus on closed deals. | Institute model with variable BD load. |

---

## 3. Market Comp Benchmarks (2025-2026, US)

- **Research institute Director / PI (early-stage, solo-to-small, non-academic):**
  $120k-$220k base. Independent research institutes (e.g., Santa Fe Institute, Allen Institute early hires): $150-$250k. Small AI governance orgs (METR, Apollo Research, Convergence Analysis): directors $130-$180k in 2024-25 per public 990s and Glassdoor.
- **EVP / Chief Business Officer, early-stage SaaS ($0-$2M ARR):**
  $140k-$200k base + 0.5-2.0% equity (Kruze Consulting, Pave 2025 reports). Pre-revenue: $80-$140k + 1-3% equity.
- **Fractional CBO / Head of BD:**
  $175-$400/hr or $6-$15k/mo retainer for 10-20 hrs/week (Chief Outsiders, Fractional Executive Solutions, Bolster 2024-25 benchmarks).
- **Reuben's $200-$300/hr:** Consistent with senior AI/ML consultant rates (Toptal $150-$300/hr; independent AI governance consultants $250-$500/hr per Gartner 2024). This is defensible as his "market rate" for deferred-comp accounting.
- **Founder pay, bootstrapped/pre-revenue (Kruze 2025):** Median $0-$50k; post-$500k ARR median jumps to $125k.

---

## 4. "Underpaid Now → Revenue Share Later" Structural Analysis

**The problem:** Reuben took $230/mo net against a stated market rate of $200-$300/hr. The gap is the "deferred comp liability" — without documentation, it's invisible and unrecoverable.

**Clean conversion mechanics:**

1. **Reconstruct the ledger.** Document hours worked × agreed hourly rate − cash received = **accrued deferred comp balance**. Sign both parties. This creates a bookable liability on HUMMBL LLC's balance sheet.
2. **Choose conversion path:**
   - **Convert to equity:** Deferred comp balance ÷ agreed company valuation = equity %. Requires 409A valuation and §83(b) election within 30 days of grant.
   - **Convert to profit units (PIUs):** Deferred balance becomes a preferred distribution tier — Reuben gets first $X of profits before any split. Cleaner tax treatment than equity conversion.
   - **Convert to promissory note:** HUMMBL LLC issues Reuben a note (e.g., $50k @ 5% AFR, payable from future revenue). IRS-clean if AFR rate is respected.
   - **Phantom equity bridge:** Grant Reuben phantom units equal to deferred balance; units pay out on liquidity event or defined revenue threshold.
3. **Sweat equity accounting rules (informal summary):**
   - IRS treats sweat equity as taxable compensation at fair market value when vested.
   - §83(b) election lets recipient pay tax on low valuation NOW rather than higher valuation later.
   - LLCs can issue PIUs with zero tax event at grant if properly structured (safe harbor: Rev. Proc. 2001-43).
4. **Triggering events for conversion:**
   - First signed client contract ≥ $25k
   - First calendar month with net income ≥ $10k
   - Formation of NewCo / entity restructuring
   - Any outside capital event
   - Defined calendar date (e.g., 2026-12-31)

---

## 5. Specific Recommendation: Reuben / Dan

### Suggested split: **75/25 with dynamic adjustment band (±10%)**

**Reasoning:**
- Reuben brought ~2 years of pre-partnership IP (governance primitives on PyPI, 14,400+ test platform, 300+ research docs, 361 Claude skills). Standard founder advice: pre-existing IP = fixed equity floor (~70-80%).
- Dan's BD channel (medical/peptide network, corporate wellness B2B) is high-optionality but unproven revenue. Start at 25%, with adjustment band to 35% if BD generates >50% of trailing-12-mo revenue, or down to 15% if BD contributes <20%.
- Adjustment band is reviewed annually and frozen at first $250k revenue milestone OR Dec 31, 2027, whichever comes first.

### Suggested comp structure: **Hybrid cross-entity invoicing + revenue share**

- **Base:** Each entity invoices the other at arm's-length rates for actual hours (Reuben $225/hr; Dan $200/hr).
- **Revenue share:** Dan earns additional 15% of gross revenue from clients he sourced (5-year tail per client).
- **Reuben's back-pay:** Reconstruct ledger for 2024-2026 underpayment → convert to preferred profit distribution (Reuben gets first $X of distributions before 75/25 split kicks in). Target: full repayment within 24 months of first $10k profit month.
- **Dan's S-Corp remains separate.** Services contract between HUMMBL LLC and Dan's S-Corp, not employment.

### Suggested vesting: **4-year milestone vest on Dan's 25%**
- 5% at signed services agreement + first BD-sourced client
- 5% at $50k cumulative BD-sourced revenue
- 5% at $150k cumulative
- 5% at $300k cumulative
- 5% at 36-month tenure mark

### Dan's future BD-driven revenue:
- Dan's 15% revenue share on BD-sourced clients applies regardless of vesting status (it's comp, not equity).
- Revenue share survives Dan's departure for 18 months on existing clients (trailing commission), then terminates.

---

## 6. Deal Breakers (Clauses You MUST Include)

1. **IP assignment & carve-out.** Reuben's pre-existing IP (everything dated before partnership execution date) is **explicitly excluded** from any assignment. Post-partnership work product assignment terms defined separately. Without this, Dan could claim rights to the 14,400-test platform.
2. **Vesting + cliff on Dan's equity.** No equity grant without 1-year cliff. Prevents the "leave in month 2 with 25%" scenario.
3. **Buy-out / ROFR clause.** Formula-based buyback (1-2x trailing 12-mo revenue attributable to Dan's equity, or book value — whichever is higher) on voluntary departure, termination for cause, death, disability, or bankruptcy.
4. **Deferred comp ledger documentation.** Reuben's accrued back-pay must be a written, signed, balance-sheet liability BEFORE any equity issuance to Dan. Otherwise Dan dilutes Reuben's unrecovered contribution.
5. **Non-compete / non-solicit (narrow & enforceable).** 12-month non-solicit of HUMMBL clients; no broad non-compete (GA & FTC 2024 rule make these shaky).
6. **Deadlock / exit mechanism.** Shotgun clause or independent tiebreaker for material decisions. Silence here is a slow-motion disaster.
7. **Confidentiality + data rights.** Research data, client lists, proprietary methodologies remain HUMMBL LLC property.
8. **409A / valuation baseline.** Document fair market value at partnership formation for tax compliance on any equity grant.

---

**Recommended next steps:**
1. Retain a Delaware-licensed startup attorney (~$3-7k for founding docs).
2. Retain a CPA for cross-entity tax structuring ($1-2k).
3. Draft a non-binding term sheet (2 pages) covering the above BEFORE lawyers touch it.
4. 409A valuation deferred until first $100k ARR (cost: $2-5k).
