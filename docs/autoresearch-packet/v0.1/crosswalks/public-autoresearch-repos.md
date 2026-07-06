# Public Autoresearch Repositories Crosswalk

**Status**: candidate (not canon)
**Date**: 2026-07-06
**Purpose**: Bounded comparison of public autoresearch-style systems against the Autoresearch Packet v0.1 candidate schema.

> **Note on star counts**: All star/fork counts are point-in-time snapshots as of 2026-07-06 and will drift. They are labeled with `~` to indicate approximation.

## Fact Posture Legend

- **public-source fact**: Directly verifiable from GitHub repo, README, code, commits, or releases
- **local execution fact**: Would require running the code to verify (none in this document)
- **inferred design pattern**: Reasonable inference from documented behavior (clearly labeled)
- **non-claim**: Not applicable or not a feature of the system

---

## 1. karpathy/autoresearch

**Repo**: https://github.com/karpathy/autoresearch
**License**: MIT [public-source fact]
**Stars**: ~89,938 [public-source fact]
**Created**: 2026-03-06 [public-source fact]

### Repository structure
- `prepare.py` — fixed constants, data prep, evaluation (immutable) [public-source fact]
- `train.py` — model, optimizer, training loop (agent-modifiable) [public-source fact]
- `program.md` — agent instructions (human-authored) [public-source fact]
- `results.tsv` — experiment ledger (untracked by git) [public-source fact]
- `analysis.ipynb` — post-hoc analysis [public-source fact]

### Experiment definition
- No formal config schema. Experiments defined by direct code modification of `train.py` [public-source fact]
- Natural language instructions in `program.md` provide objectives and constraints [public-source fact]
- Mutable parameters: DEPTH, ASPECT_RATIO, HEAD_DIM, WINDOW_PATTERN, learning rates, TOTAL_BATCH_SIZE [public-source fact]

### Measurement
- Primary metric: `val_bpb` (validation bits per byte, minimize) [public-source fact]
- `evaluate_bpb()` in `prepare.py` (immutable) [public-source fact]
- Metric extraction: `grep "^val_bpb:" run.log` [public-source fact]
- Fixed eval constants: MAX_SEQ_LEN=2048, TIME_BUDGET=300, EVAL_TOKENS=40*524288 [public-source fact]

### Results ledger
- `results.tsv` — TSV, 5 columns: `commit val_bpb memory_gb status description` [public-source fact]
- Status values: `keep`, `discard`, `crash` [public-source fact]
- Append-only, untracked by git [public-source fact]

### Keep/discard
- Keep if `val_bpb` strictly improves (lower) [public-source fact]
- Discard: `git reset --hard` to previous commit [public-source fact]
- Crash: `git reset --hard`, log as crash [public-source fact]

### Safety/autonomy bounds
- Single file scope: agent only modifies `train.py` [public-source fact]
- Fixed 300s wall-clock time budget [public-source fact]
- No network access during loop [public-source fact]
- Git dirty check, VRAM pre-flight, script hash tracking [public-source fact]
- Runs indefinitely until manually interrupted [public-source fact]

### Receipt/audit
- `results.tsv`: complete append-only log (all attempts including crashes) [public-source fact]
- Git history: linear path of successful improvements only [public-source fact]
- `analysis.ipynb` for post-hoc analysis [public-source fact]

---

## 2. davebcn87/pi-autoresearch

**Repo**: https://github.com/davebcn87/pi-autoresearch
**License**: MIT [public-source fact]
**Stars**: 6,855 [public-source fact]
**Created**: 2026-03-11 [public-source fact]
**Latest release**: v1.4.0 (2026-05-06) [public-source fact]

### Repository structure
- `extensions/pi-autoresearch/` — TypeScript extension (index.ts, compaction.ts, hooks.ts, jsonl.ts) [public-source fact]
- `skills/autoresearch-create/` — skill definition with SKILL.md [public-source fact]
- Session files in `.auto/` subfolder [public-source fact]

