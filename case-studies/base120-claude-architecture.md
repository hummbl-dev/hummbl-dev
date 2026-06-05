# Case Study: Building the HUMMBL Base120 Structured-Reasoning Surface

**Public evidence from the Base120 SDK, MCP server, and HUMMBL ecosystem repos**

---

**Client:** HUMMBL, LLC (Internal Product Development)  
**Architect:** Reuben Bowlby, Founder & Principal Architect  
**Timeline:** 2024–2026 (ongoing public surface; snapshot updated June 2026)  
**Public stack surface:** Python SDK (`base120`) · MCP server (`@hummbl/mcp-server`) · GitHub · HUMMBL web/docs surfaces

---

## Evidence Posture

This case study intentionally separates what is directly visible on public HUMMBL surfaces from broader architectural interpretation.

**Publicly verifiable in linked repos as of June 2026**

- The [`base120`](https://github.com/hummbl-dev/base120) repo documents 120 named mental models across 6 transformation families.
- The `base120` Python package is documented as stdlib-only with `dependencies = []` in `pyproject.toml`.
- The [`mcp-server`](https://github.com/hummbl-dev/mcp-server) repo documents MCP access to Base120 models and includes Claude Desktop configuration examples.
- Public HUMMBL repos position `base120`, `mcp-server`, and `hummbl-governance` as related parts of the same ecosystem.

**Interpretive or synthesized context**

- Internal usage patterns, operator workflow, and the broader architectural thesis behind Base120.
- Exact production topology for HUMMBL web/app surfaces unless explicitly documented in the linked public repos.
- Operational claims that may evolve faster than a static case study.

---

## The Challenge

AI-assisted reasoning becomes difficult to trust when the process is implicit. A team may get useful outputs, but still lack:

- a stable vocabulary for repeatable reasoning
- explicit transformation steps that can be reviewed later
- delivery surfaces that make the framework usable inside real workflows rather than as a static document

HUMMBL's public Base120 surface addresses that gap by turning a mental-model corpus into an SDK and tool-access layer that can be invoked programmatically.

---

## The Solution

### Framework Structure

The public Base120 surface documents **120 named mental models** organized across six transformation families:

- **Perspective (P)** for framing and viewpoint shifts
- **Inversion (IN)** for counterfactual and failure-oriented analysis
- **Composition (CO)** for synthesis and system construction
- **Decomposition (DE)** for breaking problems into inspectable parts
- **Recursion (RE)** for iteration, self-reference, and feedback patterns
- **Systems (SY)** for dynamics, emergence, control, and resilience

The repo positions these models as a canonical registry plus a Python SDK that makes them addressable by code, CLI, and MCP tooling.

### Public Delivery Surfaces

The current public delivery pattern is visible across two repos:

- [`base120`](https://github.com/hummbl-dev/base120): authoritative registry plus Python SDK
- [`mcp-server`](https://github.com/hummbl-dev/mcp-server): TypeScript MCP server for serving Base120 models to MCP-compatible clients

The public docs support three practical access modes:

- direct registry access from the canonical files in the `base120` repo
- Python SDK access via the `base120` package and CLI
- Claude/Desktop-style tool access via MCP server configuration

### Ecosystem Relationship

The public HUMMBL repo network presents Base120 as part of a larger governed-agent architecture rather than a standalone inspiration deck. In particular:

- `base120` supplies the reasoning substrate
- `mcp-server` exposes that substrate as tools/resources/prompts
- `hummbl-governance` provides adjacent control-plane primitives for safety and coordination

That relationship is publicly documented even where the full internal production topology is not.

---

## Results

### Public Reference Surface

As of the current public snapshot:

- the `base120` repo describes itself as the authoritative source for the Base120 registry and the current Python v2 SDK
- the package metadata shows `version = "2.0.0"` and `dependencies = []`
- the repo README documents 120 models across 6 transformation families

### MCP Availability

The `mcp-server` public repo documents:

- npm distribution for `@hummbl/mcp-server`
- Claude Desktop configuration examples
- tool, prompt, and resource access patterns for working with Base120 through MCP

### Practical Engineering Outcome

The public evidence supports a narrower but defensible claim:

**Base120 is not just a written framework. It is exposed as a maintained SDK and MCP-accessible tool surface that can be integrated into real workflows.**

That is a stronger and more supportable claim than broad assertions about private runtime topology or undocumented production metrics.

---

## Technical Stack Summary

| Layer | Publicly documented surface |
|---|---|
| Canonical model registry | `base120` repo |
| Python SDK | `base120` package |
| CLI | `base120` entry point |
| MCP access | `base120-mcp` entry point and `@hummbl/mcp-server` |
| Tool protocol | Model Context Protocol (MCP) |
| Ecosystem context | HUMMBL public GitHub repos |

---

## Key Takeaways

**Structured reasoning becomes more credible when it is packaged as an interface, not only a philosophy.** The Base120 public surface shows a registry, an SDK, and MCP delivery paths.

**Public repo evidence is strongest at the package and interface layer.** It clearly supports model counts, transformation families, package metadata, and MCP configuration patterns.

**Architecture claims should stay inside what the public repos can prove.** Internal workflows, broader production topology, and operator usage patterns may still matter, but they should be labeled as synthesis unless separately evidenced.

---

## About HUMMBL

HUMMBL, LLC develops governed AI infrastructure, structured reasoning tools, and adjacent public research surfaces. Base120 represents the cognitive/reasoning layer of that public ecosystem.

**Website:** [hummbl.io](https://hummbl.io)  
**Founded by:** Reuben Bowlby  
**Focus:** Structured Reasoning · Agent Governance · MCP Tooling

---

*Snapshot note: this case study reflects publicly inspectable repo/package surfaces reviewed in June 2026. Counts, versions, and interfaces may evolve after publication.*
