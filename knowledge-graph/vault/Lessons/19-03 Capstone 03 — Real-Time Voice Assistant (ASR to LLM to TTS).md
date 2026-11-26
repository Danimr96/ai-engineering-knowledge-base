---
id: "lesson:19/03"
type: lesson
ref: 19/03
phase: 19
num: 3
title: "Capstone 03 — Real-Time Voice Assistant (ASR to LLM to TTS)"
lesson_type: capstone
languages:
  - Python
  - TypeScript
time_min: 1800
on_route: false
quiz_count: 7
code_files: 10
concepts: 7
prereqs: 0
community: 9
libraries:
  - hono
  - ws
  - zod
aliases:
  - 19/03
  - 19-03
tags:
  - phase/19
  - type/capstone
  - community/09
  - stdlib-only
source: ai-engineering-from-scratch/phases/19-capstone-projects/03-realtime-voice-assistant/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/03-realtime-voice-assistant"
---

# 19/03 Capstone 03 — Real-Time Voice Assistant (ASR to LLM to TTS)

> A voice agent that feels right has end-to-end latency under 800ms, knows when you have stopped talking, handles barge-in, and can call a tool without stalling. Retell, Vapi, LiveKit Agents, and Pipecat all hit this bar in 2026. They do it with the same shape: a streaming ASR, a turn-detector, a streaming LLM, and a streaming TTS, all wired through WebRTC with aggressive latency budgets at every hop. Build one, measure WER and MOS and false-cutoff rate, and run it under packet loss.

**Phase:** [[Phases/19 Capstone Projects|Phase 19: Capstone Projects]] · **Type:** Capstone · **Time:** 1800 min · **Languages:** Python, TypeScript · **Status:** —  
**Open:** [[Upstream/19-capstone-projects/03-realtime-voice-assistant/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/19-capstone-projects/03-realtime-voice-assistant) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/19-capstone-projects/03-realtime-voice-assistant) · code: main.py, ts/src/index.ts, ts/src/orchestrator.ts, ts/src/protocol.ts, ts/src/server.ts, ts/src/types.ts … · quiz: 7 questions  
**Community:** [[Communities/09 VAD · Barge-in · Full duplex|09 VAD · Barge-in · Full duplex]] · **Libraries:** [[Libraries/hono (typescript)|hono]], [[Libraries/ws (typescript)|ws]], [[Libraries/zod (typescript)|zod]]  

## Prerequisites

Stated upstream: `Phase 6 (speech and audio), Phase 7 (transformers), Phase 11 (LLM engineering), Phase 13 (tools), Phase 14 (agents), Phase 17 (infrastructure)`

- Whole phase: [[Phases/11 LLM Engineering|Phase 11: LLM Engineering]] — LLM engineering ·  medium confidence
- Whole phase: [[Phases/13 Tools & Protocols|Phase 13: Tools & Protocols]] — tools ·  medium confidence
- Whole phase: [[Phases/14 Agent Engineering|Phase 14: Agent Engineering]] — agents ·  medium confidence
- Whole phase: [[Phases/17 Infrastructure & Production|Phase 17: Infrastructure & Production]] — infrastructure ·  medium confidence
- Whole phase: [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] — speech and audio ·  medium confidence
- Whole phase: [[Phases/07 Transformers Deep Dive|Phase 7: Transformers Deep Dive]] — transformers ·  medium confidence

## Concepts taught

- [[Concepts/Turn detection|Turn detection]] `lesson term` — Classifier that, given VAD silence and a partial transcript, decides the user is done speaking
- [[Concepts/Barge-in|Barge-in]] `lesson term` — Canceling TTS mid-playback when VAD detects new user speech
- First-audio-out `lesson term` — Time from user stops speaking to the first audio packet leaving the server
- [[Concepts/VAD|VAD]] `lesson term` — Model classifying audio frames as speech vs silence; Silero VAD v5 is the 2026 default
- [[Concepts/Jitter buffer|Jitter buffer]] `lesson term` — Client-side buffer that holds packets briefly to absorb network variance
- Filler `lesson term` — Short phrase the agent emits to avoid silence when a tool is slow
- [[Concepts/MOS|MOS]] `lesson term` — Perceptual speech quality rating; NISQA is the automated proxy

## Ships

- [[Artifacts/19-03 voice-agent|voice-agent]] `skill` — Build a real-time voice agent with sub-800ms first-audio-out, barge-in handling, and mid-conversation tool use.

## Further reading

- Deepgram Nova-3 documentation ([link](https://developers.deepgram.com/docs)) — streaming ASR reference
- Cartesia Sonic-2 ([link](https://docs.cartesia.ai)) — low-latency TTS reference
- Retell AI architecture ([link](https://docs.retellai.com)) — production voice agent architecture
- Vapi.ai production stack ([link](https://docs.vapi.ai)) — alternate production reference
- [[Resources/LiveKit Agents 1.0|LiveKit Agents 1.0]] ([link](https://github.com/livekit/agents)) — reference WebRTC agent framework ·  also cited by 1 other lesson
- [[Resources/Pipecat — voice agent examples|Pipecat — voice agent examples]] ([link](https://github.com/pipecat-ai/pipecat)) — alternate Python-first streaming agent framework ·  also cited by 1 other lesson
- [[Resources/Silero VAD repo|Silero VAD repo]] ([link](https://github.com/snakers4/silero-vad)) — VAD reference model ·  also cited by 2 other lessons
- [[Resources/OpenAI Realtime API|OpenAI Realtime API]] ([link](https://platform.openai.com/docs/guides/realtime)) — reference for integrated speech models ·  also cited by 2 other lessons


%% ── my notes ── %%
