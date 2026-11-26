---
id: "lesson:18/10"
type: lesson
ref: 18/10
phase: 18
num: 10
title: "AI Control — Safety Despite Subversion"
lesson_type: learn
languages:
  - Python
time_min: 75
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 3
community: 52
aliases:
  - 18/10
  - 18-10
tags:
  - phase/18
  - type/learn
  - community/52
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/10-ai-control-subversion/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/10-ai-control-subversion"
---

# 18/10 AI Control — Safety Despite Subversion

> Greenblatt, Shlegeris, Sachan, Roger (Redwood Research, arXiv:2312.06942, ICML 2024). Control reframes the safety question: given an untrusted strong model U that may be adversarially optimizing against you, what protocols let you extract useful work while bounding the probability of an unacceptable outcome? Resources are a trusted weaker model T, a budget of trusted human labor H, and the ability to edit U's outputs. Within this frame, Trusted Editing Pareto-dominates Untrusted Monitoring on code-backdoor tasks. The frame inherits worst-case assumptions from security engineering: safety is the probability that an adversarially chosen U cannot cause a concrete unacceptable outcome, measured under red-team pressure that stands in for U.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 75 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/10-ai-control-subversion/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/10-ai-control-subversion) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/10-ai-control-subversion) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/52 Alignment faking|52 Alignment faking]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 07 (sleeper agents), Phase 18 · 08 (scheming), Phase 18 · 09 (alignment faking)`

- [[Lessons/18-07 Sleeper Agents — Persistent Deception|18/07 Sleeper Agents — Persistent Deception]] — sleeper agents
- [[Lessons/18-08 In-Context Scheming in Frontier Models|18/08 In-Context Scheming in Frontier Models]] — scheming
- [[Lessons/18-09 Alignment Faking|18/09 Alignment Faking]] — alignment faking

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/18-06 Mesa-Optimization and Deceptive Alignment|18/06 Mesa-Optimization and Deceptive Alignment]]
- depth 3: [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]]

## Builds on this

- [[Lessons/18-11 Scalable Oversight and Weak-to-Strong Generalization|18/11 Scalable Oversight and Weak-to-Strong Generalization]]
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- AI Control `lesson term` — Protocol design that bounds unacceptable outcomes under a worst-case U
- Untrusted model (as *Untrusted model (U)*) `lesson term` — The capable model we want to extract work from but do not trust
- Trusted model (as *Trusted model (T)*) `lesson term` — A weaker model, known not to be adversarial, used as editor/monitor
- Trusted human (as *Trusted human (H)*) `lesson term` — Bounded expert labor; expensive; the ground-truth signal
- Trusted Editing `lesson term` — Protocol where T is the gate on U's outputs; H called on ambiguous outputs
- Untrusted Monitoring `lesson term` — Protocol where a second U instance scores outputs; collusion-resistant only with extra investment
- Control safety case `lesson term` — Written argument that a protocol bounds the adversary's success under worst-case U

## Ships

- [[Artifacts/18-10 control-protocol-audit|control-protocol-audit]] `skill` — Audit a deployment protocol under the AI Control threat model.

## Further reading

- Greenblatt, Shlegeris, Sachan, Roger — AI Control (arXiv:2312.06942) ([link](https://arxiv.org/abs/2312.06942)) — the canonical ICML 2024 paper
- [[Resources/Hubinger et al. — Sleeper Agents (Lesson 7, arXiv-2401.05566)|Hubinger et al. — Sleeper Agents (Lesson 7, arXiv:2401.05566)]] ([link](https://arxiv.org/abs/2401.05566)) — the threat model control assumes ·  also cited by 2 other lessons
- [[Resources/METR — Common Elements of Frontier AI Safety Policies|METR — Common Elements of Frontier AI Safety Policies]] ([link](https://metr.org/blog/2025-03-26-common-elements-of-frontier-ai-safety-policies/)) — operationalization for frontier labs ·  also cited by 3 other lessons
- Redwood Research — Recent AI Control papers index ([link](https://redwoodresearch.substack.com/)) — 2024-2025 follow-ups


%% ── my notes ── %%
