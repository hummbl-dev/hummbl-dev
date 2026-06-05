# HUMMBL for Defense / Federal — Positioning One-Pager
### AI governance primitives for IL4/IL5 workloads, CMMC 2.0, and federal AI acquisition

---

## Evidence posture

This document is a **defense/federal positioning one-pager** built from the research corpus and HUMMBL's public product posture.

- It mixes public product facts with research-backed regulatory and market synthesis.
- It should not be treated as a definitive statement of current federal procurement, CMMC audit practice, or legal advice without fresh verification.
- Buyer, pricing, and market-window statements are strategic hypotheses, not public guarantees.

See [`../../PROOF_AND_RESEARCH_EVIDENCE_POSTURE.md`](../../PROOF_AND_RESEARCH_EVIDENCE_POSTURE.md) before external reuse.

---

## The problem

Defense primes and federal contractors are being asked to deploy AI-assisted development tooling under accelerating compliance obligations. Commercial AI governance SaaS is often a poor fit for IL4/IL5 or similarly constrained environments, which may leave an opening for local-first governance approaches.

**What changed in 2024-2026**:

- **CMMC 2.0 effective Dec 2024** — unmanaged AI-assisted development may create control and evidence problems for Level 2 environments; validate current assessor practice before external reuse
- **OMB M-25-21 and M-25-22 (April 2025)** — federal AI acquisition now requires documented risk management, logging, and human oversight
- **DoD Responsible AI Strategy** — implementation cascading to primes and subcontractors
- **NIST AI RMF + SP 800-53 rev 5 AI controls** — federal baseline for AI-adjacent systems
- **Anthropic, OpenAI, Meta all announce gov-cloud offerings** — model access is no longer the blocker; **governance is**

Prime-to-subcontractor governance requirements appear to be tightening, especially where AI-assisted workflows touch sensitive environments. Specific exclusion or bid-loss claims should be validated against current buyer evidence.

---

## What buyers need that they cannot get from commercial SaaS

| Requirement | Commercial SaaS (Credo, Holistic, OneTrust, Fairly) | HUMMBL |
|-------------|----|--------|
| Deployable into IL4/IL5 air-gap | Often cloud-first | ✅ Designed for portable, local-first use |
| Open-source, auditable by government assessors | Often limited visibility | ✅ Full source review |
| Zero third-party runtime dependencies (supply chain) | Often multi-layer dependency graph | ✅ Python stdlib only |
| Contract-driven, SBOM-compatible | ⚠️ Partial | ✅ `fm-contracts-vX.Y` baseline tags |
| Append-only governance audit (FedRAMP-aligned positioning) | Often proprietary formats | ✅ JSONL, grep-friendly, inspector-readable |
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
- **Illustrative pricing hypothesis:** $150K-$300K ACV for mid-tier primes (validate against current design-partner discovery)
- Hybrid model: flat platform fee + per-agent metering + optional assessor-readiness assist
- Open-source core; commercial contract for support, indemnification, and assessor preparation

### Trojan horse
Start with a single cleared engineering team, demonstrate the audit artifacts map 1:1 to CMMC 2.0 Level 2 Practice requirements, expand horizontally across the prime.

---

## The talking points

### For the CISO at a defense prime
> *"If unmanaged AI-assisted development is becoming a Level 2 evidence problem for your teams, a local-first governance layer gives you something an assessor can inspect directly. HUMMBL's positioning is append-only audit trails, signed delegation records, and portable runtime controls rather than dashboard-only visibility."*

### For the Chief AI Officer / Head of Responsible AI
> *"Commercial AI governance is building dashboards for the compliance team. HUMMBL is building the runtime kill switch, circuit breaker, and delegation tuple enforcement that your agents actually execute. It's the `cryptography` library of agent governance, not the Splunk dashboard. You import it; you own the policy."*

### For the contracts / legal team
> *"Closed-source SaaS can complicate auditability and evidence gathering in regulated environments. HUMMBL's position is that open, portable governance primitives can produce stronger runtime evidence for risk, oversight, and framework mapping than a dashboard-only model."*

---

## Proof points to cite

- **CMMC 2.0 Level 2** Practice requirements (SC-7, AU-2, AC-2, SI-4) map to HUMMBL primitives
- **Georgia Tech Vibe Security Radar**: 74+ AI-attributable CVEs, Claude Code leaves a signature (valuable *for* attribution, exploitable *against* unmanaged use)
- **Apiiro Fortune 50 data**: 322% more privilege escalation paths in AI-generated code
- **Veracode**: AI code is 2.74× more vulnerable than human-written; security pass rate stuck at 55% for 2 years
- **MCP risk**: CVE-2025-6514 (mcp-remote RCE), postmark-mcp backdoor hit ~300 orgs Sept 2025
- **Moffatt v. Air Canada**: deployer liability remains a key legal signal to track
- **Mobley v. Workday** (pending/evolving): vendor-liability theory is worth monitoring, not treating as settled universal doctrine

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

Because **"signed, append-only, air-gap-capable, stdlib-only"** describes a constraint set that can be highly attractive in regulated environments. HUMMBL's hypothesis is that this architecture aligns well with federal/defense buyer needs where portability, inspectability, and audit evidence matter more than dashboard convenience.

And because the flywheel is real: **success in DoD → credibility in healthcare → entry to Fortune 500**. Defense/Federal is the hardest regulated vertical, which is why winning it is the best possible case study for everything downstream.

---

*Snapshot note: this one-pager is a positioning artifact derived from research lanes and public product posture. Recheck regulatory timing, buyer behavior, pricing, and legal implications before formal external use.*
