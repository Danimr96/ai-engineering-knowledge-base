---
id: "lesson:16/23"
type: lesson
ref: 16/23
phase: 16
num: 23
title: "Failure Modes — MAST, Groupthink, Monoculture, Cascading Errors"
lesson_type: learn
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 0
code_files: 1
concepts: 10
prereqs: 3
community: 6
aliases:
  - 16/23
  - 16-23
tags:
  - phase/16
  - type/learn
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/23-failure-modes-mast-groupthink/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/23-failure-modes-mast-groupthink"
---

# 16/23 Failure Modes — MAST, Groupthink, Monoculture, Cascading Errors

> The reference taxonomy for 2026 is **MAST** (Cemri et al., NeurIPS 2025, arXiv:2503.13657), derived from 1642 execution traces across 7 state-of-the-art open-source MAS showing **41–86.7% failure rate**. Three root categories: **Specification Problems** (41.77%) — role ambiguity, unclear task definitions; **Coordination Failures** (36.94%) — communication breakdowns, state desync; **Verification Gaps** (21.30%) — missing validation, absent quality checks. The **Groupthink** family (arXiv:2508.05687) adds: monoculture collapse (same base model → correlated failures), conformity bias (agents reinforce each other's errors), deficient theory of mind, mixed-motive dynamics, cascading reliability failures. Cascading example: retry storms where a payment failure triggers order retries, which trigger inventory retries, which overwhelm inventory service (10x load in seconds — needs circuit breakers). Memory poisoning: one agent's hallucination enters shared memory, downstream agents treat it as fact; accuracy decays gradually, making root-cause diagnosis painful. **STRATUS** (NeurIPS 2025) reports 1.5x mitigation-success improvement via specialized detection / diagnosis / validation agents. This lesson treats failure modes as first-class engineering targets.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/23-failure-modes-mast-groupthink/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/23-failure-modes-mast-groupthink) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/23-failure-modes-mast-groupthink) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 13 (Shared Memory), Phase 16 · 14 (Consensus and BFT), Phase 16 · 15 (Voting and Debate Topology)`

- [[Lessons/16-13 Shared Memory and Blackboard Patterns|16/13 Shared Memory and Blackboard Patterns]] — Shared Memory
- [[Lessons/16-14 Consensus and Byzantine Fault Tolerance for Agents|16/14 Consensus and Byzantine Fault Tolerance for Agents]] — Consensus and BFT
- [[Lessons/16-15 Voting, Self-Consistency, and Debate Topology|16/15 Voting, Self-Consistency, and Debate Topology]] — Voting and Debate Topology

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]], [[Lessons/16-07 Society of Mind and Multi-Agent Debate|16/07 Society of Mind and Multi-Agent Debate]], [[Lessons/16-09 Parallel - Swarm - Networked Architectures|16/09 Parallel / Swarm / Networked Architectures]]
- depth 3: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]], [[Lessons/16-05 Supervisor - Orchestrator-Worker Pattern|16/05 Supervisor / Orchestrator-Worker Pattern]]

## Builds on this

- [[Lessons/16-24 Evaluation and Coordination Benchmarks|16/24 Evaluation and Coordination Benchmarks]]
- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- MAST `lesson term` — Cemri 2025; 3 root categories + 14 sub-types of failures.
- Specification Problem `lesson term` — Task or role under-defined; agents do not know what to do.
- Coordination Failure `lesson term` — Communication or sync breakdown between agents.
- [[Concepts/Verification gap|Verification gap]] `lesson term` — Outputs accepted without independent validation.
- Groupthink family `lesson term` — Monoculture, conformity, deficient ToM, mixed-motive, cascading.
- Monoculture collapse `lesson term` — Correlated errors from shared base model or training data.
- Retry storm `lesson term` — One failure triggers retries which amplify load downstream.
- [[Concepts/Circuit Breaker|Circuit Breaker]] `glossary` — Open when error rate exceeds threshold; short-circuit with default.
- STRATUS `lesson term` — Detection + diagnosis + validation agents. 1.5x mitigation success.
- [[Concepts/Memory poisoning|Memory poisoning]] `lesson term` — Shared-memory fact tainted; downstream agents reason on poison.

## Ships

- [[Artifacts/16-23 mast-auditor|mast-auditor]] `skill` — Run a MAST-style failure-mode audit on a multi-agent system. Categorize execution-trace failures into Specification / Coordination / Verification and the Groupthink families; rank mitigations by expected failure reduction.

## Further reading

- [[Resources/Anthropic engineering — How we built our multi-agent research system|Anthropic engineering — How we built our multi-agent research system]] ([link](https://www.anthropic.com/engineering/multi-agent-research-system)) — production failure-mode notes ·  also cited by 6 other lessons
- [[Resources/Cemri et al., MASFT (arXiv-2503.13657)|Cemri et al., MASFT (arXiv:2503.13657)]] ([link](https://arxiv.org/abs/2503.13657)) — MAST taxonomy, NeurIPS 2025 ·  also cited by 4 other lessons
- Groupthink failures in multi-agent LLMs ([link](https://arxiv.org/abs/2508.05687)) — monoculture, conformity, and the five-family taxonomy
- STRATUS — specialized agents for MAS incident response ([link](https://neurips.cc/)) — NeurIPS 2025 proceedings entry (detection + diagnosis + validation)
- Release It! — stability patterns (Nygard) ([link](https://pragprog.com/titles/mnee2/release-it-second-edition/)) — the canonical circuit-breaker reference


%% ── my notes ── %%
