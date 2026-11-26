---
id: "lesson:16/03"
type: lesson
ref: 16/03
phase: 16
num: 3
title: Communication Protocols
lesson_type: build
languages:
  - TypeScript
time_min: 120
on_route: false
quiz_count: 5
code_files: 1
concepts: 9
prereqs: 1
community: 6
aliases:
  - 16/03
  - 16-03
tags:
  - phase/16
  - type/build
  - community/06
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/03-communication-protocols/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/03-communication-protocols"
---

# 16/03 Communication Protocols

> Agents that can't speak the same language aren't a team. They're strangers shouting into the void.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Build · **Time:** 120 min · **Languages:** TypeScript · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/03-communication-protocols/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/03-communication-protocols) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/03-communication-protocols) · code: main.ts · quiz: 5 questions  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]]  

## Prerequisites

Stated upstream: `Phase 14 (Agent Engineering), Lesson 16.01 (Why Multi-Agent)`

- [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]] — Why Multi-Agent
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — Agent Engineering ·  medium confidence

## Builds on this

- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- [[Concepts/MCP (Model Context Protocol)|MCP (Model Context Protocol)]] (as *MCP*) `glossary` — A client-server protocol for agents to discover and use tools. Agent-to-tool, not agent-to-agent.
- [[Concepts/A2A|A2A]] `lesson term` — A peer-to-peer protocol for agent collaboration under the Linux Foundation. Discovery via Agent Cards, 9-state task lifecycle, streaming via SSE. Supports JSON-RPC, REST, and gRPC bindings.
- ACP `lesson term` — IBM/BeeAI's REST API for agent runs with TrajectoryMetadata: every response carries the full chain of reasoning and tool calls. Merging into A2A.
- ANP `lesson term` — A community protocol using did:wba (DID) for cryptographic identity, HPKE for E2EE, and AI-powered meta-protocol negotiation for agents that have never seen each other.
- [[Concepts/Agent Card|Agent Card]] `lesson term` — A JSON document at /.well-known/agent-card.json describing skills, supported MIME types, security schemes, and protocol bindings.
- [[Concepts/DID|DID]] `lesson term` — W3C standard for cryptographically verifiable identities hosted on the agent's own domain. ANP uses did:wba method.
- TrajectoryMetadata `lesson term` — ACP's mechanism for attaching reasoning steps, tool calls, and their inputs/outputs to every agent response.
- Meta-protocol `lesson term` — ANP's approach where agents use natural language to dynamically agree on data formats, then generate code to handle them.
- [[Concepts/Task|Task]] `lesson term` — A2A's stateful object tracking work from submission through completion. Immutable once terminal.

## Ships

- [[Artifacts/16-03 prompt-protocol-selector|prompt-protocol-selector]] `prompt` — Helps choose the right agent communication protocol (MCP, A2A, ACP, ANP) based on system requirements

## Further reading

- FIPA Agent Communication Language ([link](http://www.fipa.org/specs/fipa00061/SC00061G.html)) — the academic precursor to modern agent protocols
- Agent Network Protocol ([link](https://github.com/agent-network-protocol/AgentNetworkProtocol)) — DID-based identity, E2EE, meta-protocol negotiation
- Google A2A specification ([link](https://github.com/google/A2A)) — official spec and SDKs (v1.0.0, Linux Foundation)
- IBM/BeeAI ACP specification ([link](https://github.com/i-am-bee/acp)) — OpenAPI 3.1 spec for agent runs and trajectory metadata
- [[Resources/Model Context Protocol Specification|Model Context Protocol Specification]] ([link](https://modelcontextprotocol.io)) — Anthropic's MCP specification (covered in Phase 13) ·  also cited by 1 other lesson
- RFC 9180 (HPKE) ([link](https://www.rfc-editor.org/rfc/rfc9180)) — the encryption scheme ANP uses for E2EE
- [[Resources/W3C Decentralized Identifiers|W3C Decentralized Identifiers]] ([link](https://www.w3.org/TR/did-core/)) — the identity standard underpinning ANP ·  also cited by 1 other lesson


%% ── my notes ── %%
