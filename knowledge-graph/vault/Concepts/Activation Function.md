---
id: "concept:activation-function"
type: concept
name: Activation Function
canonical: true
category: "Math & training"
taught_in: 3
community: 8
tags:
  - concept/glossary
  - category/math-and-training
  - community/08
source: ai-engineering-from-scratch/glossary/terms.md
---

# Activation Function

**Community:** [[Communities/08 Backpropagation · Gradient · Activation Function|08 Backpropagation · Gradient · Activation Function]]

> *What people say:* The nonlinear operation between layers.

**What it actually means:** A function applied after a linear or affine layer that introduces nonlinearity. Without it, composing layers with weights and biases collapses to one affine transformation. ReLU, GELU, and SiLU are common choices. The choice directly affects whether gradients flow during training.

**Category:** [[Categories/Math & training|Math & training]]

## Related concepts

- [[Concepts/Backpropagation|Backpropagation]]
- [[Concepts/CNN (Convolutional Neural Network)|CNN (Convolutional Neural Network)]]
- [[Concepts/Dropout|Dropout]]
- [[Concepts/Gradient|Gradient]]
- [[Concepts/Normalization|Normalization]]
- [[Concepts/ReLU|ReLU]]

## Taught in

- [[Lessons/03-01 The Perceptron|03/01 The Perceptron]] — A function applied after the weighted sum - step function for perceptrons, sigmoid/ReLU for modern networks
- [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]] — A function applied after the linear transformation that introduces curves into the decision boundary
- [[Lessons/03-04 Activation Functions|03/04 Activation Functions]] — A function applied to each neuron's output that breaks linearity, enabling the network to learn nonlinear mappings


%% ── my notes ── %%
