# Private Fulfillment Tracker Schema

Issue: hummbl-dev/hummbl-dev#80

Status: public-safe schema recommendation. Use only in the private commercial production lane.

## Purpose

Track fulfillment work without leaking customer, payment, or production details into public issues.

## Recommended Fields

| Field | Type | Notes |
|---|---|---|
| `task_id` | string | Stable private identifier. |
| `offer_path` | enum | `learn`, `diagnose`, `implement`, `operate_inquiry`. |
| `customer_ref` | string | Private reference only; do not mirror publicly. |
| `owner` | enum | Private assignment value. |
| `status` | enum | `intake`, `scoping`, `scheduled`, `in_progress`, `review`, `delivered`, `follow_up`, `closed`, `blocked`. |
| `public_artifact_ref` | string | Public issue, PR, or doc link when safe. |
| `private_artifact_ref` | string | Private task/doc reference. |
| `required_inputs` | list | Private checklist of missing inputs. |
| `delivery_due` | date | Optional target date. |
| `sensitive_data_present` | boolean | True means never mirror details publicly. |
| `payment_adjacent` | boolean | True means route through private/human review. |
| `human_review_required` | boolean | True for scope, refund, legal/compliance/security/medical/audit, production access, or customer-data issues. |
| `jenna_suitable_review` | boolean | True only when the task can be done without secrets, customer data, payment internals, or production access. |
| `public_closeout` | text | Sanitized summary only. |
| `private_notes` | text | Private lane only. |

## Status Values

```text
intake
scoping
scheduled
in_progress
review
delivered
follow_up
closed
blocked
```

## Required Privacy Checks

- [ ] No customer data copied into public issue.
- [ ] No payment internals copied into public issue.
- [ ] No credentials or production access details copied into public issue.
- [ ] Public closeout is generic and receipt-like.
- [ ] Human review is flagged before high-risk claims or commitments.

## Public Closeout Pattern

```text
Private production follow-up was created or updated for the relevant commercial fulfillment work. Public docs remain limited to routing, generic offer structure, and sanitized receipts.
```
