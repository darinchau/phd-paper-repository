---
title: "Look, Listen and Learn"
authors: Relja Arandjelović, Andrew Zisserman
year: 2017
doi: 10.48550/arXiv.1705.08168
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/arandjelovic-2017-look-listen-and-learn.pdf"
pdf_filename: arandjelovic-2017-look-listen-and-learn.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
---

## One-line Summary

Training vision and audio networks jointly to decide whether a video frame and an audio clip correspond yields strong features in both modalities from unlabeled video alone: the audio network beats SoundNet on sound classification, and the visual network matches self-supervised ImageNet baselines.

## 1. Document Information

- **Exact title:** *Look, Listen and Learn*. [PDF p. 1]
- **Authors:** Relja Arandjelović (DeepMind), Andrew Zisserman (VGG, University of Oxford). [PDF p. 1]
- **Source record:** arXiv `1705.08168v2` [cs.CV], 1 August 2017, 14 pages; ICCV 2017. [PDF p. 1]
- **Length and denominator:** 14/14 pages checked, including Tables 1–3, Figures 1–5, and the localisation results.
- **Extraction method:** `pdftotext -layout`; tables cross-checked against the text.
- **Canonical integrity:** SHA-256 recorded at ingest. Downloaded from `arxiv.org/pdf/1705.08168`.
- **Availability boundary:** no code release stated in the paper.

Author-reported claims are the default; repository interpretation is marked.

## 2. Key Contributions

1. **Audio–visual correspondence (AVC) as a self-supervised task.** Positives are a frame and a short audio clip from the same video at the same time; negatives come from different videos. [§1, §2]
2. **Both subnetworks trained from scratch**, unlike SoundNet's frozen visual teacher. [§1]
3. **Bidirectional benefit:** the audio features beat the prior visual-supervision baseline, and the visual features are competitive with self-supervised ImageNet methods. [§3.3, §3.4]
4. **Localisation:** the model localises sounding objects in frames and corresponding regions in the spectrogram. [§3.5]

## 3. Methodology and Architecture

- **Inputs:** a video frame and a one-second audio clip; each has its own convolutional subnetwork. [§2, Fig. 1]
- **Fusion:** the two embeddings are combined and classified as corresponding or not; the task forces semantic concepts in both modalities. [§2]
- **Training data:** unlabeled videos (Flickr-SoundNet collection). [§3]
- **Evaluation:** AVC accuracy, sound classification on ESC-50 and DCASE, and linear ImageNet classification from frozen visual features. [§3.3–3.4]

## 4. Key Results and Benchmarks

- **ESC-50:** 79.3% versus 74.2% for SoundNet and 81.3% human. [Table 2]
- **DCASE:** 93% versus 88% for SoundNet. [Table 2]
- **ImageNet top-1 (linear probe):** 32.3%, versus 12.9% for random features and 31.0–34.7% for comparable self-supervised methods. [Table 3]
- **AVC task:** the network solves the correspondence task; accuracy is reported per fold in Table 1. [Table 1]
- **Interpretation:** this is the clearest evidence that the benefit can run in *both* directions and that correspondence alone, without labels, is enough to shape both towers.

## 5. Limitations and Future Work

- **Natural video, not music.** Instruments appear, but there is no symbolic notation and no musical-structure evaluation.
- **Correspondence is a weak signal.** It requires only that *something* in the frame correlates with *something* in the audio; fine-grained musical attributes are not guaranteed.
- **Video availability.** The method needs paired audio-visual data; audio-only corpora cannot supply the signal.
- **No attribution** of which acoustic events drive a visual decision.

## 6. Related Work

- SoundNet (Aytar et al. 2016): vision-teacher → audio-student transfer.
- Modality hallucination (Hoffman et al. 2016) and modality distillation (Garcia et al. 2018): train-time-only cross-modal transfer.
- Multimodality Helps Unimodality (Lin et al. 2023): cross-modal examples improve unimodal classifiers.

## 7. Glossary

- **AVC:** Audio–Visual Correspondence.
- **DCASE:** Detection and Classification of Acoustic Scenes and Events.
- **ESC:** Environmental Sound Classification.
