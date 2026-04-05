# Partnership Lane B: IP Ownership Map & Attribution Framework

**Parties:** Reuben Bowlby (HUMMBL LLC, Georgia) and Daniel Matha (S-Corp, entity TBD)
**Date:** 2026-04-05
**Status:** DRAFT — pre-formalization baseline

---

## 1. Asset Inventory & Current Provenance

### Pure-Reuben Assets (HUMMBL LLC)
| Asset | Type | Provenance | Proposed Owner |
|---|---|---|---|
| Founder Mode platform | Software (14k+ tests, 103 services) | Reuben solo, on Reuben's machines | HUMMBL LLC |
| hummbl-governance | Framework package | Reuben solo | HUMMBL LLC |
| Base120 + 120 mental models | Methodology + content | Reuben solo, authored docs | HUMMBL LLC |
| HUAOMP methodology | Methodology | Reuben solo | HUMMBL LLC |
| MTSMU methodology | Methodology | Reuben solo | HUMMBL LLC |
| CCAF framework (v1.0-1.2) | Framework | Reuben solo | HUMMBL LLC |
| Arbiter | Quality scoring system | Reuben solo | HUMMBL LLC |
| CLP (Cognitive Ledger Protocol) | Protocol spec + impl | Reuben solo | HUMMBL LLC |
| IDP (Identity Delegation Protocol) | Protocol + impl | Reuben solo | HUMMBL LLC |
| 361 Claude skills | Skill library | Reuben solo | HUMMBL LLC |
| hummbl-agent, hummbl-tuples, hummbl-assurance, hummbl-cca-f, hummbl-iac, hummbl-mobile, hummbl-bibliography, hummbl-production | Repos | Reuben solo | HUMMBL LLC |
| 300+ research docs | Writing/research | Reuben solo | HUMMBL LLC |

### Pure-Dan Assets (Dan's S-Corp)
| Asset | Type | Provenance | Proposed Owner |
|---|---|---|---|
| Medical/peptide industry domain knowledge | Know-how | Dan's career | Dan personally / S-Corp |
| Medical/peptide network | Relationships | Dan's career | Dan personally |
| Business-development network | Relationships | Dan's career | Dan personally / S-Corp |
| Dan's physical machine | Hardware | Dan owns | Dan personally |
| foundermode-ai GitHub org (if Dan-owned) | Namespace | Dan created | Dan's S-Corp |

### Cross-Entity / Complicated Assets
| Asset | Provenance | Current Status |
|---|---|---|
| JSR (jargon-to-substance-ratio) | Dan originated in his repo; Reuben materially engineered improvements via SSH + Claude Code + Reuben-built skills | **Contested / unformalized** |
| Peptide Checker | "Joint?" per brief | **Unformalized** |
| Claude Code harness on Dan's machine | Reuben built/improved it on Dan's hardware | **Reuben tooling deployed on Dan infra** |

---

## 2. Attribution Rules Framework

### Rule A — Pure Solo Work (Bright Line)
If one party conceived, designed, authored, and shipped an asset with no material contribution from the other, that asset is 100% owned by the authoring party's entity. Documentation, git history, and repo ownership are the primary evidence. No revenue share accrues to the non-authoring party. **Reuben's 13 Founder Mode / HUMMBL artifacts and Dan's medical network fall here cleanly.**

### Rule B — Host Infrastructure Does Not Confer IP
Running on someone's hardware, SSH access, git org ownership, or file hosting does **not** by itself create co-ownership. Dan's machine hosting Reuben's harness does not make HUMMBL's harness Dan's IP. Dan's GitHub org containing JSR does not make Reuben's engineering commits Dan's. This mirrors standard work-for-hire/contractor case law: the substrate is not the work.

### Rule C — Material Engineering Contribution Creates a License Interest, Not Co-Ownership
When party A authored the original work and party B made material engineering improvements (bug-fixes, rearchitecture, performance, feature adds), default rule: **A retains IP ownership; B holds a perpetual, royalty-free license to the improvements B authored, plus a named-contributor credit.** If the improvements are severable (a module, a skill, a subsystem), B may retain IP on the severable component and license it to A. This is the JSR pattern.

### Rule D — Joint Invention Requires Joint Intent
A work is "joint" only if both parties (a) contributed to conception (not just execution), (b) intended at creation for shared ownership, and (c) can point to a contemporaneous writing or message confirming joint intent. Absent those three, default to Rule A or C. Peptide Checker needs a written call: was it Dan's concept that Reuben built, or were both in on the conception? The answer changes ownership.

### Rule E — Methodology Origination is Sticky
A methodology (Base120, HUAOMP, MTSMU, CCAF, JSR) is owned by whoever originated and named it. Subsequent improvers do not gain IP in the methodology itself, only in their specific improvements/implementations. This prevents methodology capture via incremental edits.

### Rule F — Cross-Entity Billable Work is Contract Work
When Reuben engineers on Dan's code for Dan's business purpose, that work is contractor engineering, governed by a written SOW. Default: work-for-hire on the deliverables, but Reuben's reusable tooling (skills, harness, frameworks) remains HUMMBL-owned and Dan receives a license to use it, not ownership.

---

## 3. JSR-Specific Analysis

**Pattern:** Dan authored JSR v0 in Dan's repo. Reuben SSH'd in, used Reuben-built Claude Code skills and harness to materially improve JSR. Dan cited Reuben's email as the "first-ever perfect JSR score," confirming Reuben's improvements are measurably working.

