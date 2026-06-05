# HUMMBL Dependency Tiers

> **Audience note**: This is a draft planning proposal. It is not adopted org-wide policy and should not be treated as current source-of-truth governance without explicit repo-local adoption.

> **stdlib-first does not mean stdlib-only everywhere.** It means *safety substrate is stdlib-only*, and every dependency is a deliberate, auditable choice.

**Status:** DRAFT — 2026-06-02
**Proposes replacing:** `founder-mode/.claude/rules/stdlib-only.md` if later adopted through the appropriate repo-local governance path

---

## 1. Philosophy

HUMMBL's bias toward stdlib-only runtime dependencies is not dogma. It is a **survivability constraint** for control-plane primitives that must function when everything else is broken.

- **Kill switch must work when PyPI is unreachable.**
- **Circuit breaker must work when `pip install` fails.**
- **Delegation token must work in air-gapped environments.**

But not every HUMMBL repo is a safety primitive. A consumer voice app, a TypeScript MCP server, or a LangGraph adapter can and should use the best tools available. The question is: **which tier does this repo belong to, and how do we communicate that?**

---

## 2. The Five Tiers

```
Tier 0: ABSOLUTE STDLIB ONLY
Tier 1: STDLIB CORE + OPTIONAL EXTRAS
Tier 2: ADMITTED DEPENDENCIES (gated)
Tier 3: MANAGED DEPENDENCIES (version-pinned, audited)
Tier 4: UNRESTRICTED (product/application layer)
```

### Tier 0: Absolute Stdlib Only
**Rule:** Zero third-party runtime dependencies. No exceptions. No extras. No optional imports.

**Why:** These are the primitives that must survive network partition, supply-chain compromise, and air-gapped deployment. If you can't pip install anything, these still work.

**Repos in this tier:**
| Repo | Language | Runtime Deps | Why Tier 0 |
|---|---|---|---|
| `hummbl-governance` | Python | 0 | Kill switch, circuit breaker, cost governor, delegation tokens |
| `hummbl-bus` | Python | 0 | Coordination bus — must work when everything else is down |
| `hummbl-contracts` | Python | 0 | Schema validator — must validate without external packages |
| `hummbl-trace` | Python | 0 | Behavioral trace — audit primitive |
| `crab` | Python | 0 | Shell safety guard |
| `arbiter` | Python | 0 (core) | Code quality scoring core; analyzers are Tier 1 extras |
| `base120` | Python | 0 | Mental models SDK |

**Indicator:** `pyproject.toml` has `dependencies = []`. README has badge: `[![Runtime Deps](https://img.shields.io/badge/runtime%20deps-zero-brightgreen)]()`.

**How to graduate OUT of Tier 0:** You don't. If a repo needs a third-party dep, it was never Tier 0. Re-evaluate the architecture.

---

### Tier 1: Stdlib Core + Optional Extras
**Rule:** Core functionality is stdlib-only. Optional extras provide convenience, performance, or integrations. The package installs and is useful without any extras.

**Why:** The safety substrate works without extras, but developers can opt into richer functionality.

**Repos in this tier:**
| Repo | Core | Optional Extras |
|---|---|---|
| `arbiter` | `pip install arbiter` — stdlib-only scoring | `arbiter[analyzers]` — ruff, radon, vulture, bandit |
| `hummbl-clp` | `pip install hummbl-clp` — ledger + BM25 index | `hummbl-clp[server]` — FastAPI/Open Brain server |
| `hummbl-recall` | `pip install hummbl-recall` — spaced retrieval core | `hummbl-recall[server]` — scheduling daemon |
| `hummbl-crucible` | `pip install hummbl-crucible` — trust scoring core | `hummbl-crucible[web]` — dashboard/visualization |

**Indicator:** `pyproject.toml` has `dependencies = []` and `[project.optional-dependencies]` with documented extras. README clearly shows install variants.

**How to graduate IN from Tier 0:** Add optional extras that do not touch core safety primitives. The core remains stdlib-only.

**How to graduate OUT to Tier 2:** Core functionality starts requiring third-party deps. At that point, the repo needs a formal admission packet (see Tier 2).

---

### Tier 2: Admitted Dependencies (Gated)
**Rule:** Core functionality requires one or more third-party packages. Each admission requires a written packet, peer review, and operator ratification.

