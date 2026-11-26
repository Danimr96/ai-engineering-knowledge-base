---
id: "concept:shared-embedding-space"
type: concept
name: Shared Embedding Space
canonical: true
category: Multimodal systems
taught_in: 1
community: 18
tags:
  - concept/glossary
  - category/multimodal-systems
  - community/18
source: ai-engineering-from-scratch/glossary/terms.md
---

# Shared Embedding Space

**Community:** [[Communities/18 Embedding · Cosine Similarity · HNSW|18 Embedding · Cosine Similarity · HNSW]]

**What it actually means:** A common vector space in which representations from different modalities can be compared with the same similarity function.

**Why it matters:** It enables cross-modal retrieval and matching, such as finding images from text, without requiring both items to share a raw representation.

**In practice:** Train paired and unpaired negatives deliberately, normalize vectors when the objective requires it, evaluate both retrieval directions, and inspect subgroup and language performance.

**Common confusion:** Sharing a vector dimension does not create a shared semantic space. The training objective and data must establish cross-modal comparability.

**Category:** [[Categories/Multimodal systems|Multimodal systems]]

## Related concepts

- [[Concepts/Cosine Similarity|Cosine Similarity]]
- [[Concepts/Embedding|Embedding]]
- [[Concepts/Modality Alignment|Modality Alignment]]
- [[Concepts/Semantic Search|Semantic Search]]

## Taught in

- [[Lessons/12-02 CLIP and Contrastive Vision-Language Pretraining|12/02 CLIP and Contrastive Vision-Language Pretraining]]

## Sources

- Learning Transferable Visual Models From Natural Language Supervision ([link](https://proceedings.mlr.press/v139/radford21a.html))


%% ── my notes ── %%
