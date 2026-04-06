# AI Governance Readiness Scorecard -- Assessment Template

**Target URL**: hummbl.io/readiness
**Type**: 20-question self-assessment with scored report
**Status**: SPEC DRAFT
**Date**: 2026-04-05

---

## Purpose

A structured self-assessment that produces a governance readiness grade (F through A) across five domains. Designed to:

1. Give prospects an immediate, actionable understanding of their governance posture.
2. Generate per-domain radar chart data for visual reporting.
3. Drive conversion to HUMMBL consulting engagements by surfacing specific gaps.
4. Serve as the intake instrument for formal governance assessments.

---

## Scoring System

**Per question**: 0 / 1 / 2 / 3

| Score | Label | Meaning |
|-------|-------|---------|
| 0 | Not Started | No activity, no plans, or unaware of the requirement |
| 1 | Planned | Acknowledged as a need; on a roadmap but not yet begun |
| 2 | Partial | Some implementation exists but incomplete, inconsistent, or untested |
| 3 | Implemented | Fully deployed, tested, documented, and maintained |

**Total possible**: 60 points (20 questions x 3 max)

**Grade scale**:

| Grade | Range | Label | Summary |
|-------|-------|-------|---------|
| F | 0-12 | Critical | No meaningful governance. Maximum exposure to liability, regulatory action, and uncontrolled agent behavior. Immediate action required. |
| D | 13-24 | Deficient | Some awareness but major gaps across most domains. Vulnerable to any audit, incident, or insurance review. |
| C | 25-36 | Developing | Foundation exists in some areas but controls are inconsistent. Would not survive a regulatory inquiry or serious incident without significant gaps exposed. |
| B | 37-48 | Established | Governance framework is in place with most controls operational. Gaps are known and being addressed. Defensible posture for most compliance contexts. |
| A | 49-60 | Advanced | Comprehensive governance with continuous monitoring, evidence generation, and regulatory alignment. Ready for audit, insurable, and positioned as a market differentiator. |

---

## Domain 1: Policy and Oversight (Questions 1-4)

*Assesses whether the organization has established the human governance layer required before any technical controls matter.*

### Q1. AI Acceptable Use Policy

> Does your organization have a written, approved policy governing how AI tools and agents may be used?

| Score | Criteria |
|-------|----------|
| 0 | No policy exists. AI usage is ad hoc and untracked. |
| 1 | Policy is drafted or in review but not yet approved or communicated. |
| 2 | Policy exists and is communicated, but does not cover agentic AI (autonomous agents, multi-agent systems). |
| 3 | Comprehensive policy covers all AI modalities (copilots, agents, autonomous systems), is approved by leadership, communicated to all staff, and reviewed at least annually. |

### Q2. Named AI Governance Owner

> Is there a named individual (or role) accountable for AI governance decisions?

| Score | Criteria |
|-------|----------|
| 0 | No one owns AI governance. Decisions are made ad hoc by individual teams. |
| 1 | Responsibility is informally assigned (e.g., "the CTO handles it") but not formalized. |
| 2 | A role is formally assigned but the individual lacks authority, budget, or cross-functional scope. |
| 3 | A named owner (e.g., AI Governance Lead, Chief AI Officer, or committee chair) has formal authority, budget allocation, and reports to executive leadership. |

### Q3. AI Inventory and Risk Register

> Do you maintain an inventory of all AI systems and agents in use, with associated risk classifications?

| Score | Criteria |
|-------|----------|
| 0 | No inventory exists. Unknown how many AI tools or agents are deployed. |
| 1 | Informal awareness of major AI tools, but no structured inventory or risk classification. |
| 2 | Inventory exists for some AI systems but is incomplete, not regularly updated, or lacks risk classification. |
| 3 | Complete, regularly updated inventory of all AI systems and agents with risk classifications aligned to a recognized framework (e.g., NIST AI RMF, EU AI Act risk tiers). |

### Q4. Board or Executive AI Reporting

> Does AI governance status get reported to the board, executive team, or equivalent oversight body?

| Score | Criteria |
|-------|----------|
| 0 | No reporting. Leadership is not informed about AI governance posture. |
| 1 | Ad hoc reporting when incidents occur or when leadership asks. |
| 2 | Periodic reporting exists but is informal, inconsistent, or lacks quantitative metrics. |
| 3 | Regular (at least quarterly) structured reporting to board or executive leadership with quantitative governance metrics, risk exposure, and remediation status. |

**Domain 1 max**: 12 points

---

## Domain 2: Agent Identity and Access (Questions 5-8)

