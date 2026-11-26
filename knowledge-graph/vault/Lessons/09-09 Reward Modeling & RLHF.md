---
id: "lesson:09/09"
type: lesson
ref: 09/09
phase: 9
num: 9
title: "Reward Modeling & RLHF"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 8
prereqs: 2
community: 75
aliases:
  - 09/09
  - 09-09
tags:
  - phase/09
  - type/build
  - community/75
  - stdlib-only
source: ai-engineering-from-scratch/phases/09-reinforcement-learning/09-reward-modeling-rlhf/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/09-reward-modeling-rlhf"
---

# 09/09 Reward Modeling & RLHF

> Humans cannot write a reward function for "good assistant response," but they can compare two responses and pick the better one. Fit a reward model to those comparisons, then RL the language model against it. Christiano 2017. InstructGPT 2022. The recipe that turned GPT-3 into ChatGPT. In 2026 it is mostly being replaced by DPO — but the mental model stays.

**Phase:** [[Phases/09 Reinforcement Learning|Phase 9: Reinforcement Learning]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/09-reinforcement-learning/09-reward-modeling-rlhf/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/09-reinforcement-learning/09-reward-modeling-rlhf) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/09-reinforcement-learning/09-reward-modeling-rlhf) · code: main.py  
**Community:** [[Communities/75 L2 regularization · PRM · Reward Model|75 L2 regularization · PRM · Reward Model]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 5 · 05 (Sentiment), Phase 9 · 08 (PPO)`

- [[Lessons/05-05 Sentiment Analysis|05/05 Sentiment Analysis]] — Sentiment
- [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]] — PPO

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/02-14 Naive Bayes|02/14 Naive Bayes]], [[Lessons/05-02 Bag of Words, TF-IDF, and Text Representation|05/02 Bag of Words, TF-IDF, and Text Representation]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-07 Actor-Critic — A2C and A3C|09/07 Actor-Critic — A2C and A3C]]
- depth 3: [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/02-02 Linear Regression|02/02 Linear Regression]], [[Lessons/02-03 Logistic Regression|02/03 Logistic Regression]], [[Lessons/02-04 Decision Trees and Random Forests|02/04 Decision Trees and Random Forests]], [[Lessons/02-05 Support Vector Machines|02/05 Support Vector Machines]], [[Lessons/02-06 K-Nearest Neighbors and Distances|02/06 K-Nearest Neighbors and Distances]], [[Lessons/02-07 Unsupervised Learning|02/07 Unsupervised Learning]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/05-01 Text Processing — Tokenization, Stemming, Lemmatization|05/01 Text Processing — Tokenization, Stemming, Lemmatization]], [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]], [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]]

## Builds on this

- [[Lessons/09-12 RL for Games — AlphaZero, MuZero, and the LLM-Reasoning Era|09/12 RL for Games — AlphaZero, MuZero, and the LLM-Reasoning Era]]

## Concepts taught

- [[Concepts/RLHF (Reinforcement Learning from Human Feedback)|RLHF (Reinforcement Learning from Human Feedback)]] (as *RLHF*) `glossary` — Three-stage SFT + RM + PPO pipeline (Christiano 2017, Ouyang 2022).
- [[Concepts/Reward Model|Reward Model]] (as *Reward Model (RM)*) `lesson term` — Learned scalar function fit to pairwise preferences via Bradley-Terry.
- [[Concepts/Bradley-Terry|Bradley-Terry]] `lesson term` — P(y+ ≻ y-) = σ(R(y+) - R(y-)); the standard RM objective.
- [[Concepts/KL penalty|KL penalty]] `lesson term` — β · KL(πθ || πref) in the reward; the anti-reward-hacking regularizer.
- [[Concepts/Reward hacking|Reward hacking]] `lesson term` — Policy exploits RM flaws; symptoms: reward up, human eval flat.
- [[Concepts/RLAIF|RLAIF]] `lesson term` — RLHF where labels come from another LM instead of humans.
- [[Concepts/PRM|PRM]] `lesson term` — Scores partial reasoning steps; used in reasoning pipelines.
- [[Concepts/Constitutional AI|Constitutional AI]] `lesson term` — AI-generated preferences guided by explicit rules.

## Ships

- [[Artifacts/09-09 rlhf-architect|rlhf-architect]] `skill` — Design an RLHF / DPO / GRPO alignment pipeline for a language model, including RM, KL, and data strategy.

## Further reading

- [[Resources/Christiano et al. (2017). Deep Reinforcement Learning from Human Preferences|Christiano et al. (2017). Deep Reinforcement Learning from Human Preferences]] ([link](https://arxiv.org/abs/1706.03741)) — the paper that started RLHF. ·  also cited by 2 other lessons
- [[Resources/Stiennon et al. (2020). Learning to summarize with human feedback|Stiennon et al. (2020). Learning to summarize with human feedback]] ([link](https://arxiv.org/abs/2009.01325)) — earlier RLHF for summarization. ·  also cited by 2 other lessons
- [[Resources/InstructGPT paper|InstructGPT paper]] ([link](https://arxiv.org/abs/2203.02155)) — the recipe behind ChatGPT. ·  also cited by 4 other lessons
- [[Resources/Anthropic RLHF paper (Bai et al. 2022). Training a Helpful and Harmless Assistant|Anthropic RLHF paper (Bai et al. 2022). Training a Helpful and Harmless Assistant]] ([link](https://arxiv.org/abs/2204.05862)) — the HH paper. ·  also cited by 2 other lessons
- [[Resources/Bai et al. (2022). Constitutional AI- Harmlessness from AI Feedback|Bai et al. (2022). Constitutional AI: Harmlessness from AI Feedback]] ([link](https://arxiv.org/abs/2212.08073)) — RLAIF and self-critique loop. ·  also cited by 2 other lessons
- [[Resources/Direct Preference Optimization paper|Direct Preference Optimization paper]] ([link](https://arxiv.org/abs/2305.18290)) — DPO; the post-RLHF default in 2026. ·  also cited by 3 other lessons
- von Werra et al. (2020). TRL: Transformer Reinforcement Learning ([link](https://github.com/huggingface/trl)) — the library; `examples/` has end-to-end RLHF scripts for Llama, Mistral, and Qwen.
- Hugging Face — Illustrating Reinforcement Learning from Human Feedback ([link](https://huggingface.co/blog/rlhf)) — by Lambert, Castricato, von Werra, Havrilla — the canonical walk-through of the three-stage pipeline with diagrams.
- [[Resources/Hugging Face TRL library|Hugging Face TRL library]] ([link](https://huggingface.co/docs/trl)) — production `RewardTrainer` and `PPOTrainer`. Read the trainer source for the adaptive-KL and value-head details. ·  also cited by 2 other lessons
- [[Resources/Sutton & Barto (2018). Reinforcement Learning- An Introduction, 2nd ed|Sutton & Barto (2018). Reinforcement Learning: An Introduction, 2nd ed.]] ([link](http://incompleteideas.net/book/RLbook2020.pdf)) — the reward-hypothesis view; essential prerequisite for thinking about reward hacking. ·  also cited by 10 other lessons


%% ── my notes ── %%
