---
id: "lesson:19/11"
type: lesson
ref: 19/11
phase: 19
num: 11
title: "Capstone 11 — LLM Observability & Eval Dashboard"
lesson_type: capstone
languages:
  - TypeScript
  - Python
  - TypeScript
  - SQL
time_min: 1500
on_route: false
quiz_count: 7
code_files: 9
concepts: 7
prereqs: 0
libraries:
  - "@hono/node-server"
  - hono
aliases:
  - 19/11
  - 19-11
tags:
  - phase/19
  - type/capstone
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/11-llm-observability-dashboard/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/11-llm-observability-dashboard"
---

# 19/11 Capstone 11 — LLM Observability & Eval Dashboard

> Langfuse went open-core. Arize Phoenix published the 2026 GenAI semconv mappings. Helicone and Braintrust both doubled down on per-user cost attribution. Traceloop's OpenLLMetry became the de-facto SDK instrumentation. The production shape is ClickHouse for traces, Postgres for metadata, Next.js for UI, and a small army of eval jobs (DeepEval, RAGAS, LLM-judge) running over sampled traces. Build one self-hosted, ingest from at least four SDK families, and demonstrate catching an injected regression in under five minutes.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Capstone · **Time:** 1500 min · **Languages:** TypeScript, Python, TypeScript, SQL · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/11-llm-observability-dashboard/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/11-llm-observability-dashboard) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/11-llm-observability-dashboard) · code: main.py, ts/src/index.ts, ts/src/pricing.ts, ts/src/rollup.ts, ts/src/server.ts, ts/src/spans.ts … · quiz: 7 questions  
**Libraries:** [[Libraries/@hono-node-server (typescript)|@hono/node-server]], [[Libraries/hono (typescript)|hono]]  

## Prerequisites

Stated upstream: `Phase 11 (LLM engineering), Phase 13 (tools), Phase 17 (infrastructure), Phase 18 (safety)`

- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM engineering ·  medium confidence
- Whole phase: [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] — tools ·  medium confidence
- Whole phase: [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] — infrastructure ·  medium confidence
- Whole phase: [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] — safety ·  medium confidence

## Concepts taught

- [[Concepts/GenAI semconv|GenAI semconv]] `lesson term` — 2025 OpenTelemetry spec for LLM span attributes (system, model, tokens)
- Tail sampling `lesson term` — Collector decides to keep or drop a trace after it completes (can peek errors)
- PSI `lesson term` — Drift metric comparing two distributions; > 0.2 typically signals meaningful drift
- LLM-judge `lesson term` — An LLM scoring another LLM's output on a rubric (faithfulness, toxicity, PII)
- Tail-sampling policy `lesson term` — Rule that decides which traces to persist vs drop; errored + sample-rate
- Eval span `lesson term` — Child span carrying an eval score linked to the original LLM call span
- Cost per user `lesson term` — Dollar cost attributed to a user_id over a window; key product metric

## Ships

- [[Artifacts/19-11 llm-observability|llm-observability]] `skill` — Build a self-hosted LLM observability dashboard that ingests OpenTelemetry GenAI spans, runs evals, and catches injected regressions in under five minutes.

## Further reading

- Braintrust ([link](https://www.braintrust.dev)) — alternate eval-first platform
- ClickHouse documentation ([link](https://clickhouse.com/docs)) — columnar span store
- [[Resources/Arize Phoenix|Arize Phoenix]] ([link](https://github.com/Arize-ai/phoenix)) — alternate reference with strong drift support ·  also cited by 1 other lesson
- DeepEval ([link](https://github.com/confident-ai/deepeval)) — evaluator library
- Langfuse ([link](https://github.com/langfuse/langfuse)) — the reference open-core observability platform
- OpenLLMetry (Traceloop) ([link](https://github.com/traceloop/openllmetry)) — auto-instrumentation SDK family
- [[Resources/Helicone|Helicone]] ([link](https://www.helicone.ai)) — alternate hosted observability ·  also cited by 1 other lesson
- [[Resources/OpenTelemetry — GenAI semconv|OpenTelemetry — GenAI semconv]] ([link](https://opentelemetry.io/docs/specs/semconv/gen-ai/)) — the ingest schema ·  also cited by 9 other lessons


%% ── my notes ── %%
