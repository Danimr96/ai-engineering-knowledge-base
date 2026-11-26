---
id: "lesson:16/06"
type: lesson
ref: 16/06
phase: 16
num: 6
title: Hierarchical Architecture and Its Failure Mode
lesson_type: learn+build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 7
prereqs: 1
community: 6
aliases:
  - 16/06
  - 16-06
tags:
  - phase/16
  - type/learn+build
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/06-hierarchical-architecture/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/06-hierarchical-architecture"
---

# 16/06 Hierarchical Architecture and Its Failure Mode

> Hierarchical is supervisor nested. Manager agents over sub-managers over workers. CrewAI `Process.hierarchical` is the textbook version: a `manager_llm` dynamically delegates tasks and validates outputs. The LangGraph equivalent is `create_supervisor(create_supervisor(...))`. It is the natural pattern when the task is a real org chart. It is also the pattern most likely to collapse into managerial looping — manager agents assign work poorly, misinterpret sub-outputs, or fail to reach consensus. Sequential often beats it.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn + Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/06-hierarchical-architecture/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/06-hierarchical-architecture) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/06-hierarchical-architecture) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 05 (Supervisor Pattern)`

- [[Lessons/16-05 Supervisor - Orchestrator-Worker Pattern|16/05 Supervisor / Orchestrator-Worker Pattern]] — Supervisor Pattern

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]]
- depth 3: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]]

## Builds on this

- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- [[Concepts/Hierarchical|Hierarchical]] `lesson term` — Supervisors over supervisors; only leaves do work.
- [[Concepts/Manager LLM|Manager LLM]] `lesson term` — The LLM that decomposes, assigns, and validates at an internal node.
- Decomposition drift `lesson term` — Top manager's split no longer covers the original question.
- Reconciliation loop `lesson term` — Sub-managers disagree; top re-delegates; workers re-run; loop until budget exhausted.
- Depth-2 ceiling `lesson term` — Empirical guardrail: 3+ levels collapses observability.
- Canary question `lesson term` — A worker that is always asked the original query unchanged, to detect drift.
- Provenance chain `lesson term` — Trace from each synthesis back to the leaf outputs that produced it.

## Ships

- [[Artifacts/16-06 hierarchy-fitness|hierarchy-fitness]] `skill` — Decide whether a multi-agent task fits hierarchical, flat supervisor, or sequential. Surface the failure modes that matter.

## Further reading

- [[Resources/Anthropic engineering — How we built our multi-agent research system|Anthropic engineering — How we built our multi-agent research system]] ([link](https://www.anthropic.com/engineering/multi-agent-research-system)) — why Anthropic deliberately chose flat supervisor over hierarchical ·  also cited by 6 other lessons
- [[Resources/Cemri et al., MASFT (arXiv-2503.13657)|Cemri et al., MASFT (arXiv:2503.13657)]] ([link](https://arxiv.org/abs/2503.13657)) — MAST taxonomy; section on coordination failures documents decomposition drift ·  also cited by 4 other lessons
- [[Resources/CrewAI docs introduction|CrewAI docs introduction]] ([link](https://docs.crewai.com/en/introduction)) — textbook hierarchical with a manager LLM ·  also cited by 5 other lessons
- [[Resources/LangGraph supervisor reference|LangGraph supervisor reference]] ([link](https://reference.langchain.com/python/langgraph-supervisor)) — nested supervisor via `create_supervisor` ·  also cited by 1 other lesson


%% ── my notes ── %%