### Experiment definition
- `autoresearch.config.json` with `workingDir`, `maxIterations` [public-source fact]
- Skill encodes per-domain knowledge (command, metric, direction, scope, ideas) [public-source fact]
- `.auto/prompt.md` — living session document [public-source fact]

### Measurement
- Benchmark script outputs `METRIC name=number` lines [public-source fact]
- Confidence score computed after ≥3 non-crashed experiments [public-source fact]

### Results ledger
- `.auto/log.jsonl` — append-only JSONL, one line per run [public-source fact]
- Fields: run number, status, metric, commit, description, ASI [public-source fact]

### Keep/discard
- Improved primary metric → `keep` (auto-commits) [public-source fact]
- Worse/equal → `discard` (auto-reverts via `git reset --hard`) [public-source fact]
- Run failure → `crash` (auto-reverts) [public-source fact]
- Checks failure → `checks_failed` (auto-reverts, blocks keep) [public-source fact]
- Confidence score is advisory only [public-source fact]

### Safety/autonomy bounds
- Optional `checks.sh` for tests/types/lint [public-source fact]
- `maxIterations` caps experiments per session [public-source fact]
- Optional metric-valued guards with regression thresholds [public-source fact]
- Scope deviations recorded with justification [public-source fact]

### Receipt/audit
- Git commit history per kept experiment [public-source fact]
- `.auto/log.jsonl` with all runs including discarded/crashed [public-source fact]
- `.auto/prompt.md` captures what was tried and why [public-source fact]

---

## 3. VectorInstitute/helix

**Repo**: https://github.com/VectorInstitute/helix
**License**: Apache-2.0 [public-source fact]
**Stars**: 18 [public-source fact]
**Created**: 2026-03-27 [public-source fact]

### Repository structure
- `src/helix/` — Python source (agent.py, runner.py, git.py) [public-source fact]
- Per-helix: `helix.yaml`, `program.md`, `experiments.tsv` [public-source fact]
- 99% test coverage [public-source fact]

### Experiment definition
- `helix.yaml` (YAML config) [public-source fact]
- Fields: `scope.editable`, `scope.readonly`, `metrics.primary.name`, `metrics.primary.optimize`, `metrics.evaluate.command`, `metrics.evaluate.timeout_seconds`, `metrics.evaluate.patterns` [public-source fact]

### Measurement
- Evaluation script outputs to stdout [public-source fact]
- Regex patterns extract metric values [public-source fact]
- Timeout enforced via `timeout_seconds` [public-source fact]

### Results ledger
- `experiments.tsv` — append-only TSV [public-source fact]
- Columns: `session commit tokens_per_sec bpb status description` (from helix-inference-opt example) [public-source fact]
- Status values: `keep`, `discard`, `crash` [public-source fact]

### Keep/discard
- Keep if primary metric improved AND secondary did not degrade [public-source fact]
- Discard: `git reset --hard HEAD~1` [public-source fact]

### Safety/autonomy bounds
- `scope.editable` restricts modifiable files [public-source fact]
- `scope.readonly` protects files [public-source fact]
- Fixed time budget per experiment [public-source fact]
- Agent-agnostic (ClaudeBackend, GeminiBackend, custom) [public-source fact]

### Receipt/audit
- Git history as research trail [public-source fact]
- `experiments.tsv` as append-only ledger [public-source fact]
- Each helix example is standalone git repo [public-source fact]

---

## 4. aiming-lab/AutoResearchClaw

**Repo**: https://github.com/aiming-lab/AutoResearchClaw
**License**: MIT [public-source fact]
**Stars**: 13,606 [public-source fact]
**Created**: 2026-03-15 [public-source fact]
**Latest release**: v0.5.0 (2026-05-20) [public-source fact]

