---
id: "concept:nucleus-sampling-top-p"
type: concept
name: Nucleus Sampling (Top-p)
canonical: true
category: "Models & inference"
aliases:
  - Top-p sampling
taught_in: 3
community: 5
tags:
  - concept/glossary
  - category/models-and-inference
  - community/05
source: ai-engineering-from-scratch/glossary/terms.md
---

# Nucleus Sampling (Top-p)

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

**What it actually means:** A decoding method that samples from the smallest set of next-token candidates whose cumulative probability reaches a chosen threshold.

**Why it matters:** The candidate-set size adapts to the distribution, retaining more options when uncertainty is broad and fewer when probability is concentrated.

**In practice:** Evaluate the threshold with temperature and stop settings held constant, and record the complete decoding configuration with every result.

**Common confusion:** Top-p is a probability-mass threshold, while top-k always keeps a fixed maximum number of candidates.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Decoding Strategy|Decoding Strategy]]
- [[Concepts/Softmax|Softmax]]
- [[Concepts/Temperature|Temperature]]
- [[Concepts/Top-k Sampling|Top-k Sampling]]

## Taught in

- [[Lessons/01-16 Sampling Methods|01/16 Sampling Methods]] — Keep the smallest set of tokens whose cumulative probability exceeds p. Adaptive candidate set size
- [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]] `alias` — Truncate distribution to smallest set summing to ≥p; sample from what remains.
- [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]] `alias` — Limit token sampling to the smallest set whose cumulative probability exceeds p, cutting off the long tail of unlikely tokens

## Sources

- The Curious Case of Neural Text Degeneration ([link](https://arxiv.org/abs/1904.09751))


%% ── my notes ── %%
