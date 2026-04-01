# Arbiter Archived Public Reference Fleet (2026-04-01)

This document tracks public repositories that are visible but archived.

## Archived Public Repositories

- `agentic-patterns`
- `claude-code-infrastructure-showcase`
- `hummbl-mobile`

## Interpretation

These repositories should be treated as one of the following:

- historical artifacts
- reference libraries
- reusable examples
- dormant products

They should not be counted against the active engineering fleet unless they are intentionally reactivated.

## If Reactivated

Before any archived public repository is moved back into the active fleet, apply this minimum baseline:

- unarchive the repository
- add or confirm `SECURITY.md`
- add or confirm `.github/CODEOWNERS`
- add or confirm `.github/dependabot.yml`
- verify CI exists and hard-fails on meaningful checks
- confirm the repository still belongs in the public HUMMBL story

## Repo-Specific Notes

### agentic-patterns

Strong conceptual fit with the HUMMBL governance surface. Reasonable candidate for future reactivation if there is active product intent.

### claude-code-infrastructure-showcase

Better treated as a public reference library unless there is a plan to maintain it as an active project.

### hummbl-mobile

Should only be reactivated if there is active mobile product intent and willingness to harden CI beyond the current soft-fail state.
