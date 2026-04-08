# Case Study: Shipping 20 Governance Primitives with Zero Dependencies

**A Stdlib-Only Python Library for AI Agent Governance**

---

**Client:** HUMMBL, LLC (Internal Product Development)  
**Architect:** Reuben Bowlby, Founder & Principal Architect  
**Timeline:** Q1 2026  
**Stack:** Python 3.11+ · stdlib only · PyPI · GitHub Actions · ruff

---

## The Challenge

Every AI governance vendor ships a SaaS platform. Qodo, Apiiro, Factory, Aikido, Cycode — all require sending code or telemetry to their cloud. For enterprises operating in air-gapped, classified, or regulated environments, that is a non-starter. For teams embedding agents in production pipelines, adding a network dependency to a governance check is a latency and reliability liability.

The market had no embeddable, inline governance library that could run wherever the agent runs — no cloud, no vendor lock-in, no transitive dependency tree to audit.

---

## The Solution

### Design Constraints

The architecture followed three hard rules extracted from 2+ years of multi-agent production operations:

1. **Zero runtime dependencies.** Every module uses only Python's standard library. No `requests`, no `pydantic`, no `jsonschema`. This eliminates supply chain risk, simplifies air-gap deployment, and removes version conflicts.

2. **Independent importability.** Each primitive is a self-contained module. Teams can import `KillSwitch` without pulling in `CostGovernor`. No framework coupling, no hidden initialization.

3. **Contract-driven interfaces.** Every primitive enforces explicit contracts — typed enums for states, HMAC-SHA256 signatures for tokens, append-only semantics for audit trails. No implicit behavior.

### The 20 Primitives

| Category | Primitives |
|---|---|
| **Safety controls** | KillSwitch (4 graduated modes), CircuitBreaker (CLOSED/HALF_OPEN/OPEN), CapabilityFence |
| **Authorization** | DelegationToken (HMAC-SHA256 signed), AgentRegistry (identity + trust tiers) |
| **Observability** | AuditLog (append-only JSONL), HealthCollector (composable probes), BusWriter (TSV coordination) |
| **Compliance** | ComplianceMapper (SOC 2, GDPR, OWASP), StrideMapper (threat modeling) |
| **Validation** | SchemaValidator (JSON Schema Draft 2020-12), OutputValidator, InputValidator |
| **Cost governance** | CostGovernor (soft/hard caps, ALLOW/WARN/DENY) |
| **Reasoning** | ReasoningEngine, and 6 additional primitives |

### Implementation Approach

**Schema validation without `jsonschema`:** The `SchemaValidator` implements JSON Schema Draft 2020-12 validation using only `json`, `re`, and `urllib.parse` from stdlib. This was the hardest primitive to build — Draft 2020-12 has recursive `$ref` resolution, `if/then/else` conditionals, and format validation. The implementation handles all of these without external dependencies.

**Cryptographic tokens without `cryptography`:** `DelegationToken` uses `hmac` and `hashlib` from stdlib for HMAC-SHA256 signing. Tokens carry agent identity, scope arrays, and TTL — enough for capability-based authorization without a token service.

**Append-only audit without a database:** `AuditLog` writes JSONL to the filesystem with rotation and retention policies. `BusWriter` uses `fcntl.flock` for cross-process coordination on a TSV file. Both are designed for environments where the only reliable storage is the local filesystem.

---

## Results

**Published on PyPI:** [`hummbl-governance`](https://pypi.org/project/hummbl-governance/) v0.3.0 — installable in any Python 3.11+ environment with `pip install hummbl-governance`.

**476 tests passing.** Full coverage across all 20 modules, including edge cases for token expiry, circuit breaker state transitions, kill switch mode escalation, and schema validation against Draft 2020-12 test suites.

**Arbiter grade: A (99.5).** Scored by HUMMBL's own code quality engine across ruff lint, cyclomatic complexity, security analysis, dead code detection, and duplication.

**Zero transitive dependencies.** `pip show hummbl-governance` shows `Requires:` empty. No supply chain to audit. No Dependabot alerts possible on runtime deps.

**Deployed in production.** The library governs HUMMBL's own multi-agent fleet — the same primitives that ship to customers are used internally to coordinate Claude, Codex, and infrastructure agents across 15,000+ tests daily.

---

## Technical Stack Summary

| Layer | Technology |
|---|---|
| Language | Python 3.11+ (stdlib only) |
| Package registry | PyPI |
| Signing | HMAC-SHA256 (stdlib `hmac` + `hashlib`) |
| Schema validation | JSON Schema Draft 2020-12 (stdlib implementation) |
| Audit storage | Append-only JSONL + TSV with `fcntl.flock` |
| Code quality | Arbiter (ruff + complexity + security + dead code) |
| CI/CD | GitHub Actions |
| License | Apache 2.0 |

---

## Key Takeaways

**Zero dependencies is a feature, not a constraint.** Every transitive dependency is a supply chain risk surface, a version conflict waiting to happen, and a compliance audit line item. For governance code — the code that decides whether an agent can act — the dependency count should be zero.

**Governance primitives must be embeddable, not orchestrated.** A kill switch that requires a network call to a vendor API is not a kill switch. Governance checks must execute inline, in-process, at the speed of the agent's decision loop.

**Self-referential proof matters.** HUMMBL uses `hummbl-governance` to govern the fleet that builds `hummbl-governance`. This is not a demo — it is daily production validation that the primitives work under real multi-agent coordination pressure.

---

## About HUMMBL

HUMMBL, LLC is a boutique AI governance consultancy that helps organizations design, deploy, and harden production AI agent systems. HUMMBL develops governance libraries — not platforms — to fill the gap between AI agent capabilities and the controls enterprises need.

**Website:** [hummbl.io](https://hummbl.io)  
**Founded by:** Reuben Bowlby  
**Focus:** AI Agent Governance · Compliance Mapping · Stdlib-Only Libraries · MCP Development

---

*© 2026 HUMMBL, LLC. All rights reserved.*
