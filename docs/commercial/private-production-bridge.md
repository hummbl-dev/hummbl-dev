# Private Commercial Production Bridge

Issue: hummbl-dev/hummbl-dev#80

Status: public-safe routing note. This file does not contain production implementation details.

## Purpose

Use the private commercial production lane for fulfillment, customer intake, payment-adjacent operations, implementation details, and delivery tracking that should not be mirrored in this public coordination repo.

The public repo may define generic routing, checklist, and receipt expectations. It must not hold customer records, payment internals, webhook details, credentials, private links, or private collaborator-specific details.

## What Belongs in the Private Production Lane

- customer intake records
- fulfillment status tracking
- scheduling and delivery coordination
- payment-adjacent operational notes
- production implementation details
- customer-specific follow-up
- private delivery checklists
- non-public links, account details, and access notes

## What Can Stay Public

- generic offer descriptions
- generic buyer router language
- public-safe intake field outlines
- generic fulfillment runbook structure
- sanitized proof/demo packet outline
- public/private boundary rules
- receipts that say a private follow-up exists without copying its contents

## Move-to-Private Checklist

Move work out of the public repo when it includes:

- customer name, contact, records, or private business context
- payment, Stripe, webhook, invoice, refund, or checkout internals
- credentials, API keys, tokens, links with embedded access, or account details
- production deployment, access, or operational instructions
- private collaborator, household, health, legal-outreach, or relationship details
- high-ticket scope negotiation or delivery terms not yet reviewed

## Public-to-Private Handoff

Use this public-safe handoff pattern:

```md
## Public-safe summary

Private production follow-up needed for: [generic reason].

## Public artifact

[link to public offer/menu/runbook/issue]

## Private lane action

Create or update a private production task for fulfillment, intake, customer follow-up, or payment-adjacent implementation.

## Boundary

Do not copy private task contents back into this public issue. Public closeout should include only a sanitized receipt.
```

## Jenna-Suitable Review Tasks

Jenna-suitable work in this lane should not require secrets, customer data, payment internals, or production access.

Good first-pass tasks:

- plain-English review of customer-facing copy
- intake wording review using sanitized examples
- customer FAQ organization
- delivery-complete checklist review
- proof/demo packet organization
- follow-up template clarity pass

Not suitable without deeper human review:

- payment configuration
- production access
- customer data handling
- legal/compliance/security certification claims
- private account or credential handling

## Completion Receipt

Public completion comments should include:

- public branch and PR link
- files changed
- validation run
- generic private lane action taken or recommended
- explicit confirmation that no customer data, payment internals, secrets, or private collaborator-specific details were mirrored publicly
