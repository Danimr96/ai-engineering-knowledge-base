---
id: "lesson:10/20"
type: lesson
ref: 10/20
phase: 10
num: 20
title: DeepSeek-V3 Architecture Walkthrough
lesson_type: learn
languages:
  - Python
time_min: 75
status: planned
status_auto: planned
on_route: true
route_order: 21
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 4
community: 1
aliases:
  - 10/20
  - 10-20
tags:
  - phase/10
  - type/learn
  - status/planned
  - route
  - community/01
  - stdlib-only
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/20-deepseek-v3-walkthrough/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/20-deepseek-v3-walkthrough"
---

# 10/20 DeepSeek-V3 Architecture Walkthrough

> Phase 10 · Lesson 14 named the six architectural knobs every open model turns. DeepSeek-V3 (December 2024, 671B parameters total, 37B active) turns all six and adds four more: Multi-Head Latent Attention, auxiliary-loss-free load balancing, Multi-Token Prediction, and DualPipe training. This lesson reads DeepSeek-V3's architecture top to bottom and derives every parameter count from the published config. By the end you can explain why the 671B/37B ratio is the right bet and why MLA + MoE together beat either alone at the frontier.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Learn · **Time:** 75 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/20-deepseek-v3-walkthrough/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/20-deepseek-v3-walkthrough) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/20-deepseek-v3-walkthrough) · code: main.py  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 10 · 14 (open-model walkthroughs), Phase 10 · 17 (NSA), Phase 10 · 18 (MTP), Phase 10 · 19 (DualPipe)`

- [[Lessons/10-14 Open Models- Architecture Walkthroughs|10/14 Open Models: Architecture Walkthroughs]] — open-model walkthroughs
- [[Lessons/10-17 Native Sparse Attention (DeepSeek NSA)|10/17 Native Sparse Attention (DeepSeek NSA)]] — NSA
- [[Lessons/10-18 Multi-Token Prediction (MTP)|10/18 Multi-Token Prediction (MTP)]] — MTP
- [[Lessons/10-19 DualPipe Parallelism|10/19 DualPipe Parallelism]] — DualPipe

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/07-11 Mixture of Experts (MoE)|07/11 Mixture of Experts (MoE)]], [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]], [[Lessons/07-15 Attention Variants — Sliding Window, Sparse, Differential|07/15 Attention Variants — Sliding Window, Sparse, Differential]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]], [[Lessons/10-15 Speculative Decoding and EAGLE-3|10/15 Speculative Decoding and EAGLE-3]], [[Lessons/10-16 Differential Attention (V2)|10/16 Differential Attention (V2)]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]], [[Lessons/07-16 Speculative Decoding — Draft, Verify, Repeat|07/16 Speculative Decoding — Draft, Verify, Repeat]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Concepts taught

- [[Concepts/MLA|MLA]] `lesson term` — Compress K and V into a shared low-rank latent (kv_lora_rank, typically 512), decompress per head on-the-fly; KV cache stores only the latent
- kv_lora_rank `lesson term` — The size of the shared latent for K and V; DeepSeek-V3 uses 512
- First k dense layers `lesson term` — The first few MoE-model layers skip the MoE router and run a dense MLP for stability
- num_experts_per_tok `lesson term` — How many routed experts fire per token; DeepSeek-V3 uses 8
- Shared experts `lesson term` — Experts that process every token regardless of routing; DeepSeek-V3 uses 1
- Auxiliary-loss-free routing `lesson term` — Per-expert bias terms adjusted during training to keep expert load balanced without adding a loss term
- [[Concepts/MTP module|MTP module]] `lesson term` — Transformer block predicting t+2 from h^(1) and E(t+1); denser training, free speculative-decoding draft
- [[Concepts/DualPipe|DualPipe]] `lesson term` — Training schedule that overlaps forward/backward compute with cross-node all-to-all
- Active parameter ratio `lesson term` — active_params / total_params; DeepSeek-V3 hits 5.5%
- FP8 training `lesson term` — Training storage and many compute ops in FP8; roughly halves memory vs BF16 at a small quality cost

## Ships

- [[Artifacts/10-20 deepseek-v3-reader|deepseek-v3-reader]] `skill` — Read a DeepSeek-family config and produce a component-by-component architecture analysis.

## Further reading

- [[Resources/DeepSeek-AI (2024). DeepSeek-V2 Technical Report|DeepSeek-AI (2024). DeepSeek-V2 Technical Report]] ([link](https://arxiv.org/abs/2405.04434)) — the predecessor that introduced MLA ·  also cited by 1 other lesson
- [[Resources/DeepSeek-AI (2024). DeepSeek-V3 Technical Report|DeepSeek-AI (2024). DeepSeek-V3 Technical Report]] ([link](https://arxiv.org/abs/2412.19437)) — the full architecture, training, and results document ·  also cited by 7 other lessons
- [[Resources/DeepSeek-AI (2025). DeepSeek-R1- Incentivizing Reasoning Capability in LLMs via Reinforcement Learning|DeepSeek-AI (2025). DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]] ([link](https://arxiv.org/abs/2501.12948)) — the reasoning-training successor on V3's architecture ·  also cited by 4 other lessons
- [[Resources/Yuan et al. (2025). Native Sparse Attention|Yuan et al. (2025). Native Sparse Attention]] ([link](https://arxiv.org/abs/2502.11089)) — the future direction for DeepSeek-family attention ·  also cited by 2 other lessons
- [[Resources/DeepSeek — DualPipe GitHub repository|DeepSeek — DualPipe GitHub repository]] ([link](https://github.com/deepseek-ai/DualPipe)) — the training-schedule reference ·  also cited by 1 other lesson
- [[Resources/DeepSeek-V3 model card on Hugging Face|DeepSeek-V3 model card on Hugging Face]] ([link](https://huggingface.co/deepseek-ai/DeepSeek-V3)) — config files and deployment notes ·  also cited by 1 other lesson

## My route

- Step 21 in *Route: Phase 10 advanced (about 12 h)*
- Plan note: DeepSeek-V3 walkthrough (ties 14–19 together)
- Previous: [[Lessons/10-19 DualPipe Parallelism|10/19 DualPipe Parallelism]]
- Next: [[Lessons/10-21 Jamba — Hybrid SSM-Transformer|10/21 Jamba — Hybrid SSM-Transformer]]


%% ── my notes ── %%
