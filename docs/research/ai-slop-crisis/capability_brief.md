# HUMMBL — Capability Brief
### Governance primitives for AI-native agent systems

---

## Who we are

**HUMMBL, LLC** — founded and operated by Reuben Bowlby (Atlanta, GA). Solo founder with a multi-agent orchestration platform, publishing open-source governance infrastructure. Production Claude systems since 2024.

Three specializations combined:
1. **Platform / SRE engineering** — 11 CI workflows, multi-machine fleet, launchd orchestration, health probes, circuit breakers
2. **AI governance architecture** — delegation tokens, governance bus, kill switches, capability attestation
3. **Structured reasoning at scale** — Base120 cognitive framework (120 canonical mental models, 660+ extensions), 2+ years of development

---

## What we ship

### `hummbl-governance` — [PyPI](https://pypi.org/project/hummbl-governance/)
**476 tests, 20 modules, zero runtime third-party dependencies, Python stdlib only.**

| Primitive | What it does |
|-----------|-------------|
| **Delegation Capability Tokens (DCT)** | HMAC-SHA256 signed tokens carrying scope, chain-depth, expiry. Runtime attribution for every agent action. |
| **Governance Bus** | Append-only JSONL audit log. grep-friendly, assessor-readable, evidence-preservation compliant. |
| **Delegation Context (DCTX)** | Chain-depth enforcement. Agents cannot escalate privilege by chaining delegations past configured depth. |
| **Circuit Breaker** | CLOSED/HALF_OPEN/OPEN state machine wrapping external adapters. Fails fast when upstream degrades. |
| **Kill Switch** | 4-mode emergency halt (DISENGAGED, HALT_NONCRITICAL, HALT_ALL, EMERGENCY). Runtime-enforced, file-system-persisted. |
| **Contract schemas** | Frozen `fm-contracts-v0.1` baseline. SemVer major bump required for breaking changes. |
| **Event store** | SQLite event persistence with content hashing. |

### `base120` — authoritative reference implementation
120 canonical mental models + 660 extended, with contract validation CLI. Two-year development arc, audited, versioned.

