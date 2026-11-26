---
id: "concept:maximum-marginal-relevance-mmr"
type: concept
name: Maximum Marginal Relevance (MMR)
canonical: true
category: "Retrieval & generation"
taught_in: 0
community: 55
tags:
  - concept/glossary
  - category/retrieval-and-generation
  - community/55
source: ai-engineering-from-scratch/glossary/terms.md
---

# Maximum Marginal Relevance (MMR)

**Community:** [[Communities/55 Grounding · RAG (Retrieval-Augmented Generation) · Chunking|55 Grounding · RAG (Retrieval-Augmented Generation) · Chunking]]

**What it actually means:** A selection rule that balances relevance to the query with novelty relative to items already selected.

**Why it matters:** It can reduce redundant chunks so a limited context budget covers more distinct evidence.

**In practice:** Retrieve a candidate pool, select the next item using a documented relevance-diversity weight, and evaluate both answer quality and source coverage.

**Common confusion:** MMR diversifies an existing candidate set; it does not retrieve missing evidence or prove that selected passages are correct.

**Category:** [[Categories/Retrieval & generation|Retrieval & generation]]

## Related concepts

- [[Concepts/Chunking|Chunking]]
- [[Concepts/Grounding|Grounding]]
- [[Concepts/RAG (Retrieval-Augmented Generation)|RAG (Retrieval-Augmented Generation)]]
- [[Concepts/Reranker|Reranker]]

## Sources

- The Use of MMR, Diversity-Based Reranking for Reordering Documents and Producing Summaries ([link](https://www.cs.cmu.edu/~jgc/publication/MMR_DiversityBased_Reranking_SIGIR_1998.pdf))


%% ── my notes ── %%
