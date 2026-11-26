---
id: "concept:vanishing-gradient"
type: concept
name: Vanishing gradient
canonical: false
taught_in: 3
community: 22
tags:
  - concept/lesson-term
  - community/22
source: ai-engineering-from-scratch/phases/03-deep-learning-core/03-backpropagation/docs/en.md
---

# Vanishing gradient

**Community:** [[Communities/22 Backward pass · Forward pass · Vanishing gradient|22 Backward pass · Forward pass · Vanishing gradient]]

> *What people say:* "Deep networks don't learn"

**What it actually means:** Gradients shrink exponentially as they propagate through layers with saturating activations like sigmoid

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]]
- [[Lessons/03-04 Activation Functions|03/04 Activation Functions]] — Gradients shrink exponentially through layers when the activation's derivative is less than 1, making early layers untrainable
- [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]] — Repeated multiplication by <1 weights in plain RNNs makes early-step gradients effectively zero.


%% ── my notes ── %%
