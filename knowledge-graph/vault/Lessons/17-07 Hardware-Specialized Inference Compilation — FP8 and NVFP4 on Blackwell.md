---
id: "lesson:17/07"
type: lesson
ref: 17/07
phase: 17
num: 7
title: "Hardware-Specialized Inference Compilation — FP8 and NVFP4 on Blackwell"
lesson_type: learn
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 1
concepts: 8
prereqs: 2
community: 1
aliases:
  - 17/07
  - 17-07
tags:
  - phase/17
  - type/learn
  - community/01
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/07-tensorrt-llm-blackwell/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/07-tensorrt-llm-blackwell"
---

# 17/07 Hardware-Specialized Inference Compilation — FP8 and NVFP4 on Blackwell

> Hardware-specialized inference compilation trades portability for throughput, and TensorRT-LLM — NVIDIA-only, tuned for Blackwell — is the clearest example of the trade paying off. On GB200 NVL72 with Dynamo orchestration, SemiAnalysis InferenceX measured $0.012 per million tokens on a 120B model in Q1-Q2 2026, against $0.09/M on H100 + vLLM — a 7x economic gap. The stack is three floating-point regimes compounded: FP8 stays critical for KV cache and attention kernels because it has the dynamic range they need; NVFP4 (4-bit microscaling) handles weights and activations; multi-token prediction (MTP) and disaggregated prefill/decode add another 2-3x on top. Day-0 model support loads FP4 weights directly without post-training conversion. The catch for 2026 engineering teams: TRT-LLM is open-source but NVIDIA-specific — CUDA- and Blackwell-specialized — so adopting it trades portability for throughput. Run the math on your mix of models and hardware before committing.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/07-tensorrt-llm-blackwell/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/07-tensorrt-llm-blackwell) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/07-tensorrt-llm-blackwell) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 04 (Serving Engine Internals), Phase 10 · 13 (Quantization)`

- [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]] — Quantization
- [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]] — Serving Engine Internals

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]], [[Lessons/10-09 Constitutional AI and Self-Improvement|10/09 Constitutional AI and Self-Improvement]], [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]], [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]], [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]], [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/01-13 Numerical Stability|01/13 Numerical Stability]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Builds on this

- [[Lessons/17-28 Self-Hosted Serving Selection — Matching Engine to Hardware and Scale|17/28 Self-Hosted Serving Selection — Matching Engine to Hardware and Scale]]

## Concepts taught

- [[Concepts/FP8|FP8]] `lesson term` — 8-bit floating point; used for KV cache and attention due to dynamic range
- NVFP4 `lesson term` — NVIDIA's 4-bit microscaling FP format; weights and activations on Blackwell
- MXFP8 `lesson term` — Microscaling FP8 variant; hardware-accelerated on Blackwell Tensor Cores
- Day-0 FP4 `lesson term` — Model providers release weights already in FP4; no post-train conversion step
- MTP `lesson term` — TRT-LLM's integrated speculative-decoding draft (Phase 17 · 05)
- [[Concepts/Disaggregated Serving|Disaggregated Serving]] `glossary` — Prefill and decode on separate GPU pools; KV transferred over NVLink/IB
- All-to-all `lesson term` — Communication pattern routing tokens to expert GPUs; NVLink 5 cuts 3x
- InferenceX `lesson term` — The 2026 industry-accepted cost-per-token benchmark

## Ships

- [[Artifacts/17-07 trtllm-blackwell-advisor|trtllm-blackwell-advisor]] `skill` — Decide whether Blackwell + TensorRT-LLM + Dynamo is worth the NVIDIA-lock for a given workload and budget.

## Further reading

- NVIDIA — MoE Inference on Blackwell ([link](https://developer.nvidia.com/blog/delivering-massive-performance-leaps-for-mixture-of-experts-inference-on-nvidia-blackwell/)) — NVLink 5 all-to-all and MoE kernels.
- [[Resources/NVIDIA — Introducing Dynamo|NVIDIA — Introducing Dynamo]] ([link](https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/)) — disaggregated orchestration above TRT-LLM. ·  also cited by 1 other lesson
- NVIDIA — Blackwell Ultra MLPerf Inference v6.0 ([link](https://developer.nvidia.com/blog/nvidia-blackwell-ultra-sets-new-inference-records-in-mlperf-debut/)) — April 2026 MLPerf results.
- [[Resources/MLPerf Inference|MLPerf Inference]] ([link](https://mlcommons.org/benchmarks/inference-datacenter/)) — the benchmark suite that publishes Blackwell numbers. ·  also cited by 1 other lesson
- TensorRT-LLM Overview ([link](https://nvidia.github.io/TensorRT-LLM/overview.html)) — official engine documentation.


%% ── my notes ── %%
