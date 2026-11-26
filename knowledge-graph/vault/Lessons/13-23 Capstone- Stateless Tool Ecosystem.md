---
id: "lesson:13/23"
type: lesson
ref: 13/23
phase: 13
num: 23
title: "Capstone: Stateless Tool Ecosystem"
lesson_type: build
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 6
code_files: 2
concepts: 6
prereqs: 22
community: 10
libraries:
  - build_catalog
  - install_skills
aliases:
  - 13/23
  - 13-23
tags:
  - phase/13
  - type/build
  - community/10
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/23-capstone-tool-ecosystem/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/23-capstone-tool-ecosystem"
---

# 13/23 Capstone: Stateless Tool Ecosystem

> A production agent system is a set of boundaries, not a pile of features. This capstone separates a readable in-process simulation from the protocol clients, authorization server, sandbox, and telemetry exporter a real deployment still needs.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/23-capstone-tool-ecosystem/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/23-capstone-tool-ecosystem) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/23-capstone-tool-ecosystem) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/10 Trace · Shadow Traffic · requestState|10 Trace · Shadow Traffic · requestState]] · **Libraries:** [[Libraries/build_catalog (python)|build_catalog]], [[Libraries/install_skills (python)|install_skills]]  

## Prerequisites

Stated upstream: `Phase 13 · 01 through 22, using MCP revision `2026-07-28``

- **13/01-22**:
    - [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]]
    - [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]]
    - [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]]
    - [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]]
    - [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]]
    - [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]]
    - [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]]
    - [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]]
    - [[Lessons/13-09 MCP Transports- stdio and Stateless Streamable HTTP|13/09 MCP Transports: stdio and Stateless Streamable HTTP]]
    - [[Lessons/13-10 MCP Resources and Prompts- Addressable Context for Stateless Servers|13/10 MCP Resources and Prompts: Addressable Context for Stateless Servers]]
    - [[Lessons/13-11 MCP Model Input- Sampling Migration and Stateless MRTR|13/11 MCP Model Input: Sampling Migration and Stateless MRTR]]
    - [[Lessons/13-12 Explicit Scope and Stateless Elicitation|13/12 Explicit Scope and Stateless Elicitation]]
    - [[Lessons/13-13 MCP Tasks Extension- Durable Work on a Stateless Core|13/13 MCP Tasks Extension: Durable Work on a Stateless Core]]
    - [[Lessons/13-14 MCP Apps on the Stateless Protocol|13/14 MCP Apps on the Stateless Protocol]]
    - [[Lessons/13-15 MCP Security- Poisoned Metadata, Routing, and MRTR State|13/15 MCP Security: Poisoned Metadata, Routing, and MRTR State]]
    - [[Lessons/13-16 MCP Authorization- CIMD, Issuer Binding, PKCE, and Step-Up|13/16 MCP Authorization: CIMD, Issuer Binding, PKCE, and Step-Up]]
    - [[Lessons/13-17 Stateless MCP Gateways and Registry Admission|13/17 Stateless MCP Gateways and Registry Admission]]
    - [[Lessons/13-18 MCP Auth in Production- Issuer-Bound Enrollment and Tokens|13/18 MCP Auth in Production: Issuer-Bound Enrollment and Tokens]]
    - [[Lessons/13-19 A2A — Agent-to-Agent Protocol|13/19 A2A — Agent-to-Agent Protocol]]
    - [[Lessons/13-20 OpenTelemetry GenAI — Tracing Tool Calls End-to-End|13/20 OpenTelemetry GenAI — Tracing Tool Calls End-to-End]]
    - [[Lessons/13-21 LLM Routing Layer — LiteLLM, OpenRouter, Portkey|13/21 LLM Routing Layer — LiteLLM, OpenRouter, Portkey]]
    - [[Lessons/13-22 Agent Skills- Portable Contract and Runtime Boundary|13/22 Agent Skills: Portable Contract and Runtime Boundary]]
- Not understood by the parser: `using MCP revision `2026-07-28``

## Concepts taught

- Capstone `lesson term` — A staged integration whose simulated and live boundaries remain explicit
- Protocol-shaped simulation `lesson term` — Local data and calls that resemble a protocol without implementing its wire contract
- [[Concepts/Tasks extension|Tasks extension]] `lesson term` — An optional io.modelcontextprotocol/tasks lifecycle with durable identity, polling, client input, final result, and cancellation semantics
- Opacity boundary `lesson term` — The caller sees the declared interface and artifacts, not private reasoning or internal state
- Runtime adapter `lesson term` — Host code that maps portable procedure to discovery, invocation, tools, policy, and context
- Integration evidence `lesson term` — A transcript, artifact, or receiver-side observation proving the real boundary was crossed

## Ships

- [[Artifacts/13-23 ecosystem-blueprint|ecosystem-blueprint]] `skill` — Produce a full Phase 13 ecosystem architecture given a product need; name primitives, security posture, telemetry, and packaging.

## Further reading

- [[Resources/a2a-protocol.org|a2a-protocol.org]] ([link](https://a2a-protocol.org/latest/)) — for Agent Cards, message delivery, tasks, artifacts, and transport bindings. ·  also cited by 2 other lessons
- [[Resources/Agent Skills specification|Agent Skills specification]] ([link](https://agentskills.io/specification)) — for the portable package contract used by the procedural layer. ·  also cited by 2 other lessons
- MCP Apps SDK ([link](https://github.com/modelcontextprotocol/ext-apps/blob/main/docs/overview.md)) — for `App` and `app.callServerTool`.
- [[Resources/Model Context Protocol — Specification 2026-07-28|Model Context Protocol — Specification 2026-07-28]] ([link](https://modelcontextprotocol.io/specification/2026-07-28)) — for stateless requests, discovery, tools, authorization, and transport behavior. ·  also cited by 5 other lessons
- [[Resources/MCP 2026-07-28 key changes|MCP 2026-07-28 key changes]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/changelog)) — for session removal, per-request metadata, MRTR, extensions, and deprecations. ·  also cited by 6 other lessons
- [[Resources/OpenTelemetry — GenAI semconv|OpenTelemetry — GenAI semconv]] ([link](https://opentelemetry.io/docs/specs/semconv/gen-ai/)) — for trace and attribute conventions. ·  also cited by 9 other lessons
- [[Resources/Official MCP Tasks extension|Official MCP Tasks extension]] ([link](https://tasks.extensions.modelcontextprotocol.io/specification/draft/tasks)) — for `tasks/get`, `tasks/update`, `tasks/cancel`, and final results carried by terminal tasks. ·  also cited by 3 other lessons

## In learning paths

- [[Paths/Agent Skills Engineering|Agent Skills Engineering]] — step None, optional
- [[Paths/Developer Experience and Education|Developer Experience and Education]] — step 10, required
- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]] — step None, optional


%% ── my notes ── %%
