---
title: "A Modular System for Harmonic Structure Analysis of Music"
authors: Andrew McLeod and Martin Rohrmeier
year: 2020
doi: null
source: mcleod-2020-a-modular-system-for.md
category: theory-and-constraints
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/mcleod-2020-a-modular-system-for.pdf"
pdf_filename: mcleod-2020-a-modular-system-for.pdf
source_collection: DMRN+15 workshop proceedings
source_format: pdf
extracted_date: 2026-10-11
tags: [harmonic-analysis, modular-architecture, chord-recognition, key-analysis, symbolic-music]
---

## Summary

McLeod and Rohrmeier decompose harmonic structure analysis into six modules aligned with musical granularity: chord transitions, chord classification, chord sequences, key transitions, key sequences, and initial-chord prediction. The system exposes explicit chord and local-key interfaces and can in principle accept score, MIDI, or audio inputs, although the reported experiment uses only scores.

## Key Contributions

- A theory-rich vocabulary covers 1,540 chord forms and 70 major/minor keys.
- Separate modules make boundaries, labels, and higher-level dependencies inspectable and independently replaceable.
- A private multi-composer score evaluation reports partial accuracies from .26 to .47 and full chord/key accuracy of .15.
- The paper is useful as an early design pattern for structured harmonic analysis, but modularity is workflow transparency—not evidence that each predicted label has a faithful musical explanation.

## Methodology and Architecture

The CTM detects chord starts, the CCM labels each chord, and the chord sequence model predicts relative-chord continuation. The key transition and key sequence models then segment and label local key regions; the initial-chord model initializes the relative sequence. Most modules are simple single-layer LSTM/softmax predictors. This arrangement matches model interfaces to frames, chords, and keys, while allowing future MIDI/audio adaptation through retraining of lower-level components.

## Results

On private annotated scores including works from the Annotated Beethoven Corpus, the reported average per-piece proportions correct are: chord root+triad `.47`, chord with sevenths `.32`, chord with inversion `.26`, key tonic `.45`, key mode `.34`, and all attributes jointly `.15`. No uncertainty, component ablation, public implementation, or matched integrated baseline is reported.

## Related Papers

- [[concepts/music-domain-inductive-biases]] — places modular harmonic structure alongside representations, constraints, and faithful explanation.
- [[explainability-and-auditability/pocwiardowski-2026-mi-midi-mechanistic-interpretability-of]] — intervention-oriented symbolic interpretability.
- [[explainability-and-auditability/wei-2024-do-music-generation-models-encode]] — controlled probing of recoverable music-theory information.
