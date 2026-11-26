---
id: "lesson:16/07"
type: lesson
ref: 16/07
phase: 16
num: 7
title: Society of Mind and Multi-Agent Debate
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
  - 16/07
  - 16-07
tags:
  - phase/16
  - type/learn+build
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/07-society-of-mind-debate/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/07-society-of-mind-debate"
---

# 16/07 Society of Mind and Multi-Agent Debate

> Minsky's 1986 premise — intelligence is a society of specialists — gets rediscovered every decade. In 2023 Du et al. turned it into a concrete algorithm: multiple LLM instances propose answers, read each other's answers, critique, and update. Over N rounds they converge on a consensus that beats zero-shot CoT and reflection on six reasoning and factuality tasks. Two findings matter: both **multiple agents** and **multiple rounds** contribute independently. The society beats a single-agent monologue; the multi-round exchange beats one-shot voting.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn + Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/07-society-of-mind-debate/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/07-society-of-mind-debate) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/07-society-of-mind-debate) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 04 (Primitive Model)`

- [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]] — Primitive Model

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]]

## Builds on this

- [[Lessons/16-14 Consensus and Byzantine Fault Tolerance for Agents|16/14 Consensus and Byzantine Fault Tolerance for Agents]]
- [[Lessons/16-15 Voting, Self-Consistency, and Debate Topology|16/15 Voting, Self-Consistency, and Debate Topology]]
- [[Lessons/16-18 Theory of Mind and Emergent Coordination|16/18 Theory of Mind and Emergent Coordination]]
- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- Society of Mind `lesson term` — Intelligence as interacting specialists; 1986 framing now operationalized via LLM debate.
- Multi-agent debate `lesson term` — N agents propose, critique each other, revise over R rounds, majority-vote.
- [[Concepts/Consensus|Consensus]] `lesson term` — Not epistemic truth — just fraction-on-majority-answer. Can be confidently wrong.
- Rounds `lesson term` — One round = each agent reads the others and updates once.
- Heterogeneous debate `lesson term` — Using different base models to decorrelate errors.
- Sycophancy cascade `lesson term` — Debate failure where agents defer to the most confident agent regardless of correctness.
- NLSOM `lesson term` — Natural-language society of mind; Zhuge et al.'s scaled version.
- Correlated error `lesson term` — Why self-consistency saturates; debate across different views decorrelates.

## Ships

- [[Artifacts/16-07 debate-configurator|debate-configurator]] `skill` — Configure a multi-agent debate for a given task, estimating quality gain and token cost before running.

## Further reading

- [[Resources/Du et al., Society of Minds (arXiv-2305.14325)|Du et al., Society of Minds (arXiv:2305.14325)]] ([link](https://arxiv.org/abs/2305.14325)) — the reference paper, ICML 2024 ·  also cited by 3 other lessons
- Zhuge et al. — Mindstorms in Natural Language-Based Societies of Mind ([link](https://arxiv.org/abs/2305.17066)) — 129-agent NLSOM
- [[Resources/Should we be going MAD- A Look at Multi-Agent Debate Strategies for LLMs|Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs]] ([link](https://arxiv.org/abs/2311.17371)) — benchmarks debate variants ·  also cited by 1 other lesson
- Debate project page ([link](https://composable-models.github.io/llm_debate/)) — Du et al.'s code, demos, and ablation details


%% ── my notes ── %%
