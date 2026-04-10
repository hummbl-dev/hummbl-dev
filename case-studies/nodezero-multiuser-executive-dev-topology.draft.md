---
title: "Shared Infrastructure, Separated Surfaces: Multi-User Mac Configuration for a Developer-Executive Team"
slug: nodezero-multiuser-executive-dev-topology
status: draft
mode: active
created: 2026-04-10
finalized:
repo: N/A (nodezero infrastructure)
pr: N/A
tags: [infrastructure, multi-user, macos, mlx-whisper, tailscale, onboarding, dan-matha]
---

# Case Study: Shared Infrastructure, Separated Surfaces

**Project:** nodezero (Mac Mini M4 Pro) multi-user configuration — Reuben (admin/dev) + Dan Matha (executive/learner)  
**Architect:** Reuben Bowlby, Founder & Principal Architect  
**Timeline:** April 2026 (in progress)  
**Stack:** macOS · launchd · Tailscale · mlx-whisper · ACL/group permissions · Claude Code

---

## Context

nodezero is a Mac Mini M4 Pro running as the team's primary inference host (Ollama :11434, Open Brain :11435, nightly consolidator) and CI self-hosted runner. It currently has a single user account (`nodezero`). Dan Matha, EVP/Brand Ambassador, is onboarding — both as an end-user of HUMMBL tools and as someone learning to sell and use multi-agent systems. The goal is to give Dan a functional, safe working environment on nodezero without exposing Reuben's dev environment or compromising agent operations.

---

## Problem

A single shared user account doesn't scale past one person. The specific pressures:

1. **Security boundary**: Reuben's dev credentials, agent keys, and git configs cannot be accessible to a standard executive user — not because of distrust, but because any accident (mistyped command, accidental `rm`, wrong git push) has blast radius into production agent operations.

2. **Learning environment**: Dan needs a workspace where he can break things without consequence, experiment with Claude Code and the bus tools, and develop technical fluency without a safety net that is actually Reuben's production infrastructure.

3. **Shared outputs**: Some artifacts — governance reports, briefing outputs, Arbiter scores, case studies — need to be readable and runnable by both accounts without manual copying.

4. **Transcription service**: mlx-whisper on the M4 Pro is a planned shared capability (iOS TestFlight integration, agent voice pipeline). Whether it runs as a shared daemon or per-user process is a key architectural decision gating the rest of the setup.

---

## Constraints

- **SIP must remain enabled** — no kernel extensions, no SIP bypass; M4 Pro security model is the foundation
- **No MDM currently** — restrictions must be expressible via standard macOS ACL, group permissions, and `/etc/sudoers.d/`
- **Tailscale ACL must reflect the new topology** — Dan's account on nodezero should have its own Tailscale identity or be explicitly scoped
- **Agent daemons must not be disrupted** — Ollama, Open Brain, the consolidator launchd job, and the bus bridge must keep running through account provisioning
- **Minimal sync complexity** — preference for shared filesystem (one inode, two users) over rsync daemons; add sync only if independent copies are actually required

---

## Architecture Decisions

[TO FILL: populate from handoff document decisions once the other Claude session completes the 12-section spec]

**Known decision axes from planning session (2026-04-10):**

- **Account model**: `reuben` (admin) + `dan` (standard) + shared group `hummbl` owning `/Users/Shared/hummbl/`
- **Shared surface**: `/Users/Shared/hummbl/{outputs,projects,tools}` — ACL-governed, not rsync
- **Transcription topology**: [OPEN — shared daemon vs. per-user process; gated on questions 31–46 from planning doc]
- **Dan's sudo scope**: scoped to specific `launchctl` commands via `/etc/sudoers.d/`, not full sudo
- **Agent caller identity**: [OPEN — whether `/transcribe` endpoint logs calling agent identity for governance audit trail]

---

## Implementation

[TO FILL: directory tree, ownership table, launchd plist for transcription service, sudoers.d entry, Tailscale ACL diff]

**Sections from handoff document (12-section spec, in progress):**

