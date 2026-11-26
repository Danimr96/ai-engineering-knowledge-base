---
id: "lesson:16/18"
type: lesson
ref: 16/18
phase: 16
num: 18
title: Theory of Mind and Emergent Coordination
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
  - 16/18
  - 16-18
tags:
  - phase/16
  - type/learn+build
  - community/06
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/18-theory-of-mind-coordination/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/18-theory-of-mind-coordination"
---

# 16/18 Theory of Mind and Emergent Coordination

> Li et al. (arXiv:2310.10701) showed that LLM agents in a cooperative text game exhibit **emergent high-order Theory of Mind** (ToM) — reasoning about what another agent believes about a third agent's beliefs — but fail on long-horizon planning due to context management and hallucination. Riedl (arXiv:2510.05174) measured higher-order synergy across a population and found that **only** the ToM-prompt condition produces identity-linked differentiation and goal-directed complementarity; lower-capacity LLMs show only spurious emergence. That is, coordination emergence is prompt-conditional and model-dependent, not free. This lesson implements a minimal ToM-aware agent, runs a cooperative task with and without ToM prompting, and measures the coordination delta against the Riedl 2025 protocol.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn + Build · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/18-theory-of-mind-coordination/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/18-theory-of-mind-coordination) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/18-theory-of-mind-coordination) · code: main.py  
**Community:** [[Communities/06 Communicative dehallucination · Consensus · Contract Net|06 Communicative dehallucination · Consensus · Contract Net]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 16 · 07 (Society of Mind and Debate), Phase 16 · 17 (Generative Agents)`

- [[Lessons/16-07 Society of Mind and Multi-Agent Debate|16/07 Society of Mind and Multi-Agent Debate]] — Society of Mind and Debate
- [[Lessons/16-17 Generative Agents and Emergent Simulation|16/17 Generative Agents and Emergent Simulation]] — Generative Agents

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]], [[Lessons/16-13 Shared Memory and Blackboard Patterns|16/13 Shared Memory and Blackboard Patterns]]
- depth 3: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]], [[Lessons/16-09 Parallel - Swarm - Networked Architectures|16/09 Parallel / Swarm / Networked Architectures]]

## Builds on this

- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- Theory of Mind `lesson term` — The capacity to model another agent's beliefs. Graded by order (0, 1, 2+).
- Sally-Anne test `lesson term` — 1985 developmental psychology; LLMs pass plain versions, fail complex ones.
- First-order ToM `lesson term` — Modeling one other's beliefs about facts.
- Second-order ToM `lesson term` — Recursive modeling one level deeper.
- Identity-linked differentiation `lesson term` — Riedl's metric: roles persist, not random.
- Goal-directed complementarity `lesson term` — Agents target different subtasks, not the same one.
- Higher-order synergy `lesson term` — Riedl's statistical measure for real coordination.
- Coordination illusion `lesson term` — Prompt-dressed appearance of coordination without measurable signal.

## Ships

- [[Artifacts/16-18 tom-auditor|tom-auditor]] `skill` — Audit a multi-agent system that claims "emergent coordination." Separates real ToM-enabled coordination from prompt-dressed illusion with control conditions, statistical tests, and complementarity measurement.

## Further reading

- Li et al. — Theory of Mind for Multi-Agent Collaboration via Large Language Models ([link](https://arxiv.org/abs/2310.10701)) — emergent ToM in cooperative games; long-horizon failure modes
- Riedl — Emergent Coordination in Multi-Agent Language Models ([link](https://arxiv.org/abs/2510.05174)) — population-scale measurement; ToM prompting is the load-bearing condition
- Premack & Woodruff — Does the chimpanzee have a theory of mind? ([link](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/does-the-chimpanzee-have-a-theory-of-mind/1E96B02CD9850E69AF20F81FA7EB3595)) — the 1978 origin of the ToM concept
- Baron-Cohen, Leslie, Frith — Does the autistic child have a theory of mind? ([link](https://doi.org/10.1016/0010-0277(85)) — 90022-8) — the Sally-Anne paper (1985)


%% ── my notes ── %%
