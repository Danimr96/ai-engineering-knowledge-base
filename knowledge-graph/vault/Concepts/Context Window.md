---
id: "concept:context-window"
type: concept
name: Context Window
canonical: true
category: "Prompting & context"
taught_in: 4
community: 57
tags:
  - concept/glossary
  - category/prompting-and-context
  - community/57
source: ai-engineering-from-scratch/glossary/terms.md
---

# Context Window

**Community:** [[Communities/57 Context Engineering · Context Window · Token Budget|57 Context Engineering · Context Window · Token Budget]]

> *What people say:* How much the model remembers.

**What it actually means:** The maximum token capacity available to one model inference under a specific model and API contract. The capacity may include system instructions, messages, retrieved content, tool exchanges, and generated output, with provider-specific accounting and output limits.

**Why it matters:** Conversation history is only available when the application sends or reconstructs it. A large window does not guarantee that every included detail will be used reliably.

**Common confusion:** Context is temporary input to an inference. Durable memory is stored outside the model and selected back into later context.

**Category:** [[Categories/Prompting & context|Prompting & context]]

## Related concepts

- [[Concepts/Agent State|Agent State]]
- [[Concepts/Context Engineering|Context Engineering]]
- [[Concepts/Few-Shot|Few-Shot]]
- [[Concepts/In-Context Learning|In-Context Learning]]
- [[Concepts/Lost in the Middle|Lost in the Middle]]
- [[Concepts/Paged KV Cache|Paged KV Cache]]
- [[Concepts/Prompt Cache|Prompt Cache]]
- [[Concepts/Self-Attention|Self-Attention]]
- [[Concepts/Token|Token]]
- [[Concepts/Token Budget|Token Budget]]

## Taught in

- [[Lessons/07-01 Why Transformers — The Problems with RNNs|07/01 Why Transformers — The Problems with RNNs]] — Number of positions an attention layer can take as input; quadratic memory cost scales here.
- [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]] — The maximum number of tokens (input + output) the model can process in a single call -- ranges from 8K to 2M across current models
- [[Lessons/11-05 Context Engineering- Windows, Budgets, Memory, and Retrieval|11/05 Context Engineering: Windows, Budgets, Memory, and Retrieval]] — The maximum number of tokens (input + output) the model processes in a single forward pass -- 400K for GPT-5, 200K (1M beta) for Claude Opus 4.7, 2M for Gemini 3 Pro
- [[Lessons/11-06 RAG (Retrieval-Augmented Generation)|11/06 RAG (Retrieval-Augmented Generation)]] — The maximum number of tokens the LLM can process in a single request; retrieved chunks must fit within this


%% ── my notes ── %%
