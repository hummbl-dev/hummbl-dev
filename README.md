# HUMMBL

**Governance primitives for AI agent orchestration.** Stdlib-only. Contract-driven. Air-gap capable.

AI-generated code is [42% of committed code](https://docs.research/ai-slop-crisis/03_round3_hard_data_sweep.md) and ships [2.74x more vulnerabilities](https://docs.research/ai-slop-crisis/03_round3_hard_data_sweep.md) than humans write. Insurers are [excluding it from coverage](https://docs.research/ai-slop-crisis/newsletters/2026-04-slop-tracker-01.md). Courts are [settling the liability chain](https://docs.research/ai-slop-crisis/essays/reasonable-care-age-of-agents.md). Nobody ships governance as embeddable libraries. We do.

```bash
pip install hummbl-governance
```

[![PyPI](https://img.shields.io/pypi/v/hummbl-governance)](https://pypi.org/project/hummbl-governance/)
[![Tests](https://img.shields.io/badge/tests-476%20passing-brightgreen)]()
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)]()
[![Dependencies](https://img.shields.io/badge/runtime%20deps-zero-brightgreen)]()

---

## What you get

20 governance primitives, all Python stdlib-only, all independently importable:

| Primitive | What it does |
|---|---|
| **KillSwitch** | Emergency halt with 4 graduated modes (DISENGAGED → EMERGENCY) |
| **CircuitBreaker** | Automatic failure detection + recovery (CLOSED / HALF_OPEN / OPEN) |
| **DelegationToken** | HMAC-SHA256 signed capability tokens for agent scope authorization |
| **AuditLog** | Append-only JSONL governance trail with rotation and retention |
| **AgentRegistry** | Identity management with aliases and trust tiers |
| **SchemaValidator** | JSON Schema Draft 2020-12 validation (stdlib, no jsonschema dep) |
| **CostGovernor** | Budget tracking with soft/hard caps and ALLOW/WARN/DENY decisions |
| **BusWriter** | Append-only TSV coordination bus with flock locking |
| **ComplianceMapper** | Map governance traces to SOC 2, GDPR, and OWASP controls |
| **HealthCollector** | Composable health probes with latency tracking |
| + 10 more | OutputValidator, CapabilityFence, StrideMapper, ReasoningEngine, ... |

```python
from hummbl_governance import KillSwitch, CircuitBreaker, DelegationToken

ks = KillSwitch(state_dir=Path("./governance"))
cb = CircuitBreaker(failure_threshold=5, recovery_timeout=60)
token = DelegationToken.create(agent="codex", scope=["read", "write"], ttl=3600)
```

---

## Why libraries, not platforms

Every AI governance vendor (Qodo, Apiiro, Factory, Aikido, Cycode) ships a SaaS platform. Each requires sending code or telemetry to their cloud.

HUMMBL ships **libraries you embed inline** in your agent's execution path. No cloud dependency. No vendor lock-in. Deployable wherever your workloads deploy — including air-gapped, classified, and regulated environments.

> "A signed delegation token is not a vendor pitch. It is a Caremark affirmative defense, a NIST AI RMF conformance record, and a reasonable-care evidence pack — generated at runtime, not reconstructed after the breach."

Read the full thesis: [Why Libraries, Not Platforms](docs/research/ai-slop-crisis/essays/why-libraries-not-platforms.md)

---

## Research

Our positioning is backed by a 24-document evidence corpus with 50+ primary-source citations, verified:

**Start here:**
- [Top 10 cite-ready findings](docs/research/ai-slop-crisis/README.md)
- [The Observability Argument](docs/research/ai-slop-crisis/essays/the-observability-argument.md) — why AI governance is the Datadog moment
- [The 22 Incidents](docs/research/ai-slop-crisis/essays/the-22-incidents.md) — cataloged AI code failures (2023-2026)
- [Reasonable Care in the Age of AI Agents](docs/research/ai-slop-crisis/essays/reasonable-care-age-of-agents.md) — what courts will look for

**Role-specific:**
[CISO](docs/research/ai-slop-crisis/blog/ciso-ai-code-risk.md) | [CAIO](docs/research/ai-slop-crisis/blog/caio-governance-gap.md) | [GC/Legal](docs/research/ai-slop-crisis/blog/gc-ai-liability-chain.md) | [CTO](docs/research/ai-slop-crisis/blog/cto-developer-velocity-trap.md) | [AppSec](docs/research/ai-slop-crisis/blog/appsec-devsecops-ai-code-reality.md) | [Compliance](docs/research/ai-slop-crisis/blog/compliance-grc-ai-framework-mapping.md) | [Platform Eng](docs/research/ai-slop-crisis/blog/platform-eng-governance-layer.md) | [Risk Manager](docs/research/ai-slop-crisis/blog/risk-manager-ai-insurance-crisis.md) | [Defense/Federal](docs/research/ai-slop-crisis/blog/defense-federal-cmmc-ai-governance.md) | [AI Governance Lead](docs/research/ai-slop-crisis/blog/ai-governance-lead-building-program.md)

---

## By the numbers

| Metric | Value |
|---|---|
| Governance primitives | 20 (stdlib-only, zero runtime deps) |
| Tests (`hummbl-governance`) | 476 passing |
| Tests (`founder-mode` reference impl) | 15,000+ |
| CI workflows | 11 active |
| Research corpus | 60 documents, 50+ primary sources |
| Published on PyPI | [`hummbl-governance`](https://pypi.org/project/hummbl-governance/) v0.3.0 |

---

## Projects

| Project | Purpose |
|---|---|
| [`hummbl-governance`](https://github.com/hummbl-dev/hummbl-governance) | Governance primitives — [PyPI](https://pypi.org/project/hummbl-governance/) |
| [`arbiter`](https://github.com/hummbl-dev/arbiter) | Code quality scoring engine (ruff + complexity + security + dead code + duplication) |
| [`base120`](https://github.com/hummbl-dev/base120) | Base120 mental model reference implementation + validation CLI |
| [`mcp-server`](https://github.com/hummbl-dev/mcp-server) | MCP server exposing Base120 models and governance skills |
| [`hummbl-agent`](https://github.com/hummbl-dev/hummbl-agent) | Deterministic agent infrastructure (registry-first, policy-bounded) |
| [`hummbl-assurance`](https://github.com/hummbl-dev/hummbl-assurance) | Governance assurance — verification, contract compatibility, compliance |

---

## Newsletter

**[HUMMBL Slop Tracker](https://hummbl.substack.com)** — monthly digest of AI code governance incidents, regulations, lawsuits, and the governance gap nobody is filling. Free.

[Read Issue #1: 5 Things Every CISO Should Know About AI-Generated Code Right Now](https://open.substack.com/pub/hummbl/p/5-things-every-ciso-should-know-about)

---

## Get started

```bash
pip install hummbl-governance
```

- **Self-assess**: [hummbl.io/readiness](https://hummbl.io/readiness.html) — 20-question governance posture check
- **Subscribe**: [hummbl.io/tracker](https://hummbl.io/tracker.html) — monthly intelligence digest
- **Talk to us**: reuben@hummbl.io

---

*HUMMBL, LLC | [hummbl.io](https://hummbl.io) | Atlanta, GA*
*Apache 2.0 Licensed*
