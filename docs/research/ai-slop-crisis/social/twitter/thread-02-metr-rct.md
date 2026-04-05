# Thread 02: The METR RCT -- 19% Slower, Believed 20% Faster

---

**1/** (137 chars)
A controlled trial gave experienced devs AI coding tools. They got 19% slower. They believed they were 20% faster. The full story: [thread]

**2/** (274 chars)
The study: METR (Becker, Rush, Barnes, Rein), arxiv 2507.09089. N=16 experienced open-source developers. 246 tasks on mature repos they had ~5 years of prior experience with. Each task randomly assigned to AI-allowed or AI-disallowed. Rigorous RCT design.

**3/** (242 chars)
The result: when allowed to use AI tools (primarily Cursor Pro + Claude 3.5/3.7 Sonnet), developers took 19% longer to complete tasks. Not faster. Slower. On codebases they already knew well.

**4/** (279 chars)
The perception gap: before the study, devs predicted a 24% speedup. After each task, they self-estimated a 20% speedup. ML experts predicted 38%. Economists predicted 39%. Every group was wrong in the same direction. Confidence was inversely correlated with reality.

**5/** (278 chars)
The 39-point perception gap (from +20% believed to -19% actual) is the most dangerous finding. If your engineering team reports AI is making them faster and you take that at face value, you are making resource decisions on misinformation.

**6/** (270 chars)
Important context: this was experienced devs on large, mature codebases. Other studies (Peng et al., DORA 2025) show 40-60% gains for greenfield tasks and junior developers. The gains are real -- for some work. The problem is assuming they generalize.

**7/** (269 chars)
The DORA 2025 report (Google Cloud) found 2.5x odds of successful task completion with AI. But the experience gradient matters: juniors +27-39%, seniors +8-13%. For experienced engineers on complex brownfield code, the ROI collapses or inverts.

**8/** (277 chars)
This is why "we adopted Copilot and velocity went up" is not evidence of productivity. Self-reported velocity went up in the METR study too. By 20%. While actual completion time went up 19%. You need to measure what shipped, not what people believe shipped.

**9/** (271 chars)
What engineering leaders should measure instead: cycle time to merge (objective), defect escape rate post-AI adoption, security finding density per PR, cost-per-resolved-issue. Not developer satisfaction surveys. Not token counts. Not vibes.

**10/** (267 chars)
The authors' own caveat: "the influence of experimental artifacts cannot be entirely ruled out." Fair. But the perception gap is the headline regardless. Even if the slowdown is noise, the fact that devs consistently overestimate AI benefit is signal.

**11/** (227 chars)
If your AI coding strategy is built on self-reported productivity, you are flying blind. Instrument the pipeline. Measure what matters. Govern the blast radius. The tools are powerful. The intuitions about them are wrong.

---

SCHEDULING NOTE: Post Wednesday 9:00-10:00 AM ET. Research-heavy threads perform best mid-week when engineering leaders are in planning mode. Quote-tweet the arxiv link in post 2 for credibility signal.
