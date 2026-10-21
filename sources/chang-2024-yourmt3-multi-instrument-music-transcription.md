---
title: "YourMT3+: Multi-instrument Music Transcription with Enhanced Transformer Architectures and Cross-dataset Stem Augmentation"
authors: "Sungkyun Chang, Emmanouil Benetos, Holger Kirchhoff, and Simon Dixon"
year: 2024
doi: 10.48550/arXiv.2407.04822
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/chang-2024-yourmt3-multi-instrument-music-transcription.pdf"
pdf_filename: chang-2024-yourmt3-multi-instrument-music-transcription.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
---

# YourMT3+: Multi-instrument Music Transcription with Enhanced Transformer Architectures and Cross-dataset Stem Augmentation

## One-line Summary

YourMT3+ combines a PerceiverTF spectral-cross-attention encoder with mixture-of-experts feed-forward layers, an MT3-style note-token decoder, a multi-channel decoder that masks unannotated instruments, and cross-dataset stem augmentation; it beats MT3 and PerceiverTF on multi-instrument benchmarks and transcribes singing without a separation front-end, but non-mainstream instruments in real pop recordings remain below 10% F1.

## 1. Document Information

- **Authors and affiliations:** Sungkyun Chang, Emmanouil Benetos, Holger Kirchhoff, Simon Dixon; Centre for Digital Music, Queen Mary University of London, and Huawei.
- **Venue and version:** IEEE MLSP 2024; arXiv 2407.04822v3, 1 August 2024. 15 PDF pages: main pp. 1–5, references pp. 5–8, supplement pp. 8–15 (the supplement is included in the PDF).
- **Extraction:** full text via `pdftotext -layout`; Figure 1 (architecture), Tables 1–3, Figures 2–3 (per-instrument and pop-music results), and §5.2 inspected.
- **Artifacts:** code, datasets, and demos at `https://github.com/mimbres/YourMT3`.
- **Anchors:** architecture §3 pp. 2–3; token design §3.3 p. 3; augmentation §4 pp. 3–4; data Table 1 p. 3; results Table 2 p. 3 and Table 3 p. 4; pop-music limitation §5.2 p. 4.

## 2. Key Contributions

1. **YPTF encoder**: PerceiverTF's hierarchical spectral cross-attention plus RoPE, pre-RMSNorm, and mixture-of-experts feed-forward layers (two of eight experts active).
2. **Multi-channel decoder**: one decoder channel per instrument group (13 channels from 26 latents), so loss can be masked for unannotated instruments and partially labelled datasets become usable.
3. **Cross-dataset stem augmentation**: intra-stem dropout plus iterative mixing of stems from other datasets, with pitch shifting; this enables direct singing transcription (F1 3.6% → 64% without separation).
4. **A broad, reproducible benchmark**: ten public datasets plus refined RWC-Pop annotations, with an explicit negative result on commercial pop music.

## 3. Methodology and Architecture

- **Input.** 2.048 s audio; YMT3 uses a 256×512 log-mel spectrogram; YPTF uses a 110×1,024 log-magnitude spectrogram plus a 2D ResNet pre-encoder producing 128×128 features.
- **Encoder.** PerceiverTF-style latent array with spectral cross-attention (local transformer over frequency, temporal transformer over time), 26 latents = 13 instrument-group channels × 2. RoPE in every sub-block; pre-RMSNorm. MoE replaces the FFN with 8 experts, top-2 routing.
- **Decoder.** T5-small-style autoregressive decoder conditioned on encoder states. Single-channel MT3 tokens for the baseline; multi-channel version decodes each of 13 channels independently with shared parameters, max 256 tokens per channel. Tokens follow MT3 FULL PLUS: program, pitch, velocity (only 0/1 retained), tie, shift; programs 100/101 are reserved for lead/chorus singing.
- **Training.** AdamWScale, cosine schedule, 300K steps, lr 1e-2 → 1e-5, dropout 0.05, 2×A100, bf16. Datasets: MusicNet-EM, GuitarSet, MIR-ST500, ENST-Drums, Slakh, EGMD, MAESTRO, CMedia, URMP, SMT-Bass (train); tests include MAPS, RWC-Pop, and the same corpora under splits.
- **Augmentation.** Intra-stem: keep each stem with p = 0.7. Cross-stem: iteratively add filtered stems from other datasets with survival probability e^(−0.3j), up to 5 iterations, capped at 1,024 tokens. Pitch shift −2…+2 semitones via GPU phase vocoder.

