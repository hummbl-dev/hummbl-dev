# hummbl.io Site Audit — Customer Perspective
**Date:** 2026-04-05
**Pages crawled:** 14 live pages + 11 expected-but-404 pages
**Method:** HTTP fetch + content analysis of visible text and nav structure

---

## Executive Summary

hummbl.io is a hybrid product + consulting site selling "AI governance infrastructure" — a Base120 mental-models API plus governance audits/implementation services. There are two essentially distinct products competing for attention (API/developer tooling and governance consulting), but the site fails to separate them. The biggest customer-visible problems are: **pricing contradicts itself across three pages**, the taxonomy of audit tiers is incoherent (Free Audit vs Arbiter Report vs Verified Memo vs Readiness Audit vs Implementation Sprint), the **compliance calendar shows "--" for all stats** (broken live data), **no "about" or "contact" page exists** (both 404), and the **blog has zero posts** (just "Loading posts..."). Several pages referenced in the changelog (Playground, Case Studies) exist but are orphaned from the main nav.

**Top 5 issues:**
1. **Pricing conflicts** — Services page quotes Readiness Audit at $2–5K; Consulting page quotes the same at $5–15K; Pricing page introduces entirely different tiers ($0/$500/$2,500/$5K+) with names that don't appear anywhere else.
2. **Broken/empty pages** — Blog is empty, Case Studies shows "Loading case studies...", Compliance Calendar stats all read "--", Explorer shows "Loading models...". These likely rely on JS/API calls, but a customer on first load sees a dead site.
3. **Missing foundational pages** — No /about, /team, /contact, /legal, /privacy, /security. Every SaaS buyer checks these.
4. **Identity/naming chaos** — "Free Audit," "Arbiter Report," "Verified Memo," "Readiness Audit," "Gap Assessment," and "Discovery Call" are used interchangeably with no map explaining how they relate.
5. **Stale/placeholder content** — Compliance Calendar advertises "30+ deadlines" but shows zero. Dates throughout (Jan–Feb 2026) suggest the site hasn't been updated in ~6 weeks.

---

## Page-by-Page

### / (index)
- **Purpose:** Homepage — dual pitch: Base120 API + governance consulting
- **Primary CTA:** "Try the API →" (to api.hummbl.workers.dev) + "Free Readiness Assessment" (Learn More)
- **Content:** Hero ("Governance infrastructure for AI-native teams"), the 6 transformations (P/IN/CO/DE/RE/SY), stats (120 models, 66 agents, <50ms), MCP setup, use cases
- **Inconsistencies:** States "66 Agent Identities" but changelog says "60+ coordinated agents"; playground page says "five vendor runtimes" and changelog says "6 vendor runtimes"
- **Missing:** No clear customer segment (dev vs buyer); no social proof/logos

### /services.html
- **Purpose:** Sell three consulting engagement tiers
- **Primary CTA:** "Book a Call" (×3)
- **Tiers:** Readiness Audit ($2–5K, 1wk) / Implementation Sprint ($10–25K, 2–4wk) / Retainer ($3–5K/mo)
- **Inconsistencies:** Pricing conflicts with /consulting.html ($5–15K / $15–40K / $5–15K/mo) and /pricing.html ($0/$500/$2,500/$5K+). Three entirely different pricing structures.
- **Missing:** No timeline for engagement start; no named case studies; "Arbiter" is named but never defined on this page

### /readiness.html
- **Purpose:** Framework self-assessments
- **Primary CTA:** "Start Free Assessment →" / "Book a Free Assessment"
- **Content:** Promises assessments for 5 frameworks but the framework list is not visible in the scraped text (likely JS-loaded cards)
- **Inconsistencies:** States "5 Frameworks Mapped" and "15 Governance Capabilities" — neither matches other pages
- **Missing:** The actual assessment links — the page advertises them but doesn't surface them statically
- **Good:** Clear "What We Do Not Provide" transparency section (no legal advice, no certification)

