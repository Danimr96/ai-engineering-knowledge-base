---
id: "lesson:07/11"
type: lesson
ref: 07/11
phase: 7
num: 11
title: Mixture of Experts (MoE)
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 2
community: 5
aliases:
  - 07/11
  - 07-11
tags:
  - phase/07
  - type/build
  - community/05
  - stdlib-only
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/11-mixture-of-experts/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/11-mixture-of-experts"
---

# 07/11 Mixture of Experts (MoE)

> A dense 70B transformer activates every parameter for every token. A 671B MoE activates only 37B per token and beats it on every benchmark. Sparsity is the most important scaling idea of the decade.

**Phase:** [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/07-transformers-deep-dive/11-mixture-of-experts/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/11-mixture-of-experts) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/07-transformers-deep-dive/11-mixture-of-experts) · code: main.py  
**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 7 · 05 (Full Transformer), Phase 7 · 07 (GPT)`

- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]] — Full Transformer
- [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]] — GPT

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]]
- depth 3: [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]]

## Builds on this

- [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]]

## Concepts taught

- Expert `lesson term` — An independent feed-forward network; parameters dedicated to a sparse slice of the FFN computation.
- [[Concepts/Router|Router]] `lesson term` — A tiny linear layer that scores each token against each expert; top-k selection.
- [[Concepts/Top-k routing|Top-k routing]] `lesson term` — Each token's FFN computation goes through exactly k experts, weighted by gate.
- Auxiliary loss `lesson term` — Extra loss term that penalizes skewed expert usage.
- Auxiliary-loss-free `lesson term` — Balance via per-expert bias on the router's selection only; no extra gradient.
- Shared expert `lesson term` — Extra expert through which every token passes; captures common knowledge.
- [[Concepts/Expert Parallelism|Expert Parallelism]] `glossary` — Distribute different experts to different GPUs; route tokens across the network.
- Sparsity `lesson term` — The ratio k × expert_size / (E × expert_size); 37/671 ≈ 5.5% for DeepSeek-V3.
- [[Concepts/MoE (Mixture of Experts)|MoE (Mixture of Experts)]] `glossary` — An architecture with multiple expert subnetworks and a learned router that selects a subset for each input unit, often each token. Sparse activation can increase total parameter capacity without using every expert on every forward pass.

## Ships

- [[Artifacts/07-11 moe-configurator|moe-configurator]] `skill` — Pick expert count, top-k, balancing strategy, and shared-expert layout for a new MoE transformer.

## Further reading

- Shazeer et al. (2017). Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer ([link](https://arxiv.org/abs/1701.06538)) — the idea.
- Fedus, Zoph, Shazeer (2022). Switch Transformer: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity ([link](https://arxiv.org/abs/2101.03961)) — Switch, the classic MoE.
- Kim et al. (2022). DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training ([link](https://arxiv.org/abs/2201.05596)) — original shared-expert paper.
- [[Resources/Jiang et al. (2024). Mixtral of Experts|Jiang et al. (2024). Mixtral of Experts]] ([link](https://arxiv.org/abs/2401.04088)) — Mixtral 8×7B. ·  also cited by 1 other lesson
- Dai et al. (2024). DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models ([link](https://arxiv.org/abs/2401.06066)) — the fine-grained + shared-expert split this lesson's router uses.
- Wang et al. (2024). Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts ([link](https://arxiv.org/abs/2408.15664)) — the bias-based balancing paper.
- [[Resources/DeepSeek-AI (2024). DeepSeek-V3 Technical Report|DeepSeek-AI (2024). DeepSeek-V3 Technical Report]] ([link](https://arxiv.org/abs/2412.19437)) — MLA + auxiliary-loss-free MoE + MTP. ·  also cited by 7 other lessons


%% ── my notes ── %%
