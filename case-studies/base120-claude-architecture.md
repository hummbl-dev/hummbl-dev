# Case Study: Building the HUMMBL Base120 Cognitive Framework

**A Claude-Powered Architecture for Structured Reasoning at Scale**

---

**Client:** HUMMBL, LLC (Internal Product Development)  
**Architect:** Reuben Bowlby, Founder & Principal Architect
**Timeline:** 2+ years (2024–2026)
**Stack:** Claude API · Cloudflare Workers · Cloudflare D1 · MCP · React · GitHub Actions

---

## The Challenge

Organizations using AI for complex decision-making face a fundamental gap: large language models are powerful reasoning engines, but without structured frameworks, their outputs are inconsistent, unrepeatable, and difficult to audit. Enterprise teams need systematic approaches to AI-assisted reasoning — not just better prompts, but cognitive architecture that guides AI toward validated, traceable conclusions.

HUMMBL set out to solve this by building a comprehensive cognitive framework — 120 validated mental models organized into a formal operator algebra — and delivering it through Claude-powered production infrastructure.

---

## The Solution

### Framework Architecture: Base120

HUMMBL developed the Base120 framework: 120 mental models organized across six transformation operators, each representing a distinct cognitive operation:

- **Perspective (P):** Frame and anchor point of view (20 models)
- **Inversion (IN):** Reverse assumptions and examine opposites (20 models)
- **Composition (CO):** Combine and synthesize elements (20 models)
- **Decomposition (DE):** Break complex systems into parts (20 models)
- **Recursion (RE):** Apply patterns at multiple scales (20 models)
- **Meta-Systems (SY):** Analyze the systems that govern other systems (20 models)

The operators are non-commutative — the order of application matters — expressed formally as T₁∘T₂∘...∘Tₙ = Artifact. This mathematical property enables repeatable, auditable reasoning chains.

### Production Infrastructure

The framework is delivered through a production system built natively on Claude and modern cloud infrastructure:

**API Layer:** Cloudflare Workers handle API requests with D1 database storage and KV caching, providing global edge deployment with low-latency response times.

**Claude Integration:** The Claude API powers model selection, application guidance, and validation — transforming the Base120 library from a static reference into an interactive reasoning engine.

**MCP Server Architecture:** Model Context Protocol servers expose the 120 mental models as Claude-accessible tools, resources, and prompts. Any Claude user can invoke structured reasoning frameworks directly within their workflows — for example, applying First Principles Framing (P1) or Feedback Loop Mapping (RE3) as part of a complex analysis.

**Context Engineering:** HUMMBL developed a structured approach to context window composition using the Base120 operators — treating context construction as formally as database schema design, with explicit operator sequencing and quality validation.

**CI/CD Pipeline:** GitHub Actions automate testing, linting, and deployment across the monorepo (managed with pnpm), with comprehensive test suites targeting high coverage.

**Frontend:** React application deployed at [hummbl.io](https://hummbl.io) provides the user-facing cognitive toolkit interface.

### Multi-Agent Coordination

Complex development tasks are orchestrated through a multi-agent system using structured, typed message-bus coordination protocols:

- Claude serves as the strategic lead for architecture and decision-making
- Infrastructure tasks are delegated to specialized agents
- Tactical execution follows authorization-gated workflows

This coordination pattern — validated through 2+ years of production use — directly informed HUMMBL's governance architecture, including the `hummbl-governance` runtime package: kill switch, circuit breaker, cost governor, delegation tokens, audit log, identity registry, and schema validator — all extracted as a standalone, zero-dependency Python library (476 tests, Apache 2.0).

---

## Results

**Framework Quality:** All 120 mental models are published, accessible via MCP server and REST API, and organized with empirically derived priority levels (P1–P7) based on usage frequency.

**Production Deployment:** [hummbl.io](https://hummbl.io) is live and serving users, with the full Base120 library accessible through both the web interface and MCP server infrastructure.

**Governance Package:** The `hummbl-governance` runtime package was extracted from production infrastructure — 20 modules, 476 tests, zero third-party dependencies. Available at [github.com/hummbl-dev/hummbl-governance](https://github.com/hummbl-dev/hummbl-governance).

**Test Infrastructure:** The underlying platform maintains 15,000+ automated tests across 14 CI workflows, running on every commit via self-hosted runners.

**Architecture Scalability:** The Cloudflare Workers + D1 architecture handles global edge deployment without traditional server management, while the MCP server design enables any Claude user to access HUMMBL's cognitive frameworks.

---

## Technical Stack Summary

| Layer | Technology |
|-------|------------|
| AI Engine | Claude API (Anthropic) |
| Tool Protocol | Model Context Protocol (MCP) |
| API / Compute | Cloudflare Workers |
| Database | Cloudflare D1 |
| Cache | Cloudflare KV |
| Frontend | React |
| CI/CD | GitHub Actions |
| Package Management | pnpm (monorepo) |
| Governance | hummbl-governance (kill switch, circuit breaker, cost governor) |
| Agent Coordination | Typed message-bus protocol (append-only TSV) |

---

## Key Takeaways

**Structured reasoning frameworks make AI outputs repeatable and auditable.** Without cognitive architecture, LLM outputs vary unpredictably. The Base120 framework provides the systematic scaffolding that enterprise decision-making requires.

**MCP transforms static frameworks into interactive tools.** By exposing mental models as MCP-accessible tools, HUMMBL makes structured reasoning available to every Claude user — not just HUMMBL customers.

**Context engineering is a production discipline.** Treating context window composition with the same rigor as database schema design — using explicit operators, validation, and structured sequencing — produces measurably better outputs.

**Multi-agent coordination requires explicit protocols and governance.** In production multi-agent systems, there is no shared memory between agents. Every piece of information must be explicitly passed, authorized, and verified. Governance primitives (kill switches, circuit breakers, delegation tokens) are not optional — they are the difference between a demo and a production system. HUMMBL validated this through 2+ years of daily multi-agent operations.

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│                    hummbl.io (React)                 │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│              Cloudflare Workers (API)                │
│         ┌──────────┬──────────┬──────────┐          │
│         │   D1 DB  │   KV    │  Claude   │          │
│         │ (models) │ (cache) │   API     │          │
│         └──────────┴──────────┴──────────┘          │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│              MCP Server Infrastructure               │
│  ┌─────────┐  ┌───────────┐  ┌─────────────────┐   │
│  │  Tools  │  │ Resources │  │    Prompts      │   │
│  │(120     │  │(framework │  │(transformation  │   │
│  │ models) │  │ data)     │  │ templates)      │   │
│  └─────────┘  └───────────┘  └─────────────────┘   │
└─────────────────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│           Claude Desktop / Claude.ai                 │
│     Users invoke mental models as native tools       │
└─────────────────────────────────────────────────────┘
```

---

## About HUMMBL

HUMMBL, LLC is a boutique AI architecture practice that helps organizations design, deploy, and harden production Claude systems. HUMMBL develops the Base120 cognitive framework and the `hummbl-governance` runtime to make Claude's reasoning capabilities more systematic, repeatable, and enterprise-ready.

**Website:** [hummbl.io](https://hummbl.io)
**Founded by:** Reuben Bowlby
**Focus:** Cognitive AI Architecture · Agent Governance · Claude Integration · MCP Development

---

*© 2026 HUMMBL, LLC. All rights reserved.*
