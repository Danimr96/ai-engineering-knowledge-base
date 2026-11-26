---
id: "myth:7"
type: myth
claim: Temperature makes the AI more creative
tags:
  - myth
source: ai-engineering-from-scratch/glossary/myths.md
---

# Myth: “Temperature makes the AI more creative”

**Reality:** Temperature scales the logits before softmax. Higher temperature = flatter probability distribution = more random token selection. Lower temperature = sharper distribution = more deterministic. It's not creativity, it's randomness. A high-temperature model doesn't think harder, it just considers less likely tokens.

**Why it matters:** When your output is too repetitive, raise temperature. When it's too chaotic, lower it. It's a randomness knob, nothing more.


%% ── my notes ── %%
