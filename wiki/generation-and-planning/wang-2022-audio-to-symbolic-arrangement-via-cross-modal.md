---
title: "Audio-to-symbolic Arrangement via Cross-modal Music Representation Learning"
authors: Ziyu Wang, Dejing Xu, Gus Xia, Ying Shan
year: 2022
doi: 10.48550/arXiv.2112.15110
source: wang-2022-audio-to-symbolic-arrangement-via-cross-modal.md
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/wang-2022-audio-to-symbolic-arrangement-via-cross-modal.pdf"
pdf_filename: wang-2022-audio-to-symbolic-arrangement-via-cross-modal.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
tags: [audio-to-symbolic, arrangement, cross-modal, vae]
---

## Summary

Wang et al. generate a playable piano accompaniment score from a pop-song audio mix. Chord, audio-texture, and symbolic-texture encoders share a latent space; staged training gradually removes the symbolic crutch so that inference needs audio only. A 26-subject study rates the output above baselines on faithfulness, creativity, naturalness, and musicality, with creativity rated above human compositions. The task is arrangement, not transcription, and the evaluation is task-level rather than representational.

## Key Contributions

- The first end-to-end audio-to-symbolic arrangement model, distinct from note-for-note transcription. [§1]
- A disentangled cross-modal representation (chord, audio texture, symbolic texture). [§3]
- Staged training that shifts texture information from a corrupted score to audio. [§3]
- A human evaluation on four musical criteria. [§4.2]

## Methodology and Architecture

A chord extractor, a MAESTRO-pretrained piano transcriber, and GRU encoders for audio and symbolic texture feed a shared 192-dimensional texture space and a decoder. Training starts as a symbolic VAE, then corrupts the symbolic input with masks and noise, then fine-tunes with Gaussian noise or autoregressive past bars so the model depends on audio. The model has 62M trainable parameters.

## Results

- 26 subjects; significantly better than all baselines on faithfulness, creativity, naturalness, and overall musicality. [§4.2, Fig. 3]
- Creativity significantly better than human compositions (p < 0.005). [§4.2]
- Qualitative examples show chord, bass, and groove changes tracked in the arrangement. [Fig. 2]

The one-to-many nature of arrangement is acknowledged but not measured: the study does not test diversity or explain which audio evidence produced which notes.

## Related Papers

- [[overviews/audio-symbolic-transfer]] — audio-derived symbolic content and the attribution gap.
- [[overviews/cross-modal-supervision-transfer]] — audio as a source of arrangement-level information.
- [[generation-and-planning/zhao-2026-learning-music-style-for-piano]] — a later system that separates audio style from lead-sheet content.
