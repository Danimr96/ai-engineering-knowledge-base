---
id: "lesson:01/19"
type: lesson
ref: 01/19
phase: 1
num: 19
title: Complex Numbers for AI
lesson_type: learn
time_min: 60
on_route: false
quiz_count: 5
code_files: 1
concepts: 12
prereqs: 4
community: 8
aliases:
  - 01/19
  - 01-19
tags:
  - phase/01
  - type/learn
  - community/08
  - stdlib-only
source: ai-engineering-from-scratch/phases/01-math-foundations/19-complex-numbers/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/19-complex-numbers"
---

# 01/19 Complex Numbers for AI

> The square root of -1 is not imaginary. It is the key to rotations, frequencies, and half of signal processing.

**Phase:** [[Phases/01 Math Foundations|Phase 1: Math Foundations]] · **Type:** Learn · **Time:** 60 min · **Status:** —  
**Open:** [[Upstream/01-math-foundations/19-complex-numbers/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/01-math-foundations/19-complex-numbers) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/01-math-foundations/19-complex-numbers) · code: complex_numbers.py · quiz: 5 questions  
**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 1, Lessons 01-04 (linear algebra, calculus)`

- **01/01-04** — linear algebra, calculus:
    - [[Lessons/01-01 Linear Algebra Intuition|01/01 Linear Algebra Intuition]]
    - [[Lessons/01-02 Vectors, Matrices & Operations|01/02 Vectors, Matrices & Operations]]
    - [[Lessons/01-03 Matrix Transformations|01/03 Matrix Transformations]]
    - [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]]

## Builds on this

- [[Lessons/01-20 The Fourier Transform|01/20 The Fourier Transform]]

## Concepts taught

- Complex number `lesson term` — A number a + bi where a is the real part, b is the imaginary part, and i^2 = -1
- Imaginary unit `lesson term` — The number i, defined by i^2 = -1. Not imaginary in the philosophical sense -- it is a rotation operator
- Complex plane `lesson term` — The 2D plane where the x-axis is real and the y-axis is imaginary. Also called the Argand plane
- Magnitude (as *Magnitude (modulus)*) `lesson term` — The distance from the origin: sqrt(a^2 + b^2). Written as |z|
- Phase (as *Phase (argument)*) `lesson term` — The angle from the positive real axis: atan2(b, a). Written as arg(z)
- Conjugate `lesson term` — The mirror image across the real axis: conjugate of a + bi is a - bi
- Polar form `lesson term` — Expressing z as r e^(itheta) instead of a + bi. Makes multiplication easy
- Euler's formula `lesson term` — e^(itheta) = cos(theta) + isin(theta). Connects exponentials to trigonometry
- Phasor `lesson term` — A rotating complex number e^(iomegat) representing a sinusoidal signal
- Roots of unity `lesson term` — The N complex numbers e^(2piik/N) for k = 0 to N-1. N equally spaced points on the unit circle
- [[Concepts/DFT|DFT]] `lesson term` — Discrete Fourier Transform. Decomposes a signal into complex sinusoidal components using roots of unity
- [[Concepts/RoPE|RoPE]] `lesson term` — Rotary Position Embedding. Uses complex multiplication to encode relative position in transformer attention

## Ships

- [[Artifacts/01-19 skill-complex-arithmetic|skill-complex-arithmetic]] `skill` — Quick reference for complex number operations in ML and signal processing contexts

## Further reading

- [[Resources/Attention Is All You Need|Attention Is All You Need]] ([link](https://arxiv.org/abs/1706.03762)) — the original Transformer paper with sinusoidal positional encodings ·  also cited by 8 other lessons
- [[Resources/Su et al.- RoFormer (2021)|Su et al.: RoFormer (2021)]] ([link](https://arxiv.org/abs/2104.09864)) — the paper introducing Rotary Position Embedding using complex rotations ·  also cited by 3 other lessons
- Visual Introduction to Euler's Formula ([link](https://betterexplained.com/articles/intuitive-understanding-of-eulers-formula/)) — builds geometric intuition without heavy notation
- Needham: Visual Complex Analysis ([link](https://global.oup.com/academic/product/visual-complex-analysis-9780198534464)) — the best visual treatment of complex numbers, full of geometric insight
- [[Resources/Gilbert Strang- Linear Algebra and Its Applications, Chapter 7|Gilbert Strang: Linear Algebra and Its Applications, Chapter 7]] ([link](https://math.mit.edu/~gs/linearalgebra/)) — complex numbers in the context of linear algebra and eigenvalues ·  also cited by 1 other lesson
- 3Blue1Brown: Euler's formula with introductory group theory ([link](https://www.youtube.com/watch?v=mvmuCPvRoWQ)) — visual explanation of why e^(i*pi) = -1


%% ── my notes ── %%
