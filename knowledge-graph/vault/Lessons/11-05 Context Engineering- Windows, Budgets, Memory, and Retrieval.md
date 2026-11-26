---
id: "lesson:11/05"
type: lesson
ref: 11/05
phase: 11
num: 5
title: "Context Engineering: Windows, Budgets, Memory, and Retrieval"
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 0
code_files: 2
concepts: 13
prereqs: 2
community: 57
libraries:
  - numpy
aliases:
  - 11/05
  - 11-05
tags:
  - phase/11
  - type/build
  - community/57
source: ai-engineering-from-scratch/phases/11-llm-engineering/05-context-engineering/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/05-context-engineering"
---

# 11/05 Context Engineering: Windows, Budgets, Memory, and Retrieval

> Prompt engineering is a subset. Context engineering is the whole game. A prompt is a string you type. Context is everything that goes into the model's window: system instructions, retrieved documents, tool definitions, conversation history, few-shot examples, and the prompt itself. The best AI engineers in 2026 are context engineers. They decide what goes in, what stays out, and in what order.

**Phase:** [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/11-llm-engineering/05-context-engineering/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/05-context-engineering) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/11-llm-engineering/05-context-engineering) · code: main.py, main.ts  
**Community:** [[Communities/57 Context Engineering · Context Window · Token Budget|57 Context Engineering · Context Window · Token Budget]] · **Libraries:** [[Libraries/numpy (python)|numpy]]  

## Prerequisites

Stated upstream: `Phase 10 (LLMs from Scratch), Phase 11 Lesson 01-02`

- **11/01-02**:
    - [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]]
    - [[Lessons/11-02 Few-Shot, Chain-of-Thought, Tree-of-Thought|11/02 Few-Shot, Chain-of-Thought, Tree-of-Thought]]
- Whole phase: [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] — LLMs from Scratch ·  medium confidence

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Builds on this

- [[Lessons/11-06 RAG (Retrieval-Augmented Generation)|11/06 RAG (Retrieval-Augmented Generation)]]
- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]]
- [[Lessons/11-15 Prompt Caching and Context Caching|11/15 Prompt Caching and Context Caching]]

## Concepts taught

- [[Concepts/Context Window|Context Window]] `glossary` — The maximum number of tokens (input + output) the model processes in a single forward pass -- 400K for GPT-5, 200K (1M beta) for Claude Opus 4.7, 2M for Gemini 3 Pro
- [[Concepts/Context Engineering|Context Engineering]] `glossary` — The discipline of deciding what goes into the context window, in what order, and at what priority -- encompasses retrieval, compression, tool selection, and memory management
- [[Concepts/Lost in the Middle|Lost in the Middle]] (as *Lost-in-the-middle*) `glossary` — Empirical finding that LLMs attend better to the beginning and end of context, with 10-20% accuracy drop for information placed in the middle
- [[Concepts/Token Budget|Token Budget]] `glossary` — An explicit allocation of context window capacity across components (system prompt, tools, history, retrieval, generation) with per-component limits
- Dynamic context `lesson term` — Assembling the context window differently for each query based on intent classification, relevant tool selection, and retrieval results
- History summarization `lesson term` — Replacing verbatim old conversation turns with a concise summary, reducing token cost while preserving key information
- Tool pruning `lesson term` — Classifying query intent and only including tool definitions that match, reducing tool token cost by 60-80%
- [[Concepts/Long-term memory|Long-term memory]] `lesson term` — Facts and preferences stored in a database and retrieved at session start -- CLAUDE.md, ChatGPT Memory, and similar systems
- [[Concepts/Episodic memory|Episodic memory]] `lesson term` — Past interactions stored as embeddings and retrieved when the current query is similar to a past conversation
- Generation budget `lesson term` — Tokens reserved for the model's output -- if the context fills the window completely, the model has no room to respond

## Ships

- [[Artifacts/11-05 prompt-context-optimizer|prompt-context-optimizer]] `prompt` — Audit a context assembly strategy and recommend optimizations to reduce token waste and improve response quality
- [[Artifacts/11-05 skill-context-engineering|skill-context-engineering]] `skill` — Decision framework for designing context assembly pipelines based on task type, window size, and latency budget

## Further reading

- [[Resources/Anthropic — Contextual Retrieval|Anthropic — Contextual Retrieval]] ([link](https://www.anthropic.com/news/contextual-retrieval)) — how Anthropic approaches context-aware chunk retrieval, reducing retrieval failure by 49% ·  also cited by 3 other lessons
- [[Resources/Pope et al., 2022 - -Efficiently Scaling Transformer Inference|Pope et al., 2022 -- "Efficiently Scaling Transformer Inference]] ([link](https://arxiv.org/abs/2211.05102)) — why context length drives memory and latency, and how KV cache, MQA, and GQA change the budget calculation. ·  also cited by 2 other lessons
- [[Resources/Ainslie et al. (2023). GQA- Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints|Ainslie et al. (2023). GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints]] ([link](https://arxiv.org/abs/2305.13245)) — the grouped-query attention paper that cut KV memory 8× in production decoders without quality loss. ·  also cited by 2 other lessons
- [[Resources/Liu et al. (2024). Lost in the Middle- How Language Models Use Long Contexts|Liu et al. (2024). Lost in the Middle: How Language Models Use Long Contexts]] ([link](https://arxiv.org/abs/2307.03172)) — the definitive study on position-dependent attention, showing that models struggle with information in the middle of long contexts ·  also cited by 2 other lessons
- [[Resources/Agrawal et al., -SARATHI- Efficient LLM Inference by Piggybacking Decodes with Chunked Prefills- (2023)|Agrawal et al., "SARATHI: Efficient LLM Inference by Piggybacking Decodes with Chunked Prefills" (2023)]] ([link](https://arxiv.org/abs/2308.16369)) — the two phases of inference that make long prompts expensive in TTFT but cheap in TPOT; the ground truth behind context-packing tradeoffs. ·  also cited by 1 other lesson
- [[Resources/Kamradt (2023). Needle in a Haystack analysis|Kamradt (2023). Needle in a Haystack analysis]] ([link](https://github.com/gkamradt/LLMTest_NeedleInAHaystack)) — the benchmark that revealed position-dependent retrieval failures across all major models ·  also cited by 1 other lesson
- [[Resources/LangChain documentation on RAG|LangChain documentation on RAG]] ([link](https://python.langchain.com/docs/tutorials/rag/)) — practical implementation of retrieval-augmented generation as a context engineering pattern ·  also cited by 1 other lesson
- Simon Willison's "Context Engineering ([link](https://simonwillison.net/2025/Jun/27/context-engineering/)) — the blog post that named the discipline and distinguished it from prompt engineering

## In learning paths

- [[Paths/Agent Systems Engineering|Agent Systems Engineering]] — step 6, required
- [[Paths/AI Data Systems|AI Data Systems]] — step 6, required
- [[Paths/LLM Product Engineering|LLM Product Engineering]] — step 4, required
- [[Paths/Building and Deploying AI Applications|Building and Deploying AI Applications]] — step 4, required


%% ── my notes ── %%
