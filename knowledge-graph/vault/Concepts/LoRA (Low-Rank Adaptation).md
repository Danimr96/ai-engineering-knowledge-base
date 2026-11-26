---
id: "concept:lora-low-rank-adaptation"
type: concept
name: LoRA (Low-Rank Adaptation)
canonical: true
category: "Math & training"
taught_in: 3
community: 48
tags:
  - concept/glossary
  - category/math-and-training
  - community/48
source: ai-engineering-from-scratch/glossary/terms.md
---

# LoRA (Low-Rank Adaptation)

**Community:** [[Communities/48 Fine-tuning · QLoRA · LoRA (Low-Rank Adaptation)|48 Fine-tuning · QLoRA · LoRA (Low-Rank Adaptation)]]

> *What people say:* Parameter-efficient fine-tuning.

**What it actually means:** A method that keeps base weights frozen and learns low-rank update matrices for selected layers. It reduces the number of trainable parameters and can lower training memory relative to full-parameter fine-tuning.

**Common confusion:** Actual memory and speed savings depend on rank, target modules, optimizer state, activation memory, quantization, and implementation.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Fine-tuning|Fine-tuning]]
- [[Concepts/Parameter|Parameter]]
- [[Concepts/QLoRA|QLoRA]]

## Taught in

- [[Lessons/04-11 Stable Diffusion — Architecture & Fine-Tuning|04/11 Stable Diffusion — Architecture & Fine-Tuning]] `alias` — Small rank-decomposition matrices that fine-tune attention layers without touching base weights
- [[Lessons/08-08 ControlNet, LoRA & Conditioning|08/08 ControlNet, LoRA & Conditioning]] `alias` — W + B @ A, r << d; 100x fewer params than a full fine-tune.
- [[Lessons/11-08 Fine-Tuning with LoRA & QLoRA|11/08 Fine-Tuning with LoRA & QLoRA]] — Low-Rank Adaptation: freeze base weights, train two small matrices A and B whose product approximates the full weight update

## Sources

- [[Resources/LoRA paper|LoRA paper]] ([link](https://arxiv.org/abs/2106.09685))


%% ── my notes ── %%
