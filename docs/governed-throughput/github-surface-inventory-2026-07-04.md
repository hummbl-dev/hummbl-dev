# GitHub Surface Inventory - 2026-07-04

Issue: hummbl-dev/hummbl-dev#57

This inventory maps public `hummbl-dev/*` repositories that can inherit or override the default `.github` substrate proposed in hummbl-dev/hummbl-dev#56 and hummbl-dev/.github#17.

## Scope And Privacy Boundary

- Source of truth: live `gh repo list hummbl-dev --limit 300` plus GitHub git tree API checks on each public repository default branch.
- Public repo names are listed because this document is committed to the public `hummbl-dev/hummbl-dev` repo.
- Private repository names are intentionally not listed here. Live access showed 72 non-public repos; those require a private follow-up inventory artifact or private issue.
- Empty repositories or repositories without a default branch could not be path-inspected and should be treated as `needs-human-review` if they become active.

## Summary

- Total accessible repos: 144
- Public repos inventoried by name: 72
- Non-public repos held out of this public table: 72
- Public repos with `.github/`: 33
- Public repos with non-native `github/`: 0
- Public repos with local issue templates: 15
- Public repos with local PR templates: 13
- Public repos with local workflows: 25
- Public repos with CODEOWNERS: 19
- Public override risk: High 18, Medium 16, Low 38

## Recommended Pilot Repos

- `hummbl-dev/.github`: default substrate implementation for issue forms, PR template, and report-only checks.
- `hummbl-dev/hummbl-dev`: public command surface and receipt home.
- `hummbl-dev/hummbl-agent`: public runtime/product-style repo with existing local GitHub surface.
- `hummbl-dev/governance-as-code`: docs/governance source-adapter style pilot that currently inherits defaults.
- `hummbl-dev/compendium-as-code`: new source-adapter repo; useful for validating candidate/source boundary fields before broad rollout.

## Inventory

