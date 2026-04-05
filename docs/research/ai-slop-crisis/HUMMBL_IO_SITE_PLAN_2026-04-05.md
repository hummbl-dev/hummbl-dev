# hummbl.io — Full Site Plan
### Positioning, IA, content, execution sequence
### Date: 2026-04-05

> Synthesizes: 16-doc research corpus + customer-perspective review + competitor audit (7 sites) + reference-site audit (8 sites) + hummbl.io deep audit (14 pages visited, 11 expected 404s found).

---

## PART I — SITUATION

### What's broken today

**11 expected pages return 404**: `/about`, `/contact`, `/team`, `/security`, `/privacy`, `/terms`, all 5 per-framework readiness pages (eu-ai-act-readiness.html, colorado-ai-act-readiness.html, iso-42001-readiness.html, nist-ai-rmf-readiness.html, singapore-agentic-readiness.html). A governance company with no `/security` page is itself ironic and buyer-killing.

**Pricing contradicts itself on 3 pages**:
- `/services`: Readiness Audit **$2–5K** | Retainer **$3–5K/mo**
- `/consulting`: Readiness Audit **$5–15K** | Retainer **$5–15K/mo**
- `/pricing`: "Arbiter Report" **$500** | Retainer not listed

A CISO comparing pages will not trust either number.

**5 pages render "Loading..."**: `/blog`, `/cases`, `/explorer`, `/compliance`, `/status` — JS-dependent with no static fallback. If JS fails or is slow, prospects see a broken page.

**6 overlapping audit names** with no map: Free Audit, Arbiter Report, Verified Memo, Readiness Audit, Free Gap Assessment, Discovery Call.

**Nav link "Audits" points to a 404.**

**Stale content**: Changelog last touched Feb 24 (6 weeks ago). Vendor count: 5 vs 6 (conflicting). Agent count: 12 vs 60+ vs 66 (unexplained).

### What the research corpus says to do

