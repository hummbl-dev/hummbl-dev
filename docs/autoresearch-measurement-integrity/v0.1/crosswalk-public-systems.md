# Measurement Integrity Crosswalk: Public Systems

**Status**: candidate (not canon)
**Date**: 2026-07-06
**Issue**: [hummbl-dev/hummbl-dev#109](https://github.com/hummbl-dev/hummbl-dev/issues/109)

> **Note on star counts**: All star/fork counts are point-in-time snapshots as of 2026-07-06 and will drift. They are labeled with `~` to indicate approximation.

## Source class legend

- `[PRIM]` = primary source verified (README, code, or paper abstract read directly)
- `[SEC]` = secondary (search-surfaced, arXiv ID cited, full-text verification deferred)
- `[OBS]` = direct HUMMBL observation
- `[INF]` = inferred from documented behavior

---

## 1. karpathy/autoresearch

**Repo**: https://github.com/karpathy/autoresearch
**License**: MIT [PRIM]
**Stars**: ~89,938 [PRIM]

### Decision rule
- "checks if the result improved, keeps or discards, and repeats" [PRIM, README, verified 2026-07-06]
- `val_bpb` (minimize) — single metric, single seed [PRIM]
- No noise floor, no variance, no reseeded verification [PRIM]

### IC coverage

| IC | Covered? | Evidence |
|----|----------|----------|
| IC-1 (seed variance) | **No** | Single seed per run, no variance field [PRIM] |
| IC-2 (evaluator integrity) | **Partial** | `prepare.py` is immutable by convention, but no hash check enforces it [PRIM] |
| IC-3 (holdout provenance) | **Partial** | `VAL_SHARD=6542` is fixed, but no provenance declaration or path-isolation check [PRIM] |
| IC-4 (decision rule) | **No** | Naive improve-check, no threshold or reseed [PRIM] |
| IC-5 (failure receipt) | **Partial** | Crashes logged as `status=crash, val_bpb=0.000000`, but no error_code field [PRIM] |

**Summary**: The naive baseline. No integrity layer. This is the pattern #109 is designed to govern.

---

## 2. SakanaAI/AI-Scientist-v2

**Repo**: https://github.com/SakanaAI/AI-Scientist-v2
**License**: custom (AI Scientist Source Code License) [PRIM]
**Stars**: ~6,721 [PRIM]

### Decision rule
- `Journal.get_best_node()` picks among candidates [PRIM]
- Best-first tree search with node expansion [PRIM]
- VLM (Vision-Language Model) critiques plots, gating node advancement [PRIM]
- `num_seeds` configurable in `bfts_config.yaml` [PRIM]

### IC coverage

| IC | Covered? | Evidence |
|----|----------|----------|
| IC-1 (seed variance) | **Partial** | `num_seeds` configurable, but no noise_floor or delta-vs-variance gate [PRIM] |
| IC-2 (evaluator integrity) | **No** | No evaluator hash or integrity check documented [PRIM] |
| IC-3 (holdout provenance) | **No** | No holdout provenance declaration documented [PRIM] |
| IC-4 (decision rule) | **Partial** | Tree search selection is non-naive, but no explicit decision_rule field [PRIM] |
| IC-5 (failure receipt) | **Partial** | Failed nodes logged in tree, but no structured error_code [PRIM] |

---

## 3. microsoft/RD-Agent

**Repo**: https://github.com/microsoft/RD-Agent
**License**: MIT [PRIM]
**Stars**: ~13,504 [PRIM]

### Decision rule
- LLM-based comparison between previous results [PRIM]
- `Experiment2Feedback.generate_feedback()` includes comparison [PRIM]
- Configurable action selection (e.g., "bandit") [PRIM]
- MLflow logging for tracking [PRIM]

### IC coverage

| IC | Covered? | Evidence |
|----|----------|----------|
| IC-1 (seed variance) | **No** | No seed variance or noise floor documented [PRIM] |
| IC-2 (evaluator integrity) | **No** | No evaluator hash documented [PRIM] |
| IC-3 (holdout provenance) | **Partial** | Time-segment env vars (train/valid/test dates) provide temporal separation, but no path-isolation check [PRIM] |
| IC-4 (decision rule) | **Partial** | LLM-based comparison is non-naive, but no explicit decision_rule field [PRIM] |
| IC-5 (failure receipt) | **No** | No structured error_code in feedback documented [PRIM] |

---

## 4. VectorInstitute/helix

**Repo**: https://github.com/VectorInstitute/helix
**License**: Apache-2.0 [PRIM]
**Stars**: ~18 [PRIM]

### Decision rule
- Keep if primary metric improved AND secondary did not degrade [PRIM]
- Discard: `git reset --hard HEAD~1` [PRIM]
- Timeout enforced via `timeout_seconds` [PRIM]

### IC coverage

| IC | Covered? | Evidence |
|----|----------|----------|
| IC-1 (seed variance) | **No** | Single seed per run, no variance field [PRIM] |
| IC-2 (evaluator integrity) | **Partial** | `scope.readonly` protects evaluator file, but no hash check [PRIM] |
| IC-3 (holdout provenance) | **No** | No holdout provenance declaration documented [PRIM] |
| IC-4 (decision rule) | **Partial** | Multi-metric check (primary + secondary) is non-naive, but no noise floor or reseed [PRIM] |
| IC-5 (failure receipt) | **Partial** | Crashes logged as `status=crash`, but no error_code field [PRIM] |

---

## 5. davebcn87/pi-autoresearch

**Repo**: https://github.com/davebcn87/pi-autoresearch
**License**: MIT [PRIM]
**Stars**: ~6,855 [PRIM]

### Decision rule
- Improved primary metric → keep [PRIM]
- Worse/equal → discard [PRIM]
- Confidence score computed after ≥3 non-crashed experiments (advisory only) [PRIM]

### IC coverage

| IC | Covered? | Evidence |
|----|----------|----------|
| IC-1 (seed variance) | **Partial** | Confidence score uses noise floor after ≥3 runs, but is advisory only — never auto-rejects [PRIM] |
| IC-2 (evaluator integrity) | **No** | No evaluator hash documented [PRIM] |
| IC-3 (holdout provenance) | **No** | No holdout provenance documented [PRIM] |
| IC-4 (decision rule) | **Partial** | Confidence score is non-naive, but keep/discard is still raw improve-check [PRIM] |
| IC-5 (failure receipt) | **Partial** | `checks_failed` status exists, but no error_code field [PRIM] |

---

## 6. aiming-lab/AutoResearchClaw

**Repo**: https://github.com/aiming-lab/AutoResearchClaw
**License**: MIT [PRIM]
**Stars**: ~13,606 [PRIM]

### Decision rule
- Stage 15 (RESEARCH_DECISION): PROCEED/PIVOT/ITERATE [PRIM]
- Stage 13 (ITERATIVE_REFINE): Edit→Run→Evaluate loop [PRIM]
- Stage 20 (QUALITY_GATE): final quality check [PRIM]
- Anti-fabrication: VerifiedRegistry enforces ground-truth data [PRIM]

### IC coverage

| IC | Covered? | Evidence |
|----|----------|----------|
| IC-1 (seed variance) | **No** | No seed variance or noise floor documented [PRIM] |
| IC-2 (evaluator integrity) | **Partial** | VerifiedRegistry enforces ground-truth, but no evaluator hash [PRIM] |
| IC-3 (holdout provenance) | **No** | No holdout provenance documented [PRIM] |
| IC-4 (decision rule) | **Yes** | Multi-stage decision (PROCEED/PIVOT/ITERATE) with quality gate — non-naive, explicit [PRIM] |
| IC-5 (failure receipt) | **Yes** | NaN/Inf detection in Stage 12, hard guards against fabrication cascade [PRIM] |

---

## 7. THU-Team-Eureka/EurekAgent

**Repo**: https://github.com/THU-Team-Eureka/EurekAgent
**License**: AGPL-3.0 [PRIM]
**Stars**: ~37 [PRIM]

### Decision rule
- `is_better(new_score, old_score)` function defined by user [PRIM]
- Official scores automatically recorded and ranked [PRIM]
- Hidden evaluator outside agent-visible workspace [PRIM]

### IC coverage

| IC | Covered? | Evidence |
|----|----------|----------|
| IC-1 (seed variance) | **No** | No seed variance documented [PRIM] |
| IC-2 (evaluator integrity) | **Yes** | Hidden evaluator in separate Docker container, write-protected via OS hooks [PRIM] |
| IC-3 (holdout provenance) | **Partial** | Hidden test data outside agent workspace, but no provenance declaration [PRIM] |
| IC-4 (decision rule) | **Partial** | User-defined `is_better()` is explicit, but no noise floor or reseed [PRIM] |
| IC-5 (failure receipt) | **No** | No structured error_code documented [PRIM] |

---

## Cross-system IC coverage matrix (public systems)

| System | IC-1 | IC-2 | IC-3 | IC-4 | IC-5 |
|--------|------|------|------|------|------|
| karpathy/autoresearch | No | Partial | Partial | No | Partial |
| AI-Scientist-v2 | Partial | No | No | Partial | Partial |
| RD-Agent | No | No | Partial | Partial | No |
| helix | No | Partial | No | Partial | Partial |
| pi-autoresearch | Partial | No | No | Partial | Partial |
| AutoResearchClaw | No | Partial | No | Yes | Yes |
| EurekAgent | No | Yes | Partial | Partial | No |

**Classification**: [INF] — the matrix synthesizes public-source facts into a comparison structure. Individual cells are [PRIM]; the matrix layout is a derived synthesis.

**Key finding**: No public system covers all five integrity checks. IC-1 (seed variance) is the most universally missing — only pi-autoresearch computes a noise floor, and even there it's advisory. IC-2 (evaluator integrity) is strongest in EurekAgent (Docker isolation + OS hooks).

## HUMMBL v0.1 target state (not a public system)

This spec is a candidate, not a deployed system. The target state is shown separately to avoid blurring the public-system crosswalk:

| IC | Target | Note |
|----|--------|------|
| IC-1 | Yes | Seed variance gate with signed delta |
| IC-2 | Yes | Evaluator hash comparison |
| IC-3 | Yes | Holdout path isolation |
| IC-4 | Yes | Explicit decision rule + reseed |
| IC-5 | Yes | Error code required for failures |

If adopted, HUMMBL would be the first system to enforce all five as hard gates.
