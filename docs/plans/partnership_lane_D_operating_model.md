# HUMMBL x S-Corp Partnership — Operating Model (Lane D)

**Version:** 1.0 draft | **Date:** 2026-04-05
**Principals:** Reuben Bowlby (HUMMBL LLC, Director & PI) | Daniel Matha (S-Corp, EVP)
**Model:** Bidirectional 2-principal research institute, cross-entity, async + SSH-native

---

## 1. Decision Rights Matrix

Decisions are classified R/A/C/I (Responsible / Accountable / Consulted / Informed). "A" is the single point of accountability — one name only. Where both principals must approve, the class is marked **JOINT**.

| Decision Class | Accountable | Consulted | Default Mode |
|---|---|---|---|
| **Product roadmap — Founder Mode** | Reuben | Dan | Reuben decides, Dan has 48h comment window |
| **Product roadmap — JSR** | Dan | Reuben | Dan decides, Reuben implements/advises |
| **Product roadmap — Peptide Checker** | **JOINT** | both | Dual sign-off required |
| **Product roadmap — HUMMBL primitives** | Reuben | Dan (if external surface) | Reuben decides |
| **Research direction (scientific agenda)** | Reuben (PI authority) | Dan | PI sovereignty — Dan advises on market fit |
| **Publication approval — technical/OSS** | Reuben | Dan (if names clients/deals) | Reuben signs off; Dan reviews named parties |
| **Publication approval — business/brand** | Dan | Reuben (if claims cite research) | Dan signs off; Reuben verifies claims |
| **Hiring — research/engineering contractors** | Reuben | Dan | Reuben decides under $5k/mo; JOINT above |
| **Hiring — BD/sales contractors** | Dan | Reuben | Dan decides under $5k/mo; JOINT above |
| **Budget allocation — entity-specific** | Entity principal | other | Each principal owns own P&L |
| **Budget allocation — shared infra (servers, SaaS)** | **JOINT** | — | Written allocation formula, quarterly true-up |
| **External partnership — research/tech** | Reuben | Dan | Reuben decides; Dan notified of IP terms |
| **External partnership — commercial/sponsor** | Dan | Reuben | Dan decides; Reuben reviews deliverable scope |
| **Pricing — services & deal terms** | Dan | Reuben (for delivery feasibility) | Dan decides; Reuben gates scope |
| **IP disclosure & patent filings** | **JOINT** | counsel | Neither can unilaterally file or disclose |
| **Strategic pivots (>30% effort redirect)** | **JOINT** | — | Requires written memo + 7-day reflection |
| **Expense auth — under $500** | Either | — | No approval needed, logged monthly |
| **Expense auth — $500–$2,500** | Relevant principal | other (informed) | Principal decides, notifies within 72h |
| **Expense auth — above $2,500** | **JOINT** | — | Written approval before commit |
| **Legal/compliance decisions** | **JOINT** | external counsel | Never unilateral; counsel required |
| **Sponsored-research fundraising** | Dan | Reuben (scope feasibility) | Dan leads, Reuben gates technical commitments |
| **Agent/infrastructure governance (bus, IDP)** | Reuben | Dan | Reuben owns PI-style scientific/infra authority |

**Rule of thumb:** Reuben = scientific/technical authority (PI). Dan = organizational/commercial authority (Director-external). Shared products and anything crossing the IP/brand/legal boundary = JOINT.

---

## 2. Deadlock Resolution

Two-principal partnerships deadlock predictably. We encode three layers:

### Layer 1 — Domain veto (default)
Each principal has **unilateral veto inside their own domain** (per matrix). If a decision is clearly in one domain, the other cannot block, only advise. This eliminates ~70% of potential deadlocks by pre-assigning authority.

### Layer 2 — Structured cool-off (JOINT decisions)
For JOINT decisions where principals disagree:
1. Disagreement recorded in `partnership/decisions.jsonl` (append-only) with both positions stated
2. **72-hour cool-off** — no further debate, each principal writes a one-page memo
3. Reconvene. If agreement, decision logged and executed
4. If still deadlocked, escalate to Layer 3

### Layer 3 — External advisor tiebreaker
Appoint a **standing Partnership Advisor** — a mutually trusted third party (attorney, fractional CFO, or senior founder) retained on a small annual stipend ($2k–$5k) with pre-agreed authority to break ties on JOINT decisions. The advisor does NOT have operational authority; they only adjudicate when called.

**Recommendation:** Adopt the **PI/Director precedent from research institutes**: scientific authority (PI = Reuben) is sovereign on research methodology, publication integrity, and technical architecture. Organizational authority (Director-external = Dan) is sovereign on resource allocation, external relationships, and strategic positioning. The Partnership Advisor is invoked only when a decision genuinely straddles both domains and cool-off fails.

**Hard rule:** No principal may execute a JOINT decision unilaterally while it is under dispute. Attempted unilateral execution is a partnership-level breach.

---

## 3. Bidirectional Work Protocols

### SSH & cross-machine work
- **Access grants are bidirectional and documented.** Reuben → Dan's machines (primary current pattern) and Dan → Reuben's machines (enabled, even if low-use today). Each principal maintains an `authorized_keys` manifest in their repo listing what the other can access.
- **Session announcement:** before an SSH session that will modify code, post to the coordination bus: `PROPOSAL` or `STATUS` with scope (e.g., "modifying JSR harness on Dan's mini for 30m"). Append-only TSV bus format (see `bus-protocol.md`).
- **No unannounced destructive ops.** Never `git reset --hard`, force-push, or wipe state on the other principal's machine without explicit confirmation in the current session.

