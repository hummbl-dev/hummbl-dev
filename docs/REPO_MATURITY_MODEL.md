# Repo Maturity Model

Updated 2026-07-04. Public HUMMBL repos use lightweight maturity tags so visitors can tell what is ready to use, what is exploratory, and what is retained for reference.

## Maturity levels

| Level | Meaning | Contributor access | Canon posture |
|---|---|---|---|
| `seed` | Created, concept framed, README + license + initial issues. Expect change. | Docs/schema contributions only | Non-canon |
| `v0.1-packet` | Has v0.1 boundary doc, prior art, JSON schema, valid/invalid fixtures, and receipt. Minimal but coherent. | Docs/schema/fixture contributions | Non-canon |
| `exploratory` | Active investigation or prototype. Useful, but not stable guidance. | Scoped contributions | Non-canon |
| `active` | Maintained project with current work, issue triage, and review expectations. | Open or scoped (see CONTRIBUTING.md) | Non-canon unless marked |
| `canonical-candidate` | Proposed for HUMMBL canon. Under audit. May become canonical after review. | Scoped contributions | Candidate — not yet canon |
| `canonical` | Approved authority surface. Backed by receipts, audit, and explicit adoption. | Scoped contributions with review gates | Canon |
| `maintenance` | Usable but mostly receiving fixes, docs updates, or dependency care. | Fixes only | Non-canon unless marked |
| `archived` | Retained for reference. Do not treat as current unless explicitly marked. | Closed | Non-canon |
| `hold` | Frozen pending operator decision. Do not extend. | Closed | Indeterminate |
| `private/not-public` | Known org surface that is not part of the public collaboration path. | N/A | N/A |

## Surface types

| Type | Meaning |
|---|---|
| `implementation-bearing` | Ships runnable code. Tests, builds, releases. |
| `pattern/reference` | Docs, schemas, fixtures, prior art. No runtime code. |
| `docs-first` | Documentation surface. May graduate to implementation-bearing later. |
| `distribution` | Generated or policy-validated install surface (Homebrew, Scoop, winget, Nix). |
| `profile` | Organization profile, governance defaults, shared templates. |

## Contributor readiness

| Level | Meaning |
|---|---|
| `open` | Accepting contributions from outside collaborators. |
| `scoped` | Accepting contributions within defined scope — read CONTRIBUTING.md. |
| `closed` | Not accepting contributions. |

## Use

Status tags describe repository maturity, not legal, compliance, or security assurance. A `seed` or `v0.1-packet` repo can be useful without being canon. A `canonical` repo still needs source-specific review before operational adoption.

## Promotion path

```text
seed → v0.1-packet → exploratory/active → canonical-candidate → canonical
                                                        ↓
                                                    maintenance → archived
```

Promotion requires:
1. Explicit operator decision (not agent self-promotion)
2. Receipt documenting the promotion rationale
3. Audit evidence (tests, reviews, adoption proof)
4. Update to this model and `docs/repo-map.md`

Demotion to `hold` or `archived` requires the same.
