# Archived Stylized Repo Classification - 2026-07-04

Issue: [#42](https://github.com/hummbl-dev/hummbl-dev/issues/42)

This memo classifies the archived public stylized-name repo cluster so searched public profile, archive, and inventory surfaces do not treat these repositories as active HUMMBL products or unexplained operational artifacts.

## Summary

| Repository | Disposition | Public-surface treatment |
|---|---|---|
| [`G0DM0D3`](https://github.com/hummbl-dev/G0DM0D3) | Archived public fork/import evidence archive; experimental chat interface artifact | Do not list as active HUMMBL product. Retain only as archived historical evidence unless separately reviewed. |
| [`CL4R1T4S`](https://github.com/hummbl-dev/CL4R1T4S) | Archived public fork/import evidence archive; system-prompt transparency corpus artifact | Do not list as active HUMMBL product. Treat as sensitive public-surface evidence, not active doctrine. |
| [`L1B3RT4S`](https://github.com/hummbl-dev/L1B3RT4S) | Archived public fork/import evidence archive; prompt/jailbreak-corpus artifact | Do not list as active HUMMBL product. Treat as high brand/context-risk archive content. |
| [`OBLITERATUS`](https://github.com/hummbl-dev/OBLITERATUS) | Archived public fork/import evidence archive; model-abliteration/HF-space artifact | Do not list as active HUMMBL product. Treat as experimental security-adjacent archive content. |
| [`ST3GG`](https://github.com/hummbl-dev/ST3GG) | Archived public fork/import evidence archive; steganography toolkit artifact | Do not list as active HUMMBL product. Treat as security-adjacent archive content. |
| [`V3SP3R`](https://github.com/hummbl-dev/V3SP3R) | Archived public fork/import evidence archive; AI/Flipper control artifact | Do not list as active HUMMBL product. Treat as security-adjacent archive content. |

## Evidence

Live GitHub metadata checked on 2026-07-04:

| Repository | Visibility | Archived | Fork | Default branch | Disk usage | License | Description signal |
|---|---|---:|---:|---|---:|---|---|
| `hummbl-dev/G0DM0D3` | public | yes | yes | `main` | 435 KB | AGPL-3.0 | "LIBERATED AI CHAT" |
| `hummbl-dev/CL4R1T4S` | public | yes | yes | `main` | 755 KB | AGPL-3.0 | "LEAKED SYSTEM PROMPTS..." |
| `hummbl-dev/L1B3RT4S` | public | yes | yes | `main` | 1019 KB | AGPL-3.0 | "TOTALLY HARMLESS LIBERATION PROMPTS..." |
| `hummbl-dev/OBLITERATUS` | public | yes | yes | `main` | 608 KB | AGPL-3.0 | "OBLITERATE THE CHAINS THAT BIND YOU" |
| `hummbl-dev/ST3GG` | public | yes | yes | `main` | 2844 KB | AGPL-3.0 | "All-in-one steganography suite" |
| `hummbl-dev/V3SP3R` | public | yes | yes | `main` | 41943 KB | AGPL/GPL family signal | "AI Flipper control" |

The repository README excerpts show upstream or experimental positioning, not HUMMBL-maintained product, public collaboration, or governance primitive positioning.

Existing repo-local evidence:

- `docs/ARCHIVE_POSTURE_2026-05-13.md` already classifies `CL4R1T4S`, `ST3GG`, `OBLITERATUS`, `G0DM0D3`, `V3SP3R`, and `L1B3RT4S` as public historical evidence or experimental named repos.
- `docs/GITHUB_REPO_INVENTORY_2026-05-08.md` lists several of the repos in a historical inventory table.

Search command:

```text
rg -n "G0DM0D3|CL4R1T4S|L1B3RT4S|OBLITERATUS|ST3GG|V3SP3R" README.md docs .github governance -S
```

Within the searched surfaces, references appear in archive posture, historical inventory, planning material, and this #42 classification work. They are not listed in the active README "Start Here" routing surface.

## Decision

Classify all six repos as archived public fork/import evidence archives with brand and security-adjacent public-surface risk.

They should not be linked from active-product lists, "Start Here" surfaces, agent task routing surfaces, or current HUMMBL product narratives. If they remain visible in inventory, use `archived`, `fork/import`, and `historical evidence` boundary language.

## Brand and Risk Posture

The risk is not that archived repos exist. The risk is ambiguity: stylized names and security-adjacent README language can be mistaken for current HUMMBL positioning.

Accepted current posture:

- Leave archived repos archived.
- Do not promote them as current products.
- Preserve historical/evidence value unless the operator chooses future archive, rename, visibility, or boundary-file work.
- Do not make archive/delete/rename changes from this memo alone.

## Agent Routing

Agents should not file active product, security-tooling, prompt-corpus, or steganography work in these archived repos by default.

Use one of these routes instead:

- Public profile or inventory hygiene: `hummbl-dev/hummbl-dev`.
- Current agent runtime work: `hummbl-dev/hummbl-agent`.
- Security-sensitive findings: follow `SECURITY.md`; do not use public issues for sensitive details.
- Cross-repo public-surface proposal: `hummbl-dev/hummbl-dev` using the cross-repo proposal template.

## Follow-Up

- A future fork-boundary sweep can add minimal archived-repo boundary notes inside each retained fork.
- A future public-surface review can decide whether any repo should be renamed, made private, or retained as-is.
- No archive/delete/rename action is recommended from this memo alone.
