---
id: "concept:eagle-3"
type: concept
name: EAGLE-3
canonical: false
taught_in: 4
community: 20
tags:
  - concept/lesson-term
  - community/20
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/15-speculative-decoding-eagle3/docs/en.md
---

# EAGLE-3

**Community:** [[Communities/20 Acceptance rate · Draft model · EAGLE-3|20 Acceptance rate · Draft model · EAGLE-3]]

> *What people say:* "training-time test"

**What it actually means:** Drops the feature-prediction loss, trains on direct token prediction with the draft fed its own outputs during training

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/10-15 Speculative Decoding and EAGLE-3|10/15 Speculative Decoding and EAGLE-3]]
- [[Lessons/17-05 EAGLE-3 Speculative Decoding in Production|17/05 EAGLE-3 Speculative Decoding in Production]] — 2025-2026 variant; trains draft head on multiple target layers; alpha 0.6-0.8 on general chat
- [[Lessons/19-07 Capstone 07 — End-to-End Fine-Tuning Pipeline (Data to SFT to DPO to Serve)|19/07 Capstone 07 — End-to-End Fine-Tuning Pipeline (Data to SFT to DPO to Serve)]] — Draft heads that predict N tokens ahead; vLLM verifies with target model
- [[Lessons/19-14 Capstone 14 — Speculative-Decoding Inference Server|19/14 Capstone 14 — Speculative-Decoding Inference Server]] — Draft head trained on target hidden states; ~75% acceptance


%% ── my notes ── %%
