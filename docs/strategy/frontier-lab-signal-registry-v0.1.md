# Frontier Lab Signal Registry v0.1

**Status: SOURCE-GROUNDED — NON-CANON — RE-CHECK REQUIRED BEFORE MERGE**

Issue: hummbl-dev/hummbl-dev#141
Observation date: 2026-07-10

## Purpose

A bounded, source-grounded registry tracking major frontier-lab platform shifts so HUMMBL / Ownward / Codex routing can reason from signals without turning vendor announcements into architecture dependencies or canon.

This is a living registry seed, not a one-time market report.

## Posture

- Source-grounded: official sources preferred; non-official claims marked
- Dated: observation date stated per row
- Non-canon: all entries are candidates, not doctrine
- Re-check-required: re-verify before merge or downstream architectural use
- Vendor-neutral: no lab is adopted as an architectural dependency

## Registry fields

| Field | Meaning |
|-------|---------|
| `lab_or_platform` | Lab, platform, or model family name |
| `latest_observed_signal` | Short, source-grounded summary of latest meaningful shift |
| `observation_date` | Date sources were reviewed |
| `source_links` | Official sources first; credible news only when official unavailable |
| `source_posture` | Official / press / paper / repo / unverified / mixed |
| `model_or_runtime_surface` | Model, agent, app, API, IDE, voice, cloud, local, or enterprise surface |
| `agentic_relevance` | Low / medium / high + one sentence |
| `coding_relevance` | Low / medium / high + one sentence |
| `voice_multimodal_relevance` | Low / medium / high + one sentence |
| `enterprise_or_sovereign_posture` | Enterprise, on-prem, cloud, regulated, sovereign, open-weight, etc. |
| `data_governance_risk` | Privacy, retention, jurisdiction, export-control, sensitive-data notes |
| `HUMMBL_impact` | Practical implication for HUMMBL governance / BaseN / public docs |
| `Ownward_impact` | Practical implication for voice-first coaching runtime / safety / UX |
| `Codex_agent_impact` | Practical implication for repo work, code migration, research, benchmarks |
| `routing_recommendation` | observe / benchmark / use-with-public-data / private-data-prohibited / premium-lane / fallback-lane / no-action |
| `open_questions` | What needs future verification |

## Registry rows

### 1. OpenAI

- **lab_or_platform**: OpenAI
- **latest_observed_signal**: ChatGPT Work — delegated execution surface for multi-step tasks; GPT-5.6 model family; agent runtime expansion
- **observation_date**: 2026-07-10
- **source_links**: https://openai.com/index/chatgpt-for-your-most-ambitious-work/ , https://openai.com/chatgpt-work/ , https://openai.com/index/gpt-5-6/
- **source_posture**: official
- **model_or_runtime_surface**: Model (GPT-5.6), app (ChatGPT), agent (ChatGPT Work), API, IDE (Codex), enterprise
- **agentic_relevance**: High — ChatGPT Work and Codex are agentic execution surfaces
- **coding_relevance**: High — Codex is a repo-aware code agent
- **voice_multimodal_relevance**: Medium — voice mode exists but not frontier-setting for voice-first coaching
- **enterprise_or_sovereign_posture**: Cloud, enterprise (ChatGPT Enterprise), API
- **data_governance_risk**: US jurisdiction; enterprise data retention policies vary; consumer data used for training by default (opt-out available)
- **HUMMBL_impact**: ChatGPT Work is a candidate execution lane for bounded tasks; Codex is a code implementation lane; neither replaces HUMMBL governance
- **Ownward_impact**: Voice mode is a reference signal but not a runtime dependency; Ownward remains vendor-neutral
- **Codex_agent_impact**: Codex (the OpenAI product) is a parallel to Codex (the HUMMBL agent identity) — naming collision requires careful disambiguation
- **routing_recommendation**: observe + use-with-public-data
- **open_questions**: ChatGPT Work tool-use boundaries, data retention for enterprise, long-horizon task reliability

### 2. Anthropic

