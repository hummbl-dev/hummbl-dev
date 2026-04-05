# Mapping AI Agent Governance to SOC 2, NIST AI RMF, and ISO 42001: A Practical Guide

*Your existing control framework was not designed for autonomous software agents. Here is how to extend it -- with runtime primitives that generate compliance evidence automatically.*

---

## The Control Gap You Already Have

If you manage a SOC 2 Type II program, a NIST Cybersecurity Framework implementation, or an ISO 27001-certified ISMS, you have controls for access management, change management, logging, and incident response. What you almost certainly do not have are controls for AI agents that write code, execute shell commands, connect to internal APIs, and make decisions without human review.

This is not a theoretical gap. **42% of all code is now AI-generated or AI-assisted** (Sonar 2026 survey). AI coding agents run with developer-level privileges. They read environment files, execute commands, and connect to services through tool integrations that most security teams have never examined. Your SOC 2 controls govern human access to production systems. They do not govern what an AI agent is permitted to do inside a developer's IDE at 2 AM.

The regulatory landscape is closing this gap from multiple directions simultaneously -- and the enforcement timelines are specific.

## Enforcement Timelines That Matter

**EU AI Act -- August 2, 2026.** High-risk AI system obligations become fully applicable. Non-compliance penalties: **up to 35 million euros or 7% of global annual turnover** for the most serious violations. Finland activated national supervision laws on January 1, 2026, becoming the first EU member state with fully operational enforcement powers. Ireland published its AI Office bill on February 4, 2026. Spain's AESIA has published 16 compliance guides. The enforcement apparatus is operational.

**Colorado AI Act -- June 30, 2026.** Covers "high-risk AI systems" making consequential decisions in employment, education, housing, financial services, healthcare, legal services, and government. Requires a risk management program, impact assessments, and consumer notice. Penalties: **up to $20,000 per violation** under the Colorado Consumer Protection Act.

**NYC Local Law 144 -- Live since July 2023.** Requires independent annual bias audits of automated employment decision tools. Penalties: $500-$1,500 per day, per violation. A December 2025 New York State Comptroller audit found enforcement gaps, but DLA Piper predicts a stricter enforcement phase following.

**Insurance as de facto enforcement.** Berkley Insurance Group introduced **absolute AI exclusions** for D&O, E&O, and fiduciary policies in late 2025: no coverage for claims "based upon, arising out of, or attributable to" AI use, deployment, AI-generated content, or inadequate AI governance. Hamilton Insurance Group filed similar exclusions. The market is bifurcating: firms with documented AI governance artifacts get affirmative coverage; firms without face absolute exclusions at renewal.

## Framework Mapping: Where Your Controls Fall Short

### SOC 2 Trust Service Criteria

SOC 2 covers Security, Availability, Processing Integrity, Confidentiality, and Privacy. AI agent behavior creates gaps in at least three categories:

| TSC | Current Control | AI Agent Gap |
|-----|----------------|--------------|
| **CC6.1** (Logical access) | User access provisioned and reviewed | AI agents inherit developer credentials with no separate identity, no session scope, no privilege boundary |
| **CC6.3** (Access removal) | Terminated users deprovisioned | AI agent sessions persist indefinitely; no revocation mechanism for agent-level access |
| **CC8.1** (Change management) | Changes tested, approved, deployed via pipeline | AI agents generate and commit code outside formal change management; no provenance trail linking output to prompt |
| **PI1.1** (Processing integrity) | Inputs validated, outputs verified | AI agent outputs are not validated against business rules before execution |
| **CC7.2** (Monitoring) | Security events logged and monitored | AI agent actions (tool calls, file modifications, API requests) are not captured in SIEM |

To close these gaps, you need runtime governance primitives -- not policy documents.

### NIST AI Risk Management Framework (AI RMF 1.0)

NIST AI RMF organizes AI governance into four functions: **GOVERN, MAP, MEASURE, MANAGE.** The Generative AI Profile (NIST AI 600-1, released July 2024) adds 200+ suggested actions across twelve GenAI-specific risk areas.

Key mappings to runtime controls:

- **GOVERN 1.1** (Policies for AI lifecycle): Requires documented policies governing AI development. Runtime implementation: a contract schema that defines what each agent is permitted to do, enforced at execution time rather than documented in a binder.
- **MAP 1.5** (AI system inventory): Requires an organizational inventory of deployed AI systems. Runtime implementation: an agent registry with identity, scope, and trust level for every active agent.
- **MEASURE 2.6** (Testing and evaluation): Requires ongoing monitoring of AI system performance. Runtime implementation: append-only audit logs capturing every agent action, decision, and output for continuous evaluation.
- **MANAGE 2.2** (Risk response): Requires mechanisms to respond to identified risks. Runtime implementation: kill switches with graduated escalation (halt non-critical, halt all, emergency stop) and circuit breakers wrapping external service calls.

