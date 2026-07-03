# Profile billboard enhancement plan

Status: draft agent handoff
Date: 2026-07-03
Repo: hummbl-dev/hummbl-dev

## Purpose

Enhance `hummbl-dev/hummbl-dev` as the primary public profile billboard and routing hub for HUMMBL, agents, collaborators, and repo discovery.

This repo already has a strong README spine: public HUMMBL profile/static-tools/docs surface, start-here repo table, governance definition, research/tools/contact sections, and repo boundary language. The next upgrade should make the first-screen experience sharper and make public collaboration/agent routing more explicit.

## Recommended positioning

Treat this repository as:

> The public HUMMBL profile, repo directory, agent coordination surface, and collaboration router for the `hummbl-dev` account.

## Enhancement lanes

### 1. First-screen README polish

Add a high-signal opening block that immediately answers:

- What is HUMMBL?
- What should a visitor click first?
- What is ready to use today?
- What is research/candidate work?
- How can a human or agent contribute?

Suggested first-screen structure:

```md
# HUMMBL

Governance infrastructure for AI agents.

HUMMBL builds small, inspectable control-plane primitives for agentic systems: delegation tokens, append-only receipts, kill switches, circuit breakers, capability fences, source-verification gates, and review workflows that create evidence while the system runs.

## Start here

- Use runtime primitives: hummbl-governance
- Explore mental-model infrastructure: base120
- Review source-verification gates: evidence-gate
- Build MCP/agent surfaces: mcp-server and hummbl-agent
- Coordinate cross-repo work: hummbl-dev issues
```

### 2. Add explicit public collaboration section

Add a section explaining where outsiders should go:

- For bugs: open issues in target repo
- For broad ideas: GitHub Discussions where enabled
- For cross-repo proposals: open issue here
- For security: use `SECURITY.md`, not public issues
- For agent tasks: use `agent-handoff` issues

### 3. Add agent routing section

Add a small visible section for agents:

```md
## Agent routing

Agents should read `AGENTS.md` before making changes. Cross-repo or org-level work should be coordinated through issues in this repo. Repo-specific changes should happen in the target repo unless the task is explicitly about public profile, inventory, templates, or cross-repo governance.
```

### 4. Add repo maturity/status legend

Define status tags for public repos:

- active
- seed
- exploratory
- stable
- maintenance
- archived
- private/not-public

Then use those statuses in the repo directory or a linked inventory doc.

### 5. Add `*-as-code` public repo family once created

After agents create the seven public repos, add a `*-as-code` family section:

- governance-as-code
- agent-as-code
- policy-as-code
- protocol-as-code
- knowledge-as-code
- model-routing-as-code
- observability-as-code

Status should be `seed` until each repo has scope, README, license, and first issues.

### 6. Add profile CTA block

Add a concise call-to-action:

```md
## Work with HUMMBL

If you are building agentic systems and need runtime governance, source verification, auditability, or public/private agent workflow design, start with the repos above or contact reuben@hummbl.io.
```

### 7. Refresh inventory and metrics

The README currently says inventory was captured on 2026-07-03 but links to a historical May 2026 inventory. Agents should refresh the inventory or clearly mark what is current vs historical.

## Recommended new/updated files

- `README.md` — first-screen and routing improvements
- `docs/PUBLIC_COLLABORATION.md` — contributor and external collaboration routing
- `docs/AGENT_ROUTING.md` — org-level agent routing guidance
- `docs/REPO_MATURITY_MODEL.md` — repo status tags and expectations
- `.github/ISSUE_TEMPLATE/agent-handoff.md` — reusable agent handoff template
- `.github/ISSUE_TEMPLATE/cross-repo-proposal.md` — cross-repo proposal template

## Guardrails

- Preserve existing public/private boundary language.
- Do not add private repo details, secrets, internal receipts, or unverified claims.
- Do not imply HUMMBL/BaseN/Ownward candidates are canon unless already adopted elsewhere.
- Keep README concise; move details to docs.
- Prefer small PRs: one concern per PR.

## Acceptance criteria

- [ ] README first screen clearly explains HUMMBL and routes visitors.
- [ ] README includes clear human/agent collaboration path.
- [ ] README includes or links repo status/maturity definitions.
- [ ] `*-as-code` repo family is linked after the repos exist.
- [ ] Public/private boundary remains explicit.
- [ ] New docs/templates are linked from README or CONTRIBUTING.
