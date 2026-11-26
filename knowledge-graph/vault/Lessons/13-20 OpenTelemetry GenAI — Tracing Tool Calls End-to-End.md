---
id: "lesson:13/20"
type: lesson
ref: 13/20
phase: 13
num: 20
title: "OpenTelemetry GenAI — Tracing Tool Calls End-to-End"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 2
community: 10
aliases:
  - 13/20
  - 13-20
tags:
  - phase/13
  - type/build
  - community/10
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/20-opentelemetry-genai/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/20-opentelemetry-genai"
---

# 13/20 OpenTelemetry GenAI — Tracing Tool Calls End-to-End

> An agent calls five tools, three MCP servers, and two sub-agents. You need one trace across all of it. The OpenTelemetry GenAI semantic conventions (stable attributes in v1.37 and up) are the 2026 standard, natively supported by Datadog, Langfuse, Arize Phoenix, OpenLLMetry, and AgentOps. This lesson names the required attributes, walks the span hierarchy (agent → LLM → tool), and ships a stdlib span emitter you can plug into any OTel exporter.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/20-opentelemetry-genai/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/20-opentelemetry-genai) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/20-opentelemetry-genai) · code: main.py  
**Community:** [[Communities/10 Trace · Shadow Traffic · requestState|10 Trace · Shadow Traffic · requestState]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 07 (MCP server), Phase 13 · 08 (MCP client)`

- [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]] — MCP server
- [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]] — MCP client

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]], [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]]

## Builds on this

- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]
- [[Lessons/19-28 Capstone Lesson 28- Observability with OTel GenAI Spans and Prometheus Metrics|19/28 Capstone Lesson 28: Observability with OTel GenAI Spans and Prometheus Metrics]]

## Concepts taught

- OTel `lesson term` — Open standard for traces, metrics, logs
- [[Concepts/GenAI semconv|GenAI semconv]] `lesson term` — Stable attribute names for LLM / tool / agent spans
- gen_ai. `lesson term` — All GenAI attributes share this prefix
- Span `lesson term` — A unit of work with a start, end, and attributes
- [[Concepts/Trace|Trace]] `glossary` — Tree of spans sharing a trace id
- SpanKind `lesson term` — Hints about span direction
- OTLP `lesson term` — Wire format for exporters
- Opt-in content `lesson term` — Off by default; env var to enable
- traceparent `lesson term` — Propagates trace context across services
- Exporter `lesson term` — Component that sends spans to Jaeger / Datadog / etc.

## Ships

- [[Artifacts/13-20 otel-genai-instrumentation|otel-genai-instrumentation]] `skill` — Produce an instrumentation plan for an agent codebase to emit OTel GenAI spans end-to-end.

## Further reading

- Datadog — LLM OTel semantic convention ([link](https://www.datadoghq.com/blog/llm-otel-semantic-convention/)) — production integration walkthrough
- open-telemetry/semantic-conventions — GenAI spans ([link](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/gen-ai/gen-ai-spans.md)) — GitHub-hosted source of truth
- [[Resources/OpenTelemetry — GenAI semconv|OpenTelemetry — GenAI semconv]] ([link](https://opentelemetry.io/docs/specs/semconv/gen-ai/)) — canonical conventions for GenAI spans, metrics, and events ·  also cited by 9 other lessons
- OpenTelemetry — GenAI agent spans ([link](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/)) — agent-level `invoke_agent` span
- OpenTelemetry — GenAI spans ([link](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-spans/)) — LLM and tool-execution span attribute list


%% ── my notes ── %%
