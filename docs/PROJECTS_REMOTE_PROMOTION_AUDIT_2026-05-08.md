# PROJECTS Remote Promotion Audit — 2026-05-08

## Scope

Read-only audit of immediate children under the local Windows `PROJECTS`
directory.
The audit looks for local project directories that either lack a git remote or
lack a git repository but appear to be durable HUMMBL work.

No repositories were created, deleted, or force-pushed during this audit.

## High-Priority Promotion Candidates

| Local path | Current state | Evidence | Recommendation |
|---|---|---|---|
| `PROJECTS\hummbl-bki` | Git repo, no remote, dirty | `main`, head `cbbb407`, 4 dirty entries | Create private `hummbl-dev/hummbl-bki` or Gitea `HUMMBL/hummbl-bki`; clean/commit evidence docs first. |
| `PROJECTS\hummbl-learning-mechanics` | Git repo, no remote, dirty | `main`, head `4eb57eb`, 1 untracked paper text file | Create private research repo after deciding whether the paper text is licensed/cache-only. |
| `PROJECTS\hummbl-fractional-bench` | Not a git repo; GitHub repo exists as `hummbl-dev/fractional-bench` | 36 local files; GitHub private repo verified | Reconcile local folder against `hummbl-dev/fractional-bench`; replace with clone or migrate unique local files through PR. |
| `PROJECTS\hummbl-ani` | Not a git repo | 5 files, HUMMBL-named docs scaffold | Initialize/promote if this is an active primitive; otherwise archive as local concept note. |
| `PROJECTS\hummbl-physical-ai` | Not a git repo | 19 files with `src`, `tests`, `examples` | Initialize/promote; this has code-shaped structure and should not stay filesystem-only if active. |

## Medium-Priority Candidates

| Local path | Current state | Evidence | Recommendation |
|---|---|---|---|
| `PROJECTS\agent-tools` | Git repo, no remote, dirty/uncommitted initial tree | No commits; 5 untracked entries including Rust/Go code | Create private repo only after secret/license scan and first intentional commit. |
| `PROJECTS\cscs-prep` | Git repo, no remote, dirty; contains personal certification PDFs | `master`, head `6040e04`, 6 dirty entries | Do not push to HUMMBL org by default; if backed up, use a private personal repo or encrypted storage. |

## Already Covered Or Not Promotion Targets

- `PROJECTS\crab` has GitHub remote `hummbl-dev/crab`.
- `PROJECTS\hummbl-bus` has Gitea remote `HUMMBL/hummbl-bus`; separate promotion work is active.
- `PROJECTS\arcana`, `founder-mode`, `hummbl-governance`, `hummbl-production`,
  `hummbl-tuples`, and most `hummbl-*` package repos already have GitHub or
  Gitea remotes.
- `_archive`, `_audits`, `_reviews`, `_worktrees`, and other underscore-prefixed
  directories are operating surfaces, not repo-promotion candidates by default.

## Follow-Up Order

1. `hummbl-bki`: high value and already referenced by promoted architecture docs.
2. `hummbl-fractional-bench`: resolve local non-git folder vs live GitHub repo.
3. `hummbl-physical-ai`: code-shaped and at risk of becoming invisible work.
4. `hummbl-learning-mechanics`: research value, but check source/licensing first.
5. `hummbl-ani`: decide active primitive vs archive.
6. `agent-tools`: secret/license scan before first remote.
7. `cscs-prep`: keep personal/private; avoid HUMMBL org unless there is a business reason.

## Required Guardrails Before Promotion

- Run a secret scan before creating or pushing a new remote.
- Preserve dirty work; do not auto-commit user/agent changes without review.
- Prefer private GitHub/Gitea by default for research and internal IP.
- Use branch/PR for any migration into an existing remote.
- Record the destination remote and first pushed commit in this file or successor audit.
