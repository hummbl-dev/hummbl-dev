# Governed Throughput v0.2

Issue: hummbl-dev/hummbl-dev#56

This packet is the public command-surface map for turning HUMMBL GitHub templates,
issue forms, labels, and checks into enforceable merge interfaces.

It is not a canon declaration, product claim, or global enforcement switch.

## Doctrine

No ceremonial checkboxes.

Every required field must do at least one of these:

- route work to the right reviewer, repo, or phase;
- block an unsafe merge;
- reduce reviewer ambiguity;
- preserve an audit receipt;
- feed a board, report, or machine check.

If a field cannot change a reviewer, CI job, agent, board, or future auditor's
decision, it should be optional context or removed.

## Public Boundary

This public repo can name public repositories and public coordination issues.
It must not expose private repo names, private operational receipts, secrets,
client-sensitive details, or private protocol content.

The merged inventory in
`docs/governed-throughput/github-surface-inventory-2026-07-04.md` names public
repos only. Non-public repos require a private follow-up artifact before private
rollout.

## Repo Classes

| Class | Examples | Default posture |
|---|---|---|
| Command surface | `hummbl-dev/hummbl-dev` | Public coordination, receipts, issue routing. |
| Default substrate | `hummbl-dev/.github` | Default issue forms, PR template, reusable check docs. |
| Public source adapter | `compendium-as-code`, `*-as-code` repos | Strong source boundary, citation, no private data. |
| Public runtime or package | `hummbl-agent`, `arbiter`, `base120` | Preserve local workflows and CODEOWNERS; compose checks. |
| Public research/docs | `docs`, `hummbl-papers`, research packets | Require evidence and source-status fields. |
| Archived public surface | archived forks and historical repos | Human review before changes; avoid broad rollout. |
| Private/internal | not named here | Private inventory and rollout only. |

## Implementation Map

| Work item | Authority surface | Current status | Next action |
|---|---|---|---|
| Public GitHub surface inventory | hummbl-dev/hummbl-dev#57 | Done; merged in PR #60 | Use it to choose pilots and local overrides. |
| Default substrate | hummbl-dev/.github#17 | Open | Add sparse issue forms, PR template, and report-only check docs. |
| Command-surface packet | hummbl-dev/hummbl-dev#56 | This packet | Review and merge this public coordination doc. |
| Report-only governed check | `.github#17` first | Not implemented | Specify behavior before hard enforcement. |
| Pilot path | `.github`, `hummbl-dev`, one runtime repo, one source-adapter repo | Not started | Run issue form -> PR template -> check -> review -> receipt. |
| Private repo rollout | private artifact | Not started | Inventory privately; do not list private repos publicly. |

## Minimum PR Interface

A governed PR should keep required fields sparse:

```md
## Linked Issue
Closes #

## Boundary
- [ ] Public
- [ ] Private
- [ ] Internal-only
- [ ] Sensitive / requires review

## Source Status
- [ ] No source/canon impact
- [ ] Source candidate only
- [ ] Prior art
- [ ] Canon-bearing change
- [ ] Deprecated/removal

## Change Class
- [ ] Docs-only
- [ ] CI/CD
- [ ] Source packet
- [ ] Code/runtime
- [ ] Governance
- [ ] Public surface

## Evidence
Tests/checks run:
Receipt:
```

## Report-Only Check Behavior

Start as report-only. Do not make this a required status check until pilot repos
show acceptable false-positive rates.

The first check should report:

- missing linked issue;
- more than one boundary selected;
- no boundary selected;
- more than one source status selected;
- no source status selected;
- no change class selected;
- placeholder or empty evidence;
- public-boundary PRs containing private-only markers;
- canon-bearing claims without a human/canon review path;
- runtime changes without test evidence or a docs-only declaration;
- governance-sensitive file changes without CODEOWNERS or owner-review path.

## Labels With Consequences

Use labels only when they route work, drive checks, power board views, or preserve
state.

| Family | Purpose |
|---|---|
| `boundary:*` | Public/private/internal/sensitive routing and privacy checks. |
| `source:*` | Source/canon posture and source-review routing. |
| `change:*` | CI, docs, runtime, governance, source-packet routing. |
| `agent:*` | Agent-suitable handoffs and queue filtering. |
| `intake:*` | Whether required fields are complete. |
| `receipt:*` | Whether evidence and closeout receipts exist. |
| `risk:*` | Human review escalation. |

## Rollout Gates

1. Inventory first: done for public repos in #57 / PR #60.
2. Default substrate second: implement `.github#17` without overwriting existing doctrine.
3. Report-only checks third: warn before blocking.
4. Pilot fourth: prove the full path in a small set of repos.
5. Local overrides last: patch only repos that intentionally override defaults.

## Pilot Set

Use these pilots unless the operator redirects:

- `hummbl-dev/.github`: default substrate.
- `hummbl-dev/hummbl-dev`: public command surface.
- `hummbl-dev/hummbl-agent`: public runtime/product-style repo with local GitHub surface.
- `hummbl-dev/compendium-as-code`: public source-adapter repo.
- `hummbl-dev/governance-as-code`: public docs/governance source-adapter style repo.

## Open Questions

- Which private artifact should hold the non-public repo inventory?
- Should the first governed check live as a reusable workflow, a script, or both?
- Which repo should be the first hard-blocking pilot after report-only proves stable?

