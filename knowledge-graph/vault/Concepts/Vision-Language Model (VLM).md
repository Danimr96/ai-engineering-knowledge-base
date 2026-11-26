---
id: "concept:vision-language-model-vlm"
type: concept
name: Vision-Language Model (VLM)
canonical: true
category: Multimodal systems
taught_in: 2
community: 12
tags:
  - concept/glossary
  - category/multimodal-systems
  - community/12
source: ai-engineering-from-scratch/glossary/terms.md
---

# Vision-Language Model (VLM)

**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]]

**What it actually means:** A model that learns relationships between, or jointly processes, visual and language representations for tasks such as retrieval, description, question answering, or grounded generation.

**Why it matters:** VLM performance depends on the visual encoder, language component, connection mechanism, training data, and resolution policy rather than one generic capability label.

**In practice:** Evaluate text-only and vision-only controls, vary image resolution and layout, require evidence localization where possible, and report failures by visual skill and language.

**Common confusion:** Accepting an image does not prove the model uses it correctly, and a VLM is not necessarily able to generate images.

**Category:** [[Categories/Multimodal systems|Multimodal systems]]

## Related concepts

- [[Concepts/Cross-Attention|Cross-Attention]]
- [[Concepts/Multimodal Model|Multimodal Model]]
- [[Concepts/Vision Transformer (ViT)|Vision Transformer (ViT)]]
- [[Concepts/Visual Grounding|Visual Grounding]]

## Taught in

- [[Lessons/04-18 Open-Vocabulary Vision — CLIP|04/18 Open-Vocabulary Vision — CLIP]] `alias` — A CLIP-family encoder plus an LLM, trained to answer questions about images
- [[Lessons/04-25 Vision-Language Models — The ViT-MLP-LLM Pattern|04/25 Vision-Language Models — The ViT-MLP-LLM Pattern]]

## Sources

- [[Resources/CLIP|CLIP]] ([link](https://arxiv.org/abs/2103.00020))
- Flamingo: a Visual Language Model for Few-Shot Learning ([link](https://arxiv.org/abs/2204.14198))


%% ── my notes ── %%
