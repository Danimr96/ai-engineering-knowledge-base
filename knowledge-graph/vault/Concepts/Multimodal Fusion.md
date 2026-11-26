---
id: "concept:multimodal-fusion"
type: concept
name: Multimodal Fusion
canonical: true
category: Multimodal systems
taught_in: 1
community: 59
tags:
  - concept/glossary
  - category/multimodal-systems
  - community/59
source: ai-engineering-from-scratch/glossary/terms.md
---

# Multimodal Fusion

**Community:** [[Communities/59 Multimodal Fusion · Early Fusion · Late Fusion|59 Multimodal Fusion · Early Fusion · Late Fusion]]

**What it actually means:** Combining evidence or learned representations from more than one modality to produce a joint representation, prediction, or generated output.

**Why it matters:** Modalities can supply complementary evidence, but naïve combination can amplify noise, timing errors, or one dominant stream.

**In practice:** Establish single-modality baselines, specify the fusion point and masks, test missing and contradictory inputs, and report which modalities drive each evaluated slice.

**Common confusion:** Fusion is the combination operation. Alignment establishes correspondence, and merely placing two modalities in one request does not prove either occurred successfully.

**Category:** [[Categories/Multimodal systems|Multimodal systems]]

## Related concepts

- [[Concepts/Cross-Attention|Cross-Attention]]
- [[Concepts/Early Fusion|Early Fusion]]
- [[Concepts/Late Fusion|Late Fusion]]
- [[Concepts/Modality Alignment|Modality Alignment]]
- [[Concepts/Multimodal Model|Multimodal Model]]

## Taught in

- [[Lessons/19-61 Cross-Attention Fusion|19/61 Cross-Attention Fusion]]

## Sources

- Multimodal Deep Learning ([link](https://ai.stanford.edu/~ang/papers/icml11-MultimodalDeepLearning.pdf))
- Multimodal Machine Learning: A Survey and Taxonomy ([link](https://arxiv.org/abs/1705.09406))


%% ── my notes ── %%
