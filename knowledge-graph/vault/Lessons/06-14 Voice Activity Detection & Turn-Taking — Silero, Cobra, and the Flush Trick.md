---
id: "lesson:06/14"
type: lesson
ref: 06/14
phase: 6
num: 14
title: "Voice Activity Detection & Turn-Taking — Silero, Cobra, and the Flush Trick"
lesson_type: build
languages:
  - Python
time_min: 45
on_route: false
quiz_count: 0
code_files: 1
concepts: 7
prereqs: 2
community: 9
aliases:
  - 06/14
  - 06-14
tags:
  - phase/06
  - type/build
  - community/09
  - stdlib-only
source: ai-engineering-from-scratch/phases/06-speech-and-audio/14-voice-activity-detection-turn-taking/docs/en.md
github: "https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/14-voice-activity-detection-turn-taking"
---

# 06/14 Voice Activity Detection & Turn-Taking — Silero, Cobra, and the Flush Trick

> Every voice agent lives or dies on two decisions: is the user speaking now, and are they done? VAD answers the first. Turn-detection (VAD + silence-hangover + semantic endpoint model) answers the second. Get either wrong and your assistant either cuts users off or never shuts up.

**Phase:** [[Phases/06 Speech & Audio|Phase 6: Speech & Audio]] · **Type:** Build · **Time:** 45 min · **Languages:** Python · **Status:** —  
**Open:** [[Upstream/06-speech-and-audio/14-voice-activity-detection-turn-taking/docs/en|lesson text in Obsidian]] · [GitHub](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/06-speech-and-audio/14-voice-activity-detection-turn-taking) · [folder](file:///Users/danielmartinez/Documents/Proyectos%20Personales/AI-Education/ai-engineering-from-scratch/phases/06-speech-and-audio/14-voice-activity-detection-turn-taking) · code: main.py  
**Community:** [[Communities/09 VAD · Barge-in · Full duplex|09 VAD · Barge-in · Full duplex]] · **Libraries:** standard library only  

## Prerequisites

Stated upstream: `Phase 6 · 11 (Real-Time Audio), Phase 6 · 12 (Voice Assistant)`

- [[Lessons/06-11 Real-Time Audio Processing|06/11 Real-Time Audio Processing]] — Real-Time Audio
- [[Lessons/06-12 Build a Voice Assistant Pipeline — The Phase 6 Capstone|06/12 Build a Voice Assistant Pipeline — The Phase 6 Capstone]] — Voice Assistant

### Before this lesson (transitive, depth 2–3)

- depth 2: [[Lessons/06-02 Spectrograms, Mel Scale & Audio Features|06/02 Spectrograms, Mel Scale & Audio Features]], [[Lessons/06-04 Speech Recognition (ASR) — CTC, RNN-T, Attention|06/04 Speech Recognition (ASR) — CTC, RNN-T, Attention]], [[Lessons/06-05 Whisper — Architecture & Fine-Tuning|06/05 Whisper — Architecture & Fine-Tuning]], [[Lessons/06-06 Speaker Recognition & Verification|06/06 Speaker Recognition & Verification]], [[Lessons/06-07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro|06/07 Text-to-Speech (TTS) — From Tacotron to F5 and Kokoro]], [[Lessons/11-09 Function Calling & Tool Use|11/09 Function Calling & Tool Use]], [[Lessons/14-01 The Agent Loop- Observe, Think, Act|14/01 The Agent Loop: Observe, Think, Act]]
- depth 3: [[Lessons/05-08 CNNs and RNNs for Text|05/08 CNNs and RNNs for Text]], [[Lessons/05-09 Sequence-to-Sequence Models|05/09 Sequence-to-Sequence Models]], [[Lessons/05-10 Attention Mechanism — The Breakthrough|05/10 Attention Mechanism — The Breakthrough]], [[Lessons/05-22 Embedding Models — The 2026 Deep Dive|05/22 Embedding Models — The 2026 Deep Dive]], [[Lessons/06-01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform|06/01 Audio Fundamentals — Waveforms, Sampling, Fourier Transform]], [[Lessons/07-05 The Full Transformer — Encoder + Decoder|07/05 The Full Transformer — Encoder + Decoder]], [[Lessons/11-03 Structured Outputs- JSON, Schema Validation, Constrained Decoding|11/03 Structured Outputs: JSON, Schema Validation, Constrained Decoding]]

## Concepts taught

- [[Concepts/VAD|VAD]] `lesson term` — Binary per-frame: is this speech?
- [[Concepts/Turn detection|Turn detection]] `lesson term` — VAD + silence-hangover + semantic endpoint.
- Silence hangover `lesson term` — Time to wait before declaring turn end; 500-800 ms.
- [[Concepts/Pre-roll|Pre-roll]] `lesson term` — Keep 300-500 ms audio before VAD fires.
- Flush trick `lesson term` — VAD → flush-STT → 125 ms instead of 500 ms delay.
- Semantic endpoint `lesson term` — ML classifier that looks at words, not just silence.
- TPR @ FPR 5% `lesson term` — Standard VAD benchmark; 87.7% for Silero, 50% WebRTC.

## Ships

- [[Artifacts/06-14 vad-tuner|vad-tuner]] `skill` — Pick VAD model, threshold, silence hangover, pre-roll, and turn-detection strategy for a voice agent.

## Further reading

- LiveKit — turn detection ([link](https://docs.livekit.io/agents/logic/turns/)) — semantic endpointing in production.
- [[Resources/Bredin et al. (2023). pyannote.audio 3.1|Bredin et al. (2023). pyannote.audio 3.1]] ([link](https://github.com/pyannote/pyannote-audio)) — diarization-grade segmentation. ·  also cited by 1 other lesson
- [[Resources/Silero VAD repo|Silero VAD repo]] ([link](https://github.com/snakers4/silero-vad)) — the reference open VAD. ·  also cited by 2 other lessons
- Kyutai — Unmute + flush trick ([link](https://kyutai.org/stt)) — the sub-200 ms engineering trick.
- Picovoice Cobra VAD ([link](https://picovoice.ai/products/cobra/)) — commercial accuracy leader.
- WebRTC VAD ([link](https://webrtc.googlesource.com/src/)) — the legacy baseline.


%% ── my notes ── %%
