# Sponsorship Readiness v0.1

Status: Phase 2A documentation draft. Phase 2B activation is **held**.

This implementation brief incorporates the independent review conditions on
[issue #224](https://github.com/hummbl-dev/hummbl-dev/issues/224). It authorizes
no Sponsors settings, live tiers, funding link, announcement, or outreach.

## Evidence posture

- `VERIFIED`: supported by a current primary-source or reproducible receipt.
- `REPORTED`: supplied by a platform or project but not independently verified.
- `INFERRED`: a reasoned architecture choice, not an observed fact.
- `UNKNOWN`: no sufficient evidence exists.

Downloads, stars, forks, and one-off contributions are signals, not verified
adoption. Sponsor demand, retention, willingness to pay, and the private
payout/tax/bank/2FA state remain `UNKNOWN`.

## Draft architecture decisions

| Decision             | Draft posture                                                                       |
| -------------------- | ----------------------------------------------------------------------------------- |
| Sponsored identity   | Personal `hummbl-dev`; payout/tax recipient still private and `UNKNOWN`             |
| Provisional flagship | `hummbl-governance`; replace if repeat external use favors another project          |
| Feeder               | `mcp-server` as a first-party integration/discovery path only                       |
| Adoption gate        | Three consented external users is the minimum; five plus retained use is the target |
| Revenue outcomes     | Stretch targets, not forecasts or launch gates                                      |

A verified external user is unaffiliated and has a consented, dated receipt for
a concrete install, integration, evaluation, or repeat-use event.

## Phase ordering

1. Pass adoption, claims, policy, privacy, non-author review, and private
   account-readiness gates.
2. Request GitHub approval/publication.
3. After GitHub publishes the listing, immediately test the profile and checkout
   while logged out.
4. Add `FUNDING.yml` only after both smoke tests pass.
5. Treat any announcement as a separate, later authorization.

The current inherited funding target must remain absent while the listing is
inactive.

## Launch gates

- [ ] At least three consented external-user receipts exist; five is the target.
- [ ] Flagship test, maturity, version, support, and comparison claims are
      reconciled. Website metric drift is separately fixed.
- [ ] Canonical policy and receipt template receive non-author review.
- [ ] Tier copy and independence/privacy contract receive operator approval.
- [ ] Actual payout/tax recipient, payment readiness, and 2FA are privately
      verified without publishing sensitive data.
- [ ] Sponsorship and commercial support calls to action are visibly distinct.
- [ ] Baseline maintenance receipt is published.
- [ ] Logged-out profile and checkout smoke tests pass after publication.

## Experiment clock and scorecard

`T0` is the UTC timestamp when the public Sponsors profile and logged-out
checkout first pass smoke testing. Platform review time before `T0` does not
consume experiment days. Any later platform outage longer than 24 hours is
recorded and pauses sponsor-conversion measurement for that interval.

Adoption minimums:

| Metric                                    |  Before T0 |     Day 60 |                                          Day 90 |
| ----------------------------------------- | ---------: | ---------: | ----------------------------------------------: |
| Verified external users                   |        >=3 |        >=5 | >=5, including >=3 repeat events 30+ days later |
| Verified external integrations/dependents | >=1 target | >=2 target |                                      >=3 target |
| On-time public maintenance receipts       |   Baseline |          1 |                                   3 consecutive |
| Sponsor-caused roadmap exceptions         |          0 |          0 |                                               0 |
| Privacy or acknowledgement incidents      |          0 |          0 |                                               0 |

Stretch outcomes by Day 90 are ten individual sponsors, two organization
sponsors, and $500 MRR. Missing a stretch outcome does not by itself fail the
experiment. The Day-90 decision is continue, revise, replace the flagship, or
stop based on retained use, independence, privacy, administrative burden, and
evidence quality.

Campaign metadata measures completed sponsorships attributed by source. Profile
visits and conversion rates remain `UNKNOWN` unless a separate disclosed,
privacy-compatible measurement system is approved.

Pause or revise if claim drift remains, sponsor requests become support work,
receipt administration exceeds two hours per month, or any material privacy or
influence incident occurs. Do not manufacture activity to meet a target.

## Receipt architecture

Reviewed receipts live as versioned Markdown under
`docs/sponsorship-receipts/YYYY-MM.md`. They link immutable commits, tags, or
release artifacts where possible and document formulas. Corrections are dated,
appended, and reviewable; history is not silently rewritten. Receipts describe
maintenance categories and do not trace individual payments to outputs.
