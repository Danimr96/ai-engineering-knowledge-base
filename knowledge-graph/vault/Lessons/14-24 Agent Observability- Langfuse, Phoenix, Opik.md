---
id: "lesson:14/24"
type: lesson
ref: 14/24
phase: 14
num: 24
title: "Agent Observability: Langfuse, Phoenix, Opik"
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 7
code_files: 1
concepts: 8
prereqs: 1
community: 7
aliases:
  - 14/24
  - 14-24
tags:
  - phase/14
  - type/learn
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/24-agent-observability-platforms/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/24-agent-observability-platforms"
---

# 14/24 Agent Observability: Langfuse, Phoenix, Opik

> Three open-source agent observability platforms dominate 2026. Langfuse (MIT) — 6M+ installs/month, tracing + prompt management + evals + session replay. Arize Phoenix (Elastic 2.0) — deep agent-specific evals, RAG relevancy, OpenInference auto-instrumentation. Comet Opik (Apache 2.0) — automated prompt optimization, guardrails, LLM-judge hallucination detection.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/24-agent-observability-platforms/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/24-agent-observability-platforms) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/24-agent-observability-platforms) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 23 (OTel GenAI)`

- [[Lessons/14-23 OpenTelemetry GenAI Semantic Conventions|14/23 OpenTelemetry GenAI Semantic Conventions]] — OTel GenAI

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-13 Stateful Graph Orchestration — Durable Execution and Checkpoints|14/13 Stateful Graph Orchestration — Durable Execution and Checkpoints]]
- depth 3: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-12 Anthropic's Workflow Patterns- Simple Over Complex|14/12 Anthropic's Workflow Patterns: Simple Over Complex]]

## Builds on this

- [[Lessons/14-23 OpenTelemetry GenAI Semantic Conventions|14/23 OpenTelemetry GenAI Semantic Conventions]]
- [[Lessons/14-26 Failure Modes- Why Agents Break|14/26 Failure Modes: Why Agents Break]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- [[Concepts/Tracing|Tracing]] `lesson term` — Ingest OTel / SDK spans; index by session
- Prompt management `lesson term` — Versioned prompts tied to traces
- [[Concepts/LLM-as-a-Judge|LLM-as-a-Judge]] (as *LLM-as-judge*) `glossary` — Separate LLM scores agent output against a rubric
- [[Concepts/Session replay|Session replay]] `lesson term` — Step through past runs for debugging
- RAG relevancy `lesson term` — Does the retrieved context match the query
- Trace clustering `lesson term` — Cluster similar runs for drift detection
- Guardrail enforcement `lesson term` — PII/toxicity/scope checks on logged content
- [[Concepts/Observability|Observability]] `glossary` — The ability to understand an AI system's behavior from recorded inputs, outputs, state transitions, tool calls, timings, costs, errors, and evaluation signals.

## Ships

- [[Artifacts/14-24 obs-platform-wiring|obs-platform-wiring]] `skill` — Pick an observability platform (Langfuse, Phoenix, Opik, Datadog) and wire traces + evals + prompt versions into an existing agent.

## Further reading

- [[Resources/Comet Opik|Comet Opik]] ([link](https://www.comet.com/site/products/opik/)) — optimization + guardrails ·  also cited by 1 other lesson
- [[Resources/Arize Phoenix docs|Arize Phoenix docs]] ([link](https://docs.arize.com/phoenix)) — auto-instrumentation, drift ·  also cited by 2 other lessons
- [[Resources/Langfuse docs|Langfuse docs]] ([link](https://langfuse.com/)) — tracing, evals, prompt mgmt ·  also cited by 1 other lesson
- [[Resources/OpenTelemetry — GenAI semconv|OpenTelemetry — GenAI semconv]] ([link](https://opentelemetry.io/docs/specs/semconv/gen-ai/)) — the schema all three consume ·  also cited by 9 other lessons

## In learning paths

- [[Paths/Agent Systems Engineering|Agent Systems Engineering]] — step 14, required


%% ── my notes ── %%
