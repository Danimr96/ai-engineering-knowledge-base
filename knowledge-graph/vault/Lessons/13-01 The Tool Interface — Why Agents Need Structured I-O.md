---
id: "lesson:13/01"
type: lesson
ref: 13/01
phase: 13
num: 1
title: "The Tool Interface — Why Agents Need Structured I/O"
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 2
concepts: 10
prereqs: 0
community: 3
aliases:
  - 13/01
  - 13-01
tags:
  - phase/13
  - type/learn
  - community/03
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/01-the-tool-interface/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/01-the-tool-interface"
---

# 13/01 The Tool Interface — Why Agents Need Structured I/O

> A language model produces tokens. A program takes actions. The gap between those two is the tool interface: a contract that lets the model request an action and the host execute it. Every 2026 stack — function calling on OpenAI, Anthropic, and Gemini; MCP's `tools/call`; A2A's task parts — is a different encoding of the same four-step loop. This lesson names the loop and shows the minimum machinery to run it.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/01-the-tool-interface/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/01-the-tool-interface) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/01-the-tool-interface) · code: main.py, main.ts  
**Community:** [[Communities/03 Parallel tool calls · Strict mode · Refusal|03 Parallel tool calls · Strict mode · Refusal]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 11 (LLM completion APIs)`

- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM completion APIs ·  medium confidence

## Builds on this

- [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]]
- [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]]
- [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]]
- [[Lessons/13-22 Agent Skills- Portable Contract and Runtime Boundary|13/22 Agent Skills: Portable Contract and Runtime Boundary]]
- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]
- [[Lessons/14-06 Tool Use and Function Calling|14/06 Tool Use and Function Calling]]
- [[Lessons/15-02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning|15/02 STaR, V-STaR, Quiet-STaR — Self-Taught Reasoning]]
- [[Lessons/19-20 Agent Harness Loop Contract|19/20 Agent Harness Loop Contract]]
- [[Lessons/19-21 Tool Registry with Schema Validation|19/21 Tool Registry with Schema Validation]]
- [[Lessons/19-22 JSON-RPC 2.0 Over Newline-Delimited Stdio|19/22 JSON-RPC 2.0 Over Newline-Delimited Stdio]]
- [[Lessons/19-23 Function Call Dispatcher|19/23 Function Call Dispatcher]]
- [[Lessons/19-24 Plan-Execute Control Flow|19/24 Plan-Execute Control Flow]]

## Concepts taught

- [[Concepts/Tool|Tool]] `lesson term` — A triple of name + JSON-Schema-typed input + executor function
- [[Concepts/Function Calling|Function Calling]] `glossary` — Provider-level API support for emitting structured tool calls instead of prose
- [[Concepts/Tool call|Tool call]] `lesson term` — A JSON payload with id, name, arguments emitted by the model
- [[Concepts/Tool result|Tool result]] `lesson term` — The executor's output, wrapped in a tool role message with matching id
- [[Concepts/Parallel tool calls|Parallel tool calls]] `lesson term` — Multiple call objects in one model turn, independent and orderable by id
- [[Concepts/Strict mode|Strict mode]] `lesson term` — Constrained decoding that forces the model's output to validate against the declared schema
- Pure tool `lesson term` — No side effects; safe to re-run
- Consequential tool `lesson term` — Mutates external state; requires gate, audit, or user confirmation
- Four-step loop `lesson term` — describe → decide → execute → observe
- [[Concepts/Host|Host]] `lesson term` — The program that holds the tool registry, calls the model, and runs the executor

## Ships

- [[Artifacts/13-01 tool-interface-reviewer|tool-interface-reviewer]] `skill` — Audit a tool definition (name + description + JSON Schema + executor outline) for loop fitness before it ships to an LLM.

## Further reading

- [[Resources/Google — Gemini function calling|Google — Gemini function calling]] ([link](https://ai.google.dev/gemini-api/docs/function-calling)) — `functionDeclarations` and parallel-call semantics in Gemini ·  also cited by 2 other lessons
- [[Resources/Anthropic — Tool use overview|Anthropic — Tool use overview]] ([link](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview)) — Claude's `tool_use` / `tool_result` block format ·  also cited by 1 other lesson
- [[Resources/JSON Schema — 2020-12 release notes|JSON Schema — 2020-12 release notes]] ([link](https://json-schema.org/draft/2020-12/release-notes)) — the schema dialect every modern tool API speaks ·  also cited by 1 other lesson
- [[Resources/Model Context Protocol — Specification 2026-07-28|Model Context Protocol — Specification 2026-07-28]] ([link](https://modelcontextprotocol.io/specification/2026-07-28)) — the current stateless, provider-agnostic generalization of the tool interface ·  also cited by 5 other lessons
- [[Resources/OpenAI Function Calling Guide|OpenAI Function Calling Guide]] ([link](https://platform.openai.com/docs/guides/function-calling)) — canonical reference for OpenAI-style tool declarations and call shapes ·  also cited by 4 other lessons

## In learning paths

- [[Paths/Agent Systems Engineering|Agent Systems Engineering]] — step 1, required
- [[Paths/Developer Experience and Education|Developer Experience and Education]] — step 2, required
- [[Paths/Software Engineering Fundamentals|Software Engineering Fundamentals]] — step 8, required


%% ── my notes ── %%
