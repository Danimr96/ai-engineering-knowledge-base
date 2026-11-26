---
id: "lesson:19/07"
type: lesson
ref: 19/07
phase: 19
num: 7
title: "Capstone 07 — End-to-End Fine-Tuning Pipeline (Data to SFT to DPO to Serve)"
lesson_type: capstone
languages:
  - Python
  - YAML
  - Bash
time_min: 2100
on_route: false
quiz_count: 7
code_files: 1
concepts: 7
prereqs: 0
community: 20
aliases:
  - 19/07
  - 19-07
tags:
  - phase/19
  - type/capstone
  - community/20
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/07-end-to-end-fine-tuning-pipeline/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/07-end-to-end-fine-tuning-pipeline"
---

# 19/07 Capstone 07 — End-to-End Fine-Tuning Pipeline (Data to SFT to DPO to Serve)

> An 8B model trained on your own data, DPO-aligned on your own preferences, quantized, speculative-decoded, and served at measurable $/1M tokens. The 2026 open stack is Axolotl v0.8, TRL 0.15, Unsloth for iteration, GPTQ/AWQ/GGUF for quantization, vLLM 0.7 with EAGLE-3 for serving. The capstone is to run the whole pipeline reproducibly — YAML in, served endpoint out — and publish a model card under the 2026 Model Openness Framework.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Capstone · **Time:** 2100 min · **Languages:** Python, YAML, Bash · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/07-end-to-end-fine-tuning-pipeline/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/07-end-to-end-fine-tuning-pipeline) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/07-end-to-end-fine-tuning-pipeline) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/20 Acceptance rate · Draft model · EAGLE-3|20 Acceptance rate · Draft model · EAGLE-3]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 2 (ML), Phase 3 (DL), Phase 7 (transformers), Phase 10 (LLMs from scratch), Phase 11 (LLM engineering), Phase 17 (infrastructure), Phase 18 (safety)`

- Whole phase: [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] — LLMs from scratch ·  medium confidence
- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM engineering ·  medium confidence
- Whole phase: [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] — infrastructure ·  medium confidence
- Whole phase: [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] — safety ·  medium confidence
- Whole phase: [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] — ML ·  medium confidence
- Whole phase: [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] — DL ·  medium confidence
- Whole phase: [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] — transformers ·  medium confidence

## Concepts taught

- Axolotl `lesson term` — Unified YAML-driven trainer for SFT, DPO, and distillation
- TRL `lesson term` — Hugging Face library for DPO, GRPO, PPO on LLMs
- [[Concepts/GRPO|GRPO]] `lesson term` — DeepSeek R1's RL recipe with verifiable rewards
- [[Concepts/EAGLE-3|EAGLE-3]] `lesson term` — Draft heads that predict N tokens ahead; vLLM verifies with target model
- MOF `lesson term` — 2026 standard for grading model releases on data, code, license
- Contamination check `lesson term` — MinHash-based detection of test-set leakage into training
- [[Concepts/Acceptance rate|Acceptance rate]] `lesson term` — Fraction of drafted tokens the target model accepts

## Ships

- [[Artifacts/19-07 finetuning-pipeline|finetuning-pipeline]] `skill` — Run a reproducible data-to-SFT-to-DPO-to-serve fine-tuning pipeline with ablations, quantization, and a 2026 Model Openness Framework model card.

## Further reading

- [[Resources/DeepSeek-AI (2025). DeepSeek-R1- Incentivizing Reasoning Capability in LLMs via Reinforcement Learning|DeepSeek-AI (2025). DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]] ([link](https://arxiv.org/abs/2501.12948)) — GRPO methodology ·  also cited by 4 other lessons
- [[Resources/Axolotl documentation|Axolotl documentation]] ([link](https://axolotl-ai-cloud.github.io/axolotl/)) — the reference SFT / DPO trainer ·  also cited by 1 other lesson
- [[Resources/vLLM documentation|vLLM documentation]] ([link](https://docs.vllm.ai/)) — reference serving stack ·  also cited by 2 other lessons
- [[Resources/EleutherAI lm-evaluation-harness|EleutherAI lm-evaluation-harness]] ([link](https://github.com/EleutherAI/lm-evaluation-harness)) — canonical eval runner ·  also cited by 1 other lesson
- [[Resources/SGLang SpecForge|SGLang SpecForge]] ([link](https://github.com/sgl-project/SpecForge)) — alternate speculative-decoding trainer ·  also cited by 1 other lesson
- Unsloth ([link](https://github.com/unslothai/unsloth)) — single-GPU iteration reference
- [[Resources/Hugging Face TRL library|Hugging Face TRL library]] ([link](https://huggingface.co/docs/trl)) — DPO and GRPO reference implementations ·  also cited by 2 other lessons
- Model Openness Framework 2026 ([link](https://isocpp.org/)) — the open-release grading standard


%% ── my notes ── %%
