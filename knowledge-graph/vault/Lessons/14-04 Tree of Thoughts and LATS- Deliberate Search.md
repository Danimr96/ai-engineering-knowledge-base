---
id: "lesson:14/04"
type: lesson
ref: 14/04
phase: 14
num: 4
title: "Tree of Thoughts and LATS: Deliberate Search"
lesson_type: build
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 7
code_files: 1
concepts: 8
prereqs: 2
community: 7
aliases:
  - 14/04
  - 14-04
tags:
  - phase/14
  - type/build
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/04-tree-of-thoughts-lats/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/04-tree-of-thoughts-lats"
---

# 14/04 Tree of Thoughts and LATS: Deliberate Search

> A single chain-of-thought trajectory has no room to backtrack. ToT (Yao et al., 2023) turns reasoning into a tree with self-evaluation on each node. LATS (Zhou et al., 2024) unifies ToT with ReAct and Reflexion under Monte Carlo Tree Search. Game of 24 goes from 4% (CoT) to 74% (ToT); LATS hits 92.7% pass@1 on HumanEval.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/04-tree-of-thoughts-lats/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/04-tree-of-thoughts-lats) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/04-tree-of-thoughts-lats) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 01 (Agent Loop), Phase 14 · 03 (Reflexion)`

- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Agent Loop
- [[Lessons/14-03 Reflexion- Verbal Reinforcement Learning|14/03 Reflexion: Verbal Reinforcement Learning]] — Reflexion

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/14-02 ReWOO and Plan-and-Execute- Decoupled Planning|14/02 ReWOO and Plan-and-Execute: Decoupled Planning]]

## Builds on this

- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- Tree of Thoughts `lesson term` — Yao et al. — tree of thought nodes with self-evaluation
- LATS `lesson term` — Zhou et al. — unifies ToT + ReAct + Reflexion under MCTS
- UCT `lesson term` — Select formula balancing exploitation (Q) and exploration (ln N / n)
- Value function `lesson term` — Prompted LLM score or environment reward; feeds backprop
- [[Concepts/Policy|Policy]] `lesson term` — ReAct-style generator; emits candidate next thoughts/actions
- Rollout `lesson term` — Walk from a node to a leaf using policy, score with value
- Backpropagate `lesson term` — Push the leaf's reward up the path, updating visit counts and Q
- Search cost `lesson term` — 100-1000x CoT on Game of 24; budget before you adopt

## Ships

- [[Artifacts/14-04 search-policy|search-policy]] `skill` — Pick a search strategy (ReAct, ToT, LATS, evolutionary) given task shape, token budget, and evaluator quality.

## Further reading

- [[Resources/Yao et al. — Tree of Thoughts- Deliberate Problem Solving with Large Language Models (arXiv-2305.10601)|Yao et al. — Tree of Thoughts: Deliberate Problem Solving with Large Language Models (arXiv:2305.10601)]] ([link](https://arxiv.org/abs/2305.10601)) — the canonical paper ·  also cited by 2 other lessons
- Zhou et al., LATS (arXiv:2310.04406) ([link](https://arxiv.org/abs/2310.04406)) — MCTS with Reflexion feedback
- [[Resources/AlphaEvolve (arXiv-2506.13131)|AlphaEvolve (arXiv:2506.13131)]] ([link](https://arxiv.org/abs/2506.13131)) — evolutionary search with programmatic evaluators ·  also cited by 2 other lessons
- [[Resources/LangGraph Plan-and-Execute tutorial|LangGraph Plan-and-Execute tutorial]] ([link](https://docs.langchain.com/oss/python/langgraph/overview)) — subgraph patterns for search ·  also cited by 9 other lessons


%% ── my notes ── %%
