---
title: "Systematic Analysis of Music Representations from BERT"
authors: "Sangjun Han, Hyeongrae Ihm, and Woohyung Lim"
year: 2023
doi: 10.48550/arXiv.2306.04628
category: explainability-and-auditability
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/han-2023-systematic-analysis-of-music.pdf"
pdf_filename: han-2023-systematic-analysis-of-music.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
---

# Systematic Analysis of Music Representations from BERT

## One-line Summary

Probing four BERT variants trained on 9.97M bar-level LMD segments with seven music-theoretic tasks shows that bar embeddings encode chords, groove patterns, instruments, tempo, velocity, duration, and song identity, but which information is linearly recoverable depends strongly on the contrastive objective and on the chosen layer — the last layer is often not the best.

## 1. Document Information

- **Authors and affiliation:** Sangjun Han, Hyeongrae Ihm, and Woohyung Lim; LG AI Research.
- **Version and venue:** arXiv 2306.04628v1, 6 June 2023; 7 PDF pages (content pp. 1–4, references pp. 5–7). Marked "Preprint. Under review"; no venue acceptance is recorded in the PDF.
- **Extraction:** full text via `pdftotext -layout`; Figure 1 (training variants), Tables 1–3, and Figures 2 (layer-wise probes) inspected.
- **Artifacts:** code at `https://github.com/sjhan91/MusicBERT`.
- **Anchors:** data and model §2 pp. 2–3; probe definitions §2 p. 3; last-layer results Table 2 p. 4; best-layer results Table 3 p. 4; discussion §4 p. 4.

## 2. Key Contributions

1. **A direct representation audit** rather than a downstream leaderboard: seven probes measure what musical information is linearly decodable from bar-level BERT embeddings.
2. **Three contrastive variants** trained jointly with masked language modelling: pitch/velocity augmentation (BERT-aug), same-piece neighbours (BERT-neighbor), and dropout (BERT-dropout), compared with plain BERT.
3. **Layer-wise analysis** showing that musical attributes are distributed across depth and that the optimal layer differs by attribute and objective.
4. **A reusable probe suite**: chords (84 classes, multi-label), groove patterns (16-step occupancy), instruments (multi-label), tempo (32 bins), mean velocity (regression), mean duration (regression), and song clustering (K-means entropy).

## 3. Methodology and Architecture

- **Data.** Lakh MIDI Dataset (LMD), 176,581 files, converted to REMI+ (556 events: bar, tempo, instrument, pitch, drum pitch, position, duration, velocity); 9,971,616 bars total. Bars are the unit; each bar is tokenized and fed to BERT.
- **Model.** BERT-base: 12 layers, 768 hidden, 12 heads. Masked language modelling with 15% token selection (80/10/10 mask/random/keep), no next-sentence prediction. The three contrastive variants add NT-Xent (temperature 0.1) to the MLM loss: BERT-aug uses random pitch shift ±6 semitones and velocity shift ±3; BERT-neighbor uses another bar from the same piece as the positive; BERT-dropout uses two dropout views of the same masked input.
- **Probes.** Ridge classifiers/regressors and K-means on frozen embeddings; each probe is trained and evaluated on held-out data. Chord labels come from an adapted Viterbi chord recogniser (12 roots × 7 qualities). Groove pattern is a 16-position binary occupancy vector. Song clustering measures whether bars from the same file fall into the same cluster (lower entropy is better).
- **Training diagnostics.** Table 1 reports MLM accuracy around 0.87–0.90 for all models; NT-Xent training accuracy is 1.000, but validation accuracy is 0.918 (aug), 0.059 (neighbor), and 1.000 (dropout). The neighbor objective clearly overfits, which the authors flag.

## 4. Key Results and Benchmarks

**Last-layer probes (Table 2, p. 4).** Plain BERT is best for chords (0.861) and competitive for groove (0.808) and instruments (0.764); BERT-aug is best for instruments (0.855) but worst for mean velocity (13.093 error), consistent with velocity being augmented away; BERT-neighbor is best for tempo (0.946) and song clustering (0.072 entropy); BERT-dropout is best for mean velocity (7.107) and mean duration (2.371).

**Best-layer probes (Table 3, p. 4).** Performance is not monotone in depth. Examples: BERT's best groove probe is layer 5 (0.863) versus 0.808 at layer 12; instruments peak at layer 4 (0.882); tempo peaks at layer 1 (0.933); mean velocity peaks at layer 2 (4.905 error); song clustering peaks at layer 3 (0.169). For BERT-neighbor, tempo peaks at layer 4 (0.990) and song clustering at layer 6 (0.062).

**Interpretation.** The contrastive objective determines which nuisance variation is factored out. Augmenting pitch teaches chord invariance but destroys absolute-velocity information; same-piece neighbours preserve song identity but overfit; dropout preserves the most attribute information overall but still loses to task-specific layers. This is direct evidence that "a music embedding" is not a single object: its content depends on the training signal and the readout depth.

**What is not established.** Linear decodability is not causal use, and none of the probes tests musical structure beyond bar-local statistics. There is no generation, no listening test, no cross-dataset transfer, and no test of whether the embeddings support similarity or retrieval.

## 5. Limitations and Future Work

- **LMD is noisy and heterogeneous.** Web-scraped MIDI with inconsistent quantization, instrumentation, and file quality; REMI+ conversion adds its own quantization.
- **Bar-level only.** The unit is one bar, so phrase, section, and long-range structure are outside the probe set.
- **Probes are correlational.** A feature being decodable does not mean the model uses it for any task, and probe capacity/shrinkage are not swept.
- **Single corpus and model family.** No comparison with MidiBERT-Piano, MusicBERT, or audio models; no multilingual or multi-instrument transfer.
- **Contrastive variants are exploratory.** BERT-neighbor's validation collapse limits what can be concluded from its wins; the paper reports it rather than fixing it.
- **No released checkpoints** are stated, so exact reproduction depends on retraining.

## 6. Related Work

- BERT, SimCLR, SimCSE, NNCLR: the language and contrastive-learning templates.
- MusicBERT, MidiBERT-Piano, MuseBERT: symbolic BERT variants validated mainly by fine-tuning performance.
- REMI and REMI+: the bar-level event representation.
- Probing literature in NLP (Jawahar et al.; de Vries et al.) and the layer-analysis methodology borrowed from it.
- Figaro's REMI+ configuration and the chord-recognition pipeline used for labels.

## 7. Glossary

- **BERT:** Bidirectional Encoder Representations from Transformers.
- **MLM:** Masked Language Modelling.
- **NT-Xent:** Normalized Temperature-scaled Cross-Entropy loss.
- **REMI / REMI+:** Revamped MIDI / multi-track extension.
- **LMD:** Lakh MIDI Dataset.
- **Probe:** a frozen-representation classifier/regressor used to test decodability.
- **K-means entropy:** cluster-purity measure for bars from the same song.
