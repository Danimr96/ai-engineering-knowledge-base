---
id: "concept:parameter"
type: concept
name: Parameter
canonical: true
category: "Models & inference"
taught_in: 2
community: 35
tags:
  - concept/glossary
  - category/models-and-inference
  - community/35
source: ai-engineering-from-scratch/glossary/terms.md
---

# Parameter

**Community:** [[Communities/35 Checkpoint · Durable Execution · Idempotency|35 Checkpoint · Durable Execution · Idempotency]]

> *What people say:* A number used to describe model size.

**What it actually means:** A value learned during training, commonly a weight, bias, embedding element, or normalization parameter. Parameter count is one measure of model capacity, but it does not directly determine quality, memory, or serving cost.

**Common confusion:** Memory per parameter depends on numerical format, quantization metadata, sharding, optimizer state, activations, and runtime overhead.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Checkpoint|Checkpoint]]
- [[Concepts/Hyperparameter|Hyperparameter]]
- [[Concepts/LoRA (Low-Rank Adaptation)|LoRA (Low-Rank Adaptation)]]
- [[Concepts/MoE (Mixture of Experts)|MoE (Mixture of Experts)]]
- [[Concepts/Quantization|Quantization]]
- [[Concepts/Tensor|Tensor]]
- [[Concepts/Tensor Parallelism|Tensor Parallelism]]
- [[Concepts/Weight|Weight]]

## Taught in

- [[Lessons/03-10 Build Your Own Mini Framework|03/10 Build Your Own Mini Framework]] `normalized` — All values in the network that the optimizer can update -- weights and biases
- [[Lessons/07-13 Scaling Laws|07/13 Scaling Laws]] `normalized` — Non-embedding weight count; determines capacity.


%% ── my notes ── %%
