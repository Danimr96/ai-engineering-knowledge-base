---
id: "concept:fine-tuning"
type: concept
name: Fine-tuning
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

# Fine-tuning

**Community:** [[Communities/48 Fine-tuning · QLoRA · LoRA (Low-Rank Adaptation)|48 Fine-tuning · QLoRA · LoRA (Low-Rank Adaptation)]]

> *What people say:* Training a model on your data.

**What it actually means:** Continuing training from pretrained parameters on a narrower dataset or objective. Depending on the method, you may update all parameters, selected parameters, or added adapter parameters.

**Why it matters:** Fine-tuning can adapt behavior, style, format, or task performance, but it is not a dependable replacement for retrieval when facts must stay current or traceable.

**Common confusion:** Fine-tuning can influence encoded knowledge, but it does not simply append records to a searchable database inside the model.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Knowledge Distillation|Knowledge Distillation]]
- [[Concepts/LoRA (Low-Rank Adaptation)|LoRA (Low-Rank Adaptation)]]
- [[Concepts/QLoRA|QLoRA]]
- [[Concepts/RAG (Retrieval-Augmented Generation)|RAG (Retrieval-Augmented Generation)]]
- [[Concepts/SFT (Supervised Fine-Tuning)|SFT (Supervised Fine-Tuning)]]
- [[Concepts/Transfer Learning|Transfer Learning]]

## Taught in

- [[Lessons/04-05 Transfer Learning & Fine-Tuning|04/05 Transfer Learning & Fine-Tuning]] — All parameters trainable, usually with much smaller LR than scratch training
- [[Lessons/07-06 BERT — Masked Language Modeling|07/06 BERT — Masked Language Modeling]] — Keep the encoder mostly frozen; train a small head on top for the downstream task.
- [[Lessons/11-08 Fine-Tuning with LoRA & QLoRA|11/08 Fine-Tuning with LoRA & QLoRA]]


%% ── my notes ── %%
