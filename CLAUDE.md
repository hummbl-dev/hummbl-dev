# CLAUDE.md — hummbl-dev

Project guidance for Claude Code sessions on this repo. The user frequently works from their **phone**, so optimize every interaction for small diffs, concise output, and tap-friendly approvals. Full rationale and examples: [docs/mobile-coding-standards.md](docs/mobile-coding-standards.md).

## 1. How to behave on mobile

- Lead with the answer or action. Skip preamble and filler.
- Keep text output short. If one sentence works, don't write three.
- Prefer `AskUserQuestion` with 2–4 options over open-ended prose questions.
- Make small, focused changes — one concern per commit, one concern per PR.
- No drive-by refactors, no speculative abstractions, no unasked-for "improvements".
- Surface blockers early. Don't grind on a failing approach — diagnose, then ask.

## 2. Git / PR workflow

- **Never commit to `main`.** Work on a branch: `claude/<slug>` or `feat/<slug>`.
- One logical change per commit. Imperative subject, ≤ 70 chars.
- Keep diffs small — target **< 300 lines changed** per PR so they're reviewable on a phone.
- Open a PR **only when explicitly asked**. When asked:
  - Title: short (≤ 70 chars), no prefix noise.
  - Body: `## Summary` (1–3 bullets) + `## Test plan` (checklist). No walls of text.
- Push with `git push -u origin <branch>`. On network failure, retry up to 4× with exponential backoff (2s, 4s, 8s, 16s).

## 3. Communication rhythm

- Act on clearly scoped requests. Ask when scope is ambiguous.
- Status updates only at milestones: PR opened, CI green/red, blocker hit, task done.
- On CI failure or review comment: investigate → propose the fix → confirm before large changes.
- When uncertain about intent, ask **once** with tap-friendly options. Don't guess.
- Don't ask "should I proceed?" repeatedly — if the scope is clear, just go.

## 4. Security & safety guardrails

Never, without explicit in-session confirmation:

- Force-push to any branch (especially `main`).
- Run destructive ops: `git reset --hard`, `rm -rf`, `branch -D`, `push --force`, `checkout .`.
- Skip hooks (`--no-verify`) or bypass signing (`--no-gpg-sign`).
- Commit files that may contain secrets: `.env`, credentials, tokens, keys, `*.pem`.
- Modify git config, repo permissions, CI/CD workflows, or branch protection.
- Touch repositories outside the authorized scope (`hummbl-dev/hummbl-dev`).
- Create a PR the user didn't ask for.

If you're about to do any of the above, **stop and confirm first** — even if it seems implied.
