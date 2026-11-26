---
id: "myth:9"
type: myth
claim: "Bigger context window = better"
tags:
  - myth
source: ai-engineering-from-scratch/glossary/myths.md
---

# Myth: “Bigger context window = better”

**Reality:** Models degrade on long contexts. The "lost in the middle" problem means models pay more attention to the beginning and end of long prompts and less to the middle. A 200K context window doesn't mean the model uses all 200K tokens equally well. Also, longer contexts cost more and are slower.

**Why it matters:** Don't dump everything into the context. Be selective. RAG with targeted retrieval beats stuffing the full document in.


%% ── my notes ── %%
