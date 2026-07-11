# Storage Hardening Execution Playbook v0.1

**Status: OPERATOR-OWNED EXECUTION PLAYBOOK — BLOCKED ON CREDENTIAL ROTATION**

Issue: hummbl-dev/hummbl-dev#144

## Executive summary

Most remaining risk is **execution gating**, not analysis quality. A plaintext credential on removable media blocks all destructive cleanup. Classification quality is ~92.6% with one known correction. The matrix is operationally ready.

## Current high-confidence findings

### Critical unresolved blocker (P0)

- `I:\claude api key for openresearch.sh.txt` (147 bytes) — exposed plaintext credential
- **All destructive cleanup BLOCKED until key rotation is completed and replacement is placed in secret manager**

### File-system corrections validated

- `D:\casper` — Ubuntu live installer payload (keep while boot media in use)
- `D:\pool` — Ubuntu installer apt pool with .deb files (keep)
- `D:\Temp` — 4 zero-byte placeholders (safe to clean, but classify as "delete placeholder contents")
- `C:\Users\Owner\PROJECTS` — 37.86 GB (not 43.35 GB)
- `.codex\worktrees` — 18 (not 46)
- USB credential file hash: agent scan had filename mismatch; actual file hash is authoritative

## Current state snapshot

- `C:` — critically full, cleanup pressure remains
- `D:` (UBUNTU-SERV, FAT32) — boot/installer + mixed workdirs
- `H:` (BIOS_FLASH, FAT32) — BIOS + MBP offload + credential risk
- `I:` (ANVIL_XFER, exFAT) — transfer archive target

### Largest confirmed on C:

- `AppData\Local\Docker` (very large, active runtime layer)
- `AppData\Local\wsl`
- `.cache/huggingface` model cache (Qwen3-8B, Qwen3-0.6B)
- `Downloads` and `.codex`

## Execution plan

### Phase 0 — Blocking prerequisite (OPERATOR-OWNED)

1. Rotate the exposed Claude API key in Anthropic Console
2. Store new key in approved secret manager (no local plaintext key files)
3. Confirm `I:\claude api key for openresearch.sh.txt` is absent before any destructive cleanup

**Gate:** Operator must complete Phase 0. Agent cannot rotate credentials.

### Phase 1 — Post-gate cleanup run

Only after Phase 0 is complete:

#### Keep for now (12 items)

| Path | Reason |
|------|--------|
| `D:\casper` | Installer payload |
| `D:\pool` | Installer payload |
| `C:\Users\Owner\PROJECTS` | Active project tree |
| `C:\Users\Owner\.codex` | Active agent workspaces |
| `C:\Users\Owner\AppData\Local\wsl` | Active WSL |
| `C:\Users\Owner\AppData\Local\Docker` | Active Docker |
| `C:\Users\Owner\AppData\Local\Temp` | Active temp |
| `.cache\huggingface\hub\models--Qwen--Qwen3-8B` | Active model |
| `.cache\huggingface\hub\models--Qwen--Qwen3-0.6B` | Active model |
| `D:` and `H:` | Until planned media rework |
| `I:` archive trees | Claude-vm_bundles, anvil-archives, backups, repo-audits, archives, scan-outputs, model-candidates |

#### Archive (move-first, delete-after-verify) (10 items)

| Path | Action |
|------|--------|
| `D:\agent-temp` | Archive |
| `D:\codex-review` | Archive |
| `D:\codex-packages` | Archive |
| `D:\PROJECTS-failed-worktrees` | Archive |
| `H:\mbp-offload-2026-04-17` | Archive (selected subtrees) |
| `H:\mbp-offload-2026-04-17\archive-bundle` | Archive |
| `H:\mbp-offload-2026-04-17\homebrew-downloads` | Archive |
| `Downloads\ableton_live_trial_12.4.2_64.zip` | Archive |
| `Downloads\Download 2026-06-15T00-51-11-964Z.zip` | Archive |
| `I:` empty placeholders (scratch, handoffs, filesystem-inventory) | Archive |

#### Delete (post-condition required) (3 items)

| Path | Condition |
|------|-----------|
| `I:\claude api key for openresearch.sh.txt` | Only after rotation (Phase 0) |
| `H:\mbp-offload-2026-04-17\downloads\a84e8cd1...zip` | After hash/context investigation |
| `D:\Temp` placeholder files | If confirmed unused |

### Phase 2 — Media reliability hardening

- Evaluate `D:` and `H:` filesystem format (FAT32 → exFAT or partition strategy)
- Only after all keep/archive/delete state is applied and validated
- Keep boot-capable data safe through staged backup and mount boot verification

## Verification requirements before closing

- [ ] Credential file absent from all USB drives
- [ ] Restore-verify for archived directories moved off D:/H:
- [ ] Free-space delta captured on C: and removable drives
- [ ] No high-value installer payload lost (D:\casper, D:\pool remain)
- [ ] Recovery evidence: manifest + checksums for all moved/deleted candidates

## Operational learning (6)

1. Keep an explicit execution gate for security-sensitive files
2. Never classify from naming alone; inspect content when payload risk is high
3. Keep keep/archive/delete with recovery for every item
4. Treat zero-byte placeholders as data points, not empty directories
5. Prioritize proof-first (size/owner/time/hash) before action
6. Separate analysis quality from execution dependency state

## Keep/archive/delete matrix summary

| Category | Count | Status |
|----------|-------|--------|
| Keep | 12 | Validated |
| Archive | 10 | Pending Phase 0 gate |
| Delete | 3 | Pending Phase 0 gate + hash investigation |
| **Total** | **25** | **Classification ~92.6% confidence** |

## Authority and fact posture

- This is an operator-owned execution playbook derived from issue #144
- Phase 0 is operator-only (credential rotation cannot be agent-executed)
- All destructive operations require explicit operator authorization
- No agent may execute Phase 1 or Phase 2 without operator approval

## Cross-repo dependencies

- None — this is a local operational playbook

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#144
- **Critical blocker**: 1 (P0 credential on removable media)
- **File-system corrections**: 6
- **Keep items**: 12
- **Archive items**: 10
- **Delete items**: 3
- **Operational learnings**: 6
- **Verification requirements**: 5
- **Classification confidence**: ~92.6%
- **Review status**: PENDING OPERATOR APPROVAL
