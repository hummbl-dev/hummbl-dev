# HUMMBL Dev Branch Cleanup Audit - 2026-05-08

Read-only branch audit across non-archived hummbl-dev repositories.

No branches were deleted in this run. Deletion remains operator-gated.

## Classification Rules

| Status | Meaning |
|---|---|
| delete_candidate_merged_or_empty | Non-default branch has zero commits ahead of default and no open PR. Candidate for deletion after operator approval. |
| stale_low_ahead_review | Branch has 1-3 commits ahead but is far behind default. Needs human review before delete or salvage. |
| keep_unique_commits | Branch has unique work beyond the low-ahead stale threshold. Keep until reviewed. |
| keep_open_pr | Branch has an open PR. Do not delete. |
| skip_archived | Archived repo; no branch mutation recommended. |

## Summary

| Status | Count |
|---|---:|
| stale_low_ahead_review | 119 |
| keep_unique_commits | 106 |
| delete_candidate_merged_or_empty | 31 |
| keep_open_pr | 5 |
| skip_archived | 2 |

## Deletion Candidates

These are safe-looking candidates by graph shape only. Do not delete without an explicit operator approval pass.

| Repository | Branch | Default | Ahead | Behind | Protected |
|---|---|---|---:|---:|---|
| hummbl-dev/deer-flow | `copilot/refactor-channel-binding-logic` | `main` | 0 | 0 | False |
| hummbl-dev/founder-mode | `docs/claude/recon-and-research-2026-04-26` | `main` | 0 | 186 | False |
| hummbl-dev/HUMMBL-Unified-Tier-Framework | `copilot/fix-markdown-lint-errors-md040` | `main` | 0 | 8 | False |
| hummbl-dev/paramiko | `1.16` | `main` | 0 | 1989 | False |
| hummbl-dev/paramiko | `2.10` | `main` | 0 | 351 | False |
| hummbl-dev/paramiko | `2.11` | `main` | 0 | 307 | False |
| hummbl-dev/paramiko | `2.5` | `main` | 0 | 686 | False |
| hummbl-dev/paramiko | `2.6` | `main` | 0 | 627 | False |
| hummbl-dev/paramiko | `2.7` | `main` | 0 | 542 | False |
| hummbl-dev/paramiko | `2.8` | `main` | 0 | 443 | False |
| hummbl-dev/paramiko | `2.9` | `main` | 0 | 400 | False |
| hummbl-dev/paramiko | `2178-int` | `main` | 0 | 201 | False |
| hummbl-dev/paramiko | `3.0` | `main` | 0 | 198 | False |
| hummbl-dev/paramiko | `3.1` | `main` | 0 | 175 | False |
| hummbl-dev/paramiko | `3.2` | `main` | 0 | 108 | False |
| hummbl-dev/paramiko | `3.3` | `main` | 0 | 72 | False |
| hummbl-dev/paramiko | `3.4` | `main` | 0 | 39 | False |
| hummbl-dev/paramiko | `3.5` | `main` | 0 | 19 | False |
| hummbl-dev/paramiko | `387-auth-mark-ii` | `main` | 0 | 121 | False |
| hummbl-dev/paramiko | `4.0` | `main` | 0 | 0 | False |
| hummbl-dev/paramiko | `973-dsa-removal` | `main` | 0 | 16 | False |
| hummbl-dev/paramiko | `cve-2023-48795` | `main` | 0 | 60 | False |
| hummbl-dev/rich | `1717-jupyter-pretty` | `master` | 0 | 1875 | False |
| hummbl-dev/rich | `fix-detect-color` | `master` | 0 | 2107 | False |
| hummbl-dev/rich | `fix-tab-size` | `master` | 0 | 626 | False |
| hummbl-dev/rich | `meta-link` | `master` | 0 | 1009 | False |
| hummbl-dev/rich | `update-markdown-lib` | `master` | 0 | 789 | False |
| hummbl-dev/vllm | `amd_mori` | `main` | 0 | 6257 | False |
| hummbl-dev/vllm | `amd-ci` | `main` | 0 | 11089 | False |
| hummbl-dev/vllm | `andy-neuma-ibm-smoke` | `main` | 0 | 3092 | False |
| hummbl-dev/vllm | `consolidate-awq-into-awq-marlin` | `main` | 0 | 775 | False |

## Stale Low-Ahead Review Queue

First 80 branches with 1-3 unique commits and substantial drift. These are not deletion-approved; review or archive intent first.