1. Decision Log
2. Pre-Flight Checklist (SIP status, secrets audit, backup snapshot, Tailscale ACL review)
3. Account Provisioning Specification
4. Filesystem Architecture (directory tree, ownership table, permission matrix)
5. Environment Configuration
6. Transcription Service Specification (topology, process ownership, launchd config, auth model)
7. Daemon & Agent Interaction Model
8. Shared State vs. Separated State — Decision Matrix
9. Security Boundaries
10. Dan-Facing Runbook
11. Validation Test Matrix
12. Rollback Procedure

---

## Test Coverage

[TO FILL: validation test matrix from section 11 of handoff doc]

Anticipated tests:
- `sudo -u dan ls /Users/reuben` → permission denied
- `sudo -u dan ls /Users/Shared/hummbl/outputs` → success
- Ollama `:11434` still responds after account creation
- Open Brain `:11435` still responds after account creation
- Bus bridge `:18790` still responds after account creation
- mlx-whisper endpoint accessible from Dan's account (if shared daemon)
- mlx-whisper endpoint accessible from iOS TestFlight (Tailscale ACL)

---

## Multi-Agent Coordination Evidence

| Timestamp | From | To | Type | Signal |
|---|---|---|---|---|
| [TO FILL] | claude-code | all | STATUS | Planning ingest from claude.ai session — nodezero multi-user architecture |

---

## Outcomes

[TO FILL: post-implementation]

**Expected outcomes:**
- Dan has a functional terminal environment on nodezero with scoped access `[PREDICTED]`
- Zero disruption to Ollama, Open Brain, nightly consolidator, or bus bridge `[PREDICTED]`
- `/Users/Shared/hummbl/outputs/` contains Arbiter reports + governance artifacts readable by both accounts `[PREDICTED]`
- mlx-whisper transcription accessible to Dan and to iOS TestFlight via Tailscale `[PREDICTED]`
- Rollback procedure tested and documented before any account creation `[PREDICTED]`

---

## Governance Primitives Used

[TO FILL: which HUMMBL governance primitives are exercised by the transcription service and shared outputs]

Anticipated:
- **Append-only governance bus** — transcription service requests logged with caller identity if governance audit trail is implemented
- **Circuit breaker** — transcription service wrapped with circuit breaker if integrated into founder-mode pipeline
- **HUMMBL governance receipts** — if mlx-whisper is wired into the Morning Briefing pipeline, its outputs should carry governance receipts

---

## Key Takeaways

[TO FILL: post-implementation]

**Draft takeaways from architecture phase:**

- **Shared filesystem beats sync daemons for co-located users.** When two accounts live on the same machine, ACL-governed shared directories (one inode) eliminate an entire class of sync consistency bugs. Rsync daemons are the right answer only when independent writable copies are required.

- **Scope sudo grants to named commands, not roles.** An executive who can restart one specific launchd service via `/etc/sudoers.d/` has exactly the power they need. Full sudo for a non-developer user is a lateral movement vector, not a convenience.

- **Governance audit trail at the service boundary.** The decision to log caller identity on `/transcribe` requests is the difference between "mlx-whisper ran" and "the briefing agent called mlx-whisper at 06:14 with a 3-minute audio file." The second version is HUMMBL's product.

---

## Related Work

- [Seshat Sovereign Orchestration](seshat-cross-session-sovereign-orchestration.md) — the orchestration layer that will coordinate Dan's onboarding tasks
- nodezero infrastructure: `founder_mode/playbooks/DANIEL_ONBOARDING.md`
- mlx-whisper integration: `docs/tasks/` (voice pipeline task definition)
- People: [Dan Matha context](../../../.claude/projects/-Users-others/memory/people_dan_matha.md)

---

## Session Log

| Date | Update |
|---|---|
| 2026-04-10 | Draft opened. Planning session ingested from claude.ai — 12-section handoff spec in progress on separate Claude session (feat/claude/push-pull-budget-hardening). Key open questions: transcription topology (shared daemon vs. per-user), Dan's sudo scope, Tailscale ACL policy, iOS TestFlight endpoint routing. |