- **lab_or_platform**: Anthropic
- **latest_observed_signal**: Claude model family expansion; Claude Code (agentic coding); safety research leadership; enterprise API
- **observation_date**: 2026-07-10
- **source_links**: https://www.anthropic.com/ , https://docs.anthropic.com/
- **source_posture**: official
- **model_or_runtime_surface**: Model (Claude), agent (Claude Code), API, enterprise
- **agentic_relevance**: High — Claude Code is an agentic coding surface; tool use is core
- **coding_relevance**: High — Claude Code is a direct coding agent
- **voice_multimodal_relevance**: Low — no voice-first surface
- **enterprise_or_sovereign_posture**: Cloud, enterprise API
- **data_governance_risk**: US jurisdiction; enterprise data not used for training by default; consumer data has opt-out
- **HUMMBL_impact**: Claude is a primary model for HUMMBL agent sessions; Claude Code is a coding lane
- **Ownward_impact**: Low — no voice surface
- **Codex_agent_impact**: Claude Code is a peer coding agent; HUMMBL Codex agent uses Claude models
- **routing_recommendation**: observe + use-with-public-data
- **open_questions**: Long-horizon agent reliability, enterprise data governance details

### 3. Google DeepMind / Gemini

- **lab_or_platform**: Google DeepMind / Gemini
- **latest_observed_signal**: Gemini model family; multimodal capabilities; Vertex AI enterprise lane; agent framework
- **observation_date**: 2026-07-10
- **source_links**: https://deepmind.google/ , https://ai.google.dev/
- **source_posture**: official
- **model_or_runtime_surface**: Model (Gemini), API (Vertex AI), cloud, enterprise
- **agentic_relevance**: Medium — agent frameworks emerging but not frontier-setting for agentic coding
- **coding_relevance**: Medium — code generation capabilities growing
- **voice_multimodal_relevance**: High — multimodal including audio; Google Assistant integration
- **enterprise_or_sovereign_posture**: Cloud (GCP), enterprise (Vertex AI), sovereign options
- **data_governance_risk**: US jurisdiction with regional data controls; Google Cloud data governance policies apply
- **HUMMBL_impact**: Gemini is a candidate research and synthesis lane; multimodal is relevant for evidence ingestion
- **Ownward_impact**: High — multimodal and voice capabilities are directly relevant to voice-first coaching
- **Codex_agent_impact**: Gemini CLI is a research lane agent in HUMMBL; coding relevance growing
- **routing_recommendation**: observe + benchmark
- **open_questions**: Agent runtime maturity, enterprise data residency, voice API stability

### 4. xAI / Grok

- **lab_or_platform**: xAI / Grok
- **latest_observed_signal**: Grok model family; X integration; real-time data access via X platform
- **observation_date**: 2026-07-10
- **source_links**: https://x.ai/ , https://x.com/grok
- **source_posture**: official
- **model_or_runtime_surface**: Model (Grok), app (X/Grok), API
- **agentic_relevance**: Low — primarily conversational, not agentic execution
- **coding_relevance**: Low — not a coding agent surface
- **voice_multimodal_relevance**: Low — no voice-first surface
- **enterprise_or_sovereign_posture**: Cloud, consumer (X integration)
- **data_governance_risk**: US jurisdiction; X data used for training; limited enterprise governance
- **HUMMBL_impact**: Low — signal monitoring only
- **Ownward_impact**: Low
- **Codex_agent_impact**: Low
- **routing_recommendation**: observe
- **open_questions**: Enterprise API maturity, data governance for non-X use cases

### 5. Meta AI

- **lab_or_platform**: Meta AI
- **latest_observed_signal**: Llama model family (open-weight); Llama 4 series; research leadership in open-weight frontier
- **observation_date**: 2026-07-10
- **source_links**: https://ai.meta.com/ , https://github.com/meta-llama
- **source_posture**: official
- **model_or_runtime_surface**: Model (Llama), open-weight, repo (GitHub)
- **agentic_relevance**: Medium — open-weight models enable custom agent stacks
- **coding_relevance**: Medium — code-capable variants exist (Llama Code)
- **voice_multimodal_relevance**: Medium — multimodal models in research
- **enterprise_or_sovereign_posture**: Open-weight (self-hostable), enterprise (via partners)
- **data_governance_risk**: Open-weight models can be self-hosted (data stays on-prem); no vendor data governance for self-hosted
- **HUMMBL_impact**: Open-weight models are candidates for on-prem/private-data lanes
- **Ownward_impact**: Medium — open-weight voice models could enable private voice coaching
- **Codex_agent_impact**: Medium — open-weight code models for private/local development
- **routing_recommendation**: observe + benchmark (especially for private-data lanes)
- **open_questions**: Llama 4 capability frontier, open-weight license terms, local inference feasibility

### 6. Mistral AI

