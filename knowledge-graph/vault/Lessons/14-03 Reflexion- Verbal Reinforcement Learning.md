---
id: "lesson:14/03"
type: lesson
ref: 14/03
phase: 14
num: 3
title: "Reflexion: Verbal Reinforcement Learning"
lesson_type: build
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
  - 14/03
  - 14-03
tags:
  - phase/14
  - type/build
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/03-reflexion-verbal-rl/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/03-reflexion-verbal-rl"
---

# 14/03 Reflexion: Verbal Reinforcement Learning

> Gradient-based RL needs thousands of trials and a GPU cluster to fix a failure mode. Reflexion (Shinn et al., NeurIPS 2023) does it in natural language: after each failed trial, the agent writes a reflection, stores it in episodic memory, and conditions the next trial on that memory. This is the pattern behind Letta's sleep-time compute, Claude Code's CLAUDE.md learnings, and pro-workflow's learn-rule.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/03-reflexion-verbal-rl/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/03-reflexion-verbal-rl) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/03-reflexion-verbal-rl) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 01 (Agent Loop), Phase 14 · 02 (ReWOO)`

- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Agent Loop
- [[Lessons/14-02 ReWOO and Plan-and-Execute- Decoupled Planning|14/02 ReWOO and Plan-and-Execute: Decoupled Planning]] — ReWOO

## Builds on this

- [[Lessons/14-04 Tree of Thoughts and LATS- Deliberate Search|14/04 Tree of Thoughts and LATS: Deliberate Search]]
- [[Lessons/14-05 Self-Refine and CRITIC- Iterative Output Improvement|14/05 Self-Refine and CRITIC: Iterative Output Improvement]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- Reflexion `lesson term` — Shinn et al. 2023 — Actor, Evaluator, Self-Reflector plus episodic memory
- Verbal reinforcement `lesson term` — Natural-language reflection prepended to the next trial's prompt
- [[Concepts/Episodic memory|Episodic memory]] `lesson term` — Bounded buffer of prior reflections for one task class
- Scalar evaluator `lesson term` — Pass/fail or numeric score from ground truth
- Heuristic evaluator `lesson term` — Predefined failure signatures (e.g. stuck-loop, too-many-steps)
- Self-evaluator `lesson term` — Lower-signal fallback when no ground truth — pair with tool-grounded verification
- [[Concepts/Memory rot|Memory rot]] `lesson term` — Episodic buffer fills with obsolete entries; fix with compaction/TTL
- Sleep-time reflection `lesson term` — Run Self-Reflector off the hot path so primary agent stays fast

## Ships

- [[Artifacts/14-03 reflexion-buffer|reflexion-buffer]] `skill` — Maintain an episodic-memory buffer of reflections for verbal RL with TTL, dedup, and scoped scope.

## Further reading

- [[Resources/Anthropic, Effective context engineering for AI agents|Anthropic, Effective context engineering for AI agents]] ([link](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)) — managing the episodic buffer as part of context ·  also cited by 2 other lessons
- [[Resources/Shinn et al., Reflexion- Language Agents with Verbal Reinforcement Learning (arXiv-2303.11366)|Shinn et al., Reflexion: Language Agents with Verbal Reinforcement Learning (arXiv:2303.11366)]] ([link](https://arxiv.org/abs/2303.11366)) — the canonical paper ·  also cited by 1 other lesson
- [[Resources/LangGraph Plan-and-Execute tutorial|LangGraph Plan-and-Execute tutorial]] ([link](https://docs.langchain.com/oss/python/langgraph/overview)) — reflection node pattern ·  also cited by 9 other lessons
- [[Resources/Letta, Sleep-time Compute|Letta, Sleep-time Compute]] ([link](https://www.letta.com/blog/sleep-time-compute)) — async reflection in production ·  also cited by 1 other lesson


%% ── my notes ── %%
