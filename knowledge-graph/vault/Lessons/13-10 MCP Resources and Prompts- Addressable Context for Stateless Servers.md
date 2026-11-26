---
id: "lesson:13/10"
type: lesson
ref: 13/10
phase: 13
num: 10
title: "MCP Resources and Prompts: Addressable Context for Stateless Servers"
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 2
concepts: 0
prereqs: 2
community: 10
aliases:
  - 13/10
  - 13-10
tags:
  - phase/13
  - type/build
  - community/10
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/10-mcp-resources-and-prompts/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/10-mcp-resources-and-prompts"
---

# 13/10 MCP Resources and Prompts: Addressable Context for Stateless Servers

> Tools perform operations. Resources expose addressable content. Prompts package user-selected message templates. A good MCP server keeps those contracts separate and predictable.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/10-mcp-resources-and-prompts/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/10-mcp-resources-and-prompts) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/10-mcp-resources-and-prompts) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/10 Trace · Shadow Traffic · requestState|10 Trace · Shadow Traffic · requestState]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13, Lesson 07 (Building an MCP Server), Phase 13, Lesson 09 (MCP Transports)`

- [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]] — Building an MCP Server
- [[Lessons/13-09 MCP Transports- stdio and Stateless Streamable HTTP|13/09 MCP Transports: stdio and Stateless Streamable HTTP]] — MCP Transports

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]], [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]], [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]]

## Builds on this

- [[Lessons/13-11 MCP Model Input- Sampling Migration and Stateless MRTR|13/11 MCP Model Input: Sampling Migration and Stateless MRTR]]
- [[Lessons/13-14 MCP Apps on the Stateless Protocol|13/14 MCP Apps on the Stateless Protocol]]
- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]
- [[Lessons/13-28 MCP Tool Contracts and Content|13/28 MCP Tool Contracts and Content]]

## Ships

- [[Artifacts/13-10 primitive-splitter|primitive-splitter]] `skill` — Review an MCP server design and separate tools, resources, prompts, caching, and subscriptions using the 2026-07-28 contract.

## Further reading

- [[Resources/MCP Subscriptions|MCP Subscriptions]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions)) ·  also cited by 1 other lesson
- MCP 2026-07-28 Caching ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/utilities/caching))
- [[Resources/MCP Prompts|MCP Prompts]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts)) ·  also cited by 1 other lesson
- [[Resources/MCP Resources|MCP Resources]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/resources)) ·  also cited by 1 other lesson

## In learning paths

- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]] — step 5, required


%% ── my notes ── %%
