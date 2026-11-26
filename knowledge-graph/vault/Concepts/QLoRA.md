---
id: "concept:qlora"
type: concept
name: QLoRA
canonical: true
category: "Math & training"
taught_in: 1
community: 48
tags:
  - concept/glossary
  - category/math-and-training
  - community/48
source: ai-engineering-from-scratch/glossary/terms.md
---

# QLoRA

**Community:** [[Communities/48 Fine-tuning · QLoRA · LoRA (Low-Rank Adaptation)|48 Fine-tuning · QLoRA · LoRA (Low-Rank Adaptation)]]

> *What people say:* LoRA with a quantized base model.

**What it actually means:** A parameter-efficient fine-tuning method that keeps a pretrained base model frozen in a low-bit quantized representation while training LoRA adapters with higher-precision computation where needed.

**Why it matters:** It can reduce the memory needed to adapt large models, but savings and quality depend on model, rank, optimizer, sequence length, hardware, and implementation.

**Common confusion:** QLoRA does not guarantee a particular memory footprint or a fixed quality gap from full fine-tuning.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Fine-tuning|Fine-tuning]]
- [[Concepts/LoRA (Low-Rank Adaptation)|LoRA (Low-Rank Adaptation)]]
- [[Concepts/Quantization|Quantization]]

## Taught in

- [[Lessons/11-08 Fine-Tuning with LoRA & QLoRA|11/08 Fine-Tuning with LoRA & QLoRA]] — Quantized LoRA: load the base model in 4-bit NF4, train LoRA adapters in fp16 on top, enabling 7B fine-tuning in 6GB VRAM

## Sources

- QLoRA paper ([link](https://arxiv.org/abs/2305.14314))


%% ── my notes ── %%
