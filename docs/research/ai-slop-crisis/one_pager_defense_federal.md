# HUMMBL for Defense / Federal — Positioning One-Pager
### AI governance primitives for IL4/IL5 workloads, CMMC 2.0, and federal AI acquisition

---

## The problem

Defense primes and federal contractors are being asked to deploy AI-assisted development tooling under accelerating compliance obligations. **Commercial AI governance SaaS cannot operate in IL4/IL5 environments.** The market is structurally open.

**What changed in 2024-2026**:

- **CMMC 2.0 effective Dec 2024** — DIBCAC assessors now flag unmanaged Copilot / Claude / agent usage as Level 2 findings
- **OMB M-25-21 and M-25-22 (April 2025)** — federal AI acquisition now requires documented risk management, logging, and human oversight
- **DoD Responsible AI Strategy** — implementation cascading to primes and subcontractors
- **NIST AI RMF + SP 800-53 rev 5 AI controls** — federal baseline for AI-adjacent systems
- **Anthropic, OpenAI, Meta all announce gov-cloud offerings** — model access is no longer the blocker; **governance is**

Primes are cascading AI governance requirements to subs, which can kill a contract. Sub-contractors without documented AI governance posture are being excluded from bids.

---

## What buyers need that they cannot get from commercial SaaS

| Requirement | Commercial SaaS (Credo, Holistic, OneTrust, Fairly) | HUMMBL |
|-------------|----|--------|
| Deployable into IL4/IL5 air-gap | ❌ Cloud-only | ✅ Stdlib-only, fully portable |
| Open-source, auditable by government assessors | ❌ Proprietary | ✅ Full source review |
| Zero third-party runtime dependencies (supply chain) | ❌ Multi-layer npm/pip graph | ✅ Python stdlib only |
| Contract-driven, SBOM-compatible | ⚠️ Partial | ✅ `fm-contracts-vX.Y` baseline tags |
| Append-only governance audit (FedRAMP-aligned) | ⚠️ Proprietary formats | ✅ JSONL, grep-friendly, inspector-readable |
| Signed delegation tokens (HMAC-SHA256) | ❌ Not offered | ✅ IDP Phase 0 shipped |
| Kill switch + circuit breaker as library primitives | ❌ SaaS dashboards only | ✅ Stdlib primitives, air-gap safe |
| Runtime attribution: which agent, which prompt, which policy | ⚠️ External audit only | ✅ Built into DCTX |

---

## HUMMBL's sales motion

### Wedge buyer
**Mid-tier defense primes and cleared sub-contractors** (50-500 engineers) deploying AI-assisted development into classified or CUI workloads, currently blocked by:
- CMMC assessor findings on unmanaged Copilot
- IL4/IL5 air-gap requirements that exclude commercial SaaS
- Prime cascade requirements they can't currently satisfy

### Value proposition (one sentence)
**"Governance primitives that deploy where your classified workloads deploy — stdlib-only, air-gap capable, contract-driven, and readable by your CMMC assessor."**

### Pricing anchor
- **$150K-$300K ACV** for mid-tier primes (below Fortune 1000, above seat pricing)
- Hybrid model: flat platform fee + per-agent metering + optional assessor-readiness assist
- Open-source core; commercial contract for support, indemnification, and assessor preparation

### Trojan horse
Start with a single cleared engineering team, demonstrate the audit artifacts map 1:1 to CMMC 2.0 Level 2 Practice requirements, expand horizontally across the prime.

---

## The talking points

### For the CISO at a defense prime
> *"DIBCAC is flagging your Copilot usage as a Level 2 finding. Your assessor cannot audit Credo's proprietary dashboard. HUMMBL's governance primitives produce append-only JSONL audit trails the assessor can grep from the command line. The HMAC-SHA256-signed delegation tokens give you runtime attribution you can trace to the individual agent invocation. Same architecture runs in your corporate cloud and your IL5 SCIF."*

### For the Chief AI Officer / Head of Responsible AI
> *"Commercial AI governance is building dashboards for the compliance team. HUMMBL is building the runtime kill switch, circuit breaker, and delegation tuple enforcement that your agents actually execute. It's the `cryptography` library of agent governance, not the Splunk dashboard. You import it; you own the policy."*

### For the contracts / legal team
> *"Your indemnification chain breaks when you run AI-generated code through a closed-source SaaS you cannot audit. HUMMBL is open-source, stdlib-only, no third-party supply chain. Our governance record maps to NIST AI RMF conformance and provides the Caremark affirmative defense evidence your GC needs when (not if) the first AI-attributable breach lands in litigation."*

---

## Proof points to cite

- **CMMC 2.0 Level 2** Practice requirements (SC-7, AU-2, AC-2, SI-4) map to HUMMBL primitives
- **Georgia Tech Vibe Security Radar**: 74+ AI-attributable CVEs, Claude Code leaves a signature (valuable *for* attribution, exploitable *against* unmanaged use)
- **Apiiro Fortune 50 data**: 322% more privilege escalation paths in AI-generated code
- **Veracode**: AI code is 2.74× more vulnerable than human-written; security pass rate stuck at 55% for 2 years
- **MCP risk**: CVE-2025-6514 (mcp-remote RCE), postmark-mcp backdoor hit ~300 orgs Sept 2025
- **Moffatt v. Air Canada**: deploying company eats the loss when AI fails
- **Mobley v. Workday** (pending): vendor-liability theory, could reshape entire chain

---

## The 90-day plan

**Weeks 1-4**: MCP attestation reference implementation (stdlib + IDP Phase 0). Public GitHub repo. Map to OWASP MCP Top 10.

**Weeks 5-8**: CMMC 2.0 practice-mapping doc. Every HUMMBL primitive to CMMC practice ID. Produce the handout that a prime's CISO hands to their DIBCAC assessor.

**Weeks 9-12**: First design partner engagement with a mid-tier prime. Success metric: assessor sign-off on HUMMBL-governed AI workflow at Level 2.

---

## The risks

1. **Federal acquisition cycles are slow** — 12-18 months from POC to contract
2. **IL5 certification of tooling itself** is a high bar — may need partner for formal ATO path
3. **Anthropic / OpenAI / Microsoft** may ship their own gov-cloud governance — HUMMBL has to be in market before they do
4. **Inertia** — existing primes have procurement relationships with Credo, OneTrust; stdlib-only is unfamiliar to non-eng buyers

---

## Why this wins

Because **"signed, append-only, air-gap-capable, stdlib-only"** isn't a feature list — it's a set of constraints that **no commercial SaaS can satisfy and every regulated buyer needs**. HUMMBL's architecture is already aligned with federal/defense buyer requirements. The product-market fit is structural, not marketing.

And because the flywheel is real: **success in DoD → credibility in healthcare → entry to Fortune 500**. Defense/Federal is the hardest regulated vertical, which is why winning it is the best possible case study for everything downstream.

---

*Source research: Round 4 Lane A (US regulatory), Lane B (competitive intel), Lane F (enterprise spend), Round 5 Lane K (regulated verticals compound compliance).*
