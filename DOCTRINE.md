# DOCTRINE.md - hummbl-dev

**Status:** v0.1
**Steward:** HUMMBL Research Institute

## 1. Thesis

The HUMMBL GitHub organization needs a public front door — a profile, repo inventory, and documentation surface that orients newcomers without exposing internal workflow. hummbl-dev is the bet that a single public repo, clearly bounded, can serve as the map to the rest of the org without pretending to be the territory.

It states what HUMMBL is (governance infrastructure for AI agents), what the bias is (libraries over platforms, receipts over vibes, stdlib-first, human override preserved), and where each capability actually lives. It is honest about what it is not.

## 2. Conceptual vocabulary

- **Profile surface** — the public org README, repo inventory, and orientation docs.
- **Repo inventory** — the table mapping needs (governance, models, MCP, orchestration) to repos.
- **Bias statement** — the explicit design commitments (libraries, receipts, stdlib-first, human override).
- **Boundary** — what this repo is not (not internal workflow, not live runtime state).

## 3. Design principles

1. This repo is the public profile and documentation surface — not a source of truth for internals.
2. The repo inventory is the map; each row links to the canonical repo that owns the capability.
3. Bias is stated explicitly so newcomers know the design philosophy before diving in.
4. No draft cross-repo planning proposals belong here — those are internal.
5. The front door stays stable; the territory behind it evolves.

## 4. Boundaries

hummbl-dev is NOT the source of truth for internal operator workflow, private repo governance, live runtime or queue state, or draft planning proposals. It is the public orientation surface only.

## 5. Open questions

- Should the repo inventory be auto-generated from org metadata rather than hand-maintained?
- How do public-facing docs here stay in sync with canonical repos without becoming a second source?
- What is the right cadence for refreshing the profile as the org grows?
