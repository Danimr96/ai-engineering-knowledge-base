---
id: "concept:visual-grounding"
type: concept
name: Visual Grounding
canonical: true
category: Multimodal systems
taught_in: 1
community: 12
tags:
  - concept/glossary
  - category/multimodal-systems
  - community/12
source: ai-engineering-from-scratch/glossary/terms.md
---

# Visual Grounding

**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]]

**What it actually means:** Connecting a language expression to spatial evidence in an image or video, such as a region, object, mask, or tracked entity.

**Why it matters:** A fluent visual answer can be unsupported, while grounding makes the claimed referent inspectable and enables region-level evaluation.

**In practice:** Require a box, mask, or temporal segment with the answer, test ambiguous and absent referents, and score localization separately from language correctness.

**Common confusion:** Visual grounding identifies where the referenced evidence is. General image captioning can describe a scene without localizing each claim.

**Category:** [[Categories/Multimodal systems|Multimodal systems]]

## Related concepts

- [[Concepts/Attention|Attention]]
- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]]
- [[Concepts/Grounding|Grounding]]
- [[Concepts/Vision-Language Model (VLM)|Vision-Language Model (VLM)]]

## Taught in

- [[Lessons/19-61 Cross-Attention Fusion|19/61 Cross-Attention Fusion]]

## Sources

- MDETR ([link](https://arxiv.org/abs/2104.12763))


%% ── my notes ── %%
