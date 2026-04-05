# Legal Liability for AI-Generated Code Failures

**Research Round 5 — Legal Liability Chain**
**Date:** 2026-04-05
**Scope:** Liability allocation when AI-generated code causes harm (security breach, IP infringement, discrimination, financial loss)

---

## 1. The Liability Chain: Who Gets Sued?

When AI-generated code causes harm, plaintiffs face a menu of potential defendants. Current doctrine points sharply at the **deployer** (the company that ships the code), with vendors shielded by contract and developers shielded by employment. But the edges are moving.

| Candidate | Current Exposure | Trajectory |
|---|---|---|
| **Individual developer** (who prompted AI) | Low in employment context (respondeat superior). Higher for contractors and solo devs. Professional negligence theories emerging. | Rising where supervision is thin or where professional standards apply (lawyers, engineers under PE licensure). |
| **Employer / deploying company** | **HIGH — default bearer of liability.** Air Canada rule, Mobley agency theory, Caremark oversight. | Highest; becoming the settled default. |
| **AI tool vendor** (GitHub Copilot, Cursor, Windsurf, Claude Code) | Low direct exposure — shielded by ToS disclaimers. IP indemnity carve-outs exist but are narrow. Agency theory (Mobley) is the crack. | Rising via Mobley agency theory + product-liability framing. |
| **Foundation model provider** (Anthropic, OpenAI, Google) | Very low direct — aggressive LoL caps ($100 / 6-months of fees at Anthropic), broad "as is" disclaimers. | Exposed via IP training-data suits (Doe v. GitHub, NYT v. OpenAI) but code-harm claims not yet landed. |
| **Cloud infra provider** (AWS, Azure, GCP) | Near zero — Section 230 analogues, IaaS neutrality, thick contracts. | Stable; only at risk if they are also the model provider (Bedrock, Azure OpenAI). |
| **Third-party MCP / tool-server operator** | **Emerging wildcard.** No case law. Indirect-prompt-injection attacks (GitHub MCP, Perplexity Comet) make these the new attack surface. | Rising fastest. Expect first lawsuit 2026-2027 naming an MCP operator as co-defendant in a breach. |

**Default allocation today:** The deploying company eats the loss. It is the party with the duty of care to the end-user, a deep pocket, and a contract that waives recourse against the vendor.

---

## 2. Current Case Law

### 2.1 Moffatt v. Air Canada, 2024 BCCRT 149 (Feb 14, 2024)
The foundational precedent. BC Civil Resolution Tribunal held Air Canada liable for negligent misrepresentation by its chatbot. Air Canada argued the chatbot was a "separate legal entity"; the tribunal rejected that out of hand. **Rule extracted: you own what your AI tells the world.** Damages were small ($650.88 CAD), but the rule scales directly to AI-generated code: if your AI-assisted code ships a wrong answer to a customer, you can't hide behind the tool.

### 2.2 Mobley v. Workday, Inc., 3:23-cv-00770 (N.D. Cal.)
The vendor-liability crack. Judge Rita Lin (July 12, 2024) held Workday could be **directly liable as an "agent" of employers** under Title VII/ADA/ADEA for discrimination by its AI hiring screener. July 2025: certified as a collective action. The court's key holding: "There is no meaningful distinction between software decision-makers and human decision-makers for purposes of determining coverage as an agent." The EEOC filed an amicus supporting this theory.

**Why it matters for code:** If an AI vendor can be a statutory "agent" for discrimination, the same agency logic extends to any domain where the deployer has a non-delegable duty (securities disclosure, consumer protection, professional practice).

### 2.3 Doe v. GitHub, Inc., 4:22-cv-06823 (N.D. Cal.)
The IP boundary. Judge Jon Tigar dismissed the DMCA §1202(b) claims (July 2024) holding AI-generated code must be **identical** to copyrighted work to trigger CMI-stripping liability. Surviving claims: open-source license violation and breach of contract. On appeal to 9th Circuit (opening brief filed April 2025) on whether §1202(b) has an "identicality" requirement. **Practical read: the IP risk from training-data is narrow; the risk from license compliance and contract is real.**

