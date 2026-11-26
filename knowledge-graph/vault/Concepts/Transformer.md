---
id: "concept:transformer"
type: concept
name: Transformer
canonical: true
category: "Models & inference"
taught_in: 1
tags:
  - concept/glossary
  - category/models-and-inference
source: ai-engineering-from-scratch/glossary/terms.md
---

# Transformer

> *What people say:* The architecture behind many modern language models.

**What it actually means:** A neural-network architecture built from attention, position information, feed-forward sublayers, residual connections, and normalization. Encoder, decoder, and encoder-decoder variants use different masks and information flows.

**Why it matters:** Training can process many sequence positions in parallel, while autoregressive generation still produces outputs step by step.

**Common confusion:** Self-attention does not imply unrestricted all-to-all attention in every transformer.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Attention|Attention]]
- [[Concepts/Decoder|Decoder]]
- [[Concepts/Encoder|Encoder]]
- [[Concepts/GPT|GPT]]
- [[Concepts/Inductive Bias|Inductive Bias]]
- [[Concepts/LLM (Large Language Model)|LLM (Large Language Model)]]
- [[Concepts/MoE (Mixture of Experts)|MoE (Mixture of Experts)]]
- [[Concepts/Multimodal Model|Multimodal Model]]
- [[Concepts/Self-Attention|Self-Attention]]
- [[Concepts/Vision Transformer (ViT)|Vision Transformer (ViT)]]

## Taught in

- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]]

## Sources

- [[Resources/Attention Is All You Need|Attention Is All You Need]] ([link](https://arxiv.org/abs/1706.03762))


%% ── my notes ── %%
