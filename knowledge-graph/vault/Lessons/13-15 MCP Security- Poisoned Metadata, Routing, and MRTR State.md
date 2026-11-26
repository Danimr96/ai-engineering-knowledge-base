---
id: "lesson:13/15"
type: lesson
ref: 13/15
phase: 13
num: 15
title: "MCP Security: Poisoned Metadata, Routing, and MRTR State"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 2
concepts: 10
prereqs: 2
community: 10
aliases:
  - 13/15
  - 13-15
tags:
  - phase/13
  - type/learn
  - community/10
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/15-mcp-security-tool-poisoning/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/15-mcp-security-tool-poisoning"
---

# 13/15 MCP Security: Poisoned Metadata, Routing, and MRTR State

> Stateless does not mean trustless. It means every request exposes the evidence a server and gateway need to validate the call independently.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/15-mcp-security-tool-poisoning/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/15-mcp-security-tool-poisoning) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/15-mcp-security-tool-poisoning) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/10 Trace · Shadow Traffic · requestState|10 Trace · Shadow Traffic · requestState]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 07 (MCP server), Phase 13 · 08 (MCP client)`

- [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]] — MCP server
- [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]] — MCP client

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]], [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]]

## Builds on this

- [[Lessons/13-16 MCP Authorization- CIMD, Issuer Binding, PKCE, and Step-Up|13/16 MCP Authorization: CIMD, Issuer Binding, PKCE, and Step-Up]]
- [[Lessons/13-17 Stateless MCP Gateways and Registry Admission|13/17 Stateless MCP Gateways and Registry Admission]]
- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]
- [[Lessons/13-26 Skill Permissions, Sandboxes, and Trust|13/26 Skill Permissions, Sandboxes, and Trust]]

## Concepts taught

- Metadata poisoning `lesson term` — Instructions or deceptive claims embedded in a tool descriptor
- Rug pull `lesson term` — Change to a previously approved descriptor
- Tool shadowing `lesson term` — Ambiguous routing caused by duplicate unqualified names
- [[Concepts/Header mismatch|Header mismatch]] `lesson term` — Routing header and JSON-RPC body disagreement, error -32020
- Hash pin `lesson term` — Digest of the complete approved descriptor
- [[Concepts/Multi Round-Trip Request (MRTR)|Multi Round-Trip Request (MRTR)]] (as *MRTR*) `glossary` — Stateless response and retry pattern for server-requested input
- [[Concepts/requestState|requestState]] `lesson term` — Opaque round-trip value that must be treated as untrusted input
- Capability declaration `lesson term` — Statement of protocol compatibility, not authorization
- Implicit form support `lesson term` — An empty elicitation capability object, equivalent to form support
- [[Concepts/Qualified tool name|Qualified tool name]] `lesson term` — Stable gateway name such as notes.search

## Ships

- [[Artifacts/13-15 mcp-threat-model|mcp-threat-model]] `skill` — Threat-model an MCP 2026-07-28 deployment across metadata, routing, authorization, MRTR, and compatibility boundaries.

## Further reading

- [[Resources/Model Context Protocol — Specification 2026-07-28|Model Context Protocol — Specification 2026-07-28]] ([link](https://modelcontextprotocol.io/specification/2026-07-28)) ·  also cited by 5 other lessons
- [[Resources/MCP Multi Round-Trip Requests|MCP Multi Round-Trip Requests]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr)) ·  also cited by 4 other lessons
- [[Resources/MCP Streamable HTTP|MCP Streamable HTTP]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)) ·  also cited by 8 other lessons
- [[Resources/MCP deprecated features|MCP deprecated features]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)) ·  also cited by 1 other lesson

## In learning paths

- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]] — step 10, required


%% ── my notes ── %%
