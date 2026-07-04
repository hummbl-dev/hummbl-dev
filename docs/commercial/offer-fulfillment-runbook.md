# Offer Fulfillment Runbook

Status: public-safe runbook outline  
Source issue: #76

## Principle

No public checkout link should exist without a defined delivery path, scope boundary, and follow-up motion.

## Generic flow

```text
purchase or inquiry
-> confirmation
-> intake or asset delivery
-> triage
-> private fulfillment tracker
-> delivery artifact or session
-> delivery receipt
-> follow-up recommendation
```

## Offer fulfillment table

| Offer | Required next step | Private destination | Capacity note |
|---|---|---|---|
| Free Checklist | deliver checklist or capture email route | production/commercial system | unlimited once automated |
| Scorecard Report | verify automated delivery | production/commercial system | automated, monitor failures |
| Field Guide | deliver guide link/file | production/commercial system | unlimited once artifact exists |
| Intake Review | intake form then async review | production/customer tracker | cap weekly volume |
| Micro-Audit | intake, schedule, prep checklist | production/customer tracker | cap live sessions |
| Gap Assessment | intake, scope review, scheduling | production/customer tracker | human review before start |
| Starter Pack | scope review, access plan, kickoff | production/customer tracker | one active package at a time until proven otherwise |
| Workflow Sprint | qualification, scope lock, kickoff | production/customer tracker | one active sprint at a time until proven otherwise |
| Operate Inquiry | human review, custom scope | private sales/procurement lane | no public checkout |

## Intake defaults

Ask for:

- buyer name and organization
- contact email
- selected offer path
- short context paragraph
- target repo/process/workflow, if relevant
- deadline or scheduling constraints

Do not ask by default for:

- credentials
- secrets
- customer data
- private employee/personnel details
- regulated data
- legal, medical, or security incident details

## Follow-up templates

### Missing intake

```text
Thanks for starting the request. To route it correctly, please send the minimum context requested in the intake form. Do not include passwords, secrets, customer records, or regulated data.
```

### Delivery complete

```text
The agreed deliverable is complete. The next recommended step is listed in the delivery note. Any private implementation or customer-specific follow-up should stay in the private production lane.
```

### Next-step recommendation

```text
Based on this pass, the next useful step is: [recommendation]. This is a recommendation, not a certification or guarantee.
```

## Jenna-ready support tasks

- QA whether the next step is obvious to a buyer.
- Draft plain-English follow-up templates.
- Review intake wording for clarity.
- Organize proof/demo packet artifacts.
- Create fulfillment status tracker columns.

## Fulfillment tracker schema

```text
customer
email
company
offer
payment/inquiry source
intake status
scheduled date
delivery due
delivery status
follow-up due
next recommended offer
private notes location
```

## Public safety

Actual customer records, payment IDs, intake submissions, scheduling links, and private notes belong in private production/customer systems, not this public repo.

