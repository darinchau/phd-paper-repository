---
title: "Descriptor-Injected Cross-Modal Learning: A Systematic Exploration of Audio-MIDI Alignment via Spectral and Melodic Features"
authors: "Mariano Fernández Méndez"
year: 2026
doi: 10.48550/arXiv.2604.10283
category: retrieval-and-recombination
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/fernandez-mendez-2026-descriptor-injected-cross-modal-learning.pdf"
pdf_filename: fernandez-mendez-2026-descriptor-injected-cross-modal-learning.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
---

# Descriptor-Injected Cross-Modal Learning: A Systematic Exploration of Audio-MIDI Alignment via Spectral and Melodic Features

## One-line Summary

On MAESTRO, injecting a hand-crafted eight-band spectral-dynamics descriptor into a small audio encoder, and a local-pitch-interval descriptor into a MIDI encoder, raises audio–MIDI retrieval from 73.4% to 84.0% (five-seed mean), but the gain is causally carried almost entirely by the audio descriptor, and the model remains fragile to transposition, velocity change, and corpus shift.

## 1. Document Information

- **Author and affiliation:** Mariano Fernández Méndez, Asociación Civil AlterMundi, Córdoba, Argentina.
- **Version and venue:** arXiv 2604.10283v1, 11 April 2026; marked "Preprint. Under review." 26 PDF pages: main text pp. 1–18, references pp. 18–26. The paper discloses extensive AI assistance for coding, analysis, and manuscript preparation; scientific decisions are attributed to the human author.
- **Extraction:** full text via `pdftotext -layout`; Figures 1–3, Tables 1–12, the descriptor definitions, causal ablation, CKA analysis, and limitations section inspected.
- **Artifacts:** no dataset release is needed (MAESTRO v3.0.0); code availability is not stated in the PDF.
- **Anchors:** problem §3.1 p. 3; architecture §3.2 pp. 3–4; descriptors §3.4 pp. 5–6; injection §3.5 pp. 6–7; screening Table 2 p. 8; long-horizon Table 4 p. 8; causal ablation Table 6 pp. 9–10; CKA Table 8 p. 14; limitations §6 p. 17.

## 2. Key Contributions

1. **A taxonomy and screening campaign** of 13 descriptor–mechanism combinations, 6 architectural families, and 3 training schedules for audio–MIDI alignment.
2. **Reverse cross-attention**, where descriptor tokens are queries attending to encoder features; it produces 188 rather than 2,400 output tokens and is claimed to be 163× cheaper in attention operations while remaining competitive.
3. **A causal result with a twist.** The audio descriptor A4 (octave-band energy dynamics) is necessary at inference: zeroing it collapses the retrieval score by 75–78 points. The MIDI descriptor D4 (local pitch intervals) improves training but has near-zero inference effect in the dual models (the "D4 paradox").
4. **A mechanism analysis.** Centered Kernel Alignment rises from 0.435 to 0.794 between audio and MIDI transformer layers when descriptors are injected; the author argues the gain is representational convergence, not feature concatenation.

## 3. Methodology and Architecture

- **Task and metric.** Given a four-second audio segment and its aligned MIDI segment, retrieve the match. `S = min(R@10 audio→MIDI, R@10 MIDI→audio)`. Evaluation pools 256 items with 500 queries, including 64 hard negatives from the same piece at a different time and 32 same-composer negatives.
- **Encoders.** Audio: 4-layer 1D CNN (40× downsampling) + 4-layer transformer (d=1,024), 60M parameters, partially initialised from MERTEncoderLite. MIDI: pitch/velocity/duration embeddings + 4-layer pre-norm transformer (d=512), 13M parameters. Projection heads map both to 256 dimensions.
- **Loss.** VICReg (invariance 10, variance 10, covariance 1), chosen over InfoNCE for small batches and no negative pairs.
- **A4 descriptor.** STFT (nFFT 2,048, hop 512), log magnitude, average into 8 octave bands (47 Hz–12 kHz), temporal delta, per-band z-score. Shape 188×8.
- **D4 descriptor.** Four features per note: previous and next semitone interval normalised by two octaves, plus clamped versions within ±2 octaves. Shape N×4.
- **Injection.** Concatenation, standard cross-attention, or reverse cross-attention. Reverse cross-attention uses the 188 descriptor frames as queries, so the output is 188 tokens rather than 2,400; the author compares this to a Perceiver bottleneck.
- **Data.** MAESTRO v3.0.0, 1,276 performances, 200 hours, cut into four-second windows with one-second hop: 13,000 training segments. Piano only.

