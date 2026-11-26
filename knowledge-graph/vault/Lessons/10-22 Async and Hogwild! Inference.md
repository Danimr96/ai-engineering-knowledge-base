---
id: "lesson:10/22"
type: lesson
ref: 10/22
phase: 10
num: 22
title: "Async and Hogwild! Inference"
lesson_type: build
languages:
  - Python
time_min: 60
status: planned
status_auto: planned
on_route: true
route_order: 23
quiz_count: 0
code_files: 1
concepts: 9
prereqs: 2
aliases:
  - 10/22
  - 10-22
tags:
  - phase/10
  - type/build
  - status/planned
  - route
  - stdlib-only
source: ai-engineering-from-scratch/phases/10-llms-from-scratch/22-async-hogwild-inference/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/22-async-hogwild-inference"
---

# 10/22 Async and Hogwild! Inference

> Speculative decoding (Phase 10 · 15) parallelizes tokens within one sequence. Multi-agent frameworks parallelize across whole sequences but force explicit coordination (voting, sub-task splitting). Hogwild! Inference (Rodionov et al., arXiv:2504.06261) does something else: run N instances of the same LLM in parallel against a SHARED key-value cache. Each worker sees every other worker's generated tokens instantly. Modern reasoning models — QwQ, DeepSeek-R1 — can self-coordinate through that shared cache without any fine-tuning. The approach is experimental but it opens an entirely new axis of inference parallelism that sits orthogonal to spec decode. This lesson implements a two-worker Hogwild! simulator in stdlib Python and explains why the shared-cache collaboration emerges from the existing model's reasoning abilities.

