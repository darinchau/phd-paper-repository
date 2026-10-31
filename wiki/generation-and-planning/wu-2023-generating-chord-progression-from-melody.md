---
title: "Generating Chord Progression from Melody with Flexible Harmonic Rhythm and Controllable Harmonic Density"
authors: Shangda Wu, Yue Yang, Zhaowen Wang, Xiaobing Li, Maosong Sun
year: 2023
doi: 10.48550/arXiv.2112.11122
category: generation-and-planning
source: wu-2023-generating-chord-progression-from-melody.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/wu-2023-generating-chord-progression-from-melody.pdf"
pdf_filename: wu-2023-generating-chord-progression-from-melody.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-31
tags:
  - melody-harmonization
  - harmonic-rhythm
  - controllable-generation
  - gamma-sampling
  - music-theory-metrics
---
## Summary

AutoHarmonizer generates a chord progression for a given melody one sixteenth-note at a time, using explicit beat-strength and key-signature inputs and a 1,462-symbol chord vocabulary. Because prediction is frame-level rather than bar-level, chord changes need not fall on bar lines, and a single gamma parameter lets a user ask for more or fewer chord changes at inference time. Frame-level accuracy is around 31%, but the density control is monotone and clear, and a discrimination study found the output harder to tell from human progressions than two earlier systems.

## Key Contributions

- **Frame-level harmonisation.** Sixteenth-note chord prediction makes flexible harmonic rhythm representable, which bar-level and half-bar-level systems cannot express.
- **Explicit metrical context.** A beat-strength vector and a fifteen-value key encoding handle arbitrary time and key signatures, avoiding the 4/4/C-major restriction of earlier transformer baselines.
- **Gamma sampling for density.** Rescaling the probability of the previously generated chord changes how often the chord changes, with no retraining; Γ above 0.5 gives denser harmony, below 0.5 sparser.
- **A harmonic-rhythm metric suite.** Coverage, entropy, tonal distance and three new rhythmic metrics make “plausible harmonic rhythm” measurable rather than only chord labels.

## Methodology and Architecture

Each frame carries a 128-dimensional melody one-hot, a 4-dimensional beat-strength vector, a 15-value key code and a 1,462-dimensional chord one-hot. Two Bi-LSTM encoders (melody; beat and key) feed a three-layer Bi-LSTM decoder that emits chords autoregressively. Training uses Wikifonia lead sheets reduced to 5,204 tunes with a 90/10 split. Control comes from gamma sampling on the previous chord token. Evaluation combines frame accuracy with seven chord/harmonicity metrics and three harmonic-rhythm metrics, plus a human-versus-machine discrimination study with 83 participants.

The complete evidence-grounded digest, with page anchors, the corrected gamma direction and the full Table 1, is in [`sources/wu-2023-generating-chord-progression-from-melody.md`](../../sources/wu-2023-generating-chord-progression-from-melody.md).

## Results

Raising Γ from 0.5 to 0.9 increases chord coverage from 5.09 to 8.64 and chord-histogram entropy from 1.35 to 1.76 while chord tonal distance falls from 1.19 toward the ground-truth 1.07, so the control moves density in the intended direction [PDF p. 6, Table 1]. Frame accuracy is 0.309–0.314 in the middle of that range and 0.289 at Γ = 0.9, against 0.282 for the Bi-LSTM baseline and under 0.10 for the two transformer baselines that can only place two chords per bar [PDF p. 6, Table 1]. Generated progressions are more consonant than real music, with a higher chord-tone-to-non-chord-tone ratio and lower melody–chord distance [PDF pp. 6–8]. In the listening study the system was mistaken for human more often than the older baselines in every condition, the sparsest setting was rated most human-like, and half the participants also judged genuine human progressions to be machine-made [PDF p. 9].

## Related Papers

- [[concepts/music-domain-inductive-biases]] — key, beat and a fixed chord vocabulary are supplied as explicit structure rather than learned, the design choice this page illustrates.
- [[concepts/auditable-creative-editing-pipelines]] — Γ is an interpretable control, but the model does not expose which melody notes justified a chord, which is the auditability gap.
- [[theory-and-constraints/mcleod-2020-a-modular-system-for]] — modular harmonic analysis, the theory-side counterpart to the explicit chord vocabulary used here.
- [[theory-and-constraints/ebrahimzadeh-2026-emergent-tonal-structure-in-learned]] — what tonal structure emerges in learned representations, the question this model sidesteps by fixing the vocabulary.
- [[overviews/2026-symbolic-music-literature-map]] — batch index for the October 2026 intake this reading belongs to.
