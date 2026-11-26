---
id: "lesson:16/13"
type: lesson
ref: 16/13
phase: 16
num: 13
title: Shared Memory and Blackboard Patterns
lesson_type: learn+build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 6
aliases:
  - 16/13
  - 16-13
tags:
  - phase/16
  - type/learn+build
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/13-shared-memory-blackboard/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/13-shared-memory-blackboard"
---

# 16/13 Shared Memory and Blackboard Patterns

> Two approaches coexist in 2026 multi-agent systems: the **message pool** (everyone sees everyone's messages, as in AutoGen GroupChat or MetaGPT) and the **blackboard with subscription** (agents subscribe to relevant events, as in Context-Aware MCP or the Matrix framework). Both are the only stateful part of a multi-agent system — which means both are where the interesting bugs live. The reference failure mode is **memory poisoning**: one agent hallucinates a "fact," other agents treat it as verified, and accuracy decays gradually in a way that is much harder to debug than an immediate crash. This lesson builds both structures from stdlib, injects a poisoning attack, and shows the three mitigations that actually work in production.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/13-shared-memory-blackboard/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/13-shared-memory-blackboard) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/13-shared-memory-blackboard) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 04 (Primitive Model), Phase 16 · 09 (Parallel Swarm Networks)`

- [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]] — Primitive Model
- [[Lessons/16-09 Parallel - Swarm - Networked Architectures|16/09 Parallel / Swarm / Networked Architectures]] — Parallel Swarm Networks

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]], [[Lessons/16-05 Supervisor - Orchestrator-Worker Pattern|16/05 Supervisor / Orchestrator-Worker Pattern]]

## Builds on this

- [[Lessons/16-14 Consensus and Byzantine Fault Tolerance for Agents|16/14 Consensus and Byzantine Fault Tolerance for Agents]]
- [[Lessons/16-17 Generative Agents and Emergent Simulation|16/17 Generative Agents and Emergent Simulation]]
- [[Lessons/16-22 Production Scaling — Queues, Checkpoints, Durability|16/22 Production Scaling — Queues, Checkpoints, Durability]]
- [[Lessons/16-23 Failure Modes — MAST, Groupthink, Monoculture, Cascading Errors|16/23 Failure Modes — MAST, Groupthink, Monoculture, Cascading Errors]]
- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- [[Concepts/Message pool|Message pool]] `lesson term` — Append-only log that every agent reads. Full transparency, poor scaling.
- Blackboard `lesson term` — Topic-keyed pub/sub. Agents subscribe to relevant topics. Scales farther.
- [[Concepts/Provenance|Provenance]] `lesson term` — Metadata on each write: writer, timestamp, prompt, sources.
- [[Concepts/Memory poisoning|Memory poisoning]] `lesson term` — One agent's error enters shared state, downstream agents adopt it as fact.
- Append-only `lesson term` — Corrections are new entries that supersede. Preserves audit trail.
- Unwritable verifier `lesson term` — Read-only agent that re-fetches sources and flags inconsistencies.
- [[Concepts/Projection|Projection]] `lesson term` — Per-agent view computed from global state. LangGraph reducers are the canonical case.
- Knowledge Source `lesson term` — Hayes-Roth's 1985 term for a blackboard participant.

## Ships

- [[Artifacts/16-13 memory-auditor|memory-auditor]] `skill` — Audit a multi-agent system's shared-memory design for provenance, versioning, verifier separation, and projection schema. Flag memory-poisoning exposure before production.

## Further reading

- [[Resources/Anthropic engineering — How we built our multi-agent research system|Anthropic engineering — How we built our multi-agent research system]] ([link](https://www.anthropic.com/engineering/multi-agent-research-system)) — provenance and verification notes from a production deployment ·  also cited by 6 other lessons
- [[Resources/Cemri et al., MASFT (arXiv-2503.13657)|Cemri et al., MASFT (arXiv:2503.13657)]] ([link](https://arxiv.org/abs/2503.13657)) — MAST taxonomy; memory poisoning is a coordination-failure sub-family ·  also cited by 4 other lessons
- [[Resources/Matrix — A Decentralized Framework for Multi-Agent Systems|Matrix — A Decentralized Framework for Multi-Agent Systems]] ([link](https://arxiv.org/abs/2511.21686)) — message-queue-based blackboard without a central orchestrator ·  also cited by 2 other lessons
- CA-MCP — Context-Aware Multi-Server MCP ([link](https://arxiv.org/abs/2601.11595)) — Shared Context Store for coordinated MCP servers
- [[Resources/LangGraph workflows and agents|LangGraph workflows and agents]] ([link](https://docs.langchain.com/oss/python/langgraph/workflows-agents)) — the per-agent projection pattern in production ·  also cited by 4 other lessons


%% ── my notes ── %%
