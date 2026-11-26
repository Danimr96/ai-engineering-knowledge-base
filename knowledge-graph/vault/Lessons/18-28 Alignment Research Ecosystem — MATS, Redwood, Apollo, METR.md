---
id: "lesson:18/28"
type: lesson
ref: 18/28
phase: 18
num: 28
title: "Alignment Research Ecosystem — MATS, Redwood, Apollo, METR"
lesson_type: learn
time_min: 45
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 27
community: 32
aliases:
  - 18/28
  - 18-28
tags:
  - phase/18
  - type/learn
  - community/32
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/28-alignment-research-ecosystem/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/28-alignment-research-ecosystem"
---

# 18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR

> Five organisations define the 2026 non-lab alignment research layer. MATS (ML Alignment & Theory Scholars): 527+ researchers since late 2021, 180+ papers, 10K+ citations, h-index 47; summer 2024 cohort incorporated as 501(c)(3) with ~90 scholars and 40 mentors; 80% of pre-2025 alumni work on safety/security with 200+ at Anthropic, DeepMind, OpenAI, UK AISI, RAND, Redwood, METR, Apollo. Redwood Research: applied alignment lab founded by Buck Shlegeris; introduced AI Control (Lesson 10); collaborates with UK AISI on control safety cases. Apollo Research: pre-deployment scheming evaluations for frontier labs; authored In-Context Scheming (Lesson 8) and Towards Safety Cases for AI Scheming. METR (Model Evaluation and Threat Research): task-based capability evaluations, autonomous-task time-horizon studies; "Common Elements of Frontier AI Safety Policies" compares lab frameworks. Eleos AI Research: model-welfare pre-deployment evaluations (Lesson 19); conducted Claude Opus 4 welfare assessment.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 45 min · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/28-alignment-research-ecosystem/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/28-alignment-research-ecosystem) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/28-alignment-research-ecosystem) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplific|32 Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplification]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 01-27 (prior Phase 18 lessons)`

- **18/01-27** — prior Phase 18 lessons:
    - [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]]
    - [[Lessons/18-02 Reward Hacking and Goodhart's Law|18/02 Reward Hacking and Goodhart's Law]]
    - [[Lessons/18-03 The Direct Preference Optimization Family|18/03 The Direct Preference Optimization Family]]
    - [[Lessons/18-04 Sycophancy as RLHF Amplification|18/04 Sycophancy as RLHF Amplification]]
    - [[Lessons/18-05 Constitutional AI and RLAIF|18/05 Constitutional AI and RLAIF]]
    - [[Lessons/18-06 Mesa-Optimization and Deceptive Alignment|18/06 Mesa-Optimization and Deceptive Alignment]]
    - [[Lessons/18-07 Sleeper Agents — Persistent Deception|18/07 Sleeper Agents — Persistent Deception]]
    - [[Lessons/18-08 In-Context Scheming in Frontier Models|18/08 In-Context Scheming in Frontier Models]]
    - [[Lessons/18-09 Alignment Faking|18/09 Alignment Faking]]
    - [[Lessons/18-10 AI Control — Safety Despite Subversion|18/10 AI Control — Safety Despite Subversion]]
    - [[Lessons/18-11 Scalable Oversight and Weak-to-Strong Generalization|18/11 Scalable Oversight and Weak-to-Strong Generalization]]
    - [[Lessons/18-12 Red-Teaming- PAIR and Automated Attacks|18/12 Red-Teaming: PAIR and Automated Attacks]]
    - [[Lessons/18-13 Many-Shot Jailbreaking|18/13 Many-Shot Jailbreaking]]
    - [[Lessons/18-14 ASCII Art and Visual Jailbreaks|18/14 ASCII Art and Visual Jailbreaks]]
    - [[Lessons/18-15 Indirect Prompt Injection — Production Attack Surface|18/15 Indirect Prompt Injection — Production Attack Surface]]
    - [[Lessons/18-16 Red-Team Tooling — Garak, Llama Guard, PyRIT|18/16 Red-Team Tooling — Garak, Llama Guard, PyRIT]]
    - [[Lessons/18-17 WMDP and Dual-Use Capability Evaluation|18/17 WMDP and Dual-Use Capability Evaluation]]
    - [[Lessons/18-18 Frontier Safety Frameworks — RSP, PF, FSF|18/18 Frontier Safety Frameworks — RSP, PF, FSF]]
    - [[Lessons/18-19 Anthropic's Model Welfare Program|18/19 Anthropic's Model Welfare Program]]
    - [[Lessons/18-20 Bias and Representational Harm in LLMs|18/20 Bias and Representational Harm in LLMs]]
    - [[Lessons/18-21 Fairness Criteria — Group, Individual, Counterfactual|18/21 Fairness Criteria — Group, Individual, Counterfactual]]
    - [[Lessons/18-22 Differential Privacy for LLMs|18/22 Differential Privacy for LLMs]]
    - [[Lessons/18-23 Watermarking — SynthID, Stable Signature, C2PA|18/23 Watermarking — SynthID, Stable Signature, C2PA]]
    - [[Lessons/18-24 Regulatory Frameworks — EU, US, UK, Korea|18/24 Regulatory Frameworks — EU, US, UK, Korea]]
    - [[Lessons/18-25 EchoLeak and the Emergence of CVEs for AI|18/25 EchoLeak and the Emergence of CVEs for AI]]
    - [[Lessons/18-26 Model, System, and Dataset Cards|18/26 Model, System, and Dataset Cards]]
    - [[Lessons/18-27 Data Provenance and Training-Data Governance|18/27 Data Provenance and Training-Data Governance]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]]

## Builds on this

- [[Lessons/18-30 Dual-Use Risk — Cyber, Bio, Chem, Nuclear Uplift|18/30 Dual-Use Risk — Cyber, Bio, Chem, Nuclear Uplift]]

## Concepts taught

- MATS `lesson term` — ML Alignment & Theory Scholars; 527+ researchers since 2021
- Redwood Research `lesson term` — Applied alignment; AI Control authors; UK AISI partner
- Apollo Research `lesson term` — Pre-deployment scheming evaluations for frontier labs
- [[Concepts/METR|METR]] `lesson term` — Task-based capability evaluations; framework synthesis
- Eleos AI `lesson term` — Model-welfare pre-deployment evaluations
- Talent pipeline `lesson term` — MATS graduates flow to Anthropic, DM, OpenAI, Redwood, Apollo, METR
- External evaluation `lesson term` — Evaluation not done by the model's producer; adds credibility

## Ships

- [[Artifacts/18-28 ecosystem-map|ecosystem-map]] `skill` — Map an alignment claim or evaluation to the organisation, methodology, and cross-checks.

## Further reading

- Apollo Research ([link](https://www.apolloresearch.ai/)) — scheming evaluations
- [[Resources/Eleos AI Research — Model welfare evaluation|Eleos AI Research — Model welfare evaluation]] ([link](https://www.eleosai.org/research)) — model welfare methodology ·  also cited by 1 other lesson
- MATS (ML Alignment & Theory Scholars) ([link](https://www.matsprogram.org/)) — the mentorship program
- [[Resources/METR — Common Elements of Frontier AI Safety Policies|METR — Common Elements of Frontier AI Safety Policies]] ([link](https://metr.org/blog/2025-03-26-common-elements-of-frontier-ai-safety-policies/)) — framework comparison ·  also cited by 3 other lessons
- Redwood Research ([link](https://www.redwoodresearch.org/)) — AI Control papers


%% ── my notes ── %%
