# Razors for Governed Reasoning v0.1

**Status: CANDIDATE — NON-CANONICAL — PROVENANCE AUDIT REQUIRED**

Issue: hummbl-dev/hummbl-dev#142

This document preserves and operationalizes a proposed Razors for Governed Reasoning v0.1 framework. It extends Hanlon's Razor: a reasoning heuristic should not merely influence what we believe; it should shape how we treat people, change systems, evaluate evidence, and impose accountability.

## Provenance posture

No wording in this document is represented as an original historical quotation unless provenance is independently verified. Popular paraphrases are clearly labeled. HUMMBL-authored behavioral extensions are visibly marked as candidate.

## Glossary

| Term | Definition |
|------|-----------|
| Razor | A reasoning heuristic that eliminates unnecessary assumptions or explanations |
| Standard | A normative criterion for evidence quality or claim strength |
| Law | An observed regularity in systems or organizations (not a physical law) |
| Heuristic | A practical shortcut that works often but is not guaranteed |
| Principle | A general normative guideline for conduct or design |
| Doctrine | A binding organizational rule requiring compliance |

## Entry schema

Every razor or related principle uses the same schema:

- **id**: stable-kebab-case-id
- **name**: conventional name
- **class**: razor | standard | law | heuristic | doctrine
- **historical_formulation**: quoted wording only if verified
- **common_paraphrase**: clearly labeled paraphrase
- **candidate_expansion**: HUMMBL-authored behavioral extension (CANDIDATE)
- **reasoning_function**: what cognitive failure it addresses
- **behavioral_implication**: how it should affect conduct toward others
- **operational_test**: a question or test an agent or person can apply
- **misuse_risk**: how the principle can become harmful or misleading
- **accountability_transition**: when charity, caution, or restraint should give way to action
- **provenance**: verified | partially_verified | unresolved
- **canonical_status**: candidate

## Provenance table

| # | Name | Class | Provenance | Source status |
|---|------|-------|-----------|---------------|
| 1 | Occam's Razor | razor | partially_verified | Attributed to William of Ockham (c. 1287–1347); exact wording disputed |
| 2 | Hanlon's Razor | razor | partially_verified | Attributed to Robert J. Hanlon; exact origin unclear |
| 3 | Hitchens's Razor | razor | partially_verified | Christopher Hitchens; popular formulation |
| 4 | Sagan Standard | standard | partially_verified | Carl Sagan; popular formulation "extraordinary claims..." |
| 5 | Alder's Razor | razor | partially_verified | Mike Alder; Newton's Flaming Laser Sword |
| 6 | Chesterton's Fence | heuristic | partially_verified | G.K. Chesterton; 1929 essay |
| 7 | Grice's Razor | razor | partially_verified | Paul Grice; cooperative principle |
| 8 | Ad hoc rescue | heuristic | unresolved | General philosophy of science; no single origin |
| 9 | "If it isn't broken" | heuristic | unresolved | Popular engineering maxim; origin unclear |
| 10 | Goodhart's Law | law | partially_verified | Charles Goodhart; 1975 paper |
| 11 | Campbell's Law | law | partially_verified | Donald T. Campbell; 1976 paper |
| 12 | Conway's Law | law | partially_verified | Melvin Conway; 1967 |
| 13 | Parkinson's Law | law | partially_verified | C. Northcote Parkinson; 1955 essay |
| 14 | Hofstadter's Law | law | partially_verified | Douglas Hofstadter; 1979 |
| 15 | Brooks's Law | law | partially_verified | Fred Brooks; 1975, The Mythical Man-Month |

All entries: canonical_status = **candidate**. Historical formulations are popular paraphrases unless independently verified against primary sources.

## Decision matrix

| Razor | Claims | People | Systems | Metrics | Architecture | Project execution |
|-------|--------|--------|---------|---------|-------------|-------------------|
| Occam | ✓ | ✓ | | | ✓ | |
| Hanlon | | ✓ | | | | ✓ |
| Hitchens | ✓ | | | | | |
| Sagan | ✓ | | | ✓ | | |
| Alder | ✓ | | | | | |
| Chesterton | | | ✓ | ✓ | ✓ | ✓ |
| Grice | | ✓ | | | | ✓ |
| Ad hoc rescue | ✓ | | ✓ | ✓ | | |
| If it isn't broken | | | ✓ | | ✓ | ✓ |
| Goodhart | | | ✓ | ✓ | | ✓ |
| Campbell | | | | ✓ | | ✓ |
| Conway | | | | | ✓ | ✓ |
| Parkinson | | | | | | ✓ |
| Hofstadter | | | | | | ✓ |
| Brooks | | | | | | ✓ |

