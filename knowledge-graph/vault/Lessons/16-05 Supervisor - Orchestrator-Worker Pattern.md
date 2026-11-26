---
id: "lesson:16/05"
type: lesson
ref: 16/05
phase: 16
num: 5
title: Supervisor / Orchestrator-Worker Pattern
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 1
community: 6
aliases:
  - 16/05
  - 16-05
tags:
  - phase/16
  - type/learn+build
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/05-supervisor-orchestrator-pattern/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/05-supervisor-orchestrator-pattern"
---

# 16/05 Supervisor / Orchestrator-Worker Pattern

> One lead agent plans and delegates; specialized workers execute in parallel contexts and report back. This is the pattern behind Anthropic's Research system (Claude Opus 4 as lead, Sonnet 4 as subagents), measured at +90.2% over single-agent Opus 4 on internal research evals. Anthropic's engineering post reports that 80% of the variance on BrowseComp is explained by token usage alone — multi-agent wins largely because each subagent gets a fresh context window. This lesson builds the supervisor pattern from the primitives and covers the 2026 engineering lessons from production deployments.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/05-supervisor-orchestrator-pattern/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/05-supervisor-orchestrator-pattern) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/05-supervisor-orchestrator-pattern) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 04 (Primitive Model)`

- [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]] — Primitive Model

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]]

## Builds on this

- [[Lessons/16-06 Hierarchical Architecture and Its Failure Mode|16/06 Hierarchical Architecture and Its Failure Mode]]
- [[Lessons/16-08 Role Specialization — Planner, Critic, Executor, Verifier|16/08 Role Specialization — Planner, Critic, Executor, Verifier]]
- [[Lessons/16-09 Parallel - Swarm - Networked Architectures|16/09 Parallel / Swarm / Networked Architectures]]
- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- [[Concepts/Supervisor|Supervisor]] `lesson term` — An orchestrator agent that plans, delegates, and synthesizes. Does not do the work itself.
- Worker `lesson term` — A focused agent invoked by the supervisor with narrow scope and its own context window.
- Orchestrator-worker `lesson term` — Same thing, different name. The 2026 literature uses both.
- Fresh context `lesson term` — A worker's context starts from its system prompt and assigned question, not the lead's history.
- Rainbow deployment `lesson term` — Long-running stateful agents need versioned drain-and-replace, not blue-green.
- Token dominance `lesson term` — 80% of research-eval variance comes from total tokens used, not model choice, per Anthropic.
- Scale effort `lesson term` — Lead estimates query difficulty, spawns 1 vs 10+ workers accordingly.
- Synthesis conflict `lesson term` — Two workers return contradictory facts; the lead must surface disagreement, not silently pick one.

## Ships

- [[Artifacts/16-05 supervisor-designer|supervisor-designer]] `skill` — Design a supervisor/orchestrator-worker system for a given research-style query, specifying lead prompt, worker roles, decomposition rules, and synthesis template.

## Further reading

- [[Resources/Anthropic engineering — How we built our multi-agent research system|Anthropic engineering — How we built our multi-agent research system]] ([link](https://www.anthropic.com/engineering/multi-agent-research-system)) — the production reference for supervisor pattern ·  also cited by 6 other lessons
- [[Resources/OpenAI cookbook- Orchestrating Agents — Routines and Handoffs|OpenAI cookbook: Orchestrating Agents — Routines and Handoffs]] ([link](https://developers.openai.com/cookbook/examples/orchestrating_agents)) — handoff-based supervisor variant ·  also cited by 2 other lessons
- [[Resources/LangGraph workflows and agents|LangGraph workflows and agents]] ([link](https://docs.langchain.com/oss/python/langgraph/workflows-agents)) — tool-calling supervisor is now the recommended form ·  also cited by 4 other lessons
- [[Resources/LangGraph supervisor reference|LangGraph supervisor reference]] ([link](https://reference.langchain.com/python/langgraph-supervisor)) — the legacy helper, still used in 2026 production ·  also cited by 1 other lesson


%% ── my notes ── %%
