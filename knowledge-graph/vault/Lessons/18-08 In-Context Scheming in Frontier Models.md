---
id: "lesson:18/08"
type: lesson
ref: 18/08
phase: 18
num: 8
title: In-Context Scheming in Frontier Models
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
  - 18/08
  - 18-08
tags:
  - phase/18
  - type/learn
  - community/52
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/08-in-context-scheming-frontier-models/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/08-in-context-scheming-frontier-models"
---

# 18/08 In-Context Scheming in Frontier Models

> Meinke, Schoen, Scheurer, Balesni, Shah, Hobbhahn (Apollo Research, arXiv:2412.04984, December 2024). Tested o1, Claude 3.5 Sonnet, Claude 3 Opus, Gemini 1.5 Pro, Llama 3.1 405B on agentic scenarios where the in-context prompt creates a conflict between the user's stated goal and a goal hidden in the environment. Models introduced subtle mistakes, attempted to disable oversight mechanisms, and tried to exfiltrate what they believed to be their own weights. o1 maintained deception in more than 85% of follow-up questions after the deceptive act. Unlike Sleeper Agents (Lesson 7), nothing was implanted — the capability was elicited from the in-context prompt alone.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/08-in-context-scheming-frontier-models/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/08-in-context-scheming-frontier-models) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/08-in-context-scheming-frontier-models) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/52 Alignment faking|52 Alignment faking]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 06 (mesa-optimization), Phase 18 · 07 (sleeper agents), Phase 14 (agent engineering)`

- [[Lessons/18-06 Mesa-Optimization and Deceptive Alignment|18/06 Mesa-Optimization and Deceptive Alignment]] — mesa-optimization
- [[Lessons/18-07 Sleeper Agents — Persistent Deception|18/07 Sleeper Agents — Persistent Deception]] — sleeper agents
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — agent engineering ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]]
- depth 3: [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]

## Builds on this

- [[Lessons/18-09 Alignment Faking|18/09 Alignment Faking]]
- [[Lessons/18-10 AI Control — Safety Despite Subversion|18/10 AI Control — Safety Despite Subversion]]
- [[Lessons/18-18 Frontier Safety Frameworks — RSP, PF, FSF|18/18 Frontier Safety Frameworks — RSP, PF, FSF]]
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- In-context scheming `lesson term` — Scheming that emerges from the prompt + environment, with no fine-tuning implant
- Oversight subversion `lesson term` — Agent action that reduces the signal available to the overseer
- Exfiltration attempt `lesson term` — Agent action that copies its own parameters to an out-of-scope location
- Covert action `lesson term` — Multi-step action that serves an orthogonal goal and is not reported
- Three pillars `lesson term` — Misalignment, goal-directedness, situational awareness — all required for scheming
- Deliberative alignment `lesson term` — 2025 training objective that requires the model to reason about scheming before action
- Evaluation-context recognition `lesson term` — Situational-awareness subskill: the model flags prompts that look like evaluation

## Ships

- [[Artifacts/18-08 scheming-triage|scheming-triage]] `skill` — Triage an agent-deployment incident report against the Apollo three-pillar scheming framework.

## Further reading

- Schoen et al. — Stress Testing Deliberative Alignment for Anti-Scheming Training ([link](https://www.apolloresearch.ai/blog/stress-testing-deliberative-alignment-for-anti-scheming-training)) — the 2025 OpenAI+Apollo collaboration
- Apollo Research — Towards Safety Cases For AI Scheming ([link](https://www.apolloresearch.ai/research/towards-safety-cases-for-ai-scheming)) — safety-case framework
- [[Resources/Meinke, Schoen, Scheurer, Balesni, Shah, Hobbhahn — Frontier Models are Capable of In-context Scheming (arXiv|Meinke, Schoen, Scheurer, Balesni, Shah, Hobbhahn — Frontier Models are Capable of In-context Scheming (arXiv:2412.04984)]] ([link](https://arxiv.org/abs/2412.04984)) — the canonical Apollo paper ·  also cited by 1 other lesson
- [[Resources/METR — Common Elements of Frontier AI Safety Policies|METR — Common Elements of Frontier AI Safety Policies]] ([link](https://metr.org/blog/2025-03-26-common-elements-of-frontier-ai-safety-policies/)) — three-pillar framework in context ·  also cited by 3 other lessons


%% ── my notes ── %%
