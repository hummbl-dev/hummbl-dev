# Phase 3 — hummbl-agent-gateway Sprint Plan
### Secure multi-channel agent messaging built on HUMMBL governance primitives
### Date: 2026-04-05 · Owner: Reuben Bowlby · Duration: 6 weeks

---

## Strategic context

OpenClaw was frozen 2026-03-22 (API keys rotated, Node.js gateways retired). It
provided multi-channel messaging (Signal, WhatsApp, Discord, Telegram) for
agents, but carried security risks: shared credentials, no per-agent scoping,
no audit trail, centralized compromise surface.

The pattern still has market demand. HUMMBL has the primitives to ship a
secure replacement. This phase builds it as an **OSS reference implementation**
(not a commercial platform) — preserves the primitives-first positioning from
the /method manifesto while giving the market something runnable.

Decision made (2026-04-05, Q5 resolution): build inside the existing
`hummbl-dev/hummbl-agent` repo, not a new repo. hummbl-agent is already scoped
as "governed agent execution infrastructure, deterministic control plane,
dispatch-only" — a gateway subsystem composes naturally.

---

## Goal

Ship `hummbl-agent-gateway` as a subsystem inside `hummbl-agent` that:

- Routes outbound agent messages through signed, scoped, auditable channels
- Ships with 2 production channel adapters (Discord, Telegram) at launch
- Wraps every channel through hummbl-governance primitives (delegation
  tokens, governance bus, kill switch, circuit breaker)
- Runs as a single Python process / single Docker container
- Publishes one public blog post + one demo video at launch

## Success criteria (day 42)

**Must ship**:
- [ ] `hummbl-agent/gateway/` subsystem merged to main
- [ ] Discord adapter — sending + receiving works
- [ ] Telegram adapter — sending + receiving works
- [ ] CLI: register agent, issue token, send message, tail bus
- [ ] End-to-end example: agent A sends Discord message using token, bus
      records the event, kill switch halts the channel
- [ ] README + quickstart that a fresh user can follow in 15 minutes
- [ ] Dockerfile + docker-compose.yml for the gateway
- [ ] Public announcement (blog post + 1 demo video)

**Stretch**:
- [ ] Signal adapter (via signal-cli JSON-RPC)
- [ ] WhatsApp adapter (stub, not production-ready)
- [ ] Integration with Founder Gateway (dogfood)

**Not in scope**:
- Inbound webhook ingestion from external services (future)
- Managed/hosted version
- Web UI (CLI only)
- Payment rails

---

## Architecture — where it lives

```
hummbl-agent/
├── agents/                     # Existing agent definitions
├── gateway/                    # NEW — the gateway subsystem
│   ├── __init__.py
│   ├── core.py                 # Gateway class, message dispatch loop
│   ├── registry.py             # Agent identity registry (per-agent credentials)
│   ├── policy.py               # Per-channel allowlists, scope enforcement
│   ├── cli.py                  # gateway CLI entry points
│   └── adapters/
│       ├── __init__.py
│       ├── base.py             # AbstractAdapter interface
│       ├── discord.py          # Discord Webhook + Bot adapter
│       ├── telegram.py         # Telegram Bot API adapter
│       └── signal.py           # (stretch) signal-cli JSON-RPC adapter
├── tests/
│   └── gateway/
│       ├── test_core.py
│       ├── test_registry.py
│       ├── test_policy.py
│       └── test_adapters/
├── examples/
│   └── gateway/
│       ├── quickstart.py       # 30-line Hello World
│       └── docker-compose.yml
└── docs/
    └── gateway/
        ├── README.md
        ├── architecture.md
        ├── adapters.md
        └── quickstart.md
```

### Core abstractions

