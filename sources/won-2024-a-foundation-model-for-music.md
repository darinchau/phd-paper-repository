---
title: "A Foundation Model for Music Informatics"
authors: Minz Won, Yun-Ning Hung, Duc Le
year: 2024
doi: 10.1109/ICASSP48485.2024.10448314
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/won-2024-a-foundation-model-for-music.pdf"
pdf_filename: won-2024-a-foundation-model-for-music.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
---

## One-line Summary

MusicFM is an audio-only self-supervised music foundation model (BEST-RQ random tokenisation, Conformer backbone, 330M–660M parameters) whose ablation study shows that architecture, tokenisation, and training data matter more than temporal resolution, and which is a strong teacher candidate for audio-side supervision.

## 1. Document Information

- **Exact title:** *A Foundation Model for Music Informatics*. [PDF p. 1]
- **Authors:** Minz Won, Yun-Ning Hung, Duc Le (SAMI, ByteDance). [PDF p. 1]
- **Source record:** arXiv `2311.03318v1` [cs.SD], 6 November 2023; ICASSP 2024 (DOI `10.1109/ICASSP48485.2024.10448314`). [PDF p. 1; OpenAlex record]
- **Length and denominator:** 5/5 pages checked, including Table 1 and the results discussion.
- **Extraction method:** `pdftotext -layout`; Table 1 columns are wide and partially reflowed, so only clearly attributed cells are quoted.
- **Canonical integrity:** SHA-256 recorded at ingest. Downloaded from `arxiv.org/pdf/2311.03318`.
- **Availability boundary:** pretrained model at `https://github.com/minzwon/musicfm` (stated in the paper).

Author-reported claims are the default; repository interpretation is marked.

## 2. Key Contributions

1. **A controlled foundation-model study for music informatics**, varying encoder (BERT vs Conformer), tokenisation (k-means vs random projection), temporal resolution (25/50/75 Hz), input length (5 s vs 30 s), data (in-house vs FMA), and size (330M vs 660M). [§2, Table 1]
2. **A released audio-only pretrained model** (MusicFM) that is competitive with or better than MERT on several MIR tasks. [§1, Table 1]
3. **Practical findings:** random tokenisation generalises well to music; Conformer beats BERT; 25 Hz is sufficient in their setup; data source matters. [§4]

## 3. Methodology and Architecture

- **Objective:** masked token modelling (BERT-style) over discrete audio tokens. [§2.1]
- **Tokenisation:** BEST-RQ random projection + random codebook, avoiding a separately trained k-means/RVQ tokeniser. [§2.2]
- **Backbone:** Conformer, 330M parameters (660M in one variant), 25–75 Hz token rates, 5 s or 30 s inputs. [Table 1]
- **Training data:** in-house music corpus and FMA; eight A100-80GB GPUs for two weeks. [§3]
- **Downstream tasks:** beat/downbeat, chord, structure, key, and tagging, evaluated with mir_eval and standard retrieval metrics. [§3]

## 4. Key Results and Benchmarks

- **Best reported variant (FM7/FM8 family):** beat F1 0.868, downbeat F1 0.804, chord accuracy 0.714, structure 0.640, key 0.641, tagging mAP 0.482, ROC 0.920. [Table 1]
- **Against reported state of the art:** the table lists 0.723 / 0.660 / 0.470 / 0.913 for comparison rows, so MusicFM is competitive but not uniformly better; the authors claim improvements in specific metrics. [Table 1]
- **Ablations:** Conformer > BERT; random tokenisation is competitive with k-means; 25 Hz is slightly better than 50/75 Hz at lower compute; in-house data > FMA in their setting. [§4]
- **Interpretation:** this is an audio-only model; it does not use symbolic data. Its relevance here is as a frozen audio teacher or audio-only control for tests of whether symbolic models gain from audio supervision.

## 5. Limitations and Future Work

- **Audio only.** No symbolic modality, no cross-modal alignment, no note-level output.
- **In-house training data** dominates the best rows and is not released, limiting exact reproduction.
- **Task coverage** is MIR classification/regression; no generation, no perceptual blend or orchestration target.
- **Table extraction is imperfect**; some cells are ambiguous in the PDF layout, and the digest quotes only unambiguous values.

## 6. Related Work

- MERT: the main audio SSL baseline and the model MusicFM compares against. [§1, Table 1]
- CLMR, MULE, Jukebox: earlier music representation models. [§1]
- CLaMP 3, MERT, and MuQ: audio/multimodal encoders used elsewhere in this repository.

## 7. Glossary

- **BEST-RQ:** BERT-based Speech pre-Training with Random projection quantiser.
- **FMA:** Free Music Archive.
- **mAP:** mean Average Precision.
- **MERT:** Music Understanding Model with Large-Scale Self-Supervised Training.
- **MIR:** Music Information Retrieval.
- **ROC:** Receiver Operating Characteristic.
- **SSL:** Self-Supervised Learning.
