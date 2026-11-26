---
id: "lesson:14/26"
type: lesson
ref: 14/26
phase: 14
num: 26
title: "Failure Modes: Why Agents Break"
lesson_type: learn+build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 1
concepts: 8
prereqs: 2
community: 7
aliases:
  - 14/26
  - 14-26
tags:
  - phase/14
  - type/learn+build
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/26-failure-modes-agentic/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/26-failure-modes-agentic"
---

# 14/26 Failure Modes: Why Agents Break

> MASFT (Berkeley, 2025) catalogs 14 multi-agent failure modes in 3 categories. Microsoft's Taxonomy documents how existing AI failures amplify in agentic settings. Industry field data converges on five recurring modes: hallucinated actions, scope creep, cascading errors, context loss, tool misuse.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn + Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/26-failure-modes-agentic/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/26-failure-modes-agentic) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/26-failure-modes-agentic) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 05 (Self-Refine and CRITIC), Phase 14 · 24 (Observability)`

- [[Lessons/14-05 Self-Refine and CRITIC- Iterative Output Improvement|14/05 Self-Refine and CRITIC: Iterative Output Improvement]] — Self-Refine and CRITIC
- [[Lessons/14-24 Agent Observability- Langfuse, Phoenix, Opik|14/24 Agent Observability: Langfuse, Phoenix, Opik]] — Observability

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]], [[Lessons/14-03 Reflexion- Verbal Reinforcement Learning|14/03 Reflexion: Verbal Reinforcement Learning]], [[Lessons/14-23 OpenTelemetry GenAI Semantic Conventions|14/23 OpenTelemetry GenAI Semantic Conventions]]
- depth 3: [[Lessons/14-02 ReWOO and Plan-and-Execute- Decoupled Planning|14/02 ReWOO and Plan-and-Execute: Decoupled Planning]], [[Lessons/14-13 Stateful Graph Orchestration — Durable Execution and Checkpoints|14/13 Stateful Graph Orchestration — Durable Execution and Checkpoints]]

## Builds on this

- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]
- [[Lessons/14-31 Agent Workbench Engineering- Why Capable Models Still Fail|14/31 Agent Workbench Engineering: Why Capable Models Still Fail]]

## Concepts taught

- MASFT `lesson term` — Berkeley 14-mode categorization
- Cascading error `lesson term` — One early mistake propagates through N steps
- Context loss `lesson term` — Long-horizon turn drops early-turn facts
- Tool misuse `lesson term` — Valid call, wrong invocation
- Success hallucination `lesson term` — Agent claims success on a 400; state unchanged
- [[Concepts/Scope creep|Scope creep]] `lesson term` — Agent does more than asked
- Instruction-following deviation `lesson term` — Ignores system prompt or user constraint
- Sub-intention errors `lesson term` — Omission, redundancy, disorder in plan execution

## Ships

- [[Artifacts/14-26 failure-detector|failure-detector]] `skill` — Generate failure-mode detectors for agent traces, wired to a trace store, tagging the five industry-recurring modes plus domain-specific signatures.

## Further reading

- [[Resources/Building Effective Agents|Building Effective Agents]] ([link](https://www.anthropic.com/research/building-effective-agents)) — when simpler patterns avoid modes entirely ·  also cited by 16 other lessons
- [[Resources/Cemri et al., MASFT (arXiv-2503.13657)|Cemri et al., MASFT (arXiv:2503.13657)]] ([link](https://arxiv.org/abs/2503.13657)) — 14 failure modes, 3 categories ·  also cited by 4 other lessons
- Microsoft, Taxonomy of Failure Mode in Agentic AI Systems ([link](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf)) — risk register
- [[Resources/Arize Phoenix docs|Arize Phoenix docs]] ([link](https://docs.arize.com/phoenix)) — drift clustering in practice ·  also cited by 2 other lessons

## In learning paths

- [[Paths/Agent Systems Engineering|Agent Systems Engineering]] — step 10, required
- [[Paths/AI Evaluation and Reliability|AI Evaluation and Reliability]] — step 4, required


%% ── my notes ── %%
