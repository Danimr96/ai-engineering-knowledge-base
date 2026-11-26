---
id: "lesson:18/22"
type: lesson
ref: 18/22
phase: 18
num: 22
title: Differential Privacy for LLMs
lesson_type: build
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 6
code_files: 1
concepts: 8
prereqs: 2
community: 46
aliases:
  - 18/22
  - 18-22
tags:
  - phase/18
  - type/build
  - community/46
  - stdlib-only
source: ai-engineering-from-scratch/phases/18-ethics-safety-alignment/22-differential-privacy-for-llms/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/22-differential-privacy-for-llms"
---

# 18/22 Differential Privacy for LLMs

> DP-SGD remains the standard — noise-injected gradient updates provide formal (epsilon, delta) guarantees. Overhead in compute, memory, and utility is substantial; parameter-efficient DP fine-tuning (LoRA + DP-SGD) is the common 2025 configuration (ACM 2025). Two bodies of evidence in tension: canary-based membership inference (Duan et al., 2024) reports limited success against language models; training-data extraction (Carlini et al., 2021; Nasr et al., 2025) recovers substantial verbatim memorization. Resolution (arXiv:2503.06808, March 2025): the gap is in what is measured — inserted canaries vs "most extractable" data. New canary designs enable loss-based MIA without shadow models and yield the first nontrivial DP audit of an LLM trained on real data with realistic DP guarantees. Alternatives: PMixED (arXiv:2403.15638) — private prediction at inference time via mixture of experts on next-token distributions; DP synthetic data generation (Google Research 2024). Emerging attack: Differential Privacy Reversal via LLM Feedback — confidence-score leakage.

**Phase:** [[Phases/18 Ethics, Safety & Alignment|Phase 18: Ethics, Safety & Alignment]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/18-ethics-safety-alignment/22-differential-privacy-for-llms/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/18-ethics-safety-alignment/22-differential-privacy-for-llms) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/18-ethics-safety-alignment/22-differential-privacy-for-llms) · code: main.py · quiz: 6 questions  
**Community:** [[Communities/46 Audit Log · Observability · Incident Response|46 Audit Log · Observability · Incident Response]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 01 · 09 (information theory), Phase 10 · 01 (large-model training)`

- [[Lessons/01-09 Information Theory|01/09 Information Theory]] — information theory
- [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]] — large-model training

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]]
- depth 3: [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]], [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]], [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]], [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Builds on this

- [[Lessons/18-28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR|18/28 Alignment Research Ecosystem — MATS, Redwood, Apollo, METR]]

## Concepts taught

- DP `lesson term` — Formal privacy: output distribution close under neighbouring-dataset change
- DP-SGD `lesson term` — Gradient clipping + Gaussian noise addition; standard DP training
- LoRA + DP-SGD `lesson term` — DP-SGD on low-rank adapters; standard 2025 configuration
- MIA `lesson term` — Attack that determines whether an example was in training data
- [[Concepts/Canary Release|Canary Release]] (as *Canary*) `glossary` — Unique training example used to measure DP leakage
- PMixED `lesson term` — Inference-time DP via mixture-of-experts on next-token distributions
- DP Reversal `lesson term` — Attack that uses a model's confidence as an oracle for re-identification
- [[Concepts/Membership Inference|Membership Inference]] `glossary` — An attack that estimates whether a particular record or example was included in a model's training data by observing model outputs or other accessible signals.

## Ships

- [[Artifacts/18-22 dp-audit|dp-audit]] `skill` — Audit a differential-privacy claim for a language-model deployment.

## Further reading

- Abadi et al. — DP-SGD (arXiv:1607.00133) ([link](https://arxiv.org/abs/1607.00133)) — the standard DP training algorithm
- Carlini et al. — Extracting Training Data (arXiv:2012.07805) ([link](https://arxiv.org/abs/2012.07805)) — the canonical extraction paper
- Duan et al. — Canary MIA on LLMs (arXiv:2402.07841, 2024) ([link](https://arxiv.org/abs/2402.07841)) — limited-success MIA
- PMixED (arXiv:2403.15638) ([link](https://arxiv.org/abs/2403.15638)) — inference-time private prediction
- Kowalczyk et al. — Auditing DP for LLMs (arXiv:2503.06808, March 2025) ([link](https://arxiv.org/abs/2503.06808)) — resolution of the tension


%% ── my notes ── %%
