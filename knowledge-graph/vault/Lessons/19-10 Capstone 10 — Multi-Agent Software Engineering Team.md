---
id: "lesson:19/10"
type: lesson
ref: 19/10
phase: 19
num: 10
title: "Capstone 10 — Multi-Agent Software Engineering Team"
lesson_type: capstone
languages:
  - Python
  - TypeScript
  - Shell
time_min: 2400
on_route: false
quiz_count: 7
code_files: 9
concepts: 7
prereqs: 0
aliases:
  - 19/10
  - 19-10
tags:
  - phase/19
  - type/capstone
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/10-multi-agent-software-team/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/10-multi-agent-software-team"
---

# 19/10 Capstone 10 — Multi-Agent Software Engineering Team

> The 2026 shape of a multi-agent engineering team has converged: an architect plans, N coders work in parallel worktrees, a reviewer gates, a tester verifies. SWE-AF's factory architecture, MetaGPT's role-based prompting, AutoGen 0.4's typed actor graph, Cognition's Devin, and Factory's Droids all landed on it independently. Parallel worktrees convert wall-clock into throughput. Shared state and handoff protocols become the failure surface. The capstone is to build the team, evaluate on SWE-bench Pro, and report which handoffs break and how often.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Capstone · **Time:** 2400 min · **Languages:** Python, TypeScript, Shell · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/10-multi-agent-software-team/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/10-multi-agent-software-team) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/10-multi-agent-software-team) · code: main.py, ts/src/agent.ts, ts/src/coordinator.ts, ts/src/index.ts, ts/src/runtime.ts, ts/src/types.ts … · quiz: 7 questions  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 11 (LLM engineering), Phase 13 (tools), Phase 14 (agents), Phase 15 (autonomous), Phase 16 (multi-agent), Phase 17 (infrastructure)`

- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM engineering ·  medium confidence
- Whole phase: [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] — tools ·  medium confidence
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — agents ·  medium confidence
- Whole phase: [[Phases/15 Autonomous Systems|Phase 15: Autonomous Systems]] — autonomous ·  medium confidence
- Whole phase: [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] — multi-agent ·  medium confidence
- Whole phase: [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] — infrastructure ·  medium confidence

## Concepts taught

- Parallel worktree `lesson term` — git worktree add producing a fresh working tree per coder
- [[Concepts/Task board|Task board]] `lesson term` — File or Redis store of typed messages agents subscribe to
- [[Concepts/Handoff|Handoff]] `glossary` — Any message crossing from one role's context to another's
- Token amplification `lesson term` — Total tokens across roles / single-agent tokens for the same task
- A2A protocol `lesson term` — Google's 2025 spec for typed inter-agent messages
- Merge coordinator `lesson term` — Component that runs three-way merge and mediates conflicts
- False approval `lesson term` — Reviewer approves a diff with known bugs

## Ships

- [[Artifacts/19-10 multi-agent-team|multi-agent-team]] `skill` — Build a multi-agent software team with architect, parallel coders, reviewer, and tester; measure against SWE-bench Pro and produce a handoff post-mortem.

## Further reading

- [[Resources/a2a-protocol.org|a2a-protocol.org]] ([link](https://a2a-protocol.org/latest/)) — inter-agent messaging spec ·  also cited by 2 other lessons
- Cognition AI (Devin) ([link](https://cognition.ai)) — reference product
- [[Resources/Factory Droids|Factory Droids]] ([link](https://www.factory.ai)) — alternate reference product ·  also cited by 1 other lesson
- git-worktree documentation ([link](https://git-scm.com/docs/git-worktree)) — the isolation substrate
- SWE-AF factory architecture ([link](https://github.com/Agent-Field/SWE-AF)) — the reference 2026 multi-agent factory
- MetaGPT ([link](https://github.com/FoundationAgents/MetaGPT)) — role-based multi-agent framework
- AutoGen v0.4 ([link](https://github.com/microsoft/autogen)) — Microsoft's typed actor framework
- [[Resources/Jimenez et al. SWE-bench leaderboard|Jimenez et al. SWE-bench leaderboard]] ([link](https://www.swebench.com/)) — the evaluation target ·  also cited by 4 other lessons


%% ── my notes ── %%
