# Round 5: Regulated Vertical Compliance Compounding — AI Governance Sales Narratives

**Date:** 2026-04-05
**Lane:** HUMMBL vertical-specific sales narratives for regulated industries
**Question:** How does AI governance compound with existing compliance regimes, and where is the compound pain sharpest?

---

## 1. HEALTHCARE

### Existing Compliance Stack
- **HIPAA Privacy Rule + Security Rule** (45 CFR 164): PHI handling, breach notification, administrative/physical/technical safeguards.
- **FDA SaMD regulation** (21 CFR 820, 21 CFR Part 11): Software as a Medical Device, Quality System Regulation, electronic records.
- **HHS Section 1557** (April 2024 final rule): Nondiscrimination in "patient care decision support tools" — the first federal rule to explicitly regulate AI bias in clinical decision support.
- **ONC Health IT Certification** (HTI-1 Final Rule, Jan 2024): "Decision Support Interventions" (DSI) criterion requires transparency attributes ("source attributes") for predictive DSIs in certified EHRs.
- **State medical boards**: California AB 3030 (AI disclosure in patient communications), Texas HB 2060 (AI utilization review), and ~15 other state bills on AI in medical practice as of 2026.
- **CMS rules**: Medicare Advantage prior authorization AI guidance (2024 CMS final rule), requiring human review for coverage denials.

### How AI Governance Is Being Layered
- **OCR (HHS Office for Civil Rights)** issued 2024 guidance clarifying that AI tools ingesting PHI are Business Associates and require BAAs — including LLM vendors.
- **FDA Predetermined Change Control Plans (PCCPs)**: AI/ML submissions under 510(k) with PCCP allow iterative model updates without resubmission, but require a documented governance plan. ~950 AI/ML-enabled devices authorized by FDA as of early 2026.
- **Section 1557 AI provisions** (effective May 2024, compliance by July 2025): Covered entities must "make reasonable efforts" to identify and mitigate discrimination from AI decision support. This is now ENFORCEABLE.
- **ONC DSI transparency**: Certified EHRs (Epic, Cerner, Athena) must expose source attributes for predictive AI models by Dec 31 2024.

### Compound Compliance Cost & Complexity
Healthcare has the **worst** compound stack: a single AI-assisted clinical workflow can trigger HIPAA (data handling) + FDA (if it makes a clinical recommendation that crosses SaMD threshold) + Section 1557 (bias) + ONC DSI (transparency) + state board rules (disclosure) + CMS coverage rules (utilization management) simultaneously. A mid-size health system typically maintains 3-5 separate compliance programs that don't share evidence artifacts. Estimated incremental cost of layering AI governance: **$400K-$1.2M per year** for a 500-bed hospital (CIO surveys: KLAS 2025, Chartis).

### What HUMMBL Offers That Generic AI Governance Can't
A **unified evidence graph** that maps a single AI control (e.g., "output logging with PHI redaction") to HIPAA §164.312(b), FDA 820.70, Section 1557 §92.210, and ONC DSI source attribute #4 simultaneously. Generic AI governance (OneTrust, Credo, Fairly) maps to NIST AI RMF only; it does NOT crosswalk to healthcare-specific regs.

### Strongest Sales Talk Track
**"You already have a HIPAA program, an FDA quality system, and an ONC-certified EHR. Your AI tools now trigger all three plus Section 1557. We give you one control library that satisfies all four regimes with shared evidence — so your next OCR audit, FDA inspection, and ONC surveillance pull from the same attestation source."**

---

## 2. FINANCIAL SERVICES

### Existing Compliance Stack
- **Federal Reserve SR 11-7 / OCC 2011-12**: Model Risk Management (MRM) — the gold standard for model governance at US banks since 2011.
- **OCC Semiannual Risk Perspective 2023-2024**: Explicitly identifies GenAI as elevated operational risk; calls for expansion of SR 11-7 frameworks to cover LLMs.
- **FINRA Regulatory Notice 24-09** (June 2024): Supervisory obligations apply to AI tools used in broker-dealer operations, including communications supervision and record retention (Rule 3110, Rule 4511).
- **NYDFS Part 500** (cybersecurity, amended Nov 2023): Requires CISO oversight of third-party tools including AI; NYDFS October 2024 AI cybersecurity guidance.
- **CFPB Circular 2023-03**: Adverse action notices must contain specific reasons — "black box AI" does not satisfy ECOA/FCRA.
- **SEC Proposed Rule (July 2023, still pending 2026)**: Predictive data analytics conflicts of interest for investment advisers and broker-dealers.
- **Basel Committee** (BCBS 239 + 2024 AI operational risk guidance): AI counted toward operational risk capital.
- **BSA/AML**: FinCEN 2024 statement on AI in suspicious activity monitoring.

