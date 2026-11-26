---
id: "lesson:13/14"
type: lesson
ref: 13/14
phase: 13
num: 14
title: MCP Apps on the Stateless Protocol
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 2
concepts: 11
prereqs: 2
community: 10
aliases:
  - 13/14
  - 13-14
tags:
  - phase/13
  - type/build
  - community/10
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/14-mcp-apps/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/14-mcp-apps"
---

# 13/14 MCP Apps on the Stateless Protocol

> An interactive result is still an MCP tool and resource exchange. The 2026-07-28 core makes that exchange self-contained, while the Apps extension adds the sandboxed browser surface.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/14-mcp-apps/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/14-mcp-apps) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/14-mcp-apps) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/10 Trace · Shadow Traffic · requestState|10 Trace · Shadow Traffic · requestState]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 07 (MCP server), Phase 13 · 10 (resources)`

- [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]] — MCP server
- [[Lessons/13-10 MCP Resources and Prompts- Addressable Context for Stateless Servers|13/10 MCP Resources and Prompts: Addressable Context for Stateless Servers]] — resources

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]], [[Lessons/13-09 MCP Transports- stdio and Stateless Streamable HTTP|13/09 MCP Transports: stdio and Stateless Streamable HTTP]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]], [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]], [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]]

## Builds on this

- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]

## Concepts taught

- MCP Apps `lesson term` — Optional extension for interactive HTML rendered by an MCP host
- io.modelcontextprotocol/ui `lesson term` — Extension identifier advertised by both peers
- ui:// `lesson term` — Resource scheme for an App's UI template
- text/html;profile=mcp-app `lesson term` — MIME type for MCP App HTML
- [[Concepts/server-discover|server/discover]] `lesson term` — Current RPC for protocol and capability discovery
- resources/list `lesson term` — Mandatory resource listing method when the server advertises resources
- [[Concepts/resultType|resultType]] `lesson term` — Required discriminator for modern successful results
- ui/initialize `lesson term` — First Apps bridge request, separate from removed core initialization
- ui/notifications/initialized `lesson term` — Apps View readiness notification sent after the host responds
- CSP `lesson term` — Browser policy that restricts scripts, styles, images, and network origins
- Text fallback `lesson term` — Tool behavior retained for a host without Apps support

## Ships

- [[Artifacts/13-14 mcp-apps-spec|mcp-apps-spec]] `skill` — Design and review an MCP App contract on the stateless 2026-07-28 protocol.

## Further reading

- MCP Apps build guide ([link](https://modelcontextprotocol.io/extensions/apps/build))
- MCP Apps overview ([link](https://modelcontextprotocol.io/extensions/apps/overview))
- Official extension support matrix ([link](https://modelcontextprotocol.io/extensions/client-matrix))
- [[Resources/MCP Base Protocol|MCP Base Protocol]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic)) ·  also cited by 2 other lessons

## In learning paths

- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]] — step 9, required


%% ── my notes ── %%
