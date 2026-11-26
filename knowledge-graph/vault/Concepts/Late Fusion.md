---
id: "concept:late-fusion"
type: concept
name: Late Fusion
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

# Late Fusion

**Community:** [[Communities/59 Multimodal Fusion · Early Fusion · Late Fusion|59 Multimodal Fusion · Early Fusion · Late Fusion]]

**What it actually means:** Processing modalities through separate encoders or predictors and combining their high-level representations, scores, or decisions near the task output.

**Why it matters:** Separate branches can use modality-specific architectures and tolerate missing inputs, though they may miss fine-grained interactions available to earlier fusion.

**In practice:** Calibrate each branch, define how missing modalities affect the merge, compare score-level and feature-level combinations, and evaluate each branch alone as an ablation.

**Common confusion:** Late fusion describes the position of combination. It does not mean simple averaging or guarantee that the modalities contribute equally.

**Category:** [[Categories/Multimodal systems|Multimodal systems]]

## Related concepts

- [[Concepts/Early Fusion|Early Fusion]]
- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]]
- [[Concepts/Modality|Modality]]
- [[Concepts/Multimodal Fusion|Multimodal Fusion]]

## Taught in

- [[Lessons/19-61 Cross-Attention Fusion|19/61 Cross-Attention Fusion]] — Text and vision stay in separate streams; cross-attention bridges them at every block

## Sources

- Multimodal Deep Learning ([link](https://ai.stanford.edu/~ang/papers/icml11-MultimodalDeepLearning.pdf))
- Multimodal Machine Learning: A Survey and Taxonomy ([link](https://arxiv.org/abs/1705.09406))


%% ── my notes ── %%
