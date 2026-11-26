---
id: "concept:adapter"
type: concept
name: Adapter
canonical: false
taught_in: 2
community: 2
tags:
  - concept/lesson-term
  - community/02
source: ai-engineering-from-scratch/phases/11-llm-engineering/08-fine-tuning-lora/docs/en.md
---

# Adapter

**Community:** [[Communities/02 Bucket · Causal mask · Manifest|02 Bucket · Causal mask · Manifest]]

> *What people say:* "The small trained part"

**What it actually means:** The LoRA A and B matrices saved as a separate file (10-100MB), loadable on top of any copy of the base model

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/11-08 Fine-Tuning with LoRA & QLoRA|11/08 Fine-Tuning with LoRA & QLoRA]]
- [[Lessons/19-49 Language Model Evaluation Harness|19/49 Language Model Evaluation Harness]] — Object with a generate(prompts) -> list[str] method; the only model-specific code


%% ── my notes ── %%
