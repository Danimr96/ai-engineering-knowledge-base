---
id: "concept:inductive-bias"
type: concept
name: Inductive Bias
canonical: true
category: "Models & inference"
taught_in: 2
community: 47
tags:
  - concept/glossary
  - category/models-and-inference
  - community/47
source: ai-engineering-from-scratch/glossary/terms.md
---

# Inductive Bias

**Community:** [[Communities/47 Feature · Latent Space · CNN (Convolutional Neural Network)|47 Feature · Latent Space · CNN (Convolutional Neural Network)]]

> *What people say:* Assumptions built into a learning system.

**What it actually means:** Structural or statistical assumptions that favor some functions or representations over others. Convolution favors locality and shared filters; causal masking favors prediction from preceding positions.

**Common confusion:** Transformers still have inductive biases through tokenization, position handling, masking, architecture, data, and objective.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/CNN (Convolutional Neural Network)|CNN (Convolutional Neural Network)]]
- [[Concepts/Feature|Feature]]
- [[Concepts/Transformer|Transformer]]

## Taught in

- [[Lessons/07-01 Why Transformers — The Problems with RNNs|07/01 Why Transformers — The Problems with RNNs]] — Prior about what the data looks like; CNNs assume translation invariance, RNNs assume recency.
- [[Lessons/07-09 Vision Transformers (ViT)|07/09 Vision Transformers (ViT)]] — ViT has fewer priors than CNNs; needs more data to make up the gap.


%% ── my notes ── %%
