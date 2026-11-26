---
id: "lesson:11/10"
type: lesson
ref: 11/10
phase: 11
num: 10
title: "Evaluation & Testing LLM Applications"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 11
prereqs: 2
community: 3
aliases:
  - 11/10
  - 11-10
tags:
  - phase/11
  - type/build
  - community/03
  - stdlib-only
source: ai-engineering-from-scratch/phases/11-llm-engineering/10-evaluation/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/10-evaluation"
---

# 11/10 Evaluation & Testing LLM Applications

> You would never deploy a web app without tests. You would never ship a database migration without a rollback plan. But right now, most teams ship LLM applications by reading 10 outputs and saying "yeah, looks good." That is not evaluation. That is hope. Hope is not an engineering practice. Every prompt change, every model swap, every temperature tweak changes your output distribution in ways you cannot predict by reading a handful of examples. Evaluation is the only thing standing between your application and silent degradation.

**Phase:** [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/11-llm-engineering/10-evaluation/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/11-llm-engineering/10-evaluation) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/11-llm-engineering/10-evaluation) · code: eval_framework.py  
**Community:** [[Communities/03 Parallel tool calls · Strict mode · Refusal|03 Parallel tool calls · Strict mode · Refusal]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 11 Lesson 01 (Prompt Engineering), Lesson 09 (Function Calling)`

- [[Lessons/11-01 Prompt Engineering- Techniques & Patterns|11/01 Prompt Engineering: Techniques & Patterns]] — Prompt Engineering
- [[Lessons/11-09 Function Calling & Tool Use|11/09 Function Calling & Tool Use]] — Function Calling

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Builds on this

- [[Lessons/11-13 Building a Production LLM Application|11/13 Building a Production LLM Application]]
- [[Lessons/19-68 RAG Evaluation- Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance|19/68 RAG Evaluation: Precision, Recall, MRR, nDCG, Faithfulness, Answer Relevance]]
- [[Lessons/19-69 End-to-End RAG System|19/69 End-to-End RAG System]]

## Concepts taught

- [[Concepts/Evaluation (Eval)|Evaluation (Eval)]] (as *Eval*) `glossary` — Systematically scoring LLM outputs against defined criteria using automated metrics, LLM judges, or human review
- [[Concepts/LLM-as-a-Judge|LLM-as-a-Judge]] (as *LLM-as-judge*) `glossary` — Using a strong model (GPT-4o, Claude) to score outputs against a rubric -- correlates 80-85% with human judgment
- Rubric `lesson term` — Anchored descriptions for each score level (1-5) that reduce judge variance by defining exactly what each score means
- ROUGE-L `lesson term` — Longest Common Subsequence-based metric measuring how much of the reference appears in the output -- recall-oriented
- [[Concepts/Confidence interval|Confidence interval]] `lesson term` — A range around your measured score that tells you how much uncertainty remains -- wider with fewer test cases
- Regression testing `lesson term` — Running the same eval suite on old and new prompt versions to detect quality degradation before deployment
- Golden test set `lesson term` — Curated input-output pairs representing your most important use cases -- every change must pass these
- Pairwise comparison `lesson term` — Showing a judge two outputs and asking which is better -- eliminates scale calibration problems
- [[Concepts/Bootstrap|Bootstrap]] `lesson term` — Estimating confidence intervals by repeatedly sampling from your scores with replacement -- works with any distribution
- Wilson interval `lesson term` — A confidence interval for pass/fail rates that works correctly even with small sample sizes or extreme proportions

## Ships

- [[Artifacts/11-10 prompt-eval-designer|prompt-eval-designer]] `prompt` — Design tailored evaluation rubrics and test suites for LLM applications from a description of the use case
- [[Artifacts/11-10 skill-eval-patterns|skill-eval-patterns]] `skill` — Decision framework for choosing evaluation strategies -- when to use which method, how to size test suites, and how to integrate evals into CI/CD

## Further reading

- Ribeiro et al., 2020 -- "Beyond Accuracy: Behavioral Testing of NLP Models with CheckList ([link](https://arxiv.org/abs/2005.04118)) — systematic behavioral testing methodology (minimum functionality, invariance, directional expectations) applicable to LLM evaluation
- [[Resources/Liu et al. (2023). G-Eval- NLG Evaluation using GPT-4 with Better Human Alignment|Liu et al. (2023). G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment]] ([link](https://arxiv.org/abs/2303.16634)) — chain-of-thought + form-filling as a judge protocol; the calibration and bias results every judge-builder needs. ·  also cited by 1 other lesson
- [[Resources/Zheng et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena|Zheng et al. (2023). Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena]] ([link](https://arxiv.org/abs/2306.05685)) — the foundational paper on using LLMs to judge other LLMs, introducing MT-Bench and the pairwise comparison protocol ·  also cited by 2 other lessons
- [[Resources/Es et al. (2023). RAGAS- Automated Evaluation of Retrieval Augmented Generation|Es et al. (2023). RAGAS: Automated Evaluation of Retrieval Augmented Generation]] ([link](https://arxiv.org/abs/2309.15217)) — reference-free metrics for RAG (faithfulness, answer relevancy, context precision/recall); the eval pattern that scales to prod without labelers. ·  also cited by 1 other lesson
- Braintrust Eval Guide ([link](https://www.braintrust.dev/docs)) — production eval platform with experiment tracking, scoring functions, and dataset management
- [[Resources/LMSYS Chatbot Arena|LMSYS Chatbot Arena]] ([link](https://chat.lmsys.org/)) — live human evaluation platform where users vote on model outputs, the largest pairwise comparison dataset for LLMs ·  also cited by 2 other lessons
- DeepEval Documentation ([link](https://docs.confident-ai.com)) — Python-native eval framework with 14+ metrics, Pytest integration, and hallucination detection
- [[Resources/EleutherAI lm-evaluation-harness|EleutherAI lm-evaluation-harness]] ([link](https://github.com/EleutherAI/lm-evaluation-harness)) — the standard framework for automated benchmarks (MMLU, HellaSwag, TruthfulQA, BIG-Bench); the engine behind the Open LLM Leaderboard. ·  also cited by 1 other lesson
- Hugging Face LLM Evaluation Guidebook ([link](https://huggingface.co/spaces/OpenEvals/evaluation-guidebook)) — practical advice on data contamination, metric selection, and reproducibility from the team maintaining the Open LLM Leaderboard.
- promptfoo Documentation ([link](https://promptfoo.dev/docs/intro)) — the most practical open-source eval framework with YAML config, 15+ providers, LLM-as-judge, and CI integration

## In learning paths

- [[Paths/AI Data Systems|AI Data Systems]] — step 9, required
- [[Paths/AI Evaluation and Reliability|AI Evaluation and Reliability]] — step 2, required
- [[Paths/LLM Product Engineering|LLM Product Engineering]] — step 7, required
- [[Paths/Building and Deploying AI Applications|Building and Deploying AI Applications]] — step 6, required
- [[Paths/Customer AI Deployment|Customer AI Deployment]] — step 7, required


%% ── my notes ── %%