```python
# gateway/core.py
class Gateway:
    def __init__(
        self,
        registry: AgentRegistry,
        bus: BusWriter,
        kill_switch: KillSwitch,
        adapters: dict[str, Adapter],
        token_manager: DelegationTokenManager,
    ): ...

    def send(
        self,
        *,
        from_agent: str,
        channel: str,
        recipient: str,
        message: str,
        token: DelegationToken,
    ) -> SendReceipt:
        # 1. Validate token (scope includes "send:{channel}")
        # 2. Check kill switch (halt if engaged)
        # 3. Resolve channel circuit breaker
        # 4. Dispatch to adapter
        # 5. Post result to governance bus
        # 6. Return receipt

# gateway/adapters/base.py
class Adapter(Protocol):
    name: str
    def send(self, recipient: str, message: str) -> AdapterResult: ...
    def healthcheck(self) -> bool: ...
```

### Security model

| Concern | Mechanism |
|---------|-----------|
| Per-agent authority | `DelegationToken` with scope `send:discord`, `send:telegram:@channel`, etc. |
| Credential isolation | Adapters read secrets from env vars per-channel; no shared root creds |
| Audit trail | Every `Gateway.send()` call writes to `BusWriter` before and after adapter dispatch |
| Incident response | `KillSwitch` checked before every send; engage halts fleet in <2s |
| Channel degradation | Per-adapter `CircuitBreaker` opens on N failures, degrades gracefully |
| Token compromise | Tokens are HMAC-signed + expiring; compromise is contained |

---

## Week-by-week breakdown

### Week 1 (Apr 6-12) — Scaffold + Discord adapter

**Monday-Wednesday**:
- Create `gateway/` package structure
- Write `Gateway` class skeleton with `send()` method
- Write `AgentRegistry` (JSON-backed, file persistence)
- Write `AbstractAdapter` protocol
- Wire kill switch + governance bus checks into `send()`

**Thursday-Friday**:
- Implement Discord adapter (Discord Webhook API — simplest starting point)
- Write 15 tests covering happy path + token rejection + kill-switch-engaged + circuit-breaker-open
- Write `send_discord_message.py` example

**Deliverable**: `python -m hummbl_agent.gateway send --channel discord --recipient webhook-url --message "hello"` works.

### Week 2 (Apr 13-19) — Telegram adapter + CLI

**Monday-Tuesday**:
- Implement Telegram adapter (Telegram Bot API via stdlib `urllib`)
- Add Telegram-specific policy (channel allowlist, bot token per-adapter)
- 10 tests

**Wednesday-Friday**:
- Build CLI: `register-agent`, `issue-token`, `send`, `tail-bus`, `kill-switch`
- Write README quickstart (15-minute walkthrough)
- Docker image: single-binary-style Python container

**Deliverable**: quickstart works end-to-end. Fresh user can send a Discord + Telegram message in 15 minutes.

### Week 3 (Apr 20-26) — Hardening + policy

**Monday-Tuesday**:
- Per-channel policy enforcement (allowlist recipients, max message size, rate limits)
- Delegation token validation tightening (issuer verification, resource selectors)
- Token revocation mechanism

**Wednesday-Thursday**:
- Governance bus schema for gateway events (`message.send`, `message.reject`, `channel.opened`, `channel.closed`, `token.issued`, `token.revoked`)
- Bus query tools (filter by agent, by channel, by time window)

**Friday**:
- Security audit: threat-model the gateway, run Bandit + Semgrep, document findings

**Deliverable**: a design partner could run this in prod with reasonable safety expectations.

### Week 4 (Apr 27-May 3) — Docs + examples

**Monday-Tuesday**:
- Architecture doc (`docs/gateway/architecture.md`)
- Adapter-author guide (`docs/gateway/adapters.md`) — how to write a new adapter
- Quickstart doc (`docs/gateway/quickstart.md`)

**Wednesday-Thursday**:
- 3 worked examples:
  1. Minimal hello-world (single send, no governance)
  2. Multi-agent coordination (2 agents sharing a channel with scoped tokens)
  3. Incident drill (engage kill switch, observe graceful halt)
- docker-compose.yml with example services

**Friday**:
- Internal dogfood: replace Founder Gateway with hummbl-agent-gateway for HUMMBL's own messaging

**Deliverable**: documentation + examples ready for public consumption.

### Week 5 (May 4-10) — Signal adapter (stretch) + integration