**Admission packet must answer:**
1. Why can stdlib not provide this functionality?
2. What is the engineering cost of replacing this dependency with stdlib?
3. What is the license? Is it permissive (Apache-2.0, MIT, BSD)?
4. What is the CVE history of this package and its transitive deps?
5. What is the upper-bound pin strategy?
6. Is the dependency constrained to an optional extra or isolated subdirectory?
7. What is the rollback plan if this dependency is compromised or abandoned?

**Current Tier 2 admissions:**
| Package | Admitted | License | Rationale | Constrained To |
|---|---|---|---|---|
| `c2pa-python` | 2026-05-01 | Apache-2.0 / MIT | C2PA manifest read/write — ~6-12 months to replace with stdlib | `[c2pa-mcp]` extra only |
| `sigstore-python` | 2026-05-01 | Apache-2.0 | Sigstore Rekor client — ~4-6 weeks to replace with stdlib | `[c2pa-mcp]` extra only |

**Repos in this tier:**
| Repo | Language | Key Deps | Why Tier 2 |
|---|---|---|---|
| `mcp-server` | TypeScript | `@modelcontextprotocol/sdk` | MCP protocol reference implementation |
| `mcp-server` | TypeScript | `@modelcontextprotocol/sdk` | MCP protocol reference implementation |
| `NemoClaw` | TypeScript/Docker | `k3s`, `docker`, `@openshell/sdk` | NVIDIA deployment stack; not a HUMMBL-authored safety primitive |
| `hummbl-jepa` | Python | `torch`, `numpy` | JEPA architecture requires tensor operations |
| `hummbl-medical` | Python | `pydicom`, `monai` | Medical AI requires domain-specific libraries |

**Indicator:** `pyproject.toml` has deps. README has an "Admission" section listing every third-party dep with rationale. A `docs/ADMISSIONS.md` file exists with full packets.

**How to graduate IN from Tier 1:** File admission packet → Codex peer review → operator GO → ratify in cognitive ledger → add to `docs/ADMISSIONS.md`.

**How to graduate OUT to Tier 3:** Remove the admission process. The repo has proven its dependency choices are stable and low-risk. Requires 6 months of production use with zero CVEs in admitted deps.

---

### Tier 3: Managed Dependencies (Version-Pinned, Audited)
**Rule:** Dependencies are allowed, version-pinned, and subject to periodic audit. No admission packet required, but deps must be documented with `pip-audit` or `bandit` scan results.

**Why:** These repos are product-facing, integration-oriented, or use domain-specific libraries where stdlib is impractical. The risk is managed through tooling, not avoidance.

**Repos in this tier:**
| Repo | Language | Key Deps | Why Tier 3 |
|---|---|---|---|
| `founder-mode` | Python | `pytest`, `coverage`, `anyio`, `httpx` | Integration testbed — must integrate with real services |
| `foundermode-app` | Python | `fastapi`, `openai`, `firebase-admin` | Consumer app — needs HTTP, AI, database |
| `ownward-app` | Python | `fastapi`, `openai`, `firebase-admin` | Same as above |
| `hummbl-agent` | TypeScript | `@anthropic-ai/sdk`, `zod` | Agent SDK wrapper |
| `hummbl-langgraph` | Python | `langgraph`, `langchain` | Ecosystem adapter |
| `hummbl-crewai` | Python | `crewai` | Ecosystem adapter |
| `vllm` | Python | `torch`, `ray`, `transformers` | Inference engine (upstream fork) |
| `markitdown` | Python/JS | `markdown-it`, `pandoc` | Document conversion (upstream fork) |
| `mission-mode` | Python | `httpx`, `pydantic`, `rich` | Personal mission harness — not a shared primitive |

**Indicator:** `pyproject.toml` has pinned deps with upper bounds. CI runs `pip-audit` weekly. README documents all runtime deps and their purposes.

**How to graduate IN from Tier 2:** 6 months of zero CVEs in admitted deps + operator approval.

---

### Tier 4: Unrestricted (Product/Application Layer)
**Rule:** Dependencies are unrestricted. These are end-user products, not infrastructure libraries. They can use whatever they need.

**Why:** A founder's morning coaching app is not a safety primitive. It should use the best tools available.

**Repos in this tier:**
| Repo | Language | Key Deps | Why Tier 4 |
|---|---|---|---|
| `foundermode-app` (consumer) | Swift/Python | `OpenAI`, `Firebase`, `Cloud Run` | Consumer product |
| `ownward` (consumer) | Swift/Python | Same | Consumer product rebrand |
| `jsr-app` | TypeScript | React, Next.js | Web frontend |