### Code ownership marking
- Every repo root contains `OWNERS.md`: primary owner, secondary owner, decision class mapping.
- File-level `CODEOWNERS` for GitHub enforces review requirements on cross-entity paths.
- Shared products (Peptide Checker) require **one review from each entity** before merge.

### Commit attribution rules
- Commits made via cross-entity SSH are attributed to the acting principal, **not** the machine owner. Enforce via `git config user.email` per session.
- Add `Co-Authored-By:` trailer when work is genuinely collaborative.
- Never commit under the other principal's identity.

### PR review patterns
- **Cross-entity PRs:** require explicit approval from the owning entity's principal. CI gates (tests, security scans, PR guardrails) are shared and non-negotiable.
- **Single-entity PRs:** self-merge allowed for owner on owner-only repos, subject to standard CI.
- **Joint-product PRs (Peptide Checker, etc.):** dual approval required.

### Claude Code skills sharing
- Skills live in canonical `~/.claude/skills/` on each machine. Sync is **pull-based** — each principal pulls updates they want from a shared skills repo. No silent push/overwrite.
- Skills that touch credentials, financials, or external APIs require dual review before adoption.

### Work-log documentation
- Daily work is logged to the coordination bus (`STATUS`, `WIP_START`, `WIP_END`, `MILESTONE`).
- Weekly, each principal exports their bus messages into a `weekly_log.md` for shared visibility.
- Monthly, logs are rolled up into a partnership ledger entry.

---

## 4. Communication Cadence

| Cadence | Format | Channel | Duration | Purpose |
|---|---|---|---|---|
| Daily async standup | 3 bullets: yesterday / today / blockers | Bus `STATUS` + Signal DM | <5 min | Visibility, unblock |
| Weekly strategic sync | Video, agenda pre-posted | Signal/Jitsi, Tues 10am ET | 45 min | Priorities, conflicts, JOINT decisions |
| Monthly financial/ops review | Spreadsheet walkthrough + notes | Video + GitHub issue | 90 min | Budget, burn, pipeline, allocations |
| Quarterly partnership review | Written memo + retrospective | Doc + video | 2 hr | Matrix audit, advisor check-in, role fit |
| Ad-hoc design review | PR comments, threaded | GitHub | async | Technical decisions |

**Tools:** GitHub (code, PRs, issues) | coordination bus (agent + principal status) | Signal (private DM, quick async) | Email (external-facing, contracts, legal) | Slack optional for future team. **No Slack as primary principal channel** — bus + Signal is sufficient for 2-person partnership.

---

## 5. Conflict Protocols

1. **Disagreement voiced → recorded.** Any JOINT decision disagreement is logged to `partnership/decisions.jsonl` within 24h of first surfacing. Both positions stated in each principal's own words.
2. **Escalation ladder:** (a) direct discussion → (b) 72h cool-off with one-page memos → (c) Partnership Advisor tiebreak → (d) mediation if advisor cannot resolve → (e) wind-down triggers (see §6).
3. **When to pause:** if a decision is reversible and cheap to delay, default to pause. If either principal says "I need a week on this," the other honors it unless there's a hard external deadline.
4. **When to push through:** only when (a) external deadline is binding and documented, (b) cost of delay exceeds cost of imperfect decision, AND (c) the decision sits within one principal's domain.
5. **External advisor invoked when:** same deadlock surfaces twice, OR a single deadlock persists >14 days, OR principals agree the dispute is eroding trust.

---

## 6. Role Transition Protocols

### Voluntary step-back
- **90-day notice minimum** for reduced involvement; **180-day notice** for full exit.
- Exiting principal completes a knowledge-transfer package: all owned repos documented, external relationships transitioned, credentials rotated.
- Equity/economics renegotiated via pre-agreed formula in partnership agreement.

### Performance concerns
- Concerns raised in 1:1, recorded in quarterly review memo.
- 30-day corrective period with specific, measurable expectations.
- If unresolved, Partnership Advisor mediates.
- No unilateral removal — a 2-person partnership cannot fire one principal without agreement or legal dissolution.

### Buyout / wind-down triggers
Any of: (a) 6 months of unresolved deadlock on strategic direction; (b) principal unable to contribute for 90+ days without plan; (c) material breach (unauthorized IP disclosure, unilateral JOINT execution, financial misconduct); (d) mutual agreement to wind down.

Buyout formula and dissolution mechanics must be pre-agreed in the written partnership agreement (not this operating model) — recommend drafting within 60 days.

---

## 7. Meeting Cadence & Formats — Institute Model

Mirrors a small research institute with PI + Director dynamic:

- **Weekly Lab Meeting (Tues 10am ET, 45m):** status on active research threads, blockers, JOINT decisions queued. Reuben leads agenda (scientific/technical).
- **Weekly BD Sync (Thurs 10am ET, 30m):** pipeline, client conversations, proposals out, money in/out. Dan leads agenda (external/commercial).
- **Monthly All-Hands (1st Monday, 90m):** financials, matrix audit, any role/scope drift. Rotating facilitator.
- **Quarterly Offsite (virtual or in-person, 3–4h):** partnership review, advisor check-in, annual planning delta.
- **Annual Strategic Retreat (1 day, in-person if feasible):** vision, major pivots, equity/structure review.

All meetings produce a written artifact (agenda + notes + decisions + action items) committed to a shared repo within 24h. No artifact = meeting didn't happen.

---

## Adoption Checklist

- [ ] Both principals sign this operating model
- [ ] `partnership/decisions.jsonl` initialized
- [ ] `OWNERS.md` added to each product repo
- [ ] `CODEOWNERS` configured on GitHub
- [ ] Partnership Advisor identified and retained
- [ ] Written partnership agreement drafted (separate doc, 60-day target)
- [ ] Coordination bus identities registered for both principals
- [ ] First quarterly review scheduled

---
