# Governed Agent Infrastructure Discovery and Inversion

**Date:** 2026-07-18  
**Status:** Discovery receipt and candidate interpretation  
**Decision posture:** Preserve; do not adopt, standardize, or activate new workstreams yet  
**Authority:** Reuben Bowlby remains the sole OWNER and final decision authority

## Purpose

Preserve three independently discovered technical sources and the subsequent synthesis and HUMMBL Base120 Inversion review without converting general exploration into unsupported implementation commitments.

The sources are:

1. `embedded-boston/awesome-embedded-systems`
2. ClickHouse and its current agent, MCP, observability, and retrieval ecosystem
3. The GitHub Scala ecosystem, especially `lampepfl/tacit`

This document distinguishes:

- source-native observations;
- HUMMBL-adjacent interpretations;
- speculative composition;
- inversion findings;
- evidence required before activation.

## Executive decision

The three sources may illustrate a candidate lifecycle model:

```text
Authority before action
→ bounded and recoverable execution
→ attributable evidence and analysis after action
```

That model is coherent but not established as a natural or uniquely useful grouping. It may be analyst-imposed pattern completion based on existing HUMMBL governance concepts.

Therefore:

- preserve the sources separately;
- preserve the cross-domain interpretation as a hypothesis;
- open no implementation or migration commitment from this document;
- require live operational demand before any pilot, benchmark, inventory, or language/toolchain adoption;
- treat existing HUMMBL doctrine as reinforced by analogy, not newly validated.

---

## Source 1: embedded systems discovery list

### Intake verdict

Preserve as a discovery source, not as a canonical or current embedded-systems reference.

| Dimension | Assessment |
|---|---|
| Scope | Useful introductory taxonomy spanning RTOSes, protocols, serialization, testing, languages, Embedded Linux, tools, books, and courses |
| Currency | Low; default-branch activity is stale relative to the 2026 ecosystem |
| Maintenance | Weak; multiple current pull requests remain unresolved |
| Accuracy risk | Material; obsolete entries, uneven descriptions, dead projects, and broken links are documented risks |
| Licensing | README declares CC0, but no standalone `LICENSE` file was identified; linked projects retain their own licenses |
| HUMMBL relevance | Medium as bounded source material; low as authority |

### Strongest signals

- Hubris: memory isolation and message-passing architecture
- Mender and SWUpdate: recoverable edge-device deployment
- FreeRTOS and RTEMS: deterministic execution
- embedded testing and hardware-in-the-loop practices
- SiliconRig as a candidate hardware-in-the-loop reference
- Nancy Leveson's *Engineering a Safer World* for systems safety and governance

### Important omissions

The list does not adequately represent contemporary areas such as:

- Zephyr
- NuttX
- Eclipse ThreadX
- ESP-IDF
- modern RISC-V ecosystems
- Matter and Thread
- LoRaWAN
- TinyML
- secure boot
- SBOMs
- fuzzing
- observability
- contemporary embedded Rust

### Bounded disposition

Do not fork or contribute merely because the list is useful. Read, cite selectively, and revisit only when a live physical, wearable, sensor, robotic, or edge-system decision requires a current inventory.

---

## Source 2: ClickHouse ecosystem

### Intake verdict

ClickHouse is a credible candidate analytical and observability technology. It is not a replacement for canonical Git/Gitea evidence, PostgreSQL/Supabase transactional state, or object-storage receipts.

### Current strategic signals

The ecosystem includes:

- the Apache-2.0 ClickHouse analytical database;
- an Agentic Data Stack combining ClickHouse, MCP, LibreChat, and Langfuse;
- a narrow read-only ClickHouse MCP surface for discovery, schema inspection, and `SELECT`;
- a Beta Agent Builder with code execution, web search, skills, MCP, vision, memory, and subagents;
- ClickStack, an OpenTelemetry-native observability platform;
- a ClickStack MCP surface capable of investigations and some mutations;
- JSON ingestion, Kafka integration, Iceberg interoperability, and HNSW vector search.

### Potential fit

| Lane | Candidate fit | Required boundary |
|---|---|---|
| Agent runs, tool calls, latency, cost, and failures | Strong | Derived analytics only |
| OpenTelemetry across Anvil, Huxley, and agents | Strong | Redact prompts, tokens, secrets, and personal data |
| Canonical governance evidence | Analytical mirror only | Git/Gitea remains authoritative |
| HUMMBL bibliography retrieval | Candidate benchmark | Compare provenance, recall, cost, memory, and operational burden |
| Voice Chief of Staff observability | Potentially useful | Not primary user state or transactional memory |
| Per-user memory | Weak-to-partial | Keep governed transactional source of truth elsewhere |

