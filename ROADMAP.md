# HUMMBL IaC Roadmap

> **libraries over platforms** — controls should live in the execution path
> **receipts over vibes** — every governance claim should leave an audit trail
> **stdlib-first primitives** — core safety controls should survive air-gapped environments
> **human override preserved** — automation assists governance; it does not become the sovereign

**Status:** DRAFT — 2026-06-02 | **Scope:** All HUMMBL infrastructure-as-code repositories

---

## 1. Executive Summary

HUMMBL currently maintains ~100 repositories. Of these, **4 are installable by anyone today** (`hummbl-governance`, `arbiter`, `base120`, `crab`). The rest are either incomplete extractions from the `founder-mode` monolith, research stubs, or operator-specific configurations. This roadmap defines how we build a **massive library of small, inspectable control-plane primitives** — standalone packages that compose into governed agentic systems.

**The strategic decision is made: standalone packages, not consolidation.** `founder-mode` becomes the *integration testbed* that consumes the libraries it birthed.

---

## 2. The Question Storm

Before the plan, the questions this state raises:

### Strategic
1. What is the scope of "HUMMBL IaC" — Python packages only, or also Docker, npm, CLIs, MCP servers?
2. What does "massive library" mean quantitatively? How many packages? What taxonomy?
3. What is the relationship between `founder-mode` (monolith) and extracted libraries?
4. Should `founder-mode` become a consumer of its own libraries, or remain the integration testbed?
5. What is the PyPI namespace strategy? `hummbl-*` for all packages?
6. What is the versioning strategy across 20+ packages? Monorepo lockstep or independent SemVer?
7. What is the dependency graph? Which packages depend on which? Are circular deps forbidden?
8. What is the release cadence?
9. Are consumer apps (`foundermode-app`, `ownward-app`) part of IaC or a separate product layer?
10. Are research repos (`hummbl-theory`, `hummbl-papers`) libraries or documentation?

### Technical
11. How do we extract from `founder-mode` without breaking it? (Strangler fig pattern.)
12. What does "stdlib-first" mean for packages needing HTTP, JSON parsing, crypto? (Python stdlib has these. Optional extras for convenience, not core safety.)
13. How do we maintain "zero third-party runtime deps" while providing optional extras?
14. How do we test cross-package integration?
15. How do we handle Windows/macOS/Linux portability?
16. What is the MCP server strategy? One per package? One per domain?
17. How do we package CLIs? (`pyproject.toml` `[project.scripts]`)
18. What about Docker images?
19. How do we handle configuration? Env vars with documented defaults. No hardcoded operator paths.
20. Is the coordination bus a separate package or part of governance?

### Organizational
21. How many repos is too many? (We have ~100 now. Target: ~25 active, ~75 archived.)
22. What is the archive strategy for incomplete repos?
23. Who maintains each package? (Stewardship model: package owner + bus receipt for every release.)
24. What is the documentation standard? (`README.md` + `ARCHITECTURE.md` + `docs/` + MCP server schema if applicable.)
25. How do we onboard external contributors?
26. What is the relationship between `hummbl-research` and engineering?
27. How do we handle the "HUMMBL" vs "founder-mode" brand? (Namespace audit: `FOUNDER_MODE_NAMESPACE.md` already exists.)

### Ecosystem
28. What is the integration strategy with LangGraph, CrewAI, Anthropic Agent SDK?
29. What is the Gitea vs GitHub strategy? (Public libraries on GitHub + PyPI. Private integration on Gitea.)
30. What about the NVIDIA NemoClaw relationship? (Deployment target, not a dependency.)
31. What is the `evidence-gate` repo's role?
32. What is the `mcp-server` TypeScript repo's role? (Alternative runtime for TypeScript consumers.)

### Execution
33. What is the priority order for extraction?
34. How do we track drift between `founder-mode` and extracted packages?
35. What is the definition of "done" for an extraction?
36. How do we fund this? (Open source core. Hosted/certification tiers for revenue.)
37. What is the monetization model? (PyPI free. Certification + audit services paid.)
38. What about the certification tier mentioned in `base120`?
39. How do we handle backwards compatibility? (`founder-mode` pins library versions, upgrades intentionally.)
40. What is the CI strategy? (Each package has its own CI. A unified `hummbl-fleet` meta-CI runs integration smoke tests weekly.)

