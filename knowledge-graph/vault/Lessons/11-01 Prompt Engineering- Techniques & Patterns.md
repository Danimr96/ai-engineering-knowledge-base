---
id: "lesson:11/01"
type: lesson
ref: 11/01
phase: 11
num: 1
title: "Prompt Engineering: Techniques & Patterns"
lesson_type: build
languages:
  - Python
time_min: 90
on_route: false
quiz_count: 0
code_files: 2
concepts: 11
prereqs: 5
community: 1
aliases:
  - 11/01
  - 11-01
tags:
  - phase/11
  - type/build
  - community/01
  - stdlib-only
source: ai-engineering-from-scratch/phases/11-llm-engineering/01-prompt-engineering/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/01-prompt-engineering"
---

# 11/01 Prompt Engineering: Techniques & Patterns

> Most people write prompts like they are texting a friend. Then they wonder why a 200-billion parameter model gives mediocre answers. Prompt engineering is not about tricks. It is about understanding that every token you send is an instruction, and the model follows instructions literally. Write better instructions, get better outputs. It is that simple and that hard.

**Phase:** [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] · **Type:** Build · **Time:** 90 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/11-llm-engineering/01-prompt-engineering/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/01-prompt-engineering) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/11-llm-engineering/01-prompt-engineering) · code: main.ts, prompt_engineering.py  
**Community:** [[Communities/01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism|01 Expert Parallelism · Pipeline Parallelism · Tensor Parallelism]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 10, Lessons 01-05 (LLMs from Scratch)`

- **10/01-05** — LLMs from Scratch:
    - [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]]
    - [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]]
    - [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]]
    - [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]]
    - [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]]

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]
- depth 3: [[Lessons/01-04 Calculus for Machine Learning|01/04 Calculus for Machine Learning]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/03-02 Multi-Layer Networks and Forward Pass|03/02 Multi-Layer Networks and Forward Pass]], [[Lessons/03-05 Loss Functions|03/05 Loss Functions]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/19-42 Large Corpus Downloader|19/42 Large Corpus Downloader]], [[Lessons/19-43 HDF5 Tokenized Corpus|19/43 HDF5 Tokenized Corpus]], [[Lessons/19-44 Cosine LR with Linear Warmup|19/44 Cosine LR with Linear Warmup]], [[Lessons/19-45 Gradient Clipping and Mixed Precision|19/45 Gradient Clipping and Mixed Precision]], [[Lessons/19-46 Gradient Accumulation|19/46 Gradient Accumulation]], [[Lessons/19-47 Checkpoint Save and Resume|19/47 Checkpoint Save and Resume]], [[Lessons/19-48 Distributed Data Parallel and FSDP from Scratch|19/48 Distributed Data Parallel and FSDP from Scratch]], [[Lessons/19-49 Language Model Evaluation Harness|19/49 Language Model Evaluation Harness]]

## Builds on this

- [[Lessons/11-02 Few-Shot, Chain-of-Thought, Tree-of-Thought|11/02 Few-Shot, Chain-of-Thought, Tree-of-Thought]]
- [[Lessons/11-04 Embeddings & Vector Representations|11/04 Embeddings & Vector Representations]]
- [[Lessons/11-05 Context Engineering- Windows, Budgets, Memory, and Retrieval|11/05 Context Engineering: Windows, Budgets, Memory, and Retrieval]]
- [[Lessons/11-06 RAG (Retrieval-Augmented Generation)|11/06 RAG (Retrieval-Augmented Generation)]]
- [[Lessons/11-10 Evaluation & Testing LLM Applications|11/10 Evaluation & Testing LLM Applications]]
- [[Lessons/11-12 Guardrails, Safety & Content Filtering|11/12 Guardrails, Safety & Content Filtering]]
- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]]
- [[Lessons/11-15 Prompt Caching and Context Caching|11/15 Prompt Caching and Context Caching]]

## Concepts taught

- System message `lesson term` — A special message processed with high priority that sets identity, rules, and constraints for the model's entire conversation
- [[Concepts/Temperature|Temperature]] `glossary` — A scaling factor on the logit distribution before softmax -- higher values flatten the distribution (more random), lower values sharpen it (more deterministic)
- [[Concepts/Nucleus Sampling (Top-p)|Nucleus Sampling (Top-p)]] (as *Top-p*) `glossary` — Limit token sampling to the smallest set whose cumulative probability exceeds p, cutting off the long tail of unlikely tokens
- [[Concepts/Few-Shot|Few-Shot]] (as *Few-shot prompting*) `glossary` — Including 2-10 input/output examples in the prompt so the model learns the task pattern without any fine-tuning
- [[Concepts/Chain of Thought (CoT)|Chain of Thought (CoT)]] (as *Chain-of-thought*) `glossary` — Prompting the model to show intermediate reasoning steps, which improves accuracy on math, logic, and multi-step problems by 10-40%
- Role prompting `lesson term` — Setting a persona that biases sampling toward a specific quality distribution in the training data
- [[Concepts/Prompt Injection|Prompt Injection]] `glossary` — An attack where user input contains instructions that override the system prompt, causing the model to ignore its rules
- [[Concepts/Context Window|Context Window]] `glossary` — The maximum number of tokens (input + output) the model can process in a single call -- ranges from 8K to 2M across current models
- Assistant prefill `lesson term` — Providing the first few tokens of the model's response to steer format and eliminate preamble -- supported natively by Anthropic
- Meta-prompting `lesson term` — Using an LLM to generate, critique, and optimize prompts for other LLM tasks
- [[Concepts/Prompt Engineering|Prompt Engineering]] `glossary` — Designing model-facing instructions, examples, constraints, and output requirements to improve behavior on a defined task.

## Ships

- [[Artifacts/11-01 prompt-prompt-optimizer|prompt-prompt-optimizer]] `prompt` — Takes a draft prompt and rewrites it using proven prompt engineering patterns for maximum effectiveness across models
- [[Artifacts/11-01 skill-prompt-patterns|skill-prompt-patterns]] `skill` — Decision framework for choosing the right prompt pattern based on task type, reliability requirements, and target model

## Further reading

- [[Resources/Wei et al., 2022 - -Chain-of-Thought Prompting Elicits Reasoning in Large Language Models|Wei et al., 2022 -- "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models]] ([link](https://arxiv.org/abs/2201.11903)) — the foundational paper showing that "think step by step" improves LLM accuracy by 10-40% on reasoning tasks ·  also cited by 1 other lesson
- Zamfirescu-Pereira et al., 2023 -- "Why Johnny Can't Prompt ([link](https://arxiv.org/abs/2304.13529)) — research on how non-experts struggle with prompt engineering and what makes prompts effective
- Shin et al., 2023 -- "Prompt Engineering a Prompt Engineer ([link](https://arxiv.org/abs/2311.05661)) — using LLMs to automatically optimize prompts, the foundation of meta-prompting
- [[Resources/LMSYS Chatbot Arena|LMSYS Chatbot Arena]] ([link](https://chat.lmsys.org/)) — live blind comparison of LLMs where you can test the same prompt across models and vote on which response is better ·  also cited by 2 other lessons
- Anthropic Prompt Engineering Guide ([link](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)) — Claude-specific techniques including XML formatting, assistant prefill, and thinking tags
- Anthropic prompt library ([link](https://docs.anthropic.com/en/prompt-library)) — curated, known-good prompts by use case; shows the structural patterns that ship in production.
- OpenAI Prompt Engineering Guide ([link](https://platform.openai.com/docs/guides/prompt-engineering)) — official best practices from OpenAI covering system messages, few-shot, and chain-of-thought
- DAIR.AI Prompt Engineering Guide ([link](https://www.promptingguide.ai/)) — exhaustive catalogue of prompt techniques with examples (zero-shot, few-shot, CoT, ReAct, self-consistency); the reference practitioners use for the broader "Prompt engineering" surface.

## In learning paths

- [[Paths/LLM Product Engineering|LLM Product Engineering]] — step 1, required
- [[Paths/Building and Deploying AI Applications|Building and Deploying AI Applications]] — step 1, required


%% ── my notes ── %%
