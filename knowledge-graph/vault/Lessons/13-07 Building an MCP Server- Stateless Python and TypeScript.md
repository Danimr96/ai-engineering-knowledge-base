---
id: "lesson:13/07"
type: lesson
ref: 13/07
phase: 13
num: 7
title: "Building an MCP Server: Stateless Python and TypeScript"
lesson_type: build
languages:
  - Python
  - TypeScript
time_min: 85
on_route: false
quiz_count: 6
code_files: 3
concepts: 8
prereqs: 1
community: 10
aliases:
  - 13/07
  - 13-07
tags:
  - phase/13
  - type/build
  - community/10
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/07-building-an-mcp-server/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/07-building-an-mcp-server"
---

# 13/07 Building an MCP Server: Stateless Python and TypeScript

> A modern MCP server does not remember a handshake. It validates the metadata on every request, runs one handler, and returns one typed result.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 85 min · **Languages:** Python, TypeScript · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/07-building-an-mcp-server/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/07-building-an-mcp-server) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/07-building-an-mcp-server) · code: main.py, main.ts, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/10 Trace · Shadow Traffic · requestState|10 Trace · Shadow Traffic · requestState]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13, Lesson 06`

- [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]], [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]]

## Builds on this

- [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]]
- [[Lessons/13-09 MCP Transports- stdio and Stateless Streamable HTTP|13/09 MCP Transports: stdio and Stateless Streamable HTTP]]
- [[Lessons/13-10 MCP Resources and Prompts- Addressable Context for Stateless Servers|13/10 MCP Resources and Prompts: Addressable Context for Stateless Servers]]
- [[Lessons/13-11 MCP Model Input- Sampling Migration and Stateless MRTR|13/11 MCP Model Input: Sampling Migration and Stateless MRTR]]
- [[Lessons/13-12 Explicit Scope and Stateless Elicitation|13/12 Explicit Scope and Stateless Elicitation]]
- [[Lessons/13-14 MCP Apps on the Stateless Protocol|13/14 MCP Apps on the Stateless Protocol]]
- [[Lessons/13-15 MCP Security- Poisoned Metadata, Routing, and MRTR State|13/15 MCP Security: Poisoned Metadata, Routing, and MRTR State]]
- [[Lessons/13-20 OpenTelemetry GenAI — Tracing Tool Calls End-to-End|13/20 OpenTelemetry GenAI — Tracing Tool Calls End-to-End]]
- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]
- [[Lessons/13-28 MCP Tool Contracts and Content|13/28 MCP Tool Contracts and Content]]
- [[Lessons/19-20 Agent Harness Loop Contract|19/20 Agent Harness Loop Contract]]
- [[Lessons/19-21 Tool Registry with Schema Validation|19/21 Tool Registry with Schema Validation]]
- [[Lessons/19-22 JSON-RPC 2.0 Over Newline-Delimited Stdio|19/22 JSON-RPC 2.0 Over Newline-Delimited Stdio]]
- [[Lessons/19-23 Function Call Dispatcher|19/23 Function Call Dispatcher]]
- [[Lessons/19-24 Plan-Execute Control Flow|19/24 Plan-Execute Control Flow]]

## Concepts taught

- Stateless server `lesson term` — Handles each request from its own metadata without protocol-session memory
- [[Concepts/server-discover|server/discover]] `lesson term` — Mandatory modern method that advertises versions and capabilities
- Complete result `lesson term` — Successful modern result with resultType: "complete"
- [[Concepts/Cacheable result|Cacheable result]] `lesson term` — Discovery, list, or resource-read result with ttlMs and cacheScope
- Deterministic list `lesson term` — Same logical registry produces the same item order
- Server identity `lesson term` — Recommended io.modelcontextprotocol/serverInfo in result meta
- Tool error `lesson term` — Valid tool call that returns content with isError: true
- Protocol error `lesson term` — Invalid JSON-RPC or MCP request returned through error

## Ships

- [[Artifacts/13-07 mcp-server-scaffolder|mcp-server-scaffolder]] `skill` — Design a stateless MCP 2026-07-28 server with discovery, request validation, and deterministic primitives.

## Further reading

- [[Resources/Model Context Protocol — Specification 2026-07-28|Model Context Protocol — Specification 2026-07-28]] ([link](https://modelcontextprotocol.io/specification/2026-07-28)) ·  also cited by 5 other lessons
- [[Resources/MCP stdio Transport|MCP stdio Transport]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio)) ·  also cited by 2 other lessons
- [[Resources/MCP server discovery|MCP server discovery]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/discover)) ·  also cited by 8 other lessons
- [[Resources/MCP Prompts|MCP Prompts]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts)) ·  also cited by 1 other lesson
- [[Resources/MCP Resources|MCP Resources]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/resources)) ·  also cited by 1 other lesson
- [[Resources/MCP Tools|MCP Tools]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)) ·  also cited by 2 other lessons

## In learning paths

- [[Paths/Developer Experience and Education|Developer Experience and Education]] — step 5, required
- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]] — step 2, required


%% ── my notes ── %%