---

## 3. The Answer: HUMMBL IaC Taxonomy

The library is organized into **6 layers**, each independently installable:

```
Layer 6: Ecosystem Adapters          # hummbl-langgraph, hummbl-crewai, hummbl-anthropic
Layer 5: Application Primitives    # hummbl-recall, hummbl-intent, hummbl-scout
Layer 4: Agent Lifecycle             # hummbl-crucible, hummbl-trace, hummbl-library
Layer 3: Coordination                # hummbl-bus, hummbl-clp
Layer 2: Verification                # hummbl-contracts, arbiter, evidence-gate
Layer 1: Safety Substrate            # hummbl-governance
```

Each layer depends only on layers below it. No circular dependencies.

### Layer 1: Safety Substrate (SHIPPED)
| Package | Status | PyPI | Tests | MCP |
|---|---|---|---|---|
| `hummbl-governance` | v0.8.0 | ✅ | 1031 | 7 servers |
| `arbiter` | v0.x | ✅ | ~400 | — |
| `base120` | v2.0.0.dev0 | ✅ | — | ✅ |
| `crab` | source | — | — | — |

### Layer 2: Verification
| Package | Status | Blocker |
|---|---|---|
| `evidence-gate` | Repo exists | Needs stdlib-only implementation |
| `hummbl-contracts` | Schemas only | Needs `schema_validator` runtime extraction |

### Layer 3: Coordination
| Package | Status | Blocker |
|---|---|---|
| `hummbl-bus` | Extraction in progress | Drift reconciliation with founder-mode |
| `hummbl-clp` | Extraction in progress | founder-mode coupling in retrieval/consolidation |

### Layer 4: Agent Lifecycle
| Package | Status | Source in founder-mode |
|---|---|---|
| `hummbl-crucible` | Stub | `services/crucible_telemetry.py` |
| `hummbl-trace` | Planned | `services/trace/` |
| `hummbl-library` | Stub | `services/models.py`, shared utils |

### Layer 5: Application Primitives
| Package | Status | Source in founder-mode |
|---|---|---|
| `hummbl-recall` | Designed | `services/boot_context.py`, `cognition/consolidator.py` |
| `hummbl-intent` | 46 tests | `services/agent_intent.py` |
| `hummbl-scout` | Proposed | `services/career_scout.py` |

### Layer 6: Ecosystem Adapters (Future)
| Package | Status | Target |
|---|---|---|
| `hummbl-langgraph` | Proposed | LangGraph integration |
| `hummbl-crewai` | Proposed | CrewAI integration |
| `hummbl-anthropic` | Proposed | Anthropic Agent SDK wrappers |

---

## 4. Extraction Phases

### Phase 1: Safety Substrate (COMPLETE)
- `hummbl-governance` v0.8.0 on PyPI — 25 primitives, 7 MCP servers
- `arbiter` on PyPI — code quality scoring
- `base120` on PyPI — mental models SDK
- `crab` — shell safety (source-only, stdlib-only)

### Phase 2: Coordination (Q3 2026)
- `hummbl-bus` v0.1.0 — append-only TSV bus, stdlib-only
- `hummbl-clp` v0.1.0 — cognitive ledger, BM25 index, stdlib-only core
- Drift reconciliation: establish canonical bus + CLP in extracted repos; founder-mode becomes consumer

### Phase 3: Verification (Q3-Q4 2026)
- `hummbl-contracts` v0.1.0 — JSON schema runtime + validator
- `evidence-gate` v0.1.0 — source-verification gate (stdlib-only)
- `arbiter` v1.0.0 — governance compliance checks integrated

### Phase 4: Agent Lifecycle (Q4 2026)
- `hummbl-crucible` v0.1.0 — agent metrics and telemetry
- `hummbl-trace` v0.1.0 — behavioral trace primitive
- `hummbl-library` v0.1.0 — shared data models and utilities