The NIST framework is voluntary in the US, but it is the baseline that cyber insurers, procurement officers, and federal agencies cite. Under Trump EO 14179, NIST AI RMF has not been rescinded and remains the most likely basis for any federal AI standard.

### ISO/IEC 42001:2023

ISO 42001 is the first international standard for AI management systems. It uses the Plan-Do-Check-Act structure familiar to any ISO 27001 implementer and maps directly to the EU AI Act's requirements around risk management (Article 9), data governance (Article 10), and quality management (Article 17).

Critical ISO 42001 clauses for AI agent governance:

- **Clause 6.1.2** (AI risk assessment): Requires risk assessment specific to AI systems. Runtime evidence: signed delegation tokens that record which agent requested what action, with what authority, creating an auditable chain of delegation.
- **Clause 8.4** (AI system operation): Requires documented procedures for AI system operation. Runtime evidence: append-only governance logs capturing every agent interaction as a conformance record.
- **Clause 9.1** (Monitoring and measurement): Requires measurement of AI management system performance. Runtime evidence: health probes and circuit breaker state as continuous monitoring artifacts.

Organizations that implement ISO 42001 have a documented compliance path that is defensible in EU AI Act regulatory investigations. The crosswalk between ISO 42001 and NIST AI RMF is well-established, meaning a single control implementation can satisfy both.

## Runtime Governance Primitives That Generate Evidence

The pattern that closes the control gaps above requires three primitives:

### 1. Signed delegation tokens

Every AI agent action should carry a cryptographically signed token recording: the requesting identity, the authorized scope, the chain of delegation (if one agent invoked another), and the timestamp. This is simultaneously a SOC 2 CC6.1 access control artifact, a NIST AI RMF GOVERN 1.1 policy enforcement record, an ISO 42001 Clause 6.1.2 risk assessment evidence item, and a Caremark affirmative defense document showing board-level oversight of AI risk.

### 2. Append-only audit logs

Every agent action, tool call, and decision must be recorded in an immutable, append-only log. This log serves as SOC 2 CC7.2 monitoring evidence, NIST MEASURE 2.6 evaluation data, ISO 42001 Clause 9.1 measurement records, and EU AI Act Article 12 automatic logging compliance.

### 3. Runtime enforcement (kill switches and circuit breakers)

Graduated kill switches (disengage, halt non-critical, halt all, emergency stop) and circuit breakers wrapping external service calls provide NIST MANAGE 2.2 risk response mechanisms, SOC 2 CC6.6 system boundary enforcement, and EU AI Act Article 14 human oversight compliance.

When these primitives are native to the platform, compliance evidence is generated at runtime -- not reconstructed after a breach or assembled before an audit.

## The Liability Dimension

The legal landscape reinforces the framework mapping urgency. In **Moffatt v. Air Canada** (2024), the BC Civil Resolution Tribunal held that companies are legally responsible for their AI's output -- rejecting the argument that the chatbot was a "separate legal entity." In **Mobley v. Workday** (N.D. Cal., certified July 2025), the court held that AI vendors can be directly liable as "agents" of employers under anti-discrimination law.

For GRC managers, the practical implication: your existing vendor risk management program must extend to AI tool vendors, and your evidence of oversight must be continuous, not periodic. Signed delegation tokens and append-only audit logs constitute "reasonable care" evidence that is defensible in both regulatory and litigation contexts.

## What to Do This Quarter

1. **Inventory your AI agents.** Which tools have developer-level access? Which teams are using them? Map each to your SOC 2 CC6.1 access control inventory.
2. **Extend your control matrix.** Add AI agent-specific controls to your SOC 2, NIST CSF, or ISO 27001 control framework using the gap analysis above.
3. **Evaluate runtime governance tooling.** Look for platforms that generate compliance evidence automatically -- signed tokens, immutable logs, graduated enforcement -- rather than requiring manual attestation.
4. **Brief your auditor.** If your next SOC 2 Type II examination does not address AI agent access, raise it proactively. Auditors are beginning to ask; being ahead of the question is better than being behind it.
5. **Review your insurance.** Check whether your D&O and E&O policies contain AI exclusions. If they do, documented AI governance artifacts are your path to affirmative coverage.

---

**Assess your AI governance readiness:** [hummbl.io/readiness](https://hummbl.io/readiness)
**Track AI regulatory enforcement as it develops:** [hummbl.io/tracker](https://hummbl.io/tracker)
**Evidence pack (all cited sources, structured):** [github.com/hummbl-dev](https://github.com/hummbl-dev)

---

*Sources: EU AI Act (ec.europa.eu); NIST AI RMF 1.0 and AI 600-1 GenAI Profile; ISO/IEC 42001:2023; Colorado SB 24-205; NYC Local Law 144; Sonar Developer Survey 2026; Moffatt v. Air Canada, 2024 BCCRT 149; Mobley v. Workday, 3:23-cv-00770 (N.D. Cal.); Berkley Insurance Group AI exclusion filings (2025); OMB M-25-21/M-25-22; Trump EO 14179; Finland AI Act supervision (Jan 2026).*
