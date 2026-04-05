# Partnership Lane A: Legal Architecture Brief

**Principals:** Reuben Bowlby (HUMMBL LLC, GA, 100% owner) + Daniel Matha (S-Corp, entity TBD)
**Date:** 2026-04-05
**Purpose:** Inputs for legal consultation with a Georgia business attorney. **NOT legal advice.**

---

## Current State (Baseline)

- **HUMMBL LLC** (GA, single-member, disregarded entity for federal tax) — Reuben, 100%
- **Dan's S-Corp** (state TBD) — Dan, owner, elected S-Corp status
- **No operating agreement, no equity split, no IP assignment across entities**
- **Cash flow:** informal monthly Zelle
- **Products co-developed:** Founder Mode (Reuben), Peptide Checker (joint), JSR (Dan built, Reuben engineered)
- **Operating model goal:** research institute (sponsored research, publication, grant eligibility) — NOT VC-track

---

## 1. Structural Options

### Option A — New Georgia LLC as Holding Company

**Structure:** Newly formed GA LLC ("Umbrella LLC") with Reuben + Dan as members. Holds membership interests or assignment rights in HUMMBL LLC and Dan's S-Corp (or just owns new/shared IP, leaving operating entities intact below).

- **Setup cost:** $100 GA filing + $500–$2,500 attorney + $0–$500 registered agent. Ongoing: $50/yr GA annual registration.
- **Tax:** Pass-through (partnership by default; LLC with 2+ members files Form 1065, issues K-1s). Can elect S-Corp if both members are eligible, but Dan's S-Corp entity CANNOT be an S-Corp shareholder (S-Corp shareholders must be individuals, estates, or certain trusts). So Umbrella would stay partnership-taxed, or Dan holds his interest individually.
- **IP ownership:** Clean — new/shared IP (Peptide Checker, joint roadmap) assigned to Umbrella via IP Assignment Agreement. Existing HUMMBL IP and Dan's S-Corp IP stay where they are unless separately assigned or licensed up.
- **Decision rights:** Operating Agreement defines member voting (equal / weighted / tiered), manager-managed vs member-managed, reserved matters (IP transfer, dissolution, debt).
- **Exit/dissolution:** OA includes buy-sell, right of first refusal, drag-along/tag-along, valuation method (appraisal, multiple of revenue, book value).

**Best for:** Clean, GA-native, operator-friendly middle ground.

---

### Option B — Delaware C-Corp Umbrella

**Structure:** DE C-Corp owns subsidiaries or shared IP. Reuben + Dan are shareholders.

- **Setup cost:** $89 DE filing + $2,500–$7,500 attorney + $50–$400/yr DE franchise tax + GA foreign qualification (~$225).
- **Tax:** **Double taxation** — corporate income taxed at entity (21% federal + DE/GA state), then dividends taxed at shareholder level. QSBS (§1202) eligibility is the main draw if exit >$10M envisioned.
- **IP:** Corp owns IP cleanly. Standard for VC due diligence.
- **Decision rights:** Board of directors + shareholder votes. Bylaws + stockholders' agreement govern.
- **Exit:** Stock purchase, merger, acquisition — well-worn paths. Dissolution is formal (DE Chancery).

**Best for:** VC fundraising optionality. Overkill for research-institute mode; adds tax drag and formality.

---

### Option C — Joint Venture / Strategic Alliance (Contract-Only)

**Structure:** Written JV agreement between HUMMBL LLC and Dan's S-Corp. No new entity.

- **Setup cost:** $1,000–$3,000 attorney to draft JV agreement.
- **Tax:** Each entity reports its own share of revenue/expense. Possible "tax partnership" recharacterization risk if IRS views the arrangement as a de facto partnership (Rev. Rul. 75-43) — watch for this.
- **IP:** Requires explicit cross-license or joint-ownership clauses per product. Messy over time; disputes likely as portfolio grows.
- **Decision rights:** Governed by contract terms. Harder to enforce absent entity.
- **Exit/dissolution:** Contract termination clause; IP reverts per assignment terms.

**Best for:** Testing the partnership for 6–12 months before committing to entity formation.

---

### Option D — Series LLC (DE or TX)

**Structure:** Master LLC with internal "series" — each series (Founder Mode, Peptide Checker, JSR) is a liability-segregated cell.

- **Setup cost:** $90 DE / $300 TX + $3,000–$6,000 attorney. **Georgia does not recognize Series LLCs** — foreign qualification required + uncertain GA liability shield between series.
- **Tax:** Each series can elect its own tax treatment (complex). IRS guidance is still partial (Prop. Reg. §301.7701-1).
- **IP:** Each series owns its product's IP cleanly.
- **Decision rights:** Per-series operating agreements.
- **Exit:** Series can be wound down independently.

**Best for:** Many products with distinct investors / liability profiles. **Poor fit for GA residents** due to recognition gap.

---

### Option E — Partnership Between HUMMBL LLC and Dan's S-Corp (Contractual)

**Structure:** Written partnership agreement; the two entities become partners. May inadvertently create a general partnership for tax purposes (Form 1065).

