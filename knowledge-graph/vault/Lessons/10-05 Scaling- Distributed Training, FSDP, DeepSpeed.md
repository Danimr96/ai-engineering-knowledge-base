---
id: "lesson:10/05"
type: lesson
ref: 10/05
phase: 10
num: 5
title: "Scaling: Distributed Training, FSDP, DeepSpeed"
lesson_type: build
languages:
  - Python
time_min: 120
status: planned
status_auto: planned
on_route: true
route_order: 5
quiz_count: 0
code_files: 1
concepts: 12
prereqs: 1
community: 1
libraries:
  - numpy
aliases:
  - 10/05
  - 10-05
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/05-scaling-distributed/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/05-scaling-distributed"
---

# 10/05 Scaling: Distributed Training, FSDP, DeepSpeed

> Your 124M model trained on one GPU. Now try 7 billion parameters. The model doesn't fit in memory. The data takes weeks on a single machine. Distributed training isn't optional at scale. It's the only path forward.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 120 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/05-scaling-distributed/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/05-scaling-distributed) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/05-scaling-distributed) · code: main.py  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 10, Lesson 04 (Pre-Training a Mini GPT)`

- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]] — Pre-Training a Mini GPT

### Bridges to check first (my plan)

- [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]] — collective ops from scratch)

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/19-42 Large Corpus Downloader|19/42 Large Corpus Downloader]], [[Lessons/19-43 HDF5 Tokenized Corpus|19/43 HDF5 Tokenized Corpus]], [[Lessons/19-44 Cosine LR with Linear Warmup|19/44 Cosine LR with Linear Warmup]], [[Lessons/19-45 Gradient Clipping and Mixed Precision|19/45 Gradient Clipping and Mixed Precision]], [[Lessons/19-46 Gradient Accumulation|19/46 Gradient Accumulation]], [[Lessons/19-47 Checkpoint Save and Resume|19/47 Checkpoint Save and Resume]], [[Lessons/19-48 Distributed Data Parallel and FSDP from Scratch|19/48 Distributed Data Parallel and FSDP from Scratch]], [[Lessons/19-49 Language Model Evaluation Harness|19/49 Language Model Evaluation Harness]]
- depth 3: [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/19-30 BPE Tokenizer From Scratch|19/30 BPE Tokenizer From Scratch]], [[Lessons/19-31 Tokenized Dataset with Sliding Window|19/31 Tokenized Dataset with Sliding Window]], [[Lessons/19-32 Token and Positional Embeddings|19/32 Token and Positional Embeddings]], [[Lessons/19-33 Multi-Head Self-Attention|19/33 Multi-Head Self-Attention]], [[Lessons/19-34 Transformer Block from Scratch|19/34 Transformer Block from Scratch]], [[Lessons/19-35 GPT Model Assembly|19/35 GPT Model Assembly]], [[Lessons/19-36 Training Loop and Evaluation|19/36 Training Loop and Evaluation]], [[Lessons/19-37 Loading Pretrained Weights|19/37 Loading Pretrained Weights]]

## Builds on this

- [[Lessons/10-10 Evaluation- Benchmarks, Evals, LM Harness|10/10 Evaluation: Benchmarks, Evals, LM Harness]]
- [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]]
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]]
- [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]]
- [[Lessons/10-14 Open Models- Architecture Walkthroughs|10/14 Open Models: Architecture Walkthroughs]]
- [[Lessons/10-19 DualPipe Parallelism|10/19 DualPipe Parallelism]]
- [[Lessons/10-34 Gradient Checkpointing and Activation Recomputation|10/34 Gradient Checkpointing and Activation Recomputation]]
- [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]]
- [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]]

## Concepts taught

- Data parallelism `lesson term` — Each GPU processes a different data shard; gradients are averaged via all-reduce after each step
- [[Concepts/Tensor Parallelism|Tensor Parallelism]] `glossary` — Partition weight matrices so each GPU computes part of the matmul; requires fast NVLink interconnect
- [[Concepts/Pipeline Parallelism|Pipeline Parallelism]] `glossary` — Each GPU runs a different group of layers; data flows through the pipeline with micro-batches to reduce bubbles
- FSDP `lesson term` — Fully Sharded Data Parallel -- each GPU holds 1/N of weights, gradients, and optimizer states; all-gather before compute
- ZeRO `lesson term` — Zero Redundancy Optimizer with 3 stages: shard optimizer (Stage 1), + gradients (Stage 2), + parameters (Stage 3)
- [[Concepts/All-reduce|All-reduce]] `lesson term` — Collective operation where every GPU ends with the sum (or average) of all GPUs' inputs -- typically implemented as ring all-reduce
- All-gather `lesson term` — Collective operation where every GPU ends with the concatenation of all GPUs' data -- used in FSDP to reconstruct full parameters
- [[Concepts/Reduce-scatter|Reduce-scatter]] `lesson term` — Collective operation that reduces (sums) data and scatters different chunks to different GPUs -- used in FSDP for gradient sharding
- [[Concepts/Mixed Precision|Mixed Precision]] `glossary` — Use FP16/BF16 for forward/backward and FP32 for optimizer states -- saves ~25% memory, not 50%, because the optimizer dominates
- [[Concepts/Pipeline bubble|Pipeline bubble]] `lesson term` — Fraction of time GPUs sit idle waiting for data from the previous stage -- reduced by using more micro-batches

## Ships

- [[Artifacts/10-05 prompt-distributed-training-planner|prompt-distributed-training-planner]] `prompt` — Plan a distributed training run given model size and available hardware

## Further reading

- Megatron-LM ([link](https://arxiv.org/abs/1909.08053)) — NVIDIA's tensor parallelism for transformers
- [[Resources/Rajbhandari et al., 2020 - -ZeRO- Memory Optimizations Toward Training Trillion Parameter Models|Rajbhandari et al., 2020 -- "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models]] ([link](https://arxiv.org/abs/1910.02054)) — the DeepSpeed ZeRO paper that defined the three sharding stages ·  also cited by 1 other lesson
- Narayanan et al., 2021 -- "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM ([link](https://arxiv.org/abs/2104.04473)) — 3D parallelism combining data, tensor, and pipeline
- Zhao et al., 2023 -- "PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel ([link](https://arxiv.org/abs/2304.11277)) — PyTorch's native FSDP implementation
- [[Resources/Llama 3 paper (Meta, 2024)|Llama 3 paper (Meta, 2024)]] ([link](https://arxiv.org/abs/2407.21783)) — 16,384 GPU training with 3D parallelism details ·  also cited by 7 other lessons
- [[Resources/DeepSeek-AI (2024). DeepSeek-V3 Technical Report|DeepSeek-AI (2024). DeepSeek-V3 Technical Report]] ([link](https://arxiv.org/abs/2412.19437)) — how MoE architecture reduces training cost by an order of magnitude ·  also cited by 7 other lessons

## My route

- Step 5 in *Route: Phase 10 core (about 20 h, plus bridges)*
- Plan note: Scaling: distributed training, FSDP, DeepSpeed
- Previous: [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]
- Next: [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]]


%% ── my notes ── %%