### `mcp-server`
Model Context Protocol server exposing Base120 mental models and Claude Code skills. [GitHub](https://github.com/hummbl-dev/mcp-server).

### `hummbl-agent`
Deterministic agent infrastructure — registry-first, policy-bounded. For teams building agents that must stay within scope.

### `hummbl-assurance`
Governance assurance primitives — deterministic verification, contract compatibility, compliance claims.

### `governed-iac-reference`
Reference IaC with governance policy, change validation, and audit trails.

---

## Why the approach is differentiated

### Stdlib-only, zero third-party runtime deps
In a supply-chain threat landscape where npm/pip backdoors are a monthly occurrence (postmark-mcp, tj-actions, xz utils), running governance infrastructure with zero third-party attack surface is a **category of one**.

### Open-source, auditable
Government assessors, enterprise GC offices, and regulated-industry CISOs cannot audit proprietary SaaS. HUMMBL's entire source is reviewable.

### Library, not platform
HUMMBL ships as a Python package you import. Not a dashboard you log into. Not a SaaS you route agent traffic through. This means:
- **Air-gap deployable** (IL4/IL5, classified networks, on-prem)
- **No vendor lock-in** (governance primitives are yours once imported)
- **Composable** (integrates with existing compliance stacks, doesn't replace them)

### Contract-driven, versioned
Every schema is a canonical contract. Breaking changes require SemVer major bump + new baseline tag. No silent API drift.

### Agent-native, not code-scanner-retrofitted
Competitors (Qodo, Apiiro, Aikido, Snyk) scan code. HUMMBL enforces at runtime what an agent is *allowed to do* — scope, blast radius, authority delegation. Scanners describe problems after they happen. HUMMBL prevents them.

---

## Market positioning

### Where HUMMBL fits

**Inside the $10B+ DevSecOps / AI code security pool**, as the **runtime governance primitives layer** that other vendors (scanners, gateways, dashboards) can import.

### What HUMMBL is not

- Not a SaaS platform
- Not a code scanner
- Not a pre-merge review tool
- Not a compliance dashboard
- Not a replacement for your existing AppSec stack

### What HUMMBL is

- The `cryptography` / `pydantic` / `requests` of agent governance
- The runtime substrate where policy decisions get *enforced*, not just described
- The audit-trail substrate that produces evidence for your NIST RMF / ISO 42001 / SOC 2 / CMMC assessor

### Buyer personas

1. **Defense / Federal CISO** — blocked on CMMC, needs IL4/IL5-capable governance
2. **Chief AI Officer at regulated enterprise** — 75% deploying agentic AI, only 21% have mature governance (Deloitte 2026)
3. **Platform engineer building internal agent infrastructure** — needs library primitives, not another dashboard
4. **Legal / Risk leader** — needs documented governance as affirmative defense

---

## Competitive landscape — one screen

| Vendor | Funding | Model | What they ship | What they don't |
|--------|---------|-------|----------------|-----------------|
| Qodo | $120M | SaaS | Code review automation | No runtime primitives |
| Factory | $50M | SaaS | AI eng platform | Closed-source |
| Apiiro | $135M | SaaS | Code AppSec | Scans, doesn't enforce |
| Aikido | $60M | SaaS | AppSec scanner | No agent governance |
| Cycode | $80M | SaaS | ASPM | No runtime control |
| CodeRabbit | $88M | SaaS | AI code review | Pre-merge only |
| Credo AI | Series B | SaaS | Governance platform | Cloud only, closed |
| Fiddler, Arize, WhyLabs | $68M-$131M | SaaS | Model observability | Not code/agent governance |
| Snyk, Veracode, GitHub | Public/established | SaaS | Traditional AppSec | No agent-native primitives |
| **HUMMBL** | **Bootstrapped** | **Open-source library** | **Runtime governance primitives, stdlib-only, air-gap capable** | **Not a dashboard, not a platform** |

---

## Evidence and credibility

### Technical proof
- **14,400+ tests** across the founder-mode platform
- **476 tests** in hummbl-governance alone (stdlib-only)
- **11 active CI workflows** (security scans, mutation testing, contract validation, quality scoring)
- **2+ years of production operation** of the underlying platform
- **Published on PyPI** with contract baseline governance

### Governance pattern proof
Our own multi-agent development process demonstrates the pattern at work:
- Multiple AI agents (Claude Code, Codex, Gemini) committing to shared repositories
- Delegation tokens and governance bus enforcing scope between agents
- Kill switch and circuit breaker patterns used in live production

### Research corpus
- Full research library at `docs/research/ai-slop-crisis/` — 16 docs + synthesis + 2 one-pagers
- Every positioning claim cites primary sources (arxiv, NIST, EU regulatory docs, case law)

---

## What we're building next

### Near-term (Q2 2026)
- **MCP attestation reference implementation** — first local-first MCP governance primitives layer
- **CMMC 2.0 practice-to-primitive mapping** — for defense / federal buyers
- **EU AI Act Aug 2026 compliance narrative** — for multinational enterprises
- **Insurance-exclusion sales angle** — for CFO / GC buyers

### Mid-term (H2 2026)
- **First design partner** — mid-tier defense prime or regulated healthcare system
- **Conference presence** — RSA, DEF CON AI Village, EU AI Act conferences
- **Open standards contribution** — agent-governance OpenTelemetry equivalent

### Strategic
- Hold the primitive layer as Gartner's AI Governance Magic Quadrant forms (2027-2028)
- Partner, don't compete, with Qodo/Factory/Apiiro — be the library they import
- Win regulated verticals first (defense → healthcare → finance) because they have the hardest constraints that favor HUMMBL's architecture

---

## Contact

- **Owner**: Reuben Bowlby (100%)
- **Email**: reuben@hummbl.io
- **Website**: hummbl.io
- **GitHub**: github.com/hummbl-dev
- **Booking**: cal.com/hummbl/30min

---

*This capability brief is backed by 16 research documents, 5 research rounds, ~250K tokens of primary source analysis. See `docs/research/ai-slop-crisis/` for the full evidence base.*