### 2.4 Shareholder Caremark claims
No AI-code Caremark case has yet been decided on the merits, but the framework is in place. *Brewer v. Turner* (Del. Ch. Sept 29, 2025) refused to dismiss a Caremark oversight claim — showing the standard is live. AI-related securities class actions roughly doubled in 2024 and accelerated in 2025. Directors of public companies deploying AI-assisted code without a documented reporting system face foreseeable *Marchand/Caremark* exposure: a "known material risk" with no board-level reporting.

### 2.5 SEC enforcement (adjacent)
October 2024: SEC settled ~$7M with four public companies for "negligently minimized" disclosures about a supply-chain breach. This is the template for the first AI-code-breach SEC action: if AI-generated code caused the breach and disclosures obscured it, that is actionable independent of the underlying tort.

---

## 3. Contract & ToS Analysis

### 3.1 Vendor disclaimers (current)
- **Anthropic API ToS (Oct 8, 2025):** Services "as is, as available"; no warranties; **LoL capped at greater of fees paid in prior 6 months or $100**; no consequential damages even if foreseeable; **customer indemnifies Anthropic** for customer's use and third-party rights violations.
- **OpenAI, Cursor, Windsurf:** Materially similar — broad disclaimer, low LoL cap, customer-indemnifies-vendor structure.
- **GitHub Copilot:** Same base structure but layered with the Microsoft **Copilot Copyright Commitment** (Sept 2023) — Microsoft will defend copyright claims arising from unmodified Copilot suggestions *if* the customer has content filtering enabled and uses the enterprise/business tier. This is the most generous vendor indemnity in market.

### 3.2 The indemnification carve-outs swallow the rule
Kate Downing's 2023 analysis remains accurate: the GitHub/Microsoft indemnity excludes (a) modified suggestions, (b) use with filters disabled, (c) use combined with customer content that triggered the infringement. The indemnity also allows Microsoft to "terminate the license" or "modify/replace the product" as its remedy — meaning in a major suit, Microsoft can walk away and leave the customer to rewrite the code.

### 3.3 What enterprises are actually negotiating
Based on practitioner reports (Cooley, WSGR, Gunderson 2024-2025 bulletins):
1. **Uncapped IP indemnity** for AI training-data infringement (standard ask, often granted for F500).
2. **Removal of customer-indemnifies-vendor** for model outputs.
3. **Audit rights** over training-data provenance and red-team testing.
4. **Data-use prohibitions** — no training on customer prompts/outputs (GitHub Copilot Business/Enterprise already concedes this).
5. **Incident-response SLAs** — 24-hour notification of model-level security events.
6. **Model-version stability** — no silent model swaps mid-contract.

---

## 4. Legal Profession Guidance

### 4.1 ABA Formal Opinion 512 (July 29, 2024)
First comprehensive ABA ethics opinion on generative AI. Key mappings:
- **Model Rule 1.1 (competence):** lawyers must understand GAI capabilities and limits and update that understanding periodically.
- **Model Rule 1.6 (confidentiality):** informed consent required before inputting client confidences; boilerplate engagement-letter consent is insufficient.
- **Model Rule 5.1 / 5.3 (supervision):** managerial lawyers must establish firm-wide AI policies; partners are responsible for associates' and nonlawyer staff's AI use.

**Parallel for engineering:** The ABA opinion is the template that professional engineering boards and state bars (CA, FL, NY state bar opinions in 2024-2025) are copying. Expect analogous PE board guidance 2026-2027. Once PE licensure is implicated in AI-code supervision, individual-engineer exposure rises.

### 4.2 ACC / general counsel guidance
Association of Corporate Counsel (2024-2025): recommends AI governance committees, written AI-use policies, model risk management (adopted from bank regulatory SR 11-7), and vendor diligence playbooks before procurement.

---

## 5. Academic Scholarship

- **Bryan Choi, "AI Malpractice"** (SSRN 4721923) — argues for strict liability short-term, professional malpractice standard long-term. Builds on his earlier "Crashworthy Code" (Wash. L. Rev. 2019) — software should be designed to minimize harm when it fails, not just prevent failure. This is the intellectual foundation for "governance-by-design."
- **Ryan Calo, "Robotics and the Lessons of Cyberlaw"** (Cal. L. Rev. 2015) — foundational framing; AI requires new liability rules because embodied/autonomous systems break traditional tort categories.
- **Margot Kaminski & Meg Leta Jones, "Constructing AI Speech"** (Yale L.J. Forum 2024) — law *constructs* the technology; liability rules will shape what AI becomes.
- **Maarten Herbosch, "Liability for AI Agents"** (N.C. J.L. & Tech. 2025) — surveys agency-law approaches and principal liability for autonomous agents. Directly applicable to code-writing agents.
- **Lawfare, "Negligence Liability for AI Developers"** (2024) — argues classic negligence (foreseeability + reasonable care) is sufficient and is already being applied.

