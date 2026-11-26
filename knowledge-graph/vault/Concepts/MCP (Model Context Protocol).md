---
id: "concept:mcp-model-context-protocol"
type: concept
name: MCP (Model Context Protocol)
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

# MCP (Model Context Protocol)

**Community:** [[Communities/17 Tool Contract · Agent · Function Calling|17 Tool Contract · Agent · Function Calling]]

> *What people say:* A standard way for AI applications to connect to tools and context.

**What it actually means:** An open JSON-RPC protocol for a host to connect to servers that expose tools, resources, prompts, and extensions through defined request, result, discovery, and transport contracts. In revision 2026-07-28, every request carries its protocol version and client capabilities instead of relying on an initialization handshake or protocol session.

**Common confusion:** MCP standardizes discovery and exchange. It does not decide which tool is safe to call, grant permission, or forbid an application from using explicit state handles.

**Category:** [[Categories/Agents & tools|Agents & tools]]

## Related concepts

- [[Concepts/Agent Skill|Agent Skill]]
- [[Concepts/Function Calling|Function Calling]]
- [[Concepts/Least Privilege|Least Privilege]]
- [[Concepts/Multi Round-Trip Request (MRTR)|Multi Round-Trip Request (MRTR)]]
- [[Concepts/Stateless MCP|Stateless MCP]]
- [[Concepts/Tool Contract|Tool Contract]]

## Taught in

- [[Lessons/11-09 Function Calling & Tool Use|11/09 Function Calling & Tool Use]] `alias` — Model Context Protocol -- Anthropic's open standard for exposing tools via servers that any compatible client can discover and call
- [[Lessons/11-14 Model Context Protocol (MCP)|11/14 Model Context Protocol (MCP)]] — JSON-RPC protocol for server discovery, tools, resources, prompts, and extensions
- [[Lessons/16-03 Communication Protocols|16/03 Communication Protocols]] `alias` — A client-server protocol for agents to discover and use tools. Agent-to-tool, not agent-to-agent.

## Sources

- [[Resources/MCP 2026-07-28 key changes|MCP 2026-07-28 key changes]] ([link](https://modelcontextprotocol.io/specification/2026-07-28/changelog))


%% ── my notes ── %%
