---
id: "lesson:13/22"
type: lesson
ref: 13/22
phase: 13
num: 22
title: "Agent Skills: Portable Contract and Runtime Boundary"
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 6
code_files: 2
concepts: 7
prereqs: 2
community: 3
aliases:
  - 13/22
  - 13-22
tags:
  - phase/13
  - type/build
  - community/03
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/22-skills-and-agent-sdks/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/22-skills-and-agent-sdks"
---

# 13/22 Agent Skills: Portable Contract and Runtime Boundary

> A skill is not a long prompt with a better filename. It is a discoverable package of instructions, resources, and executable helpers that enters an agent's context through a runtime contract.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/22-skills-and-agent-sdks/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/22-skills-and-agent-sdks) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/22-skills-and-agent-sdks) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/03 Parallel tool calls · Strict mode · Refusal|03 Parallel tool calls · Strict mode · Refusal]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 01 (The Tool Interface), Phase 13 · 05 (Tool Schema Design)`

- [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]] — The Tool Interface
- [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]] — Tool Schema Design

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]]
- depth 3: [[Lessons/13-02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini|13/02 Function Calling Deep Dive — OpenAI, Anthropic, Gemini]]

## Builds on this

- [[Lessons/13-23 Capstone- Stateless Tool Ecosystem|13/23 Capstone: Stateless Tool Ecosystem]]
- [[Lessons/13-24 Skill Discovery and Progressive Disclosure|13/24 Skill Discovery and Progressive Disclosure]]
- [[Lessons/13-27 Skill Evals, Packaging, and Portability|13/27 Skill Evals, Packaging, and Portability]]

## Concepts taught

- [[Concepts/Agent Skill|Agent Skill]] `glossary` — A discoverable directory of procedural instructions and optional resources
- Portable core `lesson term` — The contract defined by the Agent Skills specification
- Runtime extension `lesson term` — Host-specific configuration whose behavior requires a compatible adapter
- Activation `lesson term` — The skill body entered model-visible context; execution may come later
- Skill dependency `lesson term` — A runtime-mediated invocation edge with availability and policy checks
- [[Concepts/Tool Contract|Tool Contract]] `glossary` — Inputs, outputs, permissions, side effects, errors, and evidence for a capability

## Ships

- [[Artifacts/13-22 skill-contract-reviewer|skill-contract-reviewer]] `skill` — Validate an Agent Skill package and choose the right instruction, capability, or lifecycle primitive before implementation.

## Further reading

- [[Resources/Agent Skills best practices|Agent Skills best practices]] ([link](https://agentskills.io/skill-creation/best-practices)) — for scope, instructions, and resource organization. ·  also cited by 2 other lessons
- [[Resources/Agent Skills specification|Agent Skills specification]] ([link](https://agentskills.io/specification)) — for the portable directory and frontmatter contract. ·  also cited by 2 other lessons
- [[Resources/Claude Code skills|Claude Code skills]] ([link](https://code.claude.com/docs/en/skills)) — for one runtime's invocation, argument, tool, and delegated-context extensions. ·  also cited by 1 other lesson
- [[Resources/OpenAI- Build skills|OpenAI: Build skills]] ([link](https://learn.chatgpt.com/docs/build-skills)) — for current Codex discovery and invocation behavior. ·  also cited by 3 other lessons

## In learning paths

- [[Paths/Agent Skills Engineering|Agent Skills Engineering]] — step 1, required
- [[Paths/Developer Experience and Education|Developer Experience and Education]] — step 6, required


%% ── my notes ── %%
