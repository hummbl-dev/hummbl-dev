# Repo Candidate Creation Packets

Status: planning packets. Not authorization to create repos.

Source issue: `hummbl-dev#86`

These packets cover the first-wave candidates selected in `docs/repo-map.md`.
Each candidate still requires a fresh namespace check immediately before repo
creation.

| Candidate | Boundary | Status | Current decision |
| --- | --- | --- | --- |
| `agent-receipts` | public | seed | prepare with naming-risk note |
| `claim-as-code` | public | seed | prepare |
| `hummbl-cookbook` | public | seed | prepare |
| `public-collaboration-kernel` | public | seed | prepare |
| `source-candidate-registry` | public | seed | prepare |

Namespace checks run on 2026-07-04:

- `hummbl-dev/agent-receipts`: available under `hummbl-dev`; public exact-name
  collisions exist outside the org.
- `hummbl-dev/claim-as-code`: available under `hummbl-dev`; no exact public
  search result found in the bounded check.
- `hummbl-dev/hummbl-cookbook`: available under `hummbl-dev`; no exact public
  search result found in the bounded check.
- `hummbl-dev/public-collaboration-kernel`: available under `hummbl-dev`; no
  exact public search result found in the bounded check.
- `hummbl-dev/source-candidate-registry`: available under `hummbl-dev`; no exact
  public search result found in the bounded check.

Do not treat this receipt as durable. Repeat checks immediately before creation.
