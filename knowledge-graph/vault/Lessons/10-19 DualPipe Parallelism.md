---
id: "lesson:10/19"
type: lesson
ref: 10/19
phase: 10
num: 19
title: DualPipe Parallelism
lesson_type: learn
languages:
  - Python
time_min: 60
status: planned
status_auto: planned
on_route: true
route_order: 20
quiz_count: 0
code_files: 1
concepts: 11
prereqs: 2
community: 1
aliases:
  - 10/19
  - 10-19
tags:
  - phase/10
  - type/learn
  - status/planned
  - route
  - community/01
  - stdlib-only
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/19-dualpipe-parallelism/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/19-dualpipe-parallelism"
---

# 10/19 DualPipe Parallelism

> DeepSeek-V3 was trained on 2,048 H800 GPUs with MoE experts scattered across nodes. Cross-node expert all-to-all communication cost 1 GPU-hour of comm for every 1 GPU-hour of compute. GPUs were idle half the time. DualPipe (DeepSeek, Dec 2024) is a bidirectional pipeline that overlaps forward and backward computation with the all-to-all comms they trigger. Bubbles drop, throughput climbs, and the keeping of two model-parameter copies (the "dual" that gives the name) is cheap once Expert Parallelism is already spreading experts across ranks anyway. This lesson is a Learn-type walkthrough of what DualPipe actually does and why Sea AI Lab's DualPipeV refinement drops the 2x parameter cost at the expense of a marginally tighter bubble.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/19-dualpipe-parallelism/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/19-dualpipe-parallelism) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/19-dualpipe-parallelism) · code: main.py  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 10 · 05 (distributed training, FSDP, DeepSpeed), Phase 10 · 14 (open-model architectures and MoE)`

- [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]] — distributed training, FSDP, DeepSpeed
- [[Lessons/10-14 Open Models- Architecture Walkthroughs|10/14 Open Models: Architecture Walkthroughs]] — open-model architectures and MoE

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/07-11 Mixture of Experts (MoE)|07/11 Mixture of Experts (MoE)]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]], [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]], [[Lessons/19-42 Large Corpus Downloader|19/42 Large Corpus Downloader]], [[Lessons/19-43 HDF5 Tokenized Corpus|19/43 HDF5 Tokenized Corpus]], [[Lessons/19-44 Cosine LR with Linear Warmup|19/44 Cosine LR with Linear Warmup]], [[Lessons/19-45 Gradient Clipping and Mixed Precision|19/45 Gradient Clipping and Mixed Precision]], [[Lessons/19-46 Gradient Accumulation|19/46 Gradient Accumulation]], [[Lessons/19-47 Checkpoint Save and Resume|19/47 Checkpoint Save and Resume]], [[Lessons/19-48 Distributed Data Parallel and FSDP from Scratch|19/48 Distributed Data Parallel and FSDP from Scratch]], [[Lessons/19-49 Language Model Evaluation Harness|19/49 Language Model Evaluation Harness]]

## Builds on this

- [[Lessons/10-20 DeepSeek-V3 Architecture Walkthrough|10/20 DeepSeek-V3 Architecture Walkthrough]]

## Concepts taught

- [[Concepts/Pipeline bubble|Pipeline bubble]] `lesson term` — GPU cycles wasted because a pipeline stage is waiting for its input or gradient
- [[Concepts/1F1B|1F1B]] `lesson term` — One forward / one backward interleaved scheduling; the baseline DualPipe beats
- Zero Bubble `lesson term` — Splits backward into B (input gradient) and W (weight gradient); almost fully tightens the pipeline
- [[Concepts/DualPipe|DualPipe]] `lesson term` — Bidirectional pipeline + compute-comm overlap; bubbles do not grow with micro-batch count
- DualPipeV `lesson term` — V-shape refinement that drops the 2x parameter replication at the cost of slightly larger bubbles
- [[Concepts/Chunk|Chunk]] `lesson term` — A forward or backward pass of one micro-batch through one pipeline stage
- All-to-all dispatch `lesson term` — Cross-node comm that routes tokens to their assigned MoE experts
- All-to-all combine `lesson term` — Cross-node comm that gathers expert outputs after the MLP
- [[Concepts/Expert Parallelism|Expert Parallelism]] (as *Expert Parallelism (EP)*) `glossary` — Shards MoE experts across ranks so different GPUs hold different experts
- [[Concepts/Pipeline Parallelism|Pipeline Parallelism]] (as *Pipeline Parallelism (PP)*) `glossary` — Shards model layers across ranks; the dimension DualPipe schedules
- Bubble fraction `lesson term` — (bubble_time / total_time); the fraction DualPipe drives toward zero

## Ships

- [[Artifacts/10-19 dualpipe-planner|dualpipe-planner]] `skill` — Plan a pipeline parallelism strategy (1F1B, Zero Bubble, DualPipe, DualPipeV) for a training cluster.

## Further reading

- [[Resources/Narayanan et al. — PipeDream - 1F1B (arXiv-1806.03377, 2018-2021)|Narayanan et al. — PipeDream / 1F1B (arXiv:1806.03377, 2018-2021)]] ([link](https://arxiv.org/abs/1806.03377)) — the 1F1B schedule DualPipe compares against ·  also cited by 1 other lesson
- [[Resources/GPipe|GPipe]] ([link](https://arxiv.org/abs/1811.06965)) — the original pipeline parallelism paper and bubble problem ·  also cited by 1 other lesson
- Qi et al. — Zero Bubble Pipeline Parallelism (arXiv:2401.10241, Sea AI Lab 2023) ([link](https://arxiv.org/abs/2401.10241)) — the Zero Bubble predecessor
- [[Resources/DeepSeek-AI (2024). DeepSeek-V3 Technical Report|DeepSeek-AI (2024). DeepSeek-V3 Technical Report]] ([link](https://arxiv.org/abs/2412.19437)) — the primary DualPipe reference ·  also cited by 7 other lessons
- [[Resources/DeepSeek — DualPipe GitHub repository|DeepSeek — DualPipe GitHub repository]] ([link](https://github.com/deepseek-ai/DualPipe)) — the open-source reference implementation, including DualPipeV (Cut-in-half) mode ·  also cited by 1 other lesson
- Sea AI Lab — DualPipe could be better without the Dual ([link](https://sail.sea.com/blog/articles/63)) — the DualPipeV analysis that informed DeepSeek's EP-off mode

## My route

- Step 20 in *Route: Phase 10 advanced (about 12 h)*
- Plan note: DualPipe parallelism
- Previous: [[Lessons/10-18 Multi-Token Prediction (MTP)|10/18 Multi-Token Prediction (MTP)]]
- Next: [[Lessons/10-20 DeepSeek-V3 Architecture Walkthrough|10/20 DeepSeek-V3 Architecture Walkthrough]]


%% ── my notes ── %%
