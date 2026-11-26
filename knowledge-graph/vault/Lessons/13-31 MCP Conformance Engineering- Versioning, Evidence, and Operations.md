---
id: "lesson:13/31"
type: lesson
ref: 13/31
phase: 13
num: 31
title: "MCP Conformance Engineering: Versioning, Evidence, and Operations"
lesson_type: build
languages:
  - Python
time_min: 100
on_route: false
quiz_count: 6
code_files: 2
concepts: 0
prereqs: 3
community: 19
aliases:
  - 13/31
  - 13-31
tags:
  - phase/13
  - type/build
  - community/19
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/31-mcp-conformance-versioning-and-operations/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/31-mcp-conformance-versioning-and-operations"
---

# 13/31 MCP Conformance Engineering: Versioning, Evidence, and Operations

> A server is not conformant because its happy path worked through one SDK. Conformance lives at the wire, at version boundaries, through intermediaries, and during rollback.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 100 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/31-mcp-conformance-versioning-and-operations/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/31-mcp-conformance-versioning-and-operations) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/31-mcp-conformance-versioning-and-operations) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/19 CIMD · DCR · Resource indicator|19 CIMD · DCR · Resource indicator]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 09 (transports), Phase 13 · 17 (gateways), Phase 13 · 30 (registry admission)`

- [[Lessons/13-09 MCP Transports- stdio and Stateless Streamable HTTP|13/09 MCP Transports: stdio and Stateless Streamable HTTP]] — transports
- [[Lessons/13-17 Stateless MCP Gateways and Registry Admission|13/17 Stateless MCP Gateways and Registry Admission]] — gateways
- [[Lessons/13-30 MCP Registry Supply Chain- Admission, Drift, and Rollback|13/30 MCP Registry Supply Chain: Admission, Drift, and Rollback]] — registry admission

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]], [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]], [[Lessons/13-15 MCP Security- Poisoned Metadata, Routing, and MRTR State|13/15 MCP Security: Poisoned Metadata, Routing, and MRTR State]], [[Lessons/13-16 MCP Authorization- CIMD, Issuer Binding, PKCE, and Step-Up|13/16 MCP Authorization: CIMD, Issuer Binding, PKCE, and Step-Up]], [[Lessons/13-18 MCP Auth in Production- Issuer-Bound Enrollment and Tokens|13/18 MCP Auth in Production: Issuer-Bound Enrollment and Tokens]]
- depth 3: [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]]

## Ships

- [[Artifacts/13-31 mcp-conformance-release-gate|mcp-conformance-release-gate]] `skill` — Build an MCP conformance matrix and evidence-backed promote, hold, or rollback decision.

## Further reading

- Official MCP conformance project ([link](https://github.com/modelcontextprotocol/conformance))
- [[Resources/MCP Base Protocol|MCP Base Protocol]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic)) ·  also cited by 2 other lessons
- [[Resources/MCP Streamable HTTP|MCP Streamable HTTP]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)) ·  also cited by 8 other lessons
- [[Resources/MCP Versioning|MCP Versioning]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning)) ·  also cited by 1 other lesson

## In learning paths

- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]] — step 17, required


%% ── my notes ── %%