*Assesses whether AI agents are treated as managed identities with scoped capabilities, not anonymous tools with ambient authority.*

### Q5. Agent Identity Registration

> Are AI agents (coding assistants, autonomous agents, bots) registered with unique identities in your systems?

| Score | Criteria |
|-------|----------|
| 0 | Agents operate under human accounts or shared credentials. No distinct agent identity. |
| 1 | Some agents have distinct identities, but registration is inconsistent or incomplete. |
| 2 | Most agents are registered with unique identities, but the registry is not centrally managed or enforced. |
| 3 | All agents are registered in a central identity registry with unique identifiers. Agent identity is enforced at the platform level (commits, API calls, bus messages are attributable). |

### Q6. Capability Scoping and Delegation

> Are agent capabilities explicitly scoped? Can agents only perform actions they have been delegated authority for?

| Score | Criteria |
|-------|----------|
| 0 | Agents have the same access as the human who deployed them (ambient authority). |
| 1 | Some access controls exist (e.g., repo-level permissions) but are not agent-specific. |
| 2 | Agent-specific scoping exists for some systems but is not comprehensive. Delegation is not cryptographically enforced. |
| 3 | All agents operate under explicitly scoped delegation tokens or equivalent capability grants. Delegation is signed, time-bounded, and auditable. Chain depth is enforced. |

### Q7. Agent Authentication for External Services

> When agents interact with external services (APIs, databases, cloud resources), how is authentication managed?

| Score | Criteria |
|-------|----------|
| 0 | Agents use hardcoded credentials or shared API keys with full access. |
| 1 | API keys are environment-injected but not agent-specific and not rotated. |
| 2 | Agent-specific credentials exist for some services. Rotation is manual or inconsistent. |
| 3 | All agent-external interactions use agent-specific credentials with least-privilege scoping, automatic rotation, and revocation capability. |

### Q8. Human-in-the-Loop Escalation

> Is there a defined escalation path for when agents encounter decisions beyond their delegated authority?

| Score | Criteria |
|-------|----------|
| 0 | No escalation path. Agents either fail silently or proceed with whatever access they have. |
| 1 | Agents can log errors, but there is no structured escalation to a human decision-maker. |
| 2 | Escalation exists for some agent types but is inconsistent. Response time is not defined. |
| 3 | All agents have a defined escalation policy with human-in-the-loop triggers, response time SLAs, and fallback behavior (safe default) when no human responds. |

**Domain 2 max**: 12 points

---

## Domain 3: Runtime Controls (Questions 9-12)

*Assesses whether the organization can observe, limit, and halt AI agent behavior in real time.*

### Q9. Kill Switch Capability

> Can you immediately halt all AI agent activity (or a specific class of agents) if a threat or failure is detected?

| Score | Criteria |
|-------|----------|
| 0 | No kill switch. The only way to stop an agent is to manually terminate its process or revoke its credentials. |
| 1 | Individual agents can be stopped manually, but there is no centralized halt mechanism. |
| 2 | A centralized mechanism exists but is limited (e.g., only halts all agents, no granularity by class or severity). |
| 3 | Multi-mode kill switch with graduated response (e.g., halt non-critical, halt all, emergency shutdown). Tested regularly. Response time under 60 seconds. |

### Q10. Circuit Breakers on External Integrations

> Do your AI agents have circuit breakers that automatically isolate failing external dependencies?

| Score | Criteria |
|-------|----------|
| 0 | No circuit breakers. A failing API call can cascade into repeated retries, cost overruns, or data corruption. |
| 1 | Basic retry limits exist but no automatic isolation or state tracking (closed/open/half-open). |
| 2 | Circuit breakers exist for some integrations but not all. State transitions are not logged. |
| 3 | All external integrations are wrapped in circuit breakers with defined thresholds, automatic state transitions, logging, and alerting. Half-open recovery is tested. |

### Q11. Output Validation and Guardrails

> Are AI agent outputs (code, decisions, communications) validated before they reach production or end users?

| Score | Criteria |
|-------|----------|
| 0 | Agent outputs go directly to production with no validation layer. |
| 1 | Human review is required for some outputs, but coverage is inconsistent and easily bypassed. |
| 2 | Automated validation exists (linting, security scanning, contract checks) for some output types. Human review for high-risk actions. |
| 3 | Comprehensive validation pipeline: automated checks (security scan, schema validation, policy compliance) plus human review gates for high-risk outputs. Validation is enforced, not optional. |

### Q12. Cost and Rate Governance