| Repository | Branch | Default | Ahead | Behind | Protected |
|---|---|---|---:|---:|---|
| hummbl-dev/cli | `dependabot/github_actions/peter-evans/create-or-update-comment-3` | `master` | 1 | 52 | False |
| hummbl-dev/cli | `dependabot/github_actions/peter-evans/create-pull-request-5` | `master` | 1 | 52 | False |
| hummbl-dev/cli | `feature/term-headers` | `master` | 1 | 467 | False |
| hummbl-dev/cli | `fix-initial-number-escaping` | `master` | 1 | 75 | False |
| hummbl-dev/cli | `isidentical/refactors/color-system` | `master` | 1 | 83 | False |
| hummbl-dev/cli | `mickael/oss-76-http-prompt-merge` | `master` | 1 | 319 | False |
| hummbl-dev/deer-flow | `chore/demo` | `main` | 1 | 1523 | False |
| hummbl-dev/deer-flow | `docs/volcengine` | `main` | 1 | 1584 | False |
| hummbl-dev/deer-flow | `feat/actor-framework` | `main` | 2 | 178 | False |
| hummbl-dev/deer-flow | `feat/max-search-results` | `main` | 2 | 1614 | False |
| hummbl-dev/deer-flow | `feat/python-execution-result` | `main` | 1 | 1634 | False |
| hummbl-dev/deer-flow | `feat/rfc-001-auth-module` | `main` | 1 | 149 | False |
| hummbl-dev/deer-flow | `fix/deep-think` | `main` | 1 | 1530 | False |
| hummbl-dev/deer-flow | `fix/unittest` | `main` | 1 | 1610 | False |
| hummbl-dev/deer-flow | `main-1.x` | `main` | 3 | 1327 | False |
| hummbl-dev/deer-flow | `main-1.x-container` | `main` | 2 | 1327 | False |
| hummbl-dev/deer-flow | `rayhpeng/fix-gateway-api-configuration` | `main` | 1 | 167 | False |
| hummbl-dev/deer-flow | `refactor/use-conditional-edge` | `main` | 1 | 1595 | False |
| hummbl-dev/deer-flow | `xing.liu/langgraph_dev` | `main` | 1 | 1638 | False |
| hummbl-dev/deer-flow | `xing.liu/ut_check` | `main` | 1 | 1624 | False |
| hummbl-dev/founder-mode | `feat/claude/adr-fm-020-bus-authority-phased` | `main` | 1 | 103 | False |
| hummbl-dev/founder-mode | `feat/claude/autonomous-inference-stack` | `main` | 1 | 143 | False |
| hummbl-dev/markitdown | `joshbradley/add-file-input-support` | `main` | 1 | 111 | False |
| hummbl-dev/markitdown | `onenote` | `main` | 1 | 77 | False |
| hummbl-dev/markitdown | `zip_formats` | `main` | 1 | 74 | False |
| hummbl-dev/paramiko | `2.0` | `main` | 1 | 1496 | False |
| hummbl-dev/paramiko | `2.1` | `main` | 2 | 1303 | False |
| hummbl-dev/paramiko | `2.12` | `main` | 1 | 297 | False |
| hummbl-dev/paramiko | `2.2` | `main` | 3 | 1113 | False |
| hummbl-dev/paramiko | `2.4` | `main` | 2 | 833 | False |
| hummbl-dev/paramiko | `2342-compression-test-too-specific` | `main` | 1 | 297 | False |
| hummbl-dev/paramiko | `mermaid` | `main` | 3 | 176 | False |
| hummbl-dev/rich | `blank-lines-test` | `master` | 1 | 699 | False |
| hummbl-dev/rich | `dependabot/github_actions/codecov/codecov-action-5` | `master` | 1 | 306 | False |
| hummbl-dev/rich | `dependabot/github_actions/snok/install-poetry-1.4.1` | `master` | 1 | 450 | False |
| hummbl-dev/rich | `dependabot/pip/asv-0.6.4` | `master` | 1 | 327 | False |
| hummbl-dev/rich | `dependabot/pip/black-24.3.0` | `master` | 1 | 336 | False |
| hummbl-dev/rich | `dependabot/pip/black-24.8.0` | `master` | 1 | 333 | False |
| hummbl-dev/rich | `dependabot/pip/pygments-2.17.2` | `master` | 1 | 454 | False |
| hummbl-dev/rich | `dependabot/pip/pytest-8.3.4` | `master` | 1 | 306 | False |
| hummbl-dev/rich | `dependabot/pip/sphinx-8.1.3` | `master` | 1 | 322 | False |
| hummbl-dev/rich | `dependabot/pip/sphinx-copybutton-0.5.2` | `master` | 1 | 454 | False |
| hummbl-dev/rich | `divide` | `master` | 1 | 1145 | False |
| hummbl-dev/rich | `export-live` | `master` | 2 | 1138 | False |
| hummbl-dev/rich | `max-pretty-depth` | `master` | 1 | 1915 | False |
| hummbl-dev/rich | `migrate-to-cells` | `master` | 2 | 1844 | False |
| hummbl-dev/rich | `py314` | `master` | 1 | 174 | False |
| hummbl-dev/rich | `replace-cell-len-with-cells-lib` | `master` | 1 | 1887 | False |
| hummbl-dev/rich | `restore-function-locals` | `master` | 2 | 133 | False |
| hummbl-dev/rich | `style-link-id-cache` | `master` | 2 | 614 | False |
| hummbl-dev/rich | `typing-create-literal-type-for-console-color-system` | `master` | 1 | 1297 | False |
| hummbl-dev/rich | `v10.15.1` | `master` | 1 | 1988 | False |
| hummbl-dev/vllm | `7snzwi-codex/change-default-logging-behavior` | `main` | 1 | 8131 | False |
| hummbl-dev/vllm | `add-cuda-12.8-wheel` | `main` | 3 | 1864 | False |
| hummbl-dev/vllm | `batched_triton_fallback` | `main` | 1 | 4028 | False |
| hummbl-dev/vllm | `benchmark_serving_test` | `main` | 1 | 9326 | False |
| hummbl-dev/vllm | `bind_kv_caches` | `main` | 1 | 10951 | False |
| hummbl-dev/vllm | `builder-cuda-version` | `main` | 3 | 1896 | False |
| hummbl-dev/vllm | `builder-nvcc-toolchain` | `main` | 2 | 1896 | False |
| hummbl-dev/vllm | `bump_numba` | `main` | 2 | 2570 | False |
| hummbl-dev/vllm | `ci/macos-arm-wheel` | `main` | 3 | 1015 | False |
| hummbl-dev/vllm | `ci/reorder-release-pipeline` | `main` | 3 | 100 | False |
| hummbl-dev/vllm | `claude/nervous-meitner` | `main` | 3 | 958 | False |
| hummbl-dev/vllm | `claude/optimize-weight-loading-7FlLd` | `main` | 1 | 942 | False |
| hummbl-dev/vllm | `claude/review-vllm-quantization-rfc-cGHDF` | `main` | 3 | 920 | False |
| hummbl-dev/vllm | `codex/add-auto-max-model-length-setting` | `main` | 1 | 6871 | False |
| hummbl-dev/vllm | `codex/add-pandas-and-datasets-to-requirements` | `main` | 1 | 8948 | False |
| hummbl-dev/vllm | `codex/change-default-logging-behavior` | `main` | 1 | 8131 | False |
| hummbl-dev/vllm | `codex/remove-raydistributedexecutor-from-v0-engine` | `main` | 2 | 6257 | False |
| hummbl-dev/vllm | `codex/remove-vllm-v0-engine-references-from-docs` | `main` | 1 | 5713 | False |
| hummbl-dev/vllm | `codex/update-arch-overview-md-with-vllm-v1-details` | `main` | 1 | 9325 | False |
| hummbl-dev/vllm | `compile-only-pr1` | `main` | 1 | 481 | False |
| hummbl-dev/vllm | `convert-deepseek-tests-to-b200` | `main` | 1 | 1904 | False |
| hummbl-dev/vllm | `copilot/add-sp-min-token-to-e2e-tests` | `main` | 2 | 643 | False |
| hummbl-dev/vllm | `copilot/fix-31e676e9-a4af-4ed2-b74d-19d27f0a57b2` | `main` | 3 | 6316 | False |
| hummbl-dev/vllm | `copilot/fix-56244f30-e76a-41ed-beaf-3bc9de22a2c9` | `main` | 2 | 7024 | False |
| hummbl-dev/vllm | `copilot/fix-584be906-f283-4e17-8776-c14111357ee7` | `main` | 2 | 7017 | False |
| hummbl-dev/vllm | `copilot/fix-cudagraph-flag-combination` | `main` | 2 | 6630 | False |
| hummbl-dev/vllm | `correct-docs-cuda-version` | `main` | 1 | 11848 | False |
| hummbl-dev/vllm | `cuda-toolchain-override` | `main` | 1 | 1867 | False |
