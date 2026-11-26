---
id: "lesson:13/11"
type: lesson
ref: 13/11
phase: 13
num: 11
title: "MCP Model Input: Sampling Migration and Stateless MRTR"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 2
concepts: 10
prereqs: 2
community: 10
aliases:
  - 13/11
  - 13-11
tags:
  - phase/13
  - type/build
  - community/10
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/11-mcp-sampling/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/11-mcp-sampling"
---

# 13/11 MCP Model Input: Sampling Migration and Stateless MRTR

> MCP 2026-07-28 deprecates Sampling for new designs and removes the server-to-client request channel. If an existing workflow still needs the client's model, the server returns an `input_required` result and the client retries the original request with the model output. The reasoning loop becomes explicit, bounded, and stateless at the protocol layer.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/11-mcp-sampling/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/11-mcp-sampling) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/11-mcp-sampling) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/10 Trace · Shadow Traffic · requestState|10 Trace · Shadow Traffic · requestState]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 07 (MCP server), Phase 13 · 10 (resources and prompts)`

- [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]] — MCP server
- [[Lessons/13-10 MCP Resources and Prompts- Addressable Context for Stateless Servers|13/10 MCP Resources and Prompts: Addressable Context for Stateless Servers]] — resources and prompts

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]], [[Lessons/13-09 MCP Transports- stdio and Stateless Streamable HTTP|13/09 MCP Transports: stdio and Stateless Streamable HTTP]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]], [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]], [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]]

## Builds on this

- [[Lessons/13-12 Explicit Scope and Stateless Elicitation|13/12 Explicit Scope and Stateless Elicitation]]
- [[Lessons/13-13 MCP Tasks Extension- Durable Work on a Stateless Core|13/13 MCP Tasks Extension: Durable Work on a Stateless Core]]
- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]

## Concepts taught

- [[Concepts/Sampling|Sampling]] `lesson term` — Deprecated feature that asks the client's model for a completion
- [[Concepts/Multi Round-Trip Request (MRTR)|Multi Round-Trip Request (MRTR)]] (as *MRTR*) `glossary` — Stateless retry pattern for client input required during a request
- InputRequiredResult `lesson term` — Result with resultType: "input_required"
- inputRequests `lesson term` — Server-assigned map of embedded elicitation, sampling, or roots requests
- inputResponses `lesson term` — Current round's client results keyed like inputRequests
- [[Concepts/requestState|requestState]] `lesson term` — Opaque server state echoed exactly by the client and verified by the server
- [[Concepts/resultType|resultType]] `lesson term` — Required discriminator for modern MCP results
- Direct model integration `lesson term` — Recommended replacement for new servers that need model inference
- Capability gate `lesson term` — Rule that prevents sending an embedded request the client did not advertise
- Loop budget `lesson term` — Maximum rounds, tokens, bytes, time, and spend allowed for the operation

## Ships

- [[Artifacts/13-11 sampling-loop-designer|sampling-loop-designer]] `skill` — Migrate model-assisted MCP tools to direct inference or stateless 2026-07-28 MRTR with bounded compatibility sampling.

## Further reading

- MCP Sampling deprecation ([link](https://modelcontextprotocol.io/seps/2577-deprecate-roots-sampling-and-logging))
- [[Resources/MCP Multi Round-Trip Requests|MCP Multi Round-Trip Requests]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr)) ·  also cited by 4 other lessons
- [[Resources/MCP 2026-07-28 key changes|MCP 2026-07-28 key changes]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/changelog)) ·  also cited by 6 other lessons
- [[Resources/MCP server discovery|MCP server discovery]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/discover)) ·  also cited by 8 other lessons

## In learning paths

- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]] — step 6, required


%% ── my notes ── %%
