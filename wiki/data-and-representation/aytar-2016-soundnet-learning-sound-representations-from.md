---
title: "SoundNet: Learning Sound Representations from Unlabeled Video"
authors: Yusuf Aytar, Carl Vondrick, Antonio Torralba
year: 2016
doi: 10.48550/arXiv.1610.09001
source: aytar-2016-soundnet-learning-sound-representations-from.md
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/aytar-2016-soundnet-learning-sound-representations-from.pdf"
pdf_filename: aytar-2016-soundnet-learning-sound-representations-from.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
tags: [cross-modal, distillation, audio-representation, unlabeled-video]
---

## Summary

SoundNet trains a raw-waveform sound network with supervision transferred from frozen ImageNet and Places CNNs applied to synchronised video frames. Two million unlabeled videos supply the bridge, and the resulting audio-only features beat prior hand-crafted and convolutional baselines on acoustic scene and environmental sound classification. The paper is the canonical demonstration that a second modality can teach a representation that stands alone at inference, but the transfer is one-way (vision → audio) and confined to natural sounds.

## Key Contributions

- Student–teacher distillation across modalities: KL matching to object and scene distributions at two hidden layers. [§2]
- Audio-only inference from raw waveform, with no visual input at test time. [§1]
- A large unlabeled-video training set (2M training, 140k validation videos). [§3]
- Linear-probe evaluation on DCASE, ESC-50, and ESC-10. [§3–4]

## Methodology and Architecture

An 8-layer (or 5-layer) convolutional student consumes raw audio and is trained to match the soft output distributions of frozen image teachers on the corresponding frames. The representation is then frozen and probed with an SVM on small labelled sound datasets.

## Results

- DCASE: 88% versus 78% for the prior ensemble. [Table 3]
- ESC-50: 74.2% versus 64.5% prior; human 81.3%. [Table 4]
- ESC-10: 92.2% versus 81.0% prior; human 95.7%. [Table 4]
- Deeper students benefit more from the unlabeled data. [§3]

The gains are large but bounded by the teachers' semantic space: the student learns what the image networks can already see.

## Related Papers

- [[overviews/cross-modal-supervision-transfer]] — the general principle and the conditions under which cross-modal transfer works.
- [[data-and-representation/arandjelovic-2017-look-listen-and-learn]] — learns both towers jointly instead of using a frozen teacher.
- [[other/garcia-2018-modality-distillation-with-multiple-stream]] — the train-time-only distillation template.
