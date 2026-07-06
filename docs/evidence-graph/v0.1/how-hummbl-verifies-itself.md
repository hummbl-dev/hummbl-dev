# How HUMMBL Verifies Itself

**Status**: candidate (not canon)
**Date**: 2026-07-06
**Issue**: [hummbl-dev/hummbl-dev#104](https://github.com/hummbl-dev/hummbl-dev/issues/104)

## The problem

AI agents that write code, run experiments, and make claims can optimize noise, game their own evaluators, or publish claims without evidence. The question is not "did the agent produce output?" but "can we trust the output enough to act on it?"

## HUMMBL's approach

HUMMBL dogfoods its own thesis: agentic work should be **auditable, source-linked, receipt-backed, and safe to publish**. Here is how that works in practice.

### 1. Every experiment is declared

Before an agent runs an experiment, it declares what it will do in a structured packet ([Autoresearch Packet v0.1](../autoresearch-packet/v0.1/README.md)):

- What metric it is optimizing
- What files it is allowed to change
- How long it is allowed to run
- Where it will record results

This packet is a JSON file that can be validated by a stdlib-only script. No agent self-reports its results without a packet.

### 2. Every verdict is verified

After the experiment runs, the keep/discard decision is checked against five integrity rules ([Measurement Integrity v0.1](../autoresearch-measurement-integrity/v0.1/README.md)):

- **IC-1**: Did the improvement exceed the noise floor? (Or was it seed luck?)
- **IC-2**: Did the agent modify its own evaluator? (Cheating the metric)
- **IC-3**: Did the agent train on the test set? (Holdout leakage)
- **IC-4**: Was the decision rule explicit? (Not just "did it improve?")
- **IC-5**: Was the failure recorded with an error code? (No silent failures)

A keep verdict that fails any check is rejected. The agent does not advance to the next iteration on a failed verdict.

### 3. Every claim is grounded

When HUMMBL makes a public claim (a paper, a research finding, a product assertion), it links the claim to its evidence in an [Evidence Graph](./v0.1/README.md):

- Each claim is a node with a public locator (GitHub PR, issue, or receipt)
- Each evidence link is an edge with a fact posture (public-source, local-execution, derived)
- A validator checks that every release-facing claim has at least one grounding edge

If a claim cannot resolve to evidence, it stays candidate/internal until the missing edge is closed.

### 4. Every fact is classified

Every fact in a HUMMBL artifact carries a source class:

| Class | Meaning |
|-------|---------|
| `public_source_fact` | Verifiable from a public GitHub PR, issue, or receipt |
| `local_execution_fact` | Verified by running a command locally (not yet public) |
| `user_reported_fact` | Reported by the operator (scope, context, intent) |
| `candidate_claim` | Proposed but not yet verified |
| `derived_synthesis` | Bounded inference across source-linked artifacts |

This prevents the common failure mode of mixing "we ran this and observed X" with "we believe X is true."

## What this means in practice

1. **For the operator**: Every agent action has a receipt. Every claim has a trail. Every failure has an error code.
2. **For external reviewers**: Public claims link to public evidence. Fact posture is explicit. No claim is presented as canon without evidence.
3. **For the agent**: The agent operates within bounded autonomy. It cannot self-certify its results. It cannot publish without grounding.

## Limitations

- This is a **candidate spec**, not canon. It has not been adopted as a HUMMBL standard.
- The validators are stdlib-only Python scripts, not a production runtime.
- The worked example covers one cross-repo batch. Generalization to all HUMMBL work is future work.
- Evidence grades (A/B/C/D) are defined in the schema but not yet enforced by the validator.

## Non-canon notice

This document is a **candidate explanation**. It has not been adopted as HUMMBL canon. It describes how the candidate specs (#108, #109, #104) compose into a verification pipeline. No benchmark, performance, or adoption claim is made without evidence.
