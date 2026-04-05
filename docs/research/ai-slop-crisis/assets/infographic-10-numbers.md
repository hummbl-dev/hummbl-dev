# The AI Code Crisis in 10 Numbers

**Asset type:** Infographic brief for designer (Canva, Figma, or manual layout)
**Brand:** HUMMBL
**Date:** 2026-04-05
**Source corpus:** `/docs/research/ai-slop-crisis/` (5 rounds, 12 lanes, all citations verified)

---

## Design Specifications

### Dimensions
- **Primary:** 1080 x 1350 px (Instagram / LinkedIn portrait)
- **Secondary:** 1200 x 628 px (OG image / Twitter landscape card)

### Color Palette
| Role | Hex | Usage |
|------|-----|-------|
| Background | `#1a1a1a` | Full bleed dark background |
| Primary accent | `#16a34a` | Big numbers, divider lines, HUMMBL logo mark |
| Secondary accent | `#22d3ee` | Source attributions, footnote text |
| Body text | `#ffffff` | Context lines |
| Muted text | `#a3a3a3` | Source citations below each stat |

### Typography
| Role | Font | Weight | Size (portrait) |
|------|------|--------|-----------------|
| Title | Crimson Pro | 700 | 48px |
| Big number | Inter | 800 | 72px |
| Context line | Inter | 400 | 20px |
| Source attribution | Inter | 300 italic | 14px |
| Footer | Inter | 400 | 12px |

### Layout
- **Portrait (1080x1350):** 2-column x 5-row grid. Each cell is a stat block. Title block spans full width at top. Footer spans full width at bottom.
- **Landscape (1200x628):** Single row of 10 stat blocks scrolling left-to-right, or 2 rows x 5 cols compressed. Title left-aligned, footer right-aligned.
- Each stat block: 16px padding, 1px `#16a34a` left border accent.
- Stat blocks separated by 8px vertical gap.

---

## Title Block

```
THE AI CODE CRISIS
IN 10 NUMBERS

HUMMBL | AI Governance Primitives
```

HUMMBL logo mark top-right. Subtitle in `#a3a3a3`.

---

## 10 Stat Blocks (in narrative order)

### 1. The Scale

**42%**
of code in production is now AI-generated

_Source: Sonar State of Code 2026, n=1,100+ developers_

---

### 2. The Vulnerability Multiplier

**2.74x**
more vulnerable than human-written code

_Source: Veracode GenAI Code Security Report 2025, 100+ LLMs, 4 languages_

---

### 3. The Plateau

**~55%**
security pass rate -- stuck for 2 years despite model improvements

_Source: Veracode State of Software Security, Spring 2026_

---

### 4. The Sample Evidence

**25.1%**
of AI code samples had confirmed vulnerabilities

_Source: AppSec Santa 2026, 6 LLMs, 534 samples, OWASP Top 10_

---

### 5. The Productivity Inversion

**19%**
slower with AI tools (experienced developers, mature codebases)

_Source: METR RCT 2025, arxiv 2507.09089, N=16 devs, 246 tasks_

---

### 6. The Perception Gap

**39pp**
swing between what devs believe (+20% faster) and reality (-19% slower)

_Source: METR RCT 2025, post-task self-estimate vs. measured outcome_

---

### 7. The Adoption Wave

**75%**
of enterprises plan agentic AI deployment within 2 years

_Source: Deloitte State of AI 2026_

---

### 8. The Governance Deficit

**21%**
have a mature model for agent governance

_Source: Deloitte State of AI 2026_

---

### 9. The Leadership Signal

**38.5%**
of Fortune 1000 now have a Chief AI Officer (+5.4pp YoY)

_Source: MIT AI Leadership Benchmark, n~110 (up from 33.1%)_

---

### 10. The Regulatory Hammer

**EUR 35M / 7%**
of global revenue -- EU AI Act penalties, enforcement live Aug 2, 2026

_Source: EU AI Act, Annex III high-risk systems; Finland enforcing since Jan 2026_

---

## Footer Block

```
Sources verified against primary publications. Full evidence pack:
github.com/hummbl-dev/docs/research/ai-slop-crisis | hummbl.io/tracker

HUMMBL -- Open-source AI governance primitives.
Stdlib-only. Air-gap capable. Runtime evidence at every agent call.
```

---

## Designer Notes

- The narrative arc is: scale of the problem (1-4) -> productivity reality check (5-6) -> enterprise adoption rushing ahead (7-8) -> organizational response forming (9) -> regulatory deadline forcing action (10).
- Stats 7 and 8 are the "punchline pair" -- 75% deploying vs 21% governed. Consider visual emphasis (larger type, highlight box, or contrasting background panel).
- For the landscape/OG version, stats can be abbreviated to number + 3-word label (e.g., "42% AI-Generated") with sources collapsed into a single footer line.
- All numbers come from the HUMMBL research corpus with primary-source verification completed in Round 5 Lane G. No numbers are fabricated or estimated.
