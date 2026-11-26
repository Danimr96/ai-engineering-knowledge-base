# Build report

Built at: 2026-09-25T18:28:59+00:00  
Upstream commit: `f6721a01`  

## Counts

| Node type | Count |
|---|---|
| artifact | 495 |
| category | 12 |
| community | 95 |
| concept | 3171 |
| learning_path | 12 |
| lesson | 523 |
| library | 35 |
| myth | 21 |
| phase | 20 |
| resource | 1670 |
| track | 5 |

| Edge type | Count |
|---|---|
| BRIDGE | 18 |
| CITES | 2420 |
| CONTAINS | 567 |
| INCLUDES | 145 |
| IN_CATEGORY | 250 |
| IN_COMMUNITY | 1055 |
| PHASE_REQUIRES | 21 |
| RELATED_TO | 935 |
| REQUIRES | 1627 |
| REQUIRES_PHASE | 165 |
| ROUTE_NEXT | 23 |
| SHIPS | 495 |
| TEACHES | 3905 |
| USES | 198 |

### Lesson coverage

| Metric | Value |
|---|---|
| lessons | 523 |
| lessons with at least one prerequisite edge | 521 |
| lessons whose field says None | 2 |
| lessons without a Prerequisites field | 0 |
| lessons with a field but zero edges (parser miss) | 0 |
| lessons with TEACHES edges | 473 |
| lessons with CITES edges | 441 |
| lessons with SHIPS edges | 446 |

## Validation

No dangling edges, no type mismatches, no self-loops.

## Extractor problems

None.
## Unparsed prerequisite fragments (5 in 5 distinct)

- `Calculus` — 08/13
- `Don't skip` — 07/14
- `basic NumPy` — 03/12
- `basic PyTorch familiarity` — 00/12
- `using MCP revision `2026-07-28`` — 13/23

## Key Terms matching

| Metric | Value |
|---|---|
| lessons with a Key Terms table | 473 |
| rows | 3801 |
| matched to a glossary term | 355 (9.3%) |
|   exact | 267 |
|   alias | 80 |
|   normalized | 6 |
| new (non-canonical) concepts created | 3446 |
| distinct non-canonical concepts | 2961 |

Most frequent unmatched terms (candidates for `data/aliases.json`):

- Rank (5)
- Pipeline (5)
- Bi-encoder (5)
- Cross-encoder (5)
- VAD (5)
- server/discover (5)
- Regularization (4)
- InfoNCE (4)
- Byte-level BPE (4)
- Constrained decoding (4)
- Tool call (4)
- Faithfulness (4)
- Causal mask (4)
- KL penalty (4)
- RLAIF (4)
- Constitutional AI (4)
- SWE-bench (4)
- EAGLE-3 (4)
- resultType (4)
- Task (4)
- Memory poisoning (4)
- Projection (3)
- Chain rule (3)
- Gradient checking (3)
- Sampling (3)
- Prior (3)
- Laplace smoothing (3)
- KL divergence (3)
- Mutual information (3)
- Curse of dimensionality (3)
- Condition number (3)
- Bootstrap (3)
- RoPE (3)
- Decision boundary (3)
- Sliding window (3)
- Forward pass (3)
- Vanishing gradient (3)
- RMSNorm (3)
- DataLoader (3)
- Tracing (3)

## Resources cited by 2+ lessons (359)

- Building Effective Agents — 17 lessons
- Anthropic — Measuring AI agent autonomy in practice — 17 lessons
- Sutton & Barto (2018). Reinforcement Learning: An Introduction, 2nd ed. — 11 lessons
- OpenTelemetry — GenAI semconv — 10 lessons
- LangGraph Plan-and-Execute tutorial — 10 lessons
- Attention Is All You Need — 9 lessons
- MCP server discovery — 9 lessons
- MCP Streamable HTTP — 9 lessons
- OpenAI Agents SDK docs — 9 lessons
- Leviathan, Kalman, Matias (2023). Fast Inference from Transformers via Speculative Decoding — 8 lessons
- DeepSeek-AI (2024). DeepSeek-V3 Technical Report — 8 lessons
- Llama 3 paper (Meta, 2024) — 8 lessons
- MCP 2026-07-28 key changes — 7 lessons
- Claude Agent SDK overview — 7 lessons
- Anthropic — Claude's Constitution (January 2026) — 7 lessons
- Anthropic engineering — How we built our multi-agent research system — 7 lessons
- Radford et al.: Whisper (2022) — 6 lessons
- ReAct — 6 lessons
- Model Context Protocol — Specification 2026-07-28 — 6 lessons
- CrewAI docs introduction — 6 lessons
- Nuseibeh and Easterbrook, Requirements Engineering: A Roadmap — 6 lessons
- Anthropic — Responsible Scaling Policy v3.0 (Feb 2026) — 6 lessons
- DeepMind Frontier Safety Framework v3 — 6 lessons
- Scaling Rectified Flow Transformers (Esser et al., SD3 paper) — 5 lessons
- Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection — 5 lessons
- Li et al. (2024). EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty — 5 lessons
- Li et al. (2025). EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test — 5 lessons
- InstructGPT paper — 5 lessons
- DeepSeek-AI (2025). DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning — 5 lessons
- OpenAI Function Calling Guide — 5 lessons

## Concepts taught by the most lessons

