---
title: "SoundNet: Learning Sound Representations from Unlabeled Video"
authors: Yusuf Aytar, Carl Vondrick, Antonio Torralba
year: 2016
doi: 10.48550/arXiv.1610.09001
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/aytar-2016-soundnet-learning-sound-representations-from.pdf"
pdf_filename: aytar-2016-soundnet-learning-sound-representations-from.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
---

## One-line Summary

SoundNet distils object- and scene-recognition knowledge from frozen image networks into a raw-waveform sound network through two million unlabeled videos, producing an audio-only representation that beats prior sound-classification baselines.

## 1. Document Information

- **Exact title:** *SoundNet: Learning Sound Representations from Unlabeled Video*. [PDF p. 1]
- **Authors:** Yusuf Aytar, Carl Vondrick, Antonio Torralba (MIT); Aytar and Vondrick equal contribution. [PDF p. 1]
- **Source record:** arXiv `1610.09001v1` [cs.CV], 27 October 2016, 9 pages; NIPS 2016. [PDF p. 1]
- **Length and denominator:** 9/9 pages checked, including Tables 1–4 and Figures 1–3.
- **Extraction method:** `pdftotext -layout`; result tables cross-checked against the text.
- **Canonical integrity:** SHA-256 recorded at ingest. Downloaded from `arxiv.org/pdf/1610.09001`.
- **Availability boundary:** no code release stated in the paper.

Author-reported claims are the default; repository interpretation is marked.

## 2. Key Contributions

1. **Student–teacher transfer across modalities.** A student sound network learns from the soft outputs of ImageNet and Places CNNs applied to the corresponding video frames, using synchronisation as the bridge. [§2, Fig. 1]
2. **Audio-only inference.** The student takes raw waveform and has no visual input at test time. [§1]
3. **Scale from unlabeled video.** Two million training videos and 140,000 held-out videos are used without sound labels. [§3]
4. **Representation transfer.** The learned features are evaluated by training linear SVMs on small labelled sound datasets. [§3]

## 3. Methodology and Architecture

- **Teachers:** an ImageNet CNN (object distribution) and a Places CNN (scene distribution), both frozen. [§2]
- **Student:** a convolutional network on raw audio (8-layer and 5-layer variants), trained to match teacher distributions at two intermediate layers via KL divergence. [§2, Tables 1–2]
- **Data:** unlabeled videos with synchronised audio; frames at the same timestamps provide the teacher signal. [§3]
- **Evaluation:** DCASE acoustic scene classification, ESC-50 and ESC-10; features from a chosen layer feed an SVM. [§3]

## 4. Key Results and Benchmarks

- **DCASE:** 88% accuracy, versus 78% for a prior ensemble and 69–77% for individual baselines. [Table 3]
- **ESC-50:** 74.2%, versus 64.5% for the prior convolutional baseline and 81.3% human performance. [Table 4]
- **ESC-10:** 92.2%, versus 81.0% prior and 95.7% human. [Table 4]
- **Deeper is better:** the 8-layer student outperforms the 5-layer variant, and the authors attribute this to the amount of unlabeled data. [§3]
- **Interpretation:** the paper is the cleanest early demonstration that a second modality can teach a representation that stands alone at inference; the transfer is one-way (vision → audio) and the teacher defines the semantic label space.

## 5. Limitations and Future Work

- **Natural sounds, not music.** Scenes and objects are the target; no musical structure, notes, or instruments.
- **Teacher ceiling.** The student can only learn distinctions the image teachers already encode; visually silent or ambiguous sounds are invisible.
- **One-way distillation.** Audio does not teach vision here.
- **No symbolic modality** and no note-level explanation.

## 6. Related Work

- Look, Listen and Learn (Arandjelović & Zisserman 2017): learns both modalities jointly from audio-visual correspondence.
- Modality hallucination and modality distillation: later train-time-only cross-modal transfer methods.
- MERT, MusicFM: audio-only music encoders in this repository.

## 7. Glossary

- **CNN:** Convolutional Neural Network.
- **DCASE:** Detection and Classification of Acoustic Scenes and Events.
- **ESC:** Environmental Sound Classification.
- **KL:** Kullback–Leibler divergence.
- **SVM:** Support Vector Machine.