> Are there controls preventing AI agents from generating unbounded costs (API calls, compute, token usage)?

| Score | Criteria |
|-------|----------|
| 0 | No cost controls. An agent could run up unlimited API/compute costs. |
| 1 | Budget alerts exist at the cloud/API provider level but are not agent-specific. |
| 2 | Agent-level budgets or rate limits exist for some systems. Alerts fire but do not auto-halt. |
| 3 | Per-agent cost budgets with automatic throttling or halt when thresholds are exceeded. Cost projections feed into governance dashboards. Historical spend is tracked and forecasted. |

**Domain 3 max**: 12 points

---

## Domain 4: Evidence and Audit (Questions 13-16)

*Assesses whether governance activity generates the evidence trail needed for compliance, forensics, and continuous improvement.*

### Q13. Agent Activity Audit Logs

> Do AI agents generate structured, tamper-evident audit logs of their actions?

| Score | Criteria |
|-------|----------|
| 0 | No agent-specific logging. Agent activity is mixed into general application logs (or not logged at all). |
| 1 | Agents produce logs, but they are unstructured, mutable, and not centrally collected. |
| 2 | Structured logs exist for some agents. Logs are centrally collected but not tamper-evident (append-only or signed). |
| 3 | All agents produce structured audit logs that are append-only (or cryptographically chained), centrally collected, retained per policy, and queryable for forensic investigation. |

### Q14. Delegation Token Signing

> Are delegation grants (the authority given to agents) cryptographically signed and verifiable?

| Score | Criteria |
|-------|----------|
| 0 | Delegation is informal (config files, environment variables, or implicit). No signing or verification. |
| 1 | Delegation is documented but not cryptographically signed. Tampering would not be detected. |
| 2 | Some delegation mechanisms use signing (e.g., JWTs for API access) but it is not comprehensive across all agent-authority grants. |
| 3 | All delegation tokens are cryptographically signed (e.g., HMAC-SHA256), include scope, expiry, and issuer. Verification is enforced at runtime. Invalid or expired tokens are rejected. |

### Q15. Provenance Tracking

> Can you trace any AI-generated artifact (code, decision, communication) back to the agent, model, prompt, and authority grant that produced it?

| Score | Criteria |
|-------|----------|
| 0 | No provenance. AI-generated content is indistinguishable from human-generated content in your systems. |
| 1 | Some AI outputs are labeled (e.g., Co-Authored-By tags in commits) but provenance is inconsistent and incomplete. |
| 2 | Most AI outputs are tagged with agent identity and model version. Prompt and authority context are not captured. |
| 3 | Full provenance chain: every AI-generated artifact is linked to agent identity, model version, prompt/instruction context, delegation token, and timestamp. Provenance is queryable and exportable for audit. |

### Q16. Evidence Retention and Export

> Can you produce a governance evidence package on demand (for auditors, regulators, insurers, or incident response)?

| Score | Criteria |
|-------|----------|
| 0 | No structured evidence. Reconstruction after an incident would require manual log mining across multiple systems. |
| 1 | Some governance data is retained, but producing a coherent evidence package would take days of manual work. |
| 2 | Evidence is retained and organized, but export is manual. Some gaps in coverage (e.g., delegation history, cost data). |
| 3 | Evidence packages can be generated on demand, covering: audit logs, delegation history, agent inventory, incident timeline, compliance mapping, and cost data. Format is suitable for regulatory submission. |

**Domain 4 max**: 12 points

---

## Domain 5: Compliance and Insurance (Questions 17-20)

*Assesses alignment with regulatory frameworks and insurance defensibility -- the external validation layer.*

### Q17. NIST AI RMF Mapping

> Have you mapped your AI governance controls to the NIST AI Risk Management Framework (or equivalent recognized framework)?

| Score | Criteria |
|-------|----------|
| 0 | No framework mapping. Governance controls (if any) are ad hoc and not aligned to any standard. |
| 1 | Awareness of NIST AI RMF (or ISO 42001, EU AI Act) but no formal mapping has been performed. |
| 2 | Partial mapping exists. Some controls are aligned to framework categories, but gaps have not been systematically identified. |
| 3 | Complete mapping to NIST AI RMF (or ISO 42001) with gap analysis performed, remediation plan in place, and mapping reviewed at least annually. |

### Q18. ISO 42001 / EU AI Act Readiness

> Are you prepared for ISO 42001 certification or EU AI Act compliance (if applicable to your markets)?

