---
id: "lesson:13/25"
type: lesson
ref: 13/25
phase: 13
num: 25
title: Skill Invocation and Routing
lesson_type: build
languages:
  - Python
time_min: 105
on_route: false
quiz_count: 6
code_files: 2
concepts: 8
prereqs: 1
community: 33
aliases:
  - 13/25
  - 13-25
tags:
  - phase/13
  - type/build
  - community/33
  - stdlib-only
source: ai-engineering-from-scratch/phases/13-tools-and-protocols/25-skill-invocation-and-routing/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/25-skill-invocation-and-routing"
---

# 13/25 Skill Invocation and Routing

> Invocation is an authority decision followed by a relevance decision. A good description helps the model choose; a good policy decides whether that choice is allowed.

**Phase:** [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] · **Type:** Build · **Time:** 105 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/13-tools-and-protocols/25-skill-invocation-and-routing/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols/25-skill-invocation-and-routing) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/13-tools-and-protocols/25-skill-invocation-and-routing) · code: main.py, tests/test_main.py · quiz: 6 questions  
**Community:** [[Communities/33 Advantage · Baseline · Actor|33 Advantage · Baseline · Actor]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 13 · 24 (Skill Discovery and Progressive Disclosure)`

- [[Lessons/13-24 Skill Discovery and Progressive Disclosure|13/24 Skill Discovery and Progressive Disclosure]] — Skill Discovery and Progressive Disclosure

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/13-22 Agent Skills- Portable Contract and Runtime Boundary|13/22 Agent Skills: Portable Contract and Runtime Boundary]]
- depth 3: [[Lessons/13-01 The Tool Interface — Why Agents Need Structured I-O|13/01 The Tool Interface — Why Agents Need Structured I/O]], [[Lessons/13-05 Tool Schema Design — Naming, Descriptions, Parameter Constraints|13/05 Tool Schema Design — Naming, Descriptions, Parameter Constraints]]

## Builds on this

- [[Lessons/13-26 Skill Permissions, Sandboxes, and Trust|13/26 Skill Permissions, Sandboxes, and Trust]]
- [[Lessons/13-27 Skill Evals, Packaging, and Portability|13/27 Skill Evals, Packaging, and Portability]]

## Concepts taught

- Explicit invocation `lesson term` — An actor supplies skill identity directly, subject to policy
- Implicit invocation `lesson term` — A router selects from eligible catalog metadata based on task context
- User-invocable `lesson term` — A host-specific menu or direct-invocation property, not a core field
- Model-invocable `lesson term` — Eligibility for implicit model selection under host policy
- Invocation adapter `lesson term` — Code that maps a host's fields and APIs into a declared policy model
- Near miss `lesson term` — A non-triggering request that resembles a skill's intended inputs
- Abstention `lesson term` — A deliberate routing result when evidence is absent or ambiguous
- [[Concepts/Skill Invocation|Skill Invocation]] `glossary` — The runtime-mediated process in which an eligible human, model, application, or other skill selects a skill and causes its instructions to enter the working context.

## Ships

- [[Artifacts/13-25 skill-invocation-router|skill-invocation-router]] `skill` — Design and test explicit human, implicit model or agent, programmatic application, bounded skill-composition, and harness activation policies for an Agent Skill catalog.

## Further reading

- [[Resources/Evaluating Agent Skills|Evaluating Agent Skills]] ([link](https://agentskills.io/skill-creation/evaluating-skills)) — for trigger and output eval design. ·  also cited by 1 other lesson
- [[Resources/Optimizing skill descriptions|Optimizing skill descriptions]] ([link](https://agentskills.io/skill-creation/optimizing-descriptions)) — for positive triggers, specificity, and evaluation. ·  also cited by 1 other lesson
- [[Resources/Claude Code skills|Claude Code skills]] ([link](https://code.claude.com/docs/en/skills)) — for one host's `user-invocable`, `disable-model-invocation`, arguments, and delegated context. ·  also cited by 1 other lesson
- [[Resources/OpenAI- Build skills|OpenAI: Build skills]] ([link](https://learn.chatgpt.com/docs/build-skills)) — for current Codex explicit and implicit invocation controls. ·  also cited by 3 other lessons

## In learning paths

- [[Paths/Agent Skills Engineering|Agent Skills Engineering]] — step 3, required
- [[Paths/Developer Experience and Education|Developer Experience and Education]] — step 8, required


%% ── my notes ── %%
