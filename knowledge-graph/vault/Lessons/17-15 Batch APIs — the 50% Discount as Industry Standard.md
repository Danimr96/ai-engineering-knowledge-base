---
id: "lesson:17/15"
type: lesson
ref: 17/15
phase: 17
num: 15
title: "Batch APIs — the 50% Discount as Industry Standard"
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 6
code_files: 2
concepts: 8
prereqs: 1
aliases:
  - 17/15
  - 17-15
tags:
  - phase/17
  - type/learn
  - stdlib-only
source: ai-engineering-from-scratch/phases/17-infrastructure-and-production/15-batch-apis/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/15-batch-apis"
---

# 17/15 Batch APIs — the 50% Discount as Industry Standard

> Every major provider ships an async batch API with a 50% discount and ~24-hour turnaround. OpenAI, Anthropic, Google, and most of the inference platforms (Fireworks batch tier, Together batch) implement the same pattern. Stack batch with prompt caching and overnight pipelines drop to ~10% of synchronous-uncached cost. The rule is brutally simple: if it is not interactive, it belongs on batch. Content generation pipelines, document classification, data extraction, report generation, bulk labeling, catalog tagging — anything tolerant of 24-hour latency is money left on the table until it moves to batch. The 2026 production pattern is to triage every new LLM workload into three lanes: interactive (synchronous with caching), semi-interactive (async queue with fallback), batch (overnight, cached input stacked). Workloads that pretend to be interactive but tolerate minutes of latency waste most.

**Phase:** [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/17-infrastructure-and-production/15-batch-apis/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/17-infrastructure-and-production/15-batch-apis) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/17-infrastructure-and-production/15-batch-apis) · code: main.py, main.ts · quiz: 6 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 17 · 14 (Prompt & Semantic Caching)`

- [[Lessons/17-14 Prompt Caching and Semantic Caching Economics|17/14 Prompt Caching and Semantic Caching Economics]] — Prompt & Semantic Caching

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/17-04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill|17/04 Serving Engine Internals — PagedAttention, Continuous Batching, Chunked Prefill]], [[Lessons/17-06 Prefix-Cache Serving — RadixAttention and KV Reuse|17/06 Prefix-Cache Serving — RadixAttention and KV Reuse]]
- depth 3: [[Lessons/17-01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI|17/01 Managed LLM Platforms — Bedrock, Vertex AI, Azure OpenAI]]

## Concepts taught

- [[Concepts/Batch API|Batch API]] `lesson term` — 50% off with 24h turnaround
- JSONL `lesson term` — One JSON request per line; OpenAI/Anthropic standard
- Message Batches `lesson term` — Anthropic's batch API product name
- Batch prediction `lesson term` — Vertex AI's batch API product
- Turnaround SLA `lesson term` — Guarantee, not typical; typical is 2-6h
- Workload triage `lesson term` — Interactive / semi / batch routing decision
- Output schema `lesson term` — Per-provider JSONL layout; not portable
- Stacked discount `lesson term` — ~10% of uncached sync bill when both apply

## Ships

- [[Artifacts/17-15 batch-triager|batch-triager]] `skill` — Triage LLM workloads into interactive / semi-interactive / batch lanes, compute stacked discount (batch + cache) savings, and flag mis-triaged workloads.

## Further reading

- Vertex AI Batch Prediction ([link](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/batch-prediction-gemini)) — Gemini batch semantics.
- Anthropic Message Batches ([link](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing)) — batch format and `cache_control` interaction.
- Finout — OpenAI vs Anthropic API Pricing 2026 ([link](https://www.finout.io/blog/openai-vs-anthropic-api-pricing-comparison))
- [[Resources/OpenAI Batch API|OpenAI Batch API]] ([link](https://platform.openai.com/docs/guides/batch)) — JSONL format and `/v1/batches` semantics. ·  also cited by 1 other lesson
- Zen Van Riel — LLM API Cost Comparison 2026 ([link](https://zenvanriel.com/ai-engineer-blog/llm-api-cost-comparison-2026/))


%% ── my notes ── %%
