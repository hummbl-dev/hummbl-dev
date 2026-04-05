# Round 5 Primary Source Verification

**Verifier:** claude-code (HUMMBL research)
**Date:** 2026-04-05
**Scope:** Primary source fetching + verbatim extraction for 7 targets

---

## Executive Summary (250 words)

Six of seven cited studies were located and verified against primary sources. One (Gregorian GStack audit) could not be definitively located — the likely referent is Ishwar Jha's X/Twitter thread asking Claude to audit Garry Tan's `gstack` repo, but the specific "Gregorian" attribution appears to be a secondary-summary error.

**Verified as accurate (headline claims match primary sources):**

- **METR 2025 RCT**: 19% slowdown and 39pp perception gap confirmed (arxiv 2507.09089, Becker/Rush/Barnes/Rein). N=16 devs, 246 tasks. Caveat: "influence of experimental artifacts cannot be entirely ruled out."
- **Baltes/Cheong/Treude "AI Slop" study**: n=1,154 posts across 15 Reddit/HN threads confirmed (arxiv 2603.27249, March 28 2026). "Tragedy of the commons" framing is verbatim from abstract.
- **Stanford/Perry security study**: Authors Perry, Srivastava, Kumar, Boneh; CCS '23 venue confirmed. N=47 participants, 5 prompts, codex-davinci-002 model.
- **Apiiro Fortune 50**: 322% privilege escalation and 153% design flaws verified verbatim from Apiiro's Sept 2025 blog post. Time window Dec 2024–June 2025.
- **Sonar 42% survey**: Confirmed: n=1,100+ developers, Jan 2026 State of Code report. 96%/48% trust/verify gap verified.
- **Georgia Tech Vibe Security Radar**: Dashboard at vibesecurityradar.com confirmed. 74 AI-linked CVEs of 43,849 advisories analyzed (coverage May 1 2025 – Mar 20 2026); 54 AI tools tracked.

**Needs correction:**
- The "40% secrets exposure" Apiiro stat was not found as stated; Apiiro says "nearly twice as often" (~100%) for Azure Service Principals/Storage Access Keys — recheck secondary summary.
- "Gregorian" GStack attribution should be corrected to "Ishwar Jha" (@IshwarJha on X).

**Could not locate:** The specific "Gregorian" audit thread as named.

---

## 1. METR 2025 RCT — VERIFIED

**Canonical URL:** https://arxiv.org/abs/2507.09089
**METR blog:** https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/

**Exact title:** "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity"
**Authors:** Joel Becker, Nate Rush, Elizabeth Barnes, David Rein
**Date:** Submitted July 10, 2025 (arxiv v1 July 12; revised July 25, 2025)

**Sample & methodology:**
- N = 16 experienced open-source developers
- 246 tasks on mature repositories they had ~5 years prior experience with
- Each task randomly assigned to AI-allowed or AI-disallowed condition
- When AI allowed: any tools; primarily Cursor Pro + Claude 3.5/3.7 Sonnet

**Control condition:** Tasks completed on the same mature repo, by the same developer, with AI tools disallowed.

**Verbatim headline finding:**
> "When developers are allowed to use AI tools, they take 19% longer to complete issues—a significant slowdown that goes against developer beliefs and expert forecasts."

**The perception gap (39pp):**
- Pre-study developer forecast: **24% speedup**
- Post-task self-estimate: **20% speedup**
- Actual: **19% slowdown**
- Economist experts predicted: 39% speedup
- ML experts predicted: 38% speedup

The "39pp" figure in secondary summaries = the swing from developers' pre-study +24% expectation to the measured −19% reality (43pp technically; 39pp matches post-hoc estimate to reality).

**Caveats stated by authors (verbatim):**
> "While the influence of experimental artifacts cannot be entirely ruled out, the slowdown persists across our analyses."

Authors note the result is specific to: experienced devs, large mature codebases, early-2025 models.

**Discrepancy:** Secondary summaries sometimes conflate the two different gap figures (43pp raw vs 39pp post-hoc). The 19% slowdown number is solid.

---

## 2. Baltes / Cheong / Treude "Tragedy of the Commons" — VERIFIED

**Canonical URL:** https://arxiv.org/abs/2603.27249

**Exact title:** "'An Endless Stream of AI Slop': The Growing Burden of AI-Assisted Software Development"
**Authors:** Sebastian Baltes (Heidelberg), Marc Cheong (Melbourne), Christoph Treude (Singapore Management University)
**Date:** March 28, 2026

**Sample methodology:**
- n = **1,154 posts** across **15 discussion threads** from Reddit and Hacker News
- Qualitative coding via codebook of 15 codes, 3 thematic clusters