**Product liability theory:** Scholars split on whether AI tools are "products" (strict liability) or "services" (negligence). The trend in 2025 rulings is toward a hybrid: software-as-service for the model itself, product-like duties for deployed outputs. Restatement (Third) of Torts §19 includes software in "product" definition in some jurisdictions.

---

## 6. Duty-of-Care Emergence

### 6.1 The question: when does it become negligent to ship AI-assisted code without governance?

**Answer (as of April 2026):** Probably already, for regulated industries. Definitely by 2027 for general commercial deployment.

The mechanism is classic Learned Hand (B < PL): burden of governance is low ($ cost of audit logs, review gates, signed provenance), probability of loss is demonstrably high (45% of AI code has vulnerabilities per 2025 studies; 10,000+ new findings/month by June 2025), and magnitude of loss is catastrophic (average breach remediation $4.5M).

### 6.2 NIST AI RMF + ISO 42001 as de facto duty
Neither is statutorily required federally. But:
- **Washington (HB 2309, 2025)** and similar bills in CO, TX create a **rebuttable presumption of legal compliance** for developers following NIST AI RMF or ISO 42001.
- Conversely, failure to implement creates **affirmative litigation exposure**: no safe harbor, no good-faith defense for punitive damages, no rebuttal presumption.

This is the same mechanism that made NIST CSF the de facto cybersecurity duty after 2014 — voluntary framework becomes negligence baseline through state legislation and judicial notice.

### 6.3 Security-defaults analogy
*T.J. Hooper* (1932): tugboat industry custom of not carrying radios did not immunize defendant; reasonable care required the radios even if industry hadn't adopted them. Applied here: even if your peers don't have AI governance, the court can hold that reasonable care required it. NIST AI RMF 1.0 (Jan 2023) gave courts a concrete standard to point to.

---

## 7. The HUMMBL Angle: Governance as Liability Defense

HUMMBL's architecture — **signed delegation tokens + append-only audit log + contract-driven cost governance** — maps directly onto the emerging duty-of-care defenses.

### 7.1 Three defensive postures HUMMBL enables

**(a) Caremark compliance / board oversight:**
The append-only governance bus (IDP JSONL) is exactly the "reporting system and information controls" Caremark requires. A board can point to real-time dashboards and immutable audit trails to show it did not consciously fail to oversee AI use.

**(b) Negligence defense via documented reasonable care:**
HMAC-SHA256 delegation tokens with chain-depth enforcement create non-repudiable evidence that (i) a human or identified agent authorized each AI action, (ii) scope was bounded, (iii) the action fell within policy. This is the "we exercised reasonable care" affirmative defense made concrete — analogous to how signed commits and code review defend against negligent-supervision claims.

**(c) NIST AI RMF / ISO 42001 conformance:**
The architecture maps cleanly to NIST AI RMF GOVERN (governance structure), MAP (context documented), MEASURE (metrics + cost governor), MANAGE (kill switch + circuit breaker). That conformance carries the **rebuttable presumption** benefit under WA/CO/TX pending statutes.

### 7.2 Sharpest talking point
> "When counsel for the plaintiff asks 'what oversight did you have when this AI wrote that code?' — our clients produce a cryptographically-signed, append-only log showing which agent wrote it, under which delegation token, what scope, what budget, what review gate, and which human authorized the delegation chain. That is not a compliance artifact. That is a Caremark affirmative defense, a 'reasonable care' exhibit, and a NIST AI RMF conformance record — generated automatically at runtime, not reconstructed after the breach."

### 7.3 Evidence preservation
Discovery in AI-code suits will ask for: prompts, outputs, model versions, review artifacts, policy configs, approval chains. Most deployers cannot produce these. HUMMBL's append-only ledger + content hashing + version-locked contracts produces them by construction. **Preservation-by-design** is itself a litigation-readiness posture that moves the insurance-risk needle.

