---
id: "concept:lost-in-the-middle"
type: concept
name: Lost in the Middle
canonical: true
category: "Prompting & context"
taught_in: 3
community: 57
tags:
  - concept/glossary
  - category/prompting-and-context
  - community/57
source: ai-engineering-from-scratch/glossary/terms.md
---

# Lost in the Middle

**Community:** [[Communities/57 Context Engineering · Context Window · Token Budget|57 Context Engineering · Context Window · Token Budget]]

**What it actually means:** A long-context failure pattern in which model performance changes with evidence position and can degrade when relevant information sits between the beginning and end.

**Why it matters:** Fitting evidence inside the context window does not guarantee that the model will use every position with equal reliability.

**In practice:** Test several evidence positions, reduce distractors, place decision-critical constraints where they remain salient, and verify answers against the source.

**Common confusion:** It is an observed behavior pattern, not a fixed law that affects every model, task, or position identically.

**Category:** [[Categories/Prompting & context|Prompting & context]]

## Related concepts

- [[Concepts/Context Engineering|Context Engineering]]
- [[Concepts/Context Window|Context Window]]
- [[Concepts/Eval Set|Eval Set]]
- [[Concepts/Grounding|Grounding]]

## Taught in

- [[Lessons/05-28 Long-Context Evaluation — NIAH, RULER, LongBench, MRCR|05/28 Long-Context Evaluation — NIAH, RULER, LongBench, MRCR]] — Models under-attend to content in the middle of long inputs.
- [[Lessons/10-16 Differential Attention (V2)|10/16 Differential Attention (V2)]] — Empirical phenomenon where retrieval accuracy dips for documents in the middle of a long context — DIFF attention reduces this
- [[Lessons/11-05 Context Engineering- Windows, Budgets, Memory, and Retrieval|11/05 Context Engineering: Windows, Budgets, Memory, and Retrieval]] — Empirical finding that LLMs attend better to the beginning and end of context, with 10-20% accuracy drop for information placed in the middle

## Sources

- Lost in the Middle ([link](https://aclanthology.org/2024.tacl-1.9/))


%% ── my notes ── %%
