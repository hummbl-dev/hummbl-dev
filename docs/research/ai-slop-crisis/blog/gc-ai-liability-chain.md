# Moffatt, Mobley, and the AI Liability Chain Your Legal Team Needs to Map Now

*The liability chain for AI-generated output is settling in court. Your company is the deployer. Here is what "reasonable care" looks like before the breach, not after.*

---

## The chain is settling. You are the default defendant.

When AI-generated code, content, or decisions cause harm, plaintiffs now have a clear target: **the deploying company**. Not the model provider. Not the tool vendor. You.

This is not speculation. Two cases decided in 2024-2025 have drawn the lines, and a third development -- insurance exclusions -- is making governance a financial prerequisite, not just a legal one.

The question is no longer whether your company bears the risk. It is whether you have documented the care you took before the incident.

---

## Case 1: Moffatt v. Air Canada -- you own what your AI tells the world

In February 2024, the British Columbia Civil Resolution Tribunal held Air Canada liable for negligent misrepresentation by its customer-facing chatbot (*Moffatt v. Air Canada*, 2024 BCCRT 149). The chatbot gave a passenger incorrect information about bereavement fare refund deadlines. Air Canada argued the chatbot was a "separate legal entity" and that customers should have verified its answers against the airline's website.

The tribunal rejected that argument entirely. **The deploying company owns every representation its AI makes to the public.**

Damages were small -- **$650.88 CAD** -- but the rule scales directly. If your AI-assisted code ships a wrong answer to a customer, generates a misleading disclosure, or produces output that injures a third party, you cannot hide behind the tool. Moffatt is now cited in at least three US district court filings involving AI-generated content liability.

---

## Case 2: Mobley v. Workday -- vendor liability through the agency crack

If Moffatt established that deployers bear the loss, *Mobley v. Workday* (N.D. Cal., 3:23-cv-00770) is opening the door to vendor liability.

In July 2024, Judge Rita Lin held that Workday could be **directly liable as an "agent" of employers** under Title VII, the ADA, and the ADEA for discrimination by its AI hiring screener. The court's key holding: *"There is no meaningful distinction between software decision-makers and human decision-makers for purposes of determining coverage as an agent."* The EEOC filed an amicus brief supporting this theory.

In **July 2025**, the case was certified as a collective action.

If an AI vendor can be a statutory "agent" for Title VII purposes, the same logic extends to any domain where the deployer has a non-delegable duty: securities disclosure, consumer protection, professional practice. Your AI tool vendor may become a co-defendant. But critically, **you remain the primary defendant**.

---

## The insurance forcing function: Berkley's absolute AI exclusions

While courts set precedent on a case-by-case timeline, insurers have moved faster.

**Berkley Insurance Group introduced absolute AI exclusions for D&O, E&O, and Fiduciary policies in late 2025.** The exclusion language covers claims "based upon, arising out of, or attributable to" AI use, deployment, development, AI-generated content, failure to detect AI content, inadequate AI governance, and chatbot communications. Hamilton Insurance Group filed similar broad exclusions. Hiscox and Beazley are reported to be following.

The practical consequence: **companies without documented AI governance artifacts face no underwritten coverage for AI-related claims.** This is de facto enforcement arriving years before any state attorney general brings a prosecution. A market bifurcation is forming -- firms with documented governance get affirmative coverage; firms without face absolute exclusions at renewal.

For general counsel, this changes the buyer. AI governance is no longer a CISO budget item. It is a CFO and GC imperative, because the coverage gap shows up in the D&O renewal, not in a security dashboard.

---

## The EU AI Act: August 2, 2026

The EU AI Act's high-risk obligations become fully applicable on **August 2, 2026**. Maximum penalties: **up to 35 million euros or 7% of global annual turnover**, whichever is greater. Finland activated national enforcement in January 2026. Ireland published its AI Office bill in February 2026. Spain's AESIA has published 16 compliance guides.

Compliance requires documented risk management systems, automatic logging, human oversight mechanisms, and conformity assessments **before** placing a system on the market. Over half of organizations still lack systematic inventories of AI systems in production.

---

## The Caremark affirmative defense: what boards need to produce

No AI-code Caremark case has been decided on the merits. But the framework is live. *Brewer v. Turner* (Del. Ch., Sept. 29, 2025) refused to dismiss a Caremark oversight claim, confirming the standard applies where directors face a "known material risk" with no board-level reporting system.

AI-related securities class actions roughly doubled in 2024 and accelerated in 2025. Directors of public companies deploying AI-assisted code without documented reporting systems face foreseeable *Marchand/Caremark* exposure.

The defense requires evidence of two things: (1) a reporting system existed, and (2) the board actually monitored it. For AI governance, that means immutable audit trails, delegation records, scope boundaries, and review gates -- produced at runtime, not reconstructed during discovery.

> "When counsel for the plaintiff asks 'what oversight did you have when this AI wrote that code?' -- the answer should be a cryptographically-signed, append-only log showing which agent wrote it, under which delegation token, what scope, what budget, what review gate, and which human authorized the delegation chain. That is a Caremark affirmative defense, a 'reasonable care' exhibit, and a NIST AI RMF conformance record -- generated automatically at runtime, not reconstructed after the breach."

---

## The duty-of-care standard is already forming

The mechanism is the Learned Hand test: burden of governance (low -- audit logs, review gates, signed provenance) versus probability of loss (high -- **25.1% of AI-generated code samples contain confirmed vulnerabilities** per AppSec Santa 2026) multiplied by magnitude of loss (catastrophic -- average breach remediation **$4.5M**).

Washington state's HB 2309, with similar bills in Colorado and Texas, creates a **rebuttable presumption of legal compliance** for organizations following NIST AI RMF or ISO 42001. Failure to implement removes your safe harbor and your good-faith defense for punitive damages. This is the same mechanism that made NIST CSF the de facto cybersecurity duty after 2014.

---

## What "reasonable care" looks like -- concretely

Discovery in AI-code litigation will demand: prompts, outputs, model versions, review artifacts, policy configurations, approval chains. Most deployers cannot produce these today. Governance architectures that generate evidence by construction -- signed delegation tokens, append-only audit logs, contract-driven cost governance, NIST AI RMF mapping -- are the organizations that will survive discovery.

---

## Three things your legal team should do this quarter

1. **Map your liability chain.** Identify every AI tool in use, the vendor contract terms (look for customer-indemnifies-vendor clauses and liability caps -- Anthropic's is $100 or 6 months of fees), and the gap between vendor indemnity and your actual exposure.

2. **Check your D&O/E&O renewal language.** Ask your broker whether absolute AI exclusions are present or pending. If they are, the remediation path is documented governance artifacts, not a coverage negotiation.

3. **Build the evidence trail now.** The time to produce "reasonable care" artifacts is before the breach, not during discovery. Audit logs, delegation records, model inventories, and policy documentation should be generating automatically -- not manually assembled after an incident.

---

*HUMMBL builds the governance primitives -- signed delegation tokens, append-only audit logs, contract-driven cost governance -- that produce these artifacts at runtime. No SaaS dependency. Stdlib-only. Air-gap capable.*

**Assess your readiness:** [hummbl.io/readiness](https://hummbl.io/readiness)
**Track the regulatory timeline:** [hummbl.io/tracker](https://hummbl.io/tracker)
