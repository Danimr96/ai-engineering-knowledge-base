---
id: "lesson:19/02"
type: lesson
ref: 19/02
phase: 19
num: 2
title: "Capstone 02 — RAG over Codebase (Cross-Repo Semantic Search)"
lesson_type: capstone
languages:
  - Python
  - TypeScript
time_min: 1800
on_route: false
quiz_count: 7
code_files: 10
concepts: 7
prereqs: 0
community: 81
libraries:
  - hono
  - zod
aliases:
  - 19/02
  - 19-02
tags:
  - phase/19
  - type/capstone
  - community/81
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/02-rag-over-codebase/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/02-rag-over-codebase"
---

# 19/02 Capstone 02 — RAG over Codebase (Cross-Repo Semantic Search)

> Every serious engineering org in 2026 runs an internal code search that understands meaning, not just strings. Sourcegraph Amp, Cursor's codebase answers, Augment's enterprise graph, Aider's repomap, Pinterest's internal MCP — same shape. Ingest many repos, parse with tree-sitter, embed function- and class-level chunks, hybrid-search, re-rank, answer with citations. This capstone asks you to build one that handles 2M lines of code across 10 repos and survives incremental re-indexing on every git push.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Capstone · **Time:** 1800 min · **Languages:** Python, TypeScript · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/02-rag-over-codebase/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/02-rag-over-codebase) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/02-rag-over-codebase) · code: main.py, ts/src/corpus.ts, ts/src/index.ts, ts/src/index_store.ts, ts/src/retrieval.ts, ts/src/server.ts … · quiz: 7 questions  
**Community:** [[Communities/81 Citation faithfulness · RAGAS|81 Citation faithfulness · RAGAS]] · **Libraries:** [[Libraries/hono (typescript)|hono]], [[Libraries/zod (typescript)|zod]]  

## Prerequisites

Stated upstream: `Phase 5 (NLP foundations), Phase 7 (transformers), Phase 11 (LLM engineering), Phase 13 (tools), Phase 17 (infrastructure)`

- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM engineering ·  medium confidence
- Whole phase: [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] — tools ·  medium confidence
- Whole phase: [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] — infrastructure ·  medium confidence
- Whole phase: [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] — NLP foundations ·  medium confidence
- Whole phase: [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] — transformers ·  medium confidence

## Concepts taught

- AST-aware chunking `lesson term` — Cutting code at tree-sitter node boundaries instead of fixed token windows
- [[Concepts/Hybrid search|Hybrid search]] `lesson term` — Run BM25 and vector search in parallel, merge top-k, rerank
- Cross-encoder rerank `lesson term` — Model that scores each (query, candidate) pair together, more accurate than cosine
- [[Concepts/Prompt Cache|Prompt Cache]] (as *Prompt caching*) `glossary` — 2026 Claude / OpenAI feature that discounts repeat prefix tokens up to 90%
- Symbol graph `lesson term` — Edges for imports, calls, inheritance across files and repos
- [[Concepts/Citation faithfulness|Citation faithfulness]] `lesson term` — Fraction of claims a user can verify by clicking the anchor and reading the referenced span
- Incremental re-index `lesson term` — Wall-clock from git push to the changed symbols being queryable

## Ships

- [[Artifacts/19-02 codebase-rag|codebase-rag]] `skill` — Build a cross-repo semantic search system with AST-aware chunking, hybrid retrieval, incremental re-index, and cited answers.

## Further reading

- Aider repo-map ([link](https://aider.chat/docs/repomap.html)) — tree-sitter ranked repo view
- Sourcegraph Amp ([link](https://ampcode.com)) — production cross-repo code intelligence
- Augment Code enterprise graph ([link](https://www.augmentcode.com)) — commercial symbol-graph RAG
- Cohere rerank-3 ([link](https://docs.cohere.com/reference/rerank)) — cross-encoder reference
- Voyage AI code embeddings ([link](https://docs.voyageai.com/docs/embeddings)) — Voyage-code-3 details
- [[Resources/Pinterest MCP internal search|Pinterest MCP internal search]] ([link](https://medium.com/pinterest-engineering)) — internal-platform reference ·  also cited by 1 other lesson
- Qdrant hybrid search docs ([link](https://qdrant.tech/documentation/concepts/hybrid-queries/)) — reference implementation
- Sourcegraph Cody RAG architecture ([link](https://sourcegraph.com/blog/how-cody-understands-your-codebase)) — the reference deep-dive for this capstone


%% ── my notes ── %%
