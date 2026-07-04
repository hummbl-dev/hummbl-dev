# Offer Fulfillment Runbook

Status: draft public-safe operating outline.

## Fulfillment Flow

1. Confirm offer path: Learn, Diagnose, Implement, or Operate inquiry.
2. Collect only minimum required intake.
3. Confirm scope, delivery window, review owner, and stop conditions.
4. Deliver the agreed artifact or session.
5. Send completion note and next-step recommendation.
6. Store private customer and fulfillment details only in the private production lane.

## Intake Defaults

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

## Follow-Up Templates

### Missing Intake

```text
Thanks for starting the request. To route it correctly, please send the minimum context requested in the intake form. Do not include passwords, secrets, customer records, or regulated data.
```

### Delivery Complete

```text
The agreed deliverable is complete. The next recommended step is listed in the delivery note. Any private implementation or customer-specific follow-up should stay in the private production lane.
```

### Next-Step Recommendation

```text
Based on this pass, the next useful step is: [recommendation]. This is a recommendation, not a certification or guarantee.
```

## Jenna-Suitable Review

Jenna-suitable first-pass tasks:

- plain-English clarity review
- buyer FAQ draft
- intake wording review
- completion checklist review
- proof/demo packet organization

These tasks should not require production secrets, customer data, private payments data, or regulated information.
