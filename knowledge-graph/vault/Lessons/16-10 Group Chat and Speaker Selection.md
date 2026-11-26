---
id: "lesson:16/10"
type: lesson
ref: 16/10
phase: 16
num: 10
title: Group Chat and Speaker Selection
lesson_type: learn+build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 1
community: 6
aliases:
  - 16/10
  - 16-10
tags:
  - phase/16
  - type/learn+build
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/10-group-chat-speaker-selection/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/10-group-chat-speaker-selection"
---

# 16/10 Group Chat and Speaker Selection

> Shared-conversation orchestration puts N agents in one conversation; a selector function (LLM, round-robin, or custom) picks who speaks next. This is the archetype of emergent multi-agent conversation — agents do not know their role in a static graph, they just react to the shared pool. AutoGen GroupChat and AG2 GroupChat are the reference implementations: AutoGen v0.2's GroupChat semantics were preserved in the AG2 fork; AutoGen v0.4 rewrote it as an event-driven actor model. Microsoft put AutoGen into maintenance mode in February 2026 and merged it with Semantic Kernel into Microsoft Agent Framework (RC February 2026). The GroupChat primitive survives in both AG2 and Microsoft Agent Framework — learn it once, use it everywhere.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn + Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/10-group-chat-speaker-selection/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/10-group-chat-speaker-selection) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/10-group-chat-speaker-selection) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 04 (Primitive Model)`

- [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]] — Primitive Model

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]]

## Builds on this

- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- [[Concepts/GroupChat|GroupChat]] `lesson term` — Shared message pool + selector function. AutoGen / AG2 primitive.
- [[Concepts/Speaker selection|Speaker selection]] `lesson term` — The function that picks the next agent. Round-robin, LLM-selected, or custom.
- GroupChatManager `lesson term` — AutoGen component that owns the selector and loops over turns.
- ConversableAgent `lesson term` — AutoGen base class; an agent that can send and receive messages.
- Termination token `lesson term` — Sentinel string (usually TERMINATE) that ends the chat.
- Hot speaker `lesson term` — Failure mode where the selector keeps picking the same agent.
- Context bloat `lesson term` — Each agent reads every prior message; context grows with turns.
- [[Concepts/Projection|Projection]] `lesson term` — Role-specific view into the shared pool to prevent context bloat.

## Ships

- [[Artifacts/16-10 groupchat-selector|groupchat-selector]] `skill` — Configure an AutoGen/AG2-style GroupChat selector for a task, naming the selector variant, termination, and anti-hot-speaker rules.

## Further reading

- [[Resources/AG2 (community AutoGen continuation)|AG2 (community AutoGen continuation)]] ([link](https://github.com/ag2ai/ag2)) — community AutoGen v0.2 continuation ·  also cited by 1 other lesson
- Microsoft Agent Framework docs ([link](https://learn.microsoft.com/en-us/agent-framework/)) — the merged successor, RC February 2026
- [[Resources/AutoGen stable docs|AutoGen stable docs]] ([link](https://microsoft.github.io/autogen/stable/)) — event-driven actor model rewrite details ·  also cited by 2 other lessons
- AutoGen group chat docs ([link](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/group-chat.html)) — the reference implementation


%% ── my notes ── %%