| Score | Criteria |
|-------|----------|
| 0 | No awareness or preparation. Would not know where to start if required. |
| 1 | Aware of requirements. No preparation underway. |
| 2 | Preparation underway: gap analysis started, some controls being implemented, but not yet audit-ready. |
| 3 | Audit-ready for ISO 42001 or EU AI Act (as applicable). Controls documented, evidence generated, management review completed. For EU AI Act: risk classification performed for all AI systems, high-risk systems have conformity documentation. |

**Note**: EU AI Act enforcement begins August 2, 2026. Penalty ceiling: min(EUR 35M, 7% of global annual revenue). Finland began enforcement January 2026.

### Q19. Insurance Coverage Verification

> Have you confirmed that your D&O/E&O insurance policies cover AI-related claims?

| Score | Criteria |
|-------|----------|
| 0 | Have not checked. Assume existing policies cover AI activity. |
| 1 | Aware that AI exclusions exist in the market but have not reviewed own policies. |
| 2 | Reviewed policies with broker. Some coverage exists but gaps or ambiguities remain unresolved. |
| 3 | Policies explicitly reviewed for AI coverage. Either: (a) confirmed coverage with AI-specific endorsement, or (b) identified exclusions and obtained supplemental coverage or accepted residual risk with board-level sign-off. |

**Context**: Berkley and peer carriers are issuing absolute AI exclusions on D&O/E&O policies. Moffatt v. Air Canada (2024) established that deploying companies bear liability for AI agent outputs. Mobley v. Workday (2025) certified vendor-as-agent liability theory.

### Q20. Reasonable Care Evidence

> If an AI-related incident occurred tomorrow, could you demonstrate "reasonable care" in your governance of AI systems?

| Score | Criteria |
|-------|----------|
| 0 | No evidence of reasonable care. Would rely entirely on post-incident reconstruction. |
| 1 | Some governance artifacts exist but are scattered, incomplete, and not designed for legal defensibility. |
| 2 | Core governance evidence exists (policies, some logs, some controls) but has not been reviewed for legal sufficiency. |
| 3 | Comprehensive reasonable-care evidence package: board-approved policy, named governance owner, agent inventory with risk classification, runtime controls with test records, append-only audit logs with delegation provenance, framework mapping, and insurance verification. Reviewed by legal counsel. |

**Context**: Reasonable care is the standard for Caremark liability (director duty of oversight), NIST AI RMF conformance, and insurance coverage disputes. Runtime-generated evidence (audit logs, signed delegation tokens) is stronger than retroactively assembled documentation.

**Domain 5 max**: 12 points

---

## Scoring Summary Template

```
DOMAIN                          SCORE    MAX    %
-----------------------------------------------
1. Policy & Oversight           __/12    12     __%
2. Agent Identity & Access      __/12    12     __%
3. Runtime Controls             __/12    12     __%
4. Evidence & Audit             __/12    12     __%
5. Compliance & Insurance       __/12    12     __%
-----------------------------------------------
TOTAL                           __/60    60     __%

GRADE: [F / D / C / B / A]
```

---

## Radar Chart Data

For web rendering, the five domain scores map to a radar (spider) chart:

```json
{
  "domains": [
    {"name": "Policy & Oversight", "score": 0, "max": 12},
    {"name": "Agent Identity & Access", "score": 0, "max": 12},
    {"name": "Runtime Controls", "score": 0, "max": 12},
    {"name": "Evidence & Audit", "score": 0, "max": 12},
    {"name": "Compliance & Insurance", "score": 0, "max": 12}
  ],
  "total": 0,
  "grade": "F"
}
```

Render as a five-axis radar chart with:
- Outer ring = 12 (full marks per domain)
- Shaded area = current scores
- Color coding: red (0-4), amber (5-8), green (9-12) per domain

---

## Recommended Actions by Grade

### Grade F (0-12): Critical -- Immediate Action Required

**Priority**: Establish minimum viable governance within 30 days.

1. **Week 1**: Draft and approve an AI acceptable use policy (Q1). Name a governance owner (Q2).
2. **Week 2**: Inventory all AI agents and classify by risk (Q3). Implement a kill switch for highest-risk agents (Q9).
3. **Week 3**: Review insurance policies for AI exclusions (Q19). Begin structured logging for agent activity (Q13).
4. **Week 4**: Establish human-in-the-loop escalation for autonomous agents (Q8). Brief leadership on governance posture (Q4).

**Expected outcome**: Move to Grade D within 30 days. Reduces catastrophic risk from "uncontrolled" to "deficient but aware."

---

### Grade D (13-24): Deficient -- Foundation Building

