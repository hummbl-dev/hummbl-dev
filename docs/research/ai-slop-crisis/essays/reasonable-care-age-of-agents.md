# Reasonable Care in the Age of AI Agents: What Courts Will Look For

*When an AI agent causes harm, the legal question is not "did the model hallucinate?" It is "did the deployer exercise reasonable care?" The answer depends on evidence generated before the incident -- not reconstructed after.*

---

## The Legal Framework: What "Reasonable Care" Has Always Meant

For nearly a century, American tort law has used a deceptively simple formula to decide whether someone acted negligently. Judge Learned Hand articulated it in *United States v. Carroll Towing Co.* (1947): a party is negligent when the burden of precaution (B) is less than the probability of harm (P) multiplied by the magnitude of the loss (L). If it would have cost you less to prevent the harm than the expected harm itself, you should have prevented it.

This formula has survived because it scales. It applied to tugboats in 1947. It applied to cybersecurity after the Target breach in 2013. And it applies to AI agents in 2026.

The companion doctrine -- the duty of oversight -- received its modern corporate formulation in *In re Caremark International Inc. Derivative Litigation* (Del. Ch. 1996). Chancellor Allen held that directors face personal liability if they "utterly fail to implement any reporting information system or controls" for known material risks. The standard was sharpened in *Marchand v. Barnhill* (Del. 2019): the board must have a reporting system, and it must actually function.

Together, the Learned Hand test and the Caremark standard ask two questions:

1. **Was it cheaper to govern than to absorb the loss?** (Learned Hand)
2. **Did the board implement a reporting system for the known risk?** (Caremark)

Applied to AI-assisted code generation in April 2026, both questions have clear answers. The burden of governance -- audit logs, delegation tokens, review gates, cost caps -- is measurable in engineering hours and infrastructure cost. The probability of harm is empirically documented: 25.1% of AI-generated code samples contained confirmed vulnerabilities in the AppSec Santa 2026 study (534 samples across 6 LLMs), Veracode's 2025 report found AI code is 2.74x more vulnerable than human-written code, and Apiiro's Fortune 50 analysis (Dec 2024 -- June 2025) showed AI-generated commits producing 322% more privilege-escalation paths and exposing Azure credentials nearly twice as often as human-authored code.[^1] The magnitude of loss is catastrophic: average breach remediation runs $4.5 million, and that figure excludes regulatory penalties, litigation costs, and reputational damage.

B is low. P times L is high. The math is not close.

## The AI Agent Twist: Why Traditional Oversight Breaks

Classical negligence assumed a human actor whose decisions could be supervised, logged, and explained. AI agents break every one of those assumptions.

**Autonomy.** An AI coding agent does not wait for approval before writing its next line. Modern agentic IDEs -- Cursor, Windsurf, Claude Code, Amazon Q -- generate, execute, and iterate on code with minimal human checkpoints. Google's Antigravity shipped a "Turbo/YOLO mode" that removes confirmation gates from destructive operations entirely.[^2] When the agent acts autonomously, the question of who supervised it becomes legally material.

**Scope creep.** Agents routinely exceed their intended scope. The Amazon Q Developer wiper injection (CVE-2025-8217) demonstrated this at scale: a prompt-injection payload in a pull request instructed Q to delete local files, S3 buckets, EC2 instances, and IAM users. The payload shipped in the official marketplace release.[^3] The agent's scope was "help developers write code." Its actual behavior was "execute arbitrary destructive commands."

**Hallucination as structural risk.** AI models do not merely make errors -- they generate confident, plausible-but-false outputs that resist detection. The slopsquatting research (Lasso Security, 2024-2025) found that 20% of LLM-generated code samples referenced non-existent packages, and 43% of those hallucinated package names were consistent across repeated queries -- making them predictable and squattable by attackers.[^4] This is not a bug that will be patched. It is a structural property of probabilistic text generation.

**The supervision gap.** The METR randomized controlled trial (arxiv 2507.09089, N=16 experienced developers, 246 tasks) found that developers using AI tools believed they were 20% faster but were actually 19% slower.[^5] If the humans supervising AI output cannot accurately assess their own performance with it, the quality of that supervision is legally suspect.