- **lab_or_platform**: Mistral AI
- **latest_observed_signal**: Mistral model family; mixture-of-experts architecture; European AI sovereignty positioning
- **observation_date**: 2026-07-10
- **source_links**: https://mistral.ai/ , https://docs.mistral.ai/
- **source_posture**: official
- **model_or_runtime_surface**: Model (Mistral), API (La Plateforme), open-weight (some models), enterprise
- **agentic_relevance**: Medium — agent capabilities emerging
- **coding_relevance**: Medium — Codestral code model
- **voice_multimodal_relevance**: Low
- **enterprise_or_sovereign_posture**: Cloud, enterprise, European sovereign positioning, open-weight (some)
- **data_governance_risk**: EU jurisdiction (GDPR-aligned); European data governance is a differentiator
- **HUMMBL_impact**: European sovereignty lane is relevant for EU governance work; Codestral is a coding candidate
- **Ownward_impact**: Low
- **Codex_agent_impact**: Medium — Codestral for code generation
- **routing_recommendation**: observe + benchmark
- **open_questions**: Enterprise API maturity, agent runtime capabilities

### 7. Cohere

- **lab_or_platform**: Cohere
- **latest_observed_signal**: Command model family; enterprise-focused RAG and retrieval; multilingual leadership
- **observation_date**: 2026-07-10
- **source_links**: https://cohere.com/ , https://docs.cohere.com/
- **source_posture**: official
- **model_or_runtime_surface**: Model (Command), API, enterprise
- **agentic_relevance**: Low — primarily RAG and retrieval, not agentic execution
- **coding_relevance**: Low
- **voice_multimodal_relevance**: Low
- **enterprise_or_sovereign_posture**: Cloud, enterprise, data privacy focus
- **data_governance_risk**: US/Canada jurisdiction; enterprise data not used for training; strong privacy posture
- **HUMMBL_impact**: RAG/retrieval capabilities relevant for cognition layer
- **Ownward_impact**: Low
- **Codex_agent_impact**: Low
- **routing_recommendation**: observe (RAG/retrieval lane)
- **open_questions**: Agent capabilities, multilingual enterprise features

### 8. Microsoft AI / Copilot

- **lab_or_platform**: Microsoft AI / Copilot
- **latest_observed_signal**: Copilot model stack; enterprise integration (Microsoft 365); Azure AI; Phi small models
- **observation_date**: 2026-07-10
- **source_links**: https://www.microsoft.com/en-us/ai , https://learn.microsoft.com/en-us/ai/
- **source_posture**: official
- **model_or_runtime_surface**: Model (Copilot, Phi), app (Microsoft 365), cloud (Azure AI), enterprise
- **agentic_relevance**: Medium — Copilot has agent-like capabilities within Microsoft ecosystem
- **coding_relevance**: Medium — GitHub Copilot is a coding surface (separate from OpenAI Codex)
- **voice_multimodal_relevance**: Medium — voice in Microsoft ecosystem
- **enterprise_or_sovereign_posture**: Cloud (Azure), enterprise (Microsoft 365), sovereign (Azure Government)
- **data_governance_risk**: US jurisdiction; Azure data governance policies; enterprise data isolation available
- **HUMMBL_impact**: Azure AI is a candidate cloud lane; Phi models are candidates for edge/local inference
- **Ownward_impact**: Low — not a voice-first coaching surface
- **Codex_agent_impact**: Medium — GitHub Copilot is a coding assistant (distinct from HUMMBL Codex agent)
- **routing_recommendation**: observe
- **open_questions**: Copilot agent runtime maturity, Phi model capability frontier

### 9. Amazon Nova / Bedrock

- **lab_or_platform**: Amazon Nova / Bedrock
- **latest_observed_signal**: Nova model family; Bedrock multi-model platform; enterprise cloud AI
- **observation_date**: 2026-07-10
- **source_links**: https://aws.amazon.com/ai/ , https://aws.amazon.com/bedrock/
- **source_posture**: official
- **model_or_runtime_surface**: Model (Nova), cloud (Bedrock), enterprise
- **agentic_relevance**: Medium — Bedrock agent capabilities
- **coding_relevance**: Low
- **voice_multimodal_relevance**: Medium — Nova has multimodal capabilities
- **enterprise_or_sovereign_posture**: Cloud (AWS), enterprise, sovereign (AWS GovCloud)
- **data_governance_risk**: US jurisdiction; AWS data governance; enterprise data isolation
- **HUMMBL_impact**: Bedrock is a candidate multi-model cloud lane
- **Ownward_impact**: Low
- **Codex_agent_impact**: Low
- **routing_recommendation**: observe
- **open_questions**: Nova capability frontier, Bedrock agent runtime maturity

### 10. DeepSeek

