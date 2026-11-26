---
id: "lesson:13/30"
type: lesson
ref: 13/30
phase: 13
num: 30
title: "MCP Registry Supply Chain: Admission, Drift, and Rollback"
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 0
prereqs: 2
community: 19
aliases:
  - 13/30
  - 13-30
tags:
  - phase/13
  - type/build
  - community/19
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/30-mcp-registry-supply-chain-and-drift/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/30-mcp-registry-supply-chain-and-drift"
---

# 13/30 MCP Registry Supply Chain: Admission, Drift, and Rollback

> A registry entry tells you what a publisher declared. Production admission proves what you fetched, what you observed, what you approved, and what you can safely restore.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/30-mcp-registry-supply-chain-and-drift/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/30-mcp-registry-supply-chain-and-drift) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/30-mcp-registry-supply-chain-and-drift) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/19 CIMD · DCR · Resource indicator|19 CIMD · DCR · Resource indicator]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 17 (gateways and registries), Phase 13 · 18 (production authentication)`

- [[Lessons/13-17 Stateless MCP Gateways and Registry Admission|13/17 Stateless MCP Gateways and Registry Admission]] — gateways and registries
- [[Lessons/13-18 MCP Auth in Production- Issuer-Bound Enrollment and Tokens|13/18 MCP Auth in Production: Issuer-Bound Enrollment and Tokens]] — production authentication

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-15 MCP Security- Poisoned Metadata, Routing, and MRTR State|13/15 MCP Security: Poisoned Metadata, Routing, and MRTR State]], [[Lessons/13-16 MCP Authorization- CIMD, Issuer Binding, PKCE, and Step-Up|13/16 MCP Authorization: CIMD, Issuer Binding, PKCE, and Step-Up]]
- depth 3: [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]], [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]], [[Lessons/13-09 MCP Transports- stdio and Stateless Streamable HTTP|13/09 MCP Transports: stdio and Stateless Streamable HTTP]]

## Builds on this

- [[Lessons/13-31 MCP Conformance Engineering- Versioning, Evidence, and Operations|13/31 MCP Conformance Engineering: Versioning, Evidence, and Operations]]

## Ships

- [[Artifacts/13-30 mcp-registry-admission|mcp-registry-admission]] `skill` — Admit, pin, monitor, quarantine, and roll back an MCP Registry release with supply chain evidence.

## Further reading

- [[Resources/Official Registry server.json requirements|Official Registry server.json requirements]] ([link](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/server-json/official-registry-requirements.md)) ·  also cited by 2 other lessons
- [[Resources/MCP server discovery|MCP server discovery]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/discover)) ·  also cited by 8 other lessons
- [[Resources/Official Registry OpenAPI contract|Official Registry OpenAPI contract]] ([link](https://registry.modelcontextprotocol.io/openapi.yaml)) ·  also cited by 1 other lesson

## In learning paths

- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]] — step 16, required


%% ── my notes ── %%
