---
id: "lesson:17/09"
type: lesson
ref: 17/09
phase: 17
num: 9
title: "Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4/NVFP4"
lesson_type: learn
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 1
concepts: 9
prereqs: 2
community: 1
aliases:
  - 17/09
  - 17-09
tags:
  - phase/17
  - type/learn
  - community/01
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/09-production-quantization/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/09-production-quantization"
---

# 17/09 Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4/NVFP4

> Quantization format is not a universal choice — it is a function of hardware, serving engine, and workload. GGUF Q4_K_M or Q5_K_M owns CPU and edge, delivered through llama.cpp and Ollama. GPTQ wins inside vLLM when you need multi-LoRA on the same base. AWQ with Marlin-AWQ kernels delivers ~741 tok/s on a 7B class model with the best Pass@1 at INT4 — the 2026 default for datacenter production. FP8 stays the middle ground on Hopper, Ada, and Blackwell — near-lossless and widely supported. NVFP4 and MXFP4 (Blackwell microscaling) are aggressive and require per-block validation. Two traps bite teams: calibration dataset must match deployment domain, and KV cache is separate from weight quantization — the AWQ lesson "my model is 4 GB now" forgets the 10-30 GB KV cache at production batch sizes.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/09-production-quantization/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/09-production-quantization) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/09-production-quantization) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 10 · 13 (Quantization foundations), Phase 17 · 04 (Serving Engine Internals)`

- [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]] — Quantization foundations
- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] — Serving Engine Internals

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]], [[Lessons/10-09 Constitutional AI and Self-Improvement|10/09 Constitutional AI and Self-Improvement]], [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]], [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]], [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]], [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/01-13 Numerical Stability|01/13 Numerical Stability]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Builds on this

- [[Lessons/17-12 Edge Inference — Apple Neural Engine, Qualcomm Hexagon, WebGPU-WebLLM, Jetson|17/12 Edge Inference — Apple Neural Engine, Qualcomm Hexagon, WebGPU/WebLLM, Jetson]]
- [[Lessons/17-28 Self-Hosted Serving Selection — Matching Engine to Hardware and Scale|17/28 Self-Hosted Serving Selection — Matching Engine to Hardware and Scale]]

## Concepts taught

- [[Concepts/GGUF|GGUF]] `lesson term` — File format bundling K-quant variants; CPU/edge default
- Q4_K_M `lesson term` — 4-bit K-quant medium; the production GGUF default
- [[Concepts/GPTQ|GPTQ]] `lesson term` — Post-train INT4 with calibration; supports LoRA in vLLM
- [[Concepts/AWQ|AWQ]] `lesson term` — Activation-aware INT4; Marlin kernels; best Pass@1 at INT4
- Marlin kernels `lesson term` — Custom CUDA kernels for INT4 on Hopper; 10x speedup
- [[Concepts/FP8|FP8]] `lesson term` — Safe precision default on Hopper/Ada/Blackwell
- MXFP4 / NVFP4 `lesson term` — Blackwell 4-bit FP with per-block scale factors
- Calibration dataset `lesson term` — Input text used to pick quantization parameters; must match domain
- KV cache quantization `lesson term` — Separate choice from weights; affects attention accuracy

## Ships

- [[Artifacts/17-09 quantization-picker|quantization-picker]] `skill` — Pick a 2026 quantization format given hardware, engine, workload, and quality tolerance, and produce a calibration + validation plan.

## Further reading

- [[Resources/Frantar et al., 2022 - -GPTQ- Accurate Post-Training Quantization for Generative Pre-trained Transformers|Frantar et al., 2022 -- "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers]] ([link](https://arxiv.org/abs/2210.17323)) — original GPTQ formulation. ·  also cited by 1 other lesson
- [[Resources/Lin et al., 2023 - -AWQ- Activation-aware Weight Quantization for LLM Compression and Acceleration|Lin et al., 2023 -- "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration]] ([link](https://arxiv.org/abs/2306.00978)) — original AWQ formulation. ·  also cited by 1 other lesson
- PremAI — GGUF vs AWQ vs GPTQ vs bitsandbytes 2026 ([link](https://blog.premai.io/llm-quantization-guide-gguf-vs-awq-vs-gptq-vs-bitsandbytes-compared-2026/)) — format-by-format picking.
- vLLM docs — Quantization ([link](https://docs.vllm.ai/en/latest/features/quantization/index.html)) — supported formats and flags.
- Jarvis Labs — vLLM Quantization Complete Guide ([link](https://jarvislabs.ai/blog/vllm-quantization-complete-guide-benchmarks)) — throughput numbers by format.
- VRLA Tech — LLM Quantization 2026 ([link](https://vrlatech.com/llm-quantization-explained-int4-int8-fp8-awq-and-gptq-in-2026/)) — comparative benchmarks.


%% ── my notes ── %%