- **lab_or_platform**: DeepSeek
- **latest_observed_signal**: DeepSeek-V3 / R1 reasoning models; open-weight releases; cost-efficient training claims
- **observation_date**: 2026-07-10
- **source_links**: https://www.deepseek.com/ , https://github.com/deepseek-ai
- **source_posture**: official + repo
- **model_or_runtime_surface**: Model (DeepSeek), open-weight, repo (GitHub)
- **agentic_relevance**: Low — primarily model provider, not agent runtime
- **coding_relevance**: Medium — code-capable models
- **voice_multimodal_relevance**: Low
- **enterprise_or_sovereign_posture**: Open-weight (self-hostable), cloud (DeepSeek API)
- **data_governance_risk**: China jurisdiction for API; open-weight models can be self-hosted (data stays on-prem); export-control considerations
- **HUMMBL_impact**: Open-weight reasoning models are candidates for private-data lanes; jurisdictional risk for API use
- **Ownward_impact**: Low
- **Codex_agent_impact**: Medium — code-capable open-weight models for local development
- **routing_recommendation**: observe + benchmark (open-weight only; private-data-prohibited for API)
- **open_questions**: Model capability verification, export-control implications, open-weight license terms

### 11. Alibaba Qwen

- **lab_or_platform**: Alibaba Qwen
- **latest_observed_signal**: Qwen model family; open-weight releases; multilingual; code-capable variants
- **observation_date**: 2026-07-10
- **source_links**: https://qwenlm.github.io/ , https://github.com/QwenLM
- **source_posture**: official + repo
- **model_or_runtime_surface**: Model (Qwen), open-weight, repo (GitHub), API
- **agentic_relevance**: Medium — agent capabilities emerging
- **coding_relevance**: Medium — Qwen-Coder variants
- **voice_multimodal_relevance**: Medium — Qwen-Audio variants
- **enterprise_or_sovereign_posture**: Open-weight (self-hostable), cloud (Alibaba Cloud), China sovereign
- **data_governance_risk**: China jurisdiction for API; open-weight models self-hostable; export-control considerations
- **HUMMBL_impact**: Open-weight models are candidates for private-data lanes; jurisdictional risk for API
- **Ownward_impact**: Medium — Qwen-Audio for voice research
- **Codex_agent_impact**: Medium — Qwen-Coder for local code generation
- **routing_recommendation**: observe + benchmark (open-weight only; private-data-prohibited for API)
- **open_questions**: Model capability frontier, license terms, export-control

### 12. Moonshot / Kimi

- **lab_or_platform**: Moonshot / Kimi
- **latest_observed_signal**: Kimi model; long-context capabilities; Chinese consumer AI market
- **observation_date**: 2026-07-10
- **source_links**: https://www.moonshot.cn/ , https://kimi.moonshot.cn/
- **source_posture**: official
- **model_or_runtime_surface**: Model (Kimi), app (Kimi), API
- **agentic_relevance**: Low — primarily conversational
- **coding_relevance**: Low
- **voice_multimodal_relevance**: Low
- **enterprise_or_sovereign_posture**: Cloud, China consumer market
- **data_governance_risk**: China jurisdiction; data governance under Chinese law
- **HUMMBL_impact**: Low — signal monitoring only
- **Ownward_impact**: Low
- **Codex_agent_impact**: Low
- **routing_recommendation**: observe
- **open_questions**: Long-context capability verification, API availability outside China

### 13. Z.ai / GLM

- **lab_or_platform**: Z.ai / GLM (Zhipu AI)
- **latest_observed_signal**: GLM model family; open-weight releases (ChatGLM); Chinese frontier lab
- **observation_date**: 2026-07-10
- **source_links**: https://www.zhipuai.cn/ , https://github.com/THUDM
- **source_posture**: official + repo
- **model_or_runtime_surface**: Model (GLM), open-weight, repo (GitHub), API
- **agentic_relevance**: Medium — agent capabilities emerging
- **coding_relevance**: Medium — code-capable variants
- **voice_multimodal_relevance**: Low
- **enterprise_or_sovereign_posture**: Open-weight (self-hostable), cloud, China sovereign
- **data_governance_risk**: China jurisdiction for API; open-weight self-hostable; export-control considerations
- **HUMMBL_impact**: Open-weight models are candidates for private-data lanes
- **Ownward_impact**: Low
- **Codex_agent_impact**: Medium — code-capable open-weight models
- **routing_recommendation**: observe + benchmark (open-weight only; private-data-prohibited for API)
- **open_questions**: Model capability frontier, license terms

### 14. ByteDance / Doubao

