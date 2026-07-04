# Jenna + Reuben Collaboration Repo Map

Status: public-safe routing note. This file is not a private work log.

## Rule

Use this public repo only for sanitized coordination, routing, and receipts. Private Jenna-specific, household, health, job-search, legal-outreach, relationship, customer, payment, or production-secret content belongs in the private lane that owns the work.

If a detail is not clearly public-safe, omit it and leave only a generic pointer.

## Repos

| Repo | Visibility | Purpose | Public-safe summary | Do not mirror here |
|---|---|---|---|---|
| `hummbl-dev/hummbl-dev` | public | Agent command surface and public routing | Which repo owns which workstream, sanitized receipts, public docs | Private facts, customer data, personal records, secrets |
| `jenna-mode/jenna-mode` | access verified by local checkout on Huxley; connector access was previously pending | Jenna-mode collaboration surface | Access status and routing boundaries only | Private Jenna-mode content or public positioning without approval |
| `hummbl-dev/household-income-ops` | private | Household income, role, opportunity, and receipt ops | "Jenna-ready client-success, documentation, intake, QA, and income-ops tasks are tracked privately." | Household records, financial details, job-search specifics, private contact data |
| `hummbl-dev/hummbl-physical-activity` | private | Physical-activity source work and private applied-protocol lane | Generic governance and privacy boundaries | Health/body details, protocol specifics, measurements, outcomes, photos |
| `hummbl-dev/hummbl-production` | private | HUMMBL commercial fulfillment and production implementation | Public/private boundary for commercial work | Customer records, Stripe/payment internals, webhook details, credentials |

## Routing

- Public positioning, repo maps, and agent routing docs: `hummbl-dev/hummbl-dev`.
- Jenna-specific planning or consent-sensitive collaboration: `jenna-mode/jenna-mode`.
- Household income execution and resume-safe private receipts: `hummbl-dev/household-income-ops`.
- Private applied physical-activity or protocol details: `hummbl-dev/hummbl-physical-activity`.
- Offer fulfillment, customer intake, production implementation, and payment-adjacent work: `hummbl-dev/hummbl-production`.

## Agent Stop Conditions

Stop and route privately when work includes:

- personal health, body, relationship, household, financial, legal-outreach, or job-search details
- customer, payment, fulfillment, webhook, credential, or production-secret details
- any proposed public claim about Jenna's role, status, outcomes, or private work
- legal, medical, therapeutic, compliance, security, or audit-certification claims

## Verification

- `hummbl-dev/household-income-ops`: verified by local checkout on Huxley.
- `hummbl-dev/hummbl-physical-activity`: verified by local checkout on Huxley.
- `jenna-mode/jenna-mode`: verified by local checkout on Huxley after initial connector uncertainty.
- `hummbl-dev/hummbl-production`: private repo referenced as the production lane; do not inspect or mirror private implementation unless the task explicitly requires it.
