# Public Repo Cleanup Decisions - 2026-04-01

This file is the stricter public-facing cleanup recommendation derived from the GitHub audit.

## Keep Public And Actively Maintained

### `hummbl-dev`
Decision: Keep public
Reason: profile repo; anchors the account narrative

### `.github`
Decision: Keep public
Reason: org defaults and public governance surface

### `base120`
Decision: Keep public
Reason: canonical public technical pillar

### `hummbl-governance`
Decision: Keep public
Reason: canonical public governance package

### `mcp-server`
Decision: Keep public
Reason: canonical product/integration surface

### `hummbl-agent`
Decision: Keep public
Reason: canonical agent infrastructure surface

### `hummbl-assurance`
Decision: Keep public
Reason: canonical assurance layer

### `HUMMBL-Unified-Tier-Framework`
Decision: Keep public
Reason: supports intellectual/public framework story

### `hummbl-bibliography`
Decision: Keep public
Reason: useful public support/reference repo

## Keep Public But Tighten Positioning

### `arbiter`
Decision: Keep public only if actively maintained and clearly linked from the public story
Reason: could support the ecosystem, but its role is not yet as canonical as the main spine

### `agentic-patterns`
Decision: Keep public only if it has distinct maintained value
Reason: generic name and overlap risk; easy to dilute the account narrative if not clearly active

### `hummbl-mobile`
Decision: Reassess
Reason: public but not part of the current canonical profile story; keep only if product-relevant now

## Prefer Archive Or Privatize Unless There Is A Current Owner And Purpose

### `bif`
Decision: Archive or privatize
Reason: low-signal name with no obvious role in the public HUMMBL spine

### `agent-governance-demo`
Decision: Archive or fold into a canonical repo
Reason: demo repos age badly and fragment the narrative unless actively used for outreach

## Public Cleanup Order

1. Archive or privatize `bif` unless it has an active external purpose.
2. Archive, privatize, or merge `agent-governance-demo` unless it is currently used in sales, research, or publishing.
3. Reassess whether `arbiter`, `agentic-patterns`, and `hummbl-mobile` deserve public visibility right now.
4. Re-pin public repos after cleanup so the visible story matches the canonical spine.

## Rule Of Thumb

A public repo should satisfy at least one of these:
- it is a canonical product or framework pillar
- it is actively maintained and externally understandable
- it materially supports the public HUMMBL thesis

If it does none of those, it should usually be private or archived.
