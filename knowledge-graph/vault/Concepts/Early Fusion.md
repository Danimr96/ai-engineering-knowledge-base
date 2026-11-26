---
id: "concept:early-fusion"
type: concept
name: Early Fusion
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

# Early Fusion

**Community:** [[Communities/59 Multimodal Fusion · Early Fusion · Late Fusion|59 Multimodal Fusion · Early Fusion · Late Fusion]]

**What it actually means:** Combining raw or low-level representations from several modalities before most task-specific modeling occurs.

**Why it matters:** Early interaction can expose fine-grained cross-modal relationships, but it also requires compatible representations and careful handling of alignment and missing inputs.

**In practice:** Convert each modality into a declared token or feature representation, preserve source and position markers, fuse them before the shared backbone, and compare against single-modality and late-fusion baselines.

**Common confusion:** Early fusion describes where streams are combined in the architecture. It does not guarantee that the model learns useful alignment between them.

**Category:** [[Categories/Multimodal systems|Multimodal systems]]

## Related concepts

- [[Concepts/Late Fusion|Late Fusion]]
- [[Concepts/Modality Alignment|Modality Alignment]]
- [[Concepts/Multimodal Fusion|Multimodal Fusion]]
- [[Concepts/Token|Token]]

## Taught in

- [[Lessons/12-11 Chameleon and Early-Fusion Token-Only Multimodal Models|12/11 Chameleon and Early-Fusion Token-Only Multimodal Models]] — Images converted to discrete tokens sharing the transformer's vocabulary from step one

## Sources

- Multimodal Machine Learning: A Survey and Taxonomy ([link](https://arxiv.org/abs/1705.09406))
- Chameleon: Mixed-Modal Early-Fusion Foundation Models ([link](https://arxiv.org/abs/2405.09818))


%% ── my notes ── %%
