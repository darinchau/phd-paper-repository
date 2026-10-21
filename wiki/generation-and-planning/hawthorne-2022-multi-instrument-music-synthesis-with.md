---
title: "Multi-instrument Music Synthesis with Spectrogram Diffusion"
authors: "Curtis Hawthorne, Ian Simon, Adam Roberts, Neil Zeghidour, Josh Gardner, Ethan Manilow, and Jesse Engel"
year: 2022
doi: 10.48550/arXiv.2206.05408
source: hawthorne-2022-multi-instrument-music-synthesis-with.md
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/hawthorne-2022-multi-instrument-music-synthesis-with.pdf"
pdf_filename: hawthorne-2022-multi-instrument-music-synthesis-with.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
tags: [midi-to-audio, synthesis, diffusion, spectrogram, mt3, multi-instrument, real-time, gan-vocoder]
---

# Multi-instrument Music Synthesis with Spectrogram Diffusion

## Summary

This paper treats synthesis as transcription run backwards. MT3 note tokens for any instrument combination condition a T5 encoder-decoder that generates 5.12-second mel-spectrogram segments; a diffusion decoder is conditioned on the previous segment to keep boundaries smooth, and a GAN inverter produces 16 kHz audio. The base model is slightly faster than real time and reaches transcription F1 0.36, which equals the inverter's ceiling and is well below the 0.63 achievable from raw audio. Diffusion beats an autoregressive decoder on FAD/reconstruction. The paper is the clearest demonstration that the same symbolic vocabulary can serve both directions, and that the audio-side representation — not the note model alone — limits fidelity.

## Key Contributions

- MIDI-to-spectrogram synthesis with arbitrary instrument combinations, using the MT3 note vocabulary.
- A segment-wise diffusion decoder with previous-segment context, avoiding autoregressive frame-by-frame generation and boundary artifacts.
- A real-time two-stage pipeline (transformer + GAN inverter) with note-level composition and instrumentation control.
- A measured decomposition of error: model quality vs spectrogram-inverter quality vs raw-audio ceiling.

## Methodology and Architecture

Note encoder: T5-style, 2,048 positions. Optional context encoder: 256 frames of the previous spectrogram. Decoder: 256 positions × 20 ms = 5.12 s segments; cross-attention over note and context encoders; FiLM injection of diffusion time. DDPM with L1 noise-prediction loss, logSNR/cosine schedule, 1,000 sampling steps, classifier-free guidance (dropout 0.1, weight 2.0). Autoregressive baseline: same stack, causal masking, MSE on frames, fixed-variance dithering. Vocoder: MelGAN-style GAN trained on 16k hours of music; 16 kHz, 128 mel bins, 20 ms hop. Data: MAESTRO, Slakh2100, Cerberus4, GuitarSet, MusicNet, URMP, mapped to 34 Slakh classes plus drums.

## Results

| Model | VGGish FAD ↓ | TRILL FAD ↓ | Transcription F1 ↑ | RT factor |
|---|---:|---:|---:|---:|
| Small autoregressive | 1.03 | 0.39 | 0.31 | 10.55 |
| Small + context | 1.10 | 0.53 | 0.25 | 3.07 |
| Base + context | 1.00 | 0.27 | 0.36 | 1.05 |
| Ground truth, encoded | 0.51 | 0.05 | 0.36 | 12.25 |
| Ground truth, raw | 0.00 | 0.00 | 0.63 | — |

The base diffusion model is the best synthesis model and matches the encoded-audio ceiling. The gap to raw audio (0.36 → 0.63) is the inverter's loss, not the note model's. The paper reports no listening test; musicality is supported by examples, not ratings. Segment context is necessary for boundary consistency but does not guarantee long-range timbral consistency.

## Related Papers

- [[overviews/audio-symbolic-transfer]] — the inverse direction: symbolic controlling audio, sharing MT3 tokens with transcription.
- [[data-and-representation/chang-2024-yourmt3-multi-instrument-music-transcription]] — the transcription side of the same token vocabulary, with a real-world quality ceiling.
- [[concepts/transcription-as-supervision]] — synthesis and transcription as inverse label functions; the inverter is a learned renderer that defines the audio-side likelihood.
- [[generation-and-planning/chen-2024-sympac-scalable-symbolic-music]] — symbolic generation whose outputs could feed this renderer.
- [[generation-and-planning/zhu-2025-efficient-fine-grained-guidance-for]] — symbolic diffusion with hard constraints, a different control target.
