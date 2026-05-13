# HUMMBL

Governance infrastructure for AI agents.

HUMMBL builds small, inspectable control-plane primitives for agentic systems: delegation tokens, append-only receipts, kill switches, circuit breakers, capability fences, source-verification gates, and review workflows that create evidence while the system runs.

The bias is explicit:

- **libraries over platforms** — controls should live in the execution path, not only in a dashboard after the fact
- **receipts over vibes** — every governance claim should leave an audit trail
- **stdlib-first primitives** — core safety controls should survive constrained, regulated, and air-gapped environments
- **human override preserved** — automation assists governance; it does not become the sovereign

```bash
pip install hummbl-governance
```

[![PyPI](https://img.shields.io/pypi/v/hummbl-governance)](https://pypi.org/project/hummbl-governance/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)]()
[![Runtime deps](https://img.shields.io/badge/runtime%20deps-zero-brightgreen)]()

---

## Start Here

| Need | Repository |
|---|---|
| Runtime governance primitives | [`hummbl-governance`](https://github.com/hummbl-dev/hummbl-governance) |
| Mental-model substrate | [`base120`](https://github.com/hummbl-dev/base120) |
| Source-verification gate | [`evidence-gate`](https://github.com/hummbl-dev/evidence-gate) |
| Code quality and governance scoring | [`arbiter`](https://github.com/hummbl-dev/arbiter) |
| MCP access to HUMMBL models and skills | [`mcp-server`](https://github.com/hummbl-dev/mcp-server) |
| Agent orchestration patterns | [`hummbl-agent`](https://github.com/hummbl-dev/hummbl-agent) |
| Research and citation corpus | [`hummbl-bibliography`](https://github.com/hummbl-dev/hummbl-bibliography) |
| Public profile, tools, and repo inventory | [`hummbl-dev`](https://github.com/hummbl-dev/hummbl-dev) |

---

## Current Work

| Area | What is shipping |
|---|---|
| Agent governance | `hummbl-governance`, `agent-governance-demo`, `hummbl-agent`, `mcp-server` |
| Evidence and review | `evidence-gate`, `arbiter`, governed PR review protocols, source-verification rules |
| Cognitive substrate | `base120`, `hummbl-theory`, `hummbl-bibliography`, `arcana` |
| Operator infrastructure | `founder-mode`, `claude-config`, `hummbl-iac` |
| Product research | `fractional-bench`, `coaching`, `hummbl-production` |
| Experimental public repos | `autoresearch`, `governed-compression`, `sint-protocol`, `bif` |

Some repositories are private while they contain operator workflows, client-sensitive research, or active product work. Public repositories are the durable reference surface.

---

## What HUMMBL Means by Governance

Governance is not a policy PDF. It is a runtime property:

1. **Who is acting?** Agent identity, trust tier, and delegation scope.
2. **What authority do they have?** Signed capability tokens and bounded tools.
3. **What happened?** Append-only receipts, bus messages, and evidence logs.
4. **What should stop the system?** Kill switches, circuit breakers, cost governors, and review gates.
5. **What can be audited later?** Source manifests, PR reviews, test evidence, and structured findings.

That is the spine across the org: small primitives that make governance observable, testable, and reviewable.

---

## By The Numbers

Inventory captured on 2026-05-08:

| Metric | Count |
|---|---:|
| Total repositories | 54 |
| Active public repositories | 35 |
| Active private repositories | 17 |
| Archived repositories | 2 |
| Primary language family | Python-heavy, with TypeScript, HTML, Shell, TeX, Go templates, Java |

Latest repo inventory: [`docs/GITHUB_REPO_INVENTORY_2026-05-08.md`](docs/GITHUB_REPO_INVENTORY_2026-05-08.md)

Latest branch cleanup audit: [`docs/BRANCH_CLEANUP_AUDIT_2026-05-08.md`](docs/BRANCH_CLEANUP_AUDIT_2026-05-08.md)

---

## Research

HUMMBL's public thesis is that AI governance will move from abstract policy to runtime evidence. The research corpus tracks:

- AI-generated code risk and liability
- agentic control-plane design
- source verification before publication
- governance receipts and audit trails
- mental-model infrastructure for agent reasoning
- practical compliance mapping across NIST AI RMF, ISO 42001, EU AI Act, OWASP, and related frameworks

Useful entry points:

- [AI slop crisis research corpus](docs/research/ai-slop-crisis/README.md)
- [Why libraries, not platforms](docs/research/ai-slop-crisis/essays/why-libraries-not-platforms.md)
- [Reasonable care in the age of AI agents](docs/research/ai-slop-crisis/essays/reasonable-care-age-of-agents.md)
- [The observability argument](docs/research/ai-slop-crisis/essays/the-observability-argument.md)

---

## Tools

Free self-assessments and references:

| Tool | Purpose |
|---|---|
| [Tool index](index.html) | Landing page for the public tools in this repo |
| [EU AI Act readiness](eu-ai-act-readiness.html) | Governance posture check |
| [NIST AI RMF readiness](nist-ai-rmf-readiness.html) | Framework-aligned assessment |
| [ISO 42001 readiness](iso-42001-readiness.html) | AI management system checklist |
| [Singapore agentic AI readiness](singapore-agentic-readiness.html) | Agent governance architecture assessment |
| [Colorado AI Act readiness](colorado-ai-act-readiness.html) | State-level algorithmic decision compliance |
| [Compliance calendar](compliance-calendar.html) | AI governance timeline |
| [Governance crosswalk](governance-crosswalk.html) | Framework comparison |

---

## CI Posture

This repository is the HUMMBL organization profile, public documentation surface, and static tool portfolio. It does not currently run GitHub Actions because there is no build step, package release, or testable runtime in this repo.

Validation is manual for now:

- Review Markdown changes in rendered GitHub preview.
- Open changed HTML tools locally in a browser before publication.
- Keep executable code, packages, and service workflows in their dedicated project repositories, where CI is configured per repo.

If this repository gains generated assets, JavaScript modules, or release automation, add the smallest useful CI workflow for that surface.

---

## Contact

HUMMBL, LLC is founded by **Reuben Bowlby** in Atlanta, GA.

- Site: [hummbl.io](https://hummbl.io)
- Email: reuben@hummbl.io
- Package: [`hummbl-governance` on PyPI](https://pypi.org/project/hummbl-governance/)

*Governed agents need receipts, not slogans.*