- **Defense/Federal is the sharpest wedge** — structural market opening (commercial SaaS can't touch IL4/IL5), contract-blocking urgency (DIBCAC flagging unmanaged Copilot as CMMC L2 finding)
- **HUMMBL's categorical differentiation**: library-not-platform, stdlib-only, open-source, air-gap-capable. *None* of the 10 competitors ship governance primitives as libraries.
- **Legal positioning**: "Caremark affirmative defense, NIST AI RMF conformance record, reasonable-care evidence pack generated at runtime."
- **Insurance angle**: Berkley D&O AI exclusions make governance a CFO/GC buyer, not just CISO.
- **SWE-bench inversion** (Claude Opus 4.6: 79.3% Verified, 29.2% vulnerable code): empirical destruction of "better models will fix it."

### What competitors and reference sites say to do

**Competitor category white space (Lane α)**: No site in the AI governance category combines **self-serve pricing** with **governance positioning**. Every vendor either (a) hides pricing behind "contact sales" OR (b) is a dev-first tool that doesn't lead with governance.

**Reference emulation target (Lane γ)**: **Supabase**. It is the closest structural match — open-source-first, primitive-oriented, developer-led self-serve with legitimate enterprise upsell. Linear is the closest aesthetic reference; Supabase is the closest GTM reference.

**5 reference-site patterns to adopt**:
1. Install snippet in the hero (`pip install hummbl-governance` in first viewport)
2. Live GitHub star badge in nav (once stars > ~1k)
3. Primitive-as-product naming (each primitive gets its own page)
4. Fully public tiered pricing with calculator (no sales gate until enterprise)
5. Opinionated `/method` page (Linear's most-linked artifact)

---

## PART II — POSITIONING DECISION

### Primary positioning (site-wide)

> **"Governance primitives for AI-native teams. Stdlib-only. Open source. Import from PyPI."**

**Why this wins**:
- **Fills the white space**: governance category + self-serve pricing + library distribution — nothing in the market combines all three
- **Structural differentiation**: the 10 funded competitors are all closed-source SaaS. HUMMBL is categorically different, not incrementally better.
- **Developer-first funnel**: matches Supabase template, matches HUMMBL's actual delivery model
- **Honest to the product**: HUMMBL really is stdlib-only, really is open source, really does ship on PyPI

### Secondary positioning (solutions-page tier)

**Defense & Federal** is the sharpest vertical wedge per Round 5 research. Gets its own `/solutions/defense-federal` page with CMMC 2.0 mapping, IL4/IL5 claim, air-gap capable.

**Regulated Industries** (healthcare, finance) as a second solutions page — compound compliance messaging.

**AI-Native Teams** as the third solutions page — the developer-first default buyer.

### Retired positioning

- ❌ "Structured reasoning for AI agents" (vague, two-product-stapled hero)
- ❌ "66 Agent Identities" (unexplained vanity metric)
- ❌ "5 Vendor Runtimes" (not buyer-relevant)
- ❌ Multi-framework readiness assessment positioning as primary (this is a lead-magnet, not the product)

---

## PART III — INFORMATION ARCHITECTURE

### New navigation structure

```
Primary nav (desktop):
  Primitives ▾    Solutions ▾    Docs    Pricing    Blog    GitHub

Primitives dropdown:
  / Governance Bus
  / Kill Switch
  / Circuit Breaker
  / Delegation Tokens (IDP)
  / Delegation Context (DCTX)
  / Base120 Models
  (See all primitives →)

Solutions dropdown:
  / Defense & Federal
  / Regulated Industries (healthcare, finance)
  / AI-Native Teams
  / Agent Platforms

Footer:
  Product: Primitives, Docs, Pricing, Changelog, Status
  Company: About, Blog, Method, Careers, Contact
  Trust: Security, Privacy, Terms, Compliance
  Developers: GitHub, PyPI, MCP Server, API Reference
  Community: Twitter/X, LinkedIn
```

### Page inventory — what exists, what gets built, what gets killed

**KEEP + rewrite** (7 pages):
- `/` homepage
- `/pricing`
- `/docs`
- `/blog`
- `/explorer` (Base120 model browser — keep as primitive demo)
- `/services` → rename `/solutions`
- `/compliance-calendar` (keep as lead-magnet)

**BUILD NEW** (16 pages):
- `/primitives` (index)
- `/primitives/governance-bus`
- `/primitives/kill-switch`
- `/primitives/circuit-breaker`
- `/primitives/delegation-tokens`
- `/primitives/delegation-context`
- `/primitives/base120` (repositioned from standalone)
- `/solutions` (index)
- `/solutions/defense-federal` ⭐ priority wedge
- `/solutions/regulated-industries`
- `/solutions/ai-native-teams`
- `/solutions/agent-platforms`
- `/method` (manifesto/thesis)
- `/about`
- `/security`
- `/legal` (privacy + terms combined, or split)

**FIX 404s** (5 framework readiness pages):
- Either build the 5 readiness pages (eu-ai-act, colorado-ai-act, iso-42001, nist-ai-rmf, singapore-agentic) OR remove the 404-producing links
- Recommend: **build them, because they're lead magnets that directly drive discovery-call bookings**

**KILL** (content consolidation):
- `/audits.html` (redirect to `/solutions`)
- Dual service catalogs (consolidate to one)
- "Arbiter Report / Free Audit / Verified Memo" taxonomy (replace with single audit ladder)
- `/consulting.html` if it exists separately from `/services`

---

## PART IV — HOMEPAGE REDESIGN

### Hero section (above fold)

```
┌──────────────────────────────────────────────────────┐
│  [eyebrow] OPEN SOURCE · STDLIB-ONLY · MIT LICENSE   │
│                                                       │
│  Governance primitives for                           │
│  AI-native teams.                                    │
│                                                       │
│  Delegation tokens, governance buses, kill switches, │
│  and circuit breakers. As Python packages.           │
│  Import from PyPI. Run anywhere — including          │
│  air-gapped and IL4/IL5.                             │
│                                                       │
│  $ pip install hummbl-governance                     │
│  [Copy]                                              │
│                                                       │
│  [Start Building →]   [★ 1.2k stars on GitHub]       │
└──────────────────────────────────────────────────────┘
```

**Metric bar directly below hero** (credibility anchor):

```
  476 tests · 20 modules · 0 runtime deps · MIT · PyPI
```

### Section 2: The Primitives (grid of 6)

Each primitive rendered as a card with:
- Icon
- Name
- One-line description
- 3-line code snippet (real)
- "Learn more →" link

```
┌────────────────┬────────────────┬────────────────┐
│ Governance Bus │ Kill Switch    │ Circuit Breaker│
│ ─────────────  │ ──────────     │ ──────────     │
│ Append-only    │ 4-mode halt    │ CLOSED/HALF/   │
│ audit log.     │ for emergency  │ OPEN state for │
│ Assessor-      │ response.      │ resilient      │
│ readable.      │                │ agents.        │
│                │                │                │
│ from hummbl_   │ ks.engage(     │ cb.call(       │
│  governance    │   HALT_ALL,    │   adapter,     │
│  import Bus    │   reason="…"   │   timeout=30)  │
│ bus.write(…)   │ )              │                │
│                │                │                │
│ Learn more →   │ Learn more →   │ Learn more →   │
└────────────────┴────────────────┴────────────────┘
┌────────────────┬────────────────┬────────────────┐
│ Delegation     │ Delegation     │ Base120        │
│ Tokens (IDP)   │ Context (DCTX) │ Models         │
│ ──────────     │ ──────────     │ ──────────     │
│ HMAC-SHA256    │ Chain-depth    │ 120 canonical  │
│ signed capa-   │ enforcement    │ mental models  │
│ bility tokens  │ for scoped     │ for agents.    │
│ with scope.    │ delegation.    │                │
│                │                │                │
│ dct = DCT.     │ dctx = DCTX(   │ model = b120.  │
│  issue(scope,  │   parent=tok,  │  get("P1")     │
│  depth=2)      │   max_depth=3) │                │
│                │                │                │
│ Learn more →   │ Learn more →   │ Learn more →   │
└────────────────┴────────────────┴────────────────┘
```

### Section 3: The Thesis (2-sentence manifesto)

```
AI generation is commoditizing. Governance isn't.

Every vendor will have an AI coder. Differentiation accrues to
the layer that enforces policy, tracks provenance, and maintains
accountability at runtime. That's us.

[Read the method →]
```

### Section 4: Solutions (3 cards, solutions-page links)

```
[Defense & Federal]    [Regulated Industries]    [AI-Native Teams]
 CMMC 2.0, IL4/IL5,     Healthcare, Finance —     Startup to scale:
 air-gap capable.       HIPAA, FINRA, SOC 2.      agent governance
                                                   that ships.
```

### Section 5: Proof / trust signals

```
  • 14,400+ tests across the founder-mode platform
  • 11 active CI workflows (security, mutation, contract validation)
  • 2+ years of production operation
  • Zero third-party runtime dependencies
```

### Section 6: Pricing teaser

```
  Open source forever.
  Enterprise support starts at $100/month.

  [See pricing →]
```

### Section 7: Footer CTA

```
  Ship governed agents in an afternoon.

  $ pip install hummbl-governance
  [Start Building →]
```

---

## PART V — CONTENT: KEY NEW PAGES

### `/method` — The Manifesto

**Title**: *Governance primitives, not governance platforms*

**Structure**:
1. **The observation**: Every AI governance company is building a dashboard. We're building a library.
2. **Why**: You can't audit a SaaS dashboard your assessor can't run. You can't deploy a cloud platform into IL5.
3. **The thesis**: Governance belongs in the runtime, not in a separate plane.
4. **The primitives**: What we ship and why each one is load-bearing.
5. **The compact**: What we won't do (dashboards, vendor lock-in, cloud-only, proprietary formats).

This page becomes Linear-style most-linked artifact, cited in every blog post, every pitch, every sales conversation.

### `/solutions/defense-federal` — Primary Wedge

**Title**: *AI governance for classified and controlled workloads*

**Structure**:
1. **The problem**: DIBCAC now flags unmanaged Copilot/Claude as CMMC Level 2 findings. Commercial AI governance SaaS cannot touch IL4/IL5.
2. **Our approach**: Stdlib-only Python packages. Zero runtime dependencies. Deployable into every classification level your other workloads deploy into.
3. **CMMC 2.0 mapping**: One-to-one table (CMMC practice ID → HUMMBL primitive)
4. **Evidence artifacts**: Append-only JSONL governance bus → grep-readable by your DIBCAC assessor
5. **The pricing**: $150K-$300K ACV mid-tier primes. Hybrid platform + per-agent metering + assessor-readiness assist.
6. **The call**: Book a 30-min CMMC gap review.

### `/solutions/regulated-industries`

Compound compliance framing (HIPAA + FDA + FINRA + SOC 2 + NIST AI RMF stack). Pitch: "You have five compliance regimes. AI governance is the sixth. Here's how ours composes."

### `/about`

Minimum viable:
- Reuben Bowlby bio + headshot
- HUMMBL LLC registration
- Timeline (2024: production Claude systems → 2026: governance primitives)
- "What we believe" (3 bullets from `/method`)

### `/security`

Table stakes for governance product:
- Responsible disclosure policy
- security.txt
- Vulnerability reporting: security@hummbl.io
- security-hardening practices (stdlib-only, no runtime deps, SBOM available)
- SOC 2 Type II status ("in progress" is acceptable)

### Each primitive page (6 pages, same template)

```
# [Primitive Name]

[One-line hook]

## What it does
[2-3 paragraphs]

## Install

$ pip install hummbl-governance

## Use it

[~15-line runnable example]

## When to reach for it
[3-4 bullets: specific scenarios]

## The contract
[Schema / API surface]

## See also
[Links to related primitives]
```

---

## PART VI — EXECUTION SEQUENCE

### Phase 0 — Stop the bleeding (today, ~2 hours)

**Objective**: No more obviously broken things on production. Trust leaks closed.

| Task | Est | Why |
|------|-----|-----|
| Fix 404 on `/audits` nav link (redirect to /services) | 10m | Broken nav kills credibility |
| Consolidate pricing to ONE canonical source (kill 2 of 3 pricing statements) | 30m | Three prices = zero trust |
| Update "7,700+ tests" → "14,400+ tests" site-wide | 15m | Stale numbers |
| Remove or update Singapore deadline (Jan 22, 2026 is in the past) | 5m | Factual error |
| Add minimal static fallback to Loading... pages OR temporarily remove them from nav | 45m | JS-dependent broken pages |
| Explain "Arbiter" wherever it's first referenced (one-line definition) | 10m | Unknown acronym |
| Remove "66 Agent Identities" metric or explain it | 5m | Unexplained vanity metric |
| Delete/redirect `/consulting.html` if it conflicts with `/services` | 10m | Duplicate catalog |

### Phase 1 — Build foundational pages (day 2, ~1 day)

| Task | Est | Why |
|------|-----|-----|
| Write + ship `/about` (founder bio, HUMMBL LLC, timeline) | 1h | CISO diligence requirement |
| Write + ship `/security` (security.txt, disclosure policy, SOC 2 status) | 1h | Table stakes for gov product |
| Write + ship `/legal` (privacy, terms) — basic templates | 1h | Legal basics |
| Build the 5 framework readiness pages (or kill the dead links) | 2-3h | Currently 404ing, used in funnels |
| Write + ship `/method` manifesto | 2h | Most-cited artifact |

### Phase 2 — Restructure IA + hero (day 3-4, ~2 days)

| Task | Est | Why |
|------|-----|-----|
| Implement new nav (Primitives/Solutions/Docs/Pricing/Blog/GitHub) | 2h | IA is current #1 issue |
| Rewrite homepage hero per Supabase template (install snippet + metric bar) | 3h | Positioning shift |
| Build `/primitives` index page | 1h | New IA node |
| Build 6 primitive pages (use template) | 1 day | Core new content |
| Build `/solutions` index page | 1h | New IA node |

### Phase 3 — The wedge (day 5-6, ~2 days)

| Task | Est | Why |
|------|-----|-----|
| Write + ship `/solutions/defense-federal` with CMMC mapping table | 4h | **Sharpest wedge per research** |
| Write + ship `/solutions/regulated-industries` | 2h | Secondary vertical |
| Write + ship `/solutions/ai-native-teams` | 2h | Default dev buyer |
| Integrate research talking points across site (Caremark, insurance, SWE-bench inversion) | 2h | Research → content delivery |

### Phase 4 — Polish + trust signals (day 7, ~0.5 day)

| Task | Est | Why |
|------|-----|-----|
| Add GitHub stars badge to nav (dynamic or static) | 30m | Reference pattern |
| Add changelog + keep it warm (last entry within 2 weeks) | 1h | Freshness signal |
| Add customer logos OR named design partners once you have them | - | Pending first customers |
| Add responsible-disclosure badge from security researchers | 30m | If any |
| Add `humans.txt` (small signal of care) | 15m | Polish |

### Phase 5 — Post-launch (week 2+)

- First 3 blog posts (already-written research corpus makes this cheap):
  - "The SWE-bench inversion: why better models won't fix your AI vulnerabilities"
  - "Caremark defense for AI: runtime audit trails as affirmative defense"
  - "Why we ship governance as a library, not a platform"
- First named design partner case study
- SOC 2 Type II engagement kickoff (if not started)

---

## PART VII — THE SPEC DOC

### Hero copy (exact — ready to paste)

```
EYEBROW (small, uppercase, spaced):
OPEN SOURCE · STDLIB-ONLY · MIT LICENSE

H1:
Governance primitives for
AI-native teams.

SUB:
Delegation tokens, governance buses, kill switches, and circuit
breakers. As Python packages. Import from PyPI. Run anywhere —
including air-gapped and IL4/IL5.

CODE BLOCK:
$ pip install hummbl-governance

CTA 1: [Start Building →]  (scrolls to /primitives)
CTA 2: [★ {dynamic} stars on GitHub]  (links to repo)

METRIC BAR (below fold transition):
476 tests · 20 modules · 0 runtime deps · MIT · PyPI
```

### Pricing — the canonical table

Replace all 3 pricing statements with this single table:

| Tier | For | Price | What's in |
|------|-----|-------|-----------|
| **Open Source** | Anyone | $0 | All primitives, all tests, MIT license, community support |
| **Team** | 2-10 person teams | **$100/mo** | Everything in OSS + priority email support + private Slack + monthly office hours |
| **Business** | 10-100 person teams | **$1,000/mo** | Everything in Team + SLA + dedicated Slack + 2 advisory calls/mo |
| **Enterprise / Defense** | Regulated, federal, large | **Starting at $50K/yr** | Everything in Business + assessor-readiness assist + CMMC mapping + on-prem deployment support + custom indemnification |

### Nav HTML structure (reference)

```html
<nav class="nav">
  <a href="/" class="logo">HUMMBL</a>
  <ul class="nav-links">
    <li><a href="/primitives">Primitives</a></li>
    <li><a href="/solutions">Solutions</a></li>
    <li><a href="/docs">Docs</a></li>
    <li><a href="/pricing">Pricing</a></li>
    <li><a href="/blog">Blog</a></li>
    <li><a href="https://github.com/hummbl-dev/hummbl-governance" class="github">
      <svg><!-- github icon --></svg>
      <span class="stars">★ 1.2k</span>
    </a></li>
  </ul>
</nav>
```

---

## PART VIII — SUCCESS METRICS

Track after launch:

| Metric | Baseline (today) | Target (30 days post-launch) |
|--------|------------------|-------------------------|
| Discovery calls booked / week | ? | 3+ |
| `pip install hummbl-governance` downloads / week | ? | 2x baseline |
| GitHub stars | ? | 2x baseline |
| Time-on-site (homepage) | ? | > 45s |
| Bounce rate (homepage) | ? | < 60% |
| Primitive-page depth (% users visiting ≥1 primitive page) | 0% (doesn't exist) | 30% |
| `/solutions/defense-federal` discovery-call conversion | 0% (doesn't exist) | Track |
| Changelog updates | 6 weeks stale | Weekly |

### Non-metric signals
- First case study published
- First named design partner
- First DIBCAC assessor inquiry
- First EU AI Act compliance conversation
- First enterprise POC

---

## PART IX — RISKS & MITIGATIONS

| Risk | Mitigation |
|------|-----------|
| Too much content to write in one sprint | Ship Phase 0-1 this week, Phase 2-4 next week |
| New positioning drives away current leads | Current site has no measurable lead flow — low-risk to reset |
| Defense/Federal wedge is slow to convert | Keep `/solutions/ai-native-teams` as easy-win funnel |
| Open-source repo isn't pretty enough to drive from homepage | Audit the repo README before launch; spend 2h polishing |
| Install snippet fails for a visitor | Test on macOS + Linux + Windows (PowerShell), verify on a fresh venv |
| Primitive pages are too technical for executives | Each primitive page includes "Why you need this" exec-level paragraph |
| Engineering bandwidth constraint (solo founder) | Phase 0-1 takes ~3-4 hours total — achievable today |

---

## PART X — DECISION POINTS

Before execution starts, two things need confirmation from Reuben:

1. **Pricing tiers**: is $100/$1K/$50K the right ladder? (These are defaults from reference-site analysis + research TAM data. Could go $0/$50/$500/$25K if more aggressive.)

2. **Defense/Federal emphasis**: is this the right primary vertical? (Research says yes. Could alternatively lead with "AI-native teams" and make defense a /solutions page with less homepage real-estate.)

3. **MCP primitive**: should MCP be a 7th primitive card on the homepage? (Round 4 Lane E says MCP attestation is a 2-week product wedge. If HUMMBL ships it, it should be in the hero grid.)

---

## SUMMARY — THE ONE-LINE PLAN

**Turn hummbl.io into Supabase-for-governance-primitives: fix the broken foundation today, ship primitive-page IA and Defense/Federal wedge this week, let the install snippet + GitHub stars drive the developer funnel, and let the Defense/Federal page drive the enterprise ACV.**

---

*Plan based on: competitor audit (7 sites), reference-site audit (8 sites), hummbl.io deep audit (14 pages, 11 404s found), customer-perspective review, 16-doc AI-slop-crisis research corpus.*
*Research files: `/Users/others/Downloads/hummbl_io_plan_*.md`*