**Monday-Wednesday** (stretch goal):
- Signal adapter via signal-cli JSON-RPC (reuses existing nodezero signal-cli infrastructure)
- 8 tests

**Thursday-Friday**:
- Integration smoke tests: Gateway + hummbl-governance + hummbl-agent together
- Fix whatever dogfooding surfaced last week
- Launch checklist assembly

**Deliverable**: Signal adapter optional-but-working; integration tests pass.

### Week 6 (May 11-17) — Launch

**Monday-Tuesday**:
- Blog post draft: "Secure multi-channel agent messaging, as a 300-line Python library"
- Demo video recording (asciinema or screencast, 3-5 minutes)
- hummbl.io updates: add gateway to primitives index, update MCP-attestation primitive if relevant

**Wednesday**:
- Final README polish, LICENSE check, version bump
- Push to main, tag `v0.1.0-gateway`

**Thursday**:
- Publish blog post on hummbl.io/blog
- Post to HN, Reddit (r/LocalLLaMA, r/selfhosted), X/Twitter, LinkedIn
- Submit to Python Weekly, TLDR Newsletter

**Friday**:
- Buffer day for fixes, issue triage, responses
- Metrics baseline capture (pre-announcement download count for comparison)

**Deliverable**: launched. Public announcement shipped. Metrics collection started.

---

## Risks + mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Scope creep (adding Signal + WhatsApp delays core) | High | Medium | Hard-constrain Weeks 1-4 to Discord + Telegram. Signal is stretch. WhatsApp explicitly out. |
| Discord/Telegram API changes mid-sprint | Low | Medium | Use official SDK-free HTTP calls; pin API versions in adapter code |
| hummbl-governance v0.2.0 API mismatch | Low (just verified) | High | Pin `hummbl-governance>=0.2.0,<0.3.0` in pyproject; test imports on Week 1 Day 1 |
| Signal adapter nodezero dependency introduces infrastructure load | Medium | Low | Make Signal adapter optional (extras), document nodezero requirement separately |
| Consulting revenue pressure mid-sprint | Medium | High | Timebox to 60% of working hours; consulting work preserved in parallel |
| Launch falls flat (no stars, no interest) | Medium | Medium | Have plan to write 3 follow-up blog posts in weeks 7-10 to sustain attention |
| Security vulnerability in an adapter | Low | High | Require token validation, rate-limit, and Bandit/Semgrep scan as CI gates |
| Dogfooding reveals architecture mismatch with Founder Gateway | Medium | Medium | Dogfood in Week 4, not at launch; architect migration path in Week 5 if needed |

---

## Decision points / gates

**End of Week 1 (Apr 12)** — Gate 1:
- Is the `Gateway.send()` abstraction correct? If not, refactor before Week 2.
- Does Discord adapter work end-to-end with real Discord?
- **Go/no-go**: proceed to Telegram (go) vs refactor core (no-go)

**End of Week 2 (Apr 19)** — Gate 2:
- Do 2 adapters + CLI + docker-compose give a genuinely usable product?
- Can a fresh user (not Reuben) actually follow the quickstart?
- **Go/no-go**: proceed to hardening (go) vs extend core another week (no-go)

**End of Week 4 (May 3)** — Gate 3:
- Does the dogfooding run reveal blockers?
- Is documentation ready for public read?
- **Go/no-go**: proceed to Signal adapter (go), OR skip stretch and do final polish (no-go)

**End of Week 5 (May 10)** — Gate 4:
- Launch-ready checklist complete?
- **Go/no-go**: launch next week (go), OR push launch 1 week for polish (no-go)

---

## Open questions requiring human judgment

1. **Is 60% working-hours allocation realistic?** Consulting obligations need to be real-scheduled against this sprint, not assumed-away.