**Indicator:** These repos have `LICENSE` files that may be proprietary (not Apache-2.0). They are not published to PyPI as libraries.

**How to graduate IN:** You don't. Tier 4 repos should never be depended on by Tier 0-3 repos.

---

## 3. Cross-Language Equivalents

The "stdlib-first" principle applies across languages, but the "stdlib" definition changes:

| Language | Tier 0 = Stdlib Only | Tier 1 = Optional Extras | Tier 2+ = Admitted/Managed |
|---|---|---|---|
| **Python** | `dependencies = []` in `pyproject.toml` | `dependencies = []` + `[project.optional-dependencies]` | `dependencies = ["pkg>=X,<Y"]` |
| **TypeScript** | Zero `dependencies` in `package.json`; `devDependencies` only | Same + optional peer deps | `dependencies` in `package.json` |
| **Rust** | `Cargo.toml` with only `std` features | Same + optional features | External crates with `Cargo.lock` |
| **Go** | Standard library only | Same + optional modules | External modules with `go.sum` |
| **Docker** | `FROM scratch` or `FROM distroless` | Multi-stage builds | Standard base images |

---

## 4. How This Is Indicated

Every HUMMBL repo MUST have one of these indicators:

### In `pyproject.toml` (Python)
```toml
[project]
# Tier 0
# dependencies = []
# Tier 1
# dependencies = []
# [project.optional-dependencies]
# server = ["fastapi>=0.100"]
# Tier 2
# dependencies = ["c2pa-python>=0.32,<0.33"]
# Tier 3
# dependencies = ["httpx>=0.27,<0.28", "pydantic>=2.0,<3.0"]
```

### In `README.md`
Tier 0 repos MUST have:
```markdown
[![Runtime Deps](https://img.shields.io/badge/runtime%20deps-zero-brightgreen)]()
```

Tier 1 repos MUST have:
```markdown
[![Core Deps](https://img.shields.io/badge/core%20deps-zero-brightgreen)]()
[![Optional Extras](https://img.shields.io/badge/optional-extras-blue)]()
```

Tier 2 repos MUST have:
```markdown
## Dependencies
This package requires third-party dependencies. Each admission is documented in [docs/ADMISSIONS.md](docs/ADMISSIONS.md).
```

### In `docs/ADMISSIONS.md` (Tier 2 only)
```markdown
# Dependency Admissions

| Package | Version | Admitted | License | Rationale |
|---|---|---|---|---|
| c2pa-python | >=0.32,<0.33 | 2026-05-01 | Apache-2.0 | C2PA manifest handling |
```

### In repo directory (`hummbl-dev/README.md`)
The master repo inventory MUST include a "Tier" column.

---

## 5. What To Do About It

### If you are creating a NEW repo

1. **Decide the tier BEFORE writing code.** The tier is an architectural decision, not an afterthought.
2. **Default to Tier 0.** You can always relax. It's painful to tighten later.
3. **Document the tier in the README in the first commit.**
4. **If Tier 2+:** File an admission packet in the first PR, before the dependency is imported anywhere.

### If you are extracting a module from `founder-mode`

1. Check the source module's dependency surface in `founder-mode/pyproject.toml`.
2. If the source module imports anything from `integrations/` (e.g., `github_adapter`, `google_calendar_adapter`), the extracted repo is likely **Tier 3**.
3. If the source module imports only from `services/` and uses stdlib, the extracted repo is likely **Tier 0 or 1**.
4. If the source module imports from both `services/` and `integrations/`, split it: stdlib-only core goes to Tier 0, adapter goes to Tier 3.

### If a repo wants to upgrade its tier (add dependencies)

| From → To | Process |
|---|---|
| Tier 0 → Tier 1 | No process. Add `[project.optional-dependencies]`. Core stays `dependencies = []`. |
| Tier 1 → Tier 2 | File admission packet → Codex peer review → operator GO → add to `docs/ADMISSIONS.md`. |
| Tier 2 → Tier 3 | 6 months zero CVEs + operator approval. Remove admission requirement, keep audit scans. |
| Any → Tier 4 | Operator decision. Usually means the repo is no longer a shared library. |

### If a repo wants to downgrade its tier (remove dependencies)