**Priority**: Close the largest gaps in each domain within 90 days.

1. **Month 1**: Complete agent identity registration (Q5). Implement circuit breakers on all external integrations (Q10). Begin NIST AI RMF mapping (Q17).
2. **Month 2**: Implement delegation scoping for all agents (Q6). Deploy output validation pipeline (Q11). Establish evidence retention (Q16).
3. **Month 3**: Begin regular executive reporting (Q4). Implement cost governance (Q12). Review insurance with broker (Q19).

**Expected outcome**: Move to Grade C within 90 days. Defensible posture for basic regulatory inquiries.

---

### Grade C (25-36): Developing -- Closing Gaps

**Priority**: Achieve consistency across all domains within 6 months.

1. **Months 1-2**: Upgrade partial implementations to full coverage. Focus on domains scoring below 50%.
2. **Months 3-4**: Implement delegation token signing (Q14). Build provenance tracking (Q15). Complete framework mapping with gap analysis (Q17).
3. **Months 5-6**: Prepare for ISO 42001 or EU AI Act compliance (Q18). Build on-demand evidence export capability (Q16). Conduct reasonable-care review with legal counsel (Q20).

**Expected outcome**: Move to Grade B within 6 months. Audit-ready for most compliance contexts.

---

### Grade B (37-48): Established -- Optimization

**Priority**: Close remaining gaps and establish continuous improvement within 12 months.

1. **Quarter 1**: Address any domain scoring below 9/12. Implement full provenance chain (Q15). Achieve audit-ready framework mapping (Q17).
2. **Quarter 2**: Obtain ISO 42001 certification or complete EU AI Act conformity assessment (Q18). Upgrade evidence to on-demand export (Q16).
3. **Quarters 3-4**: Conduct tabletop exercises (incident response with governance evidence). Establish governance metrics and trend reporting. Review and refine annually.

**Expected outcome**: Move to Grade A within 12 months. Governance becomes a competitive differentiator.

---

### Grade A (49-60): Advanced -- Maintain and Differentiate

**Priority**: Maintain posture. Use governance as a market advantage.

1. **Ongoing**: Annual policy review. Quarterly executive reporting. Continuous monitoring dashboards.
2. **Differentiation**: Publish governance practices (case studies, blog posts). Use governance posture in sales conversations and RFP responses.
3. **Evolution**: Stay ahead of regulatory changes (EU AI Act enforcement Aug 2, 2026). Adopt emerging standards early. Contribute to industry governance frameworks.

**Risks at this level**: Complacency (controls exist but are not exercised), drift (new agents deployed outside governance framework), and false confidence (high score does not mean zero risk).

---

## Implementation Notes

- **Web rendering**: hummbl.io/readiness -- interactive form with real-time scoring, radar chart, and grade display.
- **PDF export**: Generate a branded PDF report with all scores, the radar chart, grade, and recommended actions for the achieved grade.
- **Shareability**: Results encoded as URL params (same pattern as ROI calculator) for sharing without server storage.
- **CTA flow**: Grade F/D -> "Get an emergency assessment" (Cal.com link). Grade C -> "Accelerate with guided implementation." Grade B/A -> "Validate with a formal audit."
- **Data use**: Aggregate (anonymized) scorecard submissions provide market intelligence on governance maturity distribution. No PII collected.
- **Companion tool**: Link to ROI Calculator (hummbl.io/roi) from the results page to quantify financial exposure based on identified gaps.

---

## Source Alignment

The five domains and 20 questions align with:

| Domain | NIST AI RMF | ISO 42001 | EU AI Act | HUMMBL Governance Primitives |
|--------|-------------|-----------|-----------|------------------------------|
| Policy & Oversight | GOVERN function | Clause 5 (Leadership) | Article 9 (Risk management) | Policy layer |
| Agent Identity & Access | MAP function | Clause 7.1 (Resources) | Article 16 (Provider obligations) | Identity registry, delegation tokens |
| Runtime Controls | MANAGE function | Clause 8 (Operation) | Article 14 (Human oversight) | Kill switches, circuit breakers, cost governor |
| Evidence & Audit | MEASURE function | Clause 9 (Evaluation) | Article 12 (Record-keeping) | Append-only audit logs, governance bus |
| Compliance & Insurance | Cross-cutting | Clause 10 (Improvement) | Article 43 (Conformity) | Framework mapping, evidence packs |

---

*Last updated: 2026-04-05. Review when EU AI Act enforcement begins (Aug 2, 2026) or when NIST AI RMF updates publish.*
