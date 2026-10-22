---
title: "A Foundation Model for Music Informatics"
authors: Minz Won, Yun-Ning Hung, Duc Le
year: 2024
doi: 10.1109/ICASSP48485.2024.10448314
source: won-2024-a-foundation-model-for-music.md
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/won-2024-a-foundation-model-for-music.pdf"
pdf_filename: won-2024-a-foundation-model-for-music.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
tags: [music-foundation-model, self-supervised, audio, best-rq]
---

## Summary

MusicFM is an audio-only self-supervised music foundation model built on BEST-RQ random tokenisation and a Conformer backbone (330M–660M parameters). Its controlled ablation shows that architecture, tokenisation, and training data matter more than temporal resolution in this setup, and the released model is competitive with MERT on several MIR tasks. It contains no symbolic modality; in this repository it serves as an audio-teacher candidate and an audio-only control.

## Key Contributions

- A systematic foundation-model ablation for music informatics (encoder, tokeniser, resolution, input length, data, size). [§2, Table 1]
- A released audio-only pretrained model. [§1]
- Practical findings: Conformer > BERT; random tokenisation generalises well; 25 Hz is sufficient in their setting. [§4]

## Methodology and Architecture

Masked token modelling over audio, with BEST-RQ random projection and codebook tokenisation, a Conformer encoder, 5 s or 30 s inputs, and 25–75 Hz token rates. Trained on in-house music data and FMA with eight A100-80GB GPUs for two weeks.

## Results

- Best variant: beat F1 0.868, downbeat 0.804, chord accuracy 0.714, structure 0.640, key 0.641, tagging mAP 0.482, ROC 0.920. [Table 1]
- Competitive with the reported state of the art (0.723 / 0.660 / 0.470 / 0.913 on the comparison rows) but not uniformly better. [Table 1]
- The best rows depend on in-house data that is not released, limiting exact reproduction.

## Related Papers

- [[overviews/cross-modal-supervision-transfer]] — audio-only encoders as teacher candidates and controls.
- [[overviews/audio-symbolic-transfer]] — the audio↔symbolic programme this model can serve.
- [[data-and-representation/bradshaw-2025-scaling-self-supervised-representation]] — a symbolic counterpart trained on transcribed piano.