## Entries

### 1. Occam's Razor

- **id**: occams-razor
- **name**: Occam's Razor
- **class**: razor
- **historical_formulation**: "Entities should not be multiplied beyond necessity" (paraphrase; original Latin wording disputed)
- **common_paraphrase**: The simplest explanation is usually the correct one
- **candidate_expansion** (CANDIDATE): Among competing explanations that fit the available evidence, prefer the one requiring the fewest unsupported assumptions. Begin with the simplest sufficient model, but do not confuse simplicity with truth. Test it, remain open to complexity, and add assumptions only when evidence requires them.
- **reasoning_function**: Overcomplication; inventing elaborate explanations when simpler ones fit
- **behavioral_implication**: Do not invent elaborate stories about another person's motives when a direct explanation fits the facts
- **operational_test**: What assumptions am I adding that the evidence does not require?
- **misuse_risk**: Treating "simple" as synonymous with "correct," or erasing genuine complexity
- **accountability_transition**: When evidence accumulates that the simple model cannot explain, complexity becomes necessary, not optional
- **provenance**: partially_verified
- **canonical_status**: candidate

**Compact form:** Start simple. Test honestly. Add complexity only when reality requires it.

**Agent governance example:** When diagnosing a test failure, prefer "the test is correct and the code is broken" over "the test, CI, runtime, and environment are all simultaneously broken in a coordinated way" — unless evidence supports the broader failure.

---

### 2. Hanlon's Razor

- **id**: hanlons-razor
- **name**: Hanlon's Razor
- **class**: razor
- **historical_formulation**: "Never attribute to malice that which is adequately explained by stupidity" (popular paraphrase; origin attributed to Robert J. Hanlon, 1980)
- **common_paraphrase**: Don't assume bad intent when ignorance or incompetence suffices
- **candidate_expansion** (CANDIDATE): Never attribute to malice what can be adequately explained by ignorance, misunderstanding, incompetence, distraction, or conflicting incentives. Begin with curiosity rather than accusation, offer clarity before condemnation, and reserve stronger judgment for patterns that persist after understanding and an opportunity to correct them.
- **reasoning_function**: Hostile attribution bias; assuming ill intent when neutral explanations suffice
- **behavioral_implication**: Ask before accusing. Clarify before escalating. Teach before punishing.
- **operational_test**: Has this person been given clear information, usable feedback, and a genuine opportunity to change?
- **misuse_risk**: Using charity to excuse repeated or intentional harm; treating accountability as unkind
- **accountability_transition**: Repeated harm after clear feedback may no longer be adequately explained by ignorance
- **provenance**: partially_verified
- **canonical_status**: candidate

**Compact form:** Lead with curiosity. Follow with clarity. End with accountability.

**Agent governance example:** When an agent produces a wrong result, first check whether the instructions were ambiguous before assuming the agent "decided" to cut corners.

---

### 3. Hitchens's Razor

- **id**: hitchenss-razor
- **name**: Hitchens's Razor
- **class**: razor
- **historical_formulation**: "What can be asserted without evidence can also be dismissed without evidence" (Christopher Hitchens, 2003)
- **common_paraphrase**: Claims made without evidence can be rejected without evidence
- **candidate_expansion** (CANDIDATE): What is asserted without adequate evidence need not be accepted without adequate evidence. The claimant carries the burden of support; skepticism does not require disproving every unsupported possibility.
- **reasoning_function**: Shifting the burden of proof; demanding disproof of unsupported claims
- **behavioral_implication**: Do not let certainty, repetition, authority, or emotional force substitute for evidence
- **operational_test**: What evidence supports the claim, and who bears the burden of producing it?
- **misuse_risk**: Treating "not established" as "proven false"
- **accountability_transition**: When evidence is requested and refused, the absence becomes evidence of the claim's weakness
- **provenance**: partially_verified
- **canonical_status**: candidate

