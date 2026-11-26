---
id: "lesson:18/26"
type: lesson
ref: 18/26
phase: 18
num: 26
title: "Model, System, and Dataset Cards"
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 8
prereqs: 2
community: 87
aliases:
  - 18/26
  - 18-26
tags:
  - phase/18
  - type/build
  - community/87
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/26-model-system-dataset-cards/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/26-model-system-dataset-cards"
---

# 18/26 Model, System, and Dataset Cards

> Three documentation formats structure AI transparency. Model Cards (Mitchell et al. 2019) — nutrition labels for models: training data, quantitative disaggregated analyses, ethical considerations, caveats; only 0.3% of Hugging Face model cards document ethical considerations (Oreamuno et al. 2023). Datasheets for Datasets (Gebru et al. 2018, CACM) — motivation, composition, collection process, labeling, distribution, maintenance; electronics-datasheet analogy. Data Cards (Pushkarna et al., Google 2022) — modular layered detail (telescopic, periscopic, microscopic) as boundary objects for diverse readers. 2024-2025 developments: automated generation via LLMs (CardGen, Liu et al. 2024); model-card detail correlates with up to 29% download increase on HF (Liang et al. 2024); verifiable attestations (Laminator, Duddu et al. 2024); sustainability reporting additions for carbon/water (Jouneaux et al. July 2025); EU/ISO regulatory cards emerging. System Cards (Sidhpurwala 2024; Meta system-level transparency; "Blueprints of Trust" arXiv:2509.20394) — end-to-end AI system documentation covering security capabilities, prompt-injection protection, data-exfiltration detection, alignment with human values.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/26-model-system-dataset-cards/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/26-model-system-dataset-cards) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/26-model-system-dataset-cards) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/87 EU AI Act|87 EU AI Act]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 18 · 18 (safety frameworks), Phase 18 · 24 (regulatory)`

- [[Lessons/18-18 Frontier Safety Frameworks — RSP, PF, FSF|18/18 Frontier Safety Frameworks — RSP, PF, FSF]] — safety frameworks
- [[Lessons/18-24 Regulatory Frameworks — EU, US, UK, Korea|18/24 Regulatory Frameworks — EU, US, UK, Korea]] — regulatory

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/18-07 Sleeper Agents — Persistent Deception|18/07 Sleeper Agents — Persistent Deception]], [[Lessons/18-08 In-Context Scheming in Frontier Models|18/08 In-Context Scheming in Frontier Models]], [[Lessons/18-09 Alignment Faking|18/09 Alignment Faking]], [[Lessons/18-17 WMDP and Dual-Use Capability Evaluation|18/17 WMDP and Dual-Use Capability Evaluation]], [[Lessons/18-27 Data Provenance and Training-Data Governance|18/27 Data Provenance and Training-Data Governance]]
- depth 3: [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/18-06 Mesa-Optimization and Deceptive Alignment|18/06 Mesa-Optimization and Deceptive Alignment]], [[Lessons/18-16 Red-Team Tooling — Garak, Llama Guard, PyRIT|18/16 Red-Team Tooling — Garak, Llama Guard, PyRIT]]

## Builds on this

- [[Lessons/18-27 Data Provenance and Training-Data Governance|18/27 Data Provenance and Training-Data Governance]]
- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- [[Concepts/Model Card|Model Card]] `glossary` — Mitchell et al. 2019 standard documentation for ML models
- Datasheet `lesson term` — Gebru et al. 2018 standard documentation for datasets
- Data Card `lesson term` — Google 2022 modular layered data documentation
- System Card `lesson term` — End-to-end AI system documentation including safety stack
- Boundary object `lesson term` — Data Cards framing: same document serves diverse audiences
- Verifiable attestation `lesson term` — Cryptographic or TEE proof attached to a documentation claim
- Sustainability field `lesson term` — Emerging 2025 addition for environmental accounting
- [[Concepts/Datasheet for Datasets|Datasheet for Datasets]] `glossary` — Structured documentation of a dataset's motivation, composition, collection process, preprocessing, uses, distribution, maintenance, and known limitations.

## Ships

- [[Artifacts/18-26 card-audit|card-audit]] `skill` — Audit a model card, datasheet, or system card for completeness and verifiability.

## Further reading

- Datasheets for Datasets ([link](https://arxiv.org/abs/1803.09010)) — datasheet paper
- Mitchell et al. — Model Cards for Model Reporting (arXiv:1810.03993, FAT* 2019) ([link](https://arxiv.org/abs/1810.03993)) — the canonical model card
- Pushkarna et al. — Data Cards (Google 2022) ([link](https://arxiv.org/abs/2204.01075)) — layered data documentation
- Sidhpurwala et al. — Blueprints of Trust (arXiv:2509.20394) ([link](https://arxiv.org/abs/2509.20394)) — System Card formalization


%% ── my notes ── %%
