# Arbiter Public Fleet Update (2026-04-01)

Follow-up from the public fleet remediation packet.

## Archived Public Repositories Confirmed

The following public repositories are archived and read-only:

- `agentic-patterns`
- `claude-code-infrastructure-showcase`
- `hummbl-mobile`

This matters because they cannot be hardened in place without being unarchived first.

## Interpretation Change

These repositories should not be treated as active engineering repositories unless they are deliberately reactivated.

### Recommended handling

- keep archived if they are reference-only or historical
- unarchive only if they are intended to rejoin the canonical public engineering surface
- exclude archived public references from the active public fleet score if the goal is to measure maintainable production-facing repositories

## Live Repositories Remediated Directly

The following live public repositories received baseline governance fixes during this pass:

- `arbiter`
- `agent-governance-demo`
- `bif`
- `hummbl-bibliography` (`SECURITY.md` only; ownership and Dependabot already existed)

## Remaining Live Public Fixes

1. Replace `hummbl-governance/.github/dependabot.yml`
2. Decide whether `bif` should gain real CI or be explicitly treated as a reference repository
3. Recompute fleet grades with archived repos separated from active repos
