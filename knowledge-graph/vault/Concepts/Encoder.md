---
id: "concept:encoder"
type: concept
name: Encoder
canonical: true
category: "Models & inference"
taught_in: 1
tags:
  - concept/glossary
  - category/models-and-inference
source: ai-engineering-from-scratch/glossary/terms.md
---

# Encoder

> *What people say:* The input side of a model.

**What it actually means:** A component that transforms input into a representation. A transformer encoder commonly uses non-causal self-attention, subject to any masks, so each position can incorporate context from across the input.

**Common confusion:** Encoder-only models can produce outputs through task heads even though they are not typically used for autoregressive text generation.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Automatic Speech Recognition (ASR)|Automatic Speech Recognition (ASR)]]
- [[Concepts/Decoder|Decoder]]
- [[Concepts/Embedding|Embedding]]
- [[Concepts/Transformer|Transformer]]
- [[Concepts/VAE (Variational Autoencoder)|VAE (Variational Autoencoder)]]
- [[Concepts/Vision Transformer (ViT)|Vision Transformer (ViT)]]

## Taught in

- [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]] — Reads source. Produces per-step hidden states and a final context vector.


%% ── my notes ── %%
