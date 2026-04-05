# 5 Things Every CISO Should Know About AI-Generated Code Right Now

*HUMMBL Slop Tracker — Issue #1 | April 2026*

---

AI-generated code is now ~42% of all committed code — and it ships 2.7x more vulnerabilities than humans write. Insurers have begun excluding it from coverage. Governments have begun fining it. This is the inaugural issue of the Slop Tracker — a monthly digest of the incidents, rulings, and regulatory moves reshaping how enterprises deploy AI agents.

---

## 1. The numbers are not improving

**42% of committed code is now AI-generated** (Sonar 2026 survey, n=1,100+). Veracode confirms it ships **2.74x more vulnerabilities** than human-written code. The security pass rate has been **stuck at ~55% for two years** despite capability gains.

**The models are getting smarter. The code isn't getting safer. Capability and safety are decoupling.**

## 2. The leaderboard is inverted

Claude Opus 4.6 hits 79.3% on SWE-bench Verified — and produces vulnerable code in 29.2% of samples. GPT-5.2 scores lower on both axes. **SWE-bench no longer predicts shipping-safe code.** If your procurement team is using benchmark scores to evaluate AI coding tools, they're measuring the wrong thing.

The KPI for coding agents should be "vulnerabilities per LOC" or "security pass rate," not SWE-bench scores.

## 3. Insurance moved first

Berkley wrote absolute AI exclusions into D&O and E&O policies starting Q1 2026 — not just for "unmanaged" AI code, but for any AI-related claims regardless of governance posture. The path back to coverage runs through demonstrating documented controls: model inventory, output validation, audit trails. Hiscox and Beazley are rumored to follow.

The implication: **companies without documented AI governance will become uninsurable before they become unprosecutable.** And "documented AI governance" means concrete controls — model inventory, usage policies, and evidence-generating guardrails mapped to owners — not a three-page policy PDF. Insurance is enforcement arriving years before any state AG gets around to prosecution.

## 4. The liability chain is settling in court

Two rulings to know:

**Moffatt v. Air Canada (2024)**: Deploying company eats chatbot liability. **The AI tool is the company's mouth.** Now cited in 3+ US district court filings.

**Mobley v. Workday (cert. July 2025)**: Pushes liability up-chain — the AI vendor may be an "agent" under Title VII. If this theory holds, your AI vendor gets added as a co-defendant.

Your lawyers are already preparing for this. Your AI agents are not — and the gap between those two is your evidentiary risk surface.

## 5. The EU AI Act clock is running

Enforcement goes live **August 2, 2026**. Penalties: €35M or 7% of global revenue, whichever is greater. Finland has been enforcing since January under the "member states may enforce earlier" provision.

**If you ship AI into the EU, the clock is not approaching — it is running.**

---

## Incident of the Month

**September 2025, Fortune 50 firm** — Apiiro's customer data shows AI-assisted commits exposed Azure credentials nearly twice as often as human-authored commits. Privilege-escalation paths increased 322%.

The security team caught it, not the AI tool — which is also what generated the exposures.

An output-validation gate tied to credential patterns (detecting keys, tokens, and secrets via regex and entropy), run inline before the agent's `git commit` fires, would have caught the obvious leaks pre-commit. Cost to implement: ~50 lines of code. But the deeper risk isn't the leaked credential — it's the architectural drift that accumulates silently across thousands of AI-generated commits until a breach surfaces it all at once. Cost of the incident: undisclosed, but credential rotation plus incident response burns $250K–$2M at F50 scale.

**The agents are useful. The agents are unsupervised. The gap between "useful" and "supervised" is where the governance market lives.**

---

## The Wedge Nobody Is Filling

The governance vendor landscape: Qodo ($120M), Factory ($50M), Apiiro ($135M), Aikido ($60M), Cycode ($80M). Each ships a SaaS platform. Each requires sending code or telemetry to their cloud.

None of them ship governance primitives — libraries that enforce policies and log evidence at the point of generation — **as pip-installable packages** you can embed inline, air-gap, inspect, and audit.

A signed delegation token is not a vendor pitch. It is a **Caremark affirmative defense**, a **NIST AI RMF conformance record**, and a **reasonable-care evidence pack** — generated at runtime, not reconstructed after the breach.

---

## Quote of the Month

> "AI generation is commoditizing. Every vendor will have it. Differentiation accrues to the layer that governs output quality, enforces policy, tracks provenance, and maintains accountability. This is the observability argument applied to AI."
>
> — HUMMBL, *Round 4 Research Synthesis* (April 2026)

---

## What to read next

Every stat and claim in this issue is backed by primary sources in the full evidence pack (24 documents, 50+ cited sources, verified):
[github.com/hummbl-dev/hummbl-dev/tree/main/docs/research/ai-slop-crisis](https://github.com/hummbl-dev/hummbl-dev/tree/main/docs/research/ai-slop-crisis)

Want a governance posture check? Take the self-assessment at [hummbl.io/readiness](https://hummbl.io/readiness.html).

Questions? reuben@hummbl.io

---

*Next issue: May 2026. Coverage: EU AI Act countdown, first enforcement actions, procurement RFP shifts.*

*HUMMBL Slop Tracker is free. Subscribe at [hummbl.io/tracker](https://hummbl.io/tracker.html).*
