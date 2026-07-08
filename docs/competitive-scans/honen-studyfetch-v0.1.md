# Competitive Scan: Honen / StudyFetch

**Status**: candidate (not canon)
**Date**: 2026-07-08
**Issue**: [hummbl-dev/hummbl-dev#106](https://github.com/hummbl-dev/hummbl-dev/issues/106)

## Source class legend

- `[PRIM]` = primary source verified (website fetched directly)
- `[SEC]` = secondary (search-surfaced, cited but not fully verified)
- `[INF]` = inferred from documented behavior

## Product overview

**Honen** (`https://honen.com/`) is an AI-powered learning platform that transforms source material (docs, recordings, videos, SOPs, topics) into structured courses with multi-format learning activities and a built-in AI tutor.

- **Legal entity**: StudyFetch, Inc. [PRIM, honen.com JSON-LD schema, verified 2026-07-08]
- **Positioning**: "Automated teaching + learning infrastructure for any company" [PRIM, hones.com homepage, verified 2026-07-08]
- **Product Hunt**: Top post (badge visible on homepage) [PRIM, verified 2026-07-08]

## Verified public-source facts

| Claim | Source class | Evidence |
|-------|-------------|----------|
| Honen is a StudyFetch, Inc. product | [PRIM] | JSON-LD `legalName: "Honen (StudyFetch, Inc.)"` on honen.com [verified 2026-07-08] |
| Turns docs, recordings, videos, or topics into courses | [PRIM] | Homepage copy and demo flow [verified 2026-07-08] |
| Nine activity types (read, flashcards, quiz, scenario, projects, tutor) | [PRIM] | Homepage "Adaptable ways to learn" section [verified 2026-07-08] |
| Live tutor with voice and chat | [PRIM] | Homepage "A live tutor along the way" section [verified 2026-07-08] |
| NVIDIA collaboration for K-12 AI education | [PRIM] | Homepage "NVIDIA x Honen" section, 250K high school students [verified 2026-07-08] |
| Enterprise features: SSO, role-based access, audit logs | [PRIM] | Homepage "For Enterprise" section [verified 2026-07-08] |
| FERPA privacy walls for schools | [PRIM] | Homepage "For Schools & Institutions" section [verified 2026-07-08] |
| Free to start, no credit card | [PRIM] | Homepage CTA [verified 2026-07-08] |
| Workspace Assistant handles nudges, reports, reminders | [PRIM] | Homepage "For Small Teams" section [verified 2026-07-08] |

## Unverified public-source pointers

These URLs were listed in #106 but have not been independently fetched/verified as of 2026-07-08:

- Honen learner features: `https://honen.com/features/learner-experience` [SEC]
- Honen about page: `https://honen.com/about` [SEC]
- Honen privacy policy: `https://honen.com/privacy` [SEC]
- Honen enterprise terms: `https://honen.com/enterprise-terms` [SEC]
- NVIDIA K-12 blog: `https://blogs.nvidia.com/blog/ai-education-k-12/` [SEC]
- StudyFetch press page: `https://www.studyfetch.com/press` [SEC]
- SEC Form D for StudyFetch, Inc.: `https://www.sec.gov/Archives/edgar/data/2067704/...` [SEC]

## Relevance to HUMMBL / BaseN / Ownward

Honen is strategically relevant because it overlaps with:

- AI-generated curriculum and training surfaces
- Agentic transformation of source material into learning experiences
- Workforce learning and enterprise knowledge activation
- Tutor / coach / assistant interfaces
- Analytics and learner progress dashboards

**Likely differentiation opportunity**: HUMMBL's governed provenance — claim-evidence ledgers, receipt-bearing transformations, bounded agent handoffs, source-packet discipline, and explicit operator authority. Honen appears to be **product-first, not receipt-first** [INF].

## Disposition

**Monitor. Do not upload private materials.**

Honen / StudyFetch is worth watching, but should be treated as **product-first, not receipt-first**, until deeper evaluation proves otherwise.

Working rule:

> Do not upload proprietary, unpublished, canon-bearing, customer, partner, health, strategy, or private repo materials to Honen/StudyFetch unless/until enterprise legal/data terms are reviewed and explicitly approved.

## Legal / data questions to answer before any private use

- [ ] Does enterprise mode prohibit model training on customer data without written consent?
- [ ] Are generated outputs owned by the customer, licensed to the customer, or retained by Honen/StudyFetch?
- [ ] Are uploads excluded from marketing, SEO, benchmarking, and product-development reuse?
- [ ] What deletion/export guarantees exist?
- [ ] What subprocessors are used?
- [ ] Is there a current SOC 2 report, DPA, security whitepaper, or equivalent enterprise security packet?
- [ ] Are FERPA or education-privacy claims backed by contract terms and operational controls?

## Proposed sandbox evaluation

Use **only synthetic or public-domain source material**:

- [ ] Create or select a synthetic/public-domain mini source packet
- [ ] Upload only that safe packet to Honen
- [ ] Generate a course or learning path from the packet
- [ ] Inspect whether modules preserve source-to-claim traceability
- [ ] Inspect whether generated quizzes/activities are answerable from the provided sources
- [ ] Test whether the tutor cites sources or invents unsupported claims
- [ ] Test update propagation: change a source fact and see whether generated materials update cleanly
- [ ] Test adversarial prompts against the tutor/course assistant
- [ ] Check export options, LMS integration claims, and ownership/portability surfaces
- [ ] Capture screenshots/receipts sufficient for an audit trail

## Definition of done

- [ ] A short markdown evaluation packet exists in the appropriate repo/docs location
- [ ] All factual claims are separated into: observed-in-product, public-source verified, inferred, and unverified
- [ ] No private/proprietary materials were uploaded
- [ ] Screenshots or receipts are preserved where allowed
- [ ] A final recommendation is recorded: ignore, monitor, evaluate further, partner-track, compete-against, or adopt with enterprise controls

## Non-canon notice

This competitive scan is a **candidate analysis**. It has not been adopted as HUMMBL canon. No endorsement, partnership, or product commitment is implied. All claims carry source-class marks.
