---
id: "concept:quantization"
type: concept
name: Quantization
canonical: true
category: "Models & inference"
taught_in: 1
community: 48
tags:
  - concept/glossary
  - category/models-and-inference
  - community/48
source: ai-engineering-from-scratch/glossary/terms.md
---

# Quantization

**Community:** [[Communities/48 Fine-tuning · QLoRA · LoRA (Low-Rank Adaptation)|48 Fine-tuning · QLoRA · LoRA (Low-Rank Adaptation)]]

> *What people say:* Storing or computing model values with fewer bits.

**What it actually means:** Representing weights, activations, or caches with lower-precision formats to reduce memory, bandwidth, or compute cost. Methods differ in calibration, granularity, data type, and whether conversion happens before, during, or after training.

**Common confusion:** Moving from one nominal bit width to another does not guarantee the same end-to-end memory or speed ratio because metadata, kernels, caches, and hardware support also matter.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Knowledge Distillation|Knowledge Distillation]]
- [[Concepts/Mixed Precision|Mixed Precision]]
- [[Concepts/Parameter|Parameter]]
- [[Concepts/QLoRA|QLoRA]]

## Taught in

- [[Lessons/19-14 Capstone 14 — Speculative-Decoding Inference Server|19/14 Capstone 14 — Speculative-Decoding Inference Server]] — Lower-precision weights to fit more model in GPU memory


%% ── my notes ── %%