**Clean story:** Dan owns JSR IP. Reuben's engineering contributions are contractor improvements licensed back to Dan's S-Corp, with two carve-outs: (1) the Claude skills and harness Reuben used remain HUMMBL IP (licensed to Dan for JSR use); (2) Reuben retains a named-contributor credit and a perpetual license to reference JSR-engineering techniques in HUMMBL writing.

**Precedents:**
- **Linux kernel model** — Linus owns the project; contributors retain copyright on their patches but license them in under GPL. Dan = Linus; Reuben = core contributor.
- **GitHub + Copilot model** — GitHub hosts your repo, but your IP is yours. Reuben's harness hosted on Dan's machine does not transfer.
- **Red Hat / RHEL** — Red Hat packages upstream open-source work into a branded distribution. HUMMBL could package JSR-engineered-by-HUMMBL as a branded consulting offering, licensed from Dan.
- **Ghostwriter precedent** — named author retains IP; ghostwriter gets fee + sometimes credit. Reuben is closer to an engineering co-author than ghostwriter given measurable score impact, which justifies the credit + license carve-out.

**Recommended formal structure:** JSR IP assigned to Dan's S-Corp. Side letter: Reuben named as engineering contributor, HUMMBL skills/harness remain HUMMBL-owned with a non-exclusive license to Dan for JSR purposes, and Reuben receives revenue share on JSR commercialization tied to the measurable improvements he shipped (see §4).

---

## 4. Revenue-Share Mechanics

Dan's promise of revenue share on Founder Mode, Peptide Checker, and "anything else we build together" needs structural form. Three options, in order of cleanness:

**Option 1 — Per-Product Licensing Agreement (recommended).** Each product is a separate license agreement between HUMMBL LLC and Dan's S-Corp. Founder Mode: HUMMBL licenses to Dan's S-Corp for X% of gross revenue from Dan-sourced deals. Peptide Checker: joint license with defined revenue split (e.g., 50/50 if truly joint, or 70/30 if one party authored more). JSR: Dan licenses to HUMMBL for HUMMBL-branded consulting use, with Reuben's contributor royalty baked in. Pros: clean per-asset, renegotiable, survives entity changes.

**Option 2 — Joint Venture Sub-LLC per Product.** Form "FM Ventures LLC" (or similar) for each co-commercialized product. Both entities contribute IP via license, both receive equity proportional to contribution. Pros: formal, investor-ready. Cons: overhead, tax complexity, premature for current revenue.

**Option 3 — Royalty Side-Letter.** Single side letter covering all current and future joint work, with a standard royalty schedule (e.g., 15% to originator, 10% to material improver, balance to commercializing entity). Pros: fast. Cons: fuzzy on new products.

**Recommendation:** Option 1 for Founder Mode + Peptide Checker + JSR today. Revisit Option 2 when any product clears $100k ARR. Rev-share percentages should be written before first revenue, not after.

---

## 5. Assignment Triggers (When to Formalize)

Formalize IP in writing when **any** of these occur:
1. **First dollar of revenue** on a joint or cross-entity asset.
2. **Entity formation** (Dan's S-Corp name filed, HUMMBL LLC amendments).
3. **Third-party licensing deal** (customer, reseller, investor) referencing any asset.
4. **Publication or public attribution** (paper, talk, press) naming both parties or claiming a methodology.
5. **Hiring or subcontracting** on any asset (new contributors need chain-of-title).
6. **Investor diligence** (any raise, any term sheet).
7. **Breakup trigger** — if the partnership dissolves, pre-agreed exit terms prevent litigation.
8. **Trademark filing** (HUMMBL, Founder Mode, JSR, Peptide Checker names).

---

## 6. Red Flags / Predictable Disputes

**RF-1 — Methodology drift on JSR.** Reuben has already meaningfully improved JSR ("first perfect score"). Risk: over time the JSR that ships publicly is mostly Reuben-engineered, but Dan retains the name and revenue. Head off with written contributor credit + engineering-improvement license back to HUMMBL.

**RF-2 — "Anything we build together" is unbounded.** This phrase covers work that has not yet been conceived. It's a future-IP assignment with no scope, no rev-share numbers, and no exit. Courts disfavor unbounded future-IP assignments. Replace with a per-product process: each new joint project gets a one-page term sheet before work begins.

**RF-3 — Harness ambiguity.** Reuben's Claude Code harness and 361 skills run on Dan's machine for Dan's benefit. If Dan ever claims these as part of his S-Corp deliverables to a customer, HUMMBL's skill IP is exposed. Head off with an explicit harness license: HUMMBL-owned, Dan-licensed-for-internal-use only, no sublicensing.

**RF-4 — Underpayment + promised rev-share = disputed consideration.** Dan paying $230/mo net while promising future revenue share is exactly the fact pattern that becomes "I was underpaid and the promises weren't kept." Document the comp-vs-promised-rev-share trade in writing now, with dollar figures and vesting.

**RF-5 — foundermode-ai GitHub org naming collision.** If Dan's org uses "foundermode" and Reuben's product is "Founder Mode," trademark collision is inevitable at commercialization. Pick a resolution: shared mark with joint entity, or rename one.

**RF-6 — Peptide Checker unknown provenance.** "Joint?" with a question mark is the exact artifact that litigates. Write down today who conceived, who authored, who owns, what the split is.

**RF-7 — S-Corp entity TBD.** Dan has no formed entity yet; all of Dan's contributions are currently personal. When the S-Corp forms, all existing IP must be assigned to the S-Corp in writing with proper consideration, or the S-Corp doesn't own it.

---

**END DOCUMENT**
