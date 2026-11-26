---
id: "concept:backpropagation"
type: concept
name: Backpropagation
canonical: true
category: "Math & training"
taught_in: 2
community: 8
tags:
  - concept/glossary
  - category/math-and-training
  - community/08
source: ai-engineering-from-scratch/glossary/terms.md
---

# Backpropagation

**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]]

> *What people say:* How neural networks learn.

**What it actually means:** An efficient application of the chain rule that propagates derivatives from a scalar loss backward through a computation graph. It computes gradients; an optimizer uses those gradients to update parameters.

**Common confusion:** Backpropagation calculates gradients. It does not choose the update rule or learning rate.

**Why it's called that:** Derivative information moves backward from the loss toward earlier operations.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Activation Checkpointing|Activation Checkpointing]]
- [[Concepts/Activation Function|Activation Function]]
- [[Concepts/Autograd|Autograd]]
- [[Concepts/Gradient|Gradient]]
- [[Concepts/Gradient Accumulation|Gradient Accumulation]]
- [[Concepts/Optimizer|Optimizer]]

## Taught in

- [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]] — Computing gradients layer by layer from output to input using the chain rule. How neural networks learn.
- [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]] — An algorithm that computes dL/dw for every weight by applying the chain rule backward through the computational graph


%% ── my notes ── %%
