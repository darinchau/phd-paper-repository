---
title: "MIDI-REPA: Improving Text-to-Music Generation with Symbolic Representation Alignment"
authors: Song-Ze Yu, Fang-Duo Tsai, Yi-Hsuan Yang
year: 2026
doi: 10.48550/arXiv.2610.20967
source: yu-2026-midi-repa-improving-text-to-music.md
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/yu-2026-midi-repa-improving-text-to-music.pdf"
pdf_filename: yu-2026-midi-repa-improving-text-to-music.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
tags: [representation-alignment, symbolic-supervision, text-to-music, amt]
---

## Summary

MIDI-REPA adds an auxiliary alignment loss that pulls an early layer of a 122M flow-matching text-to-music DiT toward AMT-derived piano rolls. The best configuration (MuScriptor merged roll, layer L2, full flow trajectory) ranks first by Borda on the ATTM benchmark while training in 14.2 A100-equivalent GPU-hours, about a thirteenth of the baseline's cost. It is the mirror image of the AGT premise: symbolic content improves an audio model, not the reverse.

## Key Contributions

- A representation-alignment objective for symbolic supervision of audio generation: cosine similarity between a projected hidden state and a time-aligned piano roll, λ = 0.5. [§2.1]
- A design study over teacher (Basic Pitch vs MuScriptor), target (roll vs instrument cube), layer (L0–L11), and timestep interval. [§3]
- JamendoMIDI: 51,077 usable AMT-transcribed tracks; 49,034 used for training (3,161 hours). [§2.2.3]
- Competitive ATTM scores at a fraction of the baseline compute. [Table 4]

## Methodology and Architecture

FluxAudio-S (122M, T5+CLAP conditioning, 12 MMDiT blocks) is trained with flow matching plus a REPA-style alignment loss on an intermediate block. The symbolic target is an AMT piano roll at 108 frames × 88 pitches, produced offline. A one-layer temporal convolution projects the hidden state into the symbolic space; alignment is applied only during training, and inference needs text only.

## Results

- Teacher: MuScriptor roll best (FAD 0.5040, CLAP 0.2603 vs baseline 0.5275 / 0.2220); Basic Pitch roll is worse than no alignment (FAD 0.5363). [Table 1]
- Layer: L2 best (FAD 0.4947, CLAP 0.2686); alignment helps CLAP at every tested block and FAD at all but L0. [Table 3]
- Timesteps: full trajectory is best; late-only alignment loses FAD or CLAP. [Table 5]
- ATTM: rank 1 Borda; FAD 0.497, CLAP 0.315, CCS 0.829; 14.2 A100-equivalent hours versus 190.3 for the baseline. [Table 4]

The finding that noisy Basic Pitch targets hurt is directly relevant to AGT: the quality of the symbolic teacher is a first-order variable, so an AMT teacher is not a neutral label source.

## Related Papers

- [[overviews/audio-symbolic-transfer]] — the audio→symbolic direction and the transcription-quality constraint.
- [[overviews/cross-modal-supervision-transfer]] — symbolic/audio supervision as a special case of cross-modal transfer.
- [[generation-and-planning/jonason-2025-smart-tuning-a-symbolic-music]] — the reverse intervention: an audio reward tunes a symbolic generator.
