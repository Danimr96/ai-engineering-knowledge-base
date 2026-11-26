---
id: "concept:in-context-learning"
type: concept
name: In-Context Learning
canonical: true
category: "Prompting & context"
taught_in: 0
community: 42
tags:
  - concept/glossary
  - category/prompting-and-context
  - community/42
source: ai-engineering-from-scratch/glossary/terms.md
---

# In-Context Learning

**Community:** [[Communities/42 Few-Shot · Prompt Engineering · In-Context Learning|42 Few-Shot · Prompt Engineering · In-Context Learning]]

**What it actually means:** A model adapting its behavior from instructions, examples, or patterns supplied in the current input without an ordinary parameter update.

**Why it matters:** It explains how one pretrained model can perform a new task from context while keeping its weights unchanged.

**In practice:** Place representative demonstrations before the target input, test order and formatting variants, and keep evaluation examples separate from the demonstrations.

**Common confusion:** In-context learning is temporary conditioning, not fine-tuning, durable memory, or proof that the model inferred the intended rule.

**Category:** [[Categories/Prompting & context|Prompting & context]]

## Related concepts

- [[Concepts/Context Window|Context Window]]
- [[Concepts/Few-Shot|Few-Shot]]
- [[Concepts/Prompt Engineering|Prompt Engineering]]
- [[Concepts/Zero-Shot|Zero-Shot]]

## Sources

- Language Models are Few-Shot Learners ([link](https://arxiv.org/abs/2005.14165))


%% ── my notes ── %%
