---
title: "Modality Distillation with Multiple Stream Networks for Action Recognition"
authors: Nuno C. Garcia, Pietro Morerio, Vittorio Murino
year: 2018
doi: 10.48550/arXiv.1806.07110
category: other
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/garcia-2018-modality-distillation-with-multiple-stream.pdf"
pdf_filename: garcia-2018-modality-distillation-with-multiple-stream.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
---

## One-line Summary

Garcia et al. train an RGB-only action-recognition model with depth as privileged information at training time: a hallucination network distils depth features into the RGB stream through multiplicative connections, and the RGB-only model at test time beats models trained on RGB alone.

## 1. Document Information

- **Exact title:** *Modality Distillation with Multiple Stream Networks for Action Recognition*. [PDF p. 1]
- **Authors:** Nuno C. Garcia (IIT / University of Genoa), Pietro Morerio (IIT), Vittorio Murino (IIT / University of Verona). [PDF p. 1]
- **Source record:** arXiv `1806.07110v2` [cs.CV], 29 October 2018, 19 pages; ECCV 2018 (DOI `10.1007/978-3-030-01237-3_7`). [PDF p. 1; OpenAlex record]
- **Length and denominator:** 19/19 pages checked, including the method, Table 2, Table 3, and the supplementary inversion study.
- **Extraction method:** `pdftotext -layout`; the main accuracy table is wide and partially reflowed, so only clearly attributed comparisons are quoted.
- **Canonical integrity:** SHA-256 recorded at ingest. Downloaded from `arxiv.org/pdf/1806.07110`.
- **Category note:** filed under `other` because it is a general cross-modal distillation method, not a music-domain contribution.

Author-reported claims are the default; repository interpretation is marked.

## 2. Key Contributions

1. **Generalised distillation for missing modalities:** train with RGB and depth, deploy with RGB only. [§1]
2. **Hallucination network** that imitates depth features from RGB, connected multiplicatively to the RGB stream rather than only regressing features. [§3]
3. **Combined loss:** soft labels from the depth teacher, hard action labels, and feature-map distance. [§3]
4. **State-of-the-art NTU RGB+D results** for the RGB-only setting, plus a study of robustness when depth is noisy at training time. [§4, Table 3]

## 3. Methodology and Architecture

- **Streams:** an RGB network, a depth network (teacher), and a hallucination network that takes RGB and predicts depth-like features. [§3, Fig. 1]
- **Distillation signals:** soft class probabilities from the depth stream, hard labels, and Euclidean distance between hallucination and depth feature maps. [§3]
- **Multiplicative connections** align the hallucination and RGB feature maps, making the transferred features usable by the classifier rather than merely correlated. [§3]
- **Inference:** RGB only; the depth stream and hallucination loss are training-time constructs. [§1]

## 4. Key Results and Benchmarks

- **NTU RGB+D:** the method reports state-of-the-art RGB-only action classification; the paper's main table compares RGB-only, RGB+depth, and distillation variants. [Table 2]
- **Noisy depth:** Table 3 tests clean RGB with noisy depth at training time and reports how performance degrades, showing the transfer is not brittle to moderate depth noise. [Table 3]
- **Interpretation:** this is the closest methodological template for AGT 3: a privileged modality improves a single-modality model at inference. The difference is that depth is spatially aligned with RGB; rendered audio is a deterministic function of MIDI, so the information gain must come from acoustics the MIDI does not encode.

## 5. Limitations and Future Work

- **Action recognition only**, with RGB and depth; no music or symbolic sequences.
- **Requires paired multimodal training data.**
- **One-way transfer:** depth does not benefit from RGB here.
- **No note-level or region-level attribution** of the distilled knowledge.

## 6. Related Work

- Learning with Side Information through Modality Hallucination (Hoffman et al. 2016): the earlier RGB-D hallucination model.
- SoundNet (Aytar et al. 2016): teacher–student transfer across vision and audio.
- Greedy multimodal learning (Wu et al. 2022): why the student may ignore the privileged signal.

## 7. Glossary

- **NTU RGB+D:** a large multimodal action-recognition dataset.
- **Privileged information:** a modality available at training but not at test time.