### /audit.html
- **Purpose:** EU AI Act Annex III pitch — single-framework landing page
- **Primary CTA:** "Book a Free Assessment"
- **Content:** Countdown to Aug 2, 2026; €35M fine warning; 6 Annex III articles; 10-item checklist
- **Inconsistencies:** Countdown element shows no actual days count in static HTML; this page is for EU AI Act only but URL is generic /audit — collides with /audits.html expectation
- **Missing:** No link to /compliance calendar where other deadlines live; no mention of Arbiter grading despite being an "audit" page

### /compliance.html
- **Purpose:** Compliance calendar covering 30+ AI regulations
- **Primary CTA:** "Book a Call"
- **Content:** Region filters (US/EU/APAC/Int'l), sector filters
- **Inconsistencies/Bugs:** All key stats render as "--" in static HTML ("-- Regulations Tracked / -- Deadlines in 90 Days / -- Jurisdictions"). Promises "30+" but delivers nothing without JS
- **Missing:** A static fallback list of regulations

### /pricing.html
- **Purpose:** Pricing for both consulting (Assurance Ladder) AND API
- **Content:** Free Audit $0 / Arbiter Report $500 / Verified Memo $2,500 / Advisory $5k+; API tiers Free/Pro $29/Enterprise
- **Inconsistencies:** These four tier names (Free Audit, Arbiter Report, Verified Memo, Advisory) do NOT appear on /services.html or /consulting.html. The Pricing page invents its own taxonomy.
- **Missing:** No explanation of what Arbiter actually is; no link from "Take Assessment" to the actual assessment

### /docs.html
- **Purpose:** Base120 API reference
- **Primary CTA:** cURL commands
- **Content:** Endpoints (/health, /v1/models, /v1/models/:code, /v1/recommend, /v1/workflows/match, /security/validate), response schemas
- **Quality:** Best-executed page on the site. Clean, complete, dated timestamp "2026-02-25".
- **Missing:** No SDK links beyond reference

### /blog.html
- **Purpose:** Content/thought-leadership hub
- **Content:** "Loading posts..." — ships empty
- **Primary CTA:** "Write for the Blog" / "Submit a Case Study"
- **Critical issue:** No posts render. Either the blog has nothing or the JS fetch is broken.

### /explorer.html
- **Purpose:** Browse 120 models interactively
- **Content:** Filter UI + "Loading models..." placeholder
- **Issue:** Entirely JS-dependent; static HTML shows no models

### /consulting.html
- **Purpose:** Second consulting page with different framing (focused on Reuben Bowlby personally: "I build and audit…")
- **Pricing:** Readiness Audit $5–15K/1wk, Retainer $5–15K/mo, Implementation $15–40K/2–3wk, plus governance packages ($20–40K Agentic, $8–15K/state AI Employment)
- **Inconsistency:** This entire page duplicates /services.html with different prices, different engagement lengths, different package names. Customers hitting both pages will be confused.

### /status.html
- **Purpose:** API health dashboard
- **Content:** Live status of 6 endpoints, rate limit, incident history
- **Quality:** Good when JS runs; static shows "Checking..." for all

### /changelog.html
- **Purpose:** Product changelog
- **Content:** 7 entries from Jan 15 → Feb 24 2026
- **Issues:** Last entry Feb 24; today is Apr 5 → **6 weeks stale**. References "Playground page" and "Case Studies" as new — both orphaned from nav.

### /cases.html
- **Purpose:** Case studies
- **Content:** "Loading case studies..." + submit form
- **Issue:** No inbound link from main nav. Orphaned page.

### /playground.html
- **Purpose:** Live API sandbox with curated demos + 5-layer safety stack visualization + agent lineup
- **Issue:** Not linked from main nav. Orphaned. Says "five vendor runtimes" (conflict: changelog says 6).

---

## Cross-Page Issues

### Duplicate/Conflicting Information

| Claim | Page A | Page B | Page C |
|---|---|---|---|
| Readiness Audit price | $2–5K (services) | $5–15K (consulting) | $500 "Arbiter Report" (pricing) |
| Retainer price | $3–5K/mo (services) | $5–15K/mo (consulting) | $5K+ "Advisory" (pricing) |
| Implementation Sprint | $10–25K / 2–4wk (services) | $15–40K / 2–3wk (consulting) | not listed (pricing) |
| Agent count | 66 (index) | 60+ (changelog) | 12-agent fleet (audit) |
| Vendor runtimes | 5 (index, playground) | 6 (changelog) | — |

### Taxonomy Problem: What IS an "audit"?

Six overlapping terms with no map:
- **Free Audit** ($0, pricing page) — 17-point self-assessment
- **Free Readiness Assessment** (index, readiness) — 30-min call
- **Free Compliance Gap Assessment** (compliance) — 30-min call
- **Arbiter Report** ($500, pricing) — technical readiness review
- **Readiness Audit** ($2–5K or $5–15K, services/consulting) — 1-week engagement
- **Verified Memo** ($2,500, pricing) — human-reviewed

A buyer cannot tell whether the $0 self-assessment, the $500 Arbiter Report, and the $2–5K Readiness Audit are the same product at different tiers or different products entirely.

### Dead-End / Broken Pages
- **blog.html** — empty ("Loading posts...")
- **cases.html** — empty ("Loading case studies...")
- **explorer.html** — empty ("Loading models...")
- **compliance.html** — zeroed stats ("--")
- **status.html** — "Checking..." placeholders

All rely on client-side JS. Customers on slow connections, strict CSPs, or no-JS sessions see a dead site.

### Orphan Pages (no inbound nav link)
- **playground.html** — flagship interactive demo, not in main nav
- **cases.html** — changelog advertises it but footer nav says "Docs" instead
- **audit.html** — accessible only from homepage CTA
- **consulting.html** — accessible only from homepage CTA
- **status.html** — not in nav at all
- **changelog.html** — not in nav at all

### Missing Pages Customers Expect (all 404)
- **/about** or **/team** — who is HUMMBL? (Footer says "Reuben Bowlby" — founder not introduced)
- **/contact** — only option is "book a call" (scheduling dependency)
- **/security** — ironic for a governance company
- **/legal**, **/privacy**, **/terms** — required for any paid product
- **/eu-ai-act-readiness.html** etc. — readiness page implies per-framework pages exist; none do

### Outdated Content
- **Changelog stale since Feb 24, 2026** (6 weeks)
- **Footer still "© 2026"** — correct but feels perfunctory
- EU AI Act page's countdown requires JS; static shows "days" with no number
- Docs page timestamp: `2026-02-25T16:00:26` hard-coded in response example

### Navigation Inconsistency
Main nav across pages: **Services / Readiness / Audits / Compliance / Blog / Docs / Explorer / GitHub**
Footer across pages: **Home / Services / Readiness / Audits / Compliance / Blog / Docs / Pricing / GitHub**
- Nav says "Audits" (plural) — page is /audit.html (singular). /audits.html 404s.
- Pricing is in footer but not main nav.
- Playground, Status, Changelog, Cases, Consulting are in neither.

---

## Recommendations (priority-ordered)

1. **Pick one pricing model and reconcile** /services, /consulting, /pricing to tell the same story. Preferred: promote /services as canonical; turn /consulting into founder bio + /pricing into API-only.
2. **Fix empty pages** — either ship real content to /blog, /cases, /explorer, /compliance, or hide them until they have content. "Loading..." with no data is a trust-killer.
3. **Create the missing 5 pages** — /about, /contact, /security, /privacy, /terms. Governance buyers will not convert without these.
4. **Publish a single "Services & Assurance Ladder" taxonomy page** that maps Free Audit → Arbiter Report → Verified Memo → Readiness Audit → Implementation Sprint → Retainer with price, duration, deliverable.
5. **Reconcile the nav** — add Playground, Status, Changelog to footer. Fix "Audits" (plural) link to point to /audit.html.
6. **Update the changelog** — add a March/April entry or remove the date scaffolding to hide staleness.
7. **Add static fallbacks** to JS-loaded pages so the compliance calendar and explorer show content without JavaScript.
