---
id: "lesson:13/09"
type: lesson
ref: 13/09
phase: 13
num: 9
title: "MCP Transports: stdio and Stateless Streamable HTTP"
lesson_type: learn
languages:
  - Python
time_min: 65
on_route: false
quiz_count: 6
code_files: 2
concepts: 8
prereqs: 2
community: 10
aliases:
  - 13/09
  - 13-09
tags:
  - phase/13
  - type/learn
  - community/10
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/09-mcp-transports/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/09-mcp-transports"
---

# 13/09 MCP Transports: stdio and Stateless Streamable HTTP

> Transport carries MCP messages. It does not supply missing protocol state. In `2026-07-28`, local stdio and remote Streamable HTTP both carry self-describing requests.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Learn · **Time:** 65 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/09-mcp-transports/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/09-mcp-transports) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/09-mcp-transports) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/10 Trace · Shadow Traffic · requestState|10 Trace · Shadow Traffic · requestState]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13, Lessons 07 and 08`

- [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]]
- [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]], [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]]

## Builds on this

- [[Lessons/13-10 MCP Resources and Prompts- Addressable Context for Stateless Servers|13/10 MCP Resources and Prompts: Addressable Context for Stateless Servers]]
- [[Lessons/13-13 MCP Tasks Extension- Durable Work on a Stateless Core|13/13 MCP Tasks Extension: Durable Work on a Stateless Core]]
- [[Lessons/13-16 MCP Authorization- CIMD, Issuer Binding, PKCE, and Step-Up|13/16 MCP Authorization: CIMD, Issuer Binding, PKCE, and Step-Up]]
- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]
- [[Lessons/13-28 MCP Tool Contracts and Content|13/28 MCP Tool Contracts and Content]]
- [[Lessons/13-29 MCP Reliability, Cancellation, and Flow Control|13/29 MCP Reliability, Cancellation, and Flow Control]]
- [[Lessons/13-31 MCP Conformance Engineering- Versioning, Evidence, and Operations|13/31 MCP Conformance Engineering: Versioning, Evidence, and Operations]]

## Concepts taught

- stdio `lesson term` — Newline-delimited JSON-RPC over a client-launched subprocess
- [[Concepts/Streamable HTTP|Streamable HTTP]] `lesson term` — Single endpoint where each modern message is a new POST
- [[Concepts/Request-scoped SSE|Request-scoped SSE]] `lesson term` — POST response stream containing related notifications and final response
- [[Concepts/subscriptions-listen|subscriptions/listen]] `lesson term` — Long-lived POST request for opted-in change notifications
- [[Concepts/Header mismatch|Header mismatch]] `lesson term` — HTTP 400 and JSON-RPC -32020 when mirrored headers disagree with body
- Origin validation `lesson term` — DNS-rebinding defense for incoming connections, not authentication
- Explicit state handle `lesson term` — Application token passed as an ordinary argument instead of hidden session state
- Legacy bridge `lesson term` — Separate earlier-era behavior kept only for compatibility

## Ships

- [[Artifacts/13-09 mcp-transport-migrator|mcp-transport-migrator]] `skill` — Migrate legacy MCP HTTP transports to the stateless, POST-only 2026-07-28 contract.

## Further reading

- [[Resources/MCP Subscriptions|MCP Subscriptions]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions)) ·  also cited by 1 other lesson
- MCP Transport Overview ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports))
- [[Resources/MCP stdio Transport|MCP stdio Transport]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio)) ·  also cited by 2 other lessons
- [[Resources/MCP Streamable HTTP|MCP Streamable HTTP]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)) ·  also cited by 8 other lessons
- [[Resources/MCP 2026-07-28 key changes|MCP 2026-07-28 key changes]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/changelog)) ·  also cited by 6 other lessons

## In learning paths

- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]] — step 4, required


%% ── my notes ── %%
