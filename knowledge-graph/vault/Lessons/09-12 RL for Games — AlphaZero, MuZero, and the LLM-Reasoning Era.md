---
id: "lesson:09/12"
type: lesson
ref: 09/12
phase: 9
num: 12
title: "RL for Games — AlphaZero, MuZero, and the LLM-Reasoning Era"
lesson_type: build
languages:
  - Python
time_min: 120
on_route: false
quiz_count: 0
code_files: 1
concepts: 9
prereqs: 4
community: 60
aliases:
  - 09/12
  - 09-12
tags:
  - phase/09
  - type/build
  - community/60
  - stdlib-only
source: ai-engineering-from-scratch/phases/09-reinforcement-learning/12-rl-for-games/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/12-rl-for-games"
---

# 09/12 RL for Games — AlphaZero, MuZero, and the LLM-Reasoning Era

> 1992: TD-Gammon beat human champions at backgammon with pure TD. 2016: AlphaGo beat Lee Sedol. 2017: AlphaZero dominated chess, shogi, and Go from scratch. 2024: DeepSeek-R1 proved the same recipe, with GRPO replacing PPO, works on reasoning. Games are the benchmark that drives every breakthrough in this phase.

**Phase:** [[Phases/09 Reinforcement Learning|Phase 9: Reinforcement Learning]] · **Type:** Build · **Time:** 120 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/09-reinforcement-learning/12-rl-for-games/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/12-rl-for-games) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/09-reinforcement-learning/12-rl-for-games) · code: main.py  
**Community:** [[Communities/60 GRPO · KL penalty · League play|60 GRPO · KL penalty · League play]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 9 · 05 (DQN), Phase 9 · 08 (PPO), Phase 9 · 09 (RLHF), Phase 9 · 10 (MARL)`

- [[Lessons/09-05 Deep Q-Networks (DQN)|09/05 Deep Q-Networks (DQN)]] — DQN
- [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]] — PPO
- [[Lessons/09-09 Reward Modeling & RLHF|09/09 Reward Modeling & RLHF]] — RLHF
- [[Lessons/09-10 Multi-Agent RL|09/10 Multi-Agent RL]] — MARL

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/05-05 Sentiment Analysis|05/05 Sentiment Analysis]], [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-07 Actor-Critic — A2C and A3C|09/07 Actor-Critic — A2C and A3C]]
- depth 3: [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-02 Dynamic Programming — Policy Iteration & Value Iteration|09/02 Dynamic Programming — Policy Iteration & Value Iteration]], [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]]

## Concepts taught

- MCTS `lesson term` — Monte Carlo Tree Search; UCB1/PUCT selection with learned (p, v) priors.
- AlphaZero `lesson term` — Policy-value net trained to match MCTS visits and game outcome.
- MuZero `lesson term` — Same loop but in latent space via learned dynamics.
- [[Concepts/GRPO|GRPO]] `lesson term` — Group Relative Policy Optimization; REINFORCE with group-mean baseline + KL.
- PUCT `lesson term` — Q + c · p · √N / (1 + N_a) — balances value estimate with prior.
- [[Concepts/Self-play|Self-play]] `lesson term` — Standard for zero-sum; symmetric training signal.
- [[Concepts/League play|League play]] `lesson term` — Past + current + exploiters sampled as opponents.
- Verifier reward `lesson term` — Reward comes from a deterministic checker (tests pass, answer matches).
- Process reward `lesson term` — Scores each reasoning step, not just the final answer.

## Ships

- [[Artifacts/09-12 game-rl-designer|game-rl-designer]] `skill` — Design a game-RL or reasoning-RL training pipeline (AlphaZero / MuZero / GRPO) for a given domain.

## Further reading

- [[Resources/DeepSeek-AI (2024). DeepSeekMath- Pushing the Limits of Mathematical Reasoning in Open Language Models (GRPO)|DeepSeek-AI (2024). DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models (GRPO)]] ([link](https://arxiv.org/abs/2402.03300)) — the paper that introduced GRPO and the group-relative baseline. ·  also cited by 1 other lesson
- [[Resources/DeepSeek-AI (2025). DeepSeek-R1- Incentivizing Reasoning Capability in LLMs via Reinforcement Learning|DeepSeek-AI (2025). DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning]] ([link](https://arxiv.org/abs/2501.12948)) — the full four-stage R1 recipe plus the R1-Zero ablation. ·  also cited by 4 other lessons
- [[Resources/Tesauro (1995). TD-Gammon, A Self-Teaching Backgammon Program|Tesauro (1995). TD-Gammon, A Self-Teaching Backgammon Program]] ([link](https://dl.acm.org/doi/10.1145/203330.203343)) — the paper that started it all. ·  also cited by 1 other lesson
- Qwen Team (2024). Qwen2.5-Math — GRPO replication ([link](https://github.com/QwenLM/Qwen2.5-Math)) — open replication of the R1 recipe at multiple scales.
- Hugging Face TRL — GRPOTrainer ([link](https://huggingface.co/docs/trl/main/en/grpo_trainer)) — the production reference for applying GRPO with custom reward functions.
- [[Resources/Sutton & Barto (2018). Reinforcement Learning- An Introduction, 2nd ed|Sutton & Barto (2018). Reinforcement Learning: An Introduction, 2nd ed.]] ([link](http://incompleteideas.net/book/RLbook2020.pdf)) — the textbook framing for self-play, search, and "designed reward" that R1 instantiates at LLM scale. ·  also cited by 10 other lessons
- [[Resources/Silver et al. (2017). Mastering the game of Go without human knowledge (AlphaGo Zero)|Silver et al. (2017). Mastering the game of Go without human knowledge (AlphaGo Zero)]] ([link](https://www.nature.com/articles/nature24270)) ·  also cited by 1 other lesson
- [[Resources/Vinyals et al. (2019). Grandmaster level in StarCraft II using multi-agent reinforcement learning (AlphaStar)|Vinyals et al. (2019). Grandmaster level in StarCraft II using multi-agent reinforcement learning (AlphaStar)]] ([link](https://www.nature.com/articles/s41586-019-1724-z)) ·  also cited by 1 other lesson
- Schrittwieser et al. (2020). Mastering Atari, Go, chess and shogi by planning with a learned model (MuZero) ([link](https://www.nature.com/articles/s41586-020-03051-4))
- Silver et al. (2018). A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play (AlphaZero) ([link](https://www.science.org/doi/10.1126/science.aar6404))
- Brown et al. (2019). Superhuman AI for multiplayer poker (Pluribus) ([link](https://www.science.org/doi/10.1126/science.aay2400)) — CFR + deep-learning at scale.


%% ── my notes ── %%
