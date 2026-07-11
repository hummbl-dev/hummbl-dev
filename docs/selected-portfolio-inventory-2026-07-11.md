# Selected HUMMBL Program Portfolio — Draft PR, Issue, and Coordination Map

**Snapshot: 2026-07-11**
**Scope: 16 explicitly enumerated repositories only (NOT the full hummbl-dev org)**
**Prepared by: devin**
**Audit: ChatGPT reconciliation applied — see §Reconciliation Report**

## Bounded scope statement

This is NOT a complete hummbl-dev ecosystem map. The full organization has 97 open draft PRs across 21 repositories. This portfolio covers 72 open draft PRs across 16 selected repositories. The 25 omitted draft PRs span: founder-mode (8), agent-runtime-governance (7), hummbl-voice (3), mcp-server (2), anvil-fleet (2), hummbl-production (1), and 2 others.

## Reconciled counts

| Measure | Value |
|---------|------:|
| Repositories in scope | 16 |
| Open draft PRs in scope | 72 |
| Unique PRs represented in inventory | 72 |
| Open issues in scope (no PR) | 31 |
| Unique issue references | 31 |
| Execution lanes | 17 |
| Standing-coordination lane | 1 |
| Collision groups (competing PRs) | 4 |
| PRs with DO_NOT_ADOPT marker | 6 |
| PRs with BLOCKED marker | 1 |
| Operator-gated items | 1 |

## Disposition model

Every work item has exactly one disposition. "Ready for merge" is prohibited unless all readiness evidence is present.

| Disposition | Meaning |
|-------------|---------|
| IMPLEMENTATION_COMPLETE_PENDING_INDEPENDENT_REVIEW | Code/tests reported complete; needs independent review |
| REVIEWABLE_SPEC | Spec document complete; needs review before adoption |
| SPEC_ONLY_IMPLEMENTATION_REQUIRED | Spec only; implementation work remains |
| BLOCKED_ON_DEPENDENCY | Cannot complete until named dependency resolves |
| CONFLICTING_DUPLICATE | Competing PR owns same scope; needs adjudication |
| SUPERSEDE_OR_CONSOLIDATE | Should be superseded by a named survivor |
| OPERATOR_GATED | Requires operator action (credential, approval, etc.) |
| STALE_RECEIPT_REQUIRES_UPDATE | Historical receipt with merged dependencies; needs update |
| STANDING_COORDINATION | Persistent surface; not a work item |
| NOT_READY | Implementation incomplete or not started |

## Collision groups — 4 competing PR pairs

### Group A: model-routing-as-code#7 (scope decision)
| PR | Branch | Mergeable | Disposition |
|----|--------|-----------|------------|
| #13 | spec/runtime-vs-model-scope-decision | MERGEABLE | CONFLICTING_DUPLICATE — encodes Option C architecture |
| #16 | docs/scope-decision-runtime-vs-model-7 | MERGEABLE | CONFLICTING_DUPLICATE — encodes layered architecture |

