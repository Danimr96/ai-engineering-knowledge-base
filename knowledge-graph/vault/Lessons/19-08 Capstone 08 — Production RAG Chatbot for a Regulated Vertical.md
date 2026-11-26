---
id: "lesson:19/08"
type: lesson
ref: 19/08
phase: 19
num: 8
title: "Capstone 08 — Production RAG Chatbot for a Regulated Vertical"
lesson_type: capstone
languages:
  - Python
  - TypeScript
time_min: 1800
on_route: false
quiz_count: 7
code_files: 9
concepts: 7
prereqs: 0
community: 81
libraries:
  - hono
  - zod
aliases:
  - 19/08
  - 19-08
tags:
  - phase/19
  - type/capstone
  - community/81
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/08-production-rag-chatbot/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/08-production-rag-chatbot"
---

# 19/08 Capstone 08 — Production RAG Chatbot for a Regulated Vertical

> Harvey, Glean, Mendable, and LlamaCloud all run the same production shape in 2026. Ingest with docling or Unstructured and ColPali for visuals. Hybrid search. Re-rank with bge-reranker-v2-gemma. Synthesize with Claude Sonnet 4.7 using prompt caching at 60-80% hit rate. Guard with Llama Guard 4 and NeMo Guardrails. Watch with Langfuse and Phoenix. Grade with RAGAS on a 200-question golden set. Build one in a regulated domain (legal, clinical, insurance), and the capstone is passing the golden set, the red team, and the drift dashboard.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Capstone · **Time:** 1800 min · **Languages:** Python, TypeScript · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/08-production-rag-chatbot/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/08-production-rag-chatbot) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/08-production-rag-chatbot) · code: main.py, ts/src/index.ts, ts/src/server.ts, ts/src/session.ts, ts/src/stream.ts, ts/src/types.ts … · quiz: 7 questions  
**Community:** [[Communities/81 Citation faithfulness · RAGAS|81 Citation faithfulness · RAGAS]] · **Libraries:** [[Libraries/hono (typescript)|hono]], [[Libraries/zod (typescript)|zod]]  

## Prerequisites

Stated upstream: `Phase 5 (NLP), Phase 7 (transformers), Phase 11 (LLM engineering), Phase 12 (multimodal), Phase 17 (infrastructure), Phase 18 (safety)`

- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM engineering ·  medium confidence
- Whole phase: [[Phases/12 Multimodal AI|Phase 12: Multimodal AI]] — multimodal ·  medium confidence
- Whole phase: [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] — infrastructure ·  medium confidence
- Whole phase: [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] — safety ·  medium confidence
- Whole phase: [[Phases/05 NLP, Foundations to Advanced|Phase 5: NLP, Foundations to Advanced]] — NLP ·  medium confidence
- Whole phase: [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] — transformers ·  medium confidence

## Concepts taught

- [[Concepts/Prompt Cache|Prompt Cache]] (as *Prompt caching*) `glossary` — Claude/OpenAI feature: cached prefix tokens discounted 60-90% on hit
- [[Concepts/RAGAS|RAGAS]] `lesson term` — Automated scoring of faithfulness, answer relevance, context precision
- Golden set `lesson term` — 200+ expert-labeled Q/A with citations; the ground truth
- Jurisdiction tag `lesson term` — GDPR/HIPAA/SOC2 scope attached to chunks; enforced by retrieval filter
- [[Concepts/Citation faithfulness|Citation faithfulness]] `lesson term` — Fraction of claims backed by retrievable source spans
- [[Concepts/Drift|Drift]] `lesson term` — Weekly change in nDCG or citation score; alert threshold 5%
- [[Concepts/Red Teaming|Red Teaming]] (as *Red team*) `glossary` — Pre-release jailbreak, PII extraction, off-domain probes

## Ships

- [[Artifacts/19-08 production-rag|production-rag]] `skill` — Deploy a regulated-domain RAG chatbot with role + jurisdiction filtering, prompt caching, guardrails, and live drift monitoring.

## Further reading

- [[Resources/Anthropic Prompt Caching Guide|Anthropic Prompt Caching Guide]] ([link](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)) — the cost-lever reference ·  also cited by 3 other lessons
- LlamaCloud Parse + Index ([link](https://docs.cloud.llamaindex.ai/llamaparse/getting_started)) — managed ingestion
- [[Resources/NeMo Guardrails v0.12|NeMo Guardrails v0.12]] ([link](https://docs.nvidia.com/nemo-guardrails/)) — policy rail framework ·  also cited by 1 other lesson
- [[Resources/RAGAS 0.2 documentation|RAGAS 0.2 documentation]] ([link](https://docs.ragas.io/)) — the canonical RAG eval framework ·  also cited by 2 other lessons
- [[Resources/Arize Phoenix|Arize Phoenix]] ([link](https://github.com/Arize-ai/phoenix)) — reference drift observability ·  also cited by 1 other lesson
- Glean enterprise search ([link](https://www.glean.com)) — reference RAG at enterprise scale
- Harvey AI ([link](https://www.harvey.ai)) — reference legal production stack
- [[Resources/Meta — Llama Guard 4 model card|Meta — Llama Guard 4 model card]] ([link](https://www.llama.com/docs/model-cards-and-prompt-formats/llama-guard-4/)) — 2026 safety classifier ·  also cited by 2 other lessons
- Mendable documentation ([link](https://mendable.ai)) — developer-docs RAG reference


%% ── my notes ── %%
