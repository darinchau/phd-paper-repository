---
title: "Learning Music Style for Piano Arrangement Through Cross-Modal Bootstrapping"
authors: Jingwei Zhao, Gus Xia, Ziyu Wang, Ye Wang
year: 2026
doi: 10.48550/arXiv.2608.03050
source: zhao-2026-learning-music-style-for-piano.md
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/zhao-2026-learning-music-style-for-piano.pdf"
pdf_filename: zhao-2026-learning-music-style-for-piano.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
tags: [cross-modal, style-transfer, piano-arrangement, q-former]
---

## Summary

Zhao et al. use a Q-Former to bridge a frozen audio language model and a frozen symbolic language model: an audio example supplies implicit style (groove, dynamics, texture) and a lead sheet supplies content, producing a 16-bar piano arrangement. The model beats piano-cover baselines on style coherence and musicality and supports cross-modal style transfer and audio-to-MIDI retrieval. It is the closest positive evidence in this batch that audio supplies something a symbolic score lacks, although the symbolic backbone stays frozen and the bridge is external at inference.

## Key Contributions

- Cross-modal style bootstrapping with a Q-Former between two frozen LMs. [§1, Fig. 1]
- Two-stage training: contrastive audio–symbolic alignment, then generative arrangement. [§3]
- Content/style separation by construction: lead sheet for content, audio for style. [§1]
- Three evaluations: piano cover, style transfer, and audio-to-symbolic retrieval. [§4–5]

## Methodology and Architecture

The audio LM is frozen and the symbolic LM is frozen; only the Q-Former is trained. Stage 1 uses audio–symbolic contrastive, matching, and audio-grounded generation objectives. Stage 2 conditions the symbolic generator on the style token and the lead sheet. Outputs are 16-bar MIDI performances.

## Results

- POP909: leads on most objective metrics but has lower content preservation (MCA/CA) than PiCoGen2, attributed to lead-sheet extraction errors. [§4.3, Table 1]
- Out-of-distribution Ballroom/GTZAN: surpasses PiCoGen2 on MCA and CA. [§4.3]
- Style coherence: best GPC/VCC on POP909 and best tempo accuracy on both sets; the no-pretraining ablation is significantly worse on MCA, CA, and TA. [Table 2]
- Listening study: significantly better in coherence and musicality, comparable in naturalness. [§4.4]

The system conditions on an external audio embedding rather than internalising style into the symbolic model, and it does not attribute generated notes to specific audio evidence.

## Related Papers

- [[overviews/audio-symbolic-transfer]] — audio-derived style and the representation-versus-conditioning distinction.
- [[overviews/cross-modal-supervision-transfer]] — the general cross-modal transfer principle.
- [[generation-and-planning/wang-2022-audio-to-symbolic-arrangement-via-cross-modal]] — an earlier end-to-end audio-to-symbolic arrangement model.
