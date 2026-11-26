---
id: "lesson:13/08"
type: lesson
ref: 13/08
phase: 13
num: 8
title: "Building an MCP Client: Discovery, Routing, and Dual-Era Fallback"
lesson_type: build
languages:
  - Python
time_min: 85
on_route: false
quiz_count: 6
code_files: 2
concepts: 10
prereqs: 1
community: 10
aliases:
  - 13/08
  - 13-08
tags:
  - phase/13
  - type/build
  - community/10
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/08-building-an-mcp-client/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/08-building-an-mcp-client"
---

# 13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback

> A modern MCP client repeats its contract on every request. Its hardest compatibility decision is knowing when an old server is truly old and when a modern server is reporting a correctable error.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 85 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/08-building-an-mcp-client/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/08-building-an-mcp-client) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/08-building-an-mcp-client) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/10 Trace · Shadow Traffic · requestState|10 Trace · Shadow Traffic · requestState]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13, Lesson 07`

- [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]], [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]]

## Builds on this

- [[Lessons/13-09 MCP Transports- stdio and Stateless Streamable HTTP|13/09 MCP Transports: stdio and Stateless Streamable HTTP]]
- [[Lessons/13-15 MCP Security- Poisoned Metadata, Routing, and MRTR State|13/15 MCP Security: Poisoned Metadata, Routing, and MRTR State]]
- [[Lessons/13-19 A2A — Agent-to-Agent Protocol|13/19 A2A — Agent-to-Agent Protocol]]
- [[Lessons/13-20 OpenTelemetry GenAI — Tracing Tool Calls End-to-End|13/20 OpenTelemetry GenAI — Tracing Tool Calls End-to-End]]
- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]

## Concepts taught

- Peer `lesson term` — Client-side record for one server transport and its discovered data
- [[Concepts/Protocol era|Protocol era]] `lesson term` — Modern per-request metadata or legacy initialization semantics
- Discovery probe `lesson term` — Initial server/discover used to identify the stdio era
- Recognized modern error `lesson term` — Error that proves modern behavior and forbids legacy fallback
- Legacy allowlist `lesson term` — Operator configuration permitting one bounded compatibility probe for a pinned peer
- Positive legacy evidence `lesson term` — Valid, correlated initialize result for an explicitly supported legacy revision
- Merged namespace `lesson term` — Canonical tool names across all active peers
- [[Concepts/Collision policy|Collision policy]] `lesson term` — Prefix or reject rule for duplicate tool names
- Era cache `lesson term` — Selected modern or legacy behavior stored for one transport peer
- Transport recovery `lesson term` — Restart or reconnect, rediscover, relist, and retry safely with a new id

## Ships

- [[Artifacts/13-08 mcp-client-harness|mcp-client-harness]] `skill` — Scaffold a multi-server MCP client with modern metadata, safe era negotiation, deterministic merge, and routing.

## Further reading

- [[Resources/Model Context Protocol — Specification 2026-07-28|Model Context Protocol — Specification 2026-07-28]] ([link](https://modelcontextprotocol.io/specification/2026-07-28)) ·  also cited by 5 other lessons
- [[Resources/MCP stdio Transport|MCP stdio Transport]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio)) ·  also cited by 2 other lessons
- [[Resources/MCP Versioning|MCP Versioning]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning)) ·  also cited by 1 other lesson
- [[Resources/MCP server discovery|MCP server discovery]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/discover)) ·  also cited by 8 other lessons
- [[Resources/MCP Tools|MCP Tools]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)) ·  also cited by 2 other lessons

## In learning paths

- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]] — step 3, required


%% ── my notes ── %%
