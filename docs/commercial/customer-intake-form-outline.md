# Customer Intake Form Outline

Status: public-safe outline  
Source issues: #75, #76

## Purpose

Define a minimal, plain-English intake outline for HUMMBL async/live offers without collecting sensitive data by default.

This file is an outline only. Actual customer submissions belong in private systems, not this public repository.

## Default intake sections

### About you

- Name
- Email
- Company or project
- Role
- Preferred follow-up method

### About the work

- What are you building or operating?
- Where are you using AI, agents, or automation today?
- What workflow should HUMMBL review?
- What feels unclear, risky, slow, or hard to govern?
- What have you already tried?

### Scope and access

- What docs, repo links, screenshots, or artifacts can you safely share?
- Is anything off-limits?
- Are there credentials, secrets, customer data, or regulated data that should not be shared?
- Do you need an NDA, invoice, PO, or custom agreement before sharing more?

### Outcome

- What would make this engagement useful?
- What deadline matters?
- What decision are you trying to make?
- What would you like to receive from HUMMBL?

## Questions to avoid by default

Do not request sensitive or unnecessary information by default:

- passwords, API keys, or secrets
- customer records
- regulated personal data
- medical, legal, financial, or protected data unless explicitly scoped
- private employee records
- confidential repo access without prior agreement

## Offer routing

| Offer type | Minimum intake needed |
|---|---|
| Intake Review | workflow summary, risk/uncertainty, safe artifacts |
| Micro-Audit | workflow summary, target artifact/repo/process, scheduling context |
| Gap Assessment | team context, governance gaps, current AI/agent use, safe artifacts |
| Starter Pack | repo/process scope, desired implementation boundary, access requirements |
| Workflow Sprint | qualification, kickoff scope, access plan, decision-maker confirmation |

## Human review triggers

Route to human review before accepting or delivering when intake mentions:

- legal, compliance, security, medical, or audit certification
- regulated data or customer records
- production access or secrets
- high-ticket implementation without a clear scope
- urgent incident response
- private household, health, job-search, or relationship context

## Confirmation copy

```text
Thanks. We received your request and will route it based on the selected offer path. Please do not send passwords, API keys, customer records, regulated data, or confidential documents through this form.
```

## Private handling rule

Any actual customer submission, email address, company-specific fact, repo URL, file, screenshot, payment note, or scheduling record belongs in a private production/customer system, not in this public repository.

