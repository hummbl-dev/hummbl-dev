# You Were Just Named AI Governance Lead. Here's Your 90-Day Playbook.

*Your peers in DevSecOps went through this exact transition in 2014. They had eight years. You have about three. Here is the program-building plan distilled from what actually worked, compressed for the AI governance timeline.*

---

## You Have a Title and No Playbook

Congratulations. You are now your organization's AI Governance Lead, Head of Responsible AI, or some variant of a role that did not exist 18 months ago. You report to the CISO, the CRO, the CDO, or the General Counsel -- possibly all four, because nobody has figured out the reporting line yet.

Here is what the data says about your situation:

**75% of enterprises plan to deploy agentic AI within two years. Only 21% have a mature model for agent governance** (Deloitte State of AI in the Enterprise, 2026). You are standing in the 54-point gap between intent and readiness. That gap is your job.

**38.5% of Fortune 1000 companies now have a Chief AI Officer** (MIT AI Leadership Benchmark, n~110), up from 33.1% the prior year. AWS's 2026 survey of 3,739 senior IT leaders found 60% of organizations already have a CAIO, with another 26% planning to add one. The role is real. The infrastructure underneath it is not.

You are not alone in having no playbook. But the clock is running.

---

## The DevSecOps Precedent: Why Your Timeline Is Compressed

In 2012, Gartner analyst Neil MacDonald coined "DevSecOps." By 2016, adoption was at **0%**. The first inflection hit in 2017 at **~11%**. Mainstream adoption (20-50%) arrived around 2020. The full cycle from term to default took roughly eight years (Gartner Hype Cycle for Agile and DevOps, 2012-2022; Infosec Institute DevSecOps evolution data).

AI governance is on the same curve, but compressed:

| DevSecOps milestone | Year | AI governance equivalent | Year |
|---------------------|------|--------------------------|------|
| Term coined | 2012 | "AI governance" enters analyst lexicon | 2021-2022 |
| 0% adoption baseline | 2016 | Pre-regulation baseline | 2023 |
| First inflection (11%) | 2017 | ChatGPT enterprise panic, first AI policies | 2024 |
| Compliance catalyst (GDPR) | 2018 | **EU AI Act Annex III enforcement** | **Aug 2 2026** |
| Mainstream adoption (20-50%) | 2020 | Estimated | 2027 |

GDPR took four years from proposal to enforcement. The EU AI Act is compressing that to roughly three years. The buying cycle that GDPR triggered in data governance tooling (2016-2019) has a **15-month compressed window** to the August 2026 Annex III deadline, with penalties up to **35 million euros or 7% of global revenue** (EU AI Act, Regulation 2024/1689, Article 99).

The DevSecOps lesson that matters most: the winners were not the teams that built perfect programs. The winners were the teams that **shipped governance primitives into the pipeline before compliance pull arrived**. Policy-as-code (OPA, Sentinel) beat policy-as-document every time.

---

## The 90-Day Plan

### Weeks 1-2: Inventory

You cannot govern what you cannot see. **81% of organizations lack visibility into how AI is actually used in their codebases** (Black Duck OSSRA 2026). Start here.

**Action items:**

- **Enumerate every AI tool in use.** Copilot, Claude Code, ChatGPT Enterprise, Cursor, embedded vendor AI. Check procurement, but also shadow IT -- developer surveys consistently reveal 2-3x more usage than procurement knows about.
- **Map each tool to a data flow.** What goes in? What comes out? Where does telemetry go?
- **Identify your regulatory surface.** NIST AI RMF (US baseline), ISO/IEC 42001 (international), EU AI Act (if you serve EU customers), state laws (Colorado AI Act effective June 30 2026, NYC Local Law 144).
- **Establish your baseline metric.** How many AI-assisted outputs per week? You need this number to scope everything that follows.

> The inventory phase is unglamorous but non-negotiable. Every DevSecOps program that skipped asset discovery spent months backfilling later.

---

### Weeks 3-4: Policy

Policy comes after inventory, not before. You need to know what you are governing before you write the rules.

**Action items:**

- **Draft an Acceptable Use Policy.** Approved tools, prohibited use cases, data classification rules, disclosure requirements, human review thresholds.
- **Establish risk tiers.** A code completion suggestion is not the same as an autonomous agent making customer-facing decisions. Define 3-4 tiers with escalating controls.
- **Assign ownership.** Who approves new AI tools? Who reviews high-risk use cases? Who has kill-switch authority? If the answer is "nobody," fix that now.
- **Anchor to a framework.** NIST AI RMF is the most recognized US framework. ISO/IEC 42001 is gaining traction -- **76% of surveyed enterprises plan to pursue an AI audit or certification within 24 months** (BSI/Schellman, Q1 2026). Pick one primary, crosswalk the other.

---

### Weeks 5-8: Controls

