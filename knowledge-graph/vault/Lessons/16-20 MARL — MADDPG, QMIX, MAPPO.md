---
id: "lesson:16/20"
type: lesson
ref: 16/20
phase: 16
num: 20
title: "MARL — MADDPG, QMIX, MAPPO"
lesson_type: learn
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 0
code_files: 1
concepts: 9
prereqs: 1
aliases:
  - 16/20
  - 16-20
tags:
  - phase/16
  - type/learn
  - stdlib-only
source: ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/20-marl-maddpg-qmix-mappo/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/20-marl-maddpg-qmix-mappo"
---

# 16/20 MARL — MADDPG, QMIX, MAPPO

> The reinforcement-learning heritage of multi-agent coordination, which still informs LLM-agent systems in 2026. **MADDPG** (Lowe et al., NeurIPS 2017, arXiv:1706.02275) introduced Centralized Training, Decentralized Execution (CTDE): each critic sees all agents' states and actions during training; at test time only local actors run. Works for cooperative, competitive, and mixed settings. **QMIX** (Rashid et al., ICML 2018, arXiv:1803.11485) is value-decomposition with a monotonic mixing network; per-agent Qs combine into joint Q so `argmax` distributes cleanly — dominant on StarCraft Multi-Agent Challenge (SMAC). **MAPPO** (Yu et al., NeurIPS 2022, arXiv:2103.01955) is PPO with a centralized value function; "surprisingly effective" on particle-world, SMAC, Google Research Football, Hanabi with minimal tuning. These underpin training policies for agent teams that must act decentrally. MAPPO is the **default 2026 cooperative-MARL baseline**. This lesson builds each from a small grid-world toy and lands the three ideas in muscle memory before touching LLM-agent training.

**Phase:** [[Phases/16 Multi-Agent & Swarms|Phase 16: Multi-Agent & Swarms]] · **Type:** Learn · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/16-multi-agent-and-swarms/20-marl-maddpg-qmix-mappo/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/16-multi-agent-and-swarms/20-marl-maddpg-qmix-mappo) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/16-multi-agent-and-swarms/20-marl-maddpg-qmix-mappo) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 09 (Reinforcement Learning), Phase 16 · 09 (Parallel Swarm Networks)`

- [[Lessons/16-09 Parallel - Swarm - Networked Architectures|16/09 Parallel / Swarm / Networked Architectures]] — Parallel Swarm Networks
- Whole phase: [[Phases/09 Reinforcement Learning|Phase 9: Reinforcement Learning]] — Reinforcement Learning ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/16-04 The Multi-Agent Primitive Model|16/04 The Multi-Agent Primitive Model]], [[Lessons/16-05 Supervisor - Orchestrator-Worker Pattern|16/05 Supervisor / Orchestrator-Worker Pattern]]
- depth 3: [[Lessons/16-01 Why Multi-Agent|16/01 Why Multi-Agent?]]

## Builds on this

- [[Lessons/16-25 Case Studies and the 2026 State of the Art|16/25 Case Studies and the 2026 State of the Art]]

## Concepts taught

- MARL `lesson term` — Reinforcement learning for multi-agent systems.
- [[Concepts/CTDE|CTDE]] `lesson term` — Train with global info; deploy with local policies.
- MADDPG `lesson term` — CTDE with per-agent critic seeing all observations + actions.
- [[Concepts/QMIX|QMIX]] `lesson term` — Monotonic mixing of per-agent Qs. Cooperative.
- [[Concepts/MAPPO|MAPPO]] `lesson term` — PPO with centralized value function. 2026 default baseline.
- Value decomposition `lesson term` — Joint Q represented as a monotone function of per-agent Qs.
- Non-stationarity `lesson term` — Each agent's env changes as others learn. The core MARL problem.
- On-policy / off-policy `lesson term` — PPO is on-policy (MAPPO); DDPG and Q-learning are off-policy.
- SMAC `lesson term` — Cooperative micromanagement benchmark; QMIX's homegrown ground.

## Ships

- [[Artifacts/16-20 marl-picker|marl-picker]] `skill` — Choose a MARL algorithm (MADDPG, QMIX, MAPPO, IQL, or extensions) for a given multi-agent task. Consider cooperative vs competitive, action-space type, heterogeneity, reward structure, and scale.

## Further reading

- [[Resources/Lowe et al. (2017). Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments (MADDPG)|Lowe et al. (2017). Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments (MADDPG)]] ([link](https://arxiv.org/abs/1706.02275)) — MADDPG; NeurIPS 2017 ·  also cited by 1 other lesson
- [[Resources/Rashid et al. (2018). QMIX- Monotonic Value Function Factorisation|Rashid et al. (2018). QMIX: Monotonic Value Function Factorisation]] ([link](https://arxiv.org/abs/1803.11485)) — QMIX; ICML 2018 ·  also cited by 1 other lesson
- [[Resources/Yu et al. (2022). The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games (MAPPO)|Yu et al. (2022). The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games (MAPPO)]] ([link](https://arxiv.org/abs/2103.01955)) — MAPPO; NeurIPS 2022 ·  also cited by 1 other lesson
- BAIR blog post on MAPPO ([link](https://bair.berkeley.edu/blog/2021/07/14/mappo/)) — readable framing of the MAPPO result
- SMAC repository ([link](https://github.com/oxwhirl/smac)) — StarCraft Multi-Agent Challenge


%% ── my notes ── %%
