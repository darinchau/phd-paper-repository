---
title: "YourMT3+: Multi-instrument Music Transcription with Enhanced Transformer Architectures and Cross-dataset Stem Augmentation"
authors: "Sungkyun Chang, Emmanouil Benetos, Holger Kirchhoff, and Simon Dixon"
year: 2024
doi: 10.48550/arXiv.2407.04822
source: chang-2024-yourmt3-multi-instrument-music-transcription.md
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/chang-2024-yourmt3-multi-instrument-music-transcription.pdf"
pdf_filename: chang-2024-yourmt3-multi-instrument-music-transcription.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
tags: [multi-instrument, transcription, perceiver, mixture-of-experts, stem-augmentation, slakh, pop-music, negative-result]
---

# YourMT3+: Multi-instrument Music Transcription with Enhanced Transformer Architectures and Cross-dataset Stem Augmentation

## Summary

YourMT3+ is the current practical ceiling for open multi-instrument transcription. It pairs a PerceiverTF spectral-cross-attention encoder with MoE layers, an MT3 token decoder, a 13-channel decoder for partially labelled data, and cross-dataset stem augmentation. It reaches 84.6 Multi F1 on Slakh versus 75.2 for reproduced MT3 and 81.9 for PerceiverTF, and it transcribes singing without separation (3.6% → 64% onset F1). The paper's own pop-music test is the important counterweight: on real RWC-Pop mixes, non-main instruments fall below 10% F1, so the "transcribe anything" pipeline is not there yet. For the audio→symbolic line, this is the bottleneck paper: piano works, multi-instrument is benchmark-dependent.

## Key Contributions

- A hybrid encoder combining hierarchical spectral cross-attention, RoPE, and mixture-of-experts.
- A multi-channel decoder that makes partially annotated datasets usable by masking per-instrument loss.
- Cross-dataset intra-/cross-stem augmentation that improves robustness and removes the need for a singing-separation front-end.
- A ten-dataset reproducible benchmark plus refined RWC-Pop labels, including a candid real-world failure analysis.

## Methodology and Architecture

Input is a 2.048 s log-magnitude spectrogram plus a ResNet pre-encoder. The encoder uses 26 latents (two per instrument group) and alternating spectral/temporal transformers; MoE replaces the FFN (8 experts, top-2). The decoder is T5-small-style autoregressive with MT3 FULL PLUS tokens (program, pitch, velocity 0/1, tie, shift); the multi-channel variant decodes 13 channels independently with shared weights and 256-token limits. Training: AdamWScale, 300K steps, 2×A100, bf16. Augmentation: keep stems with p = 0.7; iteratively add stems from other datasets with survival e^(−0.3j), up to five iterations; pitch shift ±2 semitones. Evaluation: instrument note-onset F1 (±50 ms), instrument-agnostic onset, offset, and multi F1.

## Results

| Benchmark | YourMT3+ | MT3 | PerceiverTF | Anchor |
|---|---:|---:|---:|---|
| Slakh Multi F1 | 84.6 | 75.2 | 81.9 | Table 3, p. 4 |
| Slakh Onset F1 | 84.6 | 75.2 | 81.9 | Table 3, p. 4 |
| MAPS piano | 87.88 | 80.62 | — | Table 2, p. 3 |
| URMP onset | 91.65 | 70.31 | — | Table 2, p. 3 |
| Singing without separation | 55.33 | 3.6 (YMT3) | — | §5.2, p. 4 |
| RWC-Pop non-main instruments | <10% | — | — | Figure 3, p. 4 |

The Slakh number is synthetic-stem-friendly; the RWC-Pop number is the real-world check, and it is poor. The paper attributes this to training-set timbre bias and octave errors, and calls for more varied pitch-shifting and real recordings. The ablation is cumulative, so component contributions are not independent.

## Related Papers

- [[overviews/audio-symbolic-transfer]] — the transcription-quality bottleneck that limits "get past piano".
- [[concepts/transcription-as-supervision]] — why transcription F1 is not the same as symbolic-data quality for generation.
- [[data-and-representation/bradshaw-2025-aria-midi-a-dataset-of]] — piano-only scale, where transcription is reliable enough to build a 100k-hour corpus.
- [[generation-and-planning/chen-2024-sympac-scalable-symbolic-music]] — a generation system that depends on this kind of multi-track transcription.
- [[generation-and-planning/hawthorne-2022-multi-instrument-music-synthesis-with]] — the inverse task, which uses the same MT3 token vocabulary.
- [[data-and-representation/jung-2025-unified-cross-modal-translation-of]] — unified score/symbolic/audio translation.
