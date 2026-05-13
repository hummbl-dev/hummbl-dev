# HUMMBL Archived Repository Posture

Snapshot date: 2026-05-13

Archived repositories remain visible for traceability, historical evidence, and third-party fork provenance. Fleet agents should not treat archived repositories as stale active work unless a human explicitly reactivates them.

## Archive classes

| Class | Meaning | Default action |
| --- | --- | --- |
| Canonical replacement exists | Active successor repository exists or the work moved into another HUMMBL repo. | Link to the successor; do not reopen the archive. |
| Historical evidence | Repository records prior experiments, names, or research trails. | Preserve unless a human approves export/delete. |
| Third-party fork cache | Archived fork or import of upstream software. | Preserve as read-only provenance; do not issue maintenance tasks. |
| Delete/export candidate | Repository appears safe to export or remove after owner review. | Requires owner approval before destructive action. |

## Current archived repositories

| Repository | Visibility | Archive class | Notes |
| --- | --- | --- | --- |
| `autoresearch` | Public | Canonical replacement exists | Prefer `autoresearch-pipeline` and active research repos for new work. |
| `autoresearch-win-rtx` | Public | Historical evidence | Windows/RTX research runtime snapshot; do not treat as active CI work. |
| `Real-Time-Voice-Cloning` | Public | Third-party fork cache | Archived upstream/cache surface. |
| `sint-protocol` | Public | Historical evidence | Experimental protocol work. |
| `deer-flow` | Public | Third-party fork cache | Archived upstream/cache surface. |
| `cli` | Public | Third-party fork cache | Archived upstream/cache surface. |
| `paramiko` | Public | Third-party fork cache | Archived upstream/cache surface. |
| `rich` | Public | Third-party fork cache | Archived upstream/cache surface. |
| `vllm` | Public | Third-party fork cache | Archived upstream/cache surface. |
| `skills` | Public | Canonical replacement exists | Prefer active skills/config repos. |
| `markitdown` | Public | Third-party fork cache | Archived upstream/cache surface. |
| `hummbl-assurance` | Private | Canonical replacement exists | Governance assurance work moved into active governance/evidence surfaces. |
| `CL4R1T4S` | Public | Historical evidence | Experimental named repo. |
| `ST3GG` | Public | Historical evidence | Experimental named repo. |
| `OBLITERATUS` | Public | Historical evidence | Experimental named repo. |
| `G0DM0D3` | Public | Historical evidence | Experimental named repo. |
| `V3SP3R` | Public | Historical evidence | Experimental named repo. |
| `NATURALIS-FUTURA` | Public | Historical evidence | Experimental named repo. |
| `L1B3RT4S` | Public | Historical evidence | Experimental named repo. |
| `hummbl-asi` | Private | Historical evidence | Private research snapshot; owner review required before any export/delete action. |

## Agent handling rules

- Do not create CI, dependency, license, branch-protection, or stale-branch issues against archived repositories.
- If an archived repo appears in a scan, route the finding to this posture document instead of opening repo-local work.
- If an archived repo contains sensitive or legally relevant material, escalate to a human owner rather than modifying visibility or contents.
- If an archived repo should become active again, unarchive it first and then apply the active-repo baseline.
