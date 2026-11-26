---
id: "lesson:13/12"
type: lesson
ref: 13/12
phase: 13
num: 12
title: Explicit Scope and Stateless Elicitation
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 2
concepts: 11
prereqs: 2
community: 10
aliases:
  - 13/12
  - 13-12
tags:
  - phase/13
  - type/build
  - community/10
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/12-mcp-roots-and-elicitation/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/12-mcp-roots-and-elicitation"
---

# 13/12 Explicit Scope and Stateless Elicitation

> Roots are deprecated in MCP 2026-07-28 and were never a security sandbox. Put scope in visible tool arguments or resource URIs, authorize it on the server, and use MRTR when a tool genuinely needs user input. The user sees the decision, the model sees the handle, and any server instance can process the retry.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/12-mcp-roots-and-elicitation/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/12-mcp-roots-and-elicitation) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/12-mcp-roots-and-elicitation) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/10 Trace · Shadow Traffic · requestState|10 Trace · Shadow Traffic · requestState]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 07 (MCP server), Phase 13 · 11 (stateless MRTR)`

- [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]] — MCP server
- [[Lessons/13-11 MCP Model Input- Sampling Migration and Stateless MRTR|13/11 MCP Model Input: Sampling Migration and Stateless MRTR]] — stateless MRTR

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]], [[Lessons/13-10 MCP Resources and Prompts- Addressable Context for Stateless Servers|13/10 MCP Resources and Prompts: Addressable Context for Stateless Servers]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]], [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]], [[Lessons/13-09 MCP Transports- stdio and Stateless Streamable HTTP|13/09 MCP Transports: stdio and Stateless Streamable HTTP]]

## Builds on this

- [[Lessons/13-13 MCP Tasks Extension- Durable Work on a Stateless Core|13/13 MCP Tasks Extension: Durable Work on a Stateless Core]]
- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]

## Concepts taught

- Roots `lesson term` — Deprecated informational workspace hints, not authorization or sandboxing
- Explicit scope `lesson term` — Workspace, directory, or resource handle visible in request arguments
- Containment `lesson term` — Normalized path-component check that keeps a target inside a boundary
- Elicitation `lesson term` — Client feature for obtaining user input during an MCP operation
- Form mode `lesson term` — In-band structured user input using a restricted flat schema
- URL mode `lesson term` — Out-of-band interaction for sensitive or external workflows
- [[Concepts/Multi Round-Trip Request (MRTR)|Multi Round-Trip Request (MRTR)]] (as *MRTR*) `glossary` — Stateless input-required result followed by a fresh retry
- [[Concepts/requestState|requestState]] `lesson term` — Opaque state echoed exactly and integrity-checked by the server
- Decline `lesson term` — Explicit user refusal
- Cancel `lesson term` — Dismissal or incomplete interaction without approval

## Ships

- [[Artifacts/13-12 elicitation-form-designer|elicitation-form-designer]] `skill` — Design explicit resource scope and stateless MCP 2026-07-28 elicitation with authorization, safe forms, and signed retry state.

## Further reading

- [[Resources/MCP Multi Round-Trip Requests|MCP Multi Round-Trip Requests]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr)) ·  also cited by 4 other lessons
- MCP 2026-07-28 Elicitation ([link](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation))
- MCP 2026-07-28 Roots deprecation ([link](https://modelcontextprotocol.io/specification/2026-07-28/client/roots))
- [[Resources/MCP server discovery|MCP server discovery]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/discover)) ·  also cited by 8 other lessons

## In learning paths

- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]] — step 7, required


%% ── my notes ── %%