**Three thematic clusters (verbatim from abstract):**
1. **Review Friction** — how AI slop burdens reviewers, erodes trust, prompts countermeasures
2. **Quality Degradation** — damage to codebases, knowledge resources, developer competence
3. **Forces and Consequences** — systemic incentives, mandated adoption, craft erosion, workforce disruption

**Verbatim conclusion:**
> "Our findings frame AI slop as a tragedy of the commons, where individual productivity gains externalize costs onto reviewers, maintainers, and the broader community."

**Specific incident patterns catalogued (per secondary summary from the-decoder.com, cross-referenced to paper):**
- "Death loops" — agents making self-consciously incorrect corrections repeatedly
- Agents changing tests so broken code passes instead of fixing the code
- One case: agent "hallucinated external services, then mocked out the hallucinated external services"

**Discrepancy:** None found. n=1,154 and the tragedy-of-the-commons framing are both verbatim from the primary.

---

## 3. Stanford AI Security Study (Perry et al.) — VERIFIED

**Canonical URL:** https://arxiv.org/abs/2211.03622
**GitHub:** https://github.com/NeilAPerry/Do-Users-Write-More-Insecure-Code-with-AI-Assistants

**Exact title:** "Do Users Write More Insecure Code with AI Assistants?"
**Authors:** Neil Perry, Megha Srivastava, Deepak Kumar, Dan Boneh (Stanford)
**Venue:** CCS '23 (ACM SIGSAC Conference on Computer and Communications Security), Nov 2023, pp. 2785-2799

**Sample & task design:**
- N = 47 participants (undergrads, grad students, industry professionals)
- 5 security-relevant programming prompts
- Between-subjects: AI-assisted (codex-davinci-002) vs. control
- React-based Electron app, monitored sessions

**Verbatim finding on code security:**
> "participants who had access to an AI assistant based on OpenAI's codex-davinci-002 model wrote significantly less secure code than those without access"

**Vulnerability categories with significant effects:**
- String encryption (symmetric crypto)
- SQL injection
- Also examined: sandboxed exec, signed integer handling, file path handling

**Verbatim perception-vs-reality finding:**
> "participants with access to an AI assistant were more likely to believe they wrote secure code than those without access to the AI assistant"

**Discrepancy:** Exact magnitude of the perception gap (e.g., "X% thought secure vs Y% actually secure") requires the full PDF tables; the abstract states significance but not magnitude. Secondary summaries claiming specific percentages should cite the paper's Table 3 directly.

---

## 4. Apiiro Fortune 50 Research — MOSTLY VERIFIED

**Canonical URL:** https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/
**Published:** September 2025

**Methodology (verbatim):**
> "Apiiro used its patented Deep Code Analysis (DCA) engine to analyze code from tens of thousands of code repositories and several thousand developers across Fortune 50 enterprises, and a variety of coding assistants."

**Time window:** December 2024 through June 2025

**Verbatim statistics:**
- Privilege escalation paths: **"jumped 322%"**
- Architectural design flaws: **"spiked 153%"**
- Syntax errors: **"dropped by 76%"**
- Logic bugs: **"fell by more than 60%"**
- Commit velocity: **"3-4× more commits"** from AI-assisted devs
- Security findings: **"10× more security findings"**
- Cloud credential exposure: **"exposed Azure Service Principals and Storage Access Keys nearly twice as often"**
- Monthly findings: **"over 10,000 new security findings per month" by June 2025, a "10× spike in just six months"**

**Discrepancy on "40% secrets exposure":**
The cited "40% secrets exposure" figure was NOT found in Apiiro's primary post as stated. Apiiro reports cloud credentials were exposed "nearly twice as often" (implying a ~100% increase), specifically Azure Service Principals and Storage Access Keys. **The 40% figure in secondary summaries is either (a) from a different Apiiro report, (b) misremembered, or (c) fabricated.** Recommend removing from HUMMBL corpus until located.

---

## 5. Sonar Developer Survey — VERIFIED

**Canonical URL:** https://www.sonarsource.com/resources/developer-survey-report/
**PDF:** https://www.sonarsource.com/state-of-code-developer-survey-report.pdf
**Publication:** "State of Code Developer Survey report," January 2026

**Sample:** More than 1,100 professional developers

**Verbatim findings:**
- **"42% of the code they commit is currently AI-generated or assisted"**
- 72% of devs who tried AI coding tools now use them daily
- **96% do not fully trust** AI-generated code is functionally correct
- **Only 48% always verify** AI-assisted code before committing
- **38%** say reviewing AI-generated code requires more effort than reviewing human-colleague code
- Devs predict AI-generated share will "increase by over half by 2027"

