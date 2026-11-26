---
id: "concept:chain-of-thought-cot"
type: concept
name: Chain of Thought (CoT)
canonical: true
category: "Prompting & context"
taught_in: 2
community: 42
tags:
  - concept/glossary
  - category/prompting-and-context
  - community/42
source: ai-engineering-from-scratch/glossary/terms.md
---

# Chain of Thought (CoT)

**Community:** [[Communities/42 Few-Shot · Prompt Engineering · In-Context Learning|42 Few-Shot · Prompt Engineering · In-Context Learning]]

> *What people say:* Asking the model to show every step of its thinking.

**What it actually means:** Intermediate reasoning used to decompose a task before producing an answer. A prompt can request a visible rationale, while some systems use internal reasoning that is not returned to the user.

**Why it matters:** Decomposition can help on multi-step tasks, but a fluent rationale is not proof that the answer is correct or that the text faithfully represents the model's internal computation.

**In practice:** Ask for a concise plan, independently check the result, and request verifiable calculations or citations instead of relying on a long reasoning transcript.

**Common confusion:** Chain of thought is not a substitute for tools, tests, or external verification.

**Category:** [[Categories/Prompting & context|Prompting & context]]

## Related concepts

- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]]
- [[Concepts/Prompt Engineering|Prompt Engineering]]
- [[Concepts/Verification Gate|Verification Gate]]

## Taught in

- [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]] `alias` — Prompting the model to show intermediate reasoning steps, which improves accuracy on math, logic, and multi-step problems by 10-40%
- [[Lessons/11-02 Few-Shot, Chain-of-Thought, Tree-of-Thought|11/02 Few-Shot, Chain-of-Thought, Tree-of-Thought]] — Eliciting intermediate reasoning tokens that extend the model's effective computation before producing a final answer


%% ── my notes ── %%
