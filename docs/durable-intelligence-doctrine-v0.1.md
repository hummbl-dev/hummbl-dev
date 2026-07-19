# Durable Intelligence Doctrine v0.1 — Make Agent Problem-Solving Cumulative

**Status: CANDIDATE DOCTRINE — NON-CANONICAL**

Issue: hummbl-dev/hummbl-dev#162

## Purpose

Preserve and operationalize the recommendation that durable intelligence should be treated as a first-class component of HUMMBL agent workflows, not as optional documentation after the fact.

## Core thesis

Durable intelligence makes problem-solving less difficult by reducing repeated uncertainty. It converts an incoming agent's starting question from:

> What happened, what is true, what was tried, what failed, what remains, and what am I allowed to do?

into:

> Here is the current state, the evidence, the unresolved edge, and the next bounded action.

The underlying technical problem may remain unchanged, but coordination entropy, reconstruction cost, and error risk are reduced.

## Recommended doctrine

Every meaningful agent session should leave behind a compact, durable state transition answering:

1. What changed?
2. What was learned?
3. What remains uncertain?
4. What should happen next?

## Why this matters

### 1. Eliminate rediscovery
Preserve repository state, prior decisions, failed paths, rejected hypotheses, authority boundaries, known defects, and unresolved questions so new sessions start near the frontier.

### 2. Prevent false assumptions
Record claim posture explicitly. At minimum distinguish:

- observed
- source-reported
- inferred
- provisional
- verified
- refuted
- unresolved

Agents must not infer that review implies mutation, discussion implies verification, or a previous verdict implies independent confirmation.

### 3. Narrow the search space
Convert vague work into bounded verification or implementation procedures with exact targets, evidence sources, allowed dispositions, and completion criteria.

### 4. Preserve negative knowledge
Record what did not happen and what is not established:

- no code changed
- no branch created
- no commit made
- hypothesis not confirmed
- environment lacked required tools
- authority source not found

## Acceptance criteria

- [x] Core thesis documented
- [x] Recommended doctrine documented (4 questions)
- [x] 4 "why this matters" sections documented
- [x] 7 claim posture labels documented
- [x] 6 negative knowledge examples documented
- [x] Doctrine adopted as operational practice (schema, validator, fixtures, adoption guidelines)
- [ ] Agent workflows enforce durable state transitions
- [ ] Independent review

## Non-goals

- Replacing documentation with durable intelligence
- Canonizing before review
- Treating durable intelligence as optional

## Fact posture

This is a candidate doctrine derived from issue #162. Not canonical until reviewed and adopted. All recommendations are candidate until operationalized.

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#162
- **Doctrine questions**: 4
- **Why sections**: 4
- **Claim postures**: 7
- **Negative knowledge examples**: 6
- **Review status**: PENDING
