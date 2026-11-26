---
id: "lesson:14/22"
type: lesson
ref: 14/22
phase: 14
num: 22
title: "Voice Agents: Pipecat and LiveKit"
lesson_type: learn
languages:
  - Python
time_min: 60
on_route: false
quiz_count: 7
code_files: 1
concepts: 8
prereqs: 2
community: 7
aliases:
  - 14/22
  - 14-22
tags:
  - phase/14
  - type/learn
  - community/07
  - stdlib-only
source: ai-engineering-from-scratch/phases/14-agent-engineering/22-voice-agents-pipecat-livekit/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/22-voice-agents-pipecat-livekit"
---

# 14/22 Voice Agents: Pipecat and LiveKit

> Voice agents are a first-class production category in 2026. Pipecat gives you a Python frame-based pipeline (VAD → STT → LLM → TTS → transport). LiveKit Agents bridges AI models to users over WebRTC. Production latency targets land at 450–600ms end-to-end for premium stacks.

**Phase:** [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] · **Type:** Learn · **Time:** 60 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/14-agent-engineering/22-voice-agents-pipecat-livekit/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering/22-voice-agents-pipecat-livekit) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/14-agent-engineering/22-voice-agents-pipecat-livekit) · code: main.py · quiz: 7 questions  
**Community:** [[Communities/07 Swarm · Evaluator-Optimizer · Debate|07 Swarm · Evaluator-Optimizer · Debate]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 14 · 01 (Agent Loop), Phase 14 · 12 (Workflow Patterns)`

- [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]] — Agent Loop
- [[Lessons/14-12 Anthropic's Workflow Patterns- Simple Over Complex|14/12 Anthropic's Workflow Patterns: Simple Over Complex]] — Workflow Patterns

## Builds on this

- [[Lessons/14-29 Production Runtimes- Queue, Event, Cron|14/29 Production Runtimes: Queue, Event, Cron]]
- [[Lessons/14-30 Eval-Driven Agent Development|14/30 Eval-Driven Agent Development]]

## Concepts taught

- [[Concepts/Frame|Frame]] `lesson term` — Typed unit of data in the pipeline (audio, transcript, text, control)
- Processor `lesson term` — Handler with process(frame)
- DOWNSTREAM `lesson term` — Source to sink: audio in, speech out
- UPSTREAM `lesson term` — Control: cancel, metrics, barge-in
- [[Concepts/VAD|VAD]] `lesson term` — Detects when user is speaking
- Semantic turn detection `lesson term` — Model-based decision that the user is done
- MultimodalAgent `lesson term` — Audio in, audio out; no text in the middle
- VoicePipelineAgent `lesson term` — STT + LLM + TTS; text-level control

## Ships

- [[Artifacts/14-22 voice-pipeline|voice-pipeline]] `skill` — Scaffold a Pipecat-shaped voice pipeline (VAD + STT + LLM + TTS + transport) with barge-in, confidence gating, and latency budget enforcement.

## Further reading

- [[Resources/LiveKit Agents framework (2024)|LiveKit Agents framework (2024)]] ([link](https://docs.livekit.io/agents/)) — WebRTC + voice primitives ·  also cited by 2 other lessons
- Pipecat docs ([link](https://docs.pipecat.ai/getting-started/introduction)) — frame-based pipeline, processors, transports
- Retell AI ([link](https://www.retellai.com/)) — managed voice, latency-benchmarked
- Vapi ([link](https://vapi.ai/)) — managed voice platform


%% ── my notes ── %%
