---
id: "concept:awq"
type: concept
name: AWQ
canonical: false
taught_in: 2
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/11-quantization/docs/en.md
---

# AWQ

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "Activation-aware"

**What it actually means:** Scales salient weights (those multiplied by large activations) before quantization to protect them

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]]
- [[Lessons/17-09 Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4-NVFP4|17/09 Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4/NVFP4]] — Activation-aware INT4; Marlin kernels; best Pass@1 at INT4


%% ── my notes ── %%