Policy without enforcement is theater. This is where most AI governance programs stall, because "controls" in AI governance often means manual review processes that do not scale.

**Action items:**

- **Implement runtime logging.** Every AI-generated artifact needs a provenance record: which model, which prompt, which policy version, which human reviewed it. Audit trails generated at the point of creation, not reconstructed after a breach.
- **Deploy kill switches.** Halt AI-assisted operations at individual agent, tool category, and organization-wide levels. These must work without depending on the AI vendor's cooperation.
- **Establish human-in-the-loop thresholds.** Which outputs require human review before action? Base this on your risk tiers. Automate routing so high-risk outputs cannot bypass review.
- **Map controls to regulatory requirements.** Each control traces to at least one framework requirement. **One control, multiple attestation formats** -- this is how you avoid parallel compliance programs.

The insurance angle matters here: **Berkley and other carriers have begun writing absolute AI exclusions into D&O and E&O policies** (Round 3 research, verified). If your organization faces an AI-related claim and your D&O policy excludes AI, your evidence of reasonable governance controls is your only defense. Controls are not just compliance artifacts -- they are litigation insurance.

---

### Weeks 9-12: Evidence Pipeline

The final phase converts your controls into a continuous evidence stream. This is the phase that separates governance programs that survive their first audit from those that fail.

**Action items:**

- **Automate evidence collection.** Governance logs, delegation records, kill switch state changes, and human review attestations should be machine-readable artifacts generated at runtime -- not reconstructed after a breach.
- **Build your assessment-readiness package.** Whether your next audit is NIST AI RMF, ISO 42001, or an insurance underwriting review, the assessor needs: inventory, risk assessment, control implementation, monitoring records, incident response capability. Package these for on-demand production.
- **Establish your cadence.** Monthly control reviews. Quarterly risk reassessment. Annual framework alignment. Calendar it now.
- **Measure the gap closure.** What percentage of AI usage is governed? What percentage of high-risk outputs have audit trails? These are the metrics your executive sponsor needs.

---

## The Mistakes Your DevSecOps Peers Made (So You Don't Have To)

**Mistake 1: Starting with the tool, not the policy.** DevSecOps teams that bought Snyk before defining their vulnerability management policy spent years retrofitting process around tooling. Define your governance model first. Choose tools that fit.

**Mistake 2: Treating governance as a gate instead of a substrate.** The DevSecOps teams that won were the ones that embedded security into the CI/CD pipeline, not the ones that added a review committee. AI governance that exists as a manual approval process will be routed around. Governance that is embedded in the generation loop -- as runtime primitives, not dashboards -- cannot be bypassed.

**Mistake 3: Waiting for the regulation to be final.** GDPR was proposed in 2012 and enforced in 2018. The organizations that started in 2016 were ready. The ones that started in 2017 were scrambling. **EU AI Act Annex III enforcement hits August 2, 2026.** Colorado's AI Act is effective June 30, 2026. The METR randomized controlled trial found experienced developers were **19% slower with AI tools while believing they were 20% faster** (arXiv 2507.09089) -- which means your organization is accumulating unaudited AI-assisted outputs faster than anyone realizes.

---

## Your Week 1 Checklist

- [ ] Get a 30-minute meeting with your executive sponsor to align on scope
- [ ] Send a 5-question survey to engineering leads on AI tool usage
- [ ] Pull procurement records for all AI-related vendor contracts
- [ ] Identify which regulatory frameworks apply to your organization
- [ ] Read NIST AI RMF 1.0 (46 pages) and the GenAI Profile (NIST AI 600-1)
- [ ] Block 2 hours on your calendar for Week 2 to synthesize findings

You have 90 days. The organizations that build their governance programs now -- while the market is still forming -- will define the standard. The ones that wait will be retrofitting under enforcement pressure.

Start with the inventory. Everything else follows.

---

*HUMMBL builds AI governance infrastructure -- stdlib-only primitives that embed in your development pipeline, not dashboards that sit beside it.*

**Assess your governance readiness**: [hummbl.io/readiness](https://hummbl.io/readiness)
**Track regulatory deadlines**: [hummbl.io/tracker](https://hummbl.io/tracker)
**Talk to us**: [reuben@hummbl.io](mailto:reuben@hummbl.io)

---

*Sources: Deloitte State of AI in the Enterprise 2026; MIT AI Leadership Benchmark (n~110); AWS 2026 AI Survey (n=3,739); Gartner Hype Cycle for Agile and DevOps 2012-2022; EU AI Act (Regulation 2024/1689); NIST AI RMF 1.0; NIST AI 600-1 GenAI Profile; BSI/Schellman ISO 42001 survey Q1 2026; Black Duck OSSRA 2026; METR RCT (arXiv 2507.09089); Colorado AI Act SB 24-205; Berkley AI exclusion analysis (Round 3 research). All citations verified in HUMMBL Research Corpus Round 5.*
