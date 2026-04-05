# AI Exclusions Are Here. What Risk Managers Need to Know Before Renewal.

*Your D&O and E&O policies may already exclude AI-generated code incidents. If your company deploys AI agents without documented governance controls, you are self-insuring without knowing it.*

---

## The Insurance Market Moved Before You Did

In late 2025, **Berkley Insurance Group** introduced **absolute AI exclusions** across its Directors & Officers, Errors & Omissions, and Fiduciary liability policies. The exclusion language covers claims "based upon, arising out of, or attributable to" AI use, AI deployment, AI development, AI-generated content, failure to detect AI content, inadequate AI governance, and chatbot communications (Lexology carrier exclusion analysis, 2025).

**Hamilton Insurance Group** filed materially similar broad exclusions in the same period.

This is not a sub-limit reduction or a premium surcharge. It is an **absolute exclusion** -- the policy does not respond to the claim at all.

The D&O and E&O markets -- where board oversight failures and professional negligence live -- have moved first. These are precisely the policies that respond when an AI agent causes a security breach, a compliance failure, or a financial loss that triggers shareholder litigation.

> AI incidents are becoming **uninsurable before they become unprosecutable**. The insurance market is pricing the risk faster than regulators are writing the rules.

---

## The Exposure Is Quantified

If your organization uses AI coding assistants or deploys AI agents, here is what the data says about your risk profile:

**42% of code in production is now AI-generated** (Sonar 2026 developer survey, n=1,100+ developers across 4 countries). If your engineering team uses Copilot, Cursor, Claude Code, or similar tools, a substantial portion of your shipped code was not written by a human.

**AI-generated code contains 2.74x more vulnerabilities** than human-written code (Veracode 2025 analysis of 100+ LLMs across 4 languages). AppSec Santa's 2026 study tested 534 samples across six frontier models and found **25.1% contained confirmed security vulnerabilities** -- one in four.

**Security pass rates have been stuck at approximately 55% for two years** despite significant model improvements (Veracode Spring 2026). The models are getting better at writing functional code. They are not getting better at writing secure code.

**The incident cost range is $250K to $2M+** for a mid-severity AI-related breach or compliance failure, scaling to the **$4.5M average breach remediation** cost documented by IBM for data breaches generally. For incidents involving regulatory enforcement, the range expands significantly: the EU AI Act prescribes penalties up to **35 million euros or 7% of global revenue**, and Colorado's AI Act (effective June 30, 2026) allows **$20,000 per violation per affected consumer** under the Consumer Protection Act.

**81% of organizations lack visibility** into how AI is actually used in their codebases (Aikido Security 2026 survey, n=450). You cannot govern what you cannot see, and you cannot demonstrate reasonable care over a process you cannot document.

---

## The Legal Ground Is Shifting Under You

Three legal developments are converging to make ungoverned AI deployment a board-level liability risk.

### 1. Deployer Liability Is the Settled Default

**Moffatt v. Air Canada** (2024 BCCRT 149, February 2024) is the foundational case. Air Canada argued its chatbot was a "separate legal entity" with its own responsibility. The BC Civil Resolution Tribunal rejected that argument entirely. **Rule: the deploying company owns what its AI tells the world.** The damages were small ($650.88 CAD), but the rule scales directly. If your AI-assisted code ships a wrong answer, a security vulnerability, or a compliance violation to a customer, you cannot hide behind the tool.

### 2. Vendor Contracts Will Not Save You

AI tool vendors have structured their terms to push liability onto the deployer. Anthropic caps liability at **the greater of $100 or six months of fees** (October 2025 terms). GitHub's Copilot Copyright Commitment -- the most generous vendor indemnity on the market -- excludes modified suggestions, use with filters disabled, and combined-content triggers. Attorney Kate Downing's analysis: the carve-outs "swallow the rule." When something goes wrong, the vendor's contract directs the loss to you.

### 3. Board Oversight Exposure Is Live

No AI-code Caremark case has been decided on the merits yet, but the framework is in place. *Brewer v. Turner* (Del. Ch., September 2025) refused to dismiss a Caremark oversight claim, confirming the standard is live. AI-related securities class actions roughly doubled in 2024 and accelerated in 2025. Directors of companies deploying AI-assisted code without a documented reporting system face foreseeable *Marchand/Caremark* exposure: a "known material risk" with no board-level reporting mechanism.

The SEC settled approximately $7M with four public companies in October 2024 for "negligently minimized" disclosures about a supply-chain breach. This is the template for the first AI-code-breach SEC action.

---

## What Underwriters Are Asking