These four properties -- autonomy, scope creep, hallucination, and the supervision gap -- mean that the traditional negligence defense ("we had a reasonable process") requires new kinds of evidence.

## What Courts Have Already Decided

### Moffatt v. Air Canada (2024 BCCRT 149)

The foundational precedent. Air Canada's chatbot told Jake Moffatt he could book a bereavement fare and apply for a refund within 90 days. The real policy required pre-travel approval. Air Canada argued the chatbot was a "separate legal entity" responsible for its own actions. The BC Civil Resolution Tribunal rejected that argument entirely and held Air Canada liable for $812 CAD in damages.[^6]

The rule extracted: **you own what your AI tells the world.** The deploying company cannot externalize liability to the tool. This rule scales directly from chatbot misrepresentation to AI-generated code that ships a vulnerability to production.

### Mobley v. Workday (N.D. Cal., 3:23-cv-00770)

The vendor-liability crack. Judge Rita Lin held in July 2024 that Workday could be directly liable as an "agent" of employers under Title VII, ADA, and ADEA for discrimination by its AI hiring screener. The court's key holding: "There is no meaningful distinction between software decision-makers and human decision-makers for purposes of determining coverage as an agent." The case was certified as a collective action in July 2025, with the EEOC filing an amicus brief supporting the agency theory.[^7]

Mobley matters because it extends liability beyond the deployer to the vendor. If an AI coding tool's vendor can be a statutory "agent" for purposes of discrimination law, the same agency logic applies wherever the deployer has a non-delegable duty -- securities disclosure, consumer protection, professional practice. The wall between "we used a third-party tool" and "we are liable for what it did" is eroding.

### Caremark and Brewer v. Turner (Del. Ch. 2025)

No AI-specific Caremark case has yet been decided on the merits, but the framework is live. *Brewer v. Turner* (Del. Ch., Sept 29, 2025) refused to dismiss a Caremark oversight claim, confirming the standard is actively enforced.[^8] AI-related securities class actions roughly doubled in 2024 and accelerated in 2025. Directors of public companies deploying AI-assisted code without a documented reporting system face foreseeable Caremark exposure: a "known material risk" -- AI code vulnerabilities -- with no board-level reporting.

## Insurance as De Facto Enforcement

Regulation moves slowly. Insurance moves fast.

Berkley Insurance Group introduced **absolute AI exclusions** for D&O, E&O, and Fiduciary policies in late 2025. The exclusion language covers claims "based upon, arising out of, or attributable to" AI use, deployment, development, AI-generated content, failure to detect AI content, inadequate AI governance, or chatbot communications. Hamilton Insurance Group filed similar exclusions.[^9]

This is not a coverage limitation. It is a coverage elimination. A company without documented AI governance faces the prospect of an AI-related claim with no D&O or E&O coverage to absorb it. The CFO and general counsel -- not just the CISO -- become the buyers of AI governance, because the alternative is uninsured board-level liability.

Underwriters are asking a version of the Caremark question: "Show us your AI governance artifacts." The companies that can produce signed delegation logs, cost caps, scope boundaries, and review gates will get affirmative coverage. The companies that cannot will face absolute exclusions at renewal. Insurance is becoming the fastest, hardest compliance forcing function in the AI governance space.

## The EU AI Act: Article 9 and Risk Management Obligations

The EU AI Act enters its most consequential enforcement phase on August 2, 2026, when high-risk Annex III systems become subject to penalties of up to EUR 35 million or 7% of global annual turnover, whichever is higher.[^10] Finland has already begun enforcement as of January 2026.

Article 9 imposes an explicit **risk management obligation** on providers and deployers of high-risk AI systems: a continuous, iterative process of identification, analysis, estimation, and evaluation of risks, with documentation of mitigation measures. This is not a voluntary framework. It is a statutory duty with teeth.

For organizations deploying AI coding agents in any context that touches EU-regulated domains -- financial services, healthcare, critical infrastructure, employment -- Article 9 compliance requires exactly the governance primitives that the Learned Hand test would independently demand: documented risk assessments, scope boundaries, monitoring systems, and auditable evidence that the system operated within its intended parameters.

