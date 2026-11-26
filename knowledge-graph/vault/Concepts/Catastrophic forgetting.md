---
id: "concept:catastrophic-forgetting"
type: concept
name: Catastrophic forgetting
canonical: false
taught_in: 3
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/04-computer-vision/05-transfer-learning/docs/en.md
---

# Catastrophic forgetting

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "The model lost ImageNet"

**What it actually means:** A too-high LR overwrites pretrained features before the new task signal is learnt

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/04-05 Transfer Learning & Fine-Tuning|04/05 Transfer Learning & Fine-Tuning]]
- [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]] — Fine-tuning destroys pre-trained capabilities because gradient updates overwrite general knowledge with task-specific patterns
- [[Lessons/11-08 Fine-Tuning with LoRA & QLoRA|11/08 Fine-Tuning with LoRA & QLoRA]] — When updating all weights causes the model to lose previously learned capabilities


%% ── my notes ── %%
