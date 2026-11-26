---
id: "concept:context-compression"
type: concept
name: Context Compression
canonical: true
category: "Prompting & context"
taught_in: 0
community: 57
tags:
  - concept/glossary
  - category/prompting-and-context
  - community/57
source: ai-engineering-from-scratch/glossary/terms.md
---

# Context Compression

**Community:** [[Communities/57 Context Engineering · Context Window · Token Budget|57 Context Engineering · Context Window · Token Budget]]

**What it actually means:** Reducing the token footprint of source material while attempting to preserve the information required for a later model decision.

**Why it matters:** Compression can make long tasks fit within budget, but every omitted detail creates a risk that the model loses evidence, constraints, or unresolved state.

**In practice:** Preserve authoritative facts and identifiers verbatim, summarize redundant history, attach source pointers, and test the compressed context on representative tasks.

**Common confusion:** Compression is lossy unless it retains the full original. A shorter summary is not automatically an equivalent context.

**Category:** [[Categories/Prompting & context|Prompting & context]]

## Related concepts

- [[Concepts/Context Engineering|Context Engineering]]
- [[Concepts/Handoff|Handoff]]
- [[Concepts/Progressive Disclosure|Progressive Disclosure]]
- [[Concepts/Token Budget|Token Budget]]

## Sources

- LLMLingua ([link](https://arxiv.org/abs/2310.05736))


%% ── my notes ── %%
