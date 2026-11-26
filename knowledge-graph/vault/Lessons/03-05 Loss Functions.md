---
id: "lesson:03/05"
type: lesson
ref: 03/05
phase: 3
num: 5
title: Loss Functions
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 2
concepts: 10
prereqs: 1
community: 22
aliases:
  - 03/05
  - 03-05
tags:
  - phase/03
  - type/build
  - community/22
  - stdlib-only
source: ai-engineering-from-scratch/phases/03-deep-learning-core/05-loss-functions/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/05-loss-functions"
---

# 03/05 Loss Functions

> Your network makes a prediction. The ground truth says otherwise. How wrong is it? That number is the loss. Pick the wrong loss function and your model optimizes for the wrong thing entirely.

**Phase:** [[Phases/03 Deep Learning Core|Phase 3: Deep Learning Core]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/03-deep-learning-core/05-loss-functions/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/03-deep-learning-core/05-loss-functions) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/03-deep-learning-core/05-loss-functions) · code: main.jl, main.py  
**Community:** [[Communities/22 Backward pass · Forward pass · Vanishing gradient|22 Backward pass · Forward pass · Vanishing gradient]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Lesson 03.04 (Activation Functions)`

- [[Lessons/03-04 Activation Functions|03/04 Activation Functions]] — Activation Functions

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]]
- depth 3: [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]]

## Builds on this

- [[Lessons/03-06 Optimizers|03/06 Optimizers]]
- [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]]
- [[Lessons/03-12 Introduction to JAX|03/12 Introduction to JAX]]
- [[Lessons/03-13 Debugging Neural Networks|03/13 Debugging Neural Networks]]

## Concepts taught

- [[Concepts/Loss Function|Loss Function]] `glossary` — A differentiable function mapping predictions and targets to a scalar that the optimizer minimizes
- MSE `lesson term` — Mean of squared differences between predictions and targets; penalizes large errors quadratically
- [[Concepts/Cross-Entropy|Cross-Entropy]] `glossary` — Measures divergence between predicted probability distribution and true distribution using -log(p)
- [[Concepts/Binary cross-entropy|Binary cross-entropy]] `lesson term` — Cross-entropy for two classes: -(ylog(p) + (1-y)log(1-p))
- [[Concepts/Label smoothing|Label smoothing]] `lesson term` — Replacing hard 0/1 targets with soft values (e.g., 0.1/0.9) to prevent overconfidence and improve generalization
- Contrastive loss `lesson term` — A loss that learns representations by making similar pairs close and dissimilar pairs far in embedding space
- [[Concepts/InfoNCE|InfoNCE]] `lesson term` — Normalized temperature-scaled cross-entropy over similarity scores; treats contrastive learning as classification
- Focal loss `lesson term` — Cross-entropy weighted by (1-p_t)^gamma to down-weight easy examples and focus on hard ones
- [[Concepts/Triplet loss|Triplet loss]] `lesson term` — Pushes anchor closer to positive than negative by at least a margin in embedding space
- [[Concepts/Temperature|Temperature]] `glossary` — A scalar divisor on logits/similarities that controls how peaked the resulting distribution is; lower = sharper

## Ships

- [[Artifacts/03-05 prompt-loss-debugger|prompt-loss-debugger]] `prompt` — A diagnostic prompt for debugging loss curves and training failures
- [[Artifacts/03-05 prompt-loss-function-selector|prompt-loss-function-selector]] `prompt` — A decision prompt for choosing the right loss function for any ML task


%% ── my notes ── %%