## 4. Key Results and Benchmarks

**Multi-instrument (Table 3, p. 4; Slakh).**

| Model | Onset F1 | Offset F1 | Drum F1 |
|---|---:|---:|---:|
| YPTF.MoE+Multi | 84.6 | 70.7 | 90.1 |
| MT3 (reproduced) | 75.2 | 56.8 | 83.9 |
| MT3 (paper) | 76 | 57 | — |
| PerceiverTF | 81.9 | — | 78.3 |

**Other datasets (Table 2, p. 3).** YPTF.MoE+Multi reaches MAPS piano 87.88 (vs MT3 80.62), MusicNet-EM strings 91.32, MusicNet winds 96.98, URMP onset 91.65, GuitarSet 85.92, and ENST-drums 88.79–89.48 depending on input. Singing on MIR-ST500 is 55.95 with separated input and 55.33 without; the paper notes that timing errors often fall in the 50–100 ms range, so the 100 ms protocol is more favourable.

**Ablation (Table 3, p. 4).** Starting from the YMT3 base (onset 64.8), intra-stem augmentation adds +4.8, full vocabulary +4.0, data balancing +4.0, cross-stem +1.8, PTF encoder +1.5, MoE +1.8, and the multi-channel decoder brings the final model to 84.6. These are cumulative, not independent, effects.

**Pop-music negative result (Figure 3, §5.2, p. 4).** On refined RWC-Pop, non-main instruments (everything except piano, bass, vocals, drums) fall below 10% F1; the model is biased toward synthetic training timbres, and pitched instruments show octave errors in chroma-level metrics. This is the paper's own strongest limitation and the key evidence that multi-instrument transcription is not solved.

## 5. Limitations and Future Work

- **Pop/real-world gap.** Training is dominated by synthetic or clean stems (Slakh, URMP, MusicNet); commercial mixtures with reverberation, compression, and overlapping timbres degrade sharply.
- **Singing timing.** Onset errors cluster at 50–100 ms; the model is less precise than a piano-roll baseline on vocal onsets.
- **Token vocabulary and sequence length.** The multi-channel decoder caps each channel at 256 tokens, so dense passages truncate; the paper discusses truncation loss in the supplement.
- **Evaluation labels.** MusicNet-EM and RWC-Pop annotations are refined or partially annotated; cross-dataset comparisons inherit label noise.
- **No generation or representation study.** The output is notes; the paper does not test whether the transcriptions are good enough as symbolic training data for generation, which is exactly the Aria/SymPAC question.
- **Compute.** 2×A100 for 300K steps is a non-trivial budget for a solo lab, though the released code mitigates it.

## 6. Related Work

- MT3: the token-decoding template and main baseline.
- PerceiverTF: spectral cross-attention and latent-array encoder.
- Onsets-and-frames and high-resolution piano transcription: frame-based alternatives.
- Slakh, URMP, MusicNet, MAESTRO, GuitarSet, ENST-Drums, MIR-ST500, RWC-Pop: the benchmark suite.
- Source separation (Spleeter) and singing transcription: the front-end alternative that cross-stem augmentation tries to avoid.
- Aria-AMT / Aria-MIDI: the piano-only scale counterpart.

## 7. Glossary

- **AMT:** Automatic Music Transcription.
- **MT3:** Multi-Task Multitrack Music Transcription.
- **PTF:** PerceiverTF.
- **MoE:** Mixture of Experts.
- **SCA:** Spectral Cross-Attention.
- **RoPE:** Rotary Position Embedding.
- **F1:** harmonic mean of precision and recall.
- **SVS:** Singing Voice Separation.
- **RWC-Pop:** a Japanese popular-music corpus with annotations.
