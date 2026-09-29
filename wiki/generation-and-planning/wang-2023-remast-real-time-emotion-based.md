---
title: "REMAST: Real-time Emotion-based Music Arrangement with Soft Transition"
authors: Zihao Wang, Le Ma, Chen Zhang, Bo Han, Yunfei Xu, Yikai Wang, Xinyi Chen, Haorong Hong, Wenbo Liu, Xinda Wu, and Kejun Zhang
year: 2023
doi: 10.48550/arXiv.2305.08029
source: wang-2023-remast-real-time-emotion-based.md
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/wang-2023-remast-real-time-emotion-based.pdf"
pdf_filename: wang-2023-remast-real-time-emotion-based.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-09-29
tags:
  - symbolic-music-generation
  - emotion-controlled-arrangement
  - real-time-music
  - music-theory-features
  - semi-supervised-learning
  - music-therapy
  - human-evaluation
---

## Summary

REMAST arranges a known symbolic melody toward changing valence-arousal targets while attempting to preserve musical continuity. It recognizes the previous generated segment’s emotion, fuses that state with the current target, and uses the result to condition a Transformer that generates melody and harmony. A downsampled input melody controls the similarity–freedom trade-off. [REMAST PDF, Sections III–V]

The paper reports 18,201 labelled and 15,591 unlabelled four-bar segments from eleven datasets. Against three adapted baselines, REMAST obtains the best reported coherence and pitch similarity and the second-best objective emotion fit. Thirty listeners also rate it highest on coherence, softness, similarity, and fit. [REMAST PDF, Tables II–III]

## Key Contributions

- Feedback conditioning on the previous **realized** musical emotion rather than only previous target emotion.
- Four explicit music-domain features: Harmonic Color, Rhythm Pattern, Contour Factor, and Form Factor.
- Downsampling-based arrangement that preserves coarse source structure while generating detail.
- Semi-supervised use of emotion-labelled and unlabelled symbolic music.
- Joint objective, subjective, latency, and anxiety-relief evaluation.

The strongest transferable idea is state feedback: the next segment is conditioned on what the system actually expressed, not merely on what it was previously asked to express.

## Methodology and Architecture

The emotion recognizer uses MLPs over music content and the four theory features. The Transformer generator receives the current melody and a fused emotion representation. The authors compare median, concatenation, and feature-concatenation fusion; the final model uses feature concatenation.

The original melody is downsampled from sixteenth-note detail to quarter-note samples. The generator reconstructs full-resolution melody and harmony, making sampling granularity a practical control over source similarity and emotional freedom. Harmony is then expanded into multi-track accompaniment.

The training pipeline first uses labelled recognition and generation losses, then uses recognized emotions on unlabelled data. The corpus combines modern, classical, folk, game, and soundtrack material after MIDI conversion, label alignment, filtering to 4/4 and 2/4, and four-bar segmentation.

## Results

REMAST reports objective values of PCC 3.04, CEC 3.71, MCTC 1.04, overall coherence 6.21, similarity 7.60, and real-time fit 2.02. It leads all baselines on the coherence and similarity measures but is slightly below TG-Muhamed on objective fit. Subjective scores are 4.00 coherence, 3.79 softness, 3.90 similarity, and 3.66 fit.

Ablations indicate that all four theory features, beat-level granularity, downsampling, and semi-supervised training contribute to the selected operating point. Reported four-bar generation latency is about one second on an RTX 3080 Ti and 2.9 seconds on a Xeon CPU.

## Related Papers

- [[concepts/music-domain-inductive-biases]] — REMAST uses explicit music-domain descriptors, but the paper does not establish that they are faithful explanations or hard constraints.
- [[generation-and-planning/lin-2026-diff-symbo-text-controlled-long]] — both use previous-segment information, although REMAST feeds back recognized affect while Diff-Symbo conditions long-form generation through latent segment context.
- [[generation-and-planning/wang-2025-notagen-advancing-musicality-in-symbolic]] — complementary example of symbolic generation with visible representation choices and learned preference optimization.
