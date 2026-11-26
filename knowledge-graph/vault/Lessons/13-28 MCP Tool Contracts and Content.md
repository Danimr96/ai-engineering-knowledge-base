---
id: "lesson:13/28"
type: lesson
ref: 13/28
phase: 13
num: 28
title: MCP Tool Contracts and Content
lesson_type: build
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 6
code_files: 2
concepts: 8
prereqs: 3
community: 10
aliases:
  - 13/28
  - 13-28
tags:
  - phase/13
  - type/build
  - community/10
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/28-mcp-tool-contracts-and-content/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/28-mcp-tool-contracts-and-content"
---

# 13/28 MCP Tool Contracts and Content

> A tool is safe to automate only when discovery, arguments, results, pagination, and transport metadata agree on one contract.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/28-mcp-tool-contracts-and-content/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/28-mcp-tool-contracts-and-content) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/28-mcp-tool-contracts-and-content) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/10 Trace · Shadow Traffic · requestState|10 Trace · Shadow Traffic · requestState]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13, Lessons 07, 09, and 10`

- [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]]
- [[Lessons/13-09 MCP Transports- stdio and Stateless Streamable HTTP|13/09 MCP Transports: stdio and Stateless Streamable HTTP]]
- [[Lessons/13-10 MCP Resources and Prompts- Addressable Context for Stateless Servers|13/10 MCP Resources and Prompts: Addressable Context for Stateless Servers]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]], [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]], [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]]

## Concepts taught

- inputSchema `lesson term` — JSON Schema object defining accepted tool arguments
- outputSchema `lesson term` — Optional JSON Schema defining structuredContent
- structuredContent `lesson term` — Any JSON value produced by a tool result
- Content block `lesson term` — Typed text, image, audio, resource link, or embedded resource
- x-mcp-header `lesson term` — Schema annotation that mirrors a primitive argument into Streamable HTTP metadata
- Opaque cursor `lesson term` — Server-issued pagination token whose value the client does not interpret
- Completion reference `lesson term` — Prompt name or resource URI/template whose argument is being completed
- Admission `lesson term` — Client decision to expose or reject a discovered descriptor

## Ships

- [[Artifacts/13-28 mcp-contract-reviewer|mcp-contract-reviewer]] `skill` — Review MCP tool descriptors, results, pagination, completions, and parameter-header policy before exposing tools to a model.

## Further reading

- [[Resources/MCP Streamable HTTP|MCP Streamable HTTP]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)) ·  also cited by 8 other lessons
- [[Resources/MCP Tools|MCP Tools]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)) ·  also cited by 2 other lessons
- MCP Completion ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/completion))
- MCP Pagination ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination))

## In learning paths

- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]] — step 14, required


%% ── my notes ── %%
