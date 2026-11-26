---
id: "lesson:10/14"
type: lesson
ref: 10/14
phase: 10
num: 14
title: "Open Models: Architecture Walkthroughs"
lesson_type: learn
languages:
  - Python
time_min: 45
status: planned
status_auto: planned
on_route: true
route_order: 14
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 3
community: 1
aliases:
  - 10/14
  - 10-14
tags:
  - phase/10
  - type/learn
  - status/planned
  - route
  - community/01
  - stdlib-only
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/14-open-models-architecture-walkthroughs/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/14-open-models-architecture-walkthroughs"
---

# 10/14 Open Models: Architecture Walkthroughs

> You built a GPT-2 Small from scratch in Lesson 04. Frontier open models in 2026 are the same family with five or six concrete changes. RMSNorm instead of LayerNorm. SwiGLU instead of GELU. RoPE instead of learned positions. GQA or MLA instead of full MHA. Mixture-of-Experts at scale. The math you already know covers 95% of them. This lesson reads Llama 3, DeepSeek-V3, Mixtral, Qwen, and Gemma side by side and names the exact line where each architecture diverges.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/14-open-models-architecture-walkthroughs/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/14-open-models-architecture-walkthroughs) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/14-open-models-architecture-walkthroughs) · code: main.py  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 10, Lessons 04, 05, 12 (Pre-training, Scaling, Inference)`

- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]
- [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]
- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]] — Pre-training, Scaling, Inference

### Bridges to check first (my plan)

- [[Lessons/07-11 Mixture of Experts (MoE)|07/11 Mixture of Experts (MoE)]] — mixture of experts

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]], [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]
- depth 3: [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/19-42 Large Corpus Downloader|19/42 Large Corpus Downloader]], [[Lessons/19-43 HDF5 Tokenized Corpus|19/43 HDF5 Tokenized Corpus]], [[Lessons/19-44 Cosine LR with Linear Warmup|19/44 Cosine LR with Linear Warmup]], [[Lessons/19-45 Gradient Clipping and Mixed Precision|19/45 Gradient Clipping and Mixed Precision]], [[Lessons/19-46 Gradient Accumulation|19/46 Gradient Accumulation]], [[Lessons/19-47 Checkpoint Save and Resume|19/47 Checkpoint Save and Resume]], [[Lessons/19-48 Distributed Data Parallel and FSDP from Scratch|19/48 Distributed Data Parallel and FSDP from Scratch]], [[Lessons/19-49 Language Model Evaluation Harness|19/49 Language Model Evaluation Harness]]

## Builds on this

- [[Lessons/10-16 Differential Attention (V2)|10/16 Differential Attention (V2)]]
- [[Lessons/10-19 DualPipe Parallelism|10/19 DualPipe Parallelism]]
- [[Lessons/10-20 DeepSeek-V3 Architecture Walkthrough|10/20 DeepSeek-V3 Architecture Walkthrough]]
- [[Lessons/10-21 Jamba — Hybrid SSM-Transformer|10/21 Jamba — Hybrid SSM-Transformer]]

## Concepts taught

- [[Concepts/RMSNorm|RMSNorm]] `lesson term` — Normalize by root mean square only, with a learned scale — cheaper and comparable to LayerNorm
- [[Concepts/RoPE|RoPE]] `lesson term` — Rotate each Q and K vector in 2D pairs by an angle that depends on position — extrapolates beyond training length with scaling tricks
- [[Concepts/SwiGLU|SwiGLU]] `lesson term` — Gated linear unit with Swish: (xW1) sigmoid(xW1) xV — standard in every 2024+ open model
- [[Concepts/GQA|GQA]] `lesson term` — Grouped-Query Attention: G groups of Q heads share one K and one V head — shrinks KV cache without MQA's accuracy hit
- [[Concepts/MLA|MLA]] `lesson term` — Multi-Head Latent Attention: compress K/V into a shared low-rank latent, decompress per head — smallest KV cache for large models
- [[Concepts/MoE (Mixture of Experts)|MoE (Mixture of Experts)]] (as *MoE*) `glossary` — Mixture of Experts: N MLPs per block, router picks top-k per token — huge total params, small active params
- [[Concepts/Top-k routing|Top-k routing]] `lesson term` — The router computes a score per expert and activates the k highest — typical k is 2 (Mixtral) to 8 (DeepSeek)
- [[Concepts/YaRN|YaRN]] `lesson term` — Yet another RoPE extension — interpolates rotary angles to extend context from 8k to 128k+ at inference time
- [[Concepts/Sliding window attention|Sliding window attention]] (as *Sliding-window attention*) `lesson term` — Each token attends only to the last W tokens — caps attention cost at O(W) per token, used in Gemma 2 and early Mistral
- Active params `lesson term` — For MoE models, the parameter count that sees a forward pass per token (much smaller than total params) — governs per-token FLOPs

## Ships

- [[Artifacts/10-14 open-model-picker|open-model-picker]] `skill` — Pick an open LLM family, quantization, and inference stack for a given deployment target.

## Further reading

- [[Resources/Shazeer (2020). GLU Variants Improve Transformer|Shazeer (2020). GLU Variants Improve Transformer]] ([link](https://arxiv.org/abs/2002.05202)) — SwiGLU, GeGLU, and friends ·  also cited by 1 other lesson
- [[Resources/Su et al.- RoFormer (2021)|Su et al.: RoFormer (2021)]] ([link](https://arxiv.org/abs/2104.09864)) — the RoPE paper ·  also cited by 3 other lessons
- [[Resources/Ainslie et al. (2023). GQA- Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints|Ainslie et al. (2023). GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints]] ([link](https://arxiv.org/abs/2305.13245)) — the GQA paper ·  also cited by 2 other lessons
- [[Resources/Jiang et al. (2024). Mixtral of Experts|Jiang et al. (2024). Mixtral of Experts]] ([link](https://arxiv.org/abs/2401.04088)) — the canonical MoE open model paper ·  also cited by 1 other lesson
- [[Resources/Llama 3 paper (Meta, 2024)|Llama 3 paper (Meta, 2024)]] ([link](https://arxiv.org/abs/2407.21783)) — the architectural and training reference for the dense Llama 3 family ·  also cited by 7 other lessons
- [[Resources/Gemma Team (2024). Gemma 2- Improving Open Language Models at a Practical Size|Gemma Team (2024). Gemma 2: Improving Open Language Models at a Practical Size]] ([link](https://arxiv.org/abs/2408.00118)) — hybrid full+sliding attention, pre+post-norm ·  also cited by 1 other lesson
- Qwen Team, 2024 -- "Qwen 2.5 Technical Report ([link](https://arxiv.org/abs/2412.15115)) — YaRN context extension and long-context training recipes
- [[Resources/DeepSeek-AI (2024). DeepSeek-V3 Technical Report|DeepSeek-AI (2024). DeepSeek-V3 Technical Report]] ([link](https://arxiv.org/abs/2412.19437)) — MLA plus auxiliary-loss-free load balancing plus 671B MoE ·  also cited by 7 other lessons

## My route

- Step 14 in *Route: Phase 10 advanced (about 12 h)*
- Plan note: Open models: architecture walkthroughs
- Previous: [[Lessons/10-13 Building a Complete LLM Pipeline|10/13 Building a Complete LLM Pipeline]]
- Next: [[Lessons/10-25 Speculative Decoding and EAGLE|10/25 Speculative Decoding and EAGLE]]


%% ── my notes ── %%