Carriers are now including AI-specific questions in renewal applications (HUB International, Insurance Business America): What AI tools are deployed? What governance framework is documented? What human-in-the-loop processes exist? What is your NIST AI RMF compliance posture?

A market bifurcation is forming: organizations with documented governance artifacts receive affirmative coverage. Organizations without face absolute exclusions at renewal (Harvard Corporate Governance Forum, September 2025).

**Your AI governance posture is no longer a technology decision. It is an insurability decision.**

---

## What "Reasonable Care" Looks Like to an Underwriter

The legal standard emerging across multiple jurisdictions is "reasonable care" -- the classic Learned Hand calculus applied to AI deployments. The burden of governance is low. The probability of harm is demonstrably high. The loss magnitude is significant. Courts applying this framework will ask what controls you had in place, and your insurer will ask the same question before deciding whether to cover you.

Here is what a defensible governance posture includes:

**1. Signed delegation tokens.** HMAC-SHA256 cryptographic proof of who authorized each AI agent to act, with what scope, for what duration. Non-repudiable authorization records generated at runtime.

**2. Append-only audit log.** Every agent action writes to a tamper-evident log with content hashing. Entries cannot be modified or deleted. This is the Caremark "reporting system" generated automatically, not reconstructed after the incident.

**3. Circuit breakers around external integrations.** Three states (CLOSED, HALF_OPEN, OPEN) preventing cascading failures across agent fleets.

**4. Kill switches with defined escalation modes.** Four modes from normal operations through emergency shutdown. Checked before every agent action. Operable without network connectivity.

These four primitives together produce what matters most in both the courtroom and the underwriting office: **evidence of governance generated at runtime, not reconstructed after the breach.**

> "When counsel asks 'what oversight did you have when this AI wrote that code?' -- you produce a cryptographically-signed, append-only log showing which agent wrote it, under which delegation token, what scope, what budget, what review gate, and which human authorized the delegation chain. That is a Caremark affirmative defense, a reasonable-care exhibit, and a NIST AI RMF conformance record."

---

## The Compliance Landscape Reinforces the Insurance Argument

**NIST AI RMF 1.0** (January 2023) and the **Generative AI Profile (NIST AI 600-1, July 2024)** are voluntary but increasingly function as the de facto duty-of-care standard. Washington's HB 2309 and similar bills in Colorado and Texas create a **rebuttable presumption of legal compliance** for organizations following NIST AI RMF or ISO 42001. Failure to implement removes your safe harbor. This is the same mechanism that made NIST CSF the de facto cybersecurity duty after 2014. The EU AI Act (enforcement phasing through August 2027) adds an international dimension.

---

## Three Actions Before Your Next Renewal

**1. Inventory your AI exposure.** Catalog every AI tool deployed, including shadow AI. Document production access, credentials, and data reach. This is the starting point for both your governance program and your renewal application.

**2. Implement governance primitives now.** Start with an append-only audit log and a kill switch. Add delegation tokens for multi-agent workflows. Available as stdlib-only Python libraries with zero vendor lock-in -- on-premises, air-gap capable, embeddable.

**3. Brief your board.** AI deployment without documented governance is the textbook Caremark exposure pattern: a known material risk without a reporting mechanism. The board needs to know the tools, the controls, the insurance status, and the plan to close the gap before renewal.

---

**Assess your AI governance readiness:** [hummbl.io/readiness](https://hummbl.io/readiness)
**Track the regulatory landscape:** [hummbl.io/tracker](https://hummbl.io/tracker)
**Get the governance primitives:** `pip install hummbl-governance`

---

*Sources: Berkley Insurance Group AI exclusion filings (late 2025, via Lexology); Hamilton Insurance Group exclusion filings (late 2025); HUB International AI risk and insurance analysis (December 2025); Harvard Corporate Governance Forum (September 2025); Sonar 2026 Developer Survey (n=1,100+); Veracode 2025 GenAI Code Security Report (100+ LLMs, 4 languages); Veracode State of Software Security Spring 2026; AppSec Santa 2026 (534 samples, 6 LLMs); Aikido Security 2026 Developer Survey (n=450); Moffatt v. Air Canada, 2024 BCCRT 149; Mobley v. Workday, 3:23-cv-00770 (N.D. Cal.); Brewer v. Turner (Del. Ch., Sept 2025); Anthropic API Commercial Terms of Service (October 2025); Kate Downing Copilot Indemnity Analysis (2023); NIST AI RMF 1.0 (January 2023); NIST AI 600-1 GenAI Profile (July 2024); IBM Cost of a Data Breach Report.*
