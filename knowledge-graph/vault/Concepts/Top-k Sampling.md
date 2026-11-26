---
id: "concept:top-k-sampling"
type: concept
name: Top-k Sampling
canonical: true
category: "Models & inference"
taught_in: 2
community: 5
tags:
  - concept/glossary
  - category/models-and-inference
  - community/05
source: ai-engineering-from-scratch/glossary/terms.md
---

# Top-k Sampling

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

**What it actually means:** A decoding method that restricts the next-token distribution to the k highest-scoring candidates, renormalizes their probabilities, and samples from that set.

**Why it matters:** It removes the long low-probability tail from sampling while keeping a fixed maximum candidate count.

**In practice:** Evaluate k together with temperature, top-p, and stop settings, and record the complete sampler configuration with generated results.

**Common confusion:** Top-k uses a fixed candidate count, while top-p uses a probability-mass threshold whose candidate count changes by step.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Decoding Strategy|Decoding Strategy]]
- [[Concepts/Logits|Logits]]
- [[Concepts/Nucleus Sampling (Top-p)|Nucleus Sampling (Top-p)]]
- [[Concepts/Temperature|Temperature]]

## Taught in

- [[Lessons/01-16 Sampling Methods|01/16 Sampling Methods]] — Zero out all but the k highest-probability tokens, renormalize, sample. Fixed candidate set size
- [[Lessons/19-35 GPT Model Assembly|19/35 GPT Model Assembly]] — Keep the K logits with the highest values, mask the rest to negative infinity, softmax over the remainder

## Sources

- The Curious Case of Neural Text Degeneration ([link](https://arxiv.org/abs/1904.09751))


%% ── my notes ── %%
