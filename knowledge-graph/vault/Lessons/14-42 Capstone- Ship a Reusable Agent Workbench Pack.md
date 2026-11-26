---
id: "lesson:14/42"
type: lesson
ref: 14/42
phase: 14
num: 42
title: "Capstone: Ship a Reusable Agent Workbench Pack"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 7
code_files: 1
concepts: 5
prereqs: 11
community: 15
aliases:
  - 14/42
  - 14-42
tags:
  - phase/14
  - type/build
  - community/15
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/42-agent-workbench-capstone/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/42-agent-workbench-capstone"
---

# 14/42 Capstone: Ship a Reusable Agent Workbench Pack

> The mini-track ends with a pack you drop into any repo. Eleven lessons of surfaces compressed into a directory you can `cp -r` and have an agent working reliably the next morning. The capstone is the artifact this curriculum trades on.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/42-agent-workbench-capstone/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/42-agent-workbench-capstone) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/42-agent-workbench-capstone) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/15 System of record · Block severity · Definition of done|15 System of record · Block severity · Definition of done]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phases 14 · 31 to 14 · 41`

- **14/31-41**:
    - [[Lessons/14-31 Agent Workbench Engineering- Why Capable Models Still Fail|14/31 Agent Workbench Engineering: Why Capable Models Still Fail]]
    - [[Lessons/14-32 The Minimal Agent Workbench|14/32 The Minimal Agent Workbench]]
    - [[Lessons/14-33 Agent Instructions as Executable Constraints|14/33 Agent Instructions as Executable Constraints]]
    - [[Lessons/14-34 Repo Memory and Durable State|14/34 Repo Memory and Durable State]]
    - [[Lessons/14-35 Initialization Scripts for Agents|14/35 Initialization Scripts for Agents]]
    - [[Lessons/14-36 Scope Contracts and Task Boundaries|14/36 Scope Contracts and Task Boundaries]]
    - [[Lessons/14-37 Runtime Feedback Loops|14/37 Runtime Feedback Loops]]
    - [[Lessons/14-38 Verification Gates|14/38 Verification Gates]]
    - [[Lessons/14-39 Reviewer Agent- Separate Builder from Marker|14/39 Reviewer Agent: Separate Builder from Marker]]
    - [[Lessons/14-40 Multi-Session Handoff|14/40 Multi-Session Handoff]]
    - [[Lessons/14-41 The Workbench on a Real Repo|14/41 The Workbench on a Real Repo]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-26 Failure Modes- Why Agents Break|14/26 Failure Modes: Why Agents Break]]
- depth 3: [[Lessons/14-05 Self-Refine and CRITIC- Iterative Output Improvement|14/05 Self-Refine and CRITIC: Iterative Output Improvement]], [[Lessons/14-24 Agent Observability- Langfuse, Phoenix, Opik|14/24 Agent Observability: Langfuse, Phoenix, Opik]]

## Builds on this

- [[Lessons/19-29 Capstone Lesson 29- End-to-End Coding Agent on the Harness|19/29 Capstone Lesson 29: End-to-End Coding Agent on the Harness]]

## Concepts taught

- Workbench pack `lesson term` — A versioned directory carrying all seven surfaces
- Installer `lesson term` — bin/install.sh that lays the pack down idempotently
- Pack version `lesson term` — Major bumps for schema/script changes, patch for doc-only
- Drop-in pack `lesson term` — Pack works without per-repo customization on day one
- Forkable template `lesson term` — Public repo that GitHub's "Use this template" can clone from

## Ships

- [[Artifacts/14-42 workbench-pack|workbench-pack]] `skill` — Generate a project-tuned drop-in agent workbench pack — rules sharpened to the team's history, scope globs matched to the repo, rubric dimensions extended with one domain-specific entry.

## Further reading

- [[Resources/AGENTS.md specification|AGENTS.md specification]] ([link](https://agents.md/)) — what your pack's router must implement ·  also cited by 1 other lesson
- [[Resources/Anthropic, Effective harnesses for long-running agents|Anthropic, Effective harnesses for long-running agents]] ([link](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)) ·  also cited by 4 other lessons
- [[Resources/Anthropic, Harness design for long-running application development|Anthropic, Harness design for long-running application development]] ([link](https://www.anthropic.com/engineering/harness-design-long-running-apps)) ·  also cited by 2 other lessons
- [[Resources/Augment Code, A good AGENTS.md is a model upgrade. A bad one is worse than no docs at all|Augment Code, A good AGENTS.md is a model upgrade. A bad one is worse than no docs at all]] ([link](https://www.augmentcode.com/blog/how-to-write-good-agents-dot-md-files)) — pack docs quality bar ·  also cited by 1 other lesson
- [[Resources/HKUDS-OpenHarness|HKUDS/OpenHarness]] ([link](https://github.com/HKUDS/OpenHarness)) — reference implementation of a pack-equivalent ·  also cited by 1 other lesson
- [[Resources/andrewgarst-agentic_harness|andrewgarst/agentic_harness]] ([link](https://github.com/andrewgarst/agentic_harness)) — Redis-backed reference with eval suite ·  also cited by 1 other lesson
- SkillKit ([link](https://github.com/rohitg00/skillkit)) — install this skill across 32 AI agents
- [[Resources/Nx Blog, Teach Your AI Agent How to Work in a Monorepo|Nx Blog, Teach Your AI Agent How to Work in a Monorepo]] ([link](https://nx.dev/blog/nx-ai-agent-skills)) — single-source generator across six tools ·  also cited by 1 other lesson

## In learning paths

- [[Paths/Agent-Assisted Engineering|Agent-Assisted Engineering]] — step 16, required


%% ── my notes ── %%
