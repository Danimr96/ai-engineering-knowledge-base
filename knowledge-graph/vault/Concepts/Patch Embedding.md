---
id: "concept:patch-embedding"
type: concept
name: Patch Embedding
canonical: true
category: Multimodal systems
taught_in: 4
tags:
  - concept/glossary
  - category/multimodal-systems
source: ai-engineering-from-scratch/glossary/terms.md
---

# Patch Embedding

**What it actually means:** A learned projection that converts an image patch into a fixed-width vector used as one element of a transformer input sequence.

**Why it matters:** It creates the interface between a spatial image grid and a sequence model, with patch size controlling token count and retained local detail.

**In practice:** Record patch and image dimensions, handle padding or resizing explicitly, add position information, and measure how resolution changes affect both accuracy and token cost.

**Common confusion:** A patch embedding is the vector representation of a patch, not a semantic object detector or a guarantee that patch boundaries match visual entities.

**Category:** [[Categories/Multimodal systems|Multimodal systems]]

## Related concepts

- [[Concepts/Embedding|Embedding]]
- [[Concepts/Image Token|Image Token]]
- [[Concepts/Token|Token]]
- [[Concepts/Vision Transformer (ViT)|Vision Transformer (ViT)]]

## Taught in

- [[Lessons/04-14 Vision Transformers (ViT)|04/14 Vision Transformers (ViT)]] — A conv with kernel size = stride = patch size; turns the image into a grid of token embeddings
- [[Lessons/12-01 Vision Transformers and the Patch-Token Primitive|12/01 Vision Transformers and the Patch-Token Primitive]] — A shared learned matrix (or Conv2d with stride=P) mapping flattened patch pixels to D-dim vectors
- [[Lessons/12-23 ColPali and Vision-Native Document RAG|12/23 ColPali and Vision-Native Document RAG]] — One vector per image patch from a VLM encoder, cached per page
- [[Lessons/19-58 Vision Encoder Patches|19/58 Vision Encoder Patches]] — Linear projection of one flattened patch to the hidden dim

## Sources

- [[Resources/Vision Transformer|Vision Transformer]] ([link](https://arxiv.org/abs/2010.11929))


%% ── my notes ── %%
