# Jenna + Reuben Collaboration Repo Map

> **DEPRECATED 2026-07-18.** Canonical routing map moved to `hummbl-dev/jenna-collaboration-routing` (private). This file is a stale snapshot — do not update, do not route from here. Kept for historical reference only.

Status: public-safe coordination draft  
Source issue: #74

## Purpose

This document maps the current Jenna + Reuben collaboration surfaces so agents can route work without mixing public coordination, private household operations, private health/protocol work, HUMMBL production implementation, or Jenna-mode collaboration content.

This file is intentionally sanitized. It must not contain private Jenna-specific details, relationship details, personal health information, private job-search specifics, household financial records, customer data, production secrets, or private repo contents.

## Routing matrix

| Repo / surface | Verification state | Visibility | Use this repo for | Public-safe summary | Do not include |
|---|---:|---:|---|---|---|
| `hummbl-dev/hummbl-dev` | verified via GitHub connector | public | Coordination issues, public-safe repo maps, sanitized routing docs, public collaboration doctrine | Public command surface for agents | Private Jenna details, health data, household finances, customer/payment secrets |
| `hummbl-dev/household-income-ops` | verified via GitHub connector | private | Household income operations, role/work packets, opportunity tracking, Jenna-ready private task receipts | Private lane for income/role/client-readiness ops | Public mirrors of private household records or job-search specifics |
| `hummbl-dev/hummbl-physical-activity` | verified via GitHub connector | private | Physical-activity source work, protocol primitives, private applied protocol packets | Private lane for health/protocol work | Personal health/body details, photos, measurements, medical claims, public protocol claims |
| `hummbl-dev/hummbl-production` | verified via GitHub connector | private | HUMMBL production/commercial implementation, fulfillment plumbing, customer/intake/payment operations | Private implementation lane for production work | Secrets, customer records, private payment data, private Jenna-specific implementation notes |
| `jenna-mode/jenna-mode` | user-reported; connector returned 404 | unknown / pending verification | Jenna-mode collaboration, if access is verified | User-reported collaboration repo; verify before acting | Do not assume contents, access, visibility, or public permission |

## Core routing rules

1. Keep public docs generic, structural, and receipt-oriented.
2. Route sensitive or personal work to the appropriate private repo.
3. If a detail would embarrass, expose, identify, medicalize, legalize, or commercialize Jenna without explicit approval, do not publish it.
4. If a task needs customer data, Stripe internals, webhooks, private URLs, or production credentials, route to `hummbl-dev/hummbl-production`.
5. If a task concerns income tracking, role building, opportunity support, or Jenna-ready work receipts, route to `hummbl-dev/household-income-ops`.
6. If a task concerns physical activity, health protocols, private applied plans, or body/fitness materials, route to `hummbl-dev/hummbl-physical-activity`.
7. If a task explicitly belongs to `jenna-mode/jenna-mode`, first verify repository access and visibility. Until verified, preserve only a public-safe handoff stub.

## Public-safety stop conditions

Agents must stop, sanitize, or move to a private repo if work includes:

- private relationship material
- private household financial data
- medical, health, body, or fitness details tied to an individual
- legal/job-search specifics or outreach material
- private customer or prospect data
- payment data, Stripe internals, or production secrets
- private repo contents from `jenna-mode/jenna-mode`
- any claim that Jenna is legal counsel, a medical advisor, a therapist, a compliance authority, or a security auditor

## Agent execution order

1. Start with #74 for the repo map and routing boundaries.
2. Use #75 for Jenna-ready work packets.
3. Use #76 for HUMMBL commercial readiness tasks.
4. Use #77 only after verifying `jenna-mode/jenna-mode` access.
5. Use #78 when work becomes private household-income or role/receipt operations.
6. Use #79 when work becomes private physical-activity or applied-protocol material.
7. Use #80 when work involves private commercial fulfillment, customer data, production plumbing, or payment-adjacent implementation.

## Agent receipt requirements

When agents modify this repo map, completion comments must include:

- branch name
- PR link
- files changed
- verification method for each repo mentioned
- explicit privacy-boundary confirmation