### Phase 5: Application Primitives (Q1 2027)
- `hummbl-recall` v0.1.0 — spaced retrieval, memory arbiter
- `hummbl-intent` v0.1.0 — spec-driven agent lifecycle
- `hummbl-scout` v0.1.0 — structured discovery pattern

### Phase 6: Ecosystem (Q2 2027+)
- `hummbl-langgraph`, `hummbl-crewai`, `hummbl-anthropic`
- Each is a thin adapter layer: governed tool wrappers, not new primitives

---

## 5. Dependency Graph

```text
hummbl-governance (Layer 1)
    ├── arbiter (Layer 2)         [optional: uses governance primitives for scoring]
    ├── base120 (Layer 1)         [independent mental models]
    ├── hummbl-contracts (Layer 2) [depends on governance for audit schemas]
    ├── hummbl-bus (Layer 3)      [depends on governance for identity enforcement]
    ├── hummbl-clp (Layer 3)      [depends on hummbl-bus for cross-agent messaging]
    ├── hummbl-trace (Layer 4)    [depends on hummbl-bus for append-only pattern]
    ├── hummbl-crucible (Layer 4)  [depends on hummbl-governance for telemetry]
    ├── hummbl-library (Layer 4)   [shared models, minimal deps]
    ├── hummbl-recall (Layer 5)   [depends on hummbl-clp for memory storage]
    ├── hummbl-intent (Layer 5)   [depends on hummbl-governance for delegation]
    └── hummbl-scout (Layer 5)    [depends on hummbl-recall for discovery memory]
```

**Rule:** Packages in Layer N depend only on Layers 1..(N-1). No horizontal coupling within a layer.

---

## 6. Naming + Versioning Strategy

### PyPI Namespace
- All packages: `hummbl-<name>`
- Exception: `arbiter` (already established brand, stays as-is)
- CLI entry points: `hummbl-<name>-mcp` for MCP servers, `hummbl-<name>` for direct CLI

### Versioning
- Independent SemVer per package
- `founder-mode` pins versions in its `pyproject.toml` workspace
- Breaking changes in lower layers trigger cascading version bumps in dependent packages
- Monthly "fleet alignment" review: check for drift, update pins

### Release Gates
Every package release requires:
1. All tests pass (≥80% coverage for new code)
2. `py_compile` clean on Python 3.11–3.14
3. MCP server schema validation (if applicable)
4. Bus receipt posted to coordination bus
5. README install instructions verified on clean machine

---

## 7. Founder-Mode Evolution

`founder-mode` does not die. It evolves:

| Era | Role |
|---|---|
| v0.1–v0.3 | Monolith — everything lived here |
| v0.4+ | Integration testbed — consumes extracted libraries via PyPI |
| v1.0 | Reference implementation — "another team can fork this and run their own fleet" |

**The strangler fig pattern:**
1. Extract a module to standalone repo + PyPI package
2. Update `founder-mode` to `pip install hummbl-<name>` instead of local import
3. Run full founder-mode test suite to verify integration
4. Remove local copy from founder-mode after 1 release cycle
5. founder-mode becomes lighter; libraries become stronger

---

## 8. Archive / Consolidation Plan

Of ~100 repos, the disposition:

| Action | Count | Examples |
|---|---|---|
| **Keep active** | ~25 | `hummbl-governance`, `arbiter`, `base120`, `hummbl-bus`, `hummbl-clp`, `hummbl-recall`, `hummbl-intent`, `hummbl-crucible`, `hummbl-trace`, `evidence-gate`, `hummbl-contracts`, `hummbl-library`, `hummbl-scout`, `hummbl-langgraph`, `hummbl-crewai`, `hummbl-anthropic`, `crab`, `founder-mode`, `hummbl-research`, `hummbl-dev` |
| **Archive** | ~60 | `hummbl-theory`, `hummbl-papers`, `hummbl-doctrine`, `hummbl-physical-ai`, `hummbl-meta-agent-systems`, `hummbl-wargame`, `hummbl-premortem`, `hummbl-rsi`, `hummbl-strategy`, `hummbl-taxonomy`, `hummbl-transparency`, `hummbl-telemetry`, `hummbl-compass`, `hummbl-ani`, `hummbl-aspi`, `hummbl-benchmarks`, `hummbl-brand`, `hummbl-brainstorm`, `hummbl-bki`, `hummbl-caes`, `hummbl-cca-f`, `hummbl-experimenter`, `hummbl-fractional-bench`, `hummbl-gaas`, `hummbl-huaomp`, `hummbl-jepa`, `hummbl-kernel-forge`, `hummbl-learning-mechanics`, `hummbl-living-ledgers`, `hummbl-media`, `hummbl-medical`, `hummbl-mesh`, `hummbl-mtsmu`, `hummbl-paralegal`, `hummbl-primitives`, `hummbl-production`, `hummbl-professor`, `hummbl-reasoning-bench`, `hummbl-rubric-templates`, `hummbl-skills`, `hummbl-spacetime`, `hummbl-utf`, `hummbl-worstcase`, `hummbl-base120-protocol`, `hummbl-basen`, `hummbl-assurance`, `hummbl-cscs`, `hummbl-legal`, `hummbl-gitea-control-plane`, `agent-governance-demo`, `governed-compression`, `mission-mode`, `bif`, `lejepa`, `randy`, `ST3GG`, `coaching`, `fractional-bench`, `nsca`, `PSI`, `strategos`, `vault` |
| **Merge into other repo** | ~10 | `autoresearch` family → `hummbl-research`; `hummbl-arbiter` → `arbiter`; `hummbl-agent` → `hummbl-governance` (v0.9.0 adapters); `mcp-server` TypeScript → separate but linked |
| **Product repos (not IaC)** | ~5 | `foundermode-app`, `ownward-app`, `ownward`, `jsr-app`, `jsr-extension` |
| **Upstream forks** | ~5 | `vllm`, `Real-Time-Voice-Cloning`, `markitdown`, `rich`, `paramiko` |

**Archive process:**
1. Add `ARCHIVED.md` to repo root with reason + pointer to successor
2. Update `hummbl-dev/README.md` repo inventory
3. Make repo read-only in Gitea/GitHub settings
4. No deletion — preserves git history and bus receipts

---

## 9. Definition of Done (Per Extraction)

A package is "shipped" when:

- [ ] `pyproject.toml` with stdlib-only `dependencies` (optional extras allowed)
- [ ] `README.md` with: what it is, install instructions, quick example, test command
- [ ] `tests/` with ≥80% coverage
- [ ] CI on GitHub Actions: 3 OS × 3 Python (3.11, 3.12, 3.13, 3.14)
- [ ] `ARCHITECTURE.md` explaining design decisions and dependency boundaries
- [ ] If MCP server: JSON-RPC schema + `hummbl-<name>-mcp` CLI entry point
- [ ] If CLI: `hummbl-<name>` entry point with `--help`
- [ ] No hardcoded operator paths (`C:/Users/Owner`, `/Users/others`, `anvil.tail0ff7b3.ts.net`)
- [ ] All secrets via env vars with documented defaults
- [ ] Bus receipt posted: `PROPOSAL` → `ADR` → `ship` with Conventional Commits
- [ ] Version tagged: `v0.1.0` with release notes
- [ ] `founder-mode` updated to consume the package instead of local code

---

## 10. Immediate Next Steps

### This Week
1. **Create `hummbl-bus` v0.1.0 branch** — finish drift reconciliation from founder-mode
2. **Create `hummbl-clp` v0.1.0 branch** — extract core 13 files, document founder-mode coupling
3. **Archive 10 lowest-value repos** — add `ARCHIVED.md`, update inventory

### This Month
4. **Publish `hummbl-bus` v0.1.0 to PyPI**
5. **Publish `hummbl-clp` v0.1.0 to PyPI**
6. **Update `founder-mode` to consume both via `pip install`** instead of local imports
7. **Archive 30 more repos** — batch operation with bus receipts

### This Quarter
8. **Ship `hummbl-contracts` v0.1.0** — schema validator runtime
9. **Ship `evidence-gate` v0.1.0** — source-verification primitive
10. **Archive remaining 20 repos**
11. **Establish `hummbl-fleet` meta-CI** — weekly integration smoke test across all active packages

---

*Generated with [Devin](https://cli.devin.ai/docs)*
*Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>*
