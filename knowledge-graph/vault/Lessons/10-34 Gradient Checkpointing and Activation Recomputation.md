---
id: "lesson:10/34"
type: lesson
ref: 10/34
phase: 10
num: 34
title: Gradient Checkpointing and Activation Recomputation
lesson_type: build
languages:
  - Python
time_min: 70
status: planned
status_auto: planned
on_route: true
route_order: 24
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 2
community: 1
libraries:
  - numpy
aliases:
  - 10/34
  - 10-34
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/34-gradient-checkpointing/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/34-gradient-checkpointing"
---

# 10/34 Gradient Checkpointing and Activation Recomputation

> Backprop keeps every intermediate activation. At 70B parameters and 128K context that is 3 TB of activations per rank. Checkpointing trades FLOPs for memory: recompute instead of save. The question is which segments to drop, and the answer is not "all of them."

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 70 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/34-gradient-checkpointing/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/34-gradient-checkpointing) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/34-gradient-checkpointing) · code: main.py  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 10 Lesson 04 (Pre-Training Mini-GPT), Phase 10 Lesson 05 (Scaling & Distributed)`

- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]] — Pre-Training Mini-GPT
- [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]] — Scaling & Distributed

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]
- depth 3: [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/19-42 Large Corpus Downloader|19/42 Large Corpus Downloader]], [[Lessons/19-43 HDF5 Tokenized Corpus|19/43 HDF5 Tokenized Corpus]], [[Lessons/19-44 Cosine LR with Linear Warmup|19/44 Cosine LR with Linear Warmup]], [[Lessons/19-45 Gradient Clipping and Mixed Precision|19/45 Gradient Clipping and Mixed Precision]], [[Lessons/19-46 Gradient Accumulation|19/46 Gradient Accumulation]], [[Lessons/19-47 Checkpoint Save and Resume|19/47 Checkpoint Save and Resume]], [[Lessons/19-48 Distributed Data Parallel and FSDP from Scratch|19/48 Distributed Data Parallel and FSDP from Scratch]], [[Lessons/19-49 Language Model Evaluation Harness|19/49 Language Model Evaluation Harness]]

## Concepts taught

- Gradient checkpointing `lesson term` — Store segment inputs only; recompute intermediates during backward to get gradient-support tensors
- Activation recomputation `lesson term` — The HPC-flavored name for the same technique
- Segment size (as *Segment size (k)*) `lesson term` — Number of layers whose intermediates are dropped and rematerialized together
- Selective checkpointing `lesson term` — Recompute only expensive-to-store activations (attention softmax); keep cheap ones
- Full checkpointing `lesson term` — Recompute every layer's intermediates in every segment
- Block checkpointing `lesson term` — Checkpoint whole transformer blocks; largest granularity
- FLOP overhead `lesson term` — Extra FLOPs per step = (recompute FLOPs) / (fwd + bwd FLOPs); 33% naive, 5% selective
- Activation offload `lesson term` — Move activations to CPU RAM across forward->backward; alternative to recompute
- sqrt-L rule `lesson term` — For uniform-cost layers, optimal checkpoint spacing is sqrt(L) layers
- Attention-softmax volume `lesson term` — L^2 heads batch floats; dominates activation memory at long contexts

## Ships

- [[Artifacts/10-34 checkpointing-planner|checkpointing-planner]] `skill` — Choose an activation recomputation policy per layer (none / selective / full / offload) given a training config and HBM budget.

## Further reading

- Training Deep Nets with Sublinear Memory Cost ([link](https://arxiv.org/abs/1604.06174)) — the original paper that formalized gradient checkpointing
- Pudipeddi et al., 2020 -- "Training Large Neural Networks with Constant Memory using a New Execution Algorithm ([link](https://arxiv.org/abs/2002.05645)) — alternative constant-memory approach via reverse-mode rematerialization
- Ren et al., 2021 -- "ZeRO-Offload: Democratizing Billion-Scale Model Training ([link](https://arxiv.org/abs/2101.06840)) — activation offload at scale
- Korthikanti et al., 2022 -- "Reducing Activation Recomputation in Large Transformer Models ([link](https://arxiv.org/abs/2205.05198)) — selective activation recomputation and the formal cost analysis
- Megatron-Core activation recomputation documentation ([link](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/features/memory_optimizations.html)) — selective, full, and block modes
- PyTorch torch.utils.checkpoint docs ([link](https://pytorch.org/docs/stable/checkpoint.html)) — the standard API

## My route

- Step 24 in *Route: Phase 10 advanced (about 12 h)*
- Plan note: Gradient checkpointing
- Previous: [[Lessons/10-22 Async and Hogwild! Inference|10/22 Async and Hogwild! Inference]]


%% ── my notes ── %%
