---
id: "lesson:13/06"
type: lesson
ref: 13/06
phase: 13
num: 6
title: "MCP Fundamentals: Stateless Requests and JSON-RPC"
lesson_type: learn
languages:
  - Python
time_min: 55
on_route: false
quiz_count: 6
code_files: 2
concepts: 9
prereqs: 5
community: 3
aliases:
  - 13/06
  - 13-06
tags:
  - phase/13
  - type/learn
  - community/03
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/06-mcp-fundamentals/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/06-mcp-fundamentals"
---

# 13/06 MCP Fundamentals: Stateless Requests and JSON-RPC

> Modern MCP has no handshake and no protocol session. Each request must carry enough metadata to be understood, authorized, routed, and retried on its own.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Learn · **Time:** 55 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/06-mcp-fundamentals/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/06-mcp-fundamentals) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/06-mcp-fundamentals) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/03 Parallel tool calls · Strict mode · Refusal|03 Parallel tool calls · Strict mode · Refusal]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13, Lessons 01 through 05`

- **13/01-05**:
    - [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]]
    - [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]]
    - [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]]
    - [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]]
    - [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]]

## Builds on this

- [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]]
- [[Lessons/13-19 A2A — Agent-to-Agent Protocol|13/19 A2A — Agent-to-Agent Protocol]]
- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]
- [[Lessons/19-20 Agent Harness Loop Contract|19/20 Agent Harness Loop Contract]]
- [[Lessons/19-21 Tool Registry with Schema Validation|19/21 Tool Registry with Schema Validation]]
- [[Lessons/19-22 JSON-RPC 2.0 Over Newline-Delimited Stdio|19/22 JSON-RPC 2.0 Over Newline-Delimited Stdio]]
- [[Lessons/19-23 Function Call Dispatcher|19/23 Function Call Dispatcher]]
- [[Lessons/19-24 Plan-Execute Control Flow|19/24 Plan-Execute Control Flow]]

## Concepts taught

- Stateless protocol `lesson term` — Every request supplies the metadata needed to interpret it
- Request metadata `lesson term` — Version, client capabilities, and recommended client identity in params.meta
- [[Concepts/server-discover|server/discover]] `lesson term` — Mandatory server method for versions, capabilities, instructions, and identity
- [[Concepts/resultType|resultType]] `lesson term` — Discriminator on every successful modern result
- [[Concepts/Cacheable result|Cacheable result]] `lesson term` — Result that includes required ttlMs and cacheScope hints
- [[Concepts/Protocol era|Protocol era]] `lesson term` — Modern per-request metadata or legacy connection-scoped initialization
- Transport lifetime `lesson term` — Process, connection, or response-stream lifetime, not protocol session state
- -32022 `lesson term` — Unsupported protocol version error with requested and supported versions
- [[Concepts/Stateless MCP|Stateless MCP]] `glossary` — The MCP 2026-07-28 request model in which every request carries the protocol version and client capabilities in `params._meta`, while results carry an explicit `resultType`; no protocol state is keyed by an initialization handshake, connection, or `Mcp-Session-Id`.

## Ships

- [[Artifacts/13-06 mcp-request-tracer|mcp-request-tracer]] `skill` — Audit MCP transcripts message by message across modern stateless and explicit legacy protocol eras.

## Further reading

- MCP Architecture ([link](https://modelcontextprotocol.io/specification/2026-07-28/architecture))
- [[Resources/MCP Base Protocol|MCP Base Protocol]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic)) ·  also cited by 2 other lessons
- [[Resources/MCP 2026-07-28 key changes|MCP 2026-07-28 key changes]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/changelog)) ·  also cited by 6 other lessons
- [[Resources/MCP server discovery|MCP server discovery]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/discover)) ·  also cited by 8 other lessons

## In learning paths

- [[Paths/Agent Systems Engineering|Agent Systems Engineering]] — step 3, required
- [[Paths/Developer Experience and Education|Developer Experience and Education]] — step 4, required
- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]] — step 1, required


%% ── my notes ── %%