**Compact form:** Do not confuse an unrefuted claim with an established one.

**Agent governance example:** An agent claiming "this approach is faster" without benchmarks need not be refuted with benchmarks — the claim can be dismissed until evidence is produced.

---

### 4. Sagan Standard

- **id**: sagan-standard
- **name**: Sagan Standard
- **class**: standard
- **historical_formulation**: "Extraordinary claims require extraordinary evidence" (Carl Sagan, popular paraphrase)
- **common_paraphrase**: Bigger claims need bigger proof
- **candidate_expansion** (CANDIDATE): The more extraordinary a claim is relative to established knowledge, the stronger, clearer, and more independently verifiable its evidence should be. Match confidence to evidentiary quality, not to the excitement or desirability of the claim.
- **reasoning_function**: Confirmation bias; accepting exciting claims on weak evidence
- **behavioral_implication**: Increase verification rigor when a claim would overturn substantial knowledge or produce unusually consequential decisions
- **operational_test**: Is the strength and independence of the evidence proportionate to the magnitude of the claim?
- **misuse_risk**: Using "extraordinary" as a rhetorical excuse to dismiss unconventional but well-supported findings
- **accountability_transition**: When evidence accumulates to the extraordinary threshold, refusal to accept becomes the extraordinary position
- **provenance**: partially_verified
- **canonical_status**: candidate

**Compact form:** The larger the claim, the stronger the proof must be.

**Agent governance example:** A claim that "this agent is safe to operate without human oversight" requires substantially more evidence than "this agent can complete a bounded task."

---

### 5. Alder's Razor (Newton's Flaming Laser Sword)

- **id**: alders-razor
- **name**: Alder's Razor
- **class**: razor
- **historical_formulation**: "If something cannot be settled by experiment or observation, it is not worthy of debate" (Mike Alder, paraphrase)
- **common_paraphrase**: Don't debate what can't be tested
- **candidate_expansion** (CANDIDATE): Do not spend unlimited time debating claims that cannot, even in principle, be connected to observation, experiment, evidence, or practical consequence. When no empirical test could distinguish the positions, identify whether the disagreement is instead about values, definitions, or speculation.
- **reasoning_function**: Endless philosophical debate consuming practical attention
- **behavioral_implication**: Ask what evidence would change each participant's mind before allowing debate to consume attention indefinitely
- **operational_test**: What observable difference follows if one position is true rather than the other?
- **misuse_risk**: Treating ethics, mathematics, aesthetics, or conceptual analysis as meaningless merely because laboratory experimentation is unavailable
- **accountability_transition**: When the debate is revealed to be about values rather than facts, switch to value-negotiation, not fact-finding
- **provenance**: partially_verified
- **canonical_status**: candidate

**Compact form:** When no evidence could settle the dispute, stop pretending it is an empirical one.

**Agent governance example:** Debating whether an agent "truly understands" is less productive than testing whether it produces correct outputs on measurable tasks.

---

### 6. Chesterton's Fence

- **id**: chestertons-fence
- **name**: Chesterton's Fence
- **class**: heuristic
- **historical_formulation**: "Do not remove a fence until you know why it was put up" (G.K. Chesterton, 1929, paraphrase)
- **common_paraphrase**: Understand before removing
- **candidate_expansion** (CANDIDATE): Do not remove a rule, institution, constraint, convention, or architectural boundary until you understand why it exists, what problem it addressed, and what currently depends on it. Reform should follow understanding rather than precede it.
- **reasoning_function**: Reckless reform; removing safeguards without understanding their purpose
- **behavioral_implication**: Investigate origin, function, dependency, and failure history before deleting or replacing a structure
- **operational_test**: Can we state the fence's original purpose, current function, dependencies, and replacement plan?
- **misuse_risk**: Using historical purpose as a permanent veto against necessary reform
- **accountability_transition**: When the fence's purpose is understood and no longer relevant, and a replacement is ready, removal is justified
- **provenance**: partially_verified
- **canonical_status**: candidate

**Compact form:** Understand before dismantling. Replace before removing. Verify after changing.

**Agent governance example:** Before removing a guardrail that "seems unnecessary," check git history for the incident that introduced it.

---

### 7. Grice's Razor

