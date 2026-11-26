---
id: "concept:fp8"
type: concept
name: FP8
canonical: false
taught_in: 3
community: 1
tags:
  - concept/lesson-term
  - community/01
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/11-quantization/docs/en.md
---

# FP8

**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]]

> *What people say:* "Eight-bit float"

**What it actually means:** Two variants: E4M3 (inference, more precision) and E5M2 (training, more range), native on H100

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/10-11 Quantization- Making Models Fit|10/11 Quantization: Making Models Fit]]
- [[Lessons/17-07 Hardware-Specialized Inference Compilation — FP8 and NVFP4 on Blackwell|17/07 Hardware-Specialized Inference Compilation — FP8 and NVFP4 on Blackwell]] — 8-bit floating point; used for KV cache and attention due to dynamic range
- [[Lessons/17-09 Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4-NVFP4|17/09 Production Quantization — AWQ, GPTQ, GGUF K-quants, FP8, MXFP4/NVFP4]] — Safe precision default on Hopper/Ada/Blackwell


%% ── my notes ── %%
