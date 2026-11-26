---
id: "lesson:17/12"
type: lesson
ref: 17/12
phase: 17
num: 12
title: "Edge Inference — Apple Neural Engine, Qualcomm Hexagon, WebGPU/WebLLM, Jetson"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 10
prereqs: 2
community: 28
aliases:
  - 17/12
  - 17-12
tags:
  - phase/17
  - type/learn
  - community/28
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/12-edge-inference/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/12-edge-inference"
---

# 17/12 Edge Inference — Apple Neural Engine, Qualcomm Hexagon, WebGPU/WebLLM, Jetson

> The core edge constraint is memory bandwidth, not compute. Mobile DRAM sits at 50-90 GB/s; datacenter HBM3 clears 2-3 TB/s — a 30-50x gap. Decode is memory-bound so the gap is decisive. In 2026 the landscape splits four ways. Apple M4/A18 Neural Engine peaks at 38 TOPS with unified memory (no CPU↔NPU copy). Qualcomm Snapdragon X Elite / 8 Gen 4 Hexagon hits 45 TOPS. WebGPU + WebLLM runs Llama 3.1 8B (Q4) at ~41 tok/s on M3 Max (roughly 70-80% of native); 17.6k GitHub stars, OpenAI-compatible API, ~70-75% mobile coverage. NVIDIA Jetson Orin Nano Super (8GB) fits Llama 3.2 3B / Phi-3; AGX Orin runs gpt-oss-20b via vLLM at ~40 tok/s; Jetson T4000 (JetPack 7.1) is 2x AGX Orin. TensorRT Edge-LLM supports EAGLE-3, NVFP4, chunked prefill — shown at CES 2026 by Bosch, ThunderSoft, MediaTek.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/12-edge-inference/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/12-edge-inference) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/12-edge-inference) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/28 Production-stack · RadixAttention · cache_control|28 Production-stack · RadixAttention · cache_control]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 04 (Serving Engine Internals), Phase 17 · 09 (Production Quantization)`

- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] — Serving Engine Internals
- [[Lessons/17-09 Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4-NVFP4|17/09 Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4/NVFP4]] — Production Quantization

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]], [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]]
- depth 3: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]], [[Lessons/10-09 Constitutional AI and Self-Improvement|10/09 Constitutional AI and Self-Improvement]], [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]], [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]], [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]]

## Concepts taught

- ANE `lesson term` — On-device NPU in M-series and A-series; unified memory
- Hexagon `lesson term` — Snapdragon NPU; QNN SDK for access
- WebGPU `lesson term` — W3C-standardized browser GPU API; Chrome/Safari 2026
- WebLLM `lesson term` — MLC-LLM project; Apache 2.0; OpenAI-compatible JS
- Jetson `lesson term` — Orin Nano / AGX / Thor / T4000 family
- TRT Edge-LLM `lesson term` — 2026 edge port of TensorRT-LLM; EAGLE-3 + NVFP4
- Unified memory `lesson term` — CPU and NPU see same RAM; no copy overhead
- Bandwidth-bound `lesson term` — Decode gated by bytes/sec reading weights
- Core ML `lesson term` — Apple framework for ANE-native models
- QNN `lesson term` — Qualcomm Neural Network SDK

## Ships

- [[Artifacts/17-12 edge-target-picker|edge-target-picker]] `skill` — Pick an edge inference target (Apple ANE, Qualcomm Hexagon, WebGPU/WebLLM, NVIDIA Jetson) and matching quantization format given device, model, and latency budget.

## Further reading

- Qualcomm AI Hub ([link](https://aihub.qualcomm.com/)) — pre-converted models for Hexagon.
- WebLLM (arXiv:2412.15803) ([link](https://arxiv.org/html/2412.15803v2)) — design and benchmarks.
- Apple Core ML ([link](https://developer.apple.com/documentation/coreml)) — ANE-native conversion.
- NVIDIA TensorRT Edge-LLM ([link](https://developer.nvidia.com/blog/accelerating-llm-and-vlm-inference-for-automotive-and-robotics-with-nvidia-tensorrt-edge-llm/)) — 2026 edge port announcement.
- NVIDIA Jetson Edge AI ([link](https://developer.nvidia.com/blog/getting-started-with-edge-ai-on-nvidia-jetson-llms-vlms-and-foundation-models-for-robotics/)) — Orin / AGX / Thor.
- On-Device LLMs State of the Union 2026 ([link](https://v-chandra.github.io/on-device-llms/)) — landscape and benchmarks.


%% ── my notes ── %%
