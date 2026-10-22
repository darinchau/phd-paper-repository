---
title: "Learning Music Style for Piano Arrangement Through Cross-Modal Bootstrapping"
authors: Jingwei Zhao, Gus Xia, Ziyu Wang, Ye Wang
year: 2026
doi: 10.48550/arXiv.2608.03050
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/zhao-2026-learning-music-style-for-piano.pdf"
pdf_filename: zhao-2026-learning-music-style-for-piano.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
---

## One-line Summary

Zhao et al. bridge a frozen audio language model and a frozen symbolic language model with a Q-Former, so that an audio example supplies implicit style (groove, dynamics, texture) while a lead sheet supplies content, producing piano arrangements whose style coherence and musicality beat piano-cover baselines.

## 1. Document Information

- **Exact title:** *Learning Music Style for Piano Arrangement Through Cross-Modal Bootstrapping*. [PDF p. 1]
- **Authors:** Jingwei Zhao (Songscription / NUS), Gus Xia (MBZUAI), Ziyu Wang (MBZUAI / NYU), Ye Wang (NUS). [PDF p. 1]
- **Source record:** arXiv `2608.03050v1` [cs.SD], 4 August 2026, 13 pages; accepted at ISMIR 2026 (proceedings notice on p. 1). DOI recorded as the arXiv resolver.
- **Length and denominator:** 13/13 pages checked, including the main text, Tables 1–2, Figures 1–3, and the appendix material sampled for metrics definitions.
- **Extraction method:** `pdftotext -layout`; table values cross-checked against the text.
- **Canonical integrity:** SHA-256 recorded at ingest. Downloaded from `arxiv.org/pdf/2608.03050`.
- **Availability boundary:** demo page `https://zhaojw1998.github.io/bossa/`; code/checkpoint release not stated in the PDF.

Author-reported claims are the default; repository interpretation is marked.

## 2. Key Contributions

1. **Cross-modal style bootstrapping.** A lightweight Q-Former extracts a style representation from a frozen audio LM and conditions a frozen symbolic LM, without retraining either backbone. [§1, Fig. 1]
2. **Two-stage training.** Stage 1 uses audio–symbolic contrastive, matching, and audio-grounded generation objectives; stage 2 trains the symbolic generator conditioned on the style token and lead sheet. [§3]
3. **Content/style separation by design.** The lead sheet supplies melody and chords; the audio reference supplies groove, dynamics, and texture. [§1]
4. **Three evaluations:** piano-cover generation, cross-modal style transfer, and audio-to-MIDI retrieval. [§4, §5]

## 3. Methodology and Architecture

- **Backbones:** a large pretrained audio LM (frozen) and a symbolic LM (frozen); the Q-Former is the only trained bridge. [§3.1]
- **Q-Former objectives:** audio–symbolic contrastive learning, audio–symbolic matching, and audio-grounded symbolic generation, each with tailored attention masks. [§3.2]
- **Training:** two stages; stage 1 aligns auditory style with symbolic expression, stage 2 trains arrangement generation. [§1, §3]
- **Inputs at inference:** a lead-sheet MIDI (content) and a reference audio clip (style); output is a 16-bar piano MIDI performance. [§4]

## 4. Key Results and Benchmarks

- **Piano-cover generation (POP909):** the model leads on most objective metrics but has lower content preservation (MCA and CA) than PiCoGen2, attributed to errors in Sheetsage-extracted lead sheets. [§4.3, Table 1]
- **Out-of-distribution (Ballroom/GTZAN):** the model surpasses PiCoGen2 on MCA and CA, suggesting better generalisation across genres and instrumentation. [§4.3]
- **Style coherence:** best GPC and VCC on POP909 and best tempo accuracy on both test sets; the no-pretraining ablation is significantly worse on MCA, CA, and TA. [§4.3, Table 2]
- **Subjective:** double-blind listening over 6 pieces and 450/1000 sample sets; significantly better than all baselines in coherence and musicality, comparable to PCG2 in naturalness. [§4.4, Fig. 3]
- **Audio-to-symbolic retrieval:** the cross-modal representation supports retrieving symbolic material from audio; reported as a further validation of the shared style space. [§5.2]
- **Interpretation:** this is direct evidence that an audio-derived representation can supply something a lead sheet lacks — style/feel — and improve symbolic generation, which is the closest positive analogue of the AGT premise in the batch.

## 5. Limitations and Future Work

- **Piano covers only**, 16-bar outputs; style is demonstrated on groove/dynamics, not on instrumentation or multi-instrument blend.
- **Style reference is required at inference**, so the system does not internalise style into the symbolic model; it conditions on an external audio embedding.
- **Lead-sheet bottleneck.** Content errors from Sheetsage propagate; content preservation is below the strongest baseline on POP909.
- **Evaluation mostly objective**, with a modest listening study; no note-level attribution of which generated notes carry the audio style.
- **No test of whether the symbolic backbone itself has learned style** after training (the backbone stays frozen).

## 6. Related Work

- BLIP-2: the Q-Former bridge that inspires the architecture. [§1]
- PiCoGen2 and other piano-cover generation systems: the main baselines. [§4.2]
- Audio-to-symbolic arrangement (Wang et al. 2022): an earlier end-to-end audio-to-MIDI arrangement model.
- MIDI-REPA (Yu et al. 2026): aligns audio-generation layers to symbolic targets, the reverse direction.

## 7. Glossary

- **CA:** Chord Accuracy.
- **GPC:** Grooving Pattern Coherence.
- **LM:** Language Model.
- **MCA:** Melody-Chord Alignment (content-preservation metric used by the paper).
- **MIDI:** Musical Instrument Digital Interface.
- **Q-Former:** Querying Transformer.
- **TA:** Tempo Accuracy.
- **VCC:** Velocity Contour Coherence.
