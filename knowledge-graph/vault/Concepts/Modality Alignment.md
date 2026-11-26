---
id: "concept:modality-alignment"
type: concept
name: Modality Alignment
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

# Modality Alignment

**Community:** [[Communities/59 Multimodal Fusion · Early Fusion · Late Fusion|59 Multimodal Fusion · Early Fusion · Late Fusion]]

**What it actually means:** Learning or establishing correspondences between representations from different modalities so semantically or temporally related items can be matched.

**Why it matters:** Fusion and cross-modal retrieval fail when the system cannot connect the same event, object, or concept across differently structured inputs.

**In practice:** Define positive and negative pairs, preserve time or spatial metadata, evaluate mismatched examples, and measure alignment separately from downstream task accuracy.

**Common confusion:** Alignment makes representations comparable or corresponding. It does not require them to become identical or erase modality-specific information.

**Category:** [[Categories/Multimodal systems|Multimodal systems]]

## Related concepts

- [[Concepts/Contrastive Learning|Contrastive Learning]]
- [[Concepts/Early Fusion|Early Fusion]]
- [[Concepts/Grounding|Grounding]]
- [[Concepts/Multimodal Fusion|Multimodal Fusion]]
- [[Concepts/Shared Embedding Space|Shared Embedding Space]]

## Taught in

- [[Lessons/19-60 Projection Layer for Modality Alignment|19/60 Projection Layer for Modality Alignment]] — The act of making image and text embeddings comparable in one shared space

## Sources

- Learning Transferable Visual Models From Natural Language Supervision ([link](https://proceedings.mlr.press/v139/radford21a.html))


%% ── my notes ── %%