- **id**: grices-razor
- **name**: Grice's Razor
- **class**: razor
- **historical_formulation**: Cooperative principle (Paul Grice, 1975; maxims of quality, quantity, relation, manner)
- **common_paraphrase**: Interpret ordinary speech ordinarily
- **candidate_expansion** (CANDIDATE): When interpreting communication, prefer ordinary cooperative explanations before assuming hidden meanings, elaborate codes, or deliberate deception. First consider imprecision, missing context, incomplete expression, and misunderstanding.
- **reasoning_function**: Over-interpretation; finding hidden meanings where ordinary communication suffices
- **behavioral_implication**: Repair ambiguity through questions rather than maximizing adversarial interpretation
- **operational_test**: What would this statement most reasonably mean if the speaker were attempting ordinary cooperative communication?
- **misuse_risk**: Ignoring manipulation, strategic ambiguity, or deception after evidence emerges
- **accountability_transition**: When a pattern of strategic ambiguity is documented, cooperative interpretation becomes the less likely explanation
- **provenance**: partially_verified
- **canonical_status**: candidate

**Compact form:** Interpret ordinary speech ordinarily before searching for hidden intent.

**Agent governance example:** When an agent's output is ambiguous, first ask for clarification rather than assuming it is being evasive.

---

### 8. Ad hoc rescue heuristic

- **id**: ad-hoc-rescue
- **name**: Ad hoc rescue heuristic
- **class**: heuristic
- **historical_formulation**: No single origin; general philosophy of science concept
- **common_paraphrase**: If you keep adding exceptions, the rule is wrong
- **candidate_expansion** (CANDIDATE): When a theory survives only by accumulating exceptions, patches, special cases, and explanations invented after each failure, reconsider the theory itself. A model that explains every result after the fact may predict nothing beforehand.
- **reasoning_function**: Theory-protection; saving a favored model by inventing patches instead of revising it
- **behavioral_implication**: Notice when explanations are being changed to protect a favored belief rather than improve prediction
- **operational_test**: What did the model predict before the outcome was known?
- **misuse_risk**: Rejecting legitimate complexity merely because the system contains real exceptions
- **accountability_transition**: When post-hoc explanations outnumber predictions, the model has failed as a predictive tool
- **provenance**: unresolved
- **canonical_status**: candidate

**Compact form:** When the exceptions become the theory, replace the theory.

**Agent governance example:** If an agent's behavior requires a new excuse after each failure, the agent's design needs revision, not more excuses.

---

### 9. "If it isn't broken, don't fix it"

- **id**: if-it-isnt-broken
- **name**: "If it isn't broken, don't fix it"
- **class**: heuristic
- **historical_formulation**: Popular engineering maxim; origin unclear
- **common_paraphrase**: Don't change what works
- **candidate_expansion** (CANDIDATE): Do not change a functioning system merely because change is possible. Every intervention creates cost, uncertainty, transition risk, and new failure modes. Improve systems when expected benefit exceeds disruption and recovery is understood.
- **reasoning_function**: Unnecessary intervention; changing stable systems without justification
- **behavioral_implication**: Treat stability as an asset and require a defined problem before redesign
- **operational_test**: What measured failure or opportunity justifies intervention, and can the change be reversed?
- **misuse_risk**: Confusing absence of visible failure with health, fairness, or sustainability
- **accountability_transition**: When hidden failure modes are discovered (security, fairness, sustainability), "not broken" no longer applies
- **provenance**: unresolved
- **canonical_status**: candidate

**Compact form:** Do not trade known adequacy for unproven elegance without a reason.

**Agent governance example:** Do not refactor a working test suite to "improve" it unless there is a measured problem the refactor solves.

---

### 10. Goodhart's Law

- **id**: goodharts-law
- **name**: Goodhart's Law
- **class**: law
- **historical_formulation**: "When a measure becomes a target, it ceases to be a good measure" (Charles Goodhart, 1975, paraphrase)
- **common_paraphrase**: Metrics become targets, and targets get gamed
- **candidate_expansion** (CANDIDATE): When a measure becomes a target, people and systems begin optimizing the measure rather than the underlying purpose. Treat metrics as imperfect signals, use multiple forms of evidence, and verify that apparent improvement represents real improvement.
- **reasoning_function**: Metric gaming; optimizing the proxy instead of the goal
- **behavioral_implication**: Design metrics with gaming, tunnel vision, and displaced values in mind
- **operational_test**: What behavior will rational actors adopt to improve this metric without improving the actual objective?
- **misuse_risk**: Abandoning measurement entirely rather than governing it intelligently
- **accountability_transition**: When gaming is detected, the metric must be redesigned or replaced, not defended
- **provenance**: partially_verified
- **canonical_status**: candidate

