# AGENTS.md

Agent guidance for hummbl-dev.

## Identity & Purpose

This repo is the operator workflow surface for AI-assisted edits. It is not the public starting point for contributors and it is not HUMMBL product or governance canon. The operator frequently works from their **phone**, so optimize every interaction for small diffs, concise output, and tap-friendly approvals.

## Agent Role

Agents working in this repository are responsible for:
- Making small, focused changes (one concern per commit)
- Keeping text output short and concise
- Leading with the answer or action, skipping preamble
- Making small diffs (< 300 lines changed per PR)
- Surface blockers early and ask when scope is ambiguous
- Acting on clearly scoped requests

## Session Rules

1. **Mobile-first behavior**: Lead with the answer, skip preamble, keep text short
2. **Small diffs**: Target < 300 lines changed per PR for phone reviewability
3. **One concern per commit**: Imperative subject, ≤ 70 chars
4. **Never commit to main**: Work on a branch: `agent/<slug>` or `feat/<slug>`
5. **AskUserQuestion preference**: Prefer 2–4 options over open-ended prose questions
6. **No drive-by refactors**: No speculative abstractions, no unasked-for improvements
7. **Surface blockers early**: Don't grind on failing approaches — diagnose, then ask

## Security & Safety Guardrails

Never, without explicit in-session confirmation:
- Force-push to any branch (especially `main`)
- Run destructive ops: `git reset --hard`, `rm -rf`, `branch -D`, `push --force`, `checkout .`
- Skip hooks (`--no-verify`) or bypass signing (`--no-gpg-sign`)
- Commit files that may contain secrets: `.env`, credentials, tokens, keys, `*.pem`
- Modify git config, repo permissions, CI/CD workflows, or branch protection
- Touch repositories outside the authorized scope (`hummbl-dev/hummbl-dev`)
- Create a PR the user didn't ask for

## Branching and Commit Conventions

- Branch naming: `agent/<slug>` or `feat/<slug>`
- Commit format: Conventional Commits, imperative subject, ≤ 70 chars
- Merge strategy: squash-merge to `main`; rebase locally before PR
- CI must be green before merge; no direct pushes to `main`

## Multi-Agent Coordination

Agents coordinate via the coordination bus for:
- Mobile coding workflow updates
- Small diff notifications
- Blocker alerts
- PR review requests

Bus identity: `ai-steward` (no parentheticals)

## Conventions

- **Mobile-first**: Optimize for phone interaction
- **Small diffs**: Target < 300 lines changed per PR
- **Concise output**: If one sentence works, don't write three
- **Ask once**: When uncertain about intent, ask once with tap-friendly options

## Off-limits

- Never commit to `main` directly — PRs only
- Never create a PR the user didn't ask for
- Never force-push without explicit confirmation
