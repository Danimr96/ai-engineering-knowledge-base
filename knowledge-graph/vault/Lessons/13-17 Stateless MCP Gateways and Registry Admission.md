---
id: "lesson:13/17"
type: lesson
ref: 13/17
phase: 13
num: 17
title: Stateless MCP Gateways and Registry Admission
lesson_type: learn
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 2
concepts: 9
prereqs: 2
community: 19
aliases:
  - 13/17
  - 13-17
tags:
  - phase/13
  - type/learn
  - community/19
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/17-mcp-gateways-and-registries/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/17-mcp-gateways-and-registries"
---

# 13/17 Stateless MCP Gateways and Registry Admission

> A gateway should make every route explicit. The 2026-07-28 protocol gives it method, name, version, capability, identity, cache, and trace boundaries without a transport session.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Learn · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/17-mcp-gateways-and-registries/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/17-mcp-gateways-and-registries) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/17-mcp-gateways-and-registries) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/19 CIMD · DCR · Resource indicator|19 CIMD · DCR · Resource indicator]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 15 (security), Phase 13 · 16 (authorization)`

- [[Lessons/13-15 MCP Security- Poisoned Metadata, Routing, and MRTR State|13/15 MCP Security: Poisoned Metadata, Routing, and MRTR State]] — security
- [[Lessons/13-16 MCP Authorization- CIMD, Issuer Binding, PKCE, and Step-Up|13/16 MCP Authorization: CIMD, Issuer Binding, PKCE, and Step-Up]] — authorization

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]], [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]], [[Lessons/13-09 MCP Transports- stdio and Stateless Streamable HTTP|13/09 MCP Transports: stdio and Stateless Streamable HTTP]]
- depth 3: [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]]

## Builds on this

- [[Lessons/13-18 MCP Auth in Production- Issuer-Bound Enrollment and Tokens|13/18 MCP Auth in Production: Issuer-Bound Enrollment and Tokens]]
- [[Lessons/13-21 LLM Routing Layer — LiteLLM, OpenRouter, Portkey|13/21 LLM Routing Layer — LiteLLM, OpenRouter, Portkey]]
- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]
- [[Lessons/13-30 MCP Registry Supply Chain- Admission, Drift, and Rollback|13/30 MCP Registry Supply Chain: Admission, Drift, and Rollback]]
- [[Lessons/13-31 MCP Conformance Engineering- Versioning, Evidence, and Operations|13/31 MCP Conformance Engineering: Versioning, Evidence, and Operations]]

## Concepts taught

- MCP gateway `lesson term` — Policy and routing server between clients and backend MCP servers
- Admission record `lesson term` — Evidence and policy decision allowing one backend into the gateway
- [[Concepts/Qualified tool name|Qualified tool name]] `lesson term` — Stable public route such as notes.search
- Descriptor pin `lesson term` — Approved digest checked during discovery and dispatch
- Private cache scope `lesson term` — Cached result restricted to one authorization context
- [[Concepts/Request-scoped SSE|Request-scoped SSE]] `lesson term` — Streaming response attached to one POST request
- [[Concepts/subscriptions-listen|subscriptions/listen]] `lesson term` — Client-opened SSE stream for selected long-lived change notifications
- Task route `lesson term` — Application mapping from an opaque task id to its backend
- Legacy adapter `lesson term` — Explicit version-gated boundary for old handshake and session behavior

## Ships

- [[Artifacts/13-17 gateway-bootstrap|gateway-bootstrap]] `skill` — Design a stateless MCP 2026-07-28 gateway with registry admission, policy, routing, and compatibility boundaries.

## Further reading

- [[Resources/Official Registry server.json requirements|Official Registry server.json requirements]] ([link](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/server-json/official-registry-requirements.md)) ·  also cited by 2 other lessons
- [[Resources/MCP Streamable HTTP|MCP Streamable HTTP]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)) ·  also cited by 8 other lessons
- [[Resources/MCP server discovery|MCP server discovery]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/discover)) ·  also cited by 8 other lessons
- [[Resources/Official MCP Tasks extension|Official MCP Tasks extension]] ([link](https://tasks.extensions.modelcontextprotocol.io/specification/draft/tasks)) ·  also cited by 3 other lessons

## In learning paths

- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]] — step 13, required


%% ── my notes ── %%
