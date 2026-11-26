---
id: "concept:multi-round-trip-request-mrtr"
type: concept
name: Multi Round-Trip Request (MRTR)
canonical: true
category: "Agents & tools"
aliases:
  - MRTR
taught_in: 4
community: 17
tags:
  - concept/glossary
  - category/agents-and-tools
  - community/17
source: ai-engineering-from-scratch/glossary/terms.md
---

# Multi Round-Trip Request (MRTR)

**Community:** [[Communities/17 Tool Contract · Agent · Function Calling|17 Tool Contract · Agent · Function Calling]]

**What it actually means:** An MCP request pattern in which an operation returns `resultType: input_required` with one or more `inputRequests`, then the client retries the original method with `inputResponses` and the exact returned `requestState`.

**Why it matters:** It lets a stateless server request user, model, or root input without opening a server-initiated JSON-RPC exchange or storing protocol session state.

**In practice:** Return an input request from tools/call, collect the authorized response in the host, and retry that same tool call with a new JSON-RPC id.

**Common confusion:** requestState is untrusted round-trip data. Integrity-protect it before using it for authorization or business decisions, and do not treat it as a server-side session identifier.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Human-in-the-Loop (HITL)|Human-in-the-Loop (HITL)]]
- [[Concepts/MCP (Model Context Protocol)|MCP (Model Context Protocol)]]
- [[Concepts/Stateless MCP|Stateless MCP]]
- [[Concepts/Tool Contract|Tool Contract]]

## Taught in

- [[Lessons/11-14 Model Context Protocol (MCP)|11/14 Model Context Protocol (MCP)]] `alias` — Input request embedded in a result, followed by a retry of the original operation
- [[Lessons/13-11 MCP Model Input- Sampling Migration and Stateless MRTR|13/11 MCP Model Input: Sampling Migration and Stateless MRTR]] `alias` — Stateless retry pattern for client input required during a request
- [[Lessons/13-12 Explicit Scope and Stateless Elicitation|13/12 Explicit Scope and Stateless Elicitation]] — Stateless input-required result followed by a fresh retry
- [[Lessons/13-15 MCP Security- Poisoned Metadata, Routing, and MRTR State|13/15 MCP Security: Poisoned Metadata, Routing, and MRTR State]] `alias` — Stateless response and retry pattern for server-requested input

## Sources

- [[Resources/MCP Multi Round-Trip Requests|MCP Multi Round-Trip Requests]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr))


%% ── my notes ── %%