### Repository structure
- `researchclaw/` — main package (config.py, adapters.py, cli.py) [public-source fact]
- `researchclaw/pipeline/` — 23-stage pipeline (stages.py, contracts.py, executor.py, runner.py) [public-source fact]
- `researchclaw/experiment/` — sandbox.py, runner.py, git_manager.py, validator.py [public-source fact]
- `researchclaw/verification/` — VerifiedRegistry (anti-fabrication) [public-source fact]

### Experiment definition
- YAML config with `project`, `research`, `experiment` sections [public-source fact]
- Experiment modes: sandbox, docker, simulated, ssh_remote, colab_drive [public-source fact]
- Fields: `metric_key`, `metric_direction`, `time_budget_sec`, `max_iterations` [public-source fact]

### Measurement
- Structured JSON metrics from experiment execution [public-source fact]
- Stage 14 generates `experiment_summary.json` and `results_table.tex` [public-source fact]
- NaN/Inf detection in Stage 12 guard [public-source fact]

### Results ledger
- `experiment_summary.json` — aggregated metrics [public-source fact]
- `runs/run-N.json` — individual results [public-source fact]
- Stage outputs in `stage-N/` directories [public-source fact]
- `pipeline_summary.json` — overall status [public-source fact]

### Keep/discard
- Stage 15 (RESEARCH_DECISION): PROCEED/PIVOT/ITERATE [public-source fact]
- Stage 13 (ITERATIVE_REFINE): Edit→Run→Evaluate loop [public-source fact]
- Stage 20 (QUALITY_GATE): final quality check [public-source fact]

### Safety/autonomy bounds
- 3 gate stages requiring approval: Stage 5, 9, 20 [public-source fact]
- Intervention modes: Full Auto, Gate Only, Checkpoint, Co-Pilot, Step-by-Step [public-source fact]
- Anti-fabrication: VerifiedRegistry enforces ground-truth data [public-source fact]
- AST syntax check, security scan, import check [public-source fact]
- SHA256 artifact checksums in `manifest.json` [public-source fact]
- Experiment diagnosis & repair loop (max 3 cycles) [public-source fact]

### Receipt/audit
- VerifiedRegistry: `verify_claim(metric_name, claimed_value)` [public-source fact]
- Unverified numbers sanitized during paper writing [public-source fact]
- `verification_report.json` — 4-layer citation integrity [public-source fact]
- Hard guards against experiment fabrication cascade [public-source fact]

---

## 5. THU-Team-Eureka/EurekAgent

**Repo**: https://github.com/THU-Team-Eureka/EurekAgent
**License**: AGPL-3.0 [public-source fact]
**Stars**: 37 [public-source fact]
**Created**: 2026-06-11 [public-source fact]

### Repository structure
- `examples/` — problem definitions [public-source fact]
- `hidden_eval_dir/` — private evaluators [public-source fact]
- Per-problem: `INSTRUCTION.md`, `SUBMISSION_FORMAT.md`, `hidden_eval_dir/evaluate.py` [public-source fact]

### Experiment definition
- Markdown-based: `INSTRUCTION.md` (problem) + `SUBMISSION_FORMAT.md` (JSON schema) [public-source fact]
- `evaluate.py` must implement `grade_submission()` and `is_better()` [public-source fact]

### Measurement
- Private `evaluate.py` is single source of truth [public-source fact]
- Score semantics stated in `INSTRUCTION.md` (minimize, maximize, approach target) [public-source fact]
- Invalid submissions return scores that can never be "best" [public-source fact]

### Results ledger
- Filesystem + Git history as shared long-term memory [public-source fact]
- Live web monitor with score evolution, budget usage, session transcripts [public-source fact]
- `monitor_snapshot.html` for offline review [public-source fact]

### Keep/discard
- `is_better(new_score, old_score)` function defined by user [public-source fact]
- Official scores automatically recorded and ranked [public-source fact]

