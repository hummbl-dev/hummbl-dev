# HUMMBL Public Repo Map

## Core public surface

- `hummbl-dev/hummbl-dev` — public profile and organization-facing documentation
- `.github` — shared contribution workflow and governance defaults

## Distribution surfaces

- `hummbl-dev/packages` (planned for distribution spine)
- `homebrew-tap`
- `scoop-bucket`
- `winget-manifests`
- `nix`

## Governance surfaces

- issue templates
- PR templates
- review gates
- release receipts
- package identity and provenance references

## How contributors should route work

1. Start with issue creation or explicit handoff.
2. Preserve receipts for assumptions, commands, and decisions.
3. Propose changes as PRs or patch artifacts tied to those receipts.
4. Request review for authority-bearing changes.

## First five minutes

1. Read the repo map entry for your target repo.
2. Open the linked issue and confirm scope in that repo.
3. Check open PRs and status labels before commenting.
4. Follow issue-first workflow and receipts before requesting review.

## Contribution flow expectations

- Use issue-first delegation.
- Distinguish idea, candidate, source, and approved doctrine.
- Keep source-of-truth updates tied to explicit merges/review.
- Treat draft repositories and experiments as non-canonical until adopted.

## Experimental status

Some repositories are candidates, experiments, or scaffolds until formally adopted into public proof. Their docs and artifacts should clearly indicate status.

## Candidate Repo Admission Queue

Issue `hummbl-dev#86` is the current planning packet for next-wave repo
candidates. Candidate names are not authorization to create repos. Each accepted
repo still needs a namespace check, public/private boundary, non-scope, status
posture, and receipt-bearing scaffold before creation or promotion.

### Hard Gates

- Run exact GitHub namespace/collision checks immediately before creation.
- Classify the repo as public, private, or private-first/public-later.
- Write initial README scope and non-scope before promotion.
- Mark experimental surfaces as candidate/non-canonical.
- Avoid names that imply official standardization, medical authority, universal
  adoption, or category ownership without receipts.
- Seed accepted repos with contribution, security, status, receipt, and ADR
  scaffolding.

### Top 20 Candidate Decision Table

| Rank | Candidate | Boundary | Maturity | Risk | Audience | Strategic job | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `agent-receipts` | public | seed | medium | agent teams, reviewers | proof layer for agent work | prepare creation packet |
| 2 | `claim-as-code` | public | seed | medium | public-surface maintainers | machine-checkable claims and evidence state | prepare creation packet |
| 3 | `hummbl-cookbook` | public | seed | low | contributors, adopters | practical examples bridge | prepare creation packet |
| 4 | `public-collaboration-kernel` | public | seed | low | external collaborators | structured public intake | prepare creation packet |
| 5 | `source-candidate-registry` | public | seed | medium | researchers, maintainers | source intake before canon | prepare creation packet |
| 6 | `hummbl-cli` | public | candidate | medium | implementers | installable adoption wedge | defer until command scope is smaller |
| 7 | `basen-lab` | public | experimental | medium | researchers, protocol designers | non-canonical BaseN experiments | prepare after explicit non-canon README |
| 8 | `agentic-evals` | public | candidate | medium | agent infra teams | evaluate agent quality/governance | defer until eval fixtures exist |
| 9 | `context-as-code` | public | seed | medium | agent/tooling teams | context routing and boundary packets | defer until schema spine is chosen |
| 10 | `receipt-as-code` | public | seed | medium | governance adopters | portable receipt schemas | merge conceptually with `agent-receipts` first |
| 11 | `model-arbitrage` | public | exploratory | medium | infra/cost teams | cheapest-correct routing | defer; avoid finance-style overclaiming |
| 12 | `agentic-arbitrage` | public | exploratory | medium | operators, founders | business leverage narrative | defer pending public-claim review |
| 13 | `hummbl-starter-kit` | public | seed | low | new repo maintainers | copyable governed repo substrate | defer until `.github` defaults settle |
| 14 | `decision-as-code` | public | seed | medium | governance teams | decision packets with evidence and receipts | defer; overlaps governance-as-code |
| 15 | `artifact-as-code` | public | seed | medium | docs/report generators | generated artifact governance | defer until receipt model stabilizes |
| 16 | `ownward-dogfood` | private | experimental | high | internal product team | private product evidence loop | private-only; no public creation packet |
| 17 | `hummbl-behavior-change` | private-first/public-later | candidate | high | coaching/product teams | behavior-change primitives | private boundary review required |
| 18 | `prior-art-graph` | public | candidate | medium | research maintainers | novelty and overlap checks | defer until source registry exists |
| 19 | `agent-command-center` | public | candidate | medium | agent operators | control-plane spec | defer; public spec exists in this repo first |
| 20 | `workflow-as-code` | public | seed | medium | teams adopting agents | human/agent workflow gates | defer; overlaps collaboration-as-code |

### First-Wave Selection

Prepare creation packets for these first, in order:

1. `agent-receipts`
2. `claim-as-code`
3. `hummbl-cookbook`
4. `public-collaboration-kernel`
5. `source-candidate-registry`

Each packet should include:

- exact namespace check receipt,
- README scope and non-scope,
- public/private boundary,
- status posture,
- initial scaffold list,
- three seed issues,
- explicit overclaim/trademark/public-claim notes.

### Explicit Deferrals

- `ownward-dogfood` and `hummbl-behavior-change` stay private or private-first.
- `hummbl-cli` waits until command scope and package boundaries are smaller.
- `basen-lab` requires non-canonical status language before public creation.
- `agentic-arbitrage` and `model-arbitrage` require public-claim review before
  naming or launch.
- Names implying external standard status, universal protocols, or medical
  authority remain rejected unless a later receipt changes the risk posture.
