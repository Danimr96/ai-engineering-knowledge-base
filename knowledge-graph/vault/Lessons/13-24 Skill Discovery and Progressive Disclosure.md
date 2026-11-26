---
id: "lesson:13/24"
type: lesson
ref: 13/24
phase: 13
num: 24
title: Skill Discovery and Progressive Disclosure
lesson_type: build
languages:
  - Python
time_min: 105
on_route: false
quiz_count: 6
code_files: 2
concepts: 9
prereqs: 1
community: 39
aliases:
  - 13/24
  - 13-24
tags:
  - phase/13
  - type/build
  - community/39
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/24-skill-discovery-and-progressive-disclosure/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/24-skill-discovery-and-progressive-disclosure"
---

# 13/24 Skill Discovery and Progressive Disclosure

> A skill becomes useful before its body is loaded. Its name and description earn a place in the catalog; its deeper files earn context only when the task reaches them.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 105 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/24-skill-discovery-and-progressive-disclosure/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/24-skill-discovery-and-progressive-disclosure) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/24-skill-discovery-and-progressive-disclosure) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/39 Skill Catalog · Agent Skill · Progressive Disclosure|39 Skill Catalog · Agent Skill · Progressive Disclosure]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 22 (Agent Skills: Portable Contract and Runtime Boundary)`

- [[Lessons/13-22 Agent Skills- Portable Contract and Runtime Boundary|13/22 Agent Skills: Portable Contract and Runtime Boundary]] — Agent Skills: Portable Contract and Runtime Boundary

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]]
- depth 3: [[Lessons/13-04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding|13/04 Structured Output — JSON Schema, Pydantic, Zod, Constrained Decoding]]

## Builds on this

- [[Lessons/13-25 Skill Invocation and Routing|13/25 Skill Invocation and Routing]]
- [[Lessons/13-27 Skill Evals, Packaging, and Portability|13/27 Skill Evals, Packaging, and Portability]]

## Concepts taught

- [[Concepts/Skill Discovery|Skill Discovery]] `glossary` — Search configured scopes, validate packages, attach provenance, and apply policy
- [[Concepts/Skill Catalog|Skill Catalog]] `glossary` — Compact model-visible routing metadata for eligible packages
- [[Concepts/Collision policy|Collision policy]] `lesson term` — A declared rule for same-name candidates from different sources
- [[Concepts/Progressive Disclosure|Progressive Disclosure]] `glossary` — Staged context admission from catalog to body to branch-specific resources
- Reference graph `lesson term` — The reachable resource structure and its load conditions
- Path containment `lesson term` — Verify resolved resource targets remain inside the resolved package root
- [[Concepts/Coding Agent|Coding Agent]] `glossary` — An agent specialized for software work that can inspect a repository, edit files, run development tools, and use their outputs to advance a scoped engineering task.

## Ships

- [[Artifacts/13-24 skill-catalog-builder|skill-catalog-builder]] `skill` — Build a bounded Agent Skill catalog across explicit discovery scopes and report collisions before loading instruction bodies.

## Further reading

- [[Resources/Agent Skills best practices|Agent Skills best practices]] ([link](https://agentskills.io/skill-creation/best-practices)) — for direct references and entry-file size. ·  also cited by 2 other lessons
- [[Resources/Optimizing skill descriptions|Optimizing skill descriptions]] ([link](https://agentskills.io/skill-creation/optimizing-descriptions)) — for catalog routing metadata. ·  also cited by 1 other lesson
- [[Resources/Agent Skills specification|Agent Skills specification]] ([link](https://agentskills.io/specification)) — for package shape and progressive disclosure levels. ·  also cited by 2 other lessons
- [[Resources/OpenAI- Build skills|OpenAI: Build skills]] ([link](https://learn.chatgpt.com/docs/build-skills)) — for current Codex discovery scopes and catalog limits. ·  also cited by 3 other lessons

## In learning paths

- [[Paths/Agent Skills Engineering|Agent Skills Engineering]] — step 2, required
- [[Paths/Developer Experience and Education|Developer Experience and Education]] — step 7, required


%% ── my notes ── %%