2. **Does Founder Gateway dogfood have blocking dependencies?** (e.g., does Founder Gateway carry state that hummbl-agent-gateway can't reproduce?)

3. **Which launch channel gets the most attention?** HN vs Python Weekly vs direct to hummbl.io subscribers. If no mailing list yet, HN is the default.

4. **Who's the first design partner?** Ideally someone with a real agent-messaging need who can run v0.1.0 and give feedback in weeks 7-8.

5. **Brand: is "hummbl-agent-gateway" the final name?** Alternatives: `hummbl-gateway`, `hummbl-dispatch`, `hummbl-channels`. Name affects PyPI registration, docs URLs.

---

## Metrics to track (baseline → launch+30 days)

| Metric | How measured | Target by May 17 |
|--------|--------------|-------------------|
| hummbl-governance PyPI downloads/week | pypistats | 2x current baseline |
| hummbl-agent GitHub stars | gh api | +15 from current |
| hummbl-agent-gateway issues opened | gh issues | 3-5 (signal of real use) |
| Blog post traffic | Cloudflare Analytics | 500+ uniques first week |
| Discovery calls booked citing gateway | cal.com notes | 2+ |

**Kill criterion**: if metrics haven't moved by day 30 post-launch (June 17), treat the primitives-first thesis as invalidated and replan.

---

## Why this is the right next phase

- **Closes the "primitives are abstract" credibility gap**: primitive pages describe ideas; a running gateway demonstrates them in composition
- **Creates distribution flywheel**: every gateway runner imports hummbl-governance, raising its download count
- **Doesn't stack dependencies**: unlike Defense/Federal (partner + credit), this requires only Reuben's focused time
- **Preserves positioning**: OSS reference implementation, not a platform product, matches /method manifesto
- **Answers "market asking for secure-OpenClaw"**: directly, with something runnable in 6 weeks

## Why 6 weeks, not 4 or 12

- **4 weeks is too aggressive** for solo founder carrying consulting obligations; leaves no buffer for integration surprises or documentation polish
- **12 weeks is too long** — risk of losing momentum, market moves, primitives-first thesis stays unvalidated
- **6 weeks matches observed velocity**: this session shipped 9 PRs + ~45 page touches in a day of focused work; a 6-week sprint at ~50% allocation produces ~30 days of effort, comparable to prior HUMMBL delivery cycles

---

## Dependencies (must be true at Week 1 Day 1)

- [ ] hummbl-governance v0.2.0 stable on PyPI (confirmed 2026-04-05)
- [ ] hummbl-agent main branch green (check before Week 1 Monday)
- [ ] Discord bot + webhook for dev/test account (Reuben creates Monday AM)
- [ ] Telegram bot token for dev/test (Reuben creates Monday AM)
- [ ] Consulting calendar cleared to 60% for 6 weeks (decision by Reuben)

---

## Launch artifacts (produced by Week 6)

1. `hummbl-agent/gateway/` subsystem (code, tests, examples)
2. `docs/gateway/README.md` + quickstart + architecture
3. Dockerfile + docker-compose.yml
4. Blog post: "Secure multi-channel agent messaging" (hummbl.io/blog)
5. Demo video: 3-5 minute asciinema screencast
6. hummbl.io updates: /primitives/ linking to gateway, /blog post
7. PyPI release: hummbl-agent v0.X (if packaged separately), OR hummbl-governance v0.3 with gateway extras
8. Tag: `hummbl-agent/v0.1.0-gateway`
9. Changelog entry in hummbl-agent CHANGELOG.md

---

## Immediate next actions (this week, before Week 1 starts)

1. **Reuben**: confirm 60% allocation for 6 weeks
2. **Reuben**: create Discord test bot + webhook, Telegram bot, capture tokens
3. **Reuben**: finalize brand name (hummbl-agent-gateway vs alternatives)
4. **Claude**: if authorized, open `feat/claude/gateway-scaffold` branch on hummbl-agent
   and commit the `gateway/` package skeleton + abstract adapter interface + first 5 tests
5. **Claude**: draft the launch blog post during Week 6 prep, not on launch day

---

*Plan based on: Q5 strategic decision (2026-04-05 session), hummbl-governance
v0.2.0 verified API surface, /method manifesto positioning, OpenClaw freeze
post-mortem, and observed delivery velocity from Phase 0-2c site work.*

*Next plan review: end of Week 1 (2026-04-12) at Gate 1 decision point.*
