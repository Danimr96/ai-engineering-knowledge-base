---
id: "lesson:01/13"
type: lesson
ref: 01/13
phase: 1
num: 13
title: Numerical Stability
lesson_type: build
time_min: 120
on_route: false
quiz_count: 5
code_files: 1
concepts: 15
prereqs: 4
community: 8
aliases:
  - 01/13
  - 01-13
tags:
  - phase/01
  - type/build
  - community/08
  - stdlib-only
source: ai-engineering-from-scratch/phases/01-math-foundations/13-numerical-stability/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/13-numerical-stability"
---

# 01/13 Numerical Stability

> Floating point is a leaky abstraction. It will bite you during training, and you will not see it coming.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Build · **Time:** 120 min · **Status:** —  
**Open:** [[Upstream/01-math-foundations/13-numerical-stability/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/13-numerical-stability) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/13-numerical-stability) · code: numerical.py · quiz: 5 questions  
**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1, Lessons 01-04`

- **01/01-04**:
    - [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]]
    - [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]]
    - [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]]
    - [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Concepts taught

- IEEE 754 `lesson term` — International standard defining binary floating point formats, rounding rules, and special values (inf, nan). Every modern CPU and GPU implements it.
- Machine epsilon `lesson term` — The smallest value e such that 1.0 + e != 1.0 in a given float format. For float32, it is about 1.19e-7.
- Catastrophic cancellation `lesson term` — When subtracting nearly equal floating point numbers, significant digits cancel and rounding noise dominates the result.
- Overflow `lesson term` — A result exceeds the maximum representable value and becomes inf. exp(89) overflows float32.
- Underflow `lesson term` — A result is closer to zero than the smallest representable positive number and becomes 0.0. exp(-104) underflows float32.
- Log-sum-exp trick `lesson term` — Computing log(sum(exp(x))) by factoring out exp(max(x)) to prevent overflow and underflow. Used in softmax, cross-entropy, and log-probability math.
- Stable softmax `lesson term` — Subtracting max(logits) before exponentiating. Numerically identical result, no overflow possible.
- [[Concepts/Gradient checking|Gradient checking]] `lesson term` — Comparing analytical gradients from backpropagation against numerical gradients from finite differences to catch implementation bugs.
- [[Concepts/Mixed Precision|Mixed Precision]] `glossary` — Using lower-precision floats for speed-critical operations and higher-precision floats for numerically sensitive operations. Typical speedup is 2-3x.
- [[Concepts/Loss scaling|Loss scaling]] `lesson term` — Multiplying the loss by a large constant before backprop so gradients stay in float16's representable range, then dividing by the same constant before weight updates.
- bfloat16 `lesson term` — Google's 16-bit format with 8 exponent bits (same range as float32) and 7 mantissa bits (less precision than float16). Preferred for training.
- [[Concepts/Gradient Clipping|Gradient Clipping]] `glossary` — Scaling the gradient vector so its norm does not exceed a threshold. Prevents exploding gradients from ruining weights.
- [[Concepts/NaN (Not a Number)|NaN (Not a Number)]] (as *NaN*) `glossary` — Special float value from undefined operations (0/0, inf-inf, sqrt(-1)). Propagates through all subsequent arithmetic.
- Inf `lesson term` — Special float value from overflow or division by zero. Can combine to produce NaN (inf - inf, inf 0).
- Numerical gradient `lesson term` — Approximating a derivative by evaluating f(x+h) and f(x-h) and dividing by 2h. Slow but reliable for verification.

## Ships

- [[Artifacts/01-13 prompt-numerical-debugger|prompt-numerical-debugger]] `prompt` — Diagnoses NaN, Inf, and numerical stability issues in neural network training

## Further reading

- [[Resources/Mixed Precision Training (Micikevicius et al., 2018)|Mixed Precision Training (Micikevicius et al., 2018)]] ([link](https://arxiv.org/abs/1710.03740)) — the NVIDIA paper that introduced loss scaling for float16 training ·  also cited by 1 other lesson
- bfloat16 format (Google Cloud TPU docs) ([link](https://cloud.google.com/tpu/docs/bfloat16)) — why Google chose this format for TPUs
- What Every Computer Scientist Should Know About Floating-Point Arithmetic (Goldberg 1991) ([link](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)) — the definitive reference, dense but complete
- Kahan Summation (Wikipedia) ([link](https://en.wikipedia.org/wiki/Kahan_summation_algorithm)) — algorithm for reducing rounding error in floating point sums
- AMP: Automatic Mixed Precision (PyTorch docs) ([link](https://pytorch.org/docs/stable/amp.html)) — practical guide to mixed precision in PyTorch


%% ── my notes ── %%
