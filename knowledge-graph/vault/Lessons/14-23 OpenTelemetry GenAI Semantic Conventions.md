---
id: "lesson:14/23"
type: lesson
ref: 14/23
phase: 14
num: 23
title: OpenTelemetry GenAI Semantic Conventions
lesson_type: learn+build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 1
concepts: 9
prereqs: 2
community: 7
aliases:
  - 14/23
  - 14-23
tags:
  - phase/14
  - type/learn+build
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/23-otel-genai-conventions/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/23-otel-genai-conventions"
---

# 14/23 OpenTelemetry GenAI Semantic Conventions

> OpenTelemetry's GenAI SIG (launched April 2024) defines the standard schema for agent telemetry. Span names, attributes, and content-capture rules converge across vendors so agent traces mean the same thing in Datadog, Grafana, Jaeger, and Honeycomb.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn + Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/23-otel-genai-conventions/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/23-otel-genai-conventions) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/23-otel-genai-conventions) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 13 (LangGraph), Phase 14 · 24 (Observability Platforms)`

- [[Lessons/14-13 Stateful Graph Orchestration — Durable Execution and Checkpoints|14/13 Stateful Graph Orchestration — Durable Execution and Checkpoints]] — LangGraph
- [[Lessons/14-24 Agent Observability- Langfuse, Phoenix, Opik|14/24 Agent Observability: Langfuse, Phoenix, Opik]] — Observability Platforms

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-12 Anthropic's Workflow Patterns- Simple Over Complex|14/12 Anthropic's Workflow Patterns: Simple Over Complex]]

## Builds on this

- [[Lessons/14-24 Agent Observability- Langfuse, Phoenix, Opik|14/24 Agent Observability: Langfuse, Phoenix, Opik]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]
- [[Lessons/19-28 Capstone Lesson 28- Observability with OTel GenAI Spans and Prometheus Metrics|19/28 Capstone Lesson 28: Observability with OTel GenAI Spans and Prometheus Metrics]]

## Concepts taught

- GenAI SIG `lesson term` — OTel working group defining the schema
- invoke_agent `lesson term` — Name of the span representing an agent run
- CLIENT span `lesson term` — Span for a call to a remote agent service
- INTERNAL span `lesson term` — Span for an in-process agent run
- gen_ai.provider.name `lesson term` — anthropic / openai / aws.bedrock / google.vertex
- gen_ai.data_source.id `lesson term` — Which corpus/store a retrieval hit
- Content capture `lesson term` — Opt-in capture of messages; store externally in prod
- Stability opt-in `lesson term` — Env var to pin experimental conventions
- [[Concepts/Trace|Trace]] `glossary` — A correlated record of one request or task across model calls, retrieval, tools, state transitions, retries, approvals, and evaluations.

## Ships

- [[Artifacts/14-23 otel-genai|otel-genai]] `skill` — Instrument an agent with OpenTelemetry GenAI semantic conventions — invoke_agent, chat, tool_call spans with correct attributes and opt-in content capture.

## Further reading

- [[Resources/AutoGen v0.4, Microsoft Research|AutoGen v0.4, Microsoft Research]] ([link](https://www.microsoft.com/en-us/research/articles/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness/)) — OTel spans built in ·  also cited by 3 other lessons
- [[Resources/OpenAI Agents SDK docs|OpenAI Agents SDK docs]] ([link](https://openai.github.io/openai-agents-python/)) — GenAI spans by default ·  also cited by 8 other lessons
- [[Resources/OpenTelemetry — GenAI semconv|OpenTelemetry — GenAI semconv]] ([link](https://opentelemetry.io/docs/specs/semconv/gen-ai/)) — the spec ·  also cited by 9 other lessons
- [[Resources/Claude Agent SDK overview|Claude Agent SDK overview]] ([link](https://platform.claude.com/docs/en/agent-sdk/overview)) — W3C trace context propagation ·  also cited by 6 other lessons

## In learning paths

- [[Paths/AI Evaluation and Reliability|AI Evaluation and Reliability]] — step 5, required


%% ── my notes ── %%