- Temperature — 8 lessons
- Agent — 6 lessons
- Checkpoint — 6 lessons
- Function Calling — 6 lessons
- Prompt Cache — 6 lessons
- Token — 6 lessons
- Learning Rate — 6 lessons
- Cross-Attention — 6 lessons
- Context Window — 5 lessons
- Handoff — 5 lessons
- KV Cache — 5 lessons
- LLM-as-a-Judge — 5 lessons
- Multi Round-Trip Request (MRTR) — 5 lessons
- Patch — 5 lessons
- Patch Embedding — 5 lessons
- Rank (non-canonical) — 5 lessons
- Cosine Similarity — 5 lessons
- Overfitting — 5 lessons
- Pipeline (non-canonical) — 5 lessons
- Bi-encoder (non-canonical) — 5 lessons
- Cross-encoder (non-canonical) — 5 lessons
- VAD (non-canonical) — 5 lessons
- Acceptance rate (non-canonical) — 5 lessons
- server/discover (non-canonical) — 5 lessons
- Activation Function — 4 lessons

## Libraries used by the most lessons

- numpy (python) — 75 lessons
- torch (python) — 62 lessons
- hono (typescript) — 10 lessons
- scikit-learn (python) — 8 lessons
- zod (typescript) — 5 lessons
- torchvision (python) — 4 lessons
- matplotlib (python) — 3 lessons
- pandas (python) — 2 lessons
- tiktoken (python) — 2 lessons
- @hono/node-server (typescript) — 2 lessons
- anthropic (python) — 1 lessons
- datasets (python) — 1 lessons
- huggingface_hub (python) — 1 lessons
- umap (python) — 1 lessons
- optuna (python) — 1 lessons
- jax (python) — 1 lessons
- optax (python) — 1 lessons
- diffusers (python) — 1 lessons
- pydantic (python) — 1 lessons
- scipy (python) — 1 lessons

Python lessons that need nothing outside the standard library: 389

## Communities (95 with at least 4 members)

| # | Label | Lessons | Concepts | Phases |
|---|---|---|---|---|
| 1 | Expert Parallelism · Pipeline Parallelism · Tensor Parallelism | 22 | 35 | 5, 7, 10, 11, 17 |
| 2 | Bucket · Causal mask · Manifest | 38 | 10 | 19 |
| 3 | Parallel tool calls · Strict mode · Refusal | 40 | 8 | 11, 13, 15, 19 |
| 4 | Overfitting · Underfitting · Data Leakage | 16 | 28 | 2 |
| 5 | Temperature · Autoregressive · Logits | 12 | 27 | 1, 7, 8 |
| 6 | Communicative dehallucination · Consensus · Contract Net | 23 | 15 | 16 |
| 7 | Swarm · Evaluator-Optimizer · Debate | 19 | 10 | 14 |
| 8 | Backpropagation · Gradient · Activation Function | 12 | 16 | 1 |
| 9 | VAD · Barge-in · Full duplex | 11 | 15 | 6, 19 |
| 10 | Trace · Shadow Traffic · requestState | 14 | 11 | 13, 19 |
| 11 | Learning Rate · Optimizer · Batch Size | 4 | 20 | 1, 2, 3 |
| 12 | Attention · Cross-Attention · Self-Attention | 12 | 12 | 4, 5, 7 |
| 13 | Object Multiplex · Clip · Divided attention | 14 | 8 | 4 |
| 14 | Least Privilege · Prompt Injection · Sandbox | 4 | 16 | 11, 13, 14, 19 |
| 15 | System of record · Block severity · Definition of done | 14 | 4 | 14 |
| 16 | Backpressure · Rate Limit · Admission Control | 0 | 17 |  |
| 17 | Tool Contract · Agent · Function Calling | 3 | 13 | 11, 14 |
| 18 | Embedding · Cosine Similarity · HNSW | 2 | 12 | 1, 11 |
| 19 | CIMD · DCR · Resource indicator | 6 | 8 | 13 |
| 20 | Acceptance rate · Draft model · EAGLE-3 | 5 | 8 | 7, 10, 19 |
| 21 | Time to First Token (TTFT) · Time per Output Token (TPOT) · Prefill | 2 | 11 | 17 |
| 22 | Backward pass · Forward pass · Vanishing gradient | 7 | 5 | 3 |
| 23 | Automatic Speech Recognition (ASR) · Llama Guard · Homoglyph | 6 | 5 | 15, 18 |
| 24 | Eval Set · Regression Test · Test Oracle | 0 | 11 |  |
| 25 | Regression detection · AlphaEvolve · RSP | 7 | 3 | 15 |
| 26 | BM25 · Reciprocal Rank Fusion (RRF) · Bi-encoder | 3 | 7 | 5, 11 |
| 27 | Decision boundary · Bias · ELBO | 5 | 5 | 3, 8 |
| 28 | Production-stack · RadixAttention · cache_control | 7 | 3 | 17 |
| 29 | Eval-context gaming · Time horizon · thread_id | 7 | 3 | 15 |
| 30 | Evaluation (Eval) · Kill switch · Non-determinism | 6 | 4 | 17 |
| 31 | GUI grounding · VisualWebArena · OSWorld | 4 | 6 | 12, 14 |
| 32 | Instruction-Following as Alignment Signal · Reward Hacking and Goodhart's Law · Sycophancy as RLHF Amplification | 10 | 0 | 18 |
| 33 | Advantage · Baseline · Actor | 4 | 5 | 9, 13 |
| 34 | Tensor · CUDA · Mixed Precision | 1 | 8 | 1 |
| 35 | Checkpoint · Durable Execution · Idempotency | 2 | 7 | 15 |
| 36 | Scope Contract · Coding Agent · Worktree | 0 | 9 |  |
| 37 | Discriminator · Generator · Minimax | 3 | 6 | 4, 8 |
| 38 | Dev Environment · Git & Collaboration · APIs & Keys | 9 | 0 | 0 |
| 39 | Skill Catalog · Agent Skill · Progressive Disclosure | 1 | 7 | 13 |
| 40 | NaFlex · Backbone · Hard negative | 2 | 6 | 12 |

Lessons in no community (isolated or in a cluster smaller than 4): 52
