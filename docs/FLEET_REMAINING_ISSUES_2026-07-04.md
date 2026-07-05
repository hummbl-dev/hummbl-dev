# Fleet Remaining Issues Triage — 2026-07-04

Open issues across `hummbl-dev` after the Fleet Bootstrap wave, classified by bucket so agents do not attempt to auto-complete decision issues that require operator authority.

## Bucket 1: Operator authority

These issues require explicit operator decision. Agents must NOT auto-complete them.

| Repo | Issue | Title | Decision needed |
|---|---|---|---|
| homebrew-hummbl | #3 | decision: choose canonical HUMMBL Homebrew tap surface | homebrew-hummbl vs homebrew-tap |
| homebrew-hummbl | #4 | ci: add Homebrew formula validation workflow (conditional) | Blocked by #3 |
| homebrew-hummbl | #5 | automation: implement repeatable formula bump pipeline (conditional) | Blocked by #3 |
| homebrew-hummbl | #6 | governance: add CODEOWNERS and formula change templates (conditional) | Blocked by #3 |
| homebrew-hummbl | #7 | docs: add Homebrew tap maintainer runbook and usage clarity (conditional) | Blocked by #3 |
| homebrew-hummbl | #8 | policy: define formula admission and deprecation rules (conditional) | Blocked by #3 |
| mintlify-docs | #3 | decision: choose canonical HUMMBL Mintlify docs source-of-record | docs vs mintlify-docs |
| mintlify-docs | #4 | docs-bootstrap: add Mintlify config and initial nav skeleton | Blocked by #3 |
| mintlify-docs | #5 | migration: port core pages from hummbl-dev/docs (conditional) | Blocked by #3 |
| mintlify-docs | #6 | ci: add docs validation checks for Mintlify PRs (conditional) | Blocked by #3 |
| mintlify-docs | #7 | governance: define docs contribution and review policy (conditional) | Blocked by #3 |
| mintlify-docs | #8 | decommission: archive or redirect-only posture for mintlify-docs (conditional) | Blocked by #3 |
| hummbl-dev | #92 | Socials control plane: create public/private repo pair | Operator authority |

**Count: 13**

## Bucket 2: Business/personal ops

Operator-owned work. Not agent-actionable without explicit delegation.

| Repo | Issue | Title | Priority |
|---|---|---|---|
| household-income-ops | #1 | P0: Build Jenna legal resume variants | P0 |
| household-income-ops | #2 | P0: Create Reuben coaching reactivation message | P0 |
| household-income-ops | #3 | P0: Create AI/GitOps governance audit one-pager | P0 |
| household-income-ops | #4 | P0: Create Week 1 application/lead tracker | P0 |
| household-income-ops | #5 | P0: Create true-net gig-work tracker | P0 |
| household-income-ops | #6 | P1: Build law-firm intake/case-ops pilot deck or one-pager | P1 |
| household-income-ops | #7 | P1: Create list of 20 Atlanta/small-firm targets | P1 |
| household-income-ops | #8 | P1: Build sample deposition-summary template | P1 |
| household-income-ops | #9 | P1: Build executive health operating system offer sheet | P1 |
| household-income-ops | #10 | P1: Build founder/public GitHub audit checklist | P1 |
| household-income-ops | #11 | P2: Productize legal ops checklist template | P2 |
| household-income-ops | #12 | P2: Productize coaching trackers | P2 |
| household-income-ops | #13 | P2: Add public-redacted template repo after privacy review | P2 |

**Count: 13**

## Bucket 3: Infrastructure

Implementation work, not docs-first. Requires code, testing, and deployment.

| Repo | Issue | Title | Notes |
|---|---|---|---|
| mcp-server | #342 | Add MCP tool exposure profiles for readonly/dev/prod transports | Implementation |
| mcp-server | #344 | Retire deprecated HTTP/SSE server after authenticated Streamable HTTP replacement | Implementation |
| mcp-server | #347 | Post-cutover hardening: mcp.hummbl.io production MCP server | Implementation |
| mcp-server | #348 | Public read-only MCP server: mcp-public.hummbl.io | Implementation |
| mcp-server | #349 | Custom GPT REST/OpenAPI facade: api.hummbl.io | Implementation |
| mcp-server | #350 | Apps SDK widgets for HUMMBL ChatGPT App | Implementation |
| mcp-server | #351 | Stripe Billing + Checkout + Customer Portal: billing.hummbl.io | Implementation |
| mcp-server | #352 | Entitlement resolver + tool gating for public MCP and REST | Implementation |

**Count: 8**

## Bucket 4: Standing/private protocol

Permanent reminders and private protocol. Not actionable as tasks.

| Repo | Issue | Title | Notes |
|---|---|---|---|
| hummbl-physical-activity | #12 | Permanent reminder: onboarding and handoff continuity | Standing reminder |
| hummbl-physical-activity | #13 | Permanent reminder: evidence-backed claim discipline | Standing reminder |
| hummbl-physical-activity | #14 | Permanent reminder: private boundary + no public mirroring | Standing reminder |

**Count: 3**

## Bucket 5: Founder-mode internal

Internal agent infrastructure. Requires private scope and operator direction.

| Repo | Issue | Title | Notes |
|---|---|---|---|
| founder-mode | #1398 | Dev Social Operating Loop v0.1 | Internal |
| founder-mode | #1399 | Dev Social Signal Ledger v0.1 | Internal |
| founder-mode | #1400 | Add duplicate preflight across open and closed issues | Internal |
| founder-mode | #1403 | Migrate autoresearch bridge/cron off archived autoresearch repos | Internal |
| founder-mode | #1404 | Agent-Zero Human Data Source Matrix v0.1 | Internal |
| founder-mode | #1405 | Agent-Zero Human Data Consent Envelope v0.1 | Internal |
| founder-mode | #1406 | Agent-Zero read-only ingestion prototypes | Internal |
| founder-mode | #1407 | Agent-Zero validity harness: public PPG and sleep datasets | Internal |
| founder-mode | #1409 | ci: prove IssueOps admission-to-harvest receipt chain | Internal |

**Count: 9**

## Bucket 6: Applied domain (private)

| Repo | Issue | Title | Notes |
|---|---|---|---|
| lsat-prep | #5 | LSAT 180 Lab: run first five-question manual tutor session | Requires manual session |

**Count: 1**

## Summary

| Bucket | Count | Agent-actionable? |
|---|---:|---|
| Operator authority | 13 | No — escalate to operator |
| Business/personal ops | 13 | No — operator-owned |
| Infrastructure | 8 | No — requires implementation work |
| Standing/private protocol | 3 | No — permanent reminders |
| Founder-mode internal | 9 | No — requires private scope |
| Applied domain | 1 | No — requires manual session |
| **Total** | **47** | |

## Agent guidance

Before attempting to close any open issue in `hummbl-dev`:

1. Check this triage doc for the bucket classification.
2. If the issue is in Bucket 1 (operator authority), do NOT attempt to close it. Post a `BLOCKED` message to the coordination bus and escalate.
3. If the issue is in Bucket 2 (business/personal ops), do NOT attempt without explicit operator delegation.
4. If the issue is in Bucket 3 (infrastructure), only attempt if explicitly assigned and with implementation context.
5. If the issue is in Bucket 4 (standing reminders), leave it open — it is not a task.
6. If the issue is in Bucket 5 (founder-mode internal), only attempt within the private founder-mode repo scope.
7. If the issue is in Bucket 6 (applied domain), check whether it requires manual work before attempting.
