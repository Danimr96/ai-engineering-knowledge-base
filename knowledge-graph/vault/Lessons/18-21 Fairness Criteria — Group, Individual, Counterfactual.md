---
id: "lesson:18/21"
type: lesson
ref: 18/21
phase: 18
num: 21
title: "Fairness Criteria — Group, Individual, Counterfactual"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 1
community: 32
aliases:
  - 18/21
  - 18-21
tags:
  - phase/18
  - type/learn
  - community/32
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/21-fairness-criteria-group-individual-counterfactual/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/21-fairness-criteria-group-individual-counterfactual"
---

# 18/21 Fairness Criteria — Group, Individual, Counterfactual

> Three families structure the fairness literature. Group fairness: demographic parity, equalized odds, conditional use accuracy equality — equal rates across protected groups on average. Individual fairness (Dwork et al. 2012): similar individuals receive similar decisions; Lipschitz condition on the decision map. Counterfactual fairness (Kusner et al. 2017): a decision is fair to an individual if it is unchanged when sensitive attributes are counterfactually altered. 2024 theoretical result (NeurIPS 2024): there is an inherent CF-vs-accuracy trade-off; a model-agnostic method converts an optimal-but-unfair predictor into a CF one with bounded accuracy loss. Backtracking counterfactuals (arXiv:2401.13935, January 2024): new paradigm that avoids requiring interventions on legally protected attributes. Philosophical reconciliation (ICLR Blogposts 2024): with causal graphs, satisfying certain group fairness measures entails counterfactual fairness.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/21-fairness-criteria-group-individual-counterfactual/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/21-fairness-criteria-group-individual-counterfactual) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/21-fairness-criteria-group-individual-counterfactual) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplific|32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplification]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 20 (bias), Phase 02 (classical ML)`

- [[Lessons/18-20 Bias and Representational Harm in LLMs|18/20 Bias and Representational Harm in LLMs]] — bias
- Whole phase: [[Phases/02 ML Fundamentals|Phase 2: ML Fundamentals]] — classical ML ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]]
- depth 3: [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]

## Builds on this

- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- Demographic parity `lesson term` — A=a) equal across groups
- Equalized odds `lesson term` — Equal true-positive and false-positive rates across groups
- Conditional use accuracy `lesson term` — Equal predictive values across groups
- Individual fairness `lesson term` — Similar individuals get similar decisions
- Counterfactual fairness `lesson term` — Decision unchanged under counterfactual attribute alteration
- Backtracking counterfactual `lesson term` — Counterfactual reasoned backward from outcome, not forward from attribute
- Impossibility theorem `lesson term` — Chouldechova / KMR 2017: group criteria mutually exclusive under unequal base rates

## Ships

- [[Artifacts/18-21 fairness-criterion|fairness-criterion]] `skill` — Identify which fairness criterion a claim invokes and audit the associated assumptions.

## Further reading

- Dwork et al. — Fairness through Awareness (arXiv:1104.3913) ([link](https://arxiv.org/abs/1104.3913)) — individual fairness
- Chouldechova — Fair prediction with disparate impact (arXiv:1703.00056) ([link](https://arxiv.org/abs/1703.00056)) — impossibility
- Kusner, Loftus, Russell, Silva — Counterfactual Fairness (arXiv:1703.06856) ([link](https://arxiv.org/abs/1703.06856)) — counterfactual fairness
- Backtracking Counterfactuals (arXiv:2401.13935) ([link](https://arxiv.org/abs/2401.13935)) — new paradigm for protected-attribute interventions


%% ── my notes ── %%
