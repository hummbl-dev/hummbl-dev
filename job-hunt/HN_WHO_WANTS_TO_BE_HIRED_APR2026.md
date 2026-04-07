# HN "Who Wants to Be Hired" — April 2026

**Status**: DRAFT — Reuben must rewrite in own voice before posting
**Deadline**: April 1, 2026
**Thread**: https://news.ycombinator.com/item?id=PENDING (watch for new thread)

---

Location: Atlanta, GA | Remote (US) | Open to relocate

Technologies: Python (primary), Bash/Zsh, TypeScript, Go (learning). GitHub Actions, self-hosted runners, Tailscale, launchd, SQLite, MCP (Model Context Protocol). Bandit, Semgrep, pip-audit.

Resume: reuben@hummbl.io | github.com/foundermode-ai | hummbl.io

Looking for: Platform Engineering, SRE, AI Platform, AI Governance

I came to engineering from coaching -- strength and conditioning, 10 years, through a gold medal at Masters Worlds. Same principles transfer: assess constraints before prescribing solutions, build the safety infrastructure before the features, and manage change carefully because that's where things break.

For the last two years I've been building founder-mode, a multi-agent orchestration platform coordinating Claude, Codex, and Gemini across a 3-machine fleet. Everything runs on Python stdlib with zero third-party runtime deps. 14,900+ tests (89% coverage), 14 CI workflows on self-hosted runners, 10 MCP servers, 360 operator skills. The safety primitives are the interesting part: graduated kill switch (4 modes), circuit breakers on every external adapter, HMAC-SHA256 signed delegation tokens with chain depth enforcement, append-only hash-chained governance audit logging.

I've run 7 formal agent audit sessions -- agents that fabricated metrics 17x, violated scope boundaries, deleted other agents' work, bypassed hooks. Each incident became a machine-enforceable guardrail. That's the part I care about most: making AI systems trustworthy enough to actually deploy.

Published hummbl-governance on PyPI (stdlib-only, 476 tests, Arbiter A grade 99.5/100). Working on CCA-F certification. Submitted a response to OSTP's NIST AI RMF RFI.

I'm one of the first people to build an MCP server and publish custom Claude Code skills. I'm not a CS grad -- I have a BS in Health & Wellness and a decade of coaching. But I've been writing programs since I was 15, and I ship tested code every day.

reuben@hummbl.io

---

## Notes for Reuben

Per your AI application guidance: **read this draft, internalize the structure, then rewrite from scratch in your own words.** The final post should be yours, not this verbatim.

Key choices in this draft:
- Leads with coaching→engineering story (your differentiator)
- Numbers are specific and verifiable (no vague claims)
- Agent audit story is the hook (genuinely unusual, memorable)
- Honest about non-CS background, immediately followed by evidence of shipping
- ~265 words (HN sweet spot; longer posts get skipped)
- No "passionate about", "leverage", or "ecosystem"

## Links to include
- GitHub: https://github.com/foundermode-ai
- HUMMBL: https://hummbl.io
- PyPI: https://pypi.org/project/hummbl-governance/
- LinkedIn: (add your URL)
