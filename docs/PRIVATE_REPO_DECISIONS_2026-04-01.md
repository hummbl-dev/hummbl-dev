# Private Repo Cleanup Decisions - 2026-04-01

This file is the private-repo counterpart to the public cleanup decision table.

## Keep Private And Govern More Tightly

### `hummbl-production`
Decision: Keep private
Reason: active production system with operational sensitivity

### `hummbl-iac`
Decision: Keep private
Reason: real workstation and fleet configuration; should stay non-public

### `governed-iac-reference`
Decision: Keep private or selectively publish later
Reason: strategically relevant, but publication should be intentional

### `hummbl-tuples`
Decision: Keep private
Reason: strategically relevant and recent; normalize branch and governance first

### `meeting-archive`
Decision: Keep private
Reason: likely sensitive operational content

### `hummbl-cca-f`
Decision: Keep private pending clearer publication intent
Reason: not part of the current public spine

## Keep Private Only If Actively Used

### `workflow`
Decision: Reassess
Reason: large private repo but unclear role from public narrative alone

### `hummbl-systems`
Decision: Reassess
Reason: name overlap with broader HUMMBL positioning; keep only if actively used

### `hummbl-research`
Decision: Keep private if still active, otherwise archive
Reason: plausible ongoing value but likely sensitive

### `autoresearch-reports`
Decision: Keep private if actively referenced, otherwise archive
Reason: likely derived research output; can create clutter if stale

### `ci-governance`
Decision: Merge or archive unless still actively distinct
Reason: likely overlaps with governance patterns now present elsewhere

### `hummbl-v2`
Decision: Archive unless it is still a live transition workspace
Reason: version-suffixed repos often become ambiguity traps

### `hummbl-old-version`
Decision: Archive
Reason: historical repo should be explicit archive, not ambiguous active code

### `hummbl`
Decision: Reassess
Reason: generic private repo name creates ambiguity

## Prefer Archive / Delete / Consolidate

### `discovery`
Decision: Archive or delete
Reason: zero-signal placeholder unless still active

### `docs`
Decision: Merge into canonical docs location or archive
Reason: generic name and high confusion risk

### `god-mode`
Decision: Archive unless actively used and governed
Reason: confusing name, weak external readability, likely process debt

### `mirror-agent`
Decision: Archive or merge
Reason: placeholder or experimental naming without canonical role

### `rpbx`
Decision: Archive or delete
Reason: non-descriptive and low-signal

### `hummbl-gaas-platform`
Decision: Archive unless it is a current strategic initiative
Reason: zero-signal from current visible account story

### `games`
Decision: Archive or delete
Reason: unrelated or low-signal relative to current HUMMBL story

### `sys-arch-testing`
Decision: Archive if only a scratchpad
Reason: testing repos age poorly unless clearly active

### `autoresearch-pipeline`
Decision: Archive or merge into a live research repo
Reason: pipeline/report split may be unnecessary if stale

### `hummbl-prototype`
Decision: Archive
Reason: prototype repos should either graduate or become historical archive

### `hummbl-asi`
Decision: Reassess quickly; archive if inactive
Reason: broad strategic naming without visible current anchor

### `hummbl-gpts`
Decision: Archive or merge into current product-facing repo
Reason: older product surface likely superseded

### `forge`
Decision: Reassess
Reason: generic name and unclear unique function

### `init-system`
Decision: Archive or merge if it only contains bootstrap ideas now covered elsewhere
Reason: likely overlaps with `hummbl-iac` or agent infra work

### `Poe-bots`
Decision: Archive unless actively used
Reason: platform-specific historical repo likely low priority now

### `OpenAgent`
Decision: Archive unless it has current strategic value
Reason: ambiguous and likely superseded

### `codex-agent-folder`
Decision: Archive or merge
Reason: likely workspace artifact rather than a durable product repo

### `kimi-code-folder`
Decision: Archive or merge
Reason: likely workspace artifact rather than a durable product repo

### `hummbl-agent-federation`
Decision: Reassess
Reason: may still matter strategically, but name overlaps with `hummbl-agent`

### `agent-os`
Decision: Reassess
Reason: potentially strategic, but unclear relation to current canonical public spine

### `hummbl-infra`
Decision: Merge into `hummbl-iac` or archive unless clearly distinct
Reason: likely name overlap with infrastructure repos

### `base120-corpus-validator`
Decision: Merge into `base120` unless there is an active reason to keep it separate
Reason: likely belongs with the canonical Base120 repo

### `gastown`
Decision: Reassess separately
Reason: large private repo; may be active but does not map cleanly to the visible HUMMBL structure

## Suggested Private Cleanup Order

1. Archive obvious placeholders and zero-signal repos first.
2. Archive or rename historically confusing repos (`hummbl-old-version`, `hummbl-v2`, `god-mode`).
3. Merge overlapping infra/research repos where one canonical location should exist.
4. Review large or ambiguous repos (`workflow`, `gastown`, `agent-os`, `hummbl-agent-federation`) with explicit owners.

## Rule Of Thumb

A private repo should satisfy at least one of these:
- active operational use
- active research or product development
- deliberate archive value
- sensitive material that should exist but not be public

If it satisfies none, it should usually be archived or deleted.
