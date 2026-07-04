# Customer Intake Form Outline

Issue: hummbl-dev/hummbl-dev#76

Status: public-safe draft. Do not collect secrets, regulated data, customer records, or private operational details by default.

## Purpose

Collect only enough context to route a HUMMBL public offer request, schedule or scope the work, and identify whether a human review is required before delivery.

## Required Fields

| Field | Purpose |
|---|---|
| Name | Identify the requester. |
| Email | Send scheduling, intake, and delivery updates. |
| Organization or project | Understand context without requesting private details. |
| Offer path | `Learn`, `Diagnose`, `Implement`, or `Operate inquiry`. |
| Primary goal | One or two sentences on the desired outcome. |
| Current agent/tool use | High-level description only. |
| Target workflow or repo | Public link or sanitized description. |
| Deadline or timing | Scheduling and capacity planning. |
| Review constraints | Known approvals, stakeholders, or sensitive boundaries. |

## Optional Fields

- public repo or documentation links
- preferred meeting times
- prior public materials to review
- non-sensitive examples of current process friction
- accessibility or communication preferences

## Do Not Ask By Default

- passwords, API keys, tokens, or credentials
- customer records or payment data
- private employee, legal, health, or HR details
- regulated data
- confidential contracts
- security incident details
- private Jenna-specific or household details

## Human Review Triggers

Route to human review before accepting or delivering when intake mentions:

- legal, compliance, security, medical, or audit certification
- regulated data or customer records
- production access or secrets
- high-ticket implementation without a clear scope
- urgent incident response
- private household, health, job-search, or relationship context

## Confirmation Copy

```text
Thanks. We received your request and will route it based on the selected offer path. Please do not send passwords, API keys, customer records, regulated data, or confidential documents through this form.
```
