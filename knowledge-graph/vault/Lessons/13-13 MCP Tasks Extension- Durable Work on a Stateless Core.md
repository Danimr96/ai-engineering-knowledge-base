---
id: "lesson:13/13"
type: lesson
ref: 13/13
phase: 13
num: 13
title: "MCP Tasks Extension: Durable Work on a Stateless Core"
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 10
prereqs: 3
community: 10
aliases:
  - 13/13
  - 13-13
tags:
  - phase/13
  - type/build
  - community/10
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/13-mcp-async-tasks/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/13-mcp-async-tasks"
---

# 13/13 MCP Tasks Extension: Durable Work on a Stateless Core

> Stateless MCP does not mean every operation must finish in one request. The official Tasks extension gives long-running work an explicit durable handle. A server can return that handle from `tools/call`, any instance can answer `tasks/get`, and client input arrives through `tasks/update` without reviving protocol sessions.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/13-mcp-async-tasks/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/13-mcp-async-tasks) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/13-mcp-async-tasks) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/10 Trace · Shadow Traffic · requestState|10 Trace · Shadow Traffic · requestState]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 09 (transports), Phase 13 · 11 (stateless MRTR), Phase 13 · 12 (elicitation)`

- [[Lessons/13-09 MCP Transports- stdio and Stateless Streamable HTTP|13/09 MCP Transports: stdio and Stateless Streamable HTTP]] — transports
- [[Lessons/13-11 MCP Model Input- Sampling Migration and Stateless MRTR|13/11 MCP Model Input: Sampling Migration and Stateless MRTR]] — stateless MRTR
- [[Lessons/13-12 Explicit Scope and Stateless Elicitation|13/12 Explicit Scope and Stateless Elicitation]] — elicitation

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]], [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]], [[Lessons/13-10 MCP Resources and Prompts- Addressable Context for Stateless Servers|13/10 MCP Resources and Prompts: Addressable Context for Stateless Servers]]
- depth 3: [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]]

## Builds on this

- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]
- [[Lessons/13-29 MCP Reliability, Cancellation, and Flow Control|13/29 MCP Reliability, Cancellation, and Flow Control]]

## Concepts taught

- [[Concepts/Tasks extension|Tasks extension]] `lesson term` — Optional io.modelcontextprotocol/tasks capability for durable async work
- CreateTaskResult `lesson term` — Server-directed resultType: "task" response to an eligible request
- tasks/get `lesson term` — Poll a full current task snapshot, including terminal result or pending input
- tasks/update `lesson term` — Submit responses to a task's outstanding inputRequests
- tasks/cancel `lesson term` — Acknowledge cooperative cancellation intent
- [[Concepts/input_required|input_required]] `lesson term` — Task status indicating client input is outstanding
- pollIntervalMs `lesson term` — Server-suggested minimum delay before another poll
- ttlMs `lesson term` — Expiry duration measured from task creation
- Durable-before-return `lesson term` — Rule that the task id must resolve before its handle is sent
- notifications/tasks `lesson term` — Optional full task snapshot delivered on a subscribed SSE response

## Ships

- [[Artifacts/13-13 task-store-designer|task-store-designer]] `skill` — Design durable MCP work with the current Tasks extension, stateless requests, explicit ownership, polling, input updates, and cancellation.

## Further reading

- [[Resources/MCP Multi Round-Trip Requests|MCP Multi Round-Trip Requests]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr)) ·  also cited by 4 other lessons
- [[Resources/MCP Streamable HTTP|MCP Streamable HTTP]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)) ·  also cited by 8 other lessons
- [[Resources/Official MCP Tasks extension|Official MCP Tasks extension]] ([link](https://tasks.extensions.modelcontextprotocol.io/specification/draft/tasks)) ·  also cited by 3 other lessons

## In learning paths

- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]] — step 8, required


%% ── my notes ── %%
