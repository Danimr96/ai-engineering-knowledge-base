---
id: "concept:few-shot"
type: concept
name: Few-Shot
canonical: true
category: "Prompting & context"
taught_in: 4
community: 42
tags:
  - concept/glossary
  - category/prompting-and-context
  - community/42
source: ai-engineering-from-scratch/glossary/terms.md
---

# Few-Shot

**Community:** [[Communities/42 Few-Shot · Prompt Engineering · In-Context Learning|42 Few-Shot · Prompt Engineering · In-Context Learning]]

> *What people say:* Give the model a few examples in the prompt.

**What it actually means:** In-context learning that includes a small set of demonstrations before the target input so the model can infer the desired task, format, or decision boundary.

**Why it matters:** Example quality and coverage matter more than a universal example count. Poor or contradictory demonstrations can reduce reliability.

**Category:** [[Categories/Prompting & context|Prompting & context]]

## Related concepts

- [[Concepts/Context Window|Context Window]]
- [[Concepts/In-Context Learning|In-Context Learning]]
- [[Concepts/Prompt Engineering|Prompt Engineering]]
- [[Concepts/Prompt Sensitivity|Prompt Sensitivity]]
- [[Concepts/Zero-Shot|Zero-Shot]]

## Taught in

- [[Lessons/05-18 Multilingual NLP|05/18 Multilingual NLP]] — 100-500 target-language examples used for fine-tuning.
- [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]] `alias` — Including 2-10 input/output examples in the prompt so the model learns the task pattern without any fine-tuning
- [[Lessons/11-02 Few-Shot, Chain-of-Thought, Tree-of-Thought|11/02 Few-Shot, Chain-of-Thought, Tree-of-Thought]] `alias` — Including input-output demonstrations in the prompt to anchor the model's output format and behavior
- [[Lessons/12-04 Flamingo and Gated Cross-Attention for Few-Shot VLMs|12/04 Flamingo and Gated Cross-Attention for Few-Shot VLMs]] — Give a few (image, answer) pairs in the prompt; model generalizes without finetuning


%% ── my notes ── %%
