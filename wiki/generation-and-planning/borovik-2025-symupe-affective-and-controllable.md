---
title: "SyMuPe: Affective and Controllable Symbolic Music Performance"
authors: Ilya Borovik, Dmitrii Gavrilev, Vladimir Viro
year: 2025
doi: 10.1145/3746027.3755871
source: borovik-2025-symupe-affective-and-controllable.md
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/borovik-2025-symupe-affective-and-controllable.pdf"
pdf_filename: borovik-2025-symupe-affective-and-controllable.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-16
tags: [expressive-performance-rendering, flow-matching, inpainting, emotion-control, text-conditioning, piano, dataset, listening-test, classifier-free-guidance]
---

## Summary

SyMuPe is a framework for symbolic expressive piano performance rendering whose flagship model, PianoFlow, formulates rendering as multi-mask performance-feature inpainting solved by conditional flow matching (OT-CFM) with a 24M-parameter transformer encoder. Trained on PERiScoPe — a curated 2,968-hour note-aligned score–performance corpus (36,977 performances, 1,176 pieces, 67 composers, assembled from (n)ASAP, ATEPP, PDMX, and 2,215 proprietary hours) — PianoFlow wins 67.1% of blind pairwise listening comparisons against baselines and real dataset performances, and supports emotion and arbitrary-text control via a 33-emotion classifier whose bar-level soft labels weight Flan-T5 template embeddings. [PDF pp. 1, 4–8]

The perceptual headline (beating human dataset samples 57.1% head-to-head) is explicitly qualified by the authors: two-thirds of "real" samples are audio-transcribed MIDI and the listener pool was not musically expert, so the fair claim is superiority over the average ASAP/ATEPP human MIDI sample, not over human performance. [PDF pp. 7–8]

## Key Contributions

- **SyMuPe tokenizer + framework:** MidiTok-based score/performance encoding (real-valued or quantized), configurable encoder/encoder–decoder models under MLM, CLM, and flow-matching objectives. [PDF pp. 4, 6]
- **PianoFlow:** masked OT-CFM training over five mask families (notes/beats/bars/segments/end-of-sequence) plus fully-masked halves of each batch — one model for rendering, inpainting, and continuation; 355 notes/s inference. [PDF pp. 4–5, 7]
- **PERiScoPe dataset:** the largest aligned score–performance corpus reported for EPR (partly proprietary, not releasable). [PDF p. 5, Table 1]
- **Emotion/text conditioning pipeline:** 33-emotion classifier (top-1 32%) → per-bar soft labels → probability-weighted Flan-T5 embeddings of 16 templates; classifier-free guidance with per-control dropout 0.2; control injected at the middle layer. [PDF pp. 5–6, 8]

## Methodology and Architecture

Real-valued note features avoid quantization loss: score (pitch, position, position shift, duration) and performance (velocity, time shift, pressed duration, sustained duration); pedal approximated by the pressed/sustained pair. The model learns a time-conditioned vector field supervised only on masked positions; inference integrates a 10-step ODE with adaptive steps. Multi-mask training is what makes the model a universal performance infiller: it can re-express selected regions, continue a performance, or render from scratch. [PDF pp. 4–5]

Alignment (Parangonar) is cleaned of deviating onsets and 7.5% of notes are interpolated; splits are composition-level. Internal baselines (MLM encoder, EncDec) are trained on the same data; external baselines (VirtuosoNet/ISGN, DExter) run with official checkpoints and may have seen test repertoire. [PDF pp. 5–7]

## Results

| System | Overall listening win rate | Notes/s (V100) |
|---|---:|---:|
| PianoFlow | 67.1% | 355 |
| Dataset (human MIDI) | 59.6% | – |
| VirtuosoNet | 51.0% | 1700 |
| Deadpan | 41.8% | – |
| DExter | 27.7% | 30 |

708 paired ratings, 26 retained participants, 20 pieces. Objectively PianoFlow best tracks human IOI/OD/articulation correlations (IOI 0.86 vs 0.90 human–human ceiling), VirtuosoNet retains the best velocity correlation, and the KL-closest model (MLM encoder) is perceptually worst — objective distribution metrics and perceptual quality dissociate. Text control is demonstrated qualitatively (anger → louder with sustain; dreamy/sad → slower; mixed prompts interpolate), with no controlled evaluation of control strength. [PDF pp. 7–8, Table 2, Fig. 2]

## Related Papers

- [[concepts/work-identity-versus-performance-variation]] — SyMuPe renders expression conditioned on text/emotion but leaves the work/interpretation boundary implicit; Zeng et al. and Chen et al. make it an explicit modeling target.
- [[generation-and-planning/edwards-2026-learning-jazz-pianist-style-with]] — alternative performer-style conditioning via cross-attention.
- [[concepts/expression-aware-symbolic-representations]] — complementary treatment of written expression instructions vs realized performance features.
- [[overviews/2026-symbolic-music-literature-map]] — batch synthesis anchor.
- [[interaction-and-evaluation/batlle-roca-2026-on-the-human-and-computer]] — the perceptual axis this paper's listening test lacks: attribute-level expert judgment rather than aggregate preference.
