# Repo Portfolio Gap, Redundancy, and Recomposition Audit v0.1

**Status: CANDIDATE — PORTFOLIO AUDIT FRAMEWORK — NON-CANON**

Issue: hummbl-dev/hummbl-dev#148

## Summary

Perform a portfolio-level audit of the `hummbl-dev` repository landscape to identify:

1. missing capabilities that justify new greenfield repositories;
2. repositories that are thin, stale, overlapping, confusing, or genuinely redundant;
3. repositories that should remain independently bounded despite apparent similarity;
4. opportunities to absorb one repository into an existing canonical home;
5. opportunities to create new consolidation repositories from multiple predecessor repositories;
6. repositories that should be archived after migration, retained as mirrors, strengthened, split, or deferred.

This is not merely a stale-repository cleanup. The objective is a governed **repo portfolio recomposition**.

## Core distinction: greenfield vs. consolidation repositories

### `CREATE_GREENFIELD`

A new repository created for a capability with no predecessor repository and no appropriate existing canonical home.

### `CREATE_CONSOLIDATION`

A new repository created from two or more predecessor repositories. A consolidation repository is born with lineage obligations:

- source repository identities and source-head SHAs
- imported asset paths
- license preservation and compatibility review
- issue/PR disposition
- consumer and dependency migration
- redirect pointers
- history-preservation mode
- rollback posture
- migration and verification receipts

A consolidation repository MUST NOT become an unbounded miscellaneous archive.

## Action taxonomy

Every audited repository or cluster receives one proposed disposition:

| Action | Description |
|--------|-------------|
| `KEEP` | Repository is canonical, active, and correctly bounded |
| `STRENGTHEN` | Repository is needed but underdeveloped |
| `CREATE_GREENFIELD` | New repo for a capability with no predecessor |
| `CREATE_CONSOLIDATION` | New repo from two or more predecessors |
| `ABSORB_INTO` | Move assets into an existing canonical home |
| `SPLIT_FROM` | Extract a bounded subset into its own repo |
| `ARCHIVE_AFTER_MIGRATION` | Archive after assets are migrated |
| `ARCHIVE_STANDALONE` | Archive without migration |
| `RETAIN_AS_MIRROR` | Keep as a mirror of a canonical source |
| `DEFER` | No action now; revisit after dependencies resolve |

Similar names alone are not sufficient evidence of redundancy.

## First calibration wave

### 1. Documentation surface

- `hummbl-dev/docs`
- `hummbl-dev/mintlify-docs`

Questions:
- Which repository is or should be the canonical documentation deployment source?
- Is one repository a placeholder, duplicate, predecessor, or future deployment target?
- What external links, deployment hooks, DNS, or Mintlify integrations depend on either repository?
- Should one be absorbed, archived, or deliberately repurposed?

### 2. Claim-validator generalization

- `hummbl-dev/general-claim-validator`
- `hummbl-dev/psychedelic-claim-validator`

Questions:
- Is the generalized validator the intended successor?
- Which psychedelic-specific rules, fixtures, schemas, tests, and integrations remain unique?
- Can domain-specific behavior become a configuration/plugin without loss?
- Are there remaining domain-specific defaults or identifiers in the generalized implementation?
- Which consumers, including `founder-mode`, must be migrated or compatibility-tested?

### 3. Agent runtime governance surface

- `hummbl-dev/agent-runtime-governance`
- `hummbl-dev/agent-control-plane-patterns`
- `hummbl-dev/agent-handoffs`
- `hummbl-dev/agent-as-code`

Questions:
- Are these four repositories genuinely distinct concerns or should some be consolidated?
- Which repositories have overlapping schemas, fixtures, or documentation?
- What is the consumer dependency graph?
- Would consolidation reduce cognitive load without losing boundedness?

### 4. Evidence and knowledge surface

- `hummbl-dev/knowledge-as-code`
- `hummbl-dev/claim-evidence-ledger`
- `hummbl-dev/research-source-packets`
- `hummbl-dev/evidence-gate`

Questions:
- Where does each repository add unique value?
- Are there overlapping claim/evidence/provenance schemas?
- Could one repository absorb the others, or is a consolidation repository warranted?

### 5. Governance surface

- `hummbl-dev/hummbl-governance`
- `hummbl-dev/hummbl-governance-kernel`
- `hummbl-dev/hummbl-kernel-factory`

Questions:
- What is the relationship between the PyPI library, the kernel, and the factory?
- Are there overlapping primitives, tests, or documentation?
- Should any be absorbed or consolidated?

## Audit method

### Step 1: Inventory

Enumerate all repositories in the `hummbl-dev` organization with:

- name, description, primary language
- last commit date, last release date
- open issues, open PRs
- stars, forks, watchers
- CI status
- license
- dependencies (upstream and downstream)

### Step 2: Classify

For each repository, determine:

- canonical purpose
- current activity level (active, maintenance, stale, archived)
- unique value
- overlap with other repositories
- consumer count
- migration complexity

### Step 3: Propose disposition

Apply the action taxonomy to each repository or cluster.

### Step 4: Validate

For each proposed disposition:

- check consumer dependencies
- verify no canonical assets would be lost
- confirm migration path exists
- assess rollback risk
- check license compatibility

### Step 5: Document

Produce a portfolio recomposition plan with:

- per-repository disposition
- migration order (dependency-aware)
- consolidation lineage obligations
- risk assessment
- rollback posture

## Non-goals

- Does not execute any migration (this is a planning audit)
- Does not archive any repository without operator approval
- Does not create new repositories without operator approval
- Does not assume name similarity implies redundancy
- Does not treat activity level as the only signal

## Acceptance criteria

- [x] Audit framework documented
- [x] Action taxonomy defined (10 dispositions)
- [x] First calibration wave identified (5 clusters)
- [x] Audit method documented (5 steps)
- [x] Non-goals documented
- [ ] Full portfolio inventory (Step 1)
- [ ] Per-repository classification (Step 2)
- [ ] Disposition proposals (Step 3)
- [ ] Validation (Step 4)
- [ ] Portfolio recomposition plan (Step 5)

## Related

- `hummbl-dev/hummbl-dev#154` — Intentional Repository Scale & Responsibility Topology
- `hummbl-dev/hummbl-dev#153` — Research Integrity master program index

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#148
- **Action taxonomy**: 10 dispositions
- **Calibration clusters**: 5
- **Audit steps**: 5
- **Review status**: PENDING
