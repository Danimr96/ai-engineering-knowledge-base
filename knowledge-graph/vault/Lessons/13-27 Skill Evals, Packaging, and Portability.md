---
id: "lesson:13/27"
type: lesson
ref: 13/27
phase: 13
num: 27
title: "Skill Evals, Packaging, and Portability"
lesson_type: build
languages:
  - Python
time_min: 150
on_route: false
quiz_count: 6
code_files: 2
concepts: 8
prereqs: 4
community: 33
aliases:
  - 13/27
  - 13-27
tags:
  - phase/13
  - type/build
  - community/33
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/27-skill-evals-packaging-and-portability/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/27-skill-evals-packaging-and-portability"
---

# 13/27 Skill Evals, Packaging, and Portability

> A skill is finished when its package survives linting, routes on the right requests, improves a measured task, stays inside policy, and degrades honestly on another host.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 150 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/27-skill-evals-packaging-and-portability/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/27-skill-evals-packaging-and-portability) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/27-skill-evals-packaging-and-portability) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/33 Advantage · Baseline · Actor|33 Advantage · Baseline · Actor]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 22, 24, 25, and 26`

- [[Lessons/13-22 Agent Skills- Portable Contract and Runtime Boundary|13/22 Agent Skills: Portable Contract and Runtime Boundary]]
- [[Lessons/13-24 Skill Discovery and Progressive Disclosure|13/24 Skill Discovery and Progressive Disclosure]]
- [[Lessons/13-25 Skill Invocation and Routing|13/25 Skill Invocation and Routing]]
- [[Lessons/13-26 Skill Permissions, Sandboxes, and Trust|13/26 Skill Permissions, Sandboxes, and Trust]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]], [[Lessons/13-15 MCP Security- Poisoned Metadata, Routing, and MRTR State|13/15 MCP Security: Poisoned Metadata, Routing, and MRTR State]]
- depth 3: [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]], [[Lessons/13-07 Building an MCP Server- Stateless Python and TypeScript|13/07 Building an MCP Server: Stateless Python and TypeScript]], [[Lessons/13-08 Building an MCP Client- Discovery, Routing, and Dual-Era Fallback|13/08 Building an MCP Client: Discovery, Routing, and Dual-Era Fallback]]

## Concepts taught

- Trigger eval `lesson term` — Labeled measurement of selection, abstention, and confusion at the routing boundary
- Behavior eval `lesson term` — Task execution measured against artifact, quality, scope, and efficiency contracts
- [[Concepts/Baseline|Baseline]] `lesson term` — The same model, tools, task, and budget under the comparison condition
- Artifact contract `lesson term` — Independently checkable properties required for completion
- Capability matrix `lesson term` — Per-host accounting of native support, adapters, degradation, and incompatibility
- Release gate `lesson term` — Layer-specific thresholds that block a package without hiding failure classes
- Silent degradation `lesson term` — A host loses required behavior without warning the installer or user
- [[Concepts/Skill Bundle|Skill Bundle]] `glossary` — The complete installable skill directory, including `SKILL.md` and every reference, script, asset, fixture, or companion file required by the workflow.

## Ships

- [[Artifacts/13-27 skill-release-gate|skill-release-gate]] `skill` — Evaluate an Agent Skill bundle for structural integrity, trigger quality, artifact improvement, script correctness, safety, installed-tree integrity, and target-host portability before release.

## Further reading

- [[Resources/Agent Skills client implementation guide|Agent Skills client implementation guide]] ([link](https://agentskills.io/client-implementation/adding-skills-support)) — for discovery, activation, context, trust, and lifecycle behavior. ·  also cited by 1 other lesson
- [[Resources/Agent Skills best practices|Agent Skills best practices]] ([link](https://agentskills.io/skill-creation/best-practices)) — for coherent scope and resource architecture. ·  also cited by 2 other lessons
- [[Resources/Evaluating Agent Skills|Evaluating Agent Skills]] ([link](https://agentskills.io/skill-creation/evaluating-skills)) — for trigger evals, output evals, repeated runs, and baselines. ·  also cited by 1 other lesson
- [[Resources/Agent Skills- using scripts|Agent Skills: using scripts]] ([link](https://agentskills.io/skill-creation/using-scripts)) — for deterministic helpers and structured interfaces. ·  also cited by 1 other lesson
- GitSkills: A Dataset of Agent Skills from GitHub ([link](https://arxiv.org/abs/2608.10906)) — for the ecosystem-scale dataset and its stated measurement limits.

## In learning paths

- [[Paths/Agent Skills Engineering|Agent Skills Engineering]] — step 5, required
- [[Paths/Developer Experience and Education|Developer Experience and Education]] — step 9, required


%% ── my notes ── %%
