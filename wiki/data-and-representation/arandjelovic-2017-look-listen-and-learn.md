---
title: "Look, Listen and Learn"
authors: Relja Arandjelović, Andrew Zisserman
year: 2017
doi: 10.48550/arXiv.1705.08168
source: arandjelovic-2017-look-listen-and-learn.md
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/arandjelovic-2017-look-listen-and-learn.pdf"
pdf_filename: arandjelovic-2017-look-listen-and-learn.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
tags: [cross-modal, self-supervised, audio-visual, representation-learning]
---

## Summary

The paper introduces audio–visual correspondence as a self-supervised task: decide whether a video frame and a one-second audio clip come from the same moment. Training both subnetworks from scratch on unlabeled video produces strong features in both modalities — the audio network beats SoundNet on sound classification, and the visual network matches self-supervised ImageNet baselines — which makes this the clearest evidence that the benefit of a second modality can run in both directions.

## Key Contributions

- The AVC task and a two-tower architecture trained without labels. [§2]
- Audio features that set a new state of the art on ESC-50 and DCASE. [§3.3]
- Visual features competitive with self-supervised ImageNet methods. [§3.4]
- Localisation of sounding objects in frames and in the spectrogram. [§3.5]

## Methodology and Architecture

A vision subnetwork and an audio subnetwork embed a frame and a clip; fusion layers classify the pair as corresponding or not. Positives are timestamp-matched; negatives come from different videos. No semantic labels are used.

## Results

- ESC-50: 79.3% versus 74.2% for SoundNet; human 81.3%. [Table 2]
- DCASE: 93% versus 88% for SoundNet. [Table 2]
- ImageNet top-1 linear probe: 32.3% versus 12.9% random and 31.0–34.7% for comparable self-supervised methods. [Table 3]

The correspondence signal is weak — it only requires that something in the frame correlates with something in the audio — yet it is sufficient to shape both towers.

## Related Papers

- [[overviews/cross-modal-supervision-transfer]] — bidirectional cross-modal transfer and why correspondence works as supervision.
- [[data-and-representation/aytar-2016-soundnet-learning-sound-representations-from]] — the one-way teacher–student predecessor.
- [[other/lin-2023-multimodality-helps-unimodality-cross-modal]] — cross-modal examples improve unimodal classifiers.