**Phase:** [[Phases/10 LLMs from Scratch|Phase 10: LLMs from Scratch]] · **Type:** Build · **Time:** 60 min · **Languages:** Python · **Status:** planned  
**Open:** [[Upstream/10-llms-from-scratch/22-async-hogwild-inference/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/10-llms-from-scratch/22-async-hogwild-inference) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/10-llms-from-scratch/22-async-hogwild-inference) · code: main.py  
**Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 10 · 12 (inference optimization), Phase 10 · 15 (speculative decoding)`

- [[Lessons/10-12 Inference Optimization|10/12 Inference Optimization]] — inference optimization
- [[Lessons/10-15 Speculative Decoding and EAGLE-3|10/15 Speculative Decoding and EAGLE-3]] — speculative decoding

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/07-12 KV Cache, Flash Attention & Inference Optimization|07/12 KV Cache, Flash Attention & Inference Optimization]], [[Lessons/07-16 Speculative Decoding — Draft, Verify, Repeat|07/16 Speculative Decoding — Draft, Verify, Repeat]], [[Lessons/10-01 Tokenizers- BPE, WordPiece, SentencePiece|10/01 Tokenizers: BPE, WordPiece, SentencePiece]], [[Lessons/10-02 Building a Tokenizer from Scratch|10/02 Building a Tokenizer from Scratch]], [[Lessons/10-03 Data Pipelines for Pre-Training|10/03 Data Pipelines for Pre-Training]], [[Lessons/10-04 Pre-Training a Mini GPT (124M Parameters)|10/04 Pre-Training a Mini GPT (124M Parameters)]], [[Lessons/10-05 Scaling- Distributed Training, FSDP, DeepSpeed|10/05 Scaling: Distributed Training, FSDP, DeepSpeed]], [[Lessons/10-06 Instruction Tuning (SFT)|10/06 Instruction Tuning (SFT)]], [[Lessons/10-07 RLHF- Reward Model + PPO|10/07 RLHF: Reward Model + PPO]], [[Lessons/10-08 DPO- Direct Preference Optimization|10/08 DPO: Direct Preference Optimization]]
- depth 3: [[Lessons/01-05 Chain Rule & Automatic Differentiation|01/05 Chain Rule & Automatic Differentiation]], [[Lessons/01-06 Probability and Distributions|01/06 Probability and Distributions]], [[Lessons/01-09 Information Theory|01/09 Information Theory]], [[Lessons/03-03 Backpropagation from Scratch|03/03 Backpropagation from Scratch]], [[Lessons/03-06 Optimizers|03/06 Optimizers]], [[Lessons/07-02 Self-Attention from Scratch|07/02 Self-Attention from Scratch]], [[Lessons/07-03 Multi-Head Attention|07/03 Multi-Head Attention]], [[Lessons/07-04 Positional Encoding — Sinusoidal, RoPE, ALiBi|07/04 Positional Encoding — Sinusoidal, RoPE, ALiBi]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/07-07 GPT — Causal Language Modeling|07/07 GPT — Causal Language Modeling]], [[Lessons/09-01 MDPs, States, Actions & Rewards|09/01 MDPs, States, Actions & Rewards]], [[Lessons/09-06 Policy Gradient — REINFORCE from Scratch|09/06 Policy Gradient — REINFORCE from Scratch]], [[Lessons/09-08 Proximal Policy Optimization (PPO)|09/08 Proximal Policy Optimization (PPO)]], [[Lessons/19-76 Collective Ops From Scratch|19/76 Collective Ops From Scratch]]

## Concepts taught

- Hogwild! `lesson term` — N instances of the same LLM running concurrently with one shared KV cache; emergent coordination via self-prompting
- Shared KV cache `lesson term` — A single growing KV buffer that all workers read and write; enables instant token visibility across workers
- Emergent coordination `lesson term` — Reasoning-capable LLMs can read the shared cache and divide work without any fine-tuning or explicit protocol
- Coordination overhead (as *Coordination overhead (c)*) `lesson term` — The per-worker cost of reading the extended cache and deciding what to do; must stay small vs total decode time
- Parallelizable fraction (as *Parallelizable fraction (p)*) `lesson term` — Task-level parallelism: the fraction of the total work that is not intrinsically sequential
- RoPE enables Hogwild! `lesson term` — Because positions are rotations, writing into a shared cache does not require recomputing prior tokens
- Voting ensemble `lesson term` — The simplest parallel inference topology; useful for classification, less for long-form reasoning
- [[Concepts/Tree of thought|Tree of thought]] `lesson term` — Reasoning strategy that explores multiple branches and prunes; explicit coordination logic
- Multi-agent framework `lesson term` — Each agent gets a role; a coordinator orchestrates; heavy protocol overhead

## Ships

- [[Artifacts/10-22 parallel-inference-router|parallel-inference-router]] `skill` — Route a reasoning workload between voting, tree-of-thought, multi-agent, Hogwild!, and speculative decoding strategies.

## Further reading

- Recht, Re, Wright, Niu — Hogwild!: A Lock-Free Approach to Parallelizing Stochastic Gradient Descent (arXiv:1106.5730, NeurIPS 2011) ([link](https://arxiv.org/abs/1106.5730)) — the original Hogwild!, the naming origin
- [[Resources/Su et al.- RoFormer (2021)|Su et al.: RoFormer (2021)]] ([link](https://arxiv.org/abs/2104.09864)) — RoPE, the property that makes shared-cache inference tractable ·  also cited by 3 other lessons
- [[Resources/Leviathan, Kalman, Matias (2023). Fast Inference from Transformers via Speculative Decoding|Leviathan, Kalman, Matias (2023). Fast Inference from Transformers via Speculative Decoding]] ([link](https://arxiv.org/abs/2211.17192)) — speculative decoding, the within-sequence parallelism Hogwild! composes with ·  also cited by 7 other lessons
- [[Resources/Yao et al. — Tree of Thoughts- Deliberate Problem Solving with Large Language Models (arXiv-2305.10601)|Yao et al. — Tree of Thoughts: Deliberate Problem Solving with Large Language Models (arXiv:2305.10601)]] ([link](https://arxiv.org/abs/2305.10601)) — the tree-of-thought reasoning strategy Hogwild! sits orthogonal to ·  also cited by 2 other lessons
- Rodionov et al. — Hogwild! Inference: Parallel LLM Generation via Concurrent Attention (arXiv:2504.06261) ([link](https://arxiv.org/abs/2504.06261)) — the Hogwild! paper, preliminary evaluation on QwQ and DeepSeek-R1
- Hogwild! reference PyTorch implementation ([link](https://github.com/eqimp/hogwild_llm)) — the single source of truth for the paper's experiments

## My route

- Step 23 in *Route: Phase 10 advanced (about 12 h)*
- Plan note: Async and Hogwild! inference
- Previous: [[Lessons/10-21 Jamba — Hybrid SSM-Transformer|10/21 Jamba — Hybrid SSM-Transformer]]
- Next: [[Lessons/10-34 Gradient Checkpointing and Activation Recomputation|10/34 Gradient Checkpointing and Activation Recomputation]]


%% ── my notes ── %%
