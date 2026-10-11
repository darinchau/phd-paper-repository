---
title: "Interpretable Music Harmonic Analysis Through Multilinear Mixture of Experts"
authors: Thanasis Triantafyllou, Mihalis A. Nicolaou, and Yannis Panagakis
year: 2026
doi: 10.1109/ICASSP55912.2026.11463689
source: triantafyllou-2026-interpretable-music-harmonic.md
category: explainability-and-auditability
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/triantafyllou-2026-interpretable-music-harmonic.pdf"
pdf_filename: triantafyllou-2026-interpretable-music-harmonic.pdf
source_collection: IEEE ICASSP proceedings
source_format: pdf
extracted_date: 2026-10-11
tags: [roman-numeral-analysis, mixture-of-experts, intrinsic-interpretability, harmonic-analysis, symbolic-music]
---

## Summary

Triantafyllou et al. introduce MoE-RNBERT, an intrinsic interpretability variant of RNBERT for Roman numeral analysis. Factorized multilinear expert layers replace transformer feed-forward MLPs while keeping approximately 26.7M parameters. The 48-expert model remains close to RNBERT on reported test accuracy, and thresholded expert activations show key-specific and dominant-to-tonic patterns.

The evidence supports a useful inspectable hypothesis about internal specialization, not a causal explanation. The paper reports no expert ablation, counterfactual routing, or musician study, and activation semantics are affected by uneven key coverage and threshold choices.

## Key Contributions

- CP and tensor-ring multilinear experts provide sparse, differentiable, token-specific pathways inside RNBERT.
- CP-MoE-RNBERT with 48 experts reports 60.9 RN accuracy versus 62.0 for RNBERT, with both at 26.7M parameters.
- Expert statistics and piano-roll heatmaps associate pathways with I/V functions, dominant-to-tonic relations, circle-of-fifths keys, and narrower layer-specific patterns.

## Methodology and Architecture

The system fine-tunes the top three of twelve MusicBERT layers on OctupleMIDI RNA segments while freezing the first nine. Each token predicts key, degree, quality, and inversion. MoE layers replace both feed-forward linear layers; entmax computes sparse differentiable coefficients, while CP or tensor-ring factorization keeps parameter count and FLOPs close to the dense baseline.

The authors analyze coefficient vectors on 146 test scores, average overlapping segment activations, and inspect occurrences above threshold `.4`. Quantitative plots identify frequently activated Roman numerals and key relations; piano-roll heatmaps on Bach examples provide qualitative context.

## Results

RNBERT reports degree/quality/inversion/key/RN accuracies of `76.2/86.7/87.2/82.2/62.0`. The best reported MoE trade-off uses 48 experts: CP gives `74.7/86.5/86.9/81.4/60.9`, while tensor-ring gives `74.6/86.3/86.8/81.6/60.4`. The reported two-proportion test finds no significant difference (`p = .80`, maximum Cohen's `h = .033`).

Expert activations most often emphasize I and V and form dominant-to-tonic and circle-of-fifths patterns. The authors report more interpretable specialization at 48 experts than at lower or much higher counts, but these patterns remain observational and dataset-dependent.

## Related Papers

- [[theory-and-constraints/mcleod-2020-a-modular-system-for]] — inspectable modular harmonic analysis without intrinsic expert traces.
- [[concepts/music-domain-inductive-biases]] — separates architectural bias from constraints and faithful explanation.
- [[concepts/music-theory-probing]] — recoverability, interventions, and explanation utility as distinct evidence claims.
- [[explainability-and-auditability/wei-2024-do-music-generation-models-encode]] — representation probing of music-theory labels.
