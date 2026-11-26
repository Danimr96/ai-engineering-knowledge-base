---
id: "lesson:19/13"
type: lesson
ref: 19/13
phase: 19
num: 13
title: "Capstone 13: Stateless MCP Server with Registry and Governance"
lesson_type: capstone
languages:
  - Python
  - "TypeScript reference models; any production language"
time_min: 1500
on_route: false
quiz_count: 6
code_files: 8
concepts: 7
prereqs: 0
community: 10
aliases:
  - 19/13
  - 19-13
tags:
  - phase/19
  - type/capstone
  - community/10
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/13-mcp-server-with-registry/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/13-mcp-server-with-registry"
---

# 19/13 Capstone 13: Stateless MCP Server with Registry and Governance

> Production MCP is not one server process. It is a chain of contracts: publishable metadata, live discovery, a stateless request envelope, authorization, policy, audit, and deployment evidence.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Capstone · **Time:** 1500 min · **Languages:** Python, TypeScript reference models; any production language · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/13-mcp-server-with-registry/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/13-mcp-server-with-registry) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/13-mcp-server-with-registry) · code: main.py, tests/test_main.py, ts/src/index.ts, ts/src/protocol.ts, ts/src/tools.ts, ts/src/transport.ts … · quiz: 6 questions  
**Community:** [[Communities/10 Trace · Shadow Traffic · requestState|10 Trace · Shadow Traffic · requestState]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 11, Phase 13, Phase 14, Phase 17, and Phase 18`

- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] ·  medium confidence
- Whole phase: [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] ·  medium confidence
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] ·  medium confidence
- Whole phase: [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] ·  medium confidence
- Whole phase: [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] ·  medium confidence

## Concepts taught

- [[Concepts/Stateless MCP|Stateless MCP]] `glossary` — No protocol session; cross-call state is explicit and server-managed
- server.json `lesson term` — Registry metadata for naming, packaging, configuration, and transports
- [[Concepts/server-discover|server/discover]] `lesson term` — A normal mandatory RPC for live versions and capabilities, not a session initializer
- Cache scope `lesson term` — Whether a cacheable result is safe for shared or private reuse
- Policy decision `lesson term` — A separate decision over actor, tool, target, arguments, and context
- Approval record `lesson term` — Evidence bound to one actor and consequential action under an expiry policy
- Explicit handle `lesson term` — Ordinary application data for named server-managed state, not protocol connection state

## Ships

- [[Artifacts/19-13 mcp-server-platform|mcp-server-platform]] `skill` — Design a stateless MCP 2026-07-28 server with registry metadata, live discovery, authorization, policy, audit, and scale evidence.

## Further reading

- [[Resources/Official Registry server.json requirements|Official Registry server.json requirements]] ([link](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/server-json/official-registry-requirements.md)) ·  also cited by 2 other lessons
- [[Resources/MCP 2026-07-28 authorization specification|MCP 2026-07-28 authorization specification]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)) ·  also cited by 2 other lessons
- [[Resources/MCP Streamable HTTP|MCP Streamable HTTP]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)) ·  also cited by 8 other lessons
- [[Resources/MCP 2026-07-28 key changes|MCP 2026-07-28 key changes]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/changelog)) ·  also cited by 6 other lessons
- [[Resources/MCP server discovery|MCP server discovery]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/server/discover)) ·  also cited by 8 other lessons
- [[Resources/Official Registry OpenAPI contract|Official Registry OpenAPI contract]] ([link](https://registry.modelcontextprotocol.io/openapi.yaml)) ·  also cited by 1 other lesson


%% ── my notes ── %%