**Compact form:** Measure the goal, but watch what the measure teaches people to game.

**Agent governance example:** If an agent is evaluated on test pass rate, it may learn to skip failing tests rather than fix them.

---

### 11. Campbell's Law

- **id**: campbells-law
- **name**: Campbell's Law
- **class**: law
- **historical_formulation**: "The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures" (Donald T. Campbell, 1976, paraphrase)
- **common_paraphrase**: High-stakes metrics corrupt
- **candidate_expansion** (CANDIDATE): The more strongly a quantitative indicator is tied to reward, punishment, status, or access, the more pressure exists to corrupt both the indicator and the process it represents. High-stakes metrics require independent verification, anti-gaming controls, and periodic redesign.
- **reasoning_function**: Metric corruption under stakes
- **behavioral_implication**: Audit provenance and incentives when consequential decisions depend on a score
- **operational_test**: What becomes easier to distort once this number controls resources or status?
- **misuse_risk**: Assuming all corruption is deliberate; adaptation may be unconscious or structurally induced
- **accountability_transition**: When corruption is structural, the system must change, not just the metric
- **provenance**: partially_verified
- **canonical_status**: candidate

**Compact form:** The higher the stakes attached to a number, the less innocently that number should be interpreted.

**Agent governance example:** If agent promotion depends on a "trust score," agents will optimize the score, not trustworthiness.

---

### 12. Conway's Law

- **id**: conways-law
- **name**: Conway's Law
- **class**: law
- **historical_formulation**: "Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations" (Melvin Conway, 1967, paraphrase)
- **common_paraphrase**: Architecture mirrors organization
- **candidate_expansion** (CANDIDATE): Systems tend to reproduce the communication structures of the organizations that build them. Fragmented teams often produce fragmented interfaces; unclear authority often becomes architectural ambiguity. Sustainable technical change therefore requires examination of the organization producing the system.
- **reasoning_function**: Ignoring organizational causes of architectural problems
- **behavioral_implication**: Diagnose ownership, communication, incentives, and decision rights alongside code
- **operational_test**: Which organizational boundary is this technical boundary reproducing?
- **misuse_risk**: Treating organizational structure as destiny rather than a strong, governable tendency
- **accountability_transition**: When the organization is restructured, the architecture will resist unless explicitly redesigned
- **provenance**: partially_verified
- **canonical_status**: candidate

**Compact form:** Architecture reveals organization, whether intended or not.

**Agent governance example:** If two agent teams produce incompatible interfaces, check whether the teams communicate — the architecture is telling you about the org.

---

### 13. Parkinson's Law

- **id**: parkinsons-law
- **name**: Parkinson's Law
- **class**: law
- **historical_formulation**: "Work expands so as to fill the time available for its completion" (C. Northcote Parkinson, 1955)
- **common_paraphrase**: Work fills available time
- **candidate_expansion** (CANDIDATE): Work tends to expand to consume the time, attention, and resources made available to it. Define scope, constraints, decision points, and stopping conditions so effort remains proportional to value.
- **reasoning_function**: Scope expansion; work growing to fill available budget
- **behavioral_implication**: Establish "done" before work becomes indefinite polishing or ceremony
- **operational_test**: What is the smallest complete outcome, and what explicit condition ends the work?
- **misuse_risk**: Using unrealistic deadlines to manufacture urgency, hide labor, or degrade quality
- **accountability_transition**: When the stopping condition is met, stop — do not invent new work to fill remaining time
- **provenance**: partially_verified
- **canonical_status**: candidate

**Compact form:** Give work a boundary, or it will invent one at the edge of available life.

**Agent governance example:** An agent given an open-ended research task will consume all available time; define the deliverable and stopping condition first.

---

### 14. Hofstadter's Law

