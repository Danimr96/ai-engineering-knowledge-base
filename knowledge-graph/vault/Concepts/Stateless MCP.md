---
id: "concept:stateless-mcp"
type: concept
name: Stateless MCP
canonical: true
category: "Agents & tools"
taught_in: 3
community: 17
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/17
source: ai-engineering-from-scratch/glossary/terms.md
---

# Stateless MCP

**Community:** [[Communities/17 Tool Contract · Agent · Function Calling|17 Tool Contract · Agent · Function Calling]]

**What it actually means:** The MCP 2026-07-28 request model in which every request carries the protocol version and client capabilities in `params._meta`, while results carry an explicit `resultType`; no protocol state is keyed by an initialization handshake, connection, or `Mcp-Session-Id`.

**Why it matters:** Any worker can validate and process a request from its contents and authorization context, which avoids hidden connection affinity and makes horizontal routing easier to reason about.

**In practice:** Implement server/discover, rebuild request metadata on every call, validate transport headers against the JSON-RPC body, and pass server-minted application handles as ordinary tool arguments when continuity is required.

**Common confusion:** Stateless MCP removes protocol sessions, not application state, transport connections, streaming responses, tasks, or explicit handles.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Idempotency|Idempotency]]
- [[Concepts/MCP (Model Context Protocol)|MCP (Model Context Protocol)]]
- [[Concepts/Multi Round-Trip Request (MRTR)|Multi Round-Trip Request (MRTR)]]
- [[Concepts/Tool Contract|Tool Contract]]

## Taught in

- [[Lessons/11-14 Model Context Protocol (MCP)|11/14 Model Context Protocol (MCP)]] — Every request carries version and capabilities; no protocol state is keyed by a connection
- [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]]
- [[Lessons/19-13 Capstone 13- Stateless MCP Server with Registry and Governance|19/13 Capstone 13: Stateless MCP Server with Registry and Governance]] — No protocol session; cross-call state is explicit and server-managed

## Sources

- [[Resources/MCP Streamable HTTP|MCP Streamable HTTP]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http))
- [[Resources/MCP 2026-07-28 key changes|MCP 2026-07-28 key changes]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/changelog))


%% ── my notes ── %%
