---
id: "concept:image-token"
type: concept
name: Image Token
canonical: true
category: Multimodal systems
taught_in: 2
tags:
  - concept/glossary
  - category/multimodal-systems
source: ai-engineering-from-scratch/glossary/terms.md
---

# Image Token

**What it actually means:** A model-specific visual unit represented as a vector or discrete code, commonly derived from an image patch, region, or learned visual-codebook entry.

**Why it matters:** Turning visual input into a sequence lets transformer-style components process images together with text or other tokenized modalities.

**In practice:** Document whether tokens are continuous patches or discrete codes, preserve spatial position, test resolution and aspect-ratio changes, and count visual tokens in the model's input budget.

**Common confusion:** An image token is not necessarily one pixel, one object, or one fixed physical area. Its scope follows the visual encoder or tokenizer.

**Category:** [[Categories/Multimodal systems|Multimodal systems]]

## Related concepts

- [[Concepts/Patch Embedding|Patch Embedding]]
- [[Concepts/Token|Token]]
- [[Concepts/VAE (Variational Autoencoder)|VAE (Variational Autoencoder)]]
- [[Concepts/Vision Transformer (ViT)|Vision Transformer (ViT)]]

## Taught in

- [[Lessons/04-25 Vision-Language Models — The ViT-MLP-LLM Pattern|04/25 Vision-Language Models — The ViT-MLP-LLM Pattern]] — Special token in the text stream replaced by projected vision embeddings
- [[Lessons/12-05 LLaVA and Visual Instruction Tuning|12/05 LLaVA and Visual Instruction Tuning]] — Prompt marker replaced by N projected visual tokens before inference

## Sources

- [[Resources/VQ-VAE|VQ-VAE]] ([link](https://arxiv.org/abs/1711.00937))
- [[Resources/Vision Transformer|Vision Transformer]] ([link](https://arxiv.org/abs/2010.11929))


%% ── my notes ── %%
