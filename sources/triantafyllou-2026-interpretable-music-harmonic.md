---
title: "Interpretable Music Harmonic Analysis Through Multilinear Mixture of Experts"
authors: Thanasis Triantafyllou, Mihalis A. Nicolaou, and Yannis Panagakis
year: 2026
doi: 10.1109/ICASSP55912.2026.11463689
category: explainability-and-auditability
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/triantafyllou-2026-interpretable-music-harmonic.pdf"
pdf_filename: triantafyllou-2026-interpretable-music-harmonic.pdf
source_collection: IEEE ICASSP proceedings
source_format: pdf
extracted_date: 2026-10-11
---

## One-line Summary

Triantafyllou et al. replace RNBERT feed-forward blocks with factorized multilinear mixture-of-experts layers, preserving near-baseline Roman-numeral-analysis accuracy while exposing expert activations that the authors associate with key-specific and dominant-to-tonic harmonic patterns.

## 1. Document Information

- **Venue:** 2026 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP 2026), pp. 16082–16086.
- **Primary contribution/category:** intrinsic interpretability for symbolic harmonic analysis; categorized under `explainability-and-auditability`.
- **Artifact:** the paper identifies code as `https://github.com/TomusD/muMoE-RNBERT`; the supplied PDF does not establish the exact training-code revision used for the reported tables.
- **Evidence boundary:** the paper reports one test-set comparison and activation analyses on 146 test scores. The expert-to-musical-pattern interpretation is supported by thresholded statistics and piano-roll visualizations, not by causal ablation of individual experts or a human explanation-utility study.

## 2. Key Contributions

1. **Intrinsic architecture:** replace the two dense feed-forward MLP layers inside each RNBERT transformer block with multilinear mixture-of-experts layers, rather than adding a post-hoc explainer.
2. **Parameter-matched comparison:** CP and tensor-ring factorization variants retain approximately the 26.7M-parameter RNBERT budget and report near-identical RNA accuracy.
3. **Musical specialization analysis:** expert coefficients are examined for key, degree, inversion, and quality patterns, with reported specialization around dominant-to-tonic relations and circle-of-fifths neighborhoods.

## 3. Methodology and Architecture

The baseline RNBERT fine-tunes MusicBERT for multi-task token classification of four interconnected RNA attributes: key, degree, chord quality, and inversion. Scores use OctupleMIDI; salami-slicing produces homophonic segments of 1,000 tokens with 250-token overlap, quantized at the 64th-note level, and duplicate notes with identical pitch/timing are removed. Nine of MusicBERT's twelve layers are frozen and the top three are fine-tuned.

The proposed multilinear layer represents expert weights with CP or tensor-ring factorizations. A gating network uses entmax to produce sparse but differentiable expert coefficients for each note token. Both feed-forward linear layers are replaced, while task-specific classification heads remain separate. The design aims to expose shared harmonic pathways before task-specific outputs without adding the parameter or inference burden of a conventional large sparse-MoE expansion.

Training uses the original RNBERT data split and preprocessing, 50,000 steps, batch size 4, Adam, learning rate `2.5 × 10^-4`, 2,500-step linear warmup, and linear decay. Variants use 48 or 256 experts; the analysis selects 48 as the most useful trade-off for interpretable specialization.

## 4. Key Results and Benchmarks

| Model | Degree | Quality | Inversion | Key | RN accuracy | Parameters |
|---|---:|---:|---:|---:|---:|---:|
| RNBERT | 76.2 | 86.7 | 87.2 | 82.2 | 62.0 | 26.7M |
| CP-MoE-RNBERT, N=48 | 74.7 | 86.5 | 86.9 | 81.4 | 60.9 | 26.7M |
| TR-MoE-RNBERT, N=48 | 74.6 | 86.3 | 86.8 | 81.6 | 60.4 | 26.7M |
| CP-MoE-RNBERT, N=256 | 74.9 | 86.4 | 87.2 | 82.3 | 61.4 | 26.8M |
| TR-MoE-RNBERT, N=256 | 74.7 | 86.2 | 87.1 | 82.1 | 61.0 | 26.2M |

The table reports accuracy percentages on the test set. A two-proportion Z-test is reported as non-significant (`p = .80`) with maximum Cohen's `h = .033`. The 48-expert models therefore retain performance close to RNBERT while providing inspectable coefficients.

For activation analysis, overlapping segment coefficients have mean cosine similarity `μ = .99` and standard deviation `.013`; the authors use the mean across overlaps. With coefficient threshold `.4`, the most active experts commonly align with I and V labels and dominant-to-tonic relationships. Visualizations of Bach's Well-Tempered Clavier Prelude No. 23 and Chorale No. 343 show key-specific activation clusters, including circle-of-fifths patterns and expert differences between tonic and dominant contexts. Deeper layers show narrower examples such as minor-seventh or onset-related specialization.

## 5. Limitations and Future Work

- Expert activation is correlational: high coefficients and recognizable piano-roll patterns do not prove that an expert is causally necessary for a prediction. Expert ablation, activation patching, or counterfactual routing is not reported.
- The test set contains uneven key coverage; the authors specifically note that underrepresented F-sharp and C-sharp major cases make quantitative interpretation difficult.
- Thresholded top-label counts and visual examples can overstate semantic purity. Increasing expert count changes the trade-off: fewer experts are polysemantic, 128–512 can lose activation clusters, and more than 1,000 can make one expert broad rather than interpretable.
- The study inherits the RNBERT data split and preprocessing; work, composer, and corpus generalization are not newly stress-tested here.
- No musician study measures whether experts help prediction, diagnosis, correction, trust calibration, or musicological discovery.
- Future work proposes applying the approach to melody harmonization, composer classification, automatic transcription, and rhythmic MIR tasks.

## 6. Related Work

The paper builds on RNBERT and MusicBERT, and contrasts intrinsic expert specialization with post-hoc explanation methods such as LIME-style approaches. These references are not separately ingested here.

- [[theory-and-constraints/mcleod-2020-a-modular-system-for]] — modular harmonic analysis makes stages inspectable but does not expose learned internal causes.
- [[concepts/music-domain-inductive-biases]] — distinguishes architecture-level musical structure, explicit constraints, and faithful explanation.
- [[concepts/music-theory-probing]] — frames recoverability and intervention as separate claims; expert activation patterns require the same caution.
- [[explainability-and-auditability/wei-2024-do-music-generation-models-encode]] — controlled representation probing without causal intervention.

## 7. Glossary

- **Roman numeral analysis (RNA):** labeling chords by harmonic function and related attributes relative to a key.
- **RNBERT:** a MusicBERT-based transformer fine-tuned for multi-task RNA.
- **Multilinear mixture of experts:** an expert layer whose weights are factorized so token-dependent coefficients combine specialized pathways.
- **CP decomposition:** canonical polyadic factorization of the expert weight tensors.
- **Tensor ring:** a cyclic tensor factorization used as an alternative expert parameterization.
- **Entmax:** a sparse probability mapping used here to produce differentiable expert coefficients.
- **Intrinsic interpretability:** interpretability designed into the model computation, rather than applied after prediction.