- **Setup cost:** $1,500–$3,500 attorney.
- **Tax:** Partnership files Form 1065, K-1s flow to HUMMBL LLC and Dan's S-Corp. S-Corp receiving K-1 is allowed.
- **IP:** Joint IP requires explicit assignment to the partnership or cross-license.
- **Decision rights:** Partnership agreement. Joint and several liability is the default — **serious downside**.
- **Exit:** Partnership dissolution; IP division per agreement.

**Best for:** Rarely. Liability exposure usually makes an LLC umbrella (Option A) strictly better.

---

### Option F — Dan Joins HUMMBL LLC as Member

**Structure:** Reuben amends HUMMBL operating agreement, issues membership interest to Dan individually (or to his S-Corp — see note).

- **Setup cost:** $1,500–$4,000 attorney to draft OA amendment + membership interest purchase/grant. HUMMBL becomes multi-member LLC (Form 1065 required).
- **Tax:** Pass-through. **Issuing equity to Dan is a taxable event** for Dan if granted for past services (compensation income at FMV). Safer to use a profits interest (Rev. Proc. 93-27 / 2001-43) — gives Dan share of future profits without upfront tax.
- **IP:** All HUMMBL IP already in HUMMBL; Dan's contributions assigned in. Dan's S-Corp IP stays separate unless licensed/assigned.
- **Decision rights:** HUMMBL OA rewritten with voting, reserved matters, buyout.
- **Exit:** Buy-sell provisions; Reuben retains control if majority preserved.

**Best for:** Simplest path if both principals are comfortable merging into Reuben's existing entity. Loses symmetry (Dan is joining Reuben's house, not a neutral umbrella).

---

### Option G — New S-Corp Jointly Owned by Reuben + Dan

**Structure:** New GA corp, S-Corp election, Reuben + Dan as individual shareholders.

- **Setup cost:** $100 GA filing + $2,000–$4,000 attorney + Form 2553 election.
- **Tax:** Pass-through, but **S-Corp requires "reasonable salary"** for owner-employees (payroll, W-2, self-employment tax on salary portion only — this is the S-Corp tax advantage). Adds payroll admin.
- **IP:** Corp owns IP cleanly.
- **Decision rights:** Bylaws + shareholders' agreement. Only one class of stock allowed (S-Corp restriction).
- **Exit:** Stock sale; buy-sell agreement required.

**Best for:** If principals want salary optimization and are willing to run payroll. Single-class-of-stock limits flexibility vs LLC.

---

## 2. Cross-Entity Work Handling

Today Reuben SSHes into Dan's machine and engineers on Dan's JSR code; Dan contributes to Founder Mode. **Without an IP assignment, default law is messy:**
- Work-for-hire doctrine (§101 Copyright Act) only applies to employees or 9 enumerated commissioned-work categories — software usually doesn't qualify as commissioned WFH.
- Without written assignment, Reuben likely retains copyright in his contributions to Dan's JSR, and vice versa. **Joint authorship** creates undivided co-ownership with duty to account.

| Option | Cross-entity mechanics |
|--------|----------------------|
| A (Holdco LLC) | IP Assignment Agreement from each entity + each individual → Umbrella. Umbrella licenses back to operating entities as needed. Cleanest. |
| B (C-Corp) | Same mechanics; IP assigned to corp. Invention assignment agreements standard. |
| C (JV) | Per-product IP clauses in JV contract. Error-prone. |
| D (Series LLC) | Per-series IP assignments. |
| E (Partnership) | Joint ownership default; explicit assignment clause required. |
| F (Dan joins HUMMBL) | Dan signs invention assignment → HUMMBL. Dan's S-Corp IP still separate. |
| G (New S-Corp) | Both sign invention assignments → new Corp. |

**Universal recommendation regardless of option:** Execute a **mutual IP Assignment & Invention Agreement** immediately covering all prior + future joint work, with attribution clause for research-institute publication purposes.

---

## 3. Tax Treatment Summary

| Option | Entity Tax | Principal Tax | SE Tax | Inter-Entity Invoicing |
|--------|-----------|--------------|--------|----------------------|
| A (LLC Holdco) | Pass-through (1065) | K-1 ordinary | Yes on active members | Yes, arm's length required |
| B (C-Corp) | 21% fed + state | Dividends (15/20%) | No (W-2) | Yes, transfer pricing rules |
| C (JV) | None (each entity) | Via existing entities | Per existing entity | Yes |
| D (Series LLC) | Uncertain / per-series | Per election | Varies | Yes |
| E (Partnership) | 1065 | K-1 to entities | Per entity | Yes |
| F (Dan in HUMMBL) | 1065 | K-1 | Yes on active members | Dan's S-Corp invoices HUMMBL |
| G (New S-Corp) | 1120-S | K-1 + W-2 salary | On salary only | Yes |

**Reasonable salary rule (S-Corp):** IRS requires owner-employees to take "reasonable compensation" before distributions. Failure → IRS recharacterizes distributions as wages + penalties.

---

## 4. Governance Mechanics

For **Option A (recommended below)**, Operating Agreement must specify:

