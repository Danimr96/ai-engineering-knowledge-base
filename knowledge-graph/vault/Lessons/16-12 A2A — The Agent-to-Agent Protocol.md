---
id: "lesson:16/12"
type: lesson
ref: 16/12
phase: 16
num: 12
title: "A2A — The Agent-to-Agent Protocol"
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 1
aliases:
  - 16/12
  - 16-12
tags:
  - phase/16
  - type/learn+build
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/12-a2a-protocol/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/12-a2a-protocol"
---

# 16/12 A2A — The Agent-to-Agent Protocol

> Google announced A2A in April 2025; by April 2026 the spec is at https://a2a-protocol.org/latest/specification/ and 150+ organizations back it. A2A is the horizontal complement to MCP (Lesson 13): where MCP is vertical (agent ↔ tools), A2A is peer-to-peer (agent ↔ agent). It defines Agent Cards (discovery), tasks with artifacts (text, structured data, video), opaque task lifecycles, and auth. Production systems increasingly pair MCP with A2A. Google Cloud rolled A2A support into Vertex AI Agent Builder during 2025-2026.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/12-a2a-protocol/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/12-a2a-protocol) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/12-a2a-protocol) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 04 (Primitive Model)`

- [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]] — Primitive Model

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]]

## Builds on this

- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- [[Concepts/A2A|A2A]] `lesson term` — Peer protocol for agents to call other agents across systems. Google 2025.
- [[Concepts/Agent Card|Agent Card]] `lesson term` — JSON at /.well-known/agent.json describing skills, endpoints, auth.
- [[Concepts/Task|Task]] `lesson term` — Async stateful object with a lifecycle; artifacts produced on completion.
- [[Concepts/Artifact|Artifact]] `lesson term` — Typed output: text, structured JSON, image, video, audio. First-class media.
- Opaque lifecycle `lesson term` — Client sees state transitions; server is free to choose framework/tools.
- Discovery `lesson term` — GET /.well-known/agent.json returns the card.
- MCP vs A2A `lesson term` — MCP: vertical agent ↔ tool. A2A: horizontal agent ↔ agent.
- ACP / ANP / NLIP `lesson term` — Adjacent specs; A2A is the most-adopted 2026.

## Ships

- [[Artifacts/16-12 a2a-integrator|a2a-integrator]] `skill` — Design an A2A integration between two agents — Agent Card, task schemas, auth, streaming or polling.

## Further reading

- [[Resources/A2A specification|A2A specification]] ([link](https://a2a-protocol.org/latest/specification/)) — the canonical spec ·  also cited by 1 other lesson
- [[Resources/Liu et al. — A Survey of Agent Interoperability Protocols- MCP, ACP, A2A, ANP|Liu et al. — A Survey of Agent Interoperability Protocols: MCP, ACP, A2A, ANP]] ([link](https://arxiv.org/html/2505.02279v1)) — MCP, ACP, A2A, ANP comparison ·  also cited by 1 other lesson
- Google Developers Blog — A2A announcement ([link](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)) — April 2025 launch post
- [[Resources/a2aproject-A2A — GitHub|a2aproject/A2A — GitHub]] ([link](https://github.com/a2aproject/A2A)) — reference implementations and SDKs ·  also cited by 1 other lesson


%% ── my notes ── %%
