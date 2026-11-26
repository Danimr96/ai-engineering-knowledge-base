---
id: "concept:decoding-strategy"
type: concept
name: Decoding Strategy
canonical: true
category: "Models & inference"
taught_in: 0
community: 5
tags:
  - concept/glossary
  - category/models-and-inference
  - community/05
source: ai-engineering-from-scratch/glossary/terms.md
---

# Decoding Strategy

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

**What it actually means:** The algorithm that converts a model's sequence of next-token scores into selected tokens and a completed output.

**Why it matters:** Greedy selection, sampling, truncation, and search can produce different quality, diversity, latency, and repeatability from the same logits.

**In practice:** Define the task's decoding settings, stop rules, and seed behavior in the eval configuration so results can be compared fairly.

**Common confusion:** Decoding changes how outputs are selected; it does not change the model's trained parameters or add knowledge.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Autoregressive|Autoregressive]]
- [[Concepts/Nucleus Sampling (Top-p)|Nucleus Sampling (Top-p)]]
- [[Concepts/Speculative Decoding|Speculative Decoding]]
- [[Concepts/Stop Sequence|Stop Sequence]]
- [[Concepts/Temperature|Temperature]]
- [[Concepts/Top-k Sampling|Top-k Sampling]]

## Sources

- The Curious Case of Neural Text Degeneration ([link](https://arxiv.org/abs/1904.09751))


%% ── my notes ── %%
