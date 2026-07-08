# Architecture Specimen: OpenOPC

**Status**: specimen (not canon, not code-import approval)
**Date**: 2026-07-06
**Issue**: [hummbl-dev/hummbl-dev#111](https://github.com/hummbl-dev/hummbl-dev/issues/111)

## Source

- Public repo: https://github.com/HKUDS/OpenOPC
- Inspected via GitHub connector on 2026-07-06.
- Current observed package: `opc`, version `0.1.0`, Python `>=3.10`, MIT metadata in `pyproject.toml`.
- OpenOPC positioning: "Personal AI-Native Company" / Self-Built, Self-Run, Self-Grown.

## Disposition

**Monitor + architecture-mine. Do not integrate.**

OpenOPC is relevant because it embodies a role-based agent-company runtime. HUMMBL's work is broader and more governance-heavy. The repo is a useful specimen for runtime design, but should not become a dependency or canonical reference without further audit.

## Why this matters

OpenOPC appears to be an early but substantive implementation of a role-based multi-agent runtime. It overlaps with HUMMBL / Founder Mode / Ownward work at the agent-runtime layer.

## High-signal similarities to HUMMBL work

| OpenOPC primitive | Adjacent HUMMBL / Founder Mode / Ownward concern |
|---|---|
| AI-native company metaphor | Founder/operator agent org and Chief-of-Staff runtime |
| Roles / employees / talent templates | Agent roles, reusable operator lanes, protocol packets |
| Company Mode | Multi-agent governed execution mode |
| Work-item DAG | Governed handoffs, issue/task decomposition, domino routing |
| Phase-as-source-of-truth | Agent work ledger / task state machine / execution receipts |
| Manager review + rework | Peer-agent review, PR gates, no self-approval, AAR loops |
| External agents: Claude Code, Codex, Cursor, OpenCode | Existing multi-agent workflow and agent router candidates |
| Role memory / playbooks | HUMMBL memory, protocol compounding, source packets |
| Office UI / kanban / runtime cockpit | Public trust surface, runtime observability, operator visibility |
| Channels | Voice-first / channel-aware assistant workflows |

## Strongest extractable ideas

1. **Work-item phase machine** — Each agent work item is a stateful object whose phase drives ownership, runnability, kanban column, task status, and verdict. Separates runtime truth from UI presentation.

2. **Hidden report/review work items** — Worker execution can spawn report cards and review cards before final delivery. Useful for auditability and structured handoff receipts.

3. **Role-owned review/rework loops with explicit retry caps** — Avoids infinite agent loops while preserving an internal quality gate.

4. **External-agent broker** — Routes work to native, Codex, Claude Code, Cursor, or OpenCode-like adapters. Relevant to current human-mediated Claude → Codex → synthesis/QC workflow.

5. **Operator observability UI** — Workspace, kanban, agent rollups, comms, and runtime cockpit as UX patterns.

6. **Packageable organizations / talent templates** — Adjacent to protocol packets, source packets, governance kernels, and reusable issue/handoff templates.

## Governance gaps / caution flags

OpenOPC is structurally relevant but does **not** appear to be a governance model by HUMMBL standards.

Cautions:

- Do not import code until license/provenance is checked.
- Do not treat README claims as benchmarked capability.
- Do not run against private HUMMBL repos or credentialed worktrees in first pass.
- Do not run with production GitHub tokens, cloud credentials, SSH keys, browser cookies, wallets, or private user data.
- Default autonomy posture appears more permissive than HUMMBL's desired governance baseline.
- Treat all OpenOPC/HUMMBL term mappings as candidate comparisons, not canonical vocabulary.

## Proposed sandbox evaluation

Run in disposable local/VM environment only:

- throwaway repo
- throwaway API key with spend cap
- no private repos
- no GitHub write token
- no cloud credentials
- no production browser profile
- no real customer/user data

Initial hardening before test:

```yaml
autonomy:
  max_auto_approve_risk: low
  allow_external_agent_auto_approval: false
  allow_native_tool_auto_approval: false
```

Also remove network/media tools such as `curl`, `wget`, `yt-dlp`, `aria2c`, and `ffmpeg` from safe command prefixes for the first test.

## Candidate experiments

1. **Coding micro-task** — Give OpenOPC a small throwaway repo bugfix. Observe plan → implementation → review → final delivery.

2. **Research memo** — Give it a bounded research brief. Assess whether role decomposition improves output or adds overhead.

3. **Agent handoff simulation** — Simulate Claude → Codex → ChatGPT synthesis/QC workflow. Inspect `.opc-comms`, work items, logs, review artifacts, and memory updates.

## Definition of done

- [ ] Capture install/runtime receipt in disposable environment.
- [ ] Record config posture used for sandbox test.
- [ ] Run at least one coding micro-task.
- [ ] Run at least one research/handoff-style task.
- [ ] Preserve artifacts: work-item graph, comms, logs, final output, failures.
- [ ] Compare OpenOPC primitives against HUMMBL governed-agent primitives.
- [ ] Identify reusable concepts vs rejected concepts.
- [ ] Explicitly decide: ignore / monitor / architecture-mining only / prototype adapter.
- [ ] No code import without separate license/provenance gate.

## Non-canon notice

This specimen is a **candidate analysis**. It has not been adopted as HUMMBL canon. No benchmark, performance, or adoption claim is made without evidence. All OpenOPC/HUMMBL term mappings are candidate comparisons, not canonical vocabulary.
