---
id: "lesson:16/08"
type: lesson
ref: 16/08
phase: 16
num: 8
title: "Role Specialization — Planner, Critic, Executor, Verifier"
lesson_type: learn+build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 6
aliases:
  - 16/08
  - 16-08
tags:
  - phase/16
  - type/learn+build
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/08-role-specialization/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/08-role-specialization"
---

# 16/08 Role Specialization — Planner, Critic, Executor, Verifier

> The most common multi-agent decomposition in 2026: one agent plans, one executes, one critiques or verifies. MetaGPT (arXiv:2308.00352) formalizes this as SOPs encoded into role prompts — Product Manager, Architect, Project Manager, Engineer, QA Engineer — following `Code = SOP(Team)`. ChatDev (arXiv:2307.07924) chains designer, programmer, reviewer, tester through a "chat chain" with "communicative dehallucination" (agents explicitly request missing details). The verifier is load-bearing: Cemri et al. (MAST, arXiv:2503.13657) show every multi-agent failure can be traced to missing or broken verification. PwC reported 7× accuracy gain (10% → 70%) from structured validation loops in CrewAI.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn + Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/08-role-specialization/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/08-role-specialization) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/08-role-specialization) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 04 (Primitive Model), Phase 16 · 05 (Supervisor)`

- [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]] — Primitive Model
- [[Lessons/16-05 Supervisor - Orchestrator-Worker Pattern|16/05 Supervisor / Orchestrator-Worker Pattern]] — Supervisor

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]]

## Builds on this

- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- Role specialization `lesson term` — Distinct system prompts tuned for planner/executor/critic/verifier roles.
- SOP pattern `lesson term` — MetaGPT's framing: strict I/O schemas per role turn a team into a pipeline.
- [[Concepts/Communicative dehallucination|Communicative dehallucination]] `lesson term` — ChatDev pattern: executor asks planner when a detail is missing rather than making one up.
- [[Concepts/Critic|Critic]] `lesson term` — Subjective, opinionated reviewer. Catches taste issues. Can be fooled by plausible prose.
- [[Concepts/Verifier|Verifier]] `lesson term` — Code-based pass/fail. Test runner, type checker, schema validator. Cannot be fooled.
- [[Concepts/Verification gap|Verification gap]] `lesson term` — 21.3% of MAST failures. Answer shipped without a check that would have caught the bug.
- Revision loop `lesson term` — Critic rejection triggers executor re-run with feedback. Needs a budget.
- All-LLM anti-pattern `lesson term` — Every role is an LLM, no deterministic check. Classic MAST failure.

## Ships

- [[Artifacts/16-08 role-designer|role-designer]] `skill` — Produce a role roster for a multi-agent system, naming the planner/executor/critic/verifier for a given task with explicit I/O schemas.

## Further reading

- [[Resources/Qian et al. — Communicative Agents for Software Development (ChatDev)|Qian et al. — Communicative Agents for Software Development (ChatDev)]] ([link](https://arxiv.org/abs/2307.07924)) — chat chain + communicative dehallucination ·  also cited by 1 other lesson
- [[Resources/Hong et al. — MetaGPT- Meta Programming for Multi-Agent Collaboration|Hong et al. — MetaGPT: Meta Programming for Multi-Agent Collaboration]] ([link](https://arxiv.org/abs/2308.00352)) — the SOP-as-role-prompt reference paper ·  also cited by 1 other lesson
- [[Resources/Cemri et al., MASFT (arXiv-2503.13657)|Cemri et al., MASFT (arXiv:2503.13657)]] ([link](https://arxiv.org/abs/2503.13657)) — MAST taxonomy; verification gaps are 21.3% of failures ·  also cited by 4 other lessons
- [[Resources/CrewAI docs introduction|CrewAI docs introduction]] ([link](https://docs.crewai.com/en/introduction)) — production role specification surface ·  also cited by 5 other lessons


%% ── my notes ── %%
