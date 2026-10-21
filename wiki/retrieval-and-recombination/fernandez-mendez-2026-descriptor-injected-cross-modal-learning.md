---
title: "Descriptor-Injected Cross-Modal Learning: A Systematic Exploration of Audio-MIDI Alignment via Spectral and Melodic Features"
authors: "Mariano Fernández Méndez"
year: 2026
doi: 10.48550/arXiv.2604.10283
source: fernandez-mendez-2026-descriptor-injected-cross-modal-learning.md
category: retrieval-and-recombination
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/fernandez-mendez-2026-descriptor-injected-cross-modal-learning.pdf"
pdf_filename: fernandez-mendez-2026-descriptor-injected-cross-modal-learning.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
tags: [audio-midi-alignment, cross-modal-retrieval, descriptors, vicreg, cka, maestro, piano, robustness]
---

# Descriptor-Injected Cross-Modal Learning: A Systematic Exploration of Audio-MIDI Alignment via Spectral and Melodic Features

## Summary

This is a small-scale, mechanistic study of the audio–MIDI modality gap. Using MAESTRO piano segments, a 74M-parameter dual encoder, and VICReg, the author injects an eight-band spectral-dynamics descriptor (A4) into the audio encoder and a local-interval descriptor (D4) into the MIDI encoder. Retrieval rises from 73.4% to 83.8% (single seed) and 84.0 ± 2.7% (five seeds). Causal ablation shows A4 is necessary at inference (zeroing it costs 75–78 points) while D4 mainly helps training. CKA rises from 0.435 to 0.794, supporting a representational-convergence explanation. The result is valuable as a lower bound on how much hand-crafted spectral information can bridge the gap, and as a warning: without augmentation, transposition and velocity changes destroy performance (S < 18%), so the alignment is brittle and piano-specific.

## Key Contributions

- A systematic 13-arm descriptor/mechanism screen plus architecture and schedule sweeps, with five-seed replication for the headline arm.
- Reverse cross-attention: descriptor frames as queries, 163× fewer attention operations than standard cross-attention, competitive accuracy.
- A clean causal dissociation: audio-side descriptor drives inference; MIDI-side descriptor acts as a training regularizer in the dual model.
- CKA evidence that the mechanism is cross-encoder convergence rather than concatenation.

## Methodology and Architecture

Audio branch: 4-layer CNN (40× downsample) + 4-layer transformer (d=1,024), partially MERT-initialised. MIDI branch: event embeddings + 4-layer transformer (d=512). Both project to 256-d; VICReg aligns matched pairs without negatives. A4 is 8 octave-band log-magnitude temporal deltas from an STFT (188 frames × 8 bands). D4 is four per-note interval features (±2-octave clamped and raw). Injection by concatenation, cross-attention, or reverse cross-attention. Data: 13,000 four-second MAESTRO windows; evaluation uses 256-item pools with same-piece and same-composer hard negatives. The score is `min(R@10 AM, R@10 MA)`.

## Results

| Arm | S (%) | Note | Anchor |
|---|---:|---|---|
| D0 baseline | 73.4 | seed 42 | Table 5, p. 9 |
| d4a4 | 83.8 | seed 42, epoch 50 | Table 4, p. 8 |
| d4a4 five seeds | 84.0 ± 2.7 | headline | §5.9 |
| a4r | 82.0 | A4 reverse cross-attention | Table 4, p. 8 |
| Zero A4 (d4a4) | −76.0 pp | collapse | Table 6, p. 9 |
| Zero D4 (d4a4) | +0.6 pp | no inference effect | Table 6, p. 9 |
| CKA D0 → descriptors | 0.435 → 0.794 | +82% | Table 8, p. 14 |
| Velocity/octave perturbation | S < 18% | no augmentation | §5.6 |

The paper's own limitations matter for reuse: one dataset, one instrument, small training set, partially pretrained audio encoder, no augmentation, and no cross-dataset test. The descriptor is also a spectral-flux summary that may encode recording/room characteristics as much as musical content; the paper does not separate these.

## Related Papers

- [[overviews/audio-symbolic-transfer]] — the descriptor route to closing the audio–symbolic gap, at the opposite scale from CLaMP 3.
- [[concepts/audio-symbolic-modality-gap]] — the bootstrapping problem this paper tries to solve with structured priors.
- [[retrieval-and-recombination/wu-2025-clamp-3-universal-music]] — large-scale text-bridged alignment; weak emergent audio–symbolic retrieval.
- [[retrieval-and-recombination/bang-2025-pianobind-a-multimodal-joint]] — piano-specific trimodal embedding with audio and MIDI encoders.
- [[data-and-representation/bradshaw-2025-scaling-self-supervised-representation]] — symbolic-only embeddings and probes on the same kind of piano material.
