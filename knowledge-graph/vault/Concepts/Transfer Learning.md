---
id: "concept:transfer-learning"
type: concept
name: Transfer Learning
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

# Transfer Learning

**Community:** [[Communities/48 Fine-tuning · QLoRA · LoRA (Low-Rank Adaptation)|48 Fine-tuning · QLoRA · LoRA (Low-Rank Adaptation)]]

> *What people say:* Reusing a pretrained model for a new task.

**What it actually means:** Starting from representations or parameters learned on one data distribution or objective and adapting them for another. The transferable components and update strategy depend on architecture and task.

**Common confusion:** Transfer is not limited to later layers, and successful transfer is not guaranteed when source and target tasks differ sharply.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Feature|Feature]]
- [[Concepts/Fine-tuning|Fine-tuning]]
- [[Concepts/SFT (Supervised Fine-Tuning)|SFT (Supervised Fine-Tuning)]]
- [[Concepts/Zero-Shot|Zero-Shot]]

## Taught in

- [[Lessons/04-03 CNNs — LeNet to ResNet|04/03 CNNs — LeNet to ResNet]] — Loading a backbone trained on ImageNet and fine-tuning only the head on your task


%% ── my notes ── %%
