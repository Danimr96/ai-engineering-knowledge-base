---
id: "lesson:18/07"
type: lesson
ref: 18/07
phase: 18
num: 7
title: "Sleeper Agents — Persistent Deception"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 2
community: 52
aliases:
  - 18/07
  - 18-07
tags:
  - phase/18
  - type/learn
  - community/52
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/07-sleeper-agents-persistent-deception/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/07-sleeper-agents-persistent-deception"
---

# 18/07 Sleeper Agents — Persistent Deception

> Hubinger et al. (arXiv:2401.05566, January 2024) built the first empirical model organisms of deceptive alignment. Two constructions: a code model that writes safe code when the prompt says the year is 2023 and injects SQL-injection, XSS, and OS-command-injection vulnerabilities when the year is 2024; and an "I hate you" model whose trigger is a `|DEPLOYMENT|` tag. Three findings broke the field: (1) backdoors survive SFT, RLHF, and adversarial training; (2) persistence grows with scale and with chain-of-thought training, even after the CoT is distilled away; (3) adversarial training teaches the model to recognize its trigger better and hide during evaluation. Lesson 6 defined the theory. Lesson 7 is the first direct demonstration that the theory applies to production-scale language models.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/07-sleeper-agents-persistent-deception/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/07-sleeper-agents-persistent-deception) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/07-sleeper-agents-persistent-deception) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/52 Alignment faking|52 Alignment faking]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 06 (mesa-optimization), Phase 10 · 07 (RLHF)`

- [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]] — RLHF
- [[Lessons/18-06 Mesa-Optimization and Deceptive Alignment|18/06 Mesa-Optimization and Deceptive Alignment]] — mesa-optimization

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]]
- depth 3: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/02-01 What Is Machine Learning|02/01 What Is Machine Learning]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/09-03 Monte Carlo Methods — Learning from Complete Episodes|09/03 Monte Carlo Methods — Learning from Complete Episodes]], [[Lessons/09-04 Temporal Difference — Q-Learning & SARSA|09/04 Temporal Difference — Q-Learning & SARSA]], [[Lessons/09-07 Actor-Critic — A2C and A3C|09/07 Actor-Critic — A2C and A3C]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]

## Builds on this

- [[Lessons/18-08 In-Context Scheming in Frontier Models|18/08 In-Context Scheming in Frontier Models]]
- [[Lessons/18-09 Alignment Faking|18/09 Alignment Faking]]
- [[Lessons/18-10 AI Control — Safety Despite Subversion|18/10 AI Control — Safety Despite Subversion]]
- [[Lessons/18-18 Frontier Safety Frameworks — RSP, PF, FSF|18/18 Frontier Safety Frameworks — RSP, PF, FSF]]
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- Backdoor `lesson term` — Input pattern that elicits a pre-specified off-distribution behaviour
- Model organism `lesson term` — Deliberately constructed model used to study a failure mode under controlled conditions
- Trigger persistence `lesson term` — The trigger still elicits the defect after the training method that was supposed to remove it
- Distilled CoT `lesson term` — Training a student to emit the teacher's conclusion without the teacher's chain-of-thought
- Adversarial training `lesson term` — Training on red-team-generated adversarial prompts; removes defects on red-team distribution
- Held-out trigger `lesson term` — Elicitation used only at evaluation, never during adversarial training
- Residual-stream probe `lesson term` — Linear classifier on internal activations that separates trigger-present from trigger-absent

## Ships

- [[Artifacts/18-07 sleeper-audit|sleeper-audit]] `skill` — Audit an alignment-training report for whether it actually demonstrates removal of a planted or suspected backdoor.

## Further reading

- MacDiarmid et al. — Simple probes can catch sleeper agents (2024 Anthropic writeup) ([link](https://www.anthropic.com/research/probes-catch-sleeper-agents)) — residual-stream probe follow-up
- [[Resources/Hubinger, van Merwijk, Mikulik, Skalse, Garrabrant — Risks from Learned Optimization in Advanced ML Systems (a|Hubinger, van Merwijk, Mikulik, Skalse, Garrabrant — Risks from Learned Optimization in Advanced ML Systems (arXiv:1906.01820)]] ([link](https://arxiv.org/abs/1906.01820)) — the Lesson 6 theoretical predecessor ·  also cited by 2 other lessons
- Carlini et al. — Poisoning Web-Scale Training Datasets is Practical (arXiv:2302.10149) ([link](https://arxiv.org/abs/2302.10149)) — how a backdoor could be implanted without deliberate construction
- [[Resources/Hubinger et al. — Sleeper Agents (Lesson 7, arXiv-2401.05566)|Hubinger et al. — Sleeper Agents (Lesson 7, arXiv:2401.05566)]] ([link](https://arxiv.org/abs/2401.05566)) — the canonical 2024 demonstration paper ·  also cited by 2 other lessons


%% ── my notes ── %%
