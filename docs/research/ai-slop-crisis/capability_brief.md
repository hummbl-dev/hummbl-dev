# HUMMBL — Capability Brief
### Governance primitives for AI-native agent systems

---

## Evidence posture

This brief is a **positioning and capability document**, not a sworn operational record.

- Public package/repo surfaces are the strongest evidence for current product facts.
- Research-derived market, legal, insurance, and buyer claims should be treated as source-backed synthesis and rechecked before external high-stakes use.
- Counts, test totals, CI totals, and competitive-market figures are snapshot claims and may drift.

See [`../../PROOF_AND_RESEARCH_EVIDENCE_POSTURE.md`](../../PROOF_AND_RESEARCH_EVIDENCE_POSTURE.md) for reuse guidance.

---

## Who we are

**HUMMBL, LLC** — founded and operated by Reuben Bowlby (Atlanta, GA). Solo founder publishing open-source governance infrastructure and adjacent reasoning/governance tooling.

Three specializations combined:
1. **Platform / SRE engineering** — multi-machine agent infrastructure, health probes, circuit breakers, and governed workflow patterns
2. **AI governance architecture** — delegation tokens, governance bus, kill switches, capability attestation
3. **Structured reasoning at scale** — Base120 cognitive framework and related SDK / MCP delivery surfaces

---

## What we ship

### `hummbl-governance` — [PyPI](https://pypi.org/project/hummbl-governance/)
**Public package surface: stdlib-only runtime dependencies, Python 3.11+, PyPI-distributed. Snapshot counts should be rechecked against the current public repo/package surface before reuse.**

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
Public reference implementation for Base120 models, SDK access, and related tooling surfaces.

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
In a supply-chain threat landscape where npm/pip compromise risk is material, running governance infrastructure with zero runtime third-party dependencies is a distinctive positioning choice.

### Open-source, auditable
Open-source delivery creates a more inspectable surface for buyers who need direct review rather than dashboard-only claims.

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
2. **Chief AI Officer at regulated enterprise** — governance maturity still lags deployment appetite in many enterprises; verify current benchmark figures before external reuse
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
- **Public package and repo surfaces** for `hummbl-governance`, `base120`, and `mcp-server`
- **Installable public distributions** where available (for example, PyPI / npm)
- **Open-source implementation detail** visible in current public repositories
- **Research corpus** supporting the broader market and governance thesis

### Governance pattern proof
Our own multi-agent development process demonstrates the pattern at work:
- Multiple AI agents (Claude Code, Codex, Gemini) committing to shared repositories
- Delegation tokens and governance bus enforcing scope between agents
- Kill switch and circuit breaker patterns used in live production

### Research corpus
- Full research library at `docs/research/ai-slop-crisis/` — 16 docs + synthesis + 2 one-pagers
- Positioning claims are intended to be source-traceable, but legal/regulatory/market claims should still be rechecked against primary materials before formal external use

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

*Snapshot note: this capability brief mixes public proof surfaces with research-backed synthesis. Recheck package metrics, market figures, and legal/regulatory claims before formal external reuse.*
