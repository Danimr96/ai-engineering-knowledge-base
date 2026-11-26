---
id: "lesson:10/18"
type: lesson
ref: 10/18
phase: 10
num: 18
title: Multi-Token Prediction (MTP)
lesson_type: build
languages:
  - Python
time_min: 60
status: planned
status_auto: planned
on_route: true
route_order: 19
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 2
aliases:
  - 10/18
  - 10-18
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - stdlib-only
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/18-multi-token-prediction/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/18-multi-token-prediction"
---

# 10/18 Multi-Token Prediction (MTP)

> Every autoregressive LLM from GPT-2 to Llama 3 trains on one loss per position: predict the next token. DeepSeek-V3 added a second loss per position: predict the token after that. The extra 14B of parameters (on a 671B model) got distilled back into the main model through gradient flow, and the trained MTP heads were repurposed at inference as speculative-decoding drafters with 80%+ acceptance. 1.8× generation throughput came for free. This lesson builds the sequential MTP module from the DeepSeek technical report, computes the loss and the shared-head parameter layout, and explains why MTP keeps the causal chain while Gloeckle et al.'s original parallel MTP broke it.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/18-multi-token-prediction/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/18-multi-token-prediction) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/18-multi-token-prediction) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 10 · 04 (pre-training a mini GPT), Phase 10 · 15 (speculative decoding)`

- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]] — pre-training a mini GPT
- [[Lessons/10-15 Speculative Decoding and EAGLE-3|10/15 Speculative Decoding and EAGLE-3]] — speculative decoding

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-16 Speculative Decoding — Draft, Verify, Repeat|07/16 Speculative Decoding — Draft, Verify, Repeat]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]]
- depth 3: [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]], [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]

## Builds on this

- [[Lessons/10-20 DeepSeek-V3 Architecture Walkthrough|10/20 DeepSeek-V3 Architecture Walkthrough]]
- [[Lessons/17-05 EAGLE-3 Speculative Decoding in Production|17/05 EAGLE-3 Speculative Decoding in Production]]

## Concepts taught

- [[Concepts/MTP module|MTP module]] `lesson term` — A small transformer block plus projection that predicts a token k positions ahead of the main model
- Prediction depth `lesson term` — The integer k such that module k predicts t{i+k} from prefix through position i
- Parallel MTP `lesson term` — D independent heads on the same backbone hidden state, no conditional chain
- Sequential MTP `lesson term` — Each module conditions on the previous depth's hidden state plus the next token's embedding; preserves causal chain
- Shared output head `lesson term` — The MTP modules call the main model's LM head, not a separate output projection
- Shared embedding `lesson term` — Same vocabulary embedding table is used everywhere; no duplicate parameters
- Projection matrix M_k `lesson term` — An h x 2h linear layer that folds the previous hidden state and the target-token embedding into the next depth's input
- Joint loss L_MTP `lesson term` — Arithmetic mean of per-depth cross-entropy losses, scaled by lambda
- Acceptance rate at depth 1 `lesson term` — The rate at which the D=1 MTP module's top-1 prediction equals the main model's top-1 prediction; 80%+ on DeepSeek-V3
- Lambda weighting `lesson term` — Per-depth scaling factor; 0.3 at start of training, 0.1 later on DeepSeek-V3

## Ships

- [[Artifacts/10-18 mtp-planner|mtp-planner]] `skill` — Plan a multi-token prediction integration for a new pre-training run.

## Further reading

- [[Resources/Leviathan, Kalman, Matias (2023). Fast Inference from Transformers via Speculative Decoding|Leviathan, Kalman, Matias (2023). Fast Inference from Transformers via Speculative Decoding]] ([link](https://arxiv.org/abs/2211.17192)) — the speculative-decoding framework MTP fits into ·  also cited by 7 other lessons
- Gloeckle et al. — Better & Faster Large Language Models via Multi-token Prediction (arXiv:2404.19737) ([link](https://arxiv.org/abs/2404.19737)) — the parallel MTP baseline DeepSeek's design improves on
- [[Resources/DeepSeek-AI (2024). DeepSeek-V3 Technical Report|DeepSeek-AI (2024). DeepSeek-V3 Technical Report]] ([link](https://arxiv.org/abs/2412.19437)) — the full sequential MTP description (Section 2.2), including the joint-loss equations and the 1.8× speedup at inference ·  also cited by 7 other lessons
- [[Resources/Li et al. (2025). EAGLE-3- Scaling up Inference Acceleration of Large Language Models via Training-Time Test|Li et al. (2025). EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test]] ([link](https://arxiv.org/abs/2503.01840)) — EAGLE's 2025 draft architecture, the counterpart MTP competes with ·  also cited by 4 other lessons
- [[Resources/DeepSeek-V3 model card on Hugging Face|DeepSeek-V3 model card on Hugging Face]] ([link](https://huggingface.co/deepseek-ai/DeepSeek-V3)) — 685B total (671B main + 14B MTP), deployment notes ·  also cited by 1 other lesson

## My route

- Step 19 in *Route: Phase 10 advanced (about 12 h)*
- Plan note: Multi-token prediction
- Previous: [[Lessons/10-17 Native Sparse Attention (DeepSeek NSA)|10/17 Native Sparse Attention (DeepSeek NSA)]]
- Next: [[Lessons/10-19 DualPipe Parallelism|10/19 DualPipe Parallelism]]


%% ── my notes ── %%
