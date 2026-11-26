---
id: "concept:grounding"
type: concept
name: Grounding
canonical: true
category: "Retrieval & generation"
taught_in: 2
community: 55
tags:
  - concept/glossary
  - category/retrieval-and-generation
  - community/55
source: ai-engineering-from-scratch/glossary/terms.md
---

# Grounding

**Community:** [[Communities/55 Grounding · RAG (Retrieval-Augmented Generation) · Chunking|55 Grounding · RAG (Retrieval-Augmented Generation) · Chunking]]

**What it actually means:** Connecting a generated answer or action to evidence, state, or observations that the system can identify and check.

**Why it matters:** Grounding gives the system a basis beyond unconstrained generation and makes unsupported claims easier to detect.

**In practice:** Retrieve a policy section, require the answer to cite it, and reject claims that the cited passage does not support.

**Common confusion:** Adding documents to a prompt creates an opportunity for grounding. It does not guarantee the model will use them correctly.

**Category:** [[Categories/Retrieval & generation|Retrieval & generation]]

## Related concepts

- [[Concepts/Chunking|Chunking]]
- [[Concepts/Content Provenance|Content Provenance]]
- [[Concepts/Data Provenance|Data Provenance]]
- [[Concepts/Hallucination|Hallucination]]
- [[Concepts/Lost in the Middle|Lost in the Middle]]
- [[Concepts/Maximum Marginal Relevance (MMR)|Maximum Marginal Relevance (MMR)]]
- [[Concepts/Modality Alignment|Modality Alignment]]
- [[Concepts/RAG (Retrieval-Augmented Generation)|RAG (Retrieval-Augmented Generation)]]
- [[Concepts/ReAct|ReAct]]
- [[Concepts/Reranker|Reranker]]
- [[Concepts/Semantic Cache|Semantic Cache]]
- [[Concepts/Verification Gate|Verification Gate]]
- [[Concepts/Visual Grounding|Visual Grounding]]

## Taught in

- [[Lessons/11-06 RAG (Retrieval-Augmented Generation)|11/06 RAG (Retrieval-Augmented Generation)]]
- [[Lessons/12-09 Qwen-VL Family and Dynamic-FPS Video|12/09 Qwen-VL Family and Dynamic-FPS Video]] — Outputting bounding-box coordinates as text tokens; used since Qwen-VL v1


%% ── my notes ── %%
