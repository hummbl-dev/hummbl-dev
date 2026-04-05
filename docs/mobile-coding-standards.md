# Mobile Coding Standards

Standards for working on `hummbl-dev` (and collaborating with Claude Code) when the user is on a **phone**. The concise enforceable version lives in [`../CLAUDE.md`](../CLAUDE.md) at the repo root and is auto-loaded into every Claude session. This document is the longer narrative with rationale and examples.

## Why mobile-first standards?

A phone is a narrow, slow review surface. Scrolling a 500-line diff, reading long AI explanations, or typing a detailed correction is painful. So the workflow has to bias toward things the user can approve with a **tap**:

- Small diffs that fit on a screen.
- Short status messages.
- Structured yes/no or multiple-choice questions.
- PRs reviewed on GitHub's mobile app.
- Reversible actions by default.

Anything that forces the user to type a long message, scroll a long diff, or undo a mistake is a failure of the workflow.

---

## 1. How Claude should behave on mobile

### Output style
- Lead with the answer or action. No "I'll now..." preamble.
- One-sentence answers when one sentence works.
- Use markdown lists and headings sparingly — phones render them fine, but noise is noise.
- Reference file paths as `path/file.md:42` so the user can tap to navigate.

### Change sizing
- **One concern per change.** If a bug fix reveals surrounding cruft, note it — don't silently clean it up.
- No speculative abstractions, no "while I'm here" refactors, no extra configurability.
- If a task genuinely needs multiple changes, split it: multiple commits, or multiple PRs.

### Clarification style
- Prefer `AskUserQuestion` with 2–4 options over free-form questions. Tapping is faster than typing.
- Ask **once**, not iteratively. Bundle the ambiguities you see.
- If the scope is clear, don't ask — just do it and report.

### When to escalate
- If an approach fails, diagnose first. Read the error. Check assumptions. Try one focused fix.
- If still stuck after investigation, escalate with `AskUserQuestion` — not by retrying blindly and not by abandoning after one failure.

---

## 2. Git / PR workflow from a phone

### Branching
- `main` is protected. Never commit to it directly.
- Branch names: `claude/<slug>` for Claude-authored work, `feat/<slug>` or `fix/<slug>` for user-led work.
- One branch per logical unit of work.

### Commits
- Imperative subject, ≤ 70 chars. Example: `Add mobile coding standards`.
- Body explains **why**, not what (the diff shows what).
- One logical change per commit. Prefer new commits over `--amend`.
- Never stage with `git add -A` / `git add .` — add files by name to avoid accidentally committing secrets or junk.

### PRs
- **Open only when explicitly asked.** Don't surprise the user with a PR.
- Target **< 300 lines changed** per PR. Phone review breaks down past that.
- Template:
  ```markdown
  ## Summary
  - <1–3 bullets: what and why>

  ## Test plan
  - [ ] <how to verify, if applicable>
  ```
- Title: short, no noise prefixes, ≤ 70 chars.

### Pushing
- `git push -u origin <branch>` every time.
- On network failure: retry up to 4× with exponential backoff (2s, 4s, 8s, 16s).
- Never `push --force` to shared branches.

---

## 3. Communication & review rhythm

### When to act vs. ask
- **Clearly scoped request →** act, then report.
- **Ambiguous scope →** ask once with options.
- **Risky / irreversible action →** always confirm, even if it seems implied.

### Status updates
Send updates only at natural milestones:
- Branch created / PR opened (with link).
- CI green or red (with what failed).
- Blocker hit (with the specific obstacle and options).
- Task complete.

Not every tool call needs narration. Silence is fine between milestones.

### Responding to CI / review comments
1. Investigate the failure or comment.
2. Form a specific fix proposal.
3. If the fix is small and obvious → make it, report briefly.
4. If the fix is architectural or ambiguous → ask first with options.

### Asking questions
Good (tap-friendly):
> Where should the config live?
> 1. Repo root as `.mobilerc`
> 2. `docs/mobile-config.md`
> 3. Both

Bad (requires typing):
> Can you tell me more about what you want the config to do and where you'd like it?

---

## 4. Security & safety guardrails

These are **hard rules**. Never do any of them without explicit in-session confirmation from the user:

| Category | Prohibited without confirmation |
|---|---|
| Destructive git | `git reset --hard`, `push --force`, `branch -D`, `checkout .`, `clean -f`, `rebase -i` |
| Filesystem | `rm -rf`, overwriting uncommitted work, deleting untracked files |
| Integrity | `--no-verify`, `--no-gpg-sign`, amending pushed commits |
| Secrets | committing `.env`, credentials, tokens, keys, `*.pem`, `*.key` |
| Config | modifying `.git/config`, branch protection, CI/CD workflows, repo permissions |
| Scope | touching any repo other than `hummbl-dev/hummbl-dev` |
| Automation | creating PRs/issues/comments the user didn't ask for |

**Rule of thumb:** if undoing it would require the user to type on their phone, confirm first.

---

## Related

- [`../CLAUDE.md`](../CLAUDE.md) — auto-loaded concise version
- [`../README.md`](../README.md) — repo overview
- [`github-audit.md`](github-audit.md) — GitHub config audit
- [`repo-decisions.md`](repo-decisions.md) — repo-level decisions
