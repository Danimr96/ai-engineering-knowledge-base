---
id: "concept:sft-supervised-fine-tuning"
type: concept
name: SFT (Supervised Fine-Tuning)
canonical: true
category: "Math & training"
taught_in: 2
community: 66
tags:
  - concept/glossary
  - category/math-and-training
  - community/66
source: ai-engineering-from-scratch/glossary/terms.md
---

# SFT (Supervised Fine-Tuning)

**Community:** [[Communities/66 Alignment · DPO (Direct Preference Optimization) · RLHF (Reinforcement Learning from Human Feedback)|66 Alignment · DPO (Direct Preference Optimization) · RLHF (Reinforcement Learning from Human Feedback)]]

> *What people say:* Training on example inputs and desired outputs.

**What it actually means:** Fine-tuning a pretrained model on paired inputs and desired responses so it learns the demonstrated behavior under the training distribution.

**Common confusion:** SFT can adapt many behaviors beyond chat, and example quality determines what behavior is reinforced.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/DPO (Direct Preference Optimization)|DPO (Direct Preference Optimization)]]
- [[Concepts/Fine-tuning|Fine-tuning]]
- [[Concepts/Instruction Following|Instruction Following]]
- [[Concepts/RLHF (Reinforcement Learning from Human Feedback)|RLHF (Reinforcement Learning from Human Feedback)]]
- [[Concepts/Transfer Learning|Transfer Learning]]

## Taught in

- [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]] `alias` — Supervised Fine-Tuning: continuing training on (instruction, response) pairs with loss computed only on response tokens
- [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]] `alias` — Stage 1: cross-entropy fine-tune on prompt-response pairs


%% ── my notes ── %%
