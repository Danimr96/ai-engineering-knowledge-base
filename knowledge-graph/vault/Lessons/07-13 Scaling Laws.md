---
id: "lesson:07/13"
type: lesson
ref: 07/13
phase: 7
num: 13
title: Scaling Laws
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 5
aliases:
  - 07/13
  - 07-13
tags:
  - phase/07
  - type/learn
  - community/05
  - stdlib-only
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/13-scaling-laws/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/13-scaling-laws"
---

# 07/13 Scaling Laws

> The 2020 Kaplan paper said: bigger model, lower loss. The 2022 Hoffmann paper said: you were under-training. Compute goes into two buckets — parameters and tokens — and the split is not obvious.

**Phase:** [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/07-transformers-deep-dive/13-scaling-laws/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/07-transformers-deep-dive/13-scaling-laws) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/07-transformers-deep-dive/13-scaling-laws) · code: main.py  
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

- [[Concepts/Parameter|Parameter]] (as *Parameters (N)*) `glossary` — Non-embedding weight count; determines capacity.
- [[Concepts/Token|Token]] (as *Tokens (D)*) `glossary` — Number of training tokens seen; determines how well the parameters get used.
- Compute (as *Compute (C)*) `lesson term` — Approximately 6 × N × D for a standard transformer.
- Chinchilla-optimal `lesson term` — Ratio that minimizes loss per FLOP of pretraining.
- Over-training `lesson term` — Spend extra training FLOPs to save inference FLOPs; D/N >> 20.
- Irreducible loss `lesson term` — The E term in the scaling law; the entropy of the data itself.
- Emergent capability `lesson term` — Often a scorer artifact; continuous loss is smooth.
- Effective compute `lesson term` — Better data / optimizer / architecture multiplies how far a FLOP goes.

## Ships

- [[Artifacts/07-13 training-budget-estimator|training-budget-estimator]] `skill` — Estimate (N, D, hours, GPU count) for a new transformer training run given compute budget and deployment constraints.

## Further reading

- [[Resources/Kaplan et al. (2020). Scaling Laws for Neural Language Models|Kaplan et al. (2020). Scaling Laws for Neural Language Models]] ([link](https://arxiv.org/abs/2001.08361)) — the first scaling law paper; undertrained. ·  also cited by 1 other lesson
- [[Resources/Hoffmann et al. (2022). Training Compute-Optimal Large Language Models|Hoffmann et al. (2022). Training Compute-Optimal Large Language Models]] ([link](https://arxiv.org/abs/2203.15556)) — Chinchilla. ·  also cited by 2 other lessons
- Schaeffer et al. (2023). Are Emergent Abilities of Large Language Models a Mirage? ([link](https://arxiv.org/abs/2304.15004)) — emergence as measurement artifact.
- Sardana, Frankle (2024). Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws ([link](https://arxiv.org/abs/2401.00448)) — why Llama's over-training is right for its workload.
- Jordan et al. (2024). Muon: An optimizer for hidden layers in neural networks ([link](https://kellerjordan.github.io/posts/muon/)) — 2× compute multiplier.


%% ── my notes ── %%