- **Voting:** 50/50? 51/49? Weighted by capital contribution vs sweat equity? Class A (control) / Class B (economic)?
- **Reserved matters** (supermajority or unanimous): IP assignment out, dissolution, admitting new members, >$X debt, changing tax election, selling >X% of assets.
- **Deadlock resolution:** (a) mediation → arbitration ladder, (b) buy-sell "shotgun" (Texas shoot-out: one offers price, other chooses to buy or sell at that price), (c) third-party tiebreaker director, (d) Russian roulette clause.
- **Buyout triggers:** death, disability (>180 days), voluntary exit, for-cause removal, material breach. Valuation by (i) fixed formula, (ii) annual agreed value, or (iii) independent appraiser.
- **Vesting:** 4-yr vest with 1-yr cliff on equity issued for future services — protects against early departure.
- **Non-compete / non-solicit:** GA enforces reasonable restrictive covenants (O.C.G.A. §13-8-50 et seq., Restrictive Covenants Act).

---

## 5. Institute Compatibility

Research-institute mode needs: (a) sponsored research contracts, (b) grant eligibility, (c) publication authorship with institutional affiliation, (d) potential 501(c)(3) affiliate later.

| Option | Institute fit |
|--------|-------------|
| A (LLC Holdco) | **Strong.** Can sponsor research, enter MTAs/DUAs, publish with institutional affiliation. Can spawn a 501(c)(3) subsidiary later for grant eligibility. |
| B (C-Corp) | Strong for grants; double-tax drag. Corporate R&D tax credit available. |
| C (JV) | Weak. No institutional identity. |
| D (Series LLC) | Moderate; brand fragmentation. |
| E (Partnership) | Weak institutional identity. |
| F (Dan in HUMMBL) | Moderate; HUMMBL already operates institute-style. |
| G (New S-Corp) | Moderate; SE salary admin overhead distracts. |

**Note:** For federal grants (NIH SBIR/STTR, NSF), LLC and C-Corp are both eligible. 501(c)(3) path requires separate Form 1023 filing and distinct governance (public benefit, no private inurement).

---

## 6. Attorney Questions (Georgia business counsel)

1. Given Reuben is GA-resident and Dan's state TBD, does forming a GA Holdco LLC (Option A) create foreign-qualification burdens for Dan or his S-Corp? How do we minimize multi-state filings?
2. Can Dan hold his Umbrella LLC membership interest **individually** (cleanest) vs through his S-Corp, and what are the tax consequences of each? Does the S-Corp-holding-LLC-interest create passive income issues for Dan's S-Corp?
3. We want to issue Dan a **profits interest** in HUMMBL (or Umbrella) under Rev. Proc. 93-27 for future services — draft the safe-harbor grant and confirm no §83(b) election needed.
4. How do we structure a **mutual IP assignment** covering all prior joint work (Peptide Checker, JSR engineering via SSH, Founder Mode contributions) that is enforceable and doesn't trigger a §351/§721 taxable contribution issue?
5. For research-institute mode, can the Umbrella LLC enter **sponsored research agreements** and hold publication rights, and is there a pathway to spawn a 501(c)(3) affiliate for grants without tainting the LLC?
6. Draft **deadlock resolution** with a Texas shoot-out + independent appraiser fallback; what's standard for two-member GA LLCs?
7. Are **non-compete / non-solicit** clauses between Reuben and Dan enforceable in GA under O.C.G.A. §13-8-50 given both are principals not employees?
8. What **registered agent, annual registration, and GA-specific franchise/net-worth tax** obligations will the Umbrella LLC carry? Are there GA "research institute" designations that confer any tax benefit?
9. If we later want to raise institutional capital, is a **statutory LLC-to-C-Corp conversion** (GA §14-11-212 or DE equivalent) clean, or should we start as DE C-Corp now?
10. How should the **Zelle history** of monthly payments be documented retroactively — as loans, as service fees, or reclassified as capital contributions? Are there §7872 imputed-interest concerns?

---

## 7. Recommendation (Top 2 for Attorney Consultation)

### **Primary: Option A — New Georgia LLC as Holding Company**
- Symmetrical (neutral umbrella, neither principal joining the other's house)
- Pass-through tax, GA-native, minimal cost ($1–3K setup)
- Supports research-institute model; 501(c)(3) affiliate path open
- Clean IP aggregation; leaves HUMMBL and Dan's S-Corp intact
- Profits-interest grant mechanism proven

### **Backup: Option C — Joint Venture (interim, 6-12 months)**
- Low cost, tests partnership operationally before committing to entity
- Use interim to draft IP assignments, document work split, establish valuation baseline
- Graduate to Option A once product/revenue clarity emerges

**Avoid for now:** Options B (tax drag), D (GA recognition gap), E (liability), G (payroll overhead).

---

## Disclaimer

This document is **research and preparation material for a legal consultation**, not legal advice. All structural, tax, and governance decisions should be reviewed and executed by a licensed Georgia business attorney and a CPA familiar with pass-through entity taxation and S-Corp rules. IP assignments should be drafted by counsel with software/IP experience. State law varies; Dan's home state will affect several decisions above.