### How AI Governance Is Being Layered
- OCC/Fed/FDIC **joint statement (June 2023)** clarified SR 11-7 applies to GenAI. Banks must maintain inventory, independent validation, and ongoing monitoring of LLMs used in lending, fraud, or customer-facing decisions.
- **NYDFS AI guidance** (Oct 2024): specific cybersecurity controls for AI (prompt injection, training data poisoning, model theft).
- **CFPB** has initiated enforcement against lenders using "algorithmic redlining" (2024 actions against Citibank, Townstone-adjacent cases).

### Compound Compliance Cost & Complexity
SR 11-7 model inventory alone costs a G-SIB ~$50-100M/year. Layering AI adds 30-50% because LLMs don't fit classical model validation (no closed-form testable hypothesis). A regional bank typically has 200-800 "models" in inventory; LLM proliferation via Copilot, ChatGPT Enterprise, and embedded vendor AI is adding 100+ per year. Compound pain: **SR 11-7 + NYDFS 500 + FINRA 3110 + CFPB adverse action + state privacy** for one consumer lending AI workflow.

### HUMMBL Differentiation
Generic AI governance tools track AI models; they don't **inherit the SR 11-7 lifecycle stages** (development, implementation, use, validation, governance) that bank examiners demand. HUMMBL's contract-driven governance maps each AI output to a model risk tier and generates validation evidence in SR 11-7 format.

### Strongest Sales Talk Track
**"Your examiners already trust SR 11-7 evidence. We extend SR 11-7 to every LLM your developers use — automatically — so your next MRIA doesn't flag your AI code assistant as an unmanaged model."**

---

## 3. DEFENSE / FEDERAL

### Existing Compliance Stack
- **FedRAMP** (Moderate/High): Cloud authorization baseline, ~325 controls from NIST 800-53 Rev 5.
- **CMMC 2.0** (final rule Oct 2024, effective Dec 16 2024, rollout through 2028): Level 1 (self-attest), Level 2 (C3PAO assessment, 110 controls from NIST 800-171), Level 3 (DIBCAC, 800-172 subset). Required for all DoD contracts handling CUI.
- **DoD Responsible AI Strategy** (June 2022): 5 principles, implementation via CDAO (Chief Digital and AI Office).
- **DISA SRG IL2/IL4/IL5/IL6**: Impact levels for DoD cloud workloads.
- **NIST 800-53** (federal) and **NIST 800-171** (contractor CUI).
- **OMB M-24-10** (March 2024): Federal AI governance — Chief AI Officers, use case inventory, impact assessments. Successor memos **M-25-21/M-25-22** (2025) tightened acquisition requirements.

### How AI Governance Is Being Layered
- **FedRAMP AI-specific guidance**: FedRAMP PMO issued 2024 memo on AI-generated code in ATO'd systems — requires attribution, provenance, and scan evidence.
- **CMMC + AI**: DIBCAC assessors now ask about AI code assistants in the development pipeline; unmanaged Copilot usage has caused Level 2 findings.
- **DoD Directive 3000.09** (updated 2023): Autonomy in weapon systems, human judgment requirements.
- **OMB M-25-21**: Federal agencies must inventory, risk-assess, and publicly disclose rights-impacting and safety-impacting AI by specified deadlines; acquisition language now requires AI governance in vendor contracts.

### Compound Compliance Cost & Complexity
Defense contractors face the **deepest evidence burden**: CMMC assessment costs $30K-$250K per contractor; adding AI governance evidence requires demonstrating provenance of training data, model supply chain (SBOM for models), and human-in-the-loop attestation. IL5 AI workloads have near-zero commercial tooling that meets the bar. Primes are pushing governance requirements down to subs — a tier-3 supplier using Copilot on CUI code can kill a prime's Level 2.

### HUMMBL Differentiation
Commercial AI governance is **not air-gap friendly** and lacks CUI/IL-aware controls. HUMMBL's stdlib-only, contract-driven, locally-runnable architecture is the only option that fits IL4/IL5 deployment. The contract-first model maps directly to 800-53 / 800-171 control traceability.

