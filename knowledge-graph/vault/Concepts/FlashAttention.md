---
id: "concept:flashattention"
type: concept
name: FlashAttention
canonical: true
category: "Infrastructure & serving"
taught_in: 1
community: 12
tags:
  - concept/glossary
  - category/infrastructure-and-serving
  - community/12
source: ai-engineering-from-scratch/glossary/terms.md
---

# FlashAttention

**Community:** [[Communities/12 Attention · Cross-Attention · Self-Attention|12 Attention · Cross-Attention · Self-Attention]]

**What it actually means:** An exact attention algorithm that tiles the computation to reduce transfers between accelerator memory levels while avoiding materialization of the full attention matrix in high-bandwidth memory.

**Why it matters:** Attention can be limited by memory movement rather than arithmetic, especially for long sequences, so an IO-aware kernel can improve usable speed and memory efficiency.

**In practice:** Use a kernel supported by the model's shapes, masks, dtype, and hardware, verify numerical tolerance, and benchmark end-to-end latency rather than quoting a paper result as a fixed multiplier.

**Common confusion:** FlashAttention changes how attention is computed, not the mathematical attention result it targets. It is separate from KV caching and quantization.

**Category:** [[Categories/Infrastructure & serving|Infrastructure & serving]]

## Related concepts

- [[Concepts/Attention|Attention]]
- [[Concepts/KV Cache|KV Cache]]
- [[Concepts/Mixed Precision|Mixed Precision]]
- [[Concepts/Self-Attention|Self-Attention]]

## Taught in

- [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]]

## Sources

- FlashAttention ([link](https://arxiv.org/abs/2205.14135))


%% ── my notes ── %%
