---
title: "Sori: Streamable and Controllable Model for Non-musical Audio to Symbolic Music Transformation"
authors: Kyungsu Kim, Yejin Kim, Kyogu Lee
year: 2026
doi: 10.48550/arXiv.2610.15474
category: generation-and-planning
source: kim-2026-sori-streamable-and-controllable.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/kim-2026-sori-streamable-and-controllable.pdf"
pdf_filename: kim-2026-sori-streamable-and-controllable.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-31
tags:
  - audio-to-symbolic
  - controllable-generation
  - classifier-free-guidance
  - domain-adversarial-training
  - streaming-inference
---
## Summary

Sori defines non-musical audio to symbolic music transformation and trains a streaming encoder–decoder Transformer for it without any paired non-musical-audio/MIDI data: a domain-adversarial encoder aligns rain, speech or coughs to the musical feature space while the decoder is trained only on music. One classifier-free-guidance parameter γ then moves the output continuously from “ignore the input” to “follow the input closely”, at the cost of musicality, and the model runs in real time on a laptop CPU.

## Key Contributions

- **A task definition with two evaluation axes.** Input correspondence and musicality are measured separately because the task is one-to-many; no paired supervision exists.
- **Domain-adversarial training as the data workaround.** Only the encoder sees non-musical audio in the adversarial signal; the musical decoder stays purely musical.
- **A single interpretable control.** γ is a continuous, inference-time trade-off knob rather than a fixed operating point, which suits live use.
- **Bounded-latency streaming.** At most four events per 50 ms frame with a spillover flag, plus ALiBi positions and an attention-sink KV cache.

## Methodology and Architecture

A 16 kHz log-mel input (512 bins, 50 ms hop) feeds an eight-layer encoder (d = 768). An eight-layer temporal decoder produces per-frame context and a four-layer event decoder emits up to four note events per frame from a 530-token vocabulary. The model is trained on 9.53M rendered five-second segments from 953 instruments, with 530k held-out segments from 53 disjoint instruments, and tested on the unbalanced AudioSet split, which is not filtered for music. Evaluation combines onset F1 over 11 DSP detectors, multi-scale spectrogram distance, Fréchet Music Distance with CLaMP 2 embeddings against held-out Nlakh, and a listening study with 21 retained participants.

The complete evidence-grounded digest, with page anchors and the full Table 1, is in [`sources/kim-2026-sori-streamable-and-controllable.md`](../../sources/kim-2026-sori-streamable-and-controllable.md).

## Results

Objective correspondence improves monotonically with γ — onset F1 from 0.087 at γ = 0 to 0.368 at γ = 3.0, spectral distance from 57.2 to 11.8 — while musicality peaks at moderate guidance: FMD is best at γ = 0.5 (33.6) and listener-rated musicality is highest there too (3.34), falling to 2.20 at γ = 3.0 [PDF p. 4, Table 1]. At γ = 1.0 the model beats all three transcription baselines on onset F1, spectral distance and FMD. Removing domain-adversarial training improves correspondence at strong guidance but worsens FMD (324.0) and rated musicality (1.98), so the adversarial objective moves the trade-off curve rather than lifting it. Streaming runs at a mean real-time factor of 0.82 (max 0.90) on an Apple M3 CPU with 64 ms algorithmic latency [PDF p. 4].

## Related Papers

- [[concepts/audio-symbolic-modality-gap]] — the concept Sori attacks from the generation side: it does not transcribe a shared signal but maps an out-of-domain signal into a musical one.
- [[overviews/audio-symbolic-transfer]] — batch overview on audio–symbolic transfer, where Sori is the one-to-many, controllability-first entry.
- [[generation-and-planning/wang-2022-audio-to-symbolic-arrangement-via-cross-modal]] — audio-to-symbolic arrangement with cross-modal representation learning instead of adversarial domain alignment.
- [[retrieval-and-recombination/wu-2025-clamp-3-universal-music]] — contrastive audio–symbolic alignment, the embedding route to the same modality problem.
- [[overviews/2026-symbolic-music-literature-map]] — batch index for the October 2026 intake this reading belongs to.
