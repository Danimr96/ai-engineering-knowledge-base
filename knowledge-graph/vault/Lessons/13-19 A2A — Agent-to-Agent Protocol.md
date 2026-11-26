---
id: "lesson:13/19"
type: lesson
ref: 13/19
phase: 13
num: 19
title: "A2A — Agent-to-Agent Protocol"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 2
concepts: 10
prereqs: 2
community: 51
aliases:
  - 13/19
  - 13-19
tags:
  - phase/13
  - type/build
  - community/51
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/19-a2a-protocol/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/19-a2a-protocol"
---

# 13/19 A2A — Agent-to-Agent Protocol

> MCP is agent-to-tool. A2A (Agent2Agent) is agent-to-agent — an open protocol for letting opaque agents built on different frameworks collaborate. Released by Google in April 2025, donated to the Linux Foundation in June 2025, reaching v1.0 in April 2026 with 150+ supporters including AWS, Cisco, Microsoft, Salesforce, SAP, and ServiceNow. It absorbed IBM's ACP and added the AP2 payments extension. This lesson walks the Agent Card, Task lifecycle, and the two transport bindings.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/19-a2a-protocol/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/19-a2a-protocol) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/19-a2a-protocol) · code: main.py, main.ts  
**Community:** [[Communities/51 A2A · Message · Skill|51 A2A · Message · Skill]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 06 (MCP fundamentals), Phase 13 · 08 (MCP client)`

- [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]] — MCP fundamentals
- [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]] — MCP client

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]], [[Lessons/13-03 Parallel Tool Calls and Streaming with Tools|13/03 Parallel Tool Calls and Streaming with Tools]], [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]], [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]]

## Builds on this

- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]

## Concepts taught

- [[Concepts/A2A|A2A]] `lesson term` — Open protocol for opaque agent collaboration
- [[Concepts/Agent Card|Agent Card]] `lesson term` — Published metadata describing an agent's skills and endpoint
- [[Concepts/Skill|Skill]] `lesson term` — A named operation the agent supports (analog to MCP tool)
- [[Concepts/Task|Task]] `lesson term` — A work item with a lifecycle and final artifact
- [[Concepts/Message|Message]] `lesson term` — Carries Parts (text, file, data)
- Part `lesson term` — text / file / data element of a message
- [[Concepts/Artifact|Artifact]] `lesson term` — Named, typed output returned on completion
- AP2 `lesson term` — Signed Agent Cards extension for trust and payments
- Opacity `lesson term` — Called agent's internals are hidden from caller
- [[Concepts/input_required|input_required]] (as *Input-required*) `lesson term` — Lifecycle state when the agent needs more info

## Ships

- [[Artifacts/13-19 a2a-agent-spec|a2a-agent-spec]] `skill` — Produce the Agent Card and skills schema for an agent that should be callable over A2A.

## Further reading

- [[Resources/a2a-protocol.org|a2a-protocol.org]] ([link](https://a2a-protocol.org/latest/)) — canonical A2A specification ·  also cited by 2 other lessons
- Google Cloud — A2A protocol upgrade ([link](https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade)) — roadmap and partner momentum
- Google Dev — A2A 1.0 milestone ([link](https://discuss.google.dev/t/the-a2a-1-0-milestone-ensuring-and-testing-backward-compatibility/352258)) — v1.0 release notes and backward-compat guidance
- [[Resources/a2aproject-A2A — GitHub|a2aproject/A2A — GitHub]] ([link](https://github.com/a2aproject/A2A)) — reference implementations and SDKs ·  also cited by 1 other lesson
- Linux Foundation — A2A launch press release ([link](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents)) — June 2025 governance transfer


%% ── my notes ── %%
