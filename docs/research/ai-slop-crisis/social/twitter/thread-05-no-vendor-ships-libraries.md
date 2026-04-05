# Thread 05: No Vendor Ships Libraries

---

**1/** (119 chars)
Every AI governance vendor ships a SaaS platform. None of them ship libraries. Here's why that matters: [thread]

**2/** (276 chars)
We surveyed 10 AI governance and code security vendors: Qodo ($120M raised), Factory ($50M), Apiiro ($135M), Aikido ($60M, $1B valuation), Cycode ($80M), CodeRabbit ($88M), Snyk ($1.15B), Veracode (PE-backed), GitHub Advanced Security, GitLab Duo. Combined: billions in funding.

**3/** (270 chars)
Every single one is closed-source SaaS. Every one requires cloud connectivity and telemetry. Every one operates at point-of-write (PR, IDE) or point-of-scan (CI, dashboard). None operate at point-of-execution -- where autonomous agents actually run.

**4/** (271 chars)
None ship signed delegation tokens (who authorized what agent to do what). None ship an append-only governance bus (auditable agent-to-agent message log). None ship portable circuit breakers or kill switches for agent fleets. The runtime governance layer does not exist.

**5/** (278 chars)
Why this matters for defense: IL4/IL5 classified workloads cannot send telemetry to a SaaS vendor. CMMC assessors need artifacts they can inspect on-prem. Air-gapped environments cannot call home. Every governance vendor in market is architecturally excluded from this buyer.

**6/** (269 chars)
Why this matters for healthcare: HIPAA covered entities under ACA Section 1557 (effective March 2025) own the discrimination risk for AI-assisted decisions. The governance evidence must live where the workload lives. A SaaS dashboard is not an audit artifact.

**7/** (271 chars)
Why this matters for finance: FINRA Rules 3110 (supervision) and 2210 (communications) apply to GenAI. Examiners want model risk management evidence in the firm's systems, not a vendor portal. SR 11-7 compliance means the controls are yours, not rented.

**8/** (249 chars)
What governance primitives actually look like: a Python library. pip install. Import. Configure delegation tokens, circuit breakers, kill switches, governance bus. stdlib-only -- zero third-party runtime dependencies. Runs where your code runs.

**9/** (275 chars)
The architecture: HMAC-SHA256 signed delegation tokens with chain-depth enforcement. Append-only JSONL audit log with content hashing. Circuit breakers (CLOSED/HALF_OPEN/OPEN) wrapping every external adapter. Kill switch with 4 modes. All stdlib. All portable.

**10/** (262 chars)
This is the observability analogy. Before Datadog, monitoring was a SaaS dashboard. Then StatsD shipped as a library. Instrumentation moved into the application. The same shift is coming for AI governance. The primitive belongs in the runtime, not in a portal.

**11/** (234 chars)
Gartner projects $492M in AI governance platform spend in 2026, growing to $1B+ by 2030 at ~30% CAGR. The market is real. But the runtime governance primitives sub-segment -- the library layer -- has no named vendor. Until now.

**12/** (178 chars)
We're building this at HUMMBL. Open-source, stdlib-only, air-gap capable, pip-installable AI governance primitives. For the teams that can't send telemetry to a SaaS vendor.

---

SCHEDULING NOTE: Post Monday 9:00-10:00 AM ET. Competitive positioning threads perform best at start of week when engineering and security leaders are planning. Consider tagging specific vendor accounts (respectfully) to invite engagement and visibility.