| From → To | Process |
|---|---|
| Tier 3 → Tier 2 | Add admission process retroactively. Document all deps. |
| Tier 3 → Tier 1 | Remove core deps. Move to extras. Verify core works without extras. |
| Tier 2 → Tier 1 | Remove admitted deps or move to extras. Verify core works without them. |
| Tier 1 → Tier 0 | Remove all extras. Verify `dependencies = []`. |

### If `founder-mode` imports a new library

`founder-mode` is the **integration testbed**. It is Tier 3. But it has a special rule:

> **Any module in `founder-mode/services/` or `founder-mode/integrations/` that is a candidate for extraction MUST be written as if it were Tier 0.**

This means:
- Write the module with stdlib-only imports first.
- Add third-party deps only behind feature flags or in `integrations/`.
- When extracting, the stdlib-only core moves to its own Tier 0 package.
- The integration adapters stay in `founder-mode` (Tier 3) or move to a Tier 3 package.

---

## 6. Audit Checklist

Every quarter, audit every active repo:

- [ ] Is the tier correctly documented in the README?
- [ ] Does the `pyproject.toml` / `package.json` / `Cargo.toml` match the claimed tier?
- [ ] For Tier 2 repos: Is `docs/ADMISSIONS.md` up to date?
- [ ] For Tier 2-3 repos: Are there CVEs in the dependency tree? (`pip-audit`, `npm audit`, `cargo audit`)
- [ ] For Tier 2-3 repos: Are upper-bound pins still valid?
- [ ] Are there any Tier 4 repos being imported by Tier 0-2 repos? (Forbidden.)

---

## 7. Current State Audit

Applying this taxonomy to the ~25 active repos:

| Repo | Claimed Tier | Actual Tier | Gap |
|---|---|---|---|
| `hummbl-governance` | Tier 0 | ✅ Tier 0 | None |
| `arbiter` | Tier 0 (core) | ✅ Tier 1 | None; extras documented |
| `base120` | Tier 0 | ✅ Tier 0 | None |
| `crab` | — | ✅ Tier 0 | Needs README badge |
| `hummbl-bus` | — | ⚠️ In extraction | Needs tier decision before publish |
| `hummbl-clp` | — | ⚠️ In extraction | Needs tier decision before publish |
| `hummbl-contracts` | — | ⚠️ Schemas only | Tier 0 if validator is stdlib-only |
| `evidence-gate` | — | ⚠️ Repo exists | Tier 2; needs admission packet |
| `hummbl-crucible` | — | ⚠️ Stub | Decide: Tier 1 (core) or Tier 3 (dashboard)? |
| `hummbl-recall` | — | ⚠️ Designed | Likely Tier 1 (core + server extra) |
| `hummbl-intent` | — | ⚠️ 46 tests | Likely Tier 0 or 1 |
| `hummbl-trace` | — | ⚠️ Planned | Tier 0 |
| `hummbl-library` | — | ⚠️ Stub | Tier 0 or 1 (shared models) |
| `founder-mode` | Tier 3 | ✅ Tier 3 | None |
| `foundermode-app` | — | ✅ Tier 4 | None |
| `ownward-app` | — | ✅ Tier 4 | None |
| `mission-mode` | — | ✅ Tier 3 | None |
| `NemoClaw` | — | ✅ Tier 2 | NVIDIA stack; admission by origin |
| `mcp-server` (TS) | — | ✅ Tier 2 | MCP SDK; admission by origin |
| `hummbl-jepa` | — | ⚠️ Stub | Tier 2 (`torch`, `numpy`) |
| `hummbl-agent` | — | ⚠️ Stub | Tier 3 (agent SDK wrapper) |
| `hummbl-langgraph` | — | ⚠️ Planned | Tier 3 |
| `hummbl-crewai` | — | ⚠️ Planned | Tier 3 |
| `vllm` | — | ✅ Tier 3 | Upstream fork |
| `markitdown` | — | ✅ Tier 3 | Upstream fork |

**Immediate actions:**
1. Add tier badges to repos missing them (`crab`, `hummbl-crucible`, `hummbl-recall`)
2. Decide tier for `hummbl-bus` and `hummbl-clp` **before** publishing to PyPI
3. File admission packet for `evidence-gate` before importing `c2pa-python`
4. Split `hummbl-crucible` into `hummbl-crucible` (Tier 1, core) and `hummbl-crucible-web` (Tier 3, dashboard)

---

*Generated with [Devin](https://cli.devin.ai/docs)*
*Co-Authored-By: Devin <158243242+devin-ai-integration[bot]@users.noreply.github.com>*
