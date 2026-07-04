# HUMMBL Public Surface / Agent Command Center

Issue: hummbl-dev/hummbl-dev#54

Status: board specification. This document does not create the GitHub Project.

## Purpose

The Agent Command Center is the org-level operating map for public HUMMBL surface work. It sits above individual repo issue queues and helps agents, reviewers, and operators see cross-repo seeding, namespace, public-surface, and review-gate work in one place.

This public board should track public coordination only. Private repo inventory, client-sensitive details, private operational receipts, secrets, and non-public implementation details belong in private artifacts.

## Board Scope

Include:

- public repo seeding and bootstrap work
- namespace audits
- public profile and repo-directory work
- public `*-as-code` packet waves
- governed-throughput rollout tasks
- issue/PR review-gate tasks
- public-safe collaboration routing tasks

Exclude:

- private repo names or inventory
- secrets, credentials, payment, customer, or client-sensitive details
- private Jenna-specific, household, health, legal-outreach, or relationship details
- raw private operational receipts
- security vulnerabilities that belong under `SECURITY.md`

## Required Fields

| Field | Type | Values / notes |
|---|---|---|
| Public Repo Target | single select | `hummbl-dev`, `.github`, `hummbl-agent`, `compendium-as-code`, `governance-as-code`, `as-code-family`, `other-public-repo`, `not-applicable` |
| Private Lane Target | single select | `none`, `private-inventory`, `private-production`, `private-collaboration`, `private-source-work`, `private-sensitive-stop` |
| Lane | single select | `public-surface`, `repo-seed`, `namespace-audit`, `as-code-wave`, `governed-throughput`, `review-gate`, `collaboration-routing` |
| Priority | single select | `P0`, `P1`, `P2`, `P3` |
| Publicness | single select | `public`, `public-safe-summary`, `private-boundary`, `sensitive-stop` |
| Agent Suitability | single select | `agent-ready`, `agent-with-review`, `human-only`, `blocked` |
| Source Status | single select | `no-source-impact`, `source-candidate`, `source-verified`, `canon-risk`, `not-canon` |
| Complexity | number | 1-5, where 1 is documentation-only and 5 is multi-repo or policy-sensitive. |
| Target Date | date | Optional unless work is time-sensitive. |
| Notes | text | Public-safe context only. |

## Status Columns

Use these board statuses:

| Status | Meaning |
|---|---|
| Intake | Needs triage or missing required fields. |
| Ready | Scoped, public-safe, and agent-runnable. |
| In Progress | Assigned or actively being worked. |
| Review | PR, issue receipt, or human review is pending. |
| Blocked | Waiting on token scope, private access, human decision, or upstream PR. |
| Done | Merged, closed, or explicitly superseded with receipt. |

## Labels Feeding the Board

Auto-add public issues or PRs with any of:

- `agent-ready`
- `repo-seed`
- `namespace-audit`
- `public-surface`
- `needs-human-review`
- `needs-source-receipt`
- `private-boundary`
- `canon-risk`

Recommended label mapping:

| Label | Board impact |
|---|---|
| `agent-ready` | Agent Suitability = `agent-ready` |
| `needs-human-review` | Agent Suitability = `agent-with-review`, Status = `Review` |
| `private-boundary` | Publicness = `private-boundary` |
| `canon-risk` | Source Status = `canon-risk`, Agent Suitability = `agent-with-review` |
| `repo-seed` | Lane = `repo-seed` |
| `namespace-audit` | Lane = `namespace-audit` |
| `public-surface` | Lane = `public-surface` |
| `needs-source-receipt` | Source Status = `source-candidate` |

## Default Views

1. **Agent Ready**
   Filter: `Agent Suitability = agent-ready` and `Status != Done`.

2. **Review Gate**
   Filter: `Status = Review` or `Agent Suitability = agent-with-review`.

3. **Public Boundary**
   Filter: `Publicness = private-boundary` or `Publicness = sensitive-stop`.

4. **Repo Seeding**
   Filter: `Lane = repo-seed` or `Lane = namespace-audit`.

5. **As-Code Wave**
   Filter: `Lane = as-code-wave`.

## Operating Cadence

Weekly:

1. Move stale `In Progress` cards back to `Ready` or `Blocked`.
2. Close `Done` cards only after the issue or PR has a receipt.
3. Promote one small batch of `agent-ready` work.
4. Check `private-boundary` cards for accidental public leakage.
5. Keep blocker reasons short and concrete.

Before assigning an agent:

- confirm public/private boundary
- confirm controlled public repo target or private lane target
- confirm acceptance criteria
- confirm evidence or source requirements
- confirm whether non-author review is required

## Creation Blocker

Project creation needs GitHub Project scopes that may not be present in every agent token. If creation is blocked by missing `project` or `read:project` scope, leave the issue open with the exact failed command, token-scope evidence, and this spec as the implementation target.

## Acceptance

The board rollout is complete when:

- the Project exists at the org or operator-selected scope
- the required fields are present
- the default views exist
- auto-add rules cover the recommended labels
- #54 has a receipt linking the Project and listing any scope gaps
