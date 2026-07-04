# Non-Author Review Gates

Issue: hummbl-dev/hummbl-dev#63

This guidance preserves the non-author review requirement while separating two
different facts:

1. whether GitHub accepts a formal approving review; and
2. whether a bot status actually reflects a substantive review.

## Rule

Consequential work still needs a non-author check unless the operator explicitly
waives it.

A review counts as formal non-author approval only when GitHub records an
`APPROVED` review from an identity that did not author the PR head commit and is
not the same authenticated account attempting to approve it.

## Valid Formal Reviewers

When a PR is authored by `hummbl-dev`, formal approval must come from a distinct
GitHub identity that GitHub allows to approve the PR.

Valid reviewer identities can include:

- the operator using a distinct GitHub identity;
- a separate approved agent account;
- another trusted human or service account with repository review access.

The same `hummbl-dev` account that authored the PR cannot provide formal
approval for its own PR, even if the review work was performed by a different
local agent session.

## Bot Status Evidence

Bot status contexts are advisory until their comment or run evidence shows a
real review occurred.

Treat a bot status as insufficient for non-author approval when:

- the bot comment says the review was rate-limited;
- the bot comment says the review did not start;
- the bot comment says only a summary or pre-merge check ran;
- the bot review is `COMMENTED`, absent, or not a GitHub `APPROVED` review;
- the status context is `SUCCESS` but the review body contradicts substantive
  review.

Bot output can still be useful evidence for checks, summaries, and findings, but
it is not a substitute for a formal non-author approval when the gate requires
approval.

## Required Evidence Before Merge

Before merging consequential work, record or inspect:

- PR author and head commit author;
- formal GitHub review state;
- reviewer identity and whether it differs from the author identity;
- status check state;
- bot comment or run body when a bot status is used as evidence;
- any operator waiver, if the non-author approval gate is waived.

## Example: compendium-as-code PR #1

`hummbl-dev/compendium-as-code` PR #1 exposed both failure modes.

- Codex performed a review and found no blocking defects, but the formal
  approval attempt failed because GitHub rejected self-approval from the same
  `hummbl-dev` account that authored the PR.
- CodeRabbit showed a `SUCCESS` status context, but its comment said the review
  was rate-limited and did not start.

Correct disposition:

- keep the PR unmerged until a distinct GitHub identity can approve it, or until
  the operator explicitly waives the non-author approval gate;
- do not cite the CodeRabbit `SUCCESS` status alone as substantive review
  evidence;
- preserve Codex's review comment as advisory evidence, not formal approval.