## 4. Key Results and Benchmarks

**Screening and confirmation.** D4+A4 concatenation (d4a4) reaches S = 83.8 at epoch 50 with a 60-epoch cosine schedule, versus D0 = 73.4 (Table 4, p. 8). A4-only reverse cross-attention reaches 82.0. Five-seed replication gives 84.0 ± 2.7 for d4a4, with non-overlapping ranges against D0 and Cohen d = 3.51 (p < 0.001).

**Causal ablation (Table 6, pp. 9–10).**

| Ablation | d4a4 ΔS | a4r ΔS | d4-a4r ΔS |
|---|---:|---:|---:|
| Zero A4 | −76.0 | −77.6 | −75.4 |
| Noise A4 | −61.8 | −53.0 | −53.0 |
| Shuffle A4 | −37.2 | −32.2 | −32.4 |
| Zero D4 | +0.6 | — | −0.4 |
| Shuffle D4 | +0.6 | — | −0.0 |

The model is therefore not merely "using a useful feature": it has reorganized around A4 and fails without it. This is strong causal evidence for the descriptor's role, and simultaneously a robustness warning — the representation is brittle.

**CKA (Table 8, p. 14).** Mean cross-encoder CKA rises from 0.435 (D0) to 0.794 (descriptor models), about +82%. The paper interprets this as convergence of internal representations.

**Robustness (Tests 04/08/09, pp. 10–16).** High-frequency octave bands (750–12,000 Hz) carry most of the discriminative signal. Velocity scaling and octave transposition cause catastrophic drops (S < 18%); no augmentation was used in training. This makes the reported 84% a clean-condition number, not a deployment-ready result.

**Parameter controls.** Real descriptor content beats parameter-matched zero/random/shuffled controls (83.0 vs 75.0/73.6/73.6), which rules out a pure capacity explanation.

## 5. Limitations and Future Work

- **Single dataset, single instrument.** MAESTRO piano only; no multi-instrument, no cross-dataset transfer, no real-world recordings beyond MAESTRO's capture conditions.
- **Small training set.** 13,000 four-second segments; the audio encoder is partially pretrained, confounding architecture and pretraining effects.
- **Brittleness.** No augmentation; velocity and octave changes break retrieval. The descriptor solution may be overfit to MAESTRO's spectral profile.
- **A4 is a hand-crafted spectral-flux feature.** It is effective but not learnable or semantically labelled; the paper does not show that it generalises to other timbres or that it captures harmony rather than recording/room characteristics.
- **D4's role is unresolved.** The "training regularizer" explanation is a hypothesis, not a measured mechanism.
- **Review status.** A single-author preprint under review with AI-assisted analysis; the results have not been independently replicated.

## 6. Related Work

- Classical audio–MIDI alignment: chromagrams + DTW, audio fingerprinting, score-informed separation.
- Self-supervised audio: wav2vec 2.0, MERT; audio–text: CLAP, MuLan.
- Cross-modal contrastive learning: CLIP, VICReg, Barlow Twins.
- Conditioning: FiLM, mixture-of-experts, cross-attention, Perceiver.
- Representation comparison: CKA, RSA, linear probing.
- CLaMP 3 is the closest large-scale cross-modal retrieval system; this paper is the opposite scale and isolates the alignment mechanism.

## 7. Glossary

- **MIDI:** Musical Instrument Digital Interface.
- **CKA:** Centered Kernel Alignment.
- **RSA:** Representational Similarity Analysis.
- **VICReg:** Variance–Invariance–Covariance Regularization.
- **STFT:** Short-Time Fourier Transform.
- **A4 / D4:** the audio octave-band / MIDI interval descriptors.
- **R@10:** Recall at 10.
- **FiLM:** Feature-wise Linear Modulation.
- **MoE:** Mixture of Experts.
