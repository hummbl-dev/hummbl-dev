# Carousel 04: SWE-bench Is Broken. Here's What to Measure Instead.

---

## Slide 1 (Cover)

**HEADLINE:** SWE-bench Is Broken

**Body:** Your AI vendor showed you a benchmark. Here is what it does not tell you.

---

## Slide 2

**HEADLINE:** Claude: 79.3% Verified, 29.2% Vulnerable

**Body:** Claude Opus 4.6 leads SWE-bench Verified at 79.3%. In adversarial-realistic security testing, it produces vulnerable code 29.2% of the time. The leaderboard rank and the security rank are nearly inverse.

**Source:** SWE-bench Verified (Epoch AI); AppSec Santa 2026

---

## Slide 3

**HEADLINE:** GPT-5.2: Same Pattern, Same Problem

**Body:** GPT-5.2 scored best on security at 19.1% vulnerability rate -- but that still means one in five code samples has a confirmed flaw. No model is safe by default.

**Source:** AppSec Santa 2026 (89 samples per model, 6 LLMs)

---

## Slide 4

**HEADLINE:** The Leaderboard No Longer Predicts Safe Code

**Body:** OpenAI's own audit found frontier models could reproduce verbatim gold patches on SWE-bench Verified tasks. OpenAI stopped reporting Verified scores. Contamination rates: 8-10%.

**Source:** OpenAI audit (late 2025); UTBoost framework

---

## Slide 5

**HEADLINE:** Models Memorize, Not Reason

**Body:** O3-class models hit 76% file-path identification accuracy without contextual information -- consistent with memorization. On held-out repos, the same top agents resolve only 18.89% vs 22.96% on SWE-bench instances.

**Source:** "SWE-Bench Illusion" (arXiv 2506.12286)

---

## Slide 6

**HEADLINE:** What to Measure Instead

**Body:** Vulnerabilities per lines of code. Security pass rate on held-out benchmarks. Mean time to remediate AI-introduced findings. These predict production quality. Leaderboard position does not.

---

## Slide 7

**HEADLINE:** Governance Over Capability

**Body:** Better models will not fix this. Security pass rates have been stuck at 55% for two years despite capability gains. What matters is what the model is allowed to do, not how well it codes.

**Source:** Veracode Spring 2026 Update

---

## Slide 8 (CTA)

**HEADLINE:** Stop Buying Benchmarks. Start Measuring Risk.

**Body:** Subscribe to The Slop Tracker for monthly evidence on what AI code benchmarks actually predict -- and what they hide.

---

## POST CAPTION

Your AI coding vendor probably showed you a SWE-bench score. Here is what they did not show you.

Claude Opus 4.6 leads SWE-bench Verified at 79.3%. In independent security testing by AppSec Santa (534 samples, 6 LLMs, OWASP Top 10), it produces vulnerable code 29.2% of the time. The coding benchmark rank and the security rank are nearly inverse.

OpenAI's own audit found frontier models could reproduce verbatim gold patches on Verified tasks. They stopped reporting the metric. Contamination rates are 8-10%. The "SWE-Bench Illusion" paper showed o3-class models identify file paths at 76% accuracy without context -- memorization, not reasoning.

What actually predicts production quality: vulnerabilities per LOC, security pass rates on held-out benchmarks, and time to remediate AI-introduced findings.

SWE-bench tells you how well a model solves known problems. It does not tell you whether the solution is safe to ship.

#SWEBench #AIBenchmarks #CodeSecurity #AIGovernance #SoftwareEngineering #DevSecOps #LLM #MachineLearning #SlopTracker
