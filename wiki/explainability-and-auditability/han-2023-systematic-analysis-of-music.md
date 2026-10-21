---
title: "Systematic Analysis of Music Representations from BERT"
authors: "Sangjun Han, Hyeongrae Ihm, and Woohyung Lim"
year: 2023
doi: 10.48550/arXiv.2306.04628
source: han-2023-systematic-analysis-of-music.md
category: explainability-and-auditability
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/han-2023-systematic-analysis-of-music.pdf"
pdf_filename: han-2023-systematic-analysis-of-music.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
tags: [probing, symbolic-bert, remi-plus, representation-analysis, contrastive-learning, layer-wise, lakh]
---

# Systematic Analysis of Music Representations from BERT

## Summary

This is a probing study, not a generator. Four BERT-base models are trained on 9.97M bar-level LMD segments in REMI+: plain MLM, MLM + pitch/velocity augmentation, MLM + same-piece neighbours, and MLM + dropout views. Seven linear probes measure chords, groove patterns, instruments, tempo, mean velocity, mean duration, and song clustering. The main finding is that musical information is decodable but objective- and layer-dependent: plain BERT wins chords and groove; augmentation wins instruments but destroys velocity; neighbour contrast wins tempo and song identity but overfits badly; dropout is the most balanced. Last-layer embeddings are often not the best readout. The paper is a useful template for a "what transfers" study because it separates representational content from downstream task performance.

## Key Contributions

- A seven-task probe suite for bar-level symbolic embeddings, with concrete label definitions.
- Three contrastive variants that isolate what each invariance does to musical information.
- Layer-wise evidence against the assumption that the final layer is the best representation.
- A clear demonstration that a single embedding cannot be evaluated as generically "good": the objective trades one attribute against another.

## Methodology and Architecture

LMD is converted to REMI+ (bar, tempo, instrument, pitch, drum, position, duration, velocity), giving 9,971,616 bars. BERT-base (12 layers, 768 hidden, 12 heads) is trained with MLM. Contrastive variants add NT-Xent (τ = 0.1): pitch ±6/velocity ±3 augmentation; another bar from the same piece; or two dropout views. Probes are Ridge classifiers/regressors and K-means on frozen embeddings. Chords use a Viterbi recogniser over 84 labels; groove is 16-step occupancy; tempo is 32 bins; song clustering uses entropy of cluster assignments within a file.

## Results

| Probe | Best model / layer | Score | Anchor |
|---|---|---|---:|
| Chords | BERT, layer 12 | 0.861 | Table 3, p. 4 |
| Groove | BERT, layer 5 | 0.863 | Table 3, p. 4 |
| Instruments | BERT, layer 4 | 0.882 | Table 3, p. 4 |
| Tempo | BERT-neighbor, layer 4 | 0.990 | Table 3, p. 4 |
| Mean velocity (error) | BERT, layer 2 | 4.905 | Table 3, p. 4 |
| Mean duration (error) | BERT-aug, layer 6 | 1.453 | Table 3, p. 4 |
| Song clustering (entropy) | BERT-neighbor, layer 6 | 0.062 | Table 3, p. 4 |

The objective trade-offs are the useful result: augmentation makes chords invariant but removes velocity; same-piece positives preserve song identity but their validation NT-Xent collapses to 0.059; dropout preserves the most attributes but still loses to task-specific layers. Probe scores are not causal: nothing here shows the model uses these features when generating or retrieving.

## Related Papers

- [[overviews/audio-symbolic-transfer]] — supplies the probe methodology for asking what a symbolic representation actually contains, including representations trained on audio-derived data.
- [[concepts/music-theory-probing]] — the broader probe-design and construct-validity questions.
- [[data-and-representation/bradshaw-2025-scaling-self-supervised-representation]] — uses linear probes at much larger scale and with audio-derived MIDI.
- [[data-and-representation/huang-2025-musetok-symbolic-music-tokenization-for]] — probes learned discrete codes rather than BERT states.
- [[generation-and-planning/guo-2025-moonbeam-a-midi-foundation-model]] — a different symbolic inductive bias (relative attention) with downstream probes.
