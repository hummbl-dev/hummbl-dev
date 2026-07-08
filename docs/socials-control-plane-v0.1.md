# Socials Control Plane: Bootstrap Plan

**Status**: candidate (not canon)
**Date**: 2026-07-08
**Issue**: [hummbl-dev/hummbl-dev#92](https://github.com/hummbl-dev/hummbl-dev/issues/92)

## Decision

Create a dedicated social-distribution repo pair:

- **Public**: `hummbl-dev/hummbl-socials`
- **Private**: `hummbl-socials-private` (sensitive social operations)

## Rationale

Existing repos cover adjacent surfaces — public profile/billboard, production docs, outreach, package distribution, GitHub issues/discussions — but there is no dedicated canonical control plane for social strategy, channel operations, shipped-post archives, anti-clickbait policy, analytics, and relationship-aware distribution.

## Public/private boundary

> Public repo = what we would proudly show a collaborator.
> Private repo = what helps decide what to show, when, to whom, and why.

## Public repo shape: `hummbl-socials`

```text
hummbl-socials/
  README.md
  docs/
    strategy.md
    voice.md
    anti-clickbait-policy.md
    audience-map.md
    channel-map.md
    public-private-boundary.md
    metrics.md
  templates/
    build-receipt.md
    sharp-thesis.md
    collaboration-invite.md
    reply.md
    thread.md
  posts/
    x/
      shipped/
    linkedin/
      shipped/
    github-discussions/
      shipped/
  campaigns/
    governed-agentic-work/
    base-n/
    ownward/
    public-repo-spine/
  reviews/
    weekly-aar-template.md
```

## Private repo shape: `hummbl-socials-private`

```text
hummbl-socials-private/
  README.md
  drafts/
    x/
    linkedin/
    threads/
    newsletters/
  targets/
    people.md
    orgs.md
    communities.md
    podcasts.md
    newsletters.md
  relationship-notes/
  analytics/
    screenshots/
    weekly-reviews/
  experiments/
    hooks/
    posting-times/
    audience-tests/
  campaigns-private/
    founder-mode-branding/
    ownward-prelaunch/
    investor-founder-surface/
    ai-agent-collaborators/
  risk/
    do-not-post.md
    sensitive-claims.md
    ip-boundaries.md
```

## Bootstrap tasks

- [ ] Create public repo `hummbl-dev/hummbl-socials`
- [ ] Create private repo `hummbl-socials-private`
- [ ] Add README to each repo explaining the public/private boundary
- [ ] Add public docs: strategy, voice, anti-clickbait policy, audience map, channel map, metrics
- [ ] Add private docs: X cleanse protocol, target map, analytics/AAR template, sensitive-claims register, do-not-post register
- [ ] Add templates for build receipts, sharp thesis posts, collaboration invites, replies, and threads
- [ ] Add first 30-day X/LinkedIn posting experiment
- [ ] Add weekly social AAR cadence

## Acceptance criteria

- [ ] Public/private boundary is explicit before any sensitive drafts are added
- [ ] No private relationship notes, analytics screenshots, unpublished sensitive drafts, or target lists are committed to the public repo
- [ ] Public repo can serve as a visible credibility artifact for HUMMBL social distribution
- [ ] Private repo can serve as the operating cockpit for social strategy and relationship-aware distribution

## Operator action required

Repo creation requires GitHub org permissions. The following repos need to be created:

1. `hummbl-dev/hummbl-socials` — public, with README
2. `hummbl-socials-private` — private, in appropriate private org/home

Once repos exist, the bootstrap files from this plan can be committed directly.

## Status update (2026-07-08)

Both repos created:
- `hummbl-dev/hummbl-socials` — PUBLIC
- `hummbl-dev/hummbl-socials-private` — PRIVATE

Next: add README and bootstrap files to each repo per the plan above.

## Non-canon notice

This plan is a **candidate**. It has not been adopted as HUMMBL canon. No social strategy, voice, or posting cadence is canonized until operator approval.
