---
id: "lesson:08/14"
type: lesson
ref: 08/14
phase: 8
num: 14
title: "Evaluation — FID, CLIP Score, Human Preference"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 88
aliases:
  - 08/14
  - 08-14
tags:
  - phase/08
  - type/build
  - community/88
  - stdlib-only
source: ai-engineering-from-scratch/phases/08-generative-ai/14-evaluation-fid-clip-score/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/14-evaluation-fid-clip-score"
---

# 08/14 Evaluation — FID, CLIP Score, Human Preference

> Every generative model leaderboard cites FID, CLIP score, and a win rate from a human-preference arena. Each number has a failure mode a determined researcher can game. If you do not know the failure modes, you cannot tell a real improvement from a gaming run.

**Phase:** [[Phases/08 Generative AI|Phase 8: Generative AI]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/08-generative-ai/14-evaluation-fid-clip-score/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/14-evaluation-fid-clip-score) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/08-generative-ai/14-evaluation-fid-clip-score) · code: main.py  
**Community:** [[Communities/88 FID · Generative model|88 FID · Generative model]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 8 · 01 (Taxonomy), Phase 2 · 04 (Evaluation Metrics)`

- [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]] — Evaluation Metrics
- [[Lessons/08-01 Generative Models — Taxonomy & History|08/01 Generative Models — Taxonomy & History]] — Taxonomy

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/07-14 Build a Transformer from Scratch — The Capstone|07/14 Build a Transformer from Scratch — The Capstone]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/07-01 Why Transformers — The Problems with RNNs|07/01 Why Transformers — The Problems with RNNs]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]], [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]], [[Lessons/07-08 T5, BART — Encoder-Decoder Models|07/08 T5, BART — Encoder-Decoder Models]], [[Lessons/07-09 Vision Transformers (ViT)|07/09 Vision Transformers (ViT)]], [[Lessons/07-10 Audio Transformers — Whisper Architecture|07/10 Audio Transformers — Whisper Architecture]], [[Lessons/07-11 Mixture of Experts (MoE)|07/11 Mixture of Experts (MoE)]], [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]], [[Lessons/07-13 Scaling Laws|07/13 Scaling Laws]]

## Concepts taught

- [[Concepts/FID|FID]] `lesson term` — Fréchet distance of Gaussian fits to real vs gen Inception features.
- CLIP score `lesson term` — Cosine similarity between CLIP image and text embeddings.
- CMMD `lesson term` — CLIP-feature MMD; less biased, no Gaussian assumption.
- IS `lesson term` — p(y)); correlates poorly on modern models, retired.
- HPSv2 / ImageReward / PickScore `lesson term` — Small models trained on human preferences; used as automatic judges.
- Elo `lesson term` — Bradley-Terry aggregation of pairwise wins.
- PartiPrompts `lesson term` — 1,600 Google-curated prompts across 12 categories.
- FD-DINO `lesson term` — FD using DINOv2 features; better for out-of-ImageNet domains.

## Ships

- [[Artifacts/08-14 eval-report|eval-report]] `skill` — Plan a full generative-model evaluation: sample quality, adherence, preference, failure audit.

## Further reading

- Heusel et al. (2017). GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium (FID) ([link](https://arxiv.org/abs/1706.08500)) — FID paper.
- [[Resources/CLIP|CLIP]] ([link](https://arxiv.org/abs/2103.00020)) — CLIP. ·  also cited by 2 other lessons
- Yu et al. (2023). Scaling Autoregressive Models for Content-Rich Text-to-Image Generation (Parti + PartiPrompts) ([link](https://arxiv.org/abs/2206.10789)) — PartiPrompts.
- Xu et al. (2023). ImageReward: Learning and Evaluating Human Preferences for Text-to-Image Generation ([link](https://arxiv.org/abs/2304.05977)) — ImageReward.
- Stein et al. (2023). Exposing flaws of generative model evaluation metrics ([link](https://arxiv.org/abs/2306.04675)) — failure-mode survey.
- Wu et al. (2023). HPSv2: A Comprehensive Human Preference Score ([link](https://arxiv.org/abs/2306.09341)) — HPSv2.
- Jayasumana et al. (2024). Rethinking FID: Towards a Better Evaluation Metric for Image Generation (CMMD) ([link](https://arxiv.org/abs/2401.09603)) — CMMD.


%% ── my notes ── %%
