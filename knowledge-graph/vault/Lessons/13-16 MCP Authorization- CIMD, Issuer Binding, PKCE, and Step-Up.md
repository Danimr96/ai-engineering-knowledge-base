---
id: "lesson:13/16"
type: lesson
ref: 13/16
phase: 13
num: 16
title: "MCP Authorization: CIMD, Issuer Binding, PKCE, and Step-Up"
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 10
prereqs: 2
community: 19
aliases:
  - 13/16
  - 13-16
tags:
  - phase/13
  - type/build
  - community/19
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/16-mcp-security-oauth-2-1/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/16-mcp-security-oauth-2-1"
---

# 13/16 MCP Authorization: CIMD, Issuer Binding, PKCE, and Step-Up

> A remote MCP request is stateless, but its authorization is not anonymous. Bind every credential to the issuer that created it and every token to the resource that receives it.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/16-mcp-security-oauth-2-1/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/16-mcp-security-oauth-2-1) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/16-mcp-security-oauth-2-1) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/19 CIMD · DCR · Resource indicator|19 CIMD · DCR · Resource indicator]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 09 (transports), Phase 13 · 15 (security)`

- [[Lessons/13-09 MCP Transports- stdio and Stateless Streamable HTTP|13/09 MCP Transports: stdio and Stateless Streamable HTTP]] — transports
- [[Lessons/13-15 MCP Security- Poisoned Metadata, Routing, and MRTR State|13/15 MCP Security: Poisoned Metadata, Routing, and MRTR State]] — security

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]], [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]]
- depth 3: [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]]

## Builds on this

- [[Lessons/13-17 Stateless MCP Gateways and Registry Admission|13/17 Stateless MCP Gateways and Registry Admission]]
- [[Lessons/13-18 MCP Auth in Production- Issuer-Bound Enrollment and Tokens|13/18 MCP Auth in Production: Issuer-Bound Enrollment and Tokens]]
- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]

## Concepts taught

- Protected-resource metadata `lesson term` — RFC 9728 document that identifies the resource and authorization servers
- [[Concepts/CIMD|CIMD]] `lesson term` — HTTPS metadata document whose URL is the OAuth client identifier
- [[Concepts/DCR|DCR]] `lesson term` — Deprecated dynamic client enrollment retained for compatibility
- application_type `lesson term` — native or web, used to validate redirect URI rules
- PKCE `lesson term` — Verifier and S256 challenge that protect an intercepted authorization code
- iss `lesson term` — RFC 9207 authorization response issuer identifier
- [[Concepts/Resource indicator|Resource indicator]] `lesson term` — RFC 8707 parameter that binds a token request to an MCP resource
- Audience `lesson term` — Resource for which a token is valid
- Step-up `lesson term` — New consent and token issuance for an additional current-operation scope
- Issuer-bound credentials `lesson term` — Registration and token records isolated by exact authorization server issuer

## Ships

- [[Artifacts/13-16 oauth-scope-planner|oauth-scope-planner]] `skill` — Design MCP 2026-07-28 authorization with CIMD, issuer isolation, resource indicators, and step-up scopes.

## Further reading

- OAuth Client ID Metadata Document draft ([link](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/))
- [[Resources/MCP 2026-07-28 authorization specification|MCP 2026-07-28 authorization specification]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)) ·  also cited by 2 other lessons
- RFC 8707: Resource Indicators for OAuth 2.0 ([link](https://www.rfc-editor.org/rfc/rfc8707))
- RFC 9207: OAuth 2.0 Authorization Server Issuer Identification ([link](https://www.rfc-editor.org/rfc/rfc9207))
- RFC 9728: OAuth 2.0 Protected Resource Metadata ([link](https://www.rfc-editor.org/rfc/rfc9728))

## In learning paths

- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]] — step 11, required


%% ── my notes ── %%