---

## Sources

- [BC Tribunal Confirms Companies Remain Liable for Information Provided by AI Chatbot (ABA)](https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/)
- [Case Comment: Moffatt v Air Canada (CanLII)](https://www.canlii.org/en/commentary/doc/2025CanLIIDocs1963)
- [Mobley v. Workday: Court Holds AI Service Providers Could Be Directly Liable (Seyfarth Shaw)](https://www.seyfarth.com/news-insights/mobley-v-workday-court-holds-ai-service-providers-could-be-directly-liable-for-employment-discrimination-under-agent-theory.html)
- [Fisher Phillips: Mobley v. Workday Class Action Certification](https://www.fisherphillips.com/en/insights/insights/discrimination-lawsuit-over-workdays-ai-hiring-tools-can-proceed-as-class-action-6-things)
- [Judge Dismisses DMCA Claim in Doe v. GitHub (The Register)](https://www.theregister.com/2024/07/08/github_copilot_dmca/)
- [BakerHostetler Copilot Litigation Tracker](https://www.bakerlaw.com/the-copilot-litigation/)
- [GitHub Copilot Litigation Case Updates (Joseph Saveri)](https://githubcopilotlitigation.com/case-updates.html)
- [Kate Downing: GitHub Copilot Indemnity Analysis](https://katedowninglaw.com/2023/11/02/yes-github-finally-offered-to-indemnify-for-copilot-suggestions-but/)
- [Microsoft Copilot Copyright Commitment](https://blogs.microsoft.com/on-the-issues/2023/09/07/copilot-copyright-commitment-ai-legal-concerns/)
- [Runtime: AI Vendors Promised Indemnification — Details Are Messy](https://www.runtime.news/ai-vendors-promised-indemnification-against-copyright-lawsuits-the-details-are-messy/)
- [Anthropic API Commercial Terms of Service](https://www.anthropic.com/news/expanded-legal-protections-api-improvements)
- [ABA Formal Opinion 512 (ABA News)](https://www.americanbar.org/news/abanews/aba-news-archives/2024/07/aba-issues-first-ethics-guidance-ai-tools/)
- [ABA Formal Opinion 512 Analysis (UNC Law Library)](https://library.law.unc.edu/2025/02/aba-formal-opinion-512-the-paradigm-for-generative-ai-in-legal-practice/)
- [AI Governance and D&O Liability: 2026 Board Guide](https://insights.techne.ai/p/ai-governance-and-d-and-o-liability)
- [Duty of Supervision in Age of GenAI: Board Mandates (ABA BLT)](https://businesslawtoday.org/2024/03/the-duty-of-supervision-in-the-age-of-generative-ai-urgent-mandates-for-a-public-companys-board-of-directors-and-its-executive-and-legal-team/)
- [Caremark Claim Survives Board's Delay (Harvard Corp Gov)](https://corpgov.law.harvard.edu/2025/10/30/caremark-claim-survives-boards-delay-in-ending-illegal-practices/)
- [Bryan Choi, AI Malpractice (SSRN)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4721923)
- [Herbosch, Liability for AI Agents (N.C. J.L. & Tech.)](https://journals.law.unc.edu/ncjolt/wp-content/uploads/sites/4/2025/04/Herbosch-Liability-for-AI-Agents.pdf)
- [Negligence Liability for AI Developers (Lawfare)](https://www.lawfaremedia.org/article/negligence-liability-for-ai-developers)
- [Kaminski & Jones, Constructing AI Speech (Yale L.J. Forum)](https://yalelawjournal.org/forum/constructing-ai-speech)
- [AI Governance Standards: The Voluntary Framework Becoming Law (Captain Compliance)](https://captaincompliance.com/education/ai-governance-standards-in-the-us-the-voluntary-framework-that-is-quietly-becoming-the-law/)
- [AI Code Security: 45% Vulnerable (Security Magazine)](https://www.securitymagazine.com/articles/101801-ai-introduces-security-vulnerabilities-within-code-in-45-of-cases)
- [AI Coding Tools Security Exploits 2025 (Fortune)](https://fortune.com/2025/12/15/ai-coding-tools-security-exploit-software/)
