---
id: "concept:autoregressive"
type: concept
name: Autoregressive
canonical: true
category: "Models & inference"
taught_in: 3
community: 5
tags:
  - concept/glossary
  - category/models-and-inference
  - community/05
source: ai-engineering-from-scratch/glossary/terms.md
---

# Autoregressive

**Community:** [[Communities/05 Temperature · Autoregressive · Logits|05 Temperature · Autoregressive · Logits]]

> *What people say:* The model generates one word at a time.

**What it actually means:** A factorization in which each output token is predicted from the tokens that precede it. During generation, the selected token is appended to the sequence and becomes part of the next prediction's context.

**Common confusion:** The unit is a token, not necessarily a word, and generation can use decoding methods other than always selecting the highest-probability token.

**Category:** [[Categories/Models & inference|Models & inference]]

## Related concepts

- [[Concepts/Decode Phase|Decode Phase]]
- [[Concepts/Decoder|Decoder]]
- [[Concepts/Decoding Strategy|Decoding Strategy]]
- [[Concepts/GPT|GPT]]
- [[Concepts/Inference|Inference]]
- [[Concepts/KV Cache|KV Cache]]
- [[Concepts/LLM (Large Language Model)|LLM (Large Language Model)]]
- [[Concepts/Speculative Decoding|Speculative Decoding]]
- [[Concepts/Streaming|Streaming]]
- [[Concepts/Temperature|Temperature]]
- [[Concepts/Token|Token]]

## Taught in

- [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]] — Feed output back as input; parallelism only during training, not during generation.
- [[Lessons/08-01 Generative Models — Taxonomy & History|08/01 Generative Models — Taxonomy & History]] — Factorize joint as product of conditionals.
- [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]] — Each output token is conditioned on all previous tokens -- the model predicts P(token_n | token_0, ..., token{n-1})


%% ── my notes ── %%
