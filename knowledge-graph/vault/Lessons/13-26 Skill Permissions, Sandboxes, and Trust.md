---
id: "lesson:13/26"
type: lesson
ref: 13/26
phase: 13
num: 26
title: "Skill Permissions, Sandboxes, and Trust"
lesson_type: build
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 6
code_files: 3
concepts: 7
prereqs: 2
community: 14
aliases:
  - 13/26
  - 13-26
tags:
  - phase/13
  - type/build
  - community/14
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/26-skill-permissions-sandboxes-and-trust/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/26-skill-permissions-sandboxes-and-trust"
---

# 13/26 Skill Permissions, Sandboxes, and Trust

> A skill can suggest an action. Only the host can authorize it, only an isolation boundary can contain it, and only verification can tell you whether it worked.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/26-skill-permissions-sandboxes-and-trust/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/26-skill-permissions-sandboxes-and-trust) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/26-skill-permissions-sandboxes-and-trust) · code: main.py, sandbox/probe.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/14 Least Privilege · Prompt Injection · Sandbox|14 Least Privilege · Prompt Injection · Sandbox]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 25 (Skill Invocation and Routing), Phase 13 · 15 (MCP Security I)`

- [[Lessons/13-15 MCP Security- Poisoned Metadata, Routing, and MRTR State|13/15 MCP Security: Poisoned Metadata, Routing, and MRTR State]] — MCP Security I
- [[Lessons/13-25 Skill Invocation and Routing|13/25 Skill Invocation and Routing]] — Skill Invocation and Routing

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]], [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]], [[Lessons/13-24 Skill Discovery and Progressive Disclosure|13/24 Skill Discovery and Progressive Disclosure]]
- depth 3: [[Lessons/13-06 MCP Fundamentals- Stateless Requests and JSON-RPC|13/06 MCP Fundamentals: Stateless Requests and JSON-RPC]], [[Lessons/13-22 Agent Skills- Portable Contract and Runtime Boundary|13/22 Agent Skills: Portable Contract and Runtime Boundary]]

## Builds on this

- [[Lessons/13-27 Skill Evals, Packaging, and Portability|13/27 Skill Evals, Packaging, and Portability]]

## Concepts taught

- Permission `lesson term` — Policy authorizes a specific actor, operation, target, and duration
- [[Concepts/Approval Gate|Approval Gate]] `glossary` — An authorized decision before a consequential action
- [[Concepts/Sandbox|Sandbox]] `glossary` — An execution environment restricting reachable files, processes, network, credentials, and resources
- Capability exposure `lesson term` — Which operations the model can request, before authorization
- [[Concepts/Trust Boundary|Trust Boundary]] `glossary` — An interface where data or authority crosses between different trust assumptions
- Path jail `lesson term` — Filesystem containment enforced on resolved targets, not string prefixes
- Egress policy `lesson term` — Rules for which destinations and data an execution may send

## Ships

- [[Artifacts/13-26 skill-safety-reviewer|skill-safety-reviewer]] `skill` — Review a skill-requested filesystem, command, network, secret, or destructive action against an explicit sandbox policy without executing it.

## Further reading

- [[Resources/Agent Skills client implementation guide|Agent Skills client implementation guide]] ([link](https://agentskills.io/client-implementation/adding-skills-support)) — for trust, activation, and tool-mediated resource access. ·  also cited by 1 other lesson
- [[Resources/Agent Skills- using scripts|Agent Skills: using scripts]] ([link](https://agentskills.io/skill-creation/using-scripts)) — for script interfaces, error handling, and structured output. ·  also cited by 1 other lesson
- NIST SP 800-190 ([link](https://csrc.nist.gov/pubs/sp/800/190/final)) — for container security risks and controls.
- [[Resources/OpenAI- Build skills|OpenAI: Build skills]] ([link](https://learn.chatgpt.com/docs/build-skills)) — for the distinction between skill policy and current Codex sandbox controls. ·  also cited by 3 other lessons
- SLSA specification ([link](https://slsa.dev/spec/v1.2/)) — for software supply-chain provenance and integrity.

## In learning paths

- [[Paths/Agent Skills Engineering|Agent Skills Engineering]] — step 4, required


%% ── my notes ── %%
