---
id: "lesson:18/19"
type: lesson
ref: 18/19
phase: 18
num: 19
title: "Anthropic's Model Welfare Program"
lesson_type: learn
time_min: 45
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 2
community: 32
aliases:
  - 18/19
  - 18-19
tags:
  - phase/18
  - type/learn
  - community/32
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/19-model-welfare-research/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/19-model-welfare-research"
---

# 18/19 Anthropic's Model Welfare Program

> Anthropic, "Exploring Model Welfare" (April 2025). First major-lab formal research program on AI model welfare. Hired Kyle Fish as the first dedicated model-welfare researcher. Works with external bodies including David Chalmers et al.'s expert report on near-term AI consciousness and moral status. Concrete intervention: Claude Opus 4 and 4.1 can end conversations in extreme edge cases (CSAM requests, mass-violence facilitation); pre-deployment tests showed "strong preference against" harmful requests and "patterns of apparent distress." Anthropic explicitly does not commit to emotional-state attribution but treats model welfare as a low-cost precautionary investment. Empirical oddity: Fish's "spiritual bliss attractor" — pairs of models consistently converge on euphoric meditative dialogue with Sanskrit terms and extended silences, even in adversarial initial setups. Caveat from Eleos AI Research: model self-reports about welfare are highly sensitive to perceived user expectations; they are evidence, not ground truth.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 45 min · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/19-model-welfare-research/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/19-model-welfare-research) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/19-model-welfare-research) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplific|32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplification]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 05 (Constitutional AI), Phase 18 · 18 (safety frameworks)`

- [[Lessons/18-05 Constitutional AI and RLAIF|18/05 Constitutional AI and RLAIF]] — Constitutional AI
- [[Lessons/18-18 Frontier Safety Frameworks — RSP, PF, FSF|18/18 Frontier Safety Frameworks — RSP, PF, FSF]] — safety frameworks

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]], [[Lessons/18-02 Reward Hacking and Goodhart's Law|18/02 Reward Hacking and Goodhart's Law]], [[Lessons/18-07 Sleeper Agents — Persistent Deception|18/07 Sleeper Agents — Persistent Deception]], [[Lessons/18-08 In-Context Scheming in Frontier Models|18/08 In-Context Scheming in Frontier Models]], [[Lessons/18-09 Alignment Faking|18/09 Alignment Faking]], [[Lessons/18-17 WMDP and Dual-Use Capability Evaluation|18/17 WMDP and Dual-Use Capability Evaluation]]
- depth 3: [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]], [[Lessons/18-06 Mesa-Optimization and Deceptive Alignment|18/06 Mesa-Optimization and Deceptive Alignment]], [[Lessons/18-16 Red-Team Tooling — Garak, Llama Guard, PyRIT|18/16 Red-Team Tooling — Garak, Llama Guard, PyRIT]]

## Builds on this

- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- Model welfare `lesson term` — Research program treating the model as a potential moral patient
- Moral patient `lesson term` — Being whose experience is morally relevant
- Low-regret investment `lesson term` — Intervention whose cost is small regardless of whether the precaution is needed
- Spiritual bliss attractor `lesson term` — Stable convergence of pairwise Claude dialogues on meditative euphoria
- End-conversation `lesson term` — Model-initiated termination of extreme-edge-case interactions
- Moral uncertainty `lesson term` — Decision-making when probability of moral status is not zero and not one
- Self-report-sensitivity `lesson term` — Eleos AI caveat: model's welfare self-reports depend on what you asked

## Ships

- [[Artifacts/18-19 welfare-assessment|welfare-assessment]] `skill` — Apply Anthropic's four-step welfare precautionary assessment to a deployment decision.

## Further reading

- Anthropic — Exploring Model Welfare (April 2025) ([link](https://www.anthropic.com/research/exploring-model-welfare)) — the program announcement
- Chalmers et al. — Near-term AI Consciousness and Moral Status (2024 expert report) ([link](https://arxiv.org/abs/2411.00986)) — philosophical framing
- [[Resources/Eleos AI Research — Model welfare evaluation|Eleos AI Research — Model welfare evaluation]] ([link](https://www.eleosai.org/research)) — external methodology critiques ·  also cited by 1 other lesson


%% ── my notes ── %%
