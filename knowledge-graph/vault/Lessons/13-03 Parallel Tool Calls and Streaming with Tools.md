---
id: "lesson:13/03"
type: lesson
ref: 13/03
phase: 13
num: 3
title: Parallel Tool Calls and Streaming with Tools
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
  - 13/03
  - 13-03
tags:
  - phase/13
  - type/build
  - community/03
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/03-parallel-and-streaming-tool-calls/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/03-parallel-and-streaming-tool-calls"
---

# 13/03 Parallel Tool Calls and Streaming with Tools

> Three independent weather lookups serialized is three round trips. Run them in parallel and total time collapses to the slowest single call. Every frontier provider now emits multiple tool calls in a single turn. The payoff is real; the plumbing is subtle. This lesson walks both halves: the parallel fan-out and the streamed-argument reassembly, with emphasis on the id-correlation trap.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/03-parallel-and-streaming-tool-calls/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/03-parallel-and-streaming-tool-calls) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/03-parallel-and-streaming-tool-calls) · code: main.py  
**Community:** [[Communities/03 Parallel tool calls · Strict mode · Refusal|03 Parallel tool calls · Strict mode · Refusal]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 02 (function calling deep dive)`

- [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]] — function calling deep dive

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]]

## Builds on this

- [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]]
- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]
- [[Lessons/15-02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning|15/02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning]]
- [[Lessons/19-20 Agent Harness Loop Contract|19/20 Agent Harness Loop Contract]]
- [[Lessons/19-21 Tool Registry with Schema Validation|19/21 Tool Registry with Schema Validation]]
- [[Lessons/19-22 JSON-RPC 2.0 Over Newline-Delimited Stdio|19/22 JSON-RPC 2.0 Over Newline-Delimited Stdio]]
- [[Lessons/19-23 Function Call Dispatcher|19/23 Function Call Dispatcher]]
- [[Lessons/19-24 Plan-Execute Control Flow|19/24 Plan-Execute Control Flow]]

## Concepts taught

- [[Concepts/Parallel tool calls|Parallel tool calls]] `lesson term` — Model emits multiple tool calls in a single assistant message
- disable_parallel_tool_use `lesson term` — Opt-out flag; default is parallel enabled
- Tool call id `lesson term` — Per-call identifier the result message must echo
- Accumulator `lesson term` — Per-id string buffer for partial arguments chunks
- Out-of-order completion `lesson term` — Parallel calls finish in unpredictable order; ids are the glue
- Dependency graph `lesson term` — Tools whose outputs feed into inputs of other tools; cannot parallelize
- Parse-early trap `lesson term` — Attempting to parse an incomplete arguments string
- streamFunctionCallArguments `lesson term` — Streamed argument chunks with unique id per call
- Completion-order reply `lesson term` — Reply with results as they arrive, keyed by id

## Ships

- [[Artifacts/13-03 parallel-call-safety-check|parallel-call-safety-check]] `skill` — Audit a tool registry for safe parallelization. Mark each tool parallel_safe, note ordering dependencies, and flag downstream rate-limit risk.

## Further reading

- [[Resources/Google — Gemini function calling|Google — Gemini function calling]] ([link](https://ai.google.dev/gemini-api/docs/function-calling)) — id-correlated parallel calls from Gemini 3 ·  also cited by 2 other lessons
- [[Resources/Anthropic API Reference|Anthropic API Reference]] ([link](https://docs.anthropic.com/en/api/messages-streaming)) — `content_block_delta` with `input_json_delta` ·  also cited by 1 other lesson
- Anthropic — Tool use: implementing tool use ([link](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implementing-tool-use)) — `disable_parallel_tool_use` and result batching
- OpenAI — Streaming responses with tools ([link](https://platform.openai.com/docs/api-reference/responses-streaming)) — chunked argument reassembly for OpenAI streams
- [[Resources/OpenAI Function Calling Guide|OpenAI Function Calling Guide]] ([link](https://platform.openai.com/docs/guides/function-calling)) — default behavior and the opt-out flag ·  also cited by 4 other lessons


%% ── my notes ── %%
