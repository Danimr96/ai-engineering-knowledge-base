---
id: "concept:vision-transformer-vit"
type: concept
name: Vision Transformer (ViT)
canonical: true
category: Multimodal systems
taught_in: 1
tags:
  - concept/glossary
  - category/multimodal-systems
source: ai-engineering-from-scratch/glossary/terms.md
---

# Vision Transformer (ViT)

**What it actually means:** A vision architecture that represents an image as a sequence of patch embeddings with position information and processes that sequence with transformer encoder blocks.

**Why it matters:** It provides a sequence-model interface for visual data, but performance and compute depend on patch size, resolution, pretraining, and inductive biases.

**In practice:** Keep patching and normalization consistent with training, account for position-embedding behavior at new resolutions, and compare against a suitable visual baseline on the target dataset.

**Common confusion:** ViT is an architecture family, not every transformer that accepts images, and its patches are not inherently semantic objects.

**Category:** [[Categories/Multimodal systems|Multimodal systems]]

## Related concepts

- [[Concepts/Encoder|Encoder]]
- [[Concepts/Image Token|Image Token]]
- [[Concepts/Patch Embedding|Patch Embedding]]
- [[Concepts/Self-Attention|Self-Attention]]
- [[Concepts/Transformer|Transformer]]
- [[Concepts/Vision-Language Model (VLM)|Vision-Language Model (VLM)]]

## Taught in

- [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]]

## Sources

- [[Resources/Vision Transformer|Vision Transformer]] ([link](https://arxiv.org/abs/2010.11929))


%% ── my notes ── %%
