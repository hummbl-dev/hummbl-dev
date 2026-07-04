# Customer Email Templates

Issue: hummbl-dev/hummbl-dev#76

Status: public-safe draft templates. Adapt before sending.

## Missing Intake

```text
Subject: Missing context for your HUMMBL request

Thanks for starting the request. To route it correctly, please send the minimum context requested in the intake form.

Do not send passwords, API keys, customer records, regulated data, or confidential documents. A public link or sanitized description is enough for the first pass.
```

## Scheduling

```text
Subject: Scheduling your HUMMBL session

Thanks for the context. The next step is scheduling the session or review window.

Please send two or three times that work for you. If there are stakeholders who need to review the output, include their role or review need without sharing private personnel details.
```

## Delivery Complete

```text
Subject: HUMMBL delivery complete

The agreed deliverable is complete.

Next recommended step: [short recommendation]

This is not a legal, compliance, security, medical, or audit certification. Any private implementation, production access, or customer-specific follow-up should move through an approved private lane.
```

## Next-Step Recommendation

```text
Subject: Recommended next step

Based on this pass, the next useful step is:

[recommendation]

Reason:
[one or two sentences]

Known limits:
[what this recommendation does not cover]
```

## Human Review Required

```text
Subject: Human review needed before next step

The request appears to involve a boundary that needs human review before we continue.

Reason:
[boundary: legal/compliance/security/medical/audit/customer-data/production-access/high-ticket-scope]

Please wait for a human confirmation before sending additional sensitive details.
```
