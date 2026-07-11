# Peptide Science Knowledge Infrastructure v0.1

**Status: CANDIDATE — RESEARCH / INFRASTRUCTURE WORKSTREAM — NON-CANONICAL — AGENT-READY**

Issue: hummbl-dev/hummbl-dev#145

## Origin and preservation posture

A ChatGPT session produced a local append-only package named `peptide_science_infrastructure_v0.2.zip`. It is **not yet preserved in any GitHub repository**, and no agent should imply that it is.

Known package facts from the creation receipt:

- immutable baseline file: `BASELINE_peptide_science_v0.1.md`
- baseline SHA-256: `3d585b87dafb02bc9d5122800251aefa65cb14fabccbad54b13935573a2eab8b`
- integrated monograph: `peptide_science_knowledge_infrastructure_v0.2.md`
- ontology: `peptide_science_ontology_v0.1.yaml`
- claim/evidence schema: `peptide_claim_evidence_schema_v0.1.json`
- seed ledger: `peptide_evidence_ledger_seed_v0.1.jsonl`
- source registry: `peptide_source_registry_v0.1.yaml`
- validation rules: `peptide_validation_rules_v0.1.yaml`
- candidate OpenAPI contract: `peptide_api_contract_v0.1.yaml`
- razor/Base120 crosswalk: `HUMMBL_crosswalk_and_razor_audit_v0.1.yaml`
- manifest and changelog
- reported seed claim count: 29

These are **local artifact receipt facts**, not repository-state facts. The first implementation PR must preserve or deliberately reconstruct them with provenance and diff receipts.

## Governing objective

Build a reusable substrate that can answer:

> What was observed for which exact peptidoform, in which preparation, under which conditions, using which assay, relative to which comparator, with what uncertainty, and supported by which source?

## Identity model

The system must distinguish at minimum:

1. `PeptideSequence`
2. `Peptidoform`
3. `PeptideMolecule` / assembly
4. `PeptidePreparation` / batch
5. `PeptideProduct` / formulation
6. `Assay` and biological context
7. `Observation`
8. `Prediction`
9. `AtomicClaim`
10. `EvidenceItem`
11. `Conflict`, `ReplicationAttempt`, and `Supersession`
12. provenance, review, version, and governance state

## Core architectural rules

- Sequence equality must not imply peptidoform, preparation, or product equality.
- Prediction and observation must remain structurally distinct.
- In vitro, nonhuman in vivo, human observational, controlled clinical, and regulatory evidence must not collapse into one evidence stage.
- Preparation, assay, comparator, conditions, dose/concentration, time, species, matrix, and uncertainty are first-class when relevant.
- Negative results, failed replications, contradictions, corrections, and superseded claims remain visible.
- Source prestige alone cannot determine claim confidence.
- Regulatory statements require jurisdiction, document status, date, product, and indication where applicable.
- Candidate terminology cannot become HUMMBL/BaseN canon by repetition.
- Every implementation must preserve receipts, validation commands, and review results.

## Razors and canonicality

Related governing issue: #142 — Razors for Governed Reasoning v0.1.

Apply its schema and provenance requirements rather than duplicating the razor framework:

- distinguish historical wording, common paraphrase, and HUMMBL-authored extension
- keep all peptide-domain razor applications visibly non-canonical
- do not present a reconstructed formulation of "Reuben's Razor" as verified canon
- operationalize the directive to turn recurrent intelligence into durable, inspectable, reusable capability without silently promoting a new doctrine

## Workstream topology

Create bounded child issues in the repositories that already own the relevant concern:

| Repository | Responsibility |
|------------|----------------|
| `research-source-packets` | baseline/source packet and historical claim audit |
| `hummbl-bibliography` | authoritative peptide bibliography and source registry |
| `hummbl-papers` | append-only long-form scientific synthesis |
| `claim-evidence-ledger` | atomic claim/evidence schema, ledger, validator, conflicts |
| `knowledge-as-code` | peptide ontology, identifiers, provenance graph, read API contract |
| `ai-source-verification` | scientific-source verification and peptide ML leakage controls |
| `hummbl-medical` | private medical, pharmacology, CMC, regulatory, and translation layer |
| `hummbl-dev` | integration spine, governance, cross-repo acceptance, and receipts |

## Shared definition of done

Every child deliverable must:

- preserve a clear source map
- use atomic, scope-bounded claims
- mark observation versus inference versus prediction
- expose uncertainty and unresolved conflicts
- include machine validation where the artifact is structured
- add valid and invalid fixtures for schemas or validators
- document non-goals and misuse risks
- link its PR back to this issue and its child issue
- record commands, outputs, commit SHA, and review disposition
- avoid new canonical terminology unless separately audited and approved

## Suggested sequencing

1. Preserve baseline and sources
2. Stabilize identity and claim primitives
3. Add validators and fixtures
4. Seed edge-case records
5. Add assay, AI/ML, medical, and regulatory extensions
6. Integrate cross-repo references and API contract
7. Run adversarial review and publish an AAR

## Program acceptance criteria

- [ ] Source packet preserves the original baseline and audits historical/scientific claims
- [ ] Bibliography/source registry uses authoritative and primary sources where available
- [ ] Long-form monograph is append-only relative to the preserved baseline
- [ ] Identity ontology distinguishes sequence, peptidoform, preparation, assembly, and product
- [ ] Claim/evidence schema validates atomic records and rejects context collapse
- [ ] Seed ledger includes representative claims plus contradictions and negative/null examples
- [ ] Assay/preanalytical model captures sample handling, method, controls, units, and uncertainty
- [ ] AI/ML protocol includes leakage-resistant split manifests and dataset cards
- [ ] Medical translation layer separates chemistry, PK/PD, CMC, clinical, and regulatory evidence
- [ ] OpenAPI contract is read-only and clearly marked as not deployed
- [ ] Integration tests verify cross-repo identifiers and schema compatibility
- [ ] Telemetry measures provenance completeness, unresolved conflicts, validation failures, and recurring reasoning converted into reusable assets
- [ ] Final AAR records what became reusable infrastructure and what remains analysis only

## Non-goals

- Recommending personal peptide use or sourcing
- Treating research peptides, compounded products, approved products, and supplements as equivalent
- Creating a public therapeutic-claims database before identity and evidence controls exist
- Training or releasing a peptide-generation model in this first phase
- Declaring any new HUMMBL/BaseN term canonical
- Claiming that the local ChatGPT artifact package has already been committed

## Related

- `hummbl-dev/hummbl-dev#142` — Razors for Governed Reasoning v0.1
- `hummbl-dev/hummbl-dev#146` — Peptide Infrastructure Integration
- `hummbl-dev/hummbl-bibliography#77` — peptide science bibliography (draft PR #82)
- `hummbl-dev/hummbl-research#47` — peptide science research agenda (draft PR #54)

## Fact posture

This document is a coordination spec. The local artifact package exists as a receipt fact but is not yet preserved in any repository. No scientific claims are made in this document. All peptide science claims must be sourced and evidence-graded before adoption.

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#145
- **Identity model**: 12 entities
- **Architectural rules**: 9
- **Workstream repos**: 8
- **Sequencing steps**: 7
- **Program acceptance criteria**: 13
- **Non-goals**: 6
- **Review status**: PENDING