## What a "Reasonable Care" Evidence Pack Looks Like

When plaintiff's counsel asks, "What oversight did you have when this AI wrote that code?", the answer must be documentary, not testimonial. Courts credit contemporaneous records over after-the-fact reconstruction.

A reasonable-care evidence pack for AI agent deployment includes:

1. **Delegation records.** Who authorized this agent to act? What was its approved scope? Was that authorization signed and timestamped? Cryptographically signed delegation tokens with chain-depth enforcement create non-repudiable evidence that a human or identified principal authorized each AI action within a bounded scope.

2. **Append-only audit logs.** What did the agent actually do? An immutable, content-hashed log of every agent action -- every code generation, every file modification, every API call -- is the "reporting information system" that Caremark requires.

3. **Scope enforcement records.** Did the agent stay within its authorized boundaries? Logs showing that the agent was prevented from exceeding its scope (kill switch activations, circuit breaker trips, budget cap enforcement) demonstrate active governance, not passive hope.

4. **Cost governance records.** What did the agent spend? Per-agent cost caps with budget circuit breakers prevent the $2,400-overnight-API-bill scenario and demonstrate financial oversight.[^11]

5. **Review gate records.** Was the agent's output reviewed before deployment? Documented review gates with approval chains show that AI output was not shipped blindly.

6. **Policy documentation.** What was the governance policy? Written AI-use policies, approved-scope definitions, and escalation procedures -- documented before the incident -- are the foundation of the negligence defense.

## The Governance Primitive Stack

The critical insight is that these artifacts should not be created by compliance teams after the fact. They should be **generated automatically by the governance infrastructure at runtime**.

The stack that produces this evidence consists of four primitives:

- **Signed delegation tokens** (HMAC-SHA256, chain-depth enforcement): produce the delegation record and scope boundary evidence. Each token identifies the authorizing principal, the delegated agent, the permitted scope, and the expiration. The chain-depth limit prevents unbounded delegation cascades.

- **Append-only audit log** (JSONL, content-hashed, immutable): produces the activity record. Every agent action is logged with a UTC timestamp, agent identity, action type, and content hash. The log is append-only by construction -- no edits, no deletions.

- **Kill switch and circuit breaker** (graduated enforcement: DISENGAGED / HALT_NONCRITICAL / HALT_ALL / EMERGENCY): produce the scope enforcement evidence. When an agent exceeds its boundaries -- cost, scope, error rate -- the circuit breaker trips and logs the event.

- **Contract-driven cost governance** (per-agent budgets, token caps, loop detection): produces the financial oversight evidence. Budget overages are prevented, not merely detected.

Together, these primitives map to the NIST AI RMF functions -- GOVERN (governance structure via delegation tokens), MAP (context documented via audit log), MEASURE (metrics via cost governance), MANAGE (enforcement via kill switch and circuit breaker). That conformance carries a **rebuttable presumption of legal compliance** under pending legislation in Washington (HB 2309), Colorado, and Texas.[^12]

## The Caremark Defense for the AI Era

The parallel is exact. In the 1990s, Caremark asked: "Did the board implement a reporting system for known compliance risks?" Companies that could point to compliance programs, hotlines, and audit trails had an affirmative defense. Companies that could not faced personal director liability.

In 2026, the question is: "Did the organization implement a governance system for known AI risks?" Organizations that can produce cryptographically-signed delegation chains, immutable audit logs, and documented enforcement records have a Caremark affirmative defense, a Learned Hand reasonable-care argument, a NIST AI RMF conformance record, and an insurance-underwriting evidence pack -- all generated automatically at runtime, not reconstructed after the breach.

Organizations that cannot produce this evidence face the inverse: no safe harbor, no good-faith defense for punitive damages, no rebuttable presumption, and absolute insurance exclusions at renewal.

The legal question is no longer whether AI governance is necessary. The precedents are set, the insurance market has moved, and the EU enforcement deadline is four months away. The question is whether your governance infrastructure generates the evidence that courts, regulators, and underwriters will demand -- or whether you will be reconstructing it from memory after the subpoena arrives.

