---
id: "lesson:13/04"
type: lesson
ref: 13/04
phase: 13
num: 4
title: "Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 1
community: 3
aliases:
  - 13/04
  - 13-04
tags:
  - phase/13
  - type/build
  - community/03
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/04-structured-output/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/04-structured-output"
---

# 13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding

> "Ask the model nicely to return JSON" fails 5 to 15 percent of the time, even on frontier models. Structured outputs close that gap with constrained decoding: the model is literally prevented from emitting a token that would violate the schema. OpenAI's strict mode, Anthropic's schema-typed tool use, Gemini's `responseSchema`, Pydantic AI's `output_type`, and Zod's `.parse` are five surface forms of the same idea. This lesson builds the schema validator and the strict-mode contract learners will use for every production extraction pipeline.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/04-structured-output/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/04-structured-output) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/04-structured-output) · code: main.py  
**Community:** [[Communities/03 Parallel tool calls · Strict mode · Refusal|03 Parallel tool calls · Strict mode · Refusal]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 02 (function calling deep dive)`

- [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]] — function calling deep dive

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]]

## Builds on this

- [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]]
- [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]]
- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]
- [[Lessons/19-20 Agent Harness Loop Contract|19/20 Agent Harness Loop Contract]]
- [[Lessons/19-21 Tool Registry with Schema Validation|19/21 Tool Registry with Schema Validation]]
- [[Lessons/19-22 JSON-RPC 2.0 Over Newline-Delimited Stdio|19/22 JSON-RPC 2.0 Over Newline-Delimited Stdio]]
- [[Lessons/19-23 Function Call Dispatcher|19/23 Function Call Dispatcher]]
- [[Lessons/19-24 Plan-Execute Control Flow|19/24 Plan-Execute Control Flow]]

## Concepts taught

- JSON Schema 2020-12 `lesson term` — IETF-draft schema dialect every modern provider speaks
- [[Concepts/Strict mode|Strict mode]] `lesson term` — OpenAI flag that enforces schema via constrained decoding
- [[Concepts/Constrained decoding|Constrained decoding]] `lesson term` — Decode-time enforcement that masks invalid next-tokens
- [[Concepts/Refusal|Refusal]] `lesson term` — Typed outcome when input cannot fit the schema
- Parse error `lesson term` — Output did not parse as JSON; impossible under strict
- Schema violation `lesson term` — Parsed but violated types / required / enum / range
- additionalProperties: false `lesson term` — Forbids unknown fields; required in OpenAI strict
- Pydantic BaseModel `lesson term` — Python class that emits and validates JSON Schema
- Zod schema `lesson term` — TS runtime schema for provider output validation
- Grammar enforcement `lesson term` — FSM-based logit masking, as in outlines / guidance

## Ships

- [[Artifacts/13-04 structured-output-designer|structured-output-designer]] `skill` — Design a strict-mode-compatible JSON Schema plus Pydantic model for a free-text extraction target, with typed refusal and retry handling stubbed in.

## Further reading

- Pydantic AI — Output ([link](https://ai.pydantic.dev/output/)) — typed output_type bindings that serialize to each provider
- [[Resources/JSON Schema — 2020-12 release notes|JSON Schema — 2020-12 release notes]] ([link](https://json-schema.org/draft/2020-12/release-notes)) — the canonical spec ·  also cited by 1 other lesson
- Microsoft — Structured outputs in Azure OpenAI ([link](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/structured-outputs)) — enterprise deployment notes and strict-mode caveats
- OpenAI — Introducing structured outputs ([link](https://openai.com/index/introducing-structured-outputs-in-the-api/)) — August 2024 launch post explaining the decoding guarantee
- [[Resources/OpenAI — Structured Outputs guide|OpenAI — Structured Outputs guide]] ([link](https://platform.openai.com/docs/guides/structured-outputs)) — strict mode, refusals, and schema requirements ·  also cited by 3 other lessons


%% ── my notes ── %%
