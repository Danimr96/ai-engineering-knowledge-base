---
id: "lesson:13/02"
type: lesson
ref: 13/02
phase: 13
num: 2
title: "Function Calling Deep Dive — OpenAI, Anthropic, Gemini"
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
  - 13/02
  - 13-02
tags:
  - phase/13
  - type/build
  - community/03
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/02-function-calling-deep-dive/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/02-function-calling-deep-dive"
---

# 13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini

> The three frontier providers converged on the same tool-call loop in 2024 and then diverged on everything else. OpenAI uses `tools` and `tool_calls`. Anthropic uses `tool_use` and `tool_result` blocks. Gemini uses `functionDeclarations` and unique-id correlation. This lesson diffs the three side by side so code that ships on one provider does not break when you port it.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/02-function-calling-deep-dive/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/02-function-calling-deep-dive) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/02-function-calling-deep-dive) · code: main.py  
**Community:** [[Communities/03 Parallel tool calls · Strict mode · Refusal|03 Parallel tool calls · Strict mode · Refusal]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 01 (the tool interface)`

- [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]] — the tool interface

## Builds on this

- [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]]
- [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]]
- [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]]
- [[Lessons/13-21 LLM Routing Layer — LiteLLM, OpenRouter, Portkey|13/21 LLM Routing Layer — LiteLLM, OpenRouter, Portkey]]
- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]
- [[Lessons/15-02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning|15/02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning]]
- [[Lessons/19-20 Agent Harness Loop Contract|19/20 Agent Harness Loop Contract]]
- [[Lessons/19-21 Tool Registry with Schema Validation|19/21 Tool Registry with Schema Validation]]
- [[Lessons/19-22 JSON-RPC 2.0 Over Newline-Delimited Stdio|19/22 JSON-RPC 2.0 Over Newline-Delimited Stdio]]
- [[Lessons/19-23 Function Call Dispatcher|19/23 Function Call Dispatcher]]
- [[Lessons/19-24 Plan-Execute Control Flow|19/24 Plan-Execute Control Flow]]

## Concepts taught

- [[Concepts/Function Calling|Function Calling]] `glossary` — Provider-level API for structured tool-call emission
- Tool declaration `lesson term` — Name + description + JSON Schema input payload
- [[Concepts/Tool choice|Tool choice]] (as *tool_choice*) `lesson term` — Auto / required / none / specific-name modes
- [[Concepts/Strict mode|Strict mode]] `lesson term` — OpenAI flag that constrains decoding to match schema
- tool_use block `lesson term` — Inline content block with id, name, input
- functionCall part `lesson term` — A parts[] entry containing name, args, and id
- Arguments-as-string `lesson term` — OpenAI returns args as a JSON string, not an object
- [[Concepts/Parallel tool calls|Parallel tool calls]] `lesson term` — Multiple tool calls in one assistant message
- [[Concepts/Refusal|Refusal]] `lesson term` — Strict-mode-only refusal block instead of a call
- OpenAPI 3.0 subset `lesson term` — Gemini uses a JSON-Schema-like dialect with minor differences

## Ships

- [[Artifacts/13-02 provider-portability-audit|provider-portability-audit]] `skill` — Audit a function-calling integration against one provider for what breaks when ported to the other two.

## Further reading

- [[Resources/Google — Gemini function calling|Google — Gemini function calling]] ([link](https://ai.google.dev/gemini-api/docs/function-calling)) — parallel calls, unique ids, and OpenAPI subset ·  also cited by 2 other lessons
- [[Resources/Anthropic — Tool use overview|Anthropic — Tool use overview]] ([link](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)) — `tool_use` and `tool_result` block semantics ·  also cited by 1 other lesson
- Vertex AI — Function calling reference ([link](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling)) — Gemini's enterprise surface
- [[Resources/OpenAI Function Calling Guide|OpenAI Function Calling Guide]] ([link](https://platform.openai.com/docs/guides/function-calling)) — canonical reference including strict mode and parallel calls ·  also cited by 4 other lessons
- [[Resources/OpenAI — Structured Outputs guide|OpenAI — Structured Outputs guide]] ([link](https://platform.openai.com/docs/guides/structured-outputs)) — strict-mode schema enforcement details ·  also cited by 3 other lessons


%% ── my notes ── %%
