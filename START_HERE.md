# Start Here

Narrow entry point for new visitors to HUMMBL. If you only read one file before opening an issue, read this one.

## 90-second pitch

**HUMMBL** builds governance and release infrastructure for agentic work. The problem: AI agents can do real work, but real work requires authority, review, receipts, rollback, provenance, and human accountability to stay trustworthy. HUMMBL ships small runtime primitives — kill switches, circuit breakers, cost governors, delegation tokens, execution receipts — that make agent work inspectable, reviewable, and shippable. Governance is a runtime property, not a policy PDF.

**Base120** is the mental-model substrate behind HUMMBL reasoning and routing. The reference implementation lives in [`base120`](https://github.com/hummbl-dev/base120).

**Governed agentic work** means every action has identity, authority, receipts, rollback, and audit. Operators stay accountable; automation assists, it does not replace review.

The bias is explicit: governance over hype, receipts over vibes, small primitives over platforms, human accountability preserved.

Canonical surfaces today: [`hummbl-governance`](https://github.com/hummbl-dev/hummbl-governance) (runtime primitives, on PyPI) and [`base120`](https://github.com/hummbl-dev/base120) (mental-model substrate). Everything else is `active`, `v0.1-packet`, `seed`, or `hold` until explicitly promoted.

## Pick your path

| Contributor Type | Best Entry Repos |
|---|---|
| Agent engineer | [`agent-runtime-governance`](https://github.com/hummbl-dev/agent-runtime-governance), [`agent-handoffs`](https://github.com/hummbl-dev/agent-handoffs), [`agent-control-plane-patterns`](https://github.com/hummbl-dev/agent-control-plane-patterns) |
| Governance / policy person | [`governance-as-code`](https://github.com/hummbl-dev/governance-as-code), [`policy-as-code`](https://github.com/hummbl-dev/policy-as-code), [`compliance-as-code`](https://github.com/hummbl-dev/compliance-as-code) |
| Package / release engineer | [`packages`](https://github.com/hummbl-dev/packages), [`homebrew-tap`](https://github.com/hummbl-dev/homebrew-tap), [`scoop-bucket`](https://github.com/hummbl-dev/scoop-bucket), [`winget-manifests`](https://github.com/hummbl-dev/winget-manifests), [`nix`](https://github.com/hummbl-dev/nix) |
| Evidence / research person | [`claim-evidence-ledger`](https://github.com/hummbl-dev/claim-evidence-ledger), [`research-source-packets`](https://github.com/hummbl-dev/research-source-packets), [`ai-source-verification`](https://github.com/hummbl-dev/ai-source-verification) |
| Pattern designer | [`agentic-eng-patterns`](https://github.com/hummbl-dev/agentic-eng-patterns), [`agent-instruction-format`](https://github.com/hummbl-dev/agent-instruction-format), [`execution-receipts`](https://github.com/hummbl-dev/execution-receipts) |
| Tool builder | [`hummbl-governance`](https://github.com/hummbl-dev/hummbl-governance), [`base120`](https://github.com/hummbl-dev/base120), [`arbiter`](https://github.com/hummbl-dev/arbiter), [`mcp-server`](https://github.com/hummbl-dev/mcp-server) |

For the expanded version of each path — what you'd work on, which skills help, what to read first, and good first contributions — see [`docs/contributor-paths.md`](docs/contributor-paths.md).

## What not to touch yet

- [`homebrew-hummbl`](https://github.com/hummbl-dev/homebrew-hummbl) — pending decision #3 (canonical Homebrew tap surface: homebrew-hummbl vs homebrew-tap).
- [`mintlify-docs`](https://github.com/hummbl-dev/mintlify-docs) — pending decision #3 (canonical docs source-of-record: docs vs mintlify-docs).
- Any repo marked `hold` in [`docs/repo-map.md`](docs/repo-map.md) — frozen pending operator decision.
- `seed` / `v0.1-packet` repos accept docs/schema/fixture contributions only — no runtime changes. Check the repo's `docs/v0.1-boundary.md` before starting.

## How to start

1. Pick a path above and open the linked repo.
2. Read its `docs/v0.1-boundary.md` (if v0.1-packet) or README.
3. Check open issues and PRs before starting work.
4. Open an issue describing your proposed change before submitting a PR.
5. Keep PRs small and focused — one concern per PR, with explicit receipts.

New contributors typically land fastest in `v0.1-packet` repos (docs/schema/fixture work) or `hummbl-bibliography` (open contributions). `canonical` and `active` repos have scoped contribution paths with review gates — read their CONTRIBUTING.md first.

## Where to go next

- Full fleet map — [`docs/repo-map.md`](docs/repo-map.md)
- Contribution process — [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Maturity levels — [`docs/REPO_MATURITY_MODEL.md`](docs/REPO_MATURITY_MODEL.md)
- Detailed contributor routing — [`docs/contributor-paths.md`](docs/contributor-paths.md)
- Fleet issue triage — [`docs/FLEET_REMAINING_ISSUES_2026-07-04.md`](docs/FLEET_REMAINING_ISSUES_2026-07-04.md)
- Public collaboration routing — [`docs/PUBLIC_COLLABORATION.md`](docs/PUBLIC_COLLABORATION.md)

If you're still unsure where to start, open an issue in this repo (`hummbl-dev/hummbl-dev`) describing your background and interest. We'll route you.

Questions or partnership inquiries: **reuben@hummbl.io**.

*Governed agents need receipts, not slogans.*
