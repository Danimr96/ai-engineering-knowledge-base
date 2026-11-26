---
id: "concept:decoder"
type: concept
name: Decoder
canonical: true
category: "Models & inference"
taught_in: 1
tags:
  - concept/glossary
  - category/models-and-inference
source: ai-engineering-from-scratch/glossary/terms.md
---

# Decoder

> *What people say:* The output side of a model.

**What it actually means:** A component that maps a representation into an output. In an encoder-decoder transformer, the decoder uses masked self-attention and cross-attention to generate outputs. Decoder-only language models instead generate from a single causal stack.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Autoregressive|Autoregressive]]
- [[Concepts/Encoder|Encoder]]
- [[Concepts/Transformer|Transformer]]
- [[Concepts/VAE (Variational Autoencoder)|VAE (Variational Autoencoder)]]

## Taught in

- [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]] — Initialized from context vector. Generates target tokens one at a time.


%% ── my notes ── %%
