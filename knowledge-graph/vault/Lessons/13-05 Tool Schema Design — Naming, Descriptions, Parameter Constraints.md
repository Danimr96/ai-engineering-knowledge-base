---
id: "lesson:13/05"
type: lesson
ref: 13/05
phase: 13
num: 5
title: "Tool Schema Design — Naming, Descriptions, Parameter Constraints"
lesson_type: learn
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 2
community: 3
aliases:
  - 13/05
  - 13-05
tags:
  - phase/13
  - type/learn
  - community/03
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/05-tool-schema-design/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/05-tool-schema-design"
---

# 13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints

> A correct tool fails silently when the model cannot tell when to use it. Naming, descriptions, and parameter shapes drive 10 to 20 percentage-point swings in tool-selection accuracy on benchmarks like StableToolBench and MCPToolBench++. This lesson names the design rules that separate a tool a model picks reliably from a tool a model mis-fires.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Learn · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/05-tool-schema-design/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/05-tool-schema-design) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/05-tool-schema-design) · code: main.py  
**Community:** [[Communities/03 Parallel tool calls · Strict mode · Refusal|03 Parallel tool calls · Strict mode · Refusal]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 01 (the tool interface), Phase 13 · 04 (structured output)`

- [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]] — the tool interface
- [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]] — structured output

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]]

## Builds on this

- [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]]
- [[Lessons/13-22 Agent Skills- Portable Contract and Runtime Boundary|13/22 Agent Skills: Portable Contract and Runtime Boundary]]
- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]
- [[Lessons/19-20 Agent Harness Loop Contract|19/20 Agent Harness Loop Contract]]
- [[Lessons/19-21 Tool Registry with Schema Validation|19/21 Tool Registry with Schema Validation]]
- [[Lessons/19-22 JSON-RPC 2.0 Over Newline-Delimited Stdio|19/22 JSON-RPC 2.0 Over Newline-Delimited Stdio]]
- [[Lessons/19-23 Function Call Dispatcher|19/23 Function Call Dispatcher]]
- [[Lessons/19-24 Plan-Execute Control Flow|19/24 Plan-Execute Control Flow]]

## Concepts taught

- [[Concepts/Tool schema|Tool schema]] `lesson term` — JSON Schema for the tool's arguments
- Tool description `lesson term` — The natural-language brief the model reads during selection
- Atomic tool `lesson term` — A tool whose name uniquely identifies its behavior
- Monolithic tool `lesson term` — Single tool with an action string argument; selection accuracy tanks
- Enum-closed set `lesson term` — {type: "string", enum: [...]} as the correct shape for closed domains
- [[Concepts/Tool poisoning|Tool poisoning]] `lesson term` — Hidden instructions in a tool description that hijack the agent
- Tool-selection accuracy `lesson term` — Percentage of queries where the model calls the correct tool
- Description linter `lesson term` — Automated audit that enforces naming, length, disambiguation rules
- Namespace prefix `lesson term` — Shared name prefix that groups related tools in large registries
- StableToolBench `lesson term` — Public benchmark for measuring tool-selection accuracy

## Ships

- [[Artifacts/13-05 tool-schema-linter|tool-schema-linter]] `skill` — Audit a tool registry against production design rules for names, descriptions, parameters, and shape. Can run in CI on every tool-registry change.

## Further reading

- [[Resources/Anthropic — Building agents with the Claude Agent SDK|Anthropic — Building agents with the Claude Agent SDK]] ([link](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)) — description patterns for Claude-based agents ·  also cited by 2 other lessons
- Composio — How to build tools for AI agents: field guide ([link](https://composio.dev/blog/how-to-build-tools-for-ai-agents-a-field-guide)) — naming, descriptions, and measured accuracy lifts
- Databricks — Agent system design patterns ([link](https://docs.databricks.com/aws/en/generative-ai/guide/agent-system-design-patterns)) — registry-level design with measurable benchmarks
- OneUptime — Tool schemas for agents ([link](https://oneuptime.com/blog/post/2026-01-30-tool-schemas/view)) — parameter design patterns from production
- [[Resources/OpenAI Function Calling Guide|OpenAI Function Calling Guide]] ([link](https://platform.openai.com/docs/guides/function-calling)) — description length, strict-mode requirements, atomic-tool guidance ·  also cited by 4 other lessons

## In learning paths

- [[Paths/Agent Systems Engineering|Agent Systems Engineering]] — step 2, required
- [[Paths/Developer Experience and Education|Developer Experience and Education]] — step 3, required
- [[Paths/Software Engineering Fundamentals|Software Engineering Fundamentals]] — step 9, required


%% ── my notes ── %%
