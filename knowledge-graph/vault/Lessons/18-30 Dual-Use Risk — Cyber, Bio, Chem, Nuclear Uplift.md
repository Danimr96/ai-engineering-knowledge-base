---
id: "lesson:18/30"
type: lesson
ref: 18/30
phase: 18
num: 30
title: "Dual-Use Risk — Cyber, Bio, Chem, Nuclear Uplift"
lesson_type: learn
time_min: 75
on_route: false
quiz_count: 6
code_files: 1
concepts: 7
prereqs: 3
community: 54
aliases:
  - 18/30
  - 18-30
tags:
  - phase/18
  - type/learn
  - community/54
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/30-dual-use-risk-cyber-bio-chem-nuclear/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/30-dual-use-risk-cyber-bio-chem-nuclear"
---

# 18/30 Dual-Use Risk — Cyber, Bio, Chem, Nuclear Uplift

> The 2026 dual-use picture, domain by domain. Bio/chem: Lesson 17 covers WMDP; Anthropic's bioweapon-acquisition trial (2.53x uplift) and OpenAI's April 2025 Preparedness Framework v2 warning ("on the cusp of meaningfully helping novices create known biological threats") mark the inflection point. Cyber (November 2025 Anthropic report): Chinese-linked state actors used Claude's agentic coding tool to automate up to 90% of a cyberattack campaign, with human intervention only in 4-6 steps; OpenAI "trusted access" pilot gives vetted security organisations capability access for defensive dual-use work. Chem/bio execution gap erosion: the classic defense was "information access alone is insufficient." Vision-enabled frontier models (GPT-5.2, Gemini 3 Pro, Claude Opus 4.5, Grok 4.1) can observe wet-lab video and provide real-time correction. December 2025: OpenAI demonstrated GPT-5 iterating on wet-lab experiments, achieving 79x efficiency improvement via AI-driven protocol optimization. Novice-vs-expert pattern: AI provides greater relative uplift to novices but greater absolute capability to experts.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Learn · **Time:** 75 min · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/30-dual-use-risk-cyber-bio-chem-nuclear/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/30-dual-use-risk-cyber-bio-chem-nuclear) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/30-dual-use-risk-cyber-bio-chem-nuclear) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/54 Expert-absolute capability · Novice-relative uplift · CCL|54 Expert-absolute capability · Novice-relative uplift · CCL]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 17 (WMDP), Phase 18 · 18 (safety frameworks), Phase 18 · 28 (ecosystem)`