### Governance intelligence

ClickHouse's AI contribution policy is relevant comparative evidence because it permits agentic research and AI-assisted work while retaining human responsibility, reproducibility, validation, and reviewer-load constraints.

### Risks

- instrumentation and dependency gravity;
- dashboards becoming epistemically dominant over canonical evidence;
- raw prompt or personal-data overcollection;
- derived fields being mistaken for observed facts;
- retention and schema changes altering historical interpretation;
- additional operational, backup, security, and access-control burden;
- vector-index memory and filtered-ANN tradeoffs;
- Beta maturity in agent-oriented surfaces.

### Activation trigger

Do not pilot ClickHouse until the current observability stack demonstrably fails to answer a material operational question under an explicit burden ceiling.

Examples include inability to reconstruct:

- model and tool failure rates;
- cross-node incidents;
- policy-denial patterns;
- agent latency and cost;
- source-linked historical comparisons.

Any pilot must compare ClickHouse against simpler alternatives, preserve source pointers, enforce read-only analytical identities, and test whether reviewers distinguish observed, derived, inferred, and missing values.

---

## Source 3: Scala ecosystem and TACIT

### Intake verdict

Do not adopt Scala as a general HUMMBL or Founder Mode implementation language. Preserve TACIT as a candidate experimental governance primitive.

### TACIT's core idea

TACIT, "Tracked Agent Capabilities In Types," replaces direct agent tool calls with agent-generated Scala 3 programs. Capture checking and runtime mediation aim to ensure that generated programs:

- cannot forge capabilities;
- cannot exercise effects beyond granted permissions;
- cannot allow scoped capabilities to escape;
- can preserve purity for selected computations;
- can restrict classified values from leaking through ordinary output.

The architecture combines typed scopes with runtime controls such as allowlists, filesystem roots, classified-path handling, and timeouts.

### Most important assumption

The agent's ordinary shell, filesystem, and network tools must be disabled or strictly mediated. Otherwise the agent can bypass the capability harness.

This assumption is not incidental. It is central to the safety claim and may conflict with the flexibility expected from general-purpose agents.

### Potential HUMMBL relevance

TACIT suggests a stronger governance question:

> Which authorization rules can move from prompt-level convention or runtime policy into mechanically enforced capability constraints?

This may complement:

- tool authorization;
- classified-data controls;
- sandboxing;
- receipt generation;
- Safe Handoff;
- explicit authority delegation.

### Risks

- Scala/JVM and build-toolchain state;
- learning and reviewer burden;
- immature capture-checking and research assumptions;
- trusted-computing-base complexity;
- alternate-tool bypass paths;
- safety gains produced partly by removing task capability;
- uncertain transferability outside Scala 3.

### Activation trigger

Do not run a TACIT evaluation until a demonstrated authority or tool-bypass failure exists that present controls cannot adequately prevent, or until a bounded research question justifies the toolchain cost.

A valid evaluation must compare equal or acceptably comparable:

- task completion;
- task breadth;
- latency;
- usability;
- recovery burden;
- reviewer workload;
- unauthorized-effect prevention.

The key comparison is not whether TACIT is safer in isolation. It is whether it produces a better safety frontier at comparable useful capability.

---

## Candidate cross-domain synthesis

A plausible interpretation assigns the three sources different governance concerns:

| Source | Candidate concern |
|---|---|
| TACIT | Authority and effect constraints before execution |
| Embedded systems | Deterministic, local, safe, and recoverable execution |
| ClickHouse | Continuous and retrospective operational analysis |

A speculative composed flow is:

```text
Agent intention
→ delegated capability
→ runtime and gateway policy
→ edge or software execution
→ attributable receipt
→ canonical evidence storage
→ sanitized telemetry
→ analytical reconstruction
```

### Compatibility hypothesis

At a conceptual level, no fundamental contradiction prevents:

- typed capability decisions from emitting structured telemetry;
- physical systems from enforcing local safety limits;
- edge systems from sending sanitized operational events;
- analytical systems from retaining receipt hashes and source pointers.

This is generic interoperability, not proof of special architectural compatibility.

### Known incompatibilities

- ClickHouse is unsuitable as the authority or transactional source of truth.
- TACIT-like safety is undermined by unrestricted parallel shell, network, or filesystem paths.
- general Scala adoption adds unjustified fleet and toolchain complexity absent unique value.
- cloud-agent assumptions do not transfer directly to constrained, offline, real-time, or physically consequential systems.
- extensive telemetry conflicts with privacy and data minimization.
- static capability safety does not prove that a granted action is appropriate, physically safe, correctly implemented, or outcome-effective.
- additional layers create translation, ordering, identity, provenance, schema, and partial-failure risks.

