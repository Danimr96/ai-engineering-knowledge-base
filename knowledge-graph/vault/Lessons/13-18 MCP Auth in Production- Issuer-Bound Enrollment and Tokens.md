---
id: "lesson:13/18"
type: lesson
ref: 13/18
phase: 13
num: 18
title: "MCP Auth in Production: Issuer-Bound Enrollment and Tokens"
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 14
prereqs: 2
community: 19
aliases:
  - 13/18
  - 13-18
tags:
  - phase/13
  - type/build
  - community/19
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/18-mcp-auth-production/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/18-mcp-auth-production"
---

# 13/18 MCP Auth in Production: Issuer-Bound Enrollment and Tokens

> Lesson 16 built the OAuth 2.1 state machine. This lesson hardens its production boundaries for MCP 2026-07-28: Client ID Metadata Documents first, deprecated dynamic registration only for compatibility, authorization-response issuer validation, issuer-keyed client credentials, JWKS refresh, and audience-pinned tokens on every stateless request.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/18-mcp-auth-production/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/18-mcp-auth-production) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/18-mcp-auth-production) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/19 CIMD · DCR · Resource indicator|19 CIMD · DCR · Resource indicator]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 16 (OAuth 2.1 state machine), Phase 13 · 17 (gateways)`

- [[Lessons/13-16 MCP Authorization- CIMD, Issuer Binding, PKCE, and Step-Up|13/16 MCP Authorization: CIMD, Issuer Binding, PKCE, and Step-Up]] — OAuth 2.1 state machine
- [[Lessons/13-17 Stateless MCP Gateways and Registry Admission|13/17 Stateless MCP Gateways and Registry Admission]] — gateways

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-09 MCP Transports- stdio and Stateless Streamable HTTP|13/09 MCP Transports: stdio and Stateless Streamable HTTP]], [[Lessons/13-15 MCP Security- Poisoned Metadata, Routing, and MRTR State|13/15 MCP Security: Poisoned Metadata, Routing, and MRTR State]]
- depth 3: [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]], [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]]

## Builds on this

- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]
- [[Lessons/13-30 MCP Registry Supply Chain- Admission, Drift, and Rollback|13/30 MCP Registry Supply Chain: Admission, Drift, and Rollback]]

## Concepts taught

- ASM `lesson term` — RFC 8414 /.well-known/oauth-authorization-server JSON
- [[Concepts/CIMD|CIMD]] `lesson term` — Client ID Metadata Document: an HTTPS URL used as the client_id; the AS pulls the JSON. Preferred enrollment in MCP 2026-07-28
- [[Concepts/DCR|DCR]] `lesson term` — RFC 7591 POST /register; deprecated for current MCP and retained only for compatibility
- JWKS `lesson term` — JSON Web Key Set, fetched from jwks_uri, indexed by kid
- Rotate vs refresh `lesson term` — Rotate = AS mints/retires signing keys; refresh = resource server re-fetches the published set. Resource servers only ever refresh
- [[Concepts/Resource indicator|Resource indicator]] `lesson term` — RFC 8707 resource parameter pinning the token to one server
- aud claim `lesson term` — JWT claim the validator compares against the canonical resource URL
- Audience replay `lesson term` — Token issued for Server A presented to Server B; defended by audience validation (spec: access-token privilege restriction)
- Confused deputy `lesson term` — An MCP proxy with a static client ID forwarding a token without per-client consent; distinct from audience replay
- Mix-up attack `lesson term` — Client steered to redeem an honest AS's code at an attacker's endpoint; defended client-side via RFC 9207 iss
- iss allow-list `lesson term` — The set named in protected-resource metadata's authorization_servers
- resource_metadata `lesson term` — WWW-Authenticate parameter naming the RFC 9728 metadata URL on a 401/403
- Public client `lesson term` — OAuth client with no client_secret; PKCE compensates
- WWW-Authenticate `lesson term` — Carries Bearer error=... directives that drive client recovery

## Ships

- [[Artifacts/13-18 mcp-auth-wiring|mcp-auth-wiring]] `skill` — Design MCP 2026-07-28 authorization with issuer-bound enrollment, CIMD, protected-resource metadata, JWKS refresh, audience pinning, and per-request validation.

## Further reading

- OAuth Client ID Metadata Document (draft-ietf-oauth-client-id-metadata-document-00) ([link](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-client-id-metadata-document-00)) — CIMD
- RFC 7009: OAuth 2.0 Token Revocation ([link](https://datatracker.ietf.org/doc/html/rfc7009))
- RFC 7591 — OAuth 2.0 Dynamic Client Registration Protocol ([link](https://datatracker.ietf.org/doc/html/rfc7591)) — DCR (fallback path)
- RFC 7636 — Proof Key for Code Exchange (PKCE) ([link](https://datatracker.ietf.org/doc/html/rfc7636)) — public-client proof-of-possession
- RFC 7662: OAuth 2.0 Token Introspection ([link](https://datatracker.ietf.org/doc/html/rfc7662))
- RFC 8414 — OAuth 2.0 Authorization Server Metadata ([link](https://datatracker.ietf.org/doc/html/rfc8414)) — discovery contract
- RFC 8707 — Resource Indicators for OAuth 2.0 ([link](https://datatracker.ietf.org/doc/html/rfc8707)) — audience pinning
- RFC 9207 — OAuth 2.0 Authorization Server Issuer Identification ([link](https://datatracker.ietf.org/doc/html/rfc9207)) — the `iss` parameter that defends against mix-up attacks
- RFC 9728 — OAuth 2.0 Protected Resource Metadata ([link](https://datatracker.ietf.org/doc/html/rfc9728)) — resource server discovery
- [[Resources/MCP 2026-07-28 authorization specification|MCP 2026-07-28 authorization specification]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)) — the current MCP authorization profile ·  also cited by 2 other lessons
- [[Resources/MCP 2026-07-28 key changes|MCP 2026-07-28 key changes]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/changelog)) — CIMD, issuer validation, DCR deprecation, and issuer-keyed credential changes ·  also cited by 6 other lessons

## In learning paths

- [[Paths/Model Context Protocol (MCP)|Model Context Protocol (MCP)]] — step 12, required


%% ── my notes ── %%
