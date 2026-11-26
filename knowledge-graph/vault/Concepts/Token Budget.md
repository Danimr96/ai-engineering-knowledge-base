---
id: "concept:token-budget"
type: concept
name: Token Budget
canonical: true
category: "Prompting & context"
taught_in: 2
community: 57
tags:
  - concept/glossary
  - category/prompting-and-context
  - community/57
source: ai-engineering-from-scratch/glossary/terms.md
---

# Token Budget

**Community:** [[Communities/57 Context Engineering · Context Window · Token Budget|57 Context Engineering · Context Window · Token Budget]]

**What it actually means:** An explicit allocation of token capacity across instructions, evidence, history, tool results, reasoning or working space, and output.

**Why it matters:** Every included token competes for context capacity, latency, and cost. Budgeting forces you to preserve high-value evidence first.

**In practice:** Reserve output capacity, cap retrieved chunks, summarize old tool results into state, and stop or compact before the model limit is reached.

**Common confusion:** A token budget is a planning constraint. It is not the same as the model's maximum context window.

**Category:** [[Categories/Prompting & context|Prompting & context]]

## Related concepts

- [[Concepts/Context Compression|Context Compression]]
- [[Concepts/Context Engineering|Context Engineering]]
- [[Concepts/Context Window|Context Window]]
- [[Concepts/Cost per Successful Task|Cost per Successful Task]]
- [[Concepts/Progressive Disclosure|Progressive Disclosure]]
- [[Concepts/Skill Catalog|Skill Catalog]]
- [[Concepts/Termination Condition|Termination Condition]]
- [[Concepts/Time to First Token (TTFT)|Time to First Token (TTFT)]]
- [[Concepts/Token|Token]]

## Taught in

- [[Lessons/11-05 Context Engineering- Windows, Budgets, Memory, and Retrieval|11/05 Context Engineering: Windows, Budgets, Memory, and Retrieval]] — An explicit allocation of context window capacity across components (system prompt, tools, history, retrieval, generation) with per-component limits
- [[Lessons/12-08 LLaVA-OneVision- Single-Image, Multi-Image, Video in One Model|12/08 LLaVA-OneVision: Single-Image, Multi-Image, Video in One Model]] — Total visual tokens the LLM sees per training / inference sample, typically 3000-4000


%% ── my notes ── %%