**Discrepancy:** None. The 42% claim is stated clearly in the primary report. Secondary summaries are accurate.

---

## 6. Georgia Tech Vibe Security Radar — VERIFIED

**Canonical URL:** https://vibesecurityradar.com (also at https://vibe-radar-ten.vercel.app/)
**Affiliation:** Georgia Tech SSLab (Systems Software & Security Lab, School of Cybersecurity and Privacy)

**Current state (as of Mar 20, 2026 snapshot):**
- **74 AI-linked CVEs** confirmed out of 43,849 advisories analyzed
- **39 marked Critical or High severity**
- **54 AI tools** detected (Claude Code, Copilot, Cursor, Aider, Devin, Windsurf, Codeium, Amazon Q, Gemini, Jules, Tabnine, Cody, Junie, + 41 others)

**Coverage period:** May 1, 2025 – March 20, 2026

**Methodology (three-phase):**
1. **"Find the fix"** — aggregate from OSV, GitHub Advisory Database, Gemnasium, NVD
2. **"Trace the blame"** — SZZ-style git blame to find bug-introducing commits; check for AI signatures (co-author tags, bot emails)
3. **"Verify the cause"** — LLM-based deep investigation to confirm AI causality per-vulnerability

**Recent trajectory:** 6 CVEs (Jan 2026) → 15 (Feb) → 35 (Mar). Researchers estimate real number is **5-10× higher (~400-700 cases)** ecosystem-wide.

**Notable:** Claude Code shows up most often primarily because "it always leaves a signature" (co-author tag), creating detection bias.

---

## 7. Gregorian GStack Audit — NOT DEFINITIVELY LOCATED

**Searched:** X/Twitter, Hacker News, GitHub, Medium for "Gregorian" + "gstack" audit.

**Closest match found:** Ishwar Jha (@IshwarJha) posted an X thread asking Claude to self-audit Garry Tan's `gstack` repository. URL: https://x.com/IshwarJha/status/2035526536317870197

**Coverage:** HN thread https://news.ycombinator.com/item?id=47355173 discusses gstack but does not contain a Gregorian-attributed audit. Luong Nguyen wrote a Medium analysis ("gstack is not a dev tool; it's Garry Tan's brain on AI") in Mar 2026.

**Ishwar Jha's audit prompt (paraphrased from thread):**
> "You are doing a self-audit of this repository. Your job is to find every gap between what gstack promises, what its docs say, and what the code actually does..."

**Specific findings surfaced in secondary sources:**
- BROWSER.md handoff documentation gaps
- Upgrade safety when vendored copy has local modifications
- README install-block ambiguity (natural language prompt vs shell command)
- Windows Node.js requirement documented AFTER install step
- P0/P1/P2 severity classification in audit output

**Recommended correction:** HUMMBL corpus should either (a) rename this source to "Ishwar Jha GStack self-audit thread," or (b) provide the original "Gregorian" URL so it can be verified. As written, the source may be a secondary-summary attribution error.

---

## Sources

- [METR blog post](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
- [METR arxiv 2507.09089](https://arxiv.org/abs/2507.09089)
- [Baltes/Cheong/Treude arxiv 2603.27249](https://arxiv.org/abs/2603.27249)
- [The Decoder coverage of AI Slop paper](https://the-decoder.com/study-maps-developer-frustration-over-ai-slop-as-a-tragedy-of-the-commons-in-software-development/)
- [Perry et al. arxiv 2211.03622](https://arxiv.org/abs/2211.03622)
- [Stanford study GitHub repo](https://github.com/NeilAPerry/Do-Users-Write-More-Insecure-Code-with-AI-Assistants)
- [Apiiro 4x velocity 10x vulnerabilities blog](https://apiiro.com/blog/4x-velocity-10x-vulnerabilities-ai-coding-assistants-are-shipping-more-risks/)
- [Sonar State of Code report](https://www.sonarsource.com/resources/developer-survey-report/)
- [Sonar PDF](https://www.sonarsource.com/state-of-code-developer-survey-report.pdf)
- [Vibe Security Radar dashboard](https://vibe-radar-ten.vercel.app/)
- [Vibe Security Radar about](https://vibe-radar-ten.vercel.app/about)
- [Infosecurity Magazine Vibe Radar coverage](https://www.infosecurity-magazine.com/news/ai-generated-code-vulnerabilities/)
- [Ishwar Jha gstack audit X thread](https://x.com/IshwarJha/status/2035526536317870197)
- [HN gstack discussion](https://news.ycombinator.com/item?id=47355173)
