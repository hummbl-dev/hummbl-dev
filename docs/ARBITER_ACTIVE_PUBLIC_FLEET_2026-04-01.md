# Arbiter Active Public Fleet (2026-04-01)

This document separates active public engineering repositories from archived public reference repositories.

## Why Split the Fleet

Archived public repositories are read-only and should not be treated as part of the active engineering fleet unless deliberately reactivated.

Mixing archived references into the live fleet score distorts the quality signal.

## Active Public Fleet

These repositories should be treated as the current public engineering surface:

- `.github`
- `arbiter`
- `agent-governance-demo`
- `base120`
- `bif`
- `HUMMBL-Unified-Tier-Framework`
- `hummbl-agent`
- `hummbl-assurance`
- `hummbl-bibliography`
- `hummbl-dev`
- `hummbl-governance`
- `mcp-server`

## Archived Public Reference Fleet

These repositories are archived and read-only as of 2026-04-01:

- `agentic-patterns`
- `claude-code-infrastructure-showcase`
- `hummbl-mobile`

## Active Fleet Grades

| Repo | Grade | Status | Notes |
| --- | --- | --- | --- |
| `base120` | A | Green | Strongest active public repo |
| `arbiter` | A- | Green | Improved during remediation pass |
| `mcp-server` | A- | Green | Strong public core repo |
| `hummbl-agent` | A- | Green | Strong public core repo |
| `.github` | A- | Green | Governance-default repo |
| `agent-governance-demo` | B+ | Yellow | Improved during remediation pass |
| `HUMMBL-Unified-Tier-Framework` | B+ | Yellow | Good docs and CI, less engineering-focused |
| `hummbl-dev` | B+ | Yellow | Narrative/profile repo |
| `hummbl-governance` | B+ | Yellow | Broken Dependabot config remains open |
| `hummbl-bibliography` | B+ | Yellow | Improved during remediation pass |
| `hummbl-assurance` | B | Yellow | Improved baseline but still maturing |
| `bif` | B | Yellow | Improved during remediation pass, still lacks stronger CI signal |

## Archived Fleet Handling

Archived public repositories should be scored separately as references, examples, or historical artifacts.

They should only return to the active fleet if all of the following are true:

1. the repository is intentionally unarchived
2. an owner is assigned
3. CI is present and failing checks block merges
4. security and ownership metadata are present
5. the repository fits the canonical public story

## Highest-Priority Remaining Active Fix

- replace `hummbl-governance/.github/dependabot.yml`

## Second-Tier Active Fixes

- decide whether `bif` should gain real CI or remain a reference-heavy repo
- continue tightening `hummbl-assurance` toward the canonical spine standard
- re-run the fleet grading pass after the `hummbl-governance` fix lands