| Repo | Visibility | Archived | Fork | Has `.github/` | Has `github/` | Local issue templates | Local PR template | Workflows | CODEOWNERS path | Override risk | Recommended action |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| [-](https://github.com/hummbl-dev/-) | PUBLIC | True | False | False | False | False | False | False | - | Low | `needs-human-review` |
| [.github](https://github.com/hummbl-dev/.github) | PUBLIC | False | False | True | False | True | False | False | CODEOWNERS | High | `compose-governed-template` |
| [adversary-emulation-playbook](https://github.com/hummbl-dev/adversary-emulation-playbook) | PUBLIC | True | False | True | False | False | False | True | - | Medium | `needs-human-review` |
| [agent-as-code](https://github.com/hummbl-dev/agent-as-code) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [agent-control-plane-patterns](https://github.com/hummbl-dev/agent-control-plane-patterns) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [agent-evaluation-patterns](https://github.com/hummbl-dev/agent-evaluation-patterns) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [agent-governance-demo](https://github.com/hummbl-dev/agent-governance-demo) | PUBLIC | True | False | True | False | True | True | True | .github/CODEOWNERS | High | `needs-human-review` |
| [agent-handoffs](https://github.com/hummbl-dev/agent-handoffs) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [agent-instruction-format](https://github.com/hummbl-dev/agent-instruction-format) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [agent-runtime-governance](https://github.com/hummbl-dev/agent-runtime-governance) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [agentic-eng-patterns](https://github.com/hummbl-dev/agentic-eng-patterns) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [ai-source-verification](https://github.com/hummbl-dev/ai-source-verification) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [arbiter](https://github.com/hummbl-dev/arbiter) | PUBLIC | False | False | True | False | False | True | True | .github/CODEOWNERS<br>CODEOWNERS | High | `compose-governed-template` |
| [autoresearch](https://github.com/hummbl-dev/autoresearch) | PUBLIC | True | True | False | False | False | False | False | - | Low | `needs-human-review` |
| [autoresearch-reports](https://github.com/hummbl-dev/autoresearch-reports) | PUBLIC | True | False | True | False | False | False | True | - | Medium | `needs-human-review` |
| [autoresearch-win-rtx](https://github.com/hummbl-dev/autoresearch-win-rtx) | PUBLIC | True | False | True | False | False | False | False | CODEOWNERS | Medium | `needs-human-review` |
| [awesome-ai-agents](https://github.com/hummbl-dev/awesome-ai-agents) | PUBLIC | True | True | False | False | False | False | False | CODEOWNERS | Medium | `needs-human-review` |
| [awesome-ai-agents-1](https://github.com/hummbl-dev/awesome-ai-agents-1) | PUBLIC | True | True | True | False | False | True | True | - | High | `needs-human-review` |
| [awesome-ai-agents-2026](https://github.com/hummbl-dev/awesome-ai-agents-2026) | PUBLIC | True | True | False | False | False | False | False | - | Low | `needs-human-review` |
| [awesome-python](https://github.com/hummbl-dev/awesome-python) | PUBLIC | True | True | True | False | False | True | True | - | High | `needs-human-review` |
| [base120](https://github.com/hummbl-dev/base120) | PUBLIC | False | False | True | False | False | False | True | .github/CODEOWNERS<br>CODEOWNERS | Medium | `preserve-local-overrides` |
| [bif](https://github.com/hummbl-dev/bif) | PUBLIC | False | False | True | False | False | False | True | .github/CODEOWNERS | Medium | `preserve-local-overrides` |
| [CL4R1T4S](https://github.com/hummbl-dev/CL4R1T4S) | PUBLIC | True | True | False | False | False | False | False | - | Low | `needs-human-review` |
| [claim-evidence-ledger](https://github.com/hummbl-dev/claim-evidence-ledger) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [cli](https://github.com/hummbl-dev/cli) | PUBLIC | True | True | True | False | True | False | True | - | High | `needs-human-review` |
| [compendium-as-code](https://github.com/hummbl-dev/compendium-as-code) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [compliance-as-code](https://github.com/hummbl-dev/compliance-as-code) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [deer-flow](https://github.com/hummbl-dev/deer-flow) | PUBLIC | True | True | True | False | True | False | True | - | High | `needs-human-review` |
| [docs](https://github.com/hummbl-dev/docs) | PUBLIC | False | False | True | False | False | False | False | .github/CODEOWNERS | Medium | `preserve-local-overrides` |
| [evidence-gate](https://github.com/hummbl-dev/evidence-gate) | PUBLIC | True | False | True | False | False | False | True | - | Medium | `needs-human-review` |
| [execution-receipts](https://github.com/hummbl-dev/execution-receipts) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [founder-mode-showcase](https://github.com/hummbl-dev/founder-mode-showcase) | PUBLIC | True | False | False | False | False | False | False | - | Low | `needs-human-review` |
| [G0DM0D3](https://github.com/hummbl-dev/G0DM0D3) | PUBLIC | True | True | False | False | False | False | False | - | Low | `needs-human-review` |
| [governance-as-code](https://github.com/hummbl-dev/governance-as-code) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [governed-compression](https://github.com/hummbl-dev/governed-compression) | PUBLIC | False | False | True | False | False | False | True | CODEOWNERS | Medium | `preserve-local-overrides` |
| [hermes-agent](https://github.com/hummbl-dev/hermes-agent) | PUBLIC | True | True | True | False | True | True | True | - | High | `needs-human-review` |
| [homebrew-hummbl](https://github.com/hummbl-dev/homebrew-hummbl) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [homebrew-tap](https://github.com/hummbl-dev/homebrew-tap) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [hummbl-agent](https://github.com/hummbl-dev/hummbl-agent) | PUBLIC | False | False | True | False | False | False | True | .github/CODEOWNERS | Medium | `preserve-local-overrides` |
| [hummbl-bibliography](https://github.com/hummbl-dev/hummbl-bibliography) | PUBLIC | False | False | True | False | True | True | True | .github/CODEOWNERS<br>CODEOWNERS | High | `compose-governed-template` |
| [hummbl-dev](https://github.com/hummbl-dev/hummbl-dev) | PUBLIC | False | False | True | False | True | True | False | .github/CODEOWNERS<br>CODEOWNERS | High | `compose-governed-template` |
| [hummbl-governance](https://github.com/hummbl-dev/hummbl-governance) | PUBLIC | False | False | True | False | True | True | True | .github/CODEOWNERS<br>CODEOWNERS | High | `compose-governed-template` |
| [hummbl-papers](https://github.com/hummbl-dev/hummbl-papers) | PUBLIC | False | False | True | False | False | False | True | .github/CODEOWNERS<br>CODEOWNERS | Medium | `preserve-local-overrides` |
| [hummbl-toolkit](https://github.com/hummbl-dev/hummbl-toolkit) | PUBLIC | False | False | True | False | False | False | False | .github/CODEOWNERS<br>CODEOWNERS | Medium | `preserve-local-overrides` |
| [HUMMBL-Unified-Tier-Framework](https://github.com/hummbl-dev/HUMMBL-Unified-Tier-Framework) | PUBLIC | True | False | True | False | True | True | True | .github/CODEOWNERS | High | `needs-human-review` |
| [infrastructure-as-code](https://github.com/hummbl-dev/infrastructure-as-code) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [knowledge-as-code](https://github.com/hummbl-dev/knowledge-as-code) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [L1B3RT4S](https://github.com/hummbl-dev/L1B3RT4S) | PUBLIC | True | True | False | False | False | False | False | - | Low | `needs-human-review` |
| [markitdown](https://github.com/hummbl-dev/markitdown) | PUBLIC | True | True | True | False | False | False | True | - | Medium | `needs-human-review` |
| [mcp-server](https://github.com/hummbl-dev/mcp-server) | PUBLIC | False | False | True | False | True | True | True | .github/CODEOWNERS<br>CODEOWNERS | High | `compose-governed-template` |
| [mintlify-docs](https://github.com/hummbl-dev/mintlify-docs) | PUBLIC | False | False | True | False | False | False | False | .github/CODEOWNERS | Medium | `preserve-local-overrides` |
| [model-routing-as-code](https://github.com/hummbl-dev/model-routing-as-code) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [NATURALIS-FUTURA](https://github.com/hummbl-dev/NATURALIS-FUTURA) | PUBLIC | True | True | False | False | False | False | False | - | Low | `needs-human-review` |
| [nix](https://github.com/hummbl-dev/nix) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [OBLITERATUS](https://github.com/hummbl-dev/OBLITERATUS) | PUBLIC | True | True | False | False | False | False | False | - | Low | `needs-human-review` |
| [observability-as-code](https://github.com/hummbl-dev/observability-as-code) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [open_teamsuzie](https://github.com/hummbl-dev/open_teamsuzie) | PUBLIC | True | True | True | False | False | False | True | - | Medium | `needs-human-review` |
| [packages](https://github.com/hummbl-dev/packages) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [paramiko](https://github.com/hummbl-dev/paramiko) | PUBLIC | True | True | True | False | True | False | False | - | High | `needs-human-review` |
| [policy-as-code](https://github.com/hummbl-dev/policy-as-code) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [protocol-as-code](https://github.com/hummbl-dev/protocol-as-code) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [Real-Time-Voice-Cloning](https://github.com/hummbl-dev/Real-Time-Voice-Cloning) | PUBLIC | True | True | True | False | False | False | True | - | Medium | `needs-human-review` |
| [research-source-packets](https://github.com/hummbl-dev/research-source-packets) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [rich](https://github.com/hummbl-dev/rich) | PUBLIC | True | True | True | False | True | True | True | - | High | `needs-human-review` |
| [scoop-bucket](https://github.com/hummbl-dev/scoop-bucket) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [security-as-code](https://github.com/hummbl-dev/security-as-code) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |
| [sint-protocol](https://github.com/hummbl-dev/sint-protocol) | PUBLIC | True | True | True | False | True | False | True | - | High | `needs-human-review` |
| [skills](https://github.com/hummbl-dev/skills) | PUBLIC | True | True | False | False | False | False | False | - | Low | `needs-human-review` |
| [ST3GG](https://github.com/hummbl-dev/ST3GG) | PUBLIC | True | True | False | False | False | False | False | - | Low | `needs-human-review` |
| [V3SP3R](https://github.com/hummbl-dev/V3SP3R) | PUBLIC | True | True | True | False | True | True | False | - | High | `needs-human-review` |
| [vllm](https://github.com/hummbl-dev/vllm) | PUBLIC | True | True | True | False | True | True | True | .github/CODEOWNERS | High | `needs-human-review` |
| [winget-manifests](https://github.com/hummbl-dev/winget-manifests) | PUBLIC | False | False | False | False | False | False | False | - | Low | `inherit-defaults` |

## Follow-Up

- Do not mass-edit local `.github/` directories from this inventory alone.
- Create the default substrate PR in `hummbl-dev/.github` first, then use this table to decide which public repos inherit defaults and which need local composition.
- Run a private inventory for the non-public repos before any private repo rollout; do not copy private repo names into public coordination docs.
- Treat archived repos as `needs-human-review` before changing them; many are forks or historical public surfaces.
