# Peptide Infrastructure Integration v0.1 — Cross-Repo Contracts, Razor Tests, Telemetry, and AAR

**Status: INTEGRATION / GOVERNANCE ISSUE — START AFTER CORE CONTRACTS STABILIZE — NON-CANONICAL**

Issue: hummbl-dev/hummbl-dev#146
Parent: hummbl-dev/hummbl-dev#145
Governed-reasoning framework: hummbl-dev/hummbl-dev#142

## Child workstreams

- Source packet: hummbl-dev/research-source-packets#11
- Bibliography/source registry: hummbl-dev/hummbl-bibliography#77
- Long-form field atlas: hummbl-dev/hummbl-papers#17
- Claim/evidence schema and validator: hummbl-dev/claim-evidence-ledger#8
- Seed evidence: hummbl-dev/claim-evidence-ledger#9
- Identity ontology and read API: hummbl-dev/knowledge-as-code#6
- AI/ML assurance: hummbl-dev/ai-source-verification#19
- Private medical translation/governance: hummbl-dev/hummbl-medical#14

## Objective

Integrate the peptide-science workstream into one cross-repo, source-resolving, validator-backed system. Produce the public-safe docs spine, identifier contract, compatibility tests, governed-reasoning audit, telemetry, release gates, and final after-action review.

## Dependency gates (4)

### Gate A — source substrate
- source packet has stable path and checksum
- source registry has stable IDs and authority posture
- baseline preservation/diff receipt exists

### Gate B — semantic substrate
- claim/evidence schema version frozen for v0.1
- ontology identity invariants testable
- cross-repo Evidence Graph v0.1 mapping documented
- ID collision and version rules defined

### Gate C — domain extensions
- representative seed records validate
- contradiction/null/supersession cases work
- AI/ML leakage controls reviewed
- private medical lane defines public projection boundary

### Gate D — integration and release
- cross-repo references resolve
- validation suites run together
- docs and machine artifacts agree
- adversarial review closed or findings accepted
- AAR and release receipt published

## Required integration artifacts (8)

1. Public docs spine
2. Cross-repo identifier contract (source, claim, entity, preparation, assay, artifact IDs)
3. Compatibility test manifest
4. Cross-repo worked example (source → packet → bibliography → entity → assay → claim → paper → receipt)
5. Governed-reasoning audit aligned with #142
6. Telemetry specification and initial report
7. Threat/failure-mode review
8. AAR and release receipt

## Governed-reasoning tests (9)

1. Occam / unsupported-assumption
2. Hanlon / error-provenance
3. Hitchens / burden-of-evidence
4. Sagan / consequence-scaled evidence
5. Alder / empirical-connectability
6. Chesterton / change-safety
7. Goodhart / Campbell metric
8. Conway / organizational-interface
9. Parkinson / Hofstadter / Brooks execution

## Telemetry (14 metrics)

- claims with exact source locators
- claims with resolved peptidoform identity
- activity claims with complete context
- regulatory claims with jurisdiction/status/date
- unresolved conflicts
- failed validation by rule and importer
- duplicate/near-duplicate sources and claims
- retraction/correction propagation latency
- reviewer disagreement
- evidence-status calibration
- model predictions later synthesized/tested
- experiment-to-ledger latency
- recurrent questions converted to reusable queries
- private/public boundary violations

## Threat and failure modes (15)

- citation laundering
- same-sequence identity collapse
- product/formulation collapse
- ex-vivo proteolysis mistaken for biology
- incompatible assay pooling
- prediction emitted as observation
- nonhuman evidence emitted as human benefit
- stale/draft regulation emitted as current
- database recursion as independent corroboration
- model leakage and benchmark inflation
- candidate terminology emitted as canon
- private medical material projected publicly
- silent schema drift across repos
- deleted/superseded claims losing history
- local receipt facts as public-source facts

## Acceptance criteria

- [x] 4 dependency gates documented
- [x] 8 integration artifacts documented
- [x] 9 governed-reasoning tests documented
- [x] 14 telemetry metrics documented
- [x] 15 threat/failure modes documented
- [ ] All child issue and PR links present
- [ ] Cross-repo identifier contract documented
- [ ] Evidence Graph v0.1 compatibility demonstrated
- [ ] Complete worked evidence path resolves
- [ ] Deterministic integration checks pass
- [ ] Invalid/adversarial fixture fails for expected reason
- [ ] Public docs and machine artifacts agree
- [ ] Private medical artifacts not exposed
- [ ] Razor tests applied with provenance labels
- [ ] Telemetry includes anti-gaming interpretation
- [ ] AAR distinguishes completed/debt/next gates
- [ ] Final release receipt records commits, validation, reviewers, limitations

## Non-goals

- Deploying a public API in v0.1
- Building a comprehensive peptide database
- Publishing personal medical guidance
- Declaring intelligence-to-infrastructure formulation canonical
- Forcing all domain work into one repository
- Creating integration theater

## Fact posture

This is an integration/governance issue derived from #146. Start after core contracts stabilize. All gates, artifacts, and tests are candidate until child workstreams complete.

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#146
- **Dependency gates**: 4
- **Integration artifacts**: 8
- **Razor tests**: 9
- **Telemetry metrics**: 14
- **Threat modes**: 15
- **Child workstreams**: 8
- **Review status**: PENDING (gated)
