---
id: "concept:acceptance-rate"
type: concept
name: Acceptance rate
canonical: false
aliases:
  - "α"
taught_in: 5
community: 20
tags:
  - concept/lesson-term
  - community/20
source: ai-engineering-from-scratch/phases/07-transformers-deep-dive/16-speculative-decoding/docs/en.md
---

# Acceptance rate

**Community:** [[Communities/20 Acceptance rate · Draft model · EAGLE-3|20 Acceptance rate · Draft model · EAGLE-3]]

> *What people say:* "How often the draft is right"

**What it actually means:** Per-token probability that the verifier accepts the draft. 0.7–0.9 typical.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/07-16 Speculative Decoding — Draft, Verify, Repeat|07/16 Speculative Decoding — Draft, Verify, Repeat]]
- [[Lessons/10-15 Speculative Decoding and EAGLE-3|10/15 Speculative Decoding and EAGLE-3]] — Expected per-token Bernoulli-success probability under the rejection rule; governs all speedup math
- [[Lessons/10-25 Speculative Decoding and EAGLE|10/25 Speculative Decoding and EAGLE]] — Per-token probability that the draft's proposal is accepted
- [[Lessons/19-07 Capstone 07 — End-to-End Fine-Tuning Pipeline (Data to SFT to DPO to Serve)|19/07 Capstone 07 — End-to-End Fine-Tuning Pipeline (Data to SFT to DPO to Serve)]] — Fraction of drafted tokens the target model accepts
- [[Lessons/19-14 Capstone 14 — Speculative-Decoding Inference Server|19/14 Capstone 14 — Speculative-Decoding Inference Server]] — Fraction of drafted tokens accepted without resampling


%% ── my notes ── %%
