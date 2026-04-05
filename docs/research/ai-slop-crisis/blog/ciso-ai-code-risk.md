# Your AI Agents Are Writing Vulnerable Code. Your Insurance Won't Cover It.

*The security data is no longer theoretical. AI-generated code is 2.74x more vulnerable than human-written code, insurance carriers are adding absolute AI exclusions, and the governance gap is widening every quarter. Here is what CISOs need to do in the next 90 days.*

---

## The Risk Is Quantified

If you are a CISO still treating AI-generated code as a developer productivity story, the data should change your mind.

Veracode's 2025 GenAI Code Security Report tested more than 100 LLMs across four programming languages. The result: **AI-generated code contains 2.74x more vulnerabilities than human-written code** (Veracode 2025). The failure rate on secure coding benchmarks was 45%.

AppSec Santa's 2026 study went deeper. They gave six frontier LLMs -- GPT-5.2, Claude Opus 4.6, Gemini 2.5 Pro, DeepSeek V3, Llama 4 Maverick, and Grok 4 -- 89 identical coding prompts covering login forms, file uploads, and database queries. No security context was provided. Across **534 samples, 25.1% contained a confirmed security vulnerability** (AppSec Santa 2026). SSRF led with 32 findings. Injection-class weaknesses accounted for 33.1% of all confirmed vulnerabilities.

This is not a sampling artifact. It is the baseline quality of AI-generated code when no explicit security guidance is provided -- which is how most AI code gets written in practice.

## The Problem Is Not Getting Better With Better Models

Here is the finding that should concern you most: despite two years of rapid model improvement, **the security pass rate of AI-generated code has remained stuck at approximately 55%** (Veracode Spring 2026). Models are dramatically better at syntax. They are not meaningfully better at security.

Veracode identified three structural reasons. First, training data: until models are trained on corpora that prioritize secure code, security performance will not improve materially. Second, market incentives: the race to build faster coding assistants has treated security as secondary. Third, architectural limitation: the complex dataflow analysis required for XSS and injection detection remains beyond current LLM architectures.

The "better models will fix it" thesis is now empirically falsified. The SWE-bench leaderboard leader, Claude Opus 4.6 (79.3% Verified), produces the worst security outcomes in adversarial-realistic testing -- a **29.2% vulnerability rate**, tied with DeepSeek and Llama 4 Maverick (AppSec Santa 2026). GPT-5.2, which scores lower on coding benchmarks, produced the best security outcome at 19.1%. The public benchmark ranking inverts what matters for production quality.

## The Volume Makes This a Portfolio Risk

This would be manageable if AI code were a small fraction of your codebase. It is not.

**42% of all code is now AI-generated or AI-assisted** (Sonar 2026 developer survey, n=1,100+). Developers predict that share will exceed 50% by 2027. Meanwhile, Black Duck's 2026 OSSRA report found mean vulnerabilities per codebase jumped **107% year over year** to 581 across 947 audited codebases. 87% contained high or critical severity vulnerabilities.

The vulnerability rate is climbing at the exact moment the volume of AI-generated code is accelerating. That is the actual crisis.

> *"The pace at which software is created now exceeds the pace at which most organizations can secure it."* -- Jason Schmitt, CEO, Black Duck

## Your Insurance Is Retreating

If you are counting on your D&O or E&O policy to backstop an AI-related loss, check your renewal paperwork.

**Berkley Insurance Group introduced an absolute AI exclusion for D&O, E&O, and Fiduciary liability policies in late 2025** (Lexology carrier exclusion analysis, HUB International). The exclusion covers claims "based upon, arising out of, or attributable to" AI use, deployment, development, AI-generated content, failure to detect AI content, inadequate AI governance, and chatbot communications. Hamilton Insurance Group filed similar broad exclusions.

The market is bifurcating. Firms with documented AI governance artifacts -- model inventories, audit trails, risk management frameworks -- are getting affirmative coverage. Firms without are facing absolute exclusions at renewal. Carriers are now asking underwriting questions about AI tool deployment, training data provenance, governance frameworks, human-in-the-loop processes, and regulatory compliance posture (HUB International, Insurance Business America).

Insurance is becoming the de facto enforcement mechanism for AI governance, ahead of any US federal statute.

## The Liability Chain Points at You

The legal landscape reinforces the insurance picture. In **Moffatt v. Air Canada (2024 BCCRT 149)**, the tribunal rejected the argument that a chatbot is a separate entity -- the deploying company owns all AI output and eats the liability. In **Mobley v. Workday**, certified as a collective action in July 2025, the court held that an AI vendor can be directly liable as a statutory "agent" of its customer, potentially cracking vendor ToS shielding.

Until Mobley resolves, the deployer is the deep pocket with the non-delegable duty to end-users. Vendor liability caps -- Anthropic caps at $100 or 6 months of fees, whichever is greater -- offer no meaningful protection at enterprise scale (Downing analysis of Copilot indemnity; Anthropic ToS).

## What 81% of Organizations Are Missing

Cycode's 2026 AI Security Report found that **81% of organizations lack visibility into how AI is actually used in their codebases**. AI coding agents now run with developer-level privileges: they execute shell commands, read environment files, and connect to internal APIs through MCP servers that most security teams have never examined. You cannot govern what you cannot see.

Meanwhile, Aikido Security's 2026 survey of 450 developers and security leaders found **1 in 5 organizations has already experienced a serious security incident linked to AI-generated code**.

## The 90-Day Action Plan

The data is clear. The insurance market is moving. The liability chain points at the deployer. Here is what to do.

**Days 1-30: Inventory and visibility.**
Catalog every AI coding tool in use across your organization. Map MCP server connections. Identify which repositories contain AI-generated code and at what percentage. You cannot assess risk you have not measured.

**Days 31-60: Policy and controls.**
Establish a mandatory security review gate for AI-generated code before it reaches production. Define which operations AI agents are allowed to perform -- and which require human approval. Implement audit trails that record what was generated, by what model, with what prompt, and reviewed by whom. This is your "reasonable care" evidence if a regulator or plaintiff comes calling.

**Days 61-90: Governance architecture.**
Move from bolted-on scanning to built-in governance. The three loops of enforcement are: inner loop (IDE-level prevention as code is written), middle loop (policy enforcement in CI/CD), and outer loop (portfolio-level visibility for leadership). Organizations that move from Level 1 to Level 3 AI governance maturity see a **40% reduction in AI-related technical debt** and a **25% improvement in time-to-market** for new agentic features (CISIN 2026).

The goal is not to slow down AI adoption. It is to make AI adoption defensible -- to your board, your insurer, and your regulator.

---

**Assess your readiness**: [hummbl.io/readiness](https://hummbl.io/readiness) -- free AI governance self-assessment for security leaders.

**Stay informed**: Subscribe to the [HUMMBL Slop Tracker](https://hummbl.io/tracker) -- weekly evidence digest on AI code quality, governance, and regulatory developments.
