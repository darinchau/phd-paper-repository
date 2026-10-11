---
title: "Unified Cross-modal Translation of Score Images, Symbolic Music, and Performance Audio"
authors: "Jongmin Jung, Dongmin Kim, Sihun Lee, Seola Cho, Hyungjoon So, Irmak Bukey, Chris Donahue, and Dasaem Jeong"
year: 2025
doi: 10.48550/arXiv.2505.12863
category: data-and-representation
source: jung-2025-unified-cross-modal-translation-of.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/jung-2025-unified-cross-modal-translation-of.pdf"
pdf_filename: jung-2025-unified-cross-modal-translation-of.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

The paper unifies score images, symbolic notation, MIDI, and performance audio in token-level translation, showing that explicit symbolic intermediates improve note accuracy while introducing error propagation and remaining separate from provenance-preserving mashup or repair.

## Key Contributions

Core contribution

#### Authors’ claim

The paper proposes a unified token-level encoder–decoder Transformer for four modalities:

1. score images,
2. symbolic notation / MusicXML,
3. performance MIDI,
4. performance audio.

The claimed contributions are:

- a single multitask framework for cross-modal music translation;
- the first successful direct score-image-to-performance-audio system;
- the YouTube Score Video (YTSV) dataset;
- multitask improvements to OMR, AMT, MIDI-to-audio, image-to-audio, and audio-to-image tasks.

Anchors: **Abstract, pp. 1–2; Fig. 2, p. 2; Sections III–VIII, pp. 3–10.**

#### Important qualification

Despite the “unified” framing, the experiments train **two separate checkpoints**:

- Image-to-Audio direction (I2A)
- Audio-to-Image direction (A2I)

They do not share weights. The authors explicitly identify training one model for both directions as future work (**Conclusion, p. 10**).

---

### 3. Modalities and token design

#### Modality roles

The paper treats the modalities as a spectrum:

- **Score image:** scanned or rendered notation.
- **Symbolic notation:** Linearized MusicXML (LMX), including pitch, duration, voicing, articulation, slurs, tempo, and dynamics.
- **MIDI:** performance-oriented event representation with onset/offset timing, pitch, velocity, instruments, and timing markers.
- **Audio:** recorded or synthesized performance.

Anchors: **Section II, pp. 2–3; Fig. 3, p. 3.**

#### Image tokens

The authors train a modified **Residual Quantized VAE (RQVAE)**:

- 16× spatial compression;
- four unshared codebooks;
- 1,024 codes per c

The complete evidence-grounded digest is in [`sources/jung-2025-unified-cross-modal-translation-of.md`](../../sources/jung-2025-unified-cross-modal-translation-of.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
