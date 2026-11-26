---
id: "concept:context-engineering"
type: concept
name: Context Engineering
canonical: true
category: "Prompting & context"
taught_in: 1
community: 57
tags:
  - concept/glossary
  - category/prompting-and-context
  - community/57
source: ai-engineering-from-scratch/glossary/terms.md
---

# Context Engineering

**Community:** [[Communities/57 Context Engineering · Context Window · Token Budget|57 Context Engineering · Context Window · Token Budget]]

**What it actually means:** Designing the full information environment supplied to a model at each step, including instructions, selected files, retrieved evidence, tool results, examples, state, and output constraints.

**Why it matters:** Model performance often fails because relevant evidence is missing, stale, badly ordered, or overwhelmed by noise.

**In practice:** Build a compact task packet with the goal, repository rules, relevant interfaces, recent tool output, and unresolved decisions, then update it as state changes.

**Common confusion:** Prompt engineering focuses on instruction wording. Context engineering also decides what evidence and state enter the model's working context.

**Category:** [[Categories/Prompting & context|Prompting & context]]

## Related concepts

- [[Concepts/Agent Memory|Agent Memory]]
- [[Concepts/Agent State|Agent State]]
- [[Concepts/Context Compression|Context Compression]]
- [[Concepts/Context Window|Context Window]]
- [[Concepts/Data Minimization|Data Minimization]]
- [[Concepts/Lost in the Middle|Lost in the Middle]]
- [[Concepts/Progressive Disclosure|Progressive Disclosure]]
- [[Concepts/Prompt Engineering|Prompt Engineering]]
- [[Concepts/Repository Map|Repository Map]]
- [[Concepts/System Prompt|System Prompt]]
- [[Concepts/Token Budget|Token Budget]]

## Taught in

- [[Lessons/11-05 Context Engineering- Windows, Budgets, Memory, and Retrieval|11/05 Context Engineering: Windows, Budgets, Memory, and Retrieval]] — The discipline of deciding what goes into the context window, in what order, and at what priority -- encompasses retrieval, compression, tool selection, and memory management


%% ── my notes ── %%