- **lab_or_platform**: ByteDance / Doubao
- **latest_observed_signal**: Doubao model family; Chinese consumer AI; ByteDance AI infrastructure
- **observation_date**: 2026-07-10
- **source_links**: https://www.volcengine.com/ , https://www.doubao.com/
- **source_posture**: official
- **model_or_runtime_surface**: Model (Doubao), app, API (Volcano Engine)
- **agentic_relevance**: Low
- **coding_relevance**: Low
- **voice_multimodal_relevance**: Low
- **enterprise_or_sovereign_posture**: Cloud (Volcano Engine), China consumer
- **data_governance_risk**: China jurisdiction; data governance under Chinese law
- **HUMMBL_impact**: Low — signal monitoring only
- **Ownward_impact**: Low
- **Codex_agent_impact**: Low
- **routing_recommendation**: observe
- **open_questions**: Enterprise API maturity, capability verification

### 15. Baidu / ERNIE

- **lab_or_platform**: Baidu / ERNIE
- **latest_observed_signal**: ERNIE model family; Chinese search-integrated AI; enterprise API
- **observation_date**: 2026-07-10
- **source_links**: https://yiyan.baidu.com/ , https://cloud.baidu.com/
- **source_posture**: official
- **model_or_runtime_surface**: Model (ERNIE), app (Ernie Bot), API (Baidu Cloud), enterprise
- **agentic_relevance**: Low
- **coding_relevance**: Low
- **voice_multimodal_relevance**: Low
- **enterprise_or_sovereign_posture**: Cloud (Baidu Cloud), China enterprise
- **data_governance_risk**: China jurisdiction; data governance under Chinese law
- **HUMMBL_impact**: Low — signal monitoring only
- **Ownward_impact**: Low
- **Codex_agent_impact**: Low
- **routing_recommendation**: observe
- **open_questions**: Enterprise capability, API availability outside China

### 16. Tencent / Hunyuan

- **lab_or_platform**: Tencent / Hunyuan
- **latest_observed_signal**: Hunyuan model family; Tencent Cloud integration; WeChat AI; Manus agent adjacency
- **observation_date**: 2026-07-10
- **source_links**: https://hunyuan.tencent.com/ , https://cloud.tencent.com/
- **source_posture**: official
- **model_or_runtime_surface**: Model (Hunyuan), app (WeChat), API (Tencent Cloud), enterprise
- **agentic_relevance**: Medium — Manus agent adjacency reported
- **coding_relevance**: Low
- **voice_multimodal_relevance**: Medium — WeChat voice integration
- **enterprise_or_sovereign_posture**: Cloud (Tencent Cloud), China enterprise, sovereign
- **data_governance_risk**: China jurisdiction; data governance under Chinese law
- **HUMMBL_impact**: Low — signal monitoring; Manus agent adjacency is an open question
- **Ownward_impact**: Low
- **Codex_agent_impact**: Low
- **routing_recommendation**: observe
- **open_questions**: Manus agent relationship, enterprise API maturity

## Omitted or deferred labs

- **Stability AI**: Deferred — primarily image/video generation, not directly relevant to HUMMBL/Ownward/Codex routing at this time
- **Perplexity**: Deferred — primarily search/consumer, not a frontier model lab
- **Reka**: Deferred — emerging; insufficient signal for routing impact
- **01.AI (Yi)**: Deferred — open-weight models but limited recent signal
- **AI21 Labs**: Deferred — enterprise LLM but limited frontier signal
- **Inflection AI**: Deferred — pivoted to enterprise; limited current frontier signal

## Non-goals

- Do not canonize new HUMMBL/BaseN/Ownward terminology
- Do not pick winners
- Do not rewrite the public README except for a minimal link if clearly warranted
- Do not create model-routing production rules from unverified announcements
- Do not treat marketing claims as verified benchmark results
- Do not send private repo, user, health, legal, financial, or governance-canon data to any external model as part of this task
- Do not adopt any vendor as an architectural dependency

## Related work

- #139 — ChatGPT Work platform-signal intake and routing distinction
- #140 — Frontier Lab Classification v0.1 (multidimensional classification framework)
- #124 — Ownward Voice Runtime Abstraction v0.1 / GPT-Live readiness

## Receipt

- **Issue**: hummbl-dev/hummbl-dev#141
- **Observation date**: 2026-07-10
- **Labs covered**: 16 (all initial rows attempted)
- **Omitted/deferred**: 6 (with notes)
- **Source posture**: official preferred; all rows cite official sources
- **Canonical status**: non-canon
- **Review status**: PENDING — re-check sources before merge
- **Routing recommendations**: observe (default), benchmark (where capability is relevant), use-with-public-data (for trusted APIs), private-data-prohibited (for China-jurisdiction APIs)
