---
id: "lesson:19/14"
type: lesson
ref: 19/14
phase: 19
num: 14
title: "Capstone 14 — Speculative-Decoding Inference Server"
lesson_type: capstone
languages:
  - Python
  - C++
  - CUDA
  - YAML
time_min: 1800
on_route: false
quiz_count: 7
code_files: 1
concepts: 7
prereqs: 0
community: 20
aliases:
  - 19/14
  - 19-14
tags:
  - phase/19
  - type/capstone
  - community/20
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/14-speculative-decoding-server/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/14-speculative-decoding-server"
---

# 19/14 Capstone 14 — Speculative-Decoding Inference Server

> Speculative decoding — a cheap draft proposes tokens, the target model verifies them in one pass — is now a production-ready optimization, not a research trick. EAGLE-3 in vLLM 0.7 ships 2.5-3x throughput on real traffic. P-EAGLE (AWS 2026) pushed parallel speculation even further. SGLang's SpecForge trained draft heads at scale. Red Hat's Speculators hub published aligned drafts for common open models. TensorRT-LLM made speculative decoding first-class on NVIDIA. The 2026 production serving stack is vLLM or SGLang with EAGLE-family drafts, FP8 or INT4 quantization, and HPA on queue-wait. This capstone is to serve two open models at 2.5x+ baseline throughput with a full tail-latency report.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Capstone · **Time:** 1800 min · **Languages:** Python, C++, CUDA, YAML · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/14-speculative-decoding-server/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/14-speculative-decoding-server) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/14-speculative-decoding-server) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/20 Acceptance rate · Draft model · EAGLE-3|20 Acceptance rate · Draft model · EAGLE-3]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 3 (deep learning), Phase 7 (transformers), Phase 10 (LLMs from scratch), Phase 17 (infrastructure)`

- Whole phase: [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] — LLMs from scratch ·  medium confidence
- Whole phase: [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] — infrastructure ·  medium confidence
- Whole phase: [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] — deep learning ·  medium confidence
- Whole phase: [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] — transformers ·  medium confidence

## Concepts taught

- [[Concepts/Draft model|Draft model]] `lesson term` — Small model that proposes N tokens for the target to verify
- [[Concepts/EAGLE-3|EAGLE-3]] `lesson term` — Draft head trained on target hidden states; ~75% acceptance
- P-EAGLE `lesson term` — Tree of draft branches verified in one target pass
- [[Concepts/Acceptance rate|Acceptance rate]] `lesson term` — Fraction of drafted tokens accepted without resampling
- [[Concepts/Quantization|Quantization]] `glossary` — Lower-precision weights to fit more model in GPU memory
- Queue wait `lesson term` — Time a request waits in the pending queue before inference starts
- Speculators hub `lesson term` — Red Hat Neural Magic hub of EAGLE drafts for common open models

## Ships

- [[Artifacts/19-14 inference-server|inference-server]] `skill` — Ship a speculative-decoding inference server with EAGLE-3 or P-EAGLE drafts, K8s autoscaling, and a full throughput/latency/cost report.

## Further reading

- [[Resources/Li et al. (2025). EAGLE-3- Scaling up Inference Acceleration of Large Language Models via Training-Time Test|Li et al. (2025). EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test]] ([link](https://arxiv.org/abs/2503.01840)) — the method paper ·  also cited by 4 other lessons
- P-EAGLE (AWS 2026) ([link](https://aws.amazon.com/blogs/machine-learning/p-eagle-faster-llm-inference-with-parallel-speculative-decoding-in-vllm/)) — parallel speculative decoding paper + integration
- [[Resources/vLLM documentation|vLLM documentation]] ([link](https://docs.vllm.ai/)) — the reference serving stack ·  also cited by 2 other lessons
- Fireworks.ai serving architecture ([link](https://fireworks.ai/blog)) — commercial reference
- Red Hat Speculators ([link](https://github.com/neuralmagic/speculators)) — aligned draft hub
- [[Resources/SGLang SpecForge|SGLang SpecForge]] ([link](https://github.com/sgl-project/SpecForge)) — draft-head training pipeline ·  also cited by 1 other lesson
- vLLM repository ([link](https://github.com/vllm-project/vllm)) — code and benchmarks
- [[Resources/NVIDIA TensorRT-LLM documentation|NVIDIA TensorRT-LLM documentation]] ([link](https://nvidia.github.io/TensorRT-LLM/)) — vendor alternative ·  also cited by 1 other lesson


%% ── my notes ── %%