---

## HUMMBL Base120 Inversion review

### Inverted thesis

The apparent commonality may be invented.

These sources were found through general exploration, not selected as a coherent sample. The synthesis may have converted accidental adjacency into architectural significance because HUMMBL governance, agents, effects, receipts, and observability are dominant interpretive attractors.

### Primary inversion findings

#### 1. "Control over effects" may be too broad

The phrase can classify almost any technical system and therefore may not distinguish this group meaningfully.

#### 2. The synthesis may be circular

Existing HUMMBL categories were used to classify the technologies, and the resulting fit was then treated as evidence reinforcing the categories.

#### 3. Compatibility was overstated

Event emission and layered diagrams show conceptual composability, not operational compatibility, integration feasibility, or net benefit.

#### 4. The before-during-after mapping compresses source fidelity

TACIT, embedded systems, and ClickHouse each span multiple lifecycle stages. Assigning one phase to each may create false completeness.

#### 5. Priorities were assigned before a live problem

General exploration was converted into P1 and P2 work without an established operational failure, user requirement, product decision, or research commitment.

#### 6. Investigation itself has material cost

Even bounded pilots create toolchain state, schemas, retention policy, privacy review, tests, dashboards, operational ownership, and follow-up obligations.

#### 7. Technical novelty may distract from observed risks

Current dominant risks may remain ownership ambiguity, stale branches, conflicting agents, incomplete receipts, configuration drift, missing evidence, publication overclaiming, and founder attention fragmentation.

#### 8. More governance layers can increase uncertainty

Every new layer can drift, misrepresent state, fail partially, obscure responsibility, or complicate reconstruction.

#### 9. ClickHouse could worsen epistemics

A polished analytical projection may become easier to use than canonical evidence and thereby displace it in practice.

#### 10. TACIT may achieve safety by narrowing usefulness

Removing ordinary tools and forcing mediated generated code may change the agent capability being compared. Safety claims must be normalized for useful task capability.

#### 11. Embedded relevance may be speculative

Wearables, robotics, sensors, and embodied agents are plausible horizons but do not establish present decision relevance.

#### 12. The shared principle is existing doctrine

The sources may reinforce existing HUMMBL doctrine by analogy; they do not yet provide independent validation or a newly discovered principle.

---

## Falsification plan

The inversion critique would weaken if the following evidence emerged.

### Cross-source synthesis

Independent reviewers, without seeing this framing, derive substantially the same authority-execution-observation relationship and show that it improves a live decision.

### ClickHouse

A bounded comparison demonstrates that ClickHouse answers material observability or retrieval questions significantly better than simpler alternatives while preserving privacy, provenance, source distinction, and an acceptable operational burden.

### TACIT

A controlled evaluation demonstrates comparable useful task capability, materially fewer unauthorized effects, realistic bypass resistance, manageable toolchain burden, and transferable design principles.

### Embedded systems

A live product or research requirement creates an actual need for constrained devices, sensing, actuation, deterministic timing, offline resilience, OTA recovery, or hardware-in-the-loop validation.

---

## Status classification

| Item | Status |
|---|---|
| Embedded systems list | Discovery source |
| ClickHouse | Candidate analytical technology |
| TACIT | Candidate research primitive |
| Authority-execution-observation model | Hypothesized cross-domain interpretation |
| Combined architecture | Speculative composition |
| Technology pilots | Not authorized by this document |
| Shared governance principle | Existing doctrine reinforced by analogy |

## Activation policy

No installation, migration, benchmark, inventory project, dependency adoption, or new standing workstream is authorized by this receipt alone.

Activation requires:

1. a named live problem or decision;
2. evidence that current mechanisms are insufficient;
3. a bounded question and success/failure criteria;
4. a burden ceiling covering time, compute, privacy, maintenance, and fleet state;
5. explicit OWNER approval;
6. a falsification path and stop condition.

## Final recommendation

Do less and preserve carefully.

Keep the three discoveries separate. Retain the proposed commonality as a candidate interpretation. Promote no technology and create no ongoing research program until a live system problem selects a mechanism.

The most important meta-finding is:

> The discovery process can rapidly convert unrelated technical novelty into coherent HUMMBL architecture. That capability is useful, but without demand gates it can produce elegant portfolio expansion faster than externally falsifiable value.
