---
id: "myth:11"
type: myth
claim: Transformers understand order because of positional encoding
tags:
  - myth
source: ai-engineering-from-scratch/glossary/myths.md
---

# Myth: “Transformers understand order because of positional encoding”

**Reality:** Transformers have no inherent sense of order. Self-attention treats input as a set, not a sequence. Positional encoding is a hack to inject order information by adding position-dependent vectors to the input. Different methods (sinusoidal, learned, RoPE, ALiBi) handle this differently. None of them truly give the model sequential understanding the way RNNs had it.

**Why it matters:** This is why positional encoding research is still active. It's a solved-enough problem for most uses, but it's fundamentally a workaround.


%% ── my notes ── %%
