---
id: "concept:modality"
type: concept
name: Modality
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

# Modality

**Community:** [[Communities/59 Multimodal Fusion · Early Fusion · Late Fusion|59 Multimodal Fusion · Early Fusion · Late Fusion]]

**What it actually means:** A form of information with its own structure and acquisition process, such as text, image, audio, video, depth, or sensor measurements.

**Why it matters:** Different modalities have different sampling rates, noise, spatial or temporal structure, and missing-data behavior, so one preprocessing assumption rarely fits all of them.

**In practice:** Document each modality's source, units, resolution, timing, preprocessing, and missing-value policy before designing alignment or fusion.

**Common confusion:** A modality is not merely a file extension or feature column. Several encodings can represent one modality, and one sample can contain several modalities.

**Category:** [[Categories/Multimodal systems|Multimodal systems]]

## Related concepts

- [[Concepts/Embedding|Embedding]]
- [[Concepts/Late Fusion|Late Fusion]]
- [[Concepts/Multimodal Model|Multimodal Model]]
- [[Concepts/Tensor|Tensor]]
- [[Concepts/Token|Token]]

## Taught in

- [[Lessons/12-16 MIO and Any-to-Any Streaming Multimodal Models|12/16 MIO and Any-to-Any Streaming Multimodal Models]]

## Sources

- Multimodal Machine Learning: A Survey and Taxonomy ([link](https://arxiv.org/abs/1705.09406))
- ImageBind: One Embedding Space To Bind Them All ([link](https://arxiv.org/abs/2305.05665))


%% ── my notes ── %%
