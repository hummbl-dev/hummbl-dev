# HUMMBL Slop Tracker — Issue #1

**April 2026 · Inaugural edition**

*AI-generated code is now ~40% of committed code. It ships 2.7× more vulnerabilities than humans write. Insurers have begun excluding it from coverage. Governments have begun fining it. This newsletter tracks the incidents, rulings, and regulatory moves that will reshape how enterprises deploy AI agents — and the governance gap nobody is filling.*

---

## TL;DR — 5 things you should know

1. **AI code is 42% of committed code now**, per Sonar's 2026 survey (n=1,100+). Veracode confirms it ships **2.74× more vulnerabilities** than human-written code — and the security pass rate has been **stuck at ~55% for two years** despite model capability gains. Capability and safety are decoupling.
2. **SWE-bench is inverted.** Claude Opus 4.6 hits 79.3% on SWE-bench Verified — and produces vulnerable code in 29.2% of samples. GPT-5.2 scores lower on both. **The leaderboard no longer predicts shipping-safe code.**
3. **Insurers have moved first.** Berkley wrote absolute AI exclusions into D&O and E&O policies starting Q1 2026. No governance posture, no underwritten coverage. This is de-facto enforcement, arriving years before any state AG gets around to prosecution.
4. **Liability chain is settling in court.** *Moffatt v. Air Canada* (2024) established that the deploying company eats chatbot liability. *Mobley v. Workday* (cert. July 2025) pushes liability further up-chain to the AI vendor as a Title VII "agent." Both rulings survived appeals. **Your lawyers are already preparing for this. Your agents are not.**
5. **EU AI Act enforcement goes live August 2, 2026.** €35M or 7% of global revenue, whichever is greater. Finland has been enforcing since January. If you ship AI into the EU, the clock is not approaching — it is running.

---

## Incident Card — September 2025, Fortune 50 firm

> **What happened:** Apiiro's customer data shows that from March to September 2025, AI-assisted commits at a single Fortune 50 firm exposed **Azure credentials nearly twice as often** as human-authored commits over the same window. Privilege-escalation paths increased 322%.
>
> **Who caught it:** The security team, not the AI tool. The AI tool is what generated the exposures.
>
> **What governance primitive would have caught it pre-commit:** An output-validation gate tied to credential patterns, run inline before the agent's `git commit` fires. Cost to implement: ~50 LOC. Cost of the incident: undisclosed, but credential rotation plus incident response burns ~$250K-$2M per event at F50 scale.

**The thesis in one line:** *The agents are useful. The agents are unsupervised. The gap between "useful" and "supervised" is where the governance market lives.*

---

## By the Numbers

| Stat | Source | Why it matters |
|---|---|---|
| **42%** of code now AI-generated | Sonar 2026 (n=1,100+) | The denominator is large and growing |
| **2.74×** vulnerability ratio, AI vs human | Veracode 2025 GenAI report | Not a rounding error |
| **25.1%** of AI samples had confirmed vulnerabilities | AppSec Santa, 534 samples, 6 LLMs | Holds across leading models |
| **19% slower** with AI tools, believed 20% faster | METR RCT, arxiv 2507.09089 | 39pp perception gap — ops leaders are flying blind |
| **75%** of enterprises plan agentic AI deployment | Deloitte State of AI 2026 | Volume is coming |
| **21%** have mature governance in place | Deloitte State of AI 2026 | Governance is not coming |
| **38.5%** of Fortune 1000 now have a CAIO | MIT AI Leadership Benchmark | +6pp YoY, +a budget holder |

---

## Regulatory Watch

**US Federal.** Trump EO 14179 (Jan 2025) loosened federal AI guidance, but didn't preempt state law. Colorado AI Act is delayed to June 2026; NYC Local Law 144 is live; FTC has opened AI-related enforcement actions. **Patchwork, but escalating.**

**EU.** AI Act fines activate Aug 2 2026. Finland's NCA has been enforcing since Jan 2026 under the "member states may enforce earlier" provision. Expect the first cross-border enforcement action within 6 months of the August date.

**Insurance.** Berkley is the first public exclusion, not the last. Hiscox and Beazley are rumored to follow. The implication: **companies without documented AI governance will become uninsurable in specific classes of coverage before they become unprosecutable.**

**Case law.** Moffatt v. Air Canada is now cited in at least 3 US district court filings over AI-generated content liability. Mobley v. Workday is the vendor-agent test that will define whether your AI vendor gets added as a co-defendant.

---

## The Wedge

The governance vendor landscape today: Qodo ($120M), Factory ($50M), Apiiro ($135M), Aikido ($60M), Cycode ($80M). Each ships a SaaS platform. Each requires sending source code or runtime telemetry to their cloud. Each has a governance gap for workloads that cannot leave the customer's infrastructure — classified systems, regulated healthcare, air-gapped environments, allied-nation deployments.

None of them ship governance primitives **as pip-installable libraries** you can embed inline in an agent's execution path, air-gap, inspect, and audit. That's the HUMMBL wedge: **stdlib-only, contract-driven, readable, deployable wherever your classified workloads deploy.**

A signed delegation token is not a vendor pitch. It is a Caremark affirmative defense, a NIST AI RMF conformance record, and a reasonable-care evidence pack — **generated at runtime, not reconstructed after the breach.**

---

## Quote of the Month

> *"AI generation is commoditizing. Every vendor will have it. Differentiation accrues to the layer that governs output quality, enforces policy, tracks provenance, and maintains accountability. This is the observability argument applied to AI."*
>
> — HUMMBL Round 4 Synthesis

---

## What to read next

Full primary-source evidence pack: [github.com/hummbl-dev/hummbl-dev/tree/main/docs/research/ai-slop-crisis](https://github.com/hummbl-dev/hummbl-dev/tree/main/docs/research/ai-slop-crisis) — 24 documents, 50+ cited primary sources, verified by a dedicated audit lane.

---

## Subscribe / Talk

- **Subscribe** to Slop Tracker: `hummbl.io/tracker` *(TODO: wire mailing list)*
- **Self-assess** your governance posture: `hummbl.io/assessment` *(TODO: publish)*
- **Talk to us** about embedded governance for regulated workloads: `reuben@hummbl.io`

*Next issue: May 2026. Coverage: post-EU-AI-Act-countdown briefing, first court rulings to watch, procurement RFP shifts.*

---

*Issue #1 · Published 2026-04-05 · HUMMBL, LLC · [hummbl.io](https://hummbl.io)*
*All statistics cite primary sources verified in the research corpus. Corrections welcome: [github.com/hummbl-dev/hummbl-dev/issues](https://github.com/hummbl-dev/hummbl-dev/issues)*
