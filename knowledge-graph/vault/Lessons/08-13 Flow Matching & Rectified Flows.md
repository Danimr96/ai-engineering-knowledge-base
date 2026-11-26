---
id: "lesson:08/13"
type: lesson
ref: 08/13
phase: 8
num: 13
title: "Flow Matching & Rectified Flows"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
aliases:
  - 08/13
  - 08-13
tags:
  - phase/08
  - type/build
  - stdlib-only
source: ai-engineering-from-scratch/phases/08-generative-ai/13-flow-matching-rectified-flows/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/13-flow-matching-rectified-flows"
---

# 08/13 Flow Matching & Rectified Flows

> Diffusion models take 20-50 sampling steps because they walk a curved path from noise to data. Flow matching (Lipman et al., 2023) and rectified flow (Liu et al., 2022) trained straight paths. Straighter paths mean fewer steps mean faster inference. Stable Diffusion 3, Flux.1, and AudioCraft 2 all switched to flow matching in 2024.

**Phase:** [[Phases/08 Generative AI|Phase 8: Generative AI]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/08-generative-ai/13-flow-matching-rectified-flows/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/08-generative-ai/13-flow-matching-rectified-flows) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/08-generative-ai/13-flow-matching-rectified-flows) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 8 · 06 (DDPM), Phase 1 · Calculus`

- [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]] — Header says 'Phase 1 · Calculus' with no number; 01/04 is Calculus for Machine Learning. ·  low confidence ·  from override
- [[Lessons/08-06 Diffusion Models — DDPM from Scratch|08/06 Diffusion Models — DDPM from Scratch]] — DDPM
- Whole phase: [[Phases/01 Math Foundations|Phase 1: Math Foundations]] ·  medium confidence
- Not understood by the parser: `Calculus`

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/08-02 Autoencoders & Variational Autoencoders (VAE)|08/02 Autoencoders & Variational Autoencoders (VAE)]]
- depth 3: [[Lessons/03-01 The Perceptron|03/01 The Perceptron]], [[Lessons/03-07 Regularization|03/07 Regularization]], [[Lessons/08-01 Generative Models — Taxonomy & History|08/01 Generative Models — Taxonomy & History]]

## Concepts taught

- [[Concepts/Flow matching|Flow matching]] `lesson term` — Train vθ(x, t) to match x_1 - x_0 along an interpolant.
- [[Concepts/Rectified flow|Rectified flow]] `lesson term` — Iterative procedure that straightens learned flows.
- Velocity field `lesson term` — Output of the model — the direction to move x_t.
- Straight-line interpolant `lesson term` — x_t = (1-t)·x_0 + t·x_1; trivial target derivative.
- Euler sampler `lesson term` — Simplest integrator; works well when paths are straight.
- Logit-normal t `lesson term` — Concentrate t sampling toward mid-values where gradients are strongest.
- Consistency distillation `lesson term` — Train a student to map any x_t directly to x_0.
- CFG with velocity `lesson term` — v_cfg = (1+w) v_cond - w v_uncond; same trick, new variable.

## Ships

- [[Artifacts/08-13 fm-tuner|fm-tuner]] `skill` — Convert a diffusion training plan into a flow-matching / rectified-flow config.

## Further reading

- Liu, Gong, Liu (2022). Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow ([link](https://arxiv.org/abs/2209.03003)) — rectified flow.
- [[Resources/Lipman et al. (2023). Flow Matching for Generative Modeling|Lipman et al. (2023). Flow Matching for Generative Modeling]] ([link](https://arxiv.org/abs/2210.02747)) — flow matching. ·  also cited by 1 other lesson
- Song et al. (2023). Consistency Models ([link](https://arxiv.org/abs/2303.01469)) — 1-step distillation of diffusion / flow.
- Albergo, Vanden-Eijnden (2023). Stochastic Interpolants ([link](https://arxiv.org/abs/2303.08797)) — general framework that covers FM + diffusion.
- [[Resources/Sauer et al. (2023). Adversarial Diffusion Distillation|Sauer et al. (2023). Adversarial Diffusion Distillation]] ([link](https://arxiv.org/abs/2311.17042)) — turbo variant. ·  also cited by 1 other lesson
- [[Resources/Scaling Rectified Flow Transformers (Esser et al., SD3 paper)|Scaling Rectified Flow Transformers (Esser et al., SD3 paper)]] ([link](https://arxiv.org/abs/2403.03206)) — SD3, rectified flow at scale. ·  also cited by 4 other lessons
- [[Resources/Labs (2024). Flux.1 — Black Forest Labs announcement|Labs (2024). Flux.1 — Black Forest Labs announcement]] ([link](https://blackforestlabs.ai/announcing-black-forest-labs/)) — flow matching in production. ·  also cited by 1 other lesson


%% ── my notes ── %%