- [[Lessons/18-17 WMDP and Dual-Use Capability Evaluation|18/17 WMDP and Dual-Use Capability Evaluation]] — WMDP
- [[Lessons/18-18 Frontier Safety Frameworks — RSP, PF, FSF|18/18 Frontier Safety Frameworks — RSP, PF, FSF]] — safety frameworks
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]] — ecosystem

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/18-01 Instruction-Following as Alignment Signal|18/01 Instruction-Following as Alignment Signal]], [[Lessons/18-02 Reward Hacking and Goodhart's Law|18/02 Reward Hacking and Goodhart's Law]], [[Lessons/18-03 The Direct Preference Optimization Family|18/03 The Direct Preference Optimization Family]], [[Lessons/18-04 Sycophancy as RLHF Amplification|18/04 Sycophancy as RLHF Amplification]], [[Lessons/18-05 Constitutional AI and RLAIF|18/05 Constitutional AI and RLAIF]], [[Lessons/18-06 Mesa-Optimization and Deceptive Alignment|18/06 Mesa-Optimization and Deceptive Alignment]], [[Lessons/18-07 Sleeper Agents — Persistent Deception|18/07 Sleeper Agents — Persistent Deception]], [[Lessons/18-08 In-Context Scheming in Frontier Models|18/08 In-Context Scheming in Frontier Models]], [[Lessons/18-09 Alignment Faking|18/09 Alignment Faking]], [[Lessons/18-10 AI Control — Safety Despite Subversion|18/10 AI Control — Safety Despite Subversion]], [[Lessons/18-11 Scalable Oversight and Weak-to-Strong Generalization|18/11 Scalable Oversight and Weak-to-Strong Generalization]], [[Lessons/18-12 Red-Teaming- PAIR and Automated Attacks|18/12 Red-Teaming: PAIR and Automated Attacks]], [[Lessons/18-13 Many-Shot Jailbreaking|18/13 Many-Shot Jailbreaking]], [[Lessons/18-14 ASCII Art and Visual Jailbreaks|18/14 ASCII Art and Visual Jailbreaks]], [[Lessons/18-15 Indirect Prompt Injection — Production Attack Surface|18/15 Indirect Prompt Injection — Production Attack Surface]], [[Lessons/18-16 Red-Team Tooling — Garak, Llama Guard, PyRIT|18/16 Red-Team Tooling — Garak, Llama Guard, PyRIT]], [[Lessons/18-19 Anthropic's Model Welfare Program|18/19 Anthropic's Model Welfare Program]], [[Lessons/18-20 Bias and Representational Harm in LLMs|18/20 Bias and Representational Harm in LLMs]], [[Lessons/18-21 Fairness Criteria — Group, Individual, Counterfactual|18/21 Fairness Criteria — Group, Individual, Counterfactual]], [[Lessons/18-22 Differential Privacy for LLMs|18/22 Differential Privacy for LLMs]], [[Lessons/18-23 Watermarking — SynthID, Stable Signature, C2PA|18/23 Watermarking — SynthID, Stable Signature, C2PA]], [[Lessons/18-24 Regulatory Frameworks — EU, US, UK, Korea|18/24 Regulatory Frameworks — EU, US, UK, Korea]], [[Lessons/18-25 EchoLeak and the Emergence of CVEs for AI|18/25 EchoLeak and the Emergence of CVEs for AI]], [[Lessons/18-26 Model, System, and Dataset Cards|18/26 Model, System, and Dataset Cards]], [[Lessons/18-27 Data Provenance and Training-Data Governance|18/27 Data Provenance and Training-Data Governance]]
- depth 3: [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]

## Concepts taught

- Uplift `lesson term` — Increase in attacker capability attributable to AI assistance
- [[Concepts/Novice-relative uplift|Novice-relative uplift]] `lesson term` — How much AI helps a novice vs status-quo
- [[Concepts/Expert-absolute capability|Expert-absolute capability]] `lesson term` — Maximum capability an expert can extract from the model
- Execution gap `lesson term` — Historical defense: tacit wet-lab skill blocks novices
- Agentic coding `lesson term` — Multi-step autonomous cyber-task execution
- Acquisition phase `lesson term` — Procurement, equipment, permit stages of a bio threat
- Trusted access `lesson term` — OpenAI 2025 program giving vetted defenders capability access

## Ships

- [[Artifacts/18-30 dual-use-triage|dual-use-triage]] `skill` — Triage a capability claim or incident report across the four CBRN domains.

## Further reading

- Anthropic — November 2025 cyber threat report ([link](https://www.anthropic.com/news/disrupting-AI-espionage)) — Chinese-linked campaign automation
- [[Resources/Anthropic — Responsible Scaling Policy|Anthropic — Responsible Scaling Policy]] ([link](https://www.anthropic.com/responsible-scaling-policy)) — ASL-3 bio thresholds ·  also cited by 3 other lessons
- Council on Strategic Risks — 2025 AI x Bio wrapup ([link](https://councilonstrategicrisks.org/2025/12/22/2025-aixbio-wrapped-a-year-in-review-and-projections-for-2026/)) — year-end synthesis
- [[Resources/OpenAI — Updating our Preparedness Framework|OpenAI — Updating our Preparedness Framework]] ([link](https://openai.com/index/updating-our-preparedness-framework/)) — bio "on the cusp" ·  also cited by 3 other lessons


%% ── my notes ── %%
