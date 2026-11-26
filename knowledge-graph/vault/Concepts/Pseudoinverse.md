---
id: "concept:pseudoinverse"
type: concept
name: Pseudoinverse
canonical: false
taught_in: 2
community: 8
tags:
  - concept/lesson-term
  - community/08
source: ai-engineering-from-scratch/phases/01-math-foundations/11-singular-value-decomposition/docs/en.md
---

# Pseudoinverse

**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]]

> *What people say:* "Generalized inverse"

**What it actually means:** V Sigma+ U^T. Inverts non-zero singular values, leaves zeros as zeros. Solves least-squares problems for non-square or singular matrices.

*Not in the glossary: this concept exists because lessons list it in their Key Terms table. If it is really a glossary term under another name, add it to `data/aliases.json`.*

## Taught in

- [[Lessons/01-11 Singular Value Decomposition|01/11 Singular Value Decomposition]]
- [[Lessons/01-17 Linear Systems|01/17 Linear Systems]] — A+ = V Sigma+ U^T via SVD. Gives the minimum-norm least-squares solution for any matrix, square or rectangular, singular or not.


%% ── my notes ── %%