---

## Sources

[^1]: AppSec Santa 2026, 6 LLMs, 534 samples (25.1% vuln rate); Veracode 2025 GenAI Code Security Report (2.74x more vulnerable); Apiiro Sept 2025 Fortune 50 analysis (322% priv-esc paths, Azure credentials nearly twice as often). See `03_round3_hard_data_sweep.md`, `05a_round5_primary_sources.md`.

[^2]: Google Antigravity / Gemini 3 Pro drive-wipe incident, December 2025. Source: [CyberNews](https://cybernews.com/security/deeply-sorry-gemini-deletes-developers-drive/). See `04c_round4_incident_harvest.md` #7.

[^3]: CVE-2025-8217, Amazon Q Developer wiper injection, July 2025. Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/amazon-ai-coding-agent-hacked-to-inject-data-wiping-commands/), [AWS Security Bulletin AWS-2025-015](https://aws.amazon.com/security/security-bulletins/AWS-2025-015/). See `04c_round4_incident_harvest.md` #2.

[^4]: Slopsquatting research, Lasso Security (Bar Lanyado), 576,000 LLM-generated code samples. Source: [BleepingComputer](https://www.bleepingcomputer.com/news/security/ai-hallucinated-code-dependencies-become-new-supply-chain-risk/), [Trend Micro](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/slopsquatting-when-ai-agents-hallucinate-malicious-packages). See `04c_round4_incident_harvest.md` #9.

[^5]: METR RCT, arxiv 2507.09089 (Becker/Rush/Barnes/Rein), N=16 experienced developers, 246 tasks. See `05a_round5_primary_sources.md`.

[^6]: Moffatt v. Air Canada, 2024 BCCRT 149 (Feb 14, 2024). Sources: [ABA Business Law Today](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/), [CanLII Commentary](https://www.canlii.org/en/commentary/doc/2025CanLIIDocs1963). See `05c_round5_legal_liability.md` Section 2.1.

[^7]: Mobley v. Workday, Inc., 3:23-cv-00770 (N.D. Cal.). Sources: [Seyfarth Shaw](https://www.seyfarth.com/news-insights/mobley-v-workday-court-holds-ai-service-providers-could-be-directly-liable-for-employment-discrimination-under-agent-theory.html), [Fisher Phillips](https://www.fisherphillips.com/en/insights/insights/discrimination-lawsuit-over-workdays-ai-hiring-tools-can-proceed-as-class-action-6-things). See `05c_round5_legal_liability.md` Section 2.2.

[^8]: Brewer v. Turner (Del. Ch., Sept 29, 2025). Source: [Harvard Corporate Governance Blog](https://corpgov.law.harvard.edu/2025/10/30/caremark-claim-survives-boards-delay-in-ending-illegal-practices/). See `05c_round5_legal_liability.md` Section 2.4.

[^9]: Berkley Insurance Group absolute AI exclusions (late 2025); Hamilton Insurance Group similar exclusions. Source: `04a_round4_us_regulatory.md` Section on D&O/E&O AI exclusions.

[^10]: EU AI Act, Regulation (EU) 2024/1689, Article 9 (risk management systems), Annex III (high-risk AI systems). Penalties: EUR 35M or 7% global turnover. Enforcement timeline: Aug 2, 2026 for Annex III. See `04d_round4_devsecops_analogue.md`.

[^11]: Autonomous agent $2,400 overnight API bill; 200-dev Cursor deployment rolled back after $22K/month in overages. Source: [AlterSquare Medium](https://altersquare.medium.com/ai-coding-tools-in-2026-what-we-actually-use-across-20-client-projects-and-what-we-dont-84b3306ce71a). See `04c_round4_incident_harvest.md` #17.

[^12]: Washington HB 2309 (2025) and similar bills in CO, TX creating rebuttable presumption of compliance for NIST AI RMF / ISO 42001 adherence. See `05c_round5_legal_liability.md` Section 6.2.

---

*Research corpus: HUMMBL AI Slop Crisis Research, Rounds 1-5 (April 2026). All citations verified against primary sources in Round 5, Lane G.*
