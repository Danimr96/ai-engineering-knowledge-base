---
id: "myth:8"
type: myth
claim: Fine-tuning teaches the model new knowledge
tags:
  - myth
source: ai-engineering-from-scratch/glossary/myths.md
---

# Myth: “Fine-tuning teaches the model new knowledge”

**Reality:** Fine-tuning adjusts how the model uses existing knowledge, not what it knows. If information wasn't in the pre-training data, fine-tuning won't reliably add it. Fine-tuning is better for changing behavior (style, format, tone, task-specific patterns) than for adding facts. For new knowledge, use RAG.

**Why it matters:** If you need the model to know about your company's internal docs, use RAG. If you need it to respond in a specific format, fine-tune.


%% ── my notes ── %%