### Safety/autonomy bounds
- Docker containers for agent work and grading (separate) [public-source fact]
- Hidden evaluator outside agent-visible workspace [public-source fact]
- Controller-owned files write-protected via OS hooks [public-source fact]
- GPU access: default-deny with single-session lock [public-source fact]
- Time and API cost budgets per stage [public-source fact]
- Human-in-the-loop optional at every step [public-source fact]

### Receipt/audit
- All run artifacts persisted under run directory [public-source fact]
- Git commits track solution evolution [public-source fact]
- Resumable from persisted state [public-source fact]

---

## 6. SakanaAI/AI-Scientist-v2

**Repo**: https://github.com/SakanaAI/AI-Scientist-v2
**License**: "The AI Scientist Source Code License" (derivative of Responsible AI License) [public-source fact]
**Stars**: 6,721 [public-source fact]
**Created**: 2025-04-08 [public-source fact]

### Repository structure
- `ai_scientist/ideas/` — topic descriptions and generated ideas [public-source fact]
- `ai_scientist/treesearch/` — tree search implementation [public-source fact]
- `experiments/<timestamp>_<ideaname>/` — per-experiment directories [public-source fact]
- `bfts_config.yaml` — best-first tree search config [public-source fact]

### Experiment definition
- `bfts_config.yaml` with nested sections for agent, search, execution, report [public-source fact]
- Key params: `num_workers`, `steps`, `num_seeds`, `max_debug_depth`, `debug_prob`, `num_drafts`, `exec.timeout` [public-source fact]
- Idea generation: Markdown topic with Title, Keywords, TL;DR, Abstract [public-source fact]

### Measurement
- `_define_global_metrics()` proposes metrics via LLM [public-source fact]
- Validation loss tracked separately [public-source fact]
- VLM (Vision-Language Model) critiques plots [public-source fact]

### Results ledger
- `unified_tree_viz.html` — tree visualization [public-source fact]
- Generated PDF paper per experiment [public-source fact]
- Stage journals, configs, tree plots, `manager.pkl` [public-source fact]
- Prompt logs per node in `phase_logs/` [public-source fact]

### Keep/discard
- `Journal.get_best_node()` picks among candidates [public-source fact]
- Stage transitions checked with `{is_complete, reasoning, missing_criteria}` [public-source fact]
- VLM plot check gates node advancement [public-source fact]
- Best-first tree search with node expansion [public-source fact]

### Safety/autonomy bounds
- README warning: "will execute LLM-written code" [public-source fact]
- Recommended sandbox (Docker) [public-source fact]
- Timeout: 3600s per node [public-source fact]
- Max debug depth: 3 attempts [public-source fact]
- Fixed node budgets per stage [public-source fact]
- Mandatory AI-use disclosure in manuscripts [public-source fact]

### Receipt/audit
- Tree visualization HTML [public-source fact]
- Complete prompt logs per node [public-source fact]
- Stage journals and manager state preserved [public-source fact]

---

## 7. microsoft/RD-Agent

**Repo**: https://github.com/microsoft/RD-Agent
**License**: MIT [public-source fact]
**Stars**: 13,504 [public-source fact]
**Created**: 2024-04-03 [public-source fact]
**Latest release**: v0.8.0 (2025-11-03) [public-source fact]

### Repository structure
- `rdagent/core/` — abstract framework classes [public-source fact]
- `rdagent/components/` — reusable components [public-source fact]
- `rdagent/scenarios/` — scenario-specific (fin_factor, fin_model, data_science) [public-source fact]
- `rdagent/app/` — applications per scenario [public-source fact]
- `rdagent/log/` — logging + Streamlit UI [public-source fact]

### Experiment definition
- YAML config per scenario [public-source fact]
- Environment variables for time segments (train/valid/test dates) [public-source fact]
- Pydantic settings classes [public-source fact]

### Measurement
- Scenario-specific metrics (e.g., Qlib performance for financial) [public-source fact]
- `Experiment2Feedback.generate_feedback()` includes comparison with previous [public-source fact]
- MLflow integration for logging [public-source fact]

