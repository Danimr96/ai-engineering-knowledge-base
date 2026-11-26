---
id: "lesson:14/28"
type: lesson
ref: 14/28
phase: 14
num: 28
title: "Orchestration Patterns: Supervisor, Swarm, Hierarchical"
lesson_type: learn+build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 1
concepts: 7
prereqs: 2
community: 7
aliases:
  - 14/28
  - 14-28
tags:
  - phase/14
  - type/learn+build
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/28-orchestration-patterns/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/28-orchestration-patterns"
---

# 14/28 Orchestration Patterns: Supervisor, Swarm, Hierarchical

> Four orchestration patterns recur across 2026 frameworks: supervisor-worker, swarm / peer-to-peer, hierarchical, debate. Anthropic's guidance: "It's about building the right system for your needs." Start simple; add topology only when a single agent plus five workflow patterns is insufficient.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn + Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/28-orchestration-patterns/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/28-orchestration-patterns) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/28-orchestration-patterns) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 12 (Workflow Patterns), Phase 14 · 25 (Multi-Agent Debate)`

- [[Lessons/14-12 Anthropic's Workflow Patterns- Simple Over Complex|14/12 Anthropic's Workflow Patterns: Simple Over Complex]] — Workflow Patterns
- [[Lessons/14-25 Multi-Agent Debate and Collaboration|14/25 Multi-Agent Debate and Collaboration]] — Multi-Agent Debate

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-05 Self-Refine and CRITIC- Iterative Output Improvement|14/05 Self-Refine and CRITIC: Iterative Output Improvement]]
- depth 3: [[Lessons/14-03 Reflexion- Verbal Reinforcement Learning|14/03 Reflexion: Verbal Reinforcement Learning]]

## Builds on this

- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- Supervisor-worker `lesson term` — Central LLM dispatches to specialists; they don't talk to each other
- [[Concepts/Swarm|Swarm]] `glossary` — Direct handoffs via shared tools; no central router
- [[Concepts/Hierarchical|Hierarchical]] `lesson term` — Nested subgraphs for large populations
- [[Concepts/Debate|Debate]] `lesson term` — Parallel proposers, cross-critique (Lesson 25)
- Tool-call-based supervision `lesson term` — Implement supervisor as direct tool calls for context control
- [[Concepts/Crew|Crew]] `lesson term` — CrewAI's role-based collaboration mode
- [[Concepts/Flow|Flow]] `lesson term` — CrewAI's event-driven production mode

## Ships

- [[Artifacts/14-28 orchestration-picker|orchestration-picker]] `skill` — Pick an orchestration topology (supervisor, swarm, hierarchical, debate, or none) for a given problem and implement it minimally.

## Further reading

- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents)) — five patterns + agent vs workflow ·  also cited by 16 other lessons
- [[Resources/Du et al., Society of Minds (arXiv-2305.14325)|Du et al., Society of Minds (arXiv:2305.14325)]] ([link](https://arxiv.org/abs/2305.14325)) — debate pattern ·  also cited by 3 other lessons
- [[Resources/CrewAI docs introduction|CrewAI docs introduction]] ([link](https://docs.crewai.com/en/introduction)) — Crew vs Flow ·  also cited by 5 other lessons
- [[Resources/LangGraph Plan-and-Execute tutorial|LangGraph Plan-and-Execute tutorial]] ([link](https://docs.langchain.com/oss/python/langgraph/overview)) — supervisor, swarm, hierarchical ·  also cited by 9 other lessons

## In learning paths

- [[Paths/Agent Systems Engineering|Agent Systems Engineering]] — step 9, required


%% ── my notes ── %%