**Recommended action:** Produce one reconciled ADR aligned with approved control-plane plan (#156). Retain one PR, close/supersede the other. Do not merge both.

### Group B: model-routing-as-code#8 (whole-codebase routing policy)
| PR | Branch | Mergeable | Disposition |
|----|--------|-----------|------------|
| #12 | spec/whole-codebase-routing-policy-v0.1 | CONFLICTING | SUPERSEDE_OR_CONSOLIDATE — non-mergeable, contains unrelated Ultra-evaluation material |
| #17 | docs/whole-codebase-routing-policy-8 | MERGEABLE | CONFLICTING_DUPLICATE — cleaner spec but lacks machine-readable policy and benchmark evidence |

**Recommended action:** Reconstruct intended policy on clean branch preserving valid work. Do not merge #12 in current form. #17 may serve as spec reference but does not complete implementation.

### Group C: hummbl-governance#225 (research integrity standard)
| PR | Branch | Mergeable | Disposition |
|----|--------|-----------|------------|
| #228 | spec/research-integrity-standard-v0.1 | MERGEABLE | CONFLICTING_DUPLICATE — materially fuller (schemas, templates, fixtures, adoption plan) |
| #233 | docs/research-integrity-standard-225 | MERGEABLE | SUPERSEDE_OR_CONSOLIDATE — narrower predecessor |

**Recommended action:** Reconcile unique text from #233 into #228. Mark #233 as superseded. #228 still requires primary-source inspection, independent review, and operator ratification.

### Group D: hummbl-bibliography#78 (corpus pack)
| PR | Branch | Mergeable | Disposition |
|----|--------|-----------|------------|
| #81 | spec/corpus-pack-v0.1 | MERGEABLE | SUPERSEDE_OR_CONSOLIDATE — non-mergeable diff, but has validated behavior and schema coverage |
| #84 | spec/benchmark-corpus-pack-v0.1 | MERGEABLE | CONFLICTING_DUPLICATE — cleaner candidate, but must preserve best of #81 |

**Recommended action:** Compare schema coverage and validated behavior. Preserve best of #81. Supersede #81 with #84 (or a clean reconstruction). Do not merge both.

## Blocker analysis (narrowed)

### Cross-Repo Contract Standard (hummbl-governance#234 / PR #235)
- **Current state:** SPEC_ONLY_IMPLEMENTATION_REQUIRED — one document, no schema/validator/fixtures
- **Blocks:** Integration/conformance portions of peptide infrastructure (#146) and routing vertical slice (#158) ONLY
- **Does NOT block:** Bibliography work, source-packet research, research agendas, benchmark harness code, scope-decision ADRs, bibliography source selection, or any non-integration work in those lanes

### hummbl-dev#184 (peptide integration)
- **Disposition:** BLOCKED_ON_DEPENDENCY — integration spec with material gates open
- **Gate:** Cross-repo contract implementation (not just spec)

### hummbl-dev#186 (routing vertical slice)
- **Disposition:** BLOCKED_ON_DEPENDENCY — vertical-slice spec with trace execution, economic receipt, benchmark result, observability evidence, independent review, and final disposition still open

### hummbl-papers#24 (OpenClaw × Hermes publication gate)
- **Disposition:** BLOCKED_ON_DEPENDENCY — explicitly states BLOCKED_ON_RESEARCH_AND_BENCHMARKS

### hummbl-dev#144 (storage hardening)
- **Disposition:** OPERATOR_GATED — blocked on credential rotation (Phase 0)

## Classification corrections applied

1. **hummbl-research#55** — ADDED to inventory (was omitted)
2. **autoresearch-pipeline#33** — linked to issue #32 (was shown with no issue)
3. **AI-source-verification PRs #20-25** — classified as SPEC_ONLY_IMPLEMENTATION_REQUIRED with DO_NOT_ADOPT_YET marker (was implied adoption-ready)
4. **hummbl-papers#15** — reclassified as STALE_RECEIPT_REQUIRES_UPDATE (was "leave as-is")
5. **hummbl-papers#24** — classified as BLOCKED_ON_DEPENDENCY (was implied reviewable)
6. **hummbl-dev#184, #186** — classified as BLOCKED_ON_DEPENDENCY (was implied reviewable)
7. **Lane 8 blocker** — narrowed to integration/conformance only (was overstated as blocking entire lanes)

## Machine-readable inventory

```csv
repository|number|item_type|title|state|draft|mergeable|primary_lane|secondary_lanes|source_issue|acceptance_status|validation_status|ci_status|independent_review_status|dependency_status|operator_gate|collision_group|supersedes|superseded_by|recommended_disposition|as_of|evidence_locator
hummbl-dev|166|pr|Resource isolation boundaries for parallel agent execution|OPEN|true|MERGEABLE|Lane-9-Agent-Discipline||#133|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-166
hummbl-dev|167|pr|Agent mutation guardrails for high-throughput agentic work|OPEN|true|MERGEABLE|Lane-9-Agent-Discipline||#131|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-167
hummbl-dev|168|pr|Process-patch receipt template for agent workflow failures|OPEN|true|MERGEABLE|Lane-9-Agent-Discipline||#132|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-168
hummbl-dev|169|pr|Razors for governed reasoning v0.1|OPEN|true|MERGEABLE|Lane-14-Razors||#142|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-169
hummbl-dev|170|pr|ChatGPT Work platform signal routing distinction v0.1|OPEN|true|MERGEABLE|Lane-13-ChatGPT-Voice||#139|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-170
hummbl-dev|171|pr|Frontier lab signal registry v0.1|OPEN|true|MERGEABLE|Lane-11-Frontier-Lab||#141|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-171
hummbl-dev|172|pr|ChatGPT session-closeout adapter v0.1|OPEN|true|MERGEABLE|Lane-13-ChatGPT-Voice|Lane-3-Handoffs|#160|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-172
hummbl-dev|173|pr|User-driven world model generation v0.1|OPEN|true|MERGEABLE|Lane-10-World-Models||#149|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-173
hummbl-dev|174|pr|Multi-actor world models v0.1|OPEN|true|MERGEABLE|Lane-10-World-Models||#151|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-174
hummbl-dev|175|pr|HUMMBL HUMINT foundation v0.1|OPEN|true|MERGEABLE|Lane-10-World-Models||#143|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-175
hummbl-dev|176|pr|Comparative agent runtime program v0.1 — OpenClaw x Hermes pilot|OPEN|true|MERGEABLE|Lane-7-Benchmark|Lane-1-Peptide|#152|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-176
hummbl-dev|177|pr|Repo portfolio gap, redundancy, and recomposition audit v0.1|OPEN|true|MERGEABLE|Lane-12-Topology||#148|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-177
hummbl-dev|178|pr|Development scale and collaboration intelligence v0.1|OPEN|true|MERGEABLE|Lane-12-Topology||#157|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-178
hummbl-dev|179|pr|HUMMBL whole-codebase and corpus intelligence benchmark v0.1|OPEN|true|MERGEABLE|Lane-7-Benchmark||#155|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-179
hummbl-dev|180|pr|Intentional repository scale and responsibility topology v0.1|OPEN|true|MERGEABLE|Lane-12-Topology||#154|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-180
hummbl-dev|181|pr|Peptide science knowledge infrastructure v0.1|OPEN|true|MERGEABLE|Lane-1-Peptide||#145|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-181
hummbl-dev|182|pr|Muse Spark 1.1 adapter and promotion benchmark v0.1|OPEN|true|MERGEABLE|Lane-11-Frontier-Lab|Lane-2-Routing|#147|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-182
hummbl-dev|183|pr|Migration assurance README v0.1|OPEN|true|MERGEABLE|Lane-17-Migration||#134|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-183
hummbl-dev|184|pr|Peptide infrastructure integration v0.1|OPEN|true|MERGEABLE|Lane-1-Peptide||#146|spec-complete|not-validated|unknown|not-reviewed|blocked-on-cross-repo-contract-implementation|none|none|none|none|BLOCKED_ON_DEPENDENCY|2026-07-11|pr-184
hummbl-dev|185|pr|Frontier Lab Classification v0.1|OPEN|true|MERGEABLE|Lane-11-Frontier-Lab||#140|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-185
hummbl-dev|186|pr|Routing control plane vertical slice v0.1|OPEN|true|MERGEABLE|Lane-2-Routing||#158|spec-complete|not-validated|unknown|not-reviewed|blocked-on-contract-and-execution-evidence|none|none|none|none|BLOCKED_ON_DEPENDENCY|2026-07-11|pr-186
hummbl-dev|187|pr|HUMMBL Conversation Lifecycle Protocol v0.1|OPEN|true|MERGEABLE|Lane-3-Handoffs||#159|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-187
hummbl-dev|188|pr|Manual Transfer Intake Gate v0.1.1-alpha|OPEN|true|MERGEABLE|Lane-3-Handoffs||#161|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-188
hummbl-dev|189|pr|Durable Intelligence Doctrine v0.1|OPEN|true|MERGEABLE|Lane-10-World-Models||#162|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-189
hummbl-dev|190|pr|HUMMBL Model Market & Routing Control Plane v0.1 plan|OPEN|true|MERGEABLE|Lane-2-Routing||#156|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-190
hummbl-dev|191|pr|Storage Hardening Execution Playbook v0.1|OPEN|true|MERGEABLE|Lane-16-Storage||#144|spec-complete|not-validated|unknown|not-reviewed|blocked-on-credential-rotation|yes|none|none|none|OPERATOR_GATED|2026-07-11|pr-191
hummbl-governance|228|pr|Research integrity & scholarly contribution standard v0.1|OPEN|true|MERGEABLE|Lane-5-Constitutional|Lane-6-Publications|#225|implementation-complete|not-validated|unknown|not-reviewed|none|none|Group-C|none|none|CONFLICTING_DUPLICATE|2026-07-11|pr-228
hummbl-governance|229|pr|Phase -1 report for Constitutional Systems Lab admission|OPEN|true|MERGEABLE|Lane-5-Constitutional||#224|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-229
hummbl-governance|230|pr|Constitution archetype matrix and authority-source matrix v0.1|OPEN|true|MERGEABLE|Lane-5-Constitutional||#223|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-230
hummbl-governance|231|pr|Constitution bounded remediation packet v0.1|OPEN|true|MERGEABLE|Lane-5-Constitutional||#220|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-231
hummbl-governance|232|pr|Durable intelligence doctrine v0.1|OPEN|true|MERGEABLE|Lane-5-Constitutional|Lane-10-World-Models|none|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-232
hummbl-governance|233|pr|HUMMBL Research Integrity Standard v0.1|OPEN|true|MERGEABLE|Lane-5-Constitutional|Lane-6-Publications|#225|spec-complete|not-validated|unknown|not-reviewed|none|none|Group-C|none|pr-228|SUPERSEDE_OR_CONSOLIDATE|2026-07-11|pr-233
hummbl-governance|235|pr|Cross-Repo Contract Standard v0.1|OPEN|true|MERGEABLE|Lane-8-Cross-Repo-Contract||#234|spec-only|not-validated|unknown|not-reviewed|implementation-required|none|none|none|none|SPEC_ONLY_IMPLEMENTATION_REQUIRED|2026-07-11|pr-235
hummbl-papers|21|pr|Universal publication readiness gate v0.1|OPEN|true|MERGEABLE|Lane-6-Publications||#19|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-21
hummbl-papers|22|pr|LLL Engineering research protocol and prior-art search plan v0.1|OPEN|true|MERGEABLE|Lane-6-Publications||#20|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-22
hummbl-papers|23|pr|Peptide Science Field Atlas v0.1|OPEN|true|MERGEABLE|Lane-1-Peptide|Lane-6-Publications|#17|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-23
hummbl-papers|24|pr|OpenClaw × Hermes publication gate v0.1|OPEN|true|MERGEABLE|Lane-6-Publications|Lane-7-Benchmark|#18|spec-complete|not-validated|unknown|not-reviewed|blocked-on-research-and-benchmarks|none|none|none|none|BLOCKED_ON_DEPENDENCY|2026-07-11|pr-24
hummbl-bibliography|81|pr|Corpus pack v0.1 — source-selection proposal, schemas, validator|OPEN|true|MERGEABLE|Lane-6-Publications||#78|implementation-complete|not-validated|unknown|not-reviewed|none|none|Group-D|none|pr-84|SUPERSEDE_OR_CONSOLIDATE|2026-07-11|pr-81
hummbl-bibliography|82|pr|Peptide science bibliography registry v0.1|OPEN|true|MERGEABLE|Lane-1-Peptide|Lane-6-Publications|#77|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-82
hummbl-bibliography|84|pr|Benchmark corpus pack v0.1 — source-selection proposal|OPEN|true|MERGEABLE|Lane-6-Publications||#78|spec-complete|not-validated|unknown|not-reviewed|none|none|Group-D|pr-81|none|CONFLICTING_DUPLICATE|2026-07-11|pr-84
hummbl-research|53|pr|ChatGPT Voice interaction laboratory and evidence packet v0.1|OPEN|true|MERGEABLE|Lane-13-ChatGPT-Voice||#51|implementation-complete|not-validated|unknown|not-reviewed|none|none|none|none|IMPLEMENTATION_COMPLETE_PENDING_INDEPENDENT_REVIEW|2026-07-11|pr-53
hummbl-research|54|pr|Peptide science research agenda v0.1|OPEN|true|MERGEABLE|Lane-1-Peptide||#47|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-54
hummbl-research|55|pr|fix(ci): avoid duplicate markdown lint runs|OPEN|true|MERGEABLE|Lane-6-Publications||none|implementation-complete|not-validated|unknown|not-reviewed|none|none|none|none|IMPLEMENTATION_COMPLETE_PENDING_INDEPENDENT_REVIEW|2026-07-11|pr-55
claim-evidence-ledger|11|pr|Peptide claim/evidence ledger v0.1|OPEN|true|MERGEABLE|Lane-1-Peptide||#8|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-11
claim-evidence-ledger|12|pr|Peptide Claim/Evidence Seed Dataset v0.1|OPEN|true|MERGEABLE|Lane-1-Peptide||#9|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-12
claim-evidence-ledger|13|pr|Comparative Agent System Ledger v0.1|OPEN|true|MERGEABLE|Lane-1-Peptide|Lane-7-Benchmark|#10|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-13
ai-source-verification|20|pr|EvalReceipt v0.1 candidate schema|OPEN|true|MERGEABLE|Lane-4-AI-Verification||#14|spec-only-do-not-adopt|not-validated|unknown|not-reviewed|none|none|none|none|SPEC_ONLY_IMPLEMENTATION_REQUIRED|2026-07-11|pr-20
ai-source-verification|21|pr|TrainingRunReceipt v0.1 candidate schema|OPEN|true|MERGEABLE|Lane-4-AI-Verification||#10|spec-only-do-not-adopt|not-validated|unknown|not-reviewed|none|none|none|none|SPEC_ONLY_IMPLEMENTATION_REQUIRED|2026-07-11|pr-21
ai-source-verification|22|pr|Governed EnvironmentContract v0.1 candidate schema|OPEN|true|MERGEABLE|Lane-4-AI-Verification||#15|spec-only-do-not-adopt|not-validated|unknown|not-reviewed|none|none|none|none|SPEC_ONLY_IMPLEMENTATION_REQUIRED|2026-07-11|pr-22
ai-source-verification|23|pr|Specialist Subagent Assurance Profile v0.1|OPEN|true|MERGEABLE|Lane-4-AI-Verification||#11|spec-only-do-not-adopt|not-validated|unknown|not-reviewed|none|none|none|none|SPEC_ONLY_IMPLEMENTATION_REQUIRED|2026-07-11|pr-23
ai-source-verification|24|pr|Ownward Voice Runtime Training/Eval Boundary v0.1|OPEN|true|MERGEABLE|Lane-4-AI-Verification|Lane-13-ChatGPT-Voice|#12|spec-only-do-not-adopt|not-validated|unknown|not-reviewed|none|none|none|none|SPEC_ONLY_IMPLEMENTATION_REQUIRED|2026-07-11|pr-24
ai-source-verification|25|pr|RuntimeVendor Watchlist v0.1|OPEN|true|MERGEABLE|Lane-4-AI-Verification|Lane-2-Routing|#13|spec-only-do-not-adopt|not-validated|unknown|not-reviewed|none|none|none|none|SPEC_ONLY_IMPLEMENTATION_REQUIRED|2026-07-11|pr-25
ai-source-verification|26|pr|Peptide AI/ML Assurance v0.1|OPEN|true|MERGEABLE|Lane-1-Peptide|Lane-4-AI-Verification|#19|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-26
knowledge-as-code|7|pr|Peptide identity ontology and read API v0.1|OPEN|true|MERGEABLE|Lane-1-Peptide||#6|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-7
hummbl-medical|15|pr|Peptide translation and medical governance v0.1|OPEN|true|MERGEABLE|Lane-1-Peptide||#14|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-15
autoresearch-pipeline|33|pr|Voice runtime benchmark harness v0.1 (mock adapter, 12 scenarios)|OPEN|true|MERGEABLE|Lane-7-Benchmark|Lane-13-ChatGPT-Voice|#32|implementation-complete|reported-96-tests-36-subtests|unknown|not-reviewed|none|none|none|none|IMPLEMENTATION_COMPLETE_PENDING_INDEPENDENT_REVIEW|2026-07-11|pr-33
autoresearch-pipeline|34|pr|Whole-codebase & corpus intelligence benchmark harness v0.1|OPEN|true|MERGEABLE|Lane-7-Benchmark||#30|implementation-complete|not-validated|unknown|not-reviewed|none|none|none|none|IMPLEMENTATION_COMPLETE_PENDING_INDEPENDENT_REVIEW|2026-07-11|pr-34
autoresearch-pipeline|35|pr|HUMMBL routing benchmark harness v0.1|OPEN|true|MERGEABLE|Lane-2-Routing|Lane-7-Benchmark|#31|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-35
autoresearch-pipeline|36|pr|Comparative agent runtime benchmark harness v0.1|OPEN|true|MERGEABLE|Lane-7-Benchmark||#29|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-36
observability-as-code|8|pr|Model-routing observability v0.1|OPEN|true|MERGEABLE|Lane-2-Routing||#7|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-8
execution-receipts|11|pr|Conversation closeout receipt profile v0.1|OPEN|true|MERGEABLE|Lane-3-Handoffs||#10|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-11
execution-receipts|12|pr|Model-route economic receipt v0.1|OPEN|true|MERGEABLE|Lane-2-Routing||#9|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-12
agent-handoffs|10|pr|Conversation/work-session handoff profile v0.1|OPEN|true|MERGEABLE|Lane-3-Handoffs||#9|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-10
agent-handoffs|11|pr|Belief-aware agent handoffs v0.1|OPEN|true|MERGEABLE|Lane-3-Handoffs||#8|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-11
protocol-as-code|8|pr|Conversation lifecycle protocol v0.1|OPEN|true|MERGEABLE|Lane-3-Handoffs||#7|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-8
model-routing-as-code|12|pr|Whole-codebase and corpus model routing policy v0.1|OPEN|true|CONFLICTING|Lane-2-Routing||#8|implementation-incomplete|not-validated|unknown|not-reviewed|none|none|Group-B|none|pr-17|SUPERSEDE_OR_CONSOLIDATE|2026-07-11|pr-12
model-routing-as-code|13|pr|Scope decision — runtime vs model selection (Option C)|OPEN|true|MERGEABLE|Lane-2-Routing||#7|implementation-complete|not-validated|unknown|not-reviewed|none|none|Group-A|none|none|CONFLICTING_DUPLICATE|2026-07-11|pr-13
model-routing-as-code|14|pr|refactor: decompose Ultra receipt validator semantics|OPEN|true|MERGEABLE|Lane-2-Routing||#11|implementation-complete|not-validated|unknown|not-reviewed|none|none|none|none|IMPLEMENTATION_COMPLETE_PENDING_INDEPENDENT_REVIEW|2026-07-11|pr-14
model-routing-as-code|15|pr|Governed sol route evaluation scaffold|OPEN|true|MERGEABLE|Lane-2-Routing||none|implementation-complete|not-validated|unknown|not-reviewed|none|none|none|none|IMPLEMENTATION_COMPLETE_PENDING_INDEPENDENT_REVIEW|2026-07-11|pr-15
model-routing-as-code|16|pr|Scope decision runtime vs model routing v0.1|OPEN|true|MERGEABLE|Lane-2-Routing||#7|spec-complete|not-validated|unknown|not-reviewed|none|none|Group-A|none|none|CONFLICTING_DUPLICATE|2026-07-11|pr-16
model-routing-as-code|17|pr|Whole-codebase routing policy v0.1|OPEN|true|MERGEABLE|Lane-2-Routing||#8|spec-only|not-validated|unknown|not-reviewed|implementation-required|none|Group-B|none|none|CONFLICTING_DUPLICATE|2026-07-11|pr-17
model-routing-as-code|18|pr|Agent execution packet v0.1|OPEN|true|MERGEABLE|Lane-2-Routing||#9|spec-complete|not-validated|unknown|not-reviewed|none|none|none|none|REVIEWABLE_SPEC|2026-07-11|pr-18
```

## Open issues (no PR) — machine-readable

```csv
repository|number|item_type|title|state|primary_lane|recommended_disposition|as_of
hummbl-dev|131|issue|Guardrails: Agent mutation discipline|OPEN|Lane-9|has-pr-167|2026-07-11
hummbl-dev|132|issue|Receipts: Process-patch log for agent workflow failures|OPEN|Lane-9|has-pr-168|2026-07-11
hummbl-dev|133|issue|Protocol: Resource isolation boundaries|OPEN|Lane-9|has-pr-166|2026-07-11
hummbl-dev|134|issue|Docs spine: Migration assurance README|OPEN|Lane-17|has-pr-183|2026-07-11
hummbl-dev|139|issue|ChatGPT Work platform-signal intake|OPEN|Lane-13|has-pr-170|2026-07-11
hummbl-dev|140|issue|Frontier Lab Classification|OPEN|Lane-11|has-pr-185|2026-07-11
hummbl-dev|141|issue|Frontier Lab Signal Registry|OPEN|Lane-11|has-pr-171|2026-07-11
hummbl-dev|142|issue|Razors for Governed Reasoning|OPEN|Lane-14|has-pr-169|2026-07-11
hummbl-dev|143|issue|HUMMBL HUMINT foundation|OPEN|Lane-10|has-pr-175|2026-07-11
hummbl-dev|144|issue|Storage hardening|OPEN|Lane-16|OPERATOR_GATED|2026-07-11
hummbl-dev|145|issue|Peptide Science Knowledge Infrastructure|OPEN|Lane-1|has-pr-181|2026-07-11
hummbl-dev|146|issue|Peptide Infrastructure Integration|OPEN|Lane-1|has-pr-184-blocked|2026-07-11
hummbl-dev|147|issue|Muse Spark 1.1 adapter|OPEN|Lane-11|has-pr-182|2026-07-11
hummbl-dev|148|issue|Repo Portfolio Audit|OPEN|Lane-12|has-pr-177|2026-07-11
hummbl-dev|149|issue|User-Driven World Model Generation|OPEN|Lane-10|has-pr-173|2026-07-11
hummbl-dev|150|issue|Route user-model assurance work|OPEN|Lane-18|STANDING_COORDINATION|2026-07-11
hummbl-dev|151|issue|Multi-Actor World Models|OPEN|Lane-10|has-pr-174|2026-07-11
hummbl-dev|152|issue|Comparative Agent Runtime Program|OPEN|Lane-7|has-pr-176|2026-07-11
hummbl-dev|153|issue|Master program index|OPEN|Lane-18|STANDING_COORDINATION|2026-07-11
hummbl-dev|154|issue|Intentional Repository Scale|OPEN|Lane-12|has-pr-180|2026-07-11
hummbl-dev|155|issue|Whole-Codebase Benchmark|OPEN|Lane-7|has-pr-179|2026-07-11
hummbl-dev|156|issue|Model Market & Routing Control Plane plan|OPEN|Lane-2|has-pr-190|2026-07-11
hummbl-dev|157|issue|Development Scale & Collaboration Intelligence|OPEN|Lane-12|has-pr-178|2026-07-11
hummbl-dev|158|issue|Routing control plane vertical slice|OPEN|Lane-2|has-pr-186-blocked|2026-07-11
hummbl-dev|159|issue|Conversation Lifecycle Protocol|OPEN|Lane-3|has-pr-187|2026-07-11
hummbl-dev|160|issue|ChatGPT session-closeout adapter|OPEN|Lane-13|has-pr-172|2026-07-11
hummbl-dev|161|issue|Manual Transfer Intake Gate|OPEN|Lane-3|has-pr-188|2026-07-11
hummbl-dev|162|issue|Durable Intelligence Doctrine|OPEN|Lane-10|has-pr-189|2026-07-11
hummbl-dev|164|issue|Execution wave: Voice and OpenAI July 2026|OPEN|Lane-18|STANDING_COORDINATION|2026-07-11
hummbl-dev|165|issue|Agent notice: HUMMBL Drive OS routing|OPEN|Lane-18|STANDING_COORDINATION|2026-07-11
hummbl-governance|220|issue|Constitutional Integrity Remediation|OPEN|Lane-5|has-pr-231|2026-07-11
hummbl-governance|221|issue|Constitutional Truth and Reference Integrity|OPEN|Lane-5|NOT_READY|2026-07-11
hummbl-governance|222|issue|Constitutional Authority and Duplication|OPEN|Lane-5|NOT_READY|2026-07-11
hummbl-governance|223|issue|Constitutional Archetypes and Template Evolution|OPEN|Lane-5|has-pr-230|2026-07-11
hummbl-governance|224|issue|Phase -1 admission: Constitutional Systems Lab|OPEN|Lane-5|has-pr-229|2026-07-11
hummbl-governance|225|issue|Research Integrity Standard|OPEN|Lane-5|has-pr-228-collision|2026-07-11
hummbl-governance|226|issue|Admit EXP-0001 bounded GitHub issue authority|OPEN|Lane-5|NOT_READY|2026-07-11
hummbl-governance|234|issue|Cross-Repo Contract Standard|OPEN|Lane-8|has-pr-235-spec-only|2026-07-11
hummbl-governance|188|issue|Draft PR Promotion Queue|OPEN|Lane-18|STANDING_COORDINATION|2026-07-11
hummbl-governance|190|issue|Review Debt & Merge Gate Queue|OPEN|Lane-18|STANDING_COORDINATION|2026-07-11
hummbl-papers|12|issue|Seed first paper from founder-mode hardening sprint|OPEN|Lane-6|NOT_READY|2026-07-11
hummbl-papers|15|issue|Scientific Grounding Batch Receipt|OPEN|Lane-6|STALE_RECEIPT_REQUIRES_UPDATE|2026-07-11
hummbl-papers|17|issue|Peptide Science Field Atlas|OPEN|Lane-1|has-pr-23|2026-07-11
hummbl-papers|18|issue|Publication gate: OpenClaw × Hermes|OPEN|Lane-6|has-pr-24-blocked|2026-07-11
hummbl-papers|19|issue|Universal Publication Readiness Gate|OPEN|Lane-6|has-pr-21|2026-07-11
hummbl-papers|20|issue|LLL Engineering scholarly contribution program|OPEN|Lane-6|has-pr-22|2026-07-11
hummbl-bibliography|77|issue|Peptide Science Bibliography|OPEN|Lane-1|has-pr-82|2026-07-11
hummbl-bibliography|78|issue|Benchmark corpus pack|OPEN|Lane-6|has-pr-84-collision|2026-07-11
hummbl-bibliography|85|issue|Triage: ci.yml warn-only dependency audit|OPEN|Lane-6|NOT_READY|2026-07-11
hummbl-research|47|issue|Peptide Science Research Agenda|OPEN|Lane-1|has-pr-54|2026-07-11
hummbl-research|48|issue|Research campaign: OpenClaw × Hermes|OPEN|Lane-7|NOT_READY|2026-07-11
hummbl-research|51|issue|ChatGPT Voice interaction laboratory|OPEN|Lane-13|has-pr-53|2026-07-11
hummbl-research|56|issue|Standing ledger: External Claims|OPEN|Lane-18|STANDING_COORDINATION|2026-07-11
hummbl-research|57|issue|Standing ledger: prior art|OPEN|Lane-18|STANDING_COORDINATION|2026-07-11
hummbl-research|58|issue|Standing ledger: frontier model releases|OPEN|Lane-18|STANDING_COORDINATION|2026-07-11
claim-evidence-ledger|8|issue|Peptide Claim/Evidence Ledger|OPEN|Lane-1|has-pr-11|2026-07-11
claim-evidence-ledger|9|issue|Peptide Evidence Seed|OPEN|Lane-1|has-pr-12|2026-07-11
claim-evidence-ledger|10|issue|Comparative agent-system ledger|OPEN|Lane-1|has-pr-13|2026-07-11
ai-source-verification|10|issue|TrainingRunReceipt|OPEN|Lane-4|has-pr-21-do-not-adopt|2026-07-11
ai-source-verification|11|issue|Specialist Subagent Assurance Profile|OPEN|Lane-4|has-pr-23-do-not-adopt|2026-07-11
ai-source-verification|12|issue|Ownward Voice Runtime Training/Eval Boundary|OPEN|Lane-4|has-pr-24-do-not-adopt|2026-07-11
ai-source-verification|13|issue|RuntimeVendor Watchlist|OPEN|Lane-4|has-pr-25-do-not-adopt|2026-07-11
ai-source-verification|14|issue|EvalReceipt|OPEN|Lane-4|has-pr-20-do-not-adopt|2026-07-11
ai-source-verification|15|issue|Governed EnvironmentContract|OPEN|Lane-4|has-pr-22-do-not-adopt|2026-07-11
ai-source-verification|19|issue|Peptide AI/ML Assurance|OPEN|Lane-1|has-pr-26|2026-07-11
knowledge-as-code|6|issue|Peptide Identity Ontology|OPEN|Lane-1|has-pr-7|2026-07-11
hummbl-medical|14|issue|Peptide Translation and Medical Governance|OPEN|Lane-1|has-pr-15|2026-07-11
autoresearch-pipeline|29|issue|Benchmark harness: comparative agent runtime|OPEN|Lane-7|has-pr-36|2026-07-11
autoresearch-pipeline|30|issue|Whole-codebase benchmark harness|OPEN|Lane-7|has-pr-34|2026-07-11
autoresearch-pipeline|31|issue|HUMMBL routing benchmark harness|OPEN|Lane-2|has-pr-35|2026-07-11
autoresearch-pipeline|32|issue|Comparative voice-runtime benchmark harness|OPEN|Lane-7|has-pr-33|2026-07-11
observability-as-code|7|issue|Model-routing observability|OPEN|Lane-2|has-pr-8|2026-07-11
execution-receipts|9|issue|Model-route economic receipt|OPEN|Lane-2|has-pr-12|2026-07-11
execution-receipts|10|issue|Conversation closeout receipt profile|OPEN|Lane-3|has-pr-11|2026-07-11
agent-handoffs|8|issue|Belief-Aware Agent Handoffs|OPEN|Lane-3|has-pr-11|2026-07-11
agent-handoffs|9|issue|Conversation/work-session handoff profile|OPEN|Lane-3|has-pr-10|2026-07-11
protocol-as-code|7|issue|Conversation Lifecycle Protocol|OPEN|Lane-3|has-pr-8|2026-07-11
model-routing-as-code|7|issue|Scope decision: runtime vs model routing|OPEN|Lane-2|has-pr-13-collision|2026-07-11
model-routing-as-code|8|issue|Whole-codebase routing policy|OPEN|Lane-2|has-pr-17-collision|2026-07-11
model-routing-as-code|9|issue|Agent execution packet|OPEN|Lane-2|has-pr-18|2026-07-11
model-routing-as-code|11|issue|refactor: decompose Ultra receipt validator|OPEN|Lane-2|has-pr-14|2026-07-11
research-source-packets|11|issue|Peptide Science Source Packet|OPEN|Lane-15|NOT_READY|2026-07-11
research-source-packets|12|issue|Public source packet: OpenClaw × Hermes|OPEN|Lane-15|NOT_READY|2026-07-11
research-source-packets|13|issue|Pi CLI adoption evidence packet|OPEN|Lane-15|NOT_READY|2026-07-11
research-source-packets|14|issue|Teardown: promptfoo Pi provider PR|OPEN|Lane-15|NOT_READY|2026-07-11
research-source-packets|15|issue|Teardown: T3 Code Pi RPC provider PR|OPEN|Lane-15|NOT_READY|2026-07-11
research-source-packets|16|issue|Pi CLI on ARM64 edge hardware|OPEN|Lane-15|NOT_READY|2026-07-11
research-source-packets|17|issue|Development Scale Signals Source Packet|OPEN|Lane-15|NOT_READY|2026-07-11
```

## Reconciliation report

### Corrections applied from ChatGPT audit

| # | Finding | Correction |
|---|---------|------------|
| 1 | "Complete ecosystem map" is false | Renamed to "Selected HUMMBL Program Portfolio" with bounded scope statement |
| 2 | 73 PRs claimed, 78 in summary, lane headings undercount | Reconciled to 72 unique PRs (verified against live GitHub) |
| 3 | hummbl-research#55 omitted | ADDED to inventory |
| 4 | autoresearch-pipeline#33 mislinked | Linked to issue #32 |
| 5 | AI-source-verification PRs implied adoption-ready | Reclassified as SPEC_ONLY_IMPLEMENTATION_REQUIRED with DO_NOT_ADOPT marker |
| 6 | hummbl-papers#24 implied reviewable | Reclassified as BLOCKED_ON_DEPENDENCY |
| 7 | hummbl-papers#15 "leave as-is" | Reclassified as STALE_RECEIPT_REQUIRES_UPDATE |
| 8 | Lane 8 blocker overstated | Narrowed to integration/conformance portions only |
| 9 | hummbl-dev#184, #186 implied reviewable | Reclassified as BLOCKED_ON_DEPENDENCY |
| 10 | No collision section | Added 4 collision groups with adjudication recommendations |
| 11 | "Ready for review/merge" unsafe | Replaced with 10-disposition model |
| 12 | PR existence = issue complete | Explicitly rejected in disposition model |

### Count reconciliation

| Measure | Previous (rejected) | Corrected |
|---------|--------------------:|----------:|
| PR placements | 78 (inflated) | 72 (unique, verified) |
| Unique PRs | 71 | 72 |
| Open issues | ~50 | 31 unique + 9 standing = 40 |
| Execution lanes | 16 | 17 |
| Collision groups | 0 | 4 |
| DO_NOT_ADOPT PRs | not flagged | 6 |
| BLOCKED PRs | not flagged | 3 |

## Recommended close/supersede/rebuild actions

### Close (supersede)
1. **model-routing-as-code#12** — SUPERSEDE_OR_CONSOLIDATE. Non-mergeable, contains unrelated Ultra-evaluation material. Reconstruct on clean branch.
2. **hummbl-governance#233** — SUPERSEDE_OR_CONSOLIDATE. Narrower predecessor of #228. Reconcile unique text, then close.
3. **hummbl-bibliography#81** — SUPERSEDE_OR_CONSOLIDATE. Non-mergeable diff but has validated behavior. Preserve best, supersede with #84 or clean reconstruction.

### Adjudicate (retain one, close other)
4. **model-routing-as-code#13 vs #16** — CONFLICTING_DUPLICATE. Produce one reconciled ADR. Retain one, close other.

### Update (stale receipt)
5. **hummbl-papers#15** — STALE_RECEIPT_REQUIRES_UPDATE. Dependencies (hummbl-research#42, #44) are merged. Add dated supersession comment. Close or convert to standing ledger.

### Rebuild (contaminated branch)
6. **model-routing-as-code#12** — Reconstruct intended policy on clean branch preserving valid work only.

### Do NOT merge until gates resolve
7. **hummbl-dev#184** — BLOCKED_ON_DEPENDENCY (cross-repo contract implementation)
8. **hummbl-dev#186** — BLOCKED_ON_DEPENDENCY (contract + execution evidence)
9. **hummbl-papers#24** — BLOCKED_ON_DEPENDENCY (research + benchmarks)
10. **hummbl-dev#191** — OPERATOR_GATED (credential rotation)

### Do NOT adopt (spec only)
11. **ai-source-verification#20-25** — SPEC_ONLY_IMPLEMENTATION_REQUIRED, explicitly marked DO_NOT_ADOPT_YET

## Revised execution priority

### Priority 0 — Inventory truth and review-debt containment
1. Regenerate portfolio from live GitHub state (DONE — this document)
2. Deduplicate PRs and issues by canonical repository-number identity (DONE)
3. Adjudicate all competing PR pairs (PENDING — 4 groups)
4. Identify non-mergeable, contaminated, stale, and superseded branches (DONE — 3 supersede, 1 stale)
5. Stop equating "has a PR" with "issue execution complete" (DONE — disposition model applied)

### Priority 1 — Constitutional truth and authority remediation
- hummbl-governance#221 — Constitutional Truth and Reference Integrity
- hummbl-governance#222 — Constitutional Authority and Duplication
- Keep #226 as separate bounded authority decision

### Priority 2 — Resolve duplicate architecture and standard PRs
- Group A: routing scope #13/#16
- Group B: routing policy #12/#17
- Group C: research integrity #228/#233
- Group D: corpus pack #81/#84

### Priority 3 — Implement Cross-Repo Contract Standard
9 implementation slices (schema, definitions, validator, fixtures, receipts, migration, validation chain, peptide pilot, AAR)

### Priority 4 — Review implementation-complete bounded candidates
- model-routing-as-code#14
- autoresearch-pipeline#33
- autoresearch-pipeline#34
- hummbl-research#53
- hummbl-research#55
- model-routing-as-code#15

### Priority 5 — Continue unblocked evidence-substrate work
- research-source packets (7 issues)
- bibliography/source-registry work
- benchmark corpus source selection
- benchmark fixture preparation

### Priority 6 — Execute integration programs after gates resolve
- peptide cross-repo integration
- routing-control-plane vertical slice

### Priority 7 — Operator-only storage hardening
- Credential rotation (Phase 0)
- Cleanup (Phase 1)
- Media hardening (Phase 2)

### Priority 8 — Preserve standing surfaces
- hummbl-dev #150, #153, #164, #165
- hummbl-governance #188, #190
- hummbl-research #56, #57, #58

## Fact posture

- This is a corrected inventory derived from live GitHub state on 2026-07-11
- Scope is bounded to 16 selected repositories
- No PR has been merged, closed, or superseded
- No additional PRs have been created
- All counts reconcile to the machine-readable inventory
- "Ready for merge" is not used for any item
- Every conflicting duplicate has an explicit adjudication state
- Every blocker names the exact unsatisfied gate