### Results ledger
- MLflow logging [public-source fact]
- Streamlit UI: "All Loops", "Next Loop", "One Evolving" views [public-source fact]
- Log directories with full execution process [public-source fact]

### Keep/discard
- LLM-based comparison between previous results [public-source fact]
- `Experiment2Feedback` generates feedback [public-source fact]
- Configurable action selection (e.g., "bandit") [public-source fact]

### Safety/autonomy bounds
- Disclaimer: "provided 'as is', without warranty" [public-source fact]
- "Not ready-to-use for any financial investment or advice" [public-source fact]
- Users must independently assess risks [public-source fact]

### Receipt/audit
- MLflow tracking [public-source fact]
- Streamlit visualization [public-source fact]
- Comprehensive log directories [public-source fact]
- Benchmark data in JSON format [public-source fact]

---

## Cross-System Comparison Matrix

| Feature | autoresearch | pi-autoresearch | helix | AutoResearchClaw | EurekAgent | AI-Scientist-v2 | RD-Agent |
|---------|-------------|-----------------|-------|------------------|------------|-----------------|----------|
| Config format | Markdown | JSON + skill | YAML | YAML | Markdown | YAML | YAML + env |
| Ledger format | TSV | JSONL | TSV | JSON | Filesystem | HTML + pkl | MLflow |
| Metric direction | minimize | configurable | configurable | configurable | configurable | configurable | scenario-specific |
| Keep/discard | metric compare | metric + checks | metric + secondary | stage gates | is_better() | tree search | LLM comparison |
| Scope restriction | single file | optional | editable/readonly | sandbox modes | Docker isolation | sandbox recommended | scenario-specific |
| Time budget | 300s fixed | configurable | configurable | configurable | per-stage | 3600s per node | not specified |
| Auto-rollback | git reset | git reset | git reset | stage gates | Docker | debug limits | LLM feedback |
| Receipt/audit | results.tsv + git | log.jsonl + git | experiments.tsv + git | VerifiedRegistry | run artifacts | tree viz + prompt logs | MLflow + UI |
| Anti-fabrication | no | no | no | yes (VerifiedRegistry) | hidden evaluator | no | no |
| License | MIT | MIT | Apache-2.0 | MIT | AGPL-3.0 | custom | MIT |

**Classification**: inferred design pattern — the matrix above synthesizes public-source facts into a comparison structure. Individual cells are public-source facts; the matrix layout is a derived synthesis.

---

## Packet v0.1 Coverage Analysis

**Classification**: inferred design pattern

The Autoresearch Packet v0.1 schema covers the common denominator across these systems:

| Packet field | Covered in | Common denominator |
|-------------|-----------|-------------------|
| `objective.metric_name` | all 7 | every system has a named metric |
| `objective.metric_direction` | 6 of 7 | all except RD-Agent (scenario-specific) |
| `measurement.command` | 5 of 7 | autoresearch, pi-autoresearch, helix, AutoResearchClaw, EurekAgent |
| `measurement.deterministic` | 4 of 7 | autoresearch, helix, AutoResearchClaw, EurekAgent |
| `scope.editable` | 5 of 7 | autoresearch, helix, AutoResearchClaw, EurekAgent, RD-Agent |
| `scope.readonly` | 3 of 7 | autoresearch, helix, EurekAgent |
| `budget.type` | 6 of 7 | all except RD-Agent |
| `ledgers.experiments` | all 7 | every system records experiments |
| `ledgers.claims` | 2 of 7 | AutoResearchClaw (VerifiedRegistry), AI-Scientist-v2 (paper) |
| `safety.autonomy_level` | all 7 | all have some autonomy bounds |
| `safety.auto_rollback` | 4 of 7 | autoresearch, pi-autoresearch, helix, AutoResearchClaw |
| `fact_posture` | 0 of 7 | unique to HUMMBL governance layer |
