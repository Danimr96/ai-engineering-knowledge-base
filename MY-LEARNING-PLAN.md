# My Learning Plan: AI Engineering from Scratch

Source: https://github.com/rohitg00/ai-engineering-from-scratch · https://aiengineeringfromscratch.com
Repo: `AI-Education/ai-engineering-from-scratch` · Python: `.venv` (3.12)
Rewritten: 2026-09-24

## Starting point

- 7 years working in machine learning. Currently building knowledge bases, knowledge graphs and RAG.
- Energy engineering background, so no formal math, computer science or software engineering training. The gaps are foundations, not practice.
- **The route starts at Phase 10 (LLMs from Scratch)** and goes through it in order.
- Earlier phases come in only as **bridges**: a short lesson right before the Phase 10 lesson that depends on it. If a quick check shows I already know the topic, I skip the bridge.

---

## Route: Phase 10 core (about 20 h, plus bridges)

| # | Lesson | Time | Bridges to check first |
|---|---|---|---|
| 10/01 | Tokenizers: BPE, WordPiece, SentencePiece | 90m | none |
| 10/02 | Building a tokenizer from scratch | 90m | none |
| 10/03 | Data pipelines for pre-training | 90m | none |
| 10/04 | **Pre-training a mini GPT** (numpy, backward pass written by hand) | 120m | 01/05 chain rule and autodiff · 03/03 backprop · 01/09 information theory (cross-entropy) · 03/06 optimizers (Adam) · 07/02 self-attention · 07/03 multi-head · 07/04 positional encoding · 07/05 full transformer |
| 10/05 | Scaling: distributed training, FSDP, DeepSpeed | 120m | none (companion: 19/76 collective ops from scratch) |
| 10/06 | Instruction tuning (SFT) | 90m | none |
| 10/07 | RLHF: reward model and PPO | 90m | 09/01 MDPs · 09/06 policy gradients · 09/08 PPO |
| 10/08 | DPO | 90m | 01/06 probability (Bradley-Terry, log-likelihood) |
| 10/09 | Constitutional AI and self-improvement | 45m | none |
| 10/10 | Evaluation: benchmarks, LM harness | 90m | none |
| 10/11 | Quantization | 120m | 01/13 numerical stability (floating-point formats) |
| 10/12 | Inference optimization | 120m | 07/12 KV cache and flash attention |
| 10/13 | Complete LLM pipeline (capstone) | 120m | all of the above |

**Proof project after 10/13:** capstones 19/30 to 19/41. They rebuild the same GPT step by step in PyTorch: BPE, dataset, embeddings, attention, block, GPT assembly, training, loading pretrained weights, classifier fine-tuning, SFT, DPO, eval.

## Route: Phase 10 advanced (about 12 h)

| # | Lesson | Bridges |
|---|---|---|
| 10/14 | Open models: architecture walkthroughs | 07/11 mixture of experts |
| 10/25 | Speculative decoding and EAGLE | 07/16 speculative decoding |
| 10/15 | Speculative decoding and EAGLE-3 (overlaps 10/25, so skim whichever comes second) | |
| 10/16 | Differential attention V2 | 07/15 attention variants |
| 10/17 | Native sparse attention (DeepSeek NSA) | |
| 10/18 | Multi-token prediction | |
| 10/19 | DualPipe parallelism | |
| 10/20 | DeepSeek-V3 walkthrough (ties 14–19 together) | |
| 10/21 | Jamba: hybrid SSM-transformer | |
| 10/22 | Async and Hogwild! inference | |
| 10/34 | Gradient checkpointing | |

## After Phase 10 (to decide later)

- Phases 11–14 (LLM engineering, multimodal, tools and MCP, agents): I already work in this area. Test out with `/check-understanding 11` and so on, and only study the lessons I fail.
- Phase 8 (image, audio and video generation): optional. The worthwhile core is 08/01, 02, 06, 07 and 13.
- Math foundations (Phase 1) as a whole: only if the bridges show a pattern of gaps.

---

## Per-lesson loop

1. **Calibrate:** a quick check on the bridges. Skip what I already know.
2. **Visual lesson page:** diagrams, interactive labs, predict-then-reveal (saved in `lessons/`).
3. **Build it myself:** stubs and tests in `learning-artifacts/NN-slug/`. Claude gives hints and reviews, not solutions.
4. **Run the repo's reference code** and compare it with mine.
5. **Quiz:** the lesson's `quiz.json` plus Claude's questions.
6. **Reflection, 3–5 lines:** what changed in how I think about LLMs, and where it shows up in my KB/graph/RAG work.

## Repo tools (Claude Code opened inside `ai-engineering-from-scratch/`)

| Command | Use |
|---|---|
| `/check-understanding N` | Test out of a phase |
| `/course-guide` | "Where is X taught?" |
| `/learn` | The repo's own terminal tutor (an alternative to the visual lessons) |

The website is good for reading on a phone or tablet and for its interactive figures.
