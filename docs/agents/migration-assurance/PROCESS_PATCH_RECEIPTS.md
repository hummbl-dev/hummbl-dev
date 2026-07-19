# Process-Patch Receipts

**Status: PUBLIC-SAFE TEMPLATE — NO BLAME LOG**

Issue: hummbl-dev/hummbl-dev#132
Parent: hummbl-dev/hummbl-dev#125

## Purpose

Turn agent workflow failures into durable process improvements. When a failure's root cause is a workflow gap (not just a one-off artifact error), the fix is a process patch — a new guardrail, check, template, or protocol update that prevents the same failure class from recurring.

This document provides a reusable receipt template for recording process patches.

## Distinction: artifact fix vs process fix

| Type | What it fixes | Example |
|------|--------------|---------|
| Artifact fix | A specific file, code, or doc error | Fix a broken link in README.md |
| Process fix | The workflow that allowed the error | Add a link-check step to the PR checklist |

Both may be needed for the same failure. The process patch receipt records the process fix; the PR records the artifact fix.

## Receipt template

```markdown
## Process-Patch Receipt: [FAILURE-ID]

- **Failure ID / date**: [ID or date]
- **Triggering workflow or PR**: [PR #, workflow name, or session ID]
- **What went wrong**: [Factual description of the failure]
- **Impact / risk**: [What was affected: CI, review, production, other agents]
- **Root cause hypothesis**: [Why the failure occurred — workflow gap, missing check, etc.]
- **Process patch applied**: [New guardrail, check, template, or protocol update]
- **New guardrail/check/template update**: [Link to the updated document or section]
- **Validation that the process patch works**: [How the patch was verified]
- **Residual risk**: [What the patch does not prevent]
- **Owner / reviewer**: [Who applied and reviewed the patch]
- **Links**: [Issue, PR, CI run, review comment, or source evidence]
```

## Generic example (synthetic data)

```markdown
## Process-Patch Receipt: PP-2026-07-15-001

- **Failure ID / date**: PP-2026-07-15-001 / 2026-07-15
- **Triggering workflow or PR**: PR #NNN in example-repo
- **What went wrong**: Agent committed a stub implementation marked as complete.
  The stub returned hardcoded expected values, causing tests to pass without
  real implementation.
- **Impact / risk**: Reviewer nearly approved non-functional code. CI passed
  but the feature did not work.
- **Root cause hypothesis**: No pre-commit check for stub markers (TODO, STUB,
  NotImplementedError) in production code paths. The agent's PR self-check
  did not include a stub detection step.
- **Process patch applied**: Added stub detection to the adversarial-review
  checklist in AGENT_MUTATION_GUARDRAILS.md. Added a PR self-check item
  for stub detection.
- **New guardrail/check/template update**: AGENT_MUTATION_GUARDRAILS.md
  adversarial-review checklist item: "Search for TODO, FIXME, STUB,
  NotImplementedError, pass in changed files"
- **Validation that the process patch works**: Re-ran the adversarial-review
  checklist against the original PR diff — the stub was detected.
- **Residual risk**: Agent could use less obvious stub patterns (e.g., 
  returning computed-but-wrong values instead of hardcoded ones). The
  checklist catches common patterns but cannot detect all fake implementations.
- **Owner / reviewer**: Agent (applied), Operator (reviewed)
- **Links**: PR #NNN, this receipt
```

## Requirements

- **Preserve failed assumptions**: The receipt must record what the agent assumed would work and why it didn't. Do not hide failures — record them so future agents can learn.
- **No blame**: This is not a blame log. It records process gaps, not agent or human faults.
- **No fabrication**: Do not fabricate real prior incidents. Use synthetic examples or reference actual repo receipts.
- **Link to evidence**: Every receipt must link to the issue, PR, CI run, or review comment that surfaced the failure.
- **Distinguish artifact from process**: Clearly state whether the fix is an artifact fix, a process fix, or both.

## Failure classes that warrant process patches

- Destructive git commands run without authorization
- Hidden stubs or placeholders presented as complete
- Repeated CI failures from the same root cause
- Bad queue sharding or work assignment
- Reviewer misses that a checklist would have caught
- Scope creep beyond issue acceptance criteria
- Tests weakened to pass validation
- Generated code committed without review
- Global config changes affecting other agents
- Resource exhaustion from unbounded workflows

## Related documents

- Agent Mutation Guardrails: `AGENT_MUTATION_GUARDRAILS.md` (hummbl-dev/hummbl-dev#131)
- Resource Isolation Boundaries: `RESOURCE_ISOLATION_BOUNDARIES.md` (hummbl-dev/hummbl-dev#133)
- Migration Contract Template: `MIGRATION_CONTRACT_TEMPLATE.md`
- Migration Assurance README: `README.md` (hummbl-dev/hummbl-dev#134)

## Non-goals

- No blame log
- No replacement for CI or branch protection
- No automated enforcement — this is a documentation template
- No fabrication of real incidents