- **id**: hofstadters-law
- **name**: Hofstadter's Law
- **class**: law
- **historical_formulation**: "It always takes longer than you expect, even when you take into account Hofstadter's Law" (Douglas Hofstadter, 1979)
- **common_paraphrase**: Everything takes longer than expected
- **candidate_expansion** (CANDIDATE): Complex work usually takes longer than expected, even after delays have been considered. Plan with uncertainty, include slack, expose hidden dependencies, and avoid treating optimistic estimates as commitments.
- **reasoning_function**: Planning fallacy; underestimating time and complexity
- **behavioral_implication**: Use ranges and historical evidence rather than false precision
- **operational_test**: What unknown work, dependency, or integration cost is absent from the estimate?
- **misuse_risk**: Turning uncertainty into an excuse for weak decomposition or unaccountable delivery
- **accountability_transition**: When actual time consistently exceeds estimates, the estimation process itself must be revised
- **provenance**: partially_verified
- **canonical_status**: candidate

**Compact form:** Assume the unknown work is real, even before it can be named.

**Agent governance example:** When estimating a multi-step agent task, multiply the initial estimate by a uncertainty factor and include explicit checkpoints for re-estimation.

---

### 15. Brooks's Law

- **id**: brooks-law
- **name**: Brooks's Law
- **class**: law
- **historical_formulation**: "Adding human resources to a late software project makes it later" (Fred Brooks, 1975, The Mythical Man-Month)
- **common_paraphrase**: Adding people to a late project makes it later
- **candidate_expansion** (CANDIDATE): Adding people to a late, tightly coupled project can make it later because onboarding, coordination, communication, and integration consume the capacity of those already doing the work. Increase staffing only where work can be decomposed cleanly and newcomers can contribute without destabilizing the critical path.
- **reasoning_function**: Throwing people at coordination-bound problems
- **behavioral_implication**: Diagnose the bottleneck before responding to lateness with headcount
- **operational_test**: Can the delayed work be partitioned into independent units with low onboarding and integration cost?
- **misuse_risk**: Treating the law as universal when tasks are genuinely parallelizable and interfaces are mature
- **accountability_transition**: When work is genuinely parallelizable, adding capacity is correct — the law describes coupling, not a universal prohibition
- **provenance**: partially_verified
- **canonical_status**: candidate

**Compact form:** Before adding hands, determine whether the work can actually be divided.

**Agent governance example:** Adding more agents to a tightly-coupled debugging task may slow it down; adding agents to independent research tasks may help.

## Cross-cutting governed-reasoning sequence

The initial synthesis should be tested as a practical sequence:

1. Clarify the claim or decision.
2. Separate observation, inference, assumption, and preference.
3. Prefer the simplest sufficient explanation.
4. Interpret uncertain human behavior charitably.
5. Match confidence to evidence.
6. Identify what could test, falsify, or revise the conclusion.
7. Understand existing structures before changing them.
8. Examine incentives, metrics, and organizational effects.
9. Bound scope, time, and coordination cost.
10. Act proportionately, observe results, preserve receipts, and revise.

**Candidate synthesis** (CANDIDATE — NON-CANONICAL):

> Assume less. Ask more. Test what can be tested. Understand before changing. Measure without worshipping the measure. Design for incentives, uncertainty, and human limitation. Lead with charity, but let evidence determine accountability.

## Non-goals

- Declaring these formulations canonical HUMMBL or BaseN doctrine
- Treating every listed item as historically classified as a "razor"
- Inventing precise provenance where source history is disputed
- Replacing contextual judgment with a deterministic checklist
- Using charitable interpretation to excuse repeated or intentional harm
- Using simplicity to erase complexity, or skepticism to avoid fair investigation

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#142
- **Entries**: 15
- **Provenance table**: included
- **Decision matrix**: included
- **Glossary**: included
- **Schema applied**: all 15 entries use the common entry schema
- **Candidate labeling**: all expansions marked CANDIDATE
- **Provenance labeling**: all historical formulations marked as paraphrase unless verified
- **Misuse cases**: every entry includes misuse_risk
- **Accountability transitions**: every entry includes accountability_transition
- **Operational tests**: every entry includes operational_test
- **Agent governance examples**: included for every entry
- **Canonical status**: all entries = candidate
- **Review status**: PENDING independent review
