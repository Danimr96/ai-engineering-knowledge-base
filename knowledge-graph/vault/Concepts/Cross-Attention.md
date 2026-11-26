---
id: "concept:cross-attention"
type: concept
name: Cross-Attention
canonical: true
category: Multimodal systems
taught_in: 6
community: 12
tags:
  - concept/glossary
  - category/multimodal-systems
  - community/12
source: ai-engineering-from-scratch/glossary/terms.md
---

# Cross-Attention

**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]]

**What it actually means:** Attention in which the query representation comes from one sequence or representation while keys and values come from another.

**Why it matters:** It gives one stream a learnable way to retrieve information from another, such as language tokens attending to visual features.

**In practice:** State which stream supplies queries, keys, and values, apply masks for missing or invalid positions, and inspect whether the model still performs when one modality is ablated.

**Common confusion:** Cross-attention is not intrinsically multimodal. It can connect two text sequences or other representations; self-attention instead derives queries, keys, and values from the same sequence representation.

**Category:** [[Categories/Multimodal systems|Multimodal systems]]

## Related concepts

- [[Concepts/Attention|Attention]]
- [[Concepts/Multimodal Fusion|Multimodal Fusion]]
- [[Concepts/Self-Attention|Self-Attention]]
- [[Concepts/Vision-Language Model (VLM)|Vision-Language Model (VLM)]]

## Taught in

- [[Lessons/04-11 Stable Diffusion — Architecture & Fine-Tuning|04/11 Stable Diffusion — Architecture & Fine-Tuning]] — Attention from latent tokens to text tokens; injects prompt information at every U-Net level
- [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]] — MHA with Q from decoder, K/V from encoder outputs.
- [[Lessons/07-08 T5, BART — Encoder-Decoder Models|07/08 T5, BART — Encoder-Decoder Models]] — Decoder's Q × encoder's K/V. The only place encoder information enters the decoder.
- [[Lessons/08-07 Latent Diffusion & Stable Diffusion|08/07 Latent Diffusion & Stable Diffusion]] — Each U-Net block attends to text tokens as K and V.
- [[Lessons/12-03 From CLIP to BLIP-2 — Q-Former as Modality Bridge|12/03 From CLIP to BLIP-2 — Q-Former as Modality Bridge]] — Attention where query, key, and value come from different sources; how the queries pull from ViT patches
- [[Lessons/19-61 Cross-Attention Fusion|19/61 Cross-Attention Fusion]] — Q comes from one stream, K and V from another

## Sources

- [[Resources/Attention Is All You Need|Attention Is All You Need]] ([link](https://arxiv.org/abs/1706.03762))


%% ── my notes ── %%
