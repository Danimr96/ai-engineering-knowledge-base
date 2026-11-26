---
id: "concept:mixed-precision"
type: concept
name: Mixed Precision
canonical: true
category: "Math & training"
taught_in: 3
community: 34
tags:
  - concept/glossary
  - category/math-and-training
  - community/34
source: ai-engineering-from-scratch/glossary/terms.md
---

# Mixed Precision

**Community:** [[Communities/34 Tensor · CUDA · Mixed Precision|34 Tensor · CUDA · Mixed Precision]]

> *What people say:* Using lower-precision arithmetic for speed and memory savings.

**What it actually means:** A numerical strategy that uses different data types for different operations, often lower precision for many matrix operations and higher precision for values that need more range or stability.

**Common confusion:** Speed, memory, and accuracy effects depend on hardware, data type, scaling method, kernels, and model. They are not a fixed multiplier.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Activation Checkpointing|Activation Checkpointing]]
- [[Concepts/CUDA|CUDA]]
- [[Concepts/FlashAttention|FlashAttention]]
- [[Concepts/Gradient Accumulation|Gradient Accumulation]]
- [[Concepts/Gradient Clipping|Gradient Clipping]]
- [[Concepts/NaN (Not a Number)|NaN (Not a Number)]]
- [[Concepts/Normalization|Normalization]]
- [[Concepts/Quantization|Quantization]]
- [[Concepts/Tensor|Tensor]]

## Taught in

- [[Lessons/01-13 Numerical Stability|01/13 Numerical Stability]] — Using lower-precision floats for speed-critical operations and higher-precision floats for numerically sensitive operations. Typical speedup is 2-3x.
- [[Lessons/03-11 Introduction to PyTorch|03/11 Introduction to PyTorch]] — Train with float16 forward/backward for speed while keeping float32 master weights for numerical stability
- [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]] — Use FP16/BF16 for forward/backward and FP32 for optimizer states -- saves ~25% memory, not 50%, because the optimizer dominates


%% ── my notes ── %%