### Strongest Sales Talk Track
**"Your prime is about to require AI governance attestation in your next CMMC Level 2 assessment, and no cloud-based AI governance SaaS can touch your IL5 environment. HUMMBL runs on-prem, stdlib-only, with control evidence that drops directly into your CMMC System Security Plan."**

---

## 4. LEGAL / ACCOUNTING

### Existing Compliance Stack
- **ABA Model Rule 1.1 (Competence)** + **1.6 (Confidentiality)**: Formal Opinion 512 (July 2024) is the ABA's first comprehensive AI ethics opinion.
- **State bar AI opinions**: California (Nov 2023), Florida (Jan 2024), New York (April 2024), DC, Pennsylvania, Texas — as of 2026, ~35 states have issued opinions.
- **AICPA SSAE 18 / SOC 2 Type II**: Trust Services Criteria — AI systems now in scope for CC7 (system operations) and CC8 (change management).
- **AICPA AI audit guidance** (2024): "Use of AI by Auditors" and emerging standards from AICPA's Assurance Services Executive Committee.
- **PCAOB**: 2024 staff guidance on AI in audit engagements.

### How AI Governance Is Being Layered
- ABA Opinion 512 requires lawyers to verify AI output competence, protect client confidentiality (no feeding privileged docs to public LLMs without consent), supervise AI as non-lawyer assistance, and bill honestly.
- **Mata v. Avianca** (2023) and ~50+ subsequent sanctions cases for hallucinated citations — courts now issue standing orders requiring AI disclosure.
- SOC 2 auditors increasingly add "AI governance" as a supplementary criterion; AICPA has signaled a formal AI trust service criterion in 2026-2027.

### Compound Compliance Cost
Moderate. Law firms/accounting firms carry multiple state bar regimes + SOC 2 + client-specific requirements, but the compounding is less severe than healthcare/finance because ethics opinions are principles-based.

### HUMMBL Differentiation
Evidence of AI supervision, confidentiality controls, and output verification — as **discoverable artifacts** a firm can produce in a malpractice defense or bar complaint.

### Strongest Sales Talk Track
**"When your opposing counsel's motion accuses your associate of AI-fabricated citations, you need a contemporaneous evidence trail of supervision and verification. HUMMBL produces that trail automatically, per ABA Opinion 512."**

---

## 5. INSURANCE

### Existing Compliance Stack
- **NAIC Model Bulletin on AI (Dec 2023)**: Adopted in 24+ states as of early 2026 — requires written AI governance program, documentation, third-party vendor oversight.
- **Colorado Regulation 10-1-1 (2023)** and **Section 10-3-1104.9**: First state to require algorithmic discrimination testing for life insurance underwriting.
- **NY Circular Letter 7 (2024)**: AI and external consumer data in underwriting.
- **California SB 21 / CDI bulletins**: AI in claims and underwriting.
- **Actuarial Standards of Practice (ASOPs)**: ASOP 56 (modeling) + emerging AI-specific ASOP.

### How AI Governance Is Being Layered
NAIC bulletin establishes a baseline; state commissioners are customizing. Colorado requires quantitative bias testing — the most prescriptive US insurance rule. NAIC is expected to move from "Model Bulletin" to "Model Law" in 2026-2027, which would make adoption mandatory.

### Compound Cost
State-by-state fragmentation is the main burden. A national P&C carrier tracks 30+ state AI requirements plus NAIC plus actuarial standards.

### HUMMBL Differentiation
State-level crosswalk engine that maps one AI governance artifact to 30+ state bulletins.

### Strongest Sales Talk Track
**"NAIC's bulletin is adopted in 24 states with different customizations. One control library, 24 attestation formats — we handle the crosswalk."**

---

## Cross-Vertical Synthesis

| Vertical | Compound Severity | Buying Urgency | Budget Availability | HUMMBL Fit |
|----------|-------------------|----------------|---------------------|------------|
| Healthcare | EXTREME (5+ regimes) | HIGH (1557 enforceable) | Medium | STRONG |
| Financial Services | EXTREME (SR 11-7 + 6 others) | HIGH (OCC focus) | High | STRONG |
| Defense/Federal | HIGH (CMMC deadline) | EXTREME (contract-blocking) | High | UNIQUE FIT |
| Legal/Accounting | MEDIUM | MEDIUM | Medium | MODERATE |
| Insurance | MEDIUM-HIGH (state frag) | MEDIUM | Medium | MODERATE |

---
