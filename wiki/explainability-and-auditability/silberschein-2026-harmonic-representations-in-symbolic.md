---
title: "Harmonic Representations in Symbolic Music Transformers are Localized and Controllable"
authors: Adi Silberschein, Megan Wei, Tamar Rott Shaham
year: 2026
doi: 10.48550/arXiv.2610.15957
category: explainability-and-auditability
source: silberschein-2026-harmonic-representations-in-symbolic.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/silberschein-2026-harmonic-representations-in-symbolic.pdf"
pdf_filename: silberschein-2026-harmonic-representations-in-symbolic.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-31
tags:
  - mechanistic-interpretability
  - activation-patching
  - linear-probing
  - activation-steering
  - harmony
  - symbolic-music
---
## Summary

The paper asks where and how a symbolic music transformer represents tonal harmony, and whether that representation can be used as a control knob. Lowering one note at a cadence changes Aria's resolution; patching shows the causal effect appearing only from the middle layers; probes recover mode before key; and adding probe-derived directions at inference time turns tonic resolutions into relative- or parallel-minor ones while structural errors stay near zero.

## Key Contributions

- A minimal, musically meaningful counterfactual: one pitch changed from V to v, everything else held fixed.
- Causal localisation of harmonic computation to middle and late layers, converging with where probes peak.
- Evidence for a processing hierarchy: mode is decodable around layers 8–9, key identity only after layer 10.
- Training-free steering that changes cadence resolution while keeping generated music structurally intact.
- An explanation of why parallel-minor steering is cleaner than relative-minor steering: the model's geometry places relative keys closer together, and a relative-grouped probe scores higher than either the full key probe or a parallel-grouped probe.

## Methodology and Architecture

Aria is a LLaMA-based autoregressive symbolic transformer evaluated on Bach chorales without fine-tuning. Cadences are located with music21 and the chordal third of the dominant is lowered a semitone, producing 184 major-source and 91 minor-source pairs with three sampling seeds each. The three analyses are interchange intervention over layers, per-layer linear probes for mode and key on 3,176 bar-final activations, and steering along the normalised difference of two probe weight vectors added to the residual stream at selected layers. Quality is tracked with structural-error rates, out-of-range notes, Fréchet Music Distance, Roman-numeral entropy, and top-1 dominance.

The complete evidence-grounded digest, with page anchors and the corrected FMD values, is in [`sources/silberschein-2026-harmonic-representations-in-symbolic.md`](../../sources/silberschein-2026-harmonic-representations-in-symbolic.md).

## Results

Tonic resolutions in major-source chorales fall from 87.5% to 51.4% after the one-note edit [PDF p. 3, Fig. 2]. Patching layers 0–5 barely moves the output while the effect grows from layer 6 onward [PDF p. 4, Fig. 3]. Mode peaks at 82.1% (chance 50%) around layers 8–9; key reaches 65.5% by layer 15 (chance 5.6%) [PDF p. 4, Fig. 4]. From an 81% tonic baseline, relative-minor steering at α = 0.15 sends 32% of cases to vi, and parallel-minor steering at α = 0.1 sends 57% to i; mode steering at α = 0.25 reduces tonic resolutions but spreads the rest [PDF p. 5, Fig. 5]. Structural errors stay at or below 2.9% and out-of-range notes at 0% [PDF p. 6, Table 1]. The relative-grouped probe reaches 83.4% against 65.5% for the full key probe and 65.3% for the parallel-grouped probe, which the authors read as relative keys sitting closer together in representation space [PDF pp. 5–6, Figs. 6–7].

## Related Papers

- [[concepts/music-theory-probing]] — the three-claim ladder this paper advances: recoverable information, causally used information, and human-useful explanation. It establishes the first two.
- [[explainability-and-auditability/pocwiardowski-2026-mi-midi-mechanistic-interpretability-of]] — the same probing-plus-steering protocol on text2midi and MIDI-LLM, giving a second symbolic model family.
- [[explainability-and-auditability/chen-2026-dual-contrastive-sparse-autoencoders]] — the audio-latent counterpart with matched-random steering controls.
- [[theory-and-constraints/ebrahimzadeh-2026-emergent-tonal-structure-in-learned]] — what tonal structure emerges in learned representations, the theoretical question behind these probes.
- [[overviews/2026-symbolic-music-literature-map]] — batch index for the October 2026 intake this reading belongs to.
