---
id: "concept:hallucination"
type: concept
name: Hallucination
canonical: true
category: "Evaluation & safety"
taught_in: 4
community: 55
tags:
  - concept/glossary
  - category/evaluation-and-safety
  - community/55
source: ai-engineering-from-scratch/glossary/terms.md
---

# Hallucination

**Community:** [[Communities/55 Grounding · RAG (Retrieval-Augmented Generation) · Chunking|55 Grounding · RAG (Retrieval-Augmented Generation) · Chunking]]

> *What people say:* The model is lying.

**What it actually means:** Generated content that is false, unsupported by the available evidence, or inconsistent with the task's source of truth. It can arise even when the output is fluent and the model is not attempting to deceive.

**Why it matters:** You usually cannot inspect whether a statement existed in training data, so production checks should focus on support, correctness, and traceability.

**In practice:** Require cited evidence for factual answers and evaluate whether each citation actually supports the associated claim.

**Common confusion:** A hallucination is an output-quality failure, not a diagnosis of model intent.

**Category:** [[Categories/Evaluation & safety|Evaluation & safety]]

## Related concepts

- [[Concepts/Grounding|Grounding]]
- [[Concepts/RAG (Retrieval-Augmented Generation)|RAG (Retrieval-Augmented Generation)]]
- [[Concepts/Verification Gate|Verification Gate]]

## Taught in

- [[Lessons/05-11 Machine Translation|05/11 Machine Translation]] — Model output that is not supported by the source.
- [[Lessons/05-12 Text Summarization|05/12 Text Summarization]] — Content in the summary that the source does not support.
- [[Lessons/05-13 Question Answering Systems|05/13 Question Answering Systems]] — Reader output not supported by retrieved context.
- [[Lessons/06-05 Whisper — Architecture & Fine-Tuning|06/05 Whisper — Architecture & Fine-Tuning]] — Whisper produces fluent English from noise/silence.


%% ── my notes ── %%
