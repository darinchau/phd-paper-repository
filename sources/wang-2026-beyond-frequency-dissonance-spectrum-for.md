---
title: "Beyond Frequency: Dissonance Spectrum for Perceptually Motivated Music Understanding"
authors: Tianle Wang, Xinyi Tong, Liangke Zhao, Jishang Chen, Sirui Zhang, Haoxin Zhang, Xin Jin, Duo Xu, Xiaobing Li, and Song-Chun Zhu
year: 2026
doi: 10.48550/arXiv.2608.25621
category: theory-and-constraints
pdf_path: "C:/Users/User/Documents/Repository/phd-paper-digestion/phd-paper-repository/papers/wang-2026-beyond-frequency-dissonance-spectrum-for.pdf"
pdf_filename: wang-2026-beyond-frequency-dissonance-spectrum-for.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-09-07
---

## One-line Summary

Dissonance Spectrum attributes a specified rational pitch-relation model to time–frequency bins and yields small favorable mean gains as an auxiliary representation, with explicit perceptual and statistical limits.

## 1. Document Information

The canonical original is arXiv 2608.25621v1, dated 26 August 2026: nine main-paper/reference pages plus ten appended supplementary pages (19 total). The printed title “Beyond Frequency: Dissonance Spectrum for Perceptually Motivated Music Understanding” differs from the internal PDF metadata title; the printed title controls this record. Metadata declares the arXiv nonexclusive distribution license, which is not a general redistribution grant. No separate code/data archive or LaTeX was supplied.

## 2. Key Contributions

- A deterministic, nonnegative binwise attribution of rational pitch relations.
- Intrinsic and explicit-reference forms with an indexed frequency-correlation implementation.
- Controlled theory-derived tests and matched auxiliary-branch comparisons in two audio-understanding families.
- Six-seed reporting that separates mean improvement from distribution-free inferential support. [PDF pp. 2–7, 10–19]

## 3. Methodology and Architecture

### Rational relation kernel

For reduced ratios p/q with 1 ≤ p ≤ q ≤ Q, complexity is log₂(pq). Given the smaller/larger frequency ratio, choose the least-complex candidate within a 1% relative tolerance; if none qualifies, use the closest candidate. Map semitone intervals to frequency ratios, normalize complexity over one octave, and define an even octave-folded kernel D̄(|Δpitch| mod 12), with zero at unison. Q controls finite search resolution. This models one harmonic-distance/periodicity-inspired relation, not critical-band roughness or universal pleasantness. [PDF pp. 2–3]

### Spectral attribution

For nonnegative CQT magnitudes x(k,t), intrinsic attribution is

d(k,t) = x(k,t) / K × Σ_l x(l,t) D̄(p_l − p_k).

Each active target bin therefore receives amplitude-weighted relations to other bins; inactive bins receive zero. The output retains K frequency locations and T frames. Cross-reference DS replaces the reference x(l,t) by a separate tonic, chord, or spectrum. Because the kernel depends only on pitch difference, target-aligned frequency correlation avoids materializing a K×K×T pair tensor. This is a storage improvement, not a demonstrated subquadratic arithmetic complexity guarantee. [PDF pp. 3–4, 10–11]

The supplement explicitly defines correlation indices; using an ordinary valid cross-correlation with its increasing-lag storage requires a final frequency reversal or equivalently reversed lag layout. Optional temporal averaging of references is distinct from the temporal encoder applied to framewise intrinsic DS. The main downstream comparison uses intrinsic DS. [PDF pp. 10–11]

### Controlled validation versus downstream preprocessing

Controlled piano tests use 22.05kHz audio, four frames/second, 576 CQT bins across eight octaves at 72 bins/octave from C1, Q=60, tolerance .01, peak prominence .015, a relative-frame soft gate .1, and four-second context normalization. Targets and references are normalized separately. Intervals/scales use C4; chord qualities average tonic-reference and intrinsic DS; functional connections use C major. Sustained examples use the maximum framewise sum, while scales sum over time. These reference choices test different hypotheses and should not be conflated with one context-free score. [PDF pp. 5, 12–14]

Downstream inputs use 24kHz, 45-second excerpts (except PMEmo's chorus clips), hop 1,024, the same 576-bin grid, and excerpt-level maximum normalization. Features are cached with audio hash, grid/kernel parameters, preprocessing, and aligned excerpt indices. DS is log(1+D)-compressed. Gaussian and magnitude-CQT branches share architecture, parameters, pooling, and training controls; branch-input transformation/compression is not fully isolated. [PDF pp. 4–5, 16]

### Model integration and comparisons

A lightweight encoder supplies DS keys/values to a gated residual adapter queried by the host representation. Zero output-projection initialization and gate bias −3 preserve the initial baseline function. For MU-LLaMA, the adapter follows the audio projection with frozen LLaMA-2 7B and MERT-v1-330M. Trainable parameters rise from 4,205,568 to 5,565,761. Music2Emo inserts after its original 512-dimensional projection of MERT/chord/key-mode features; its trainable network rises from 1,071,617 to 1,280,962, with frozen 95M MERT. [PDF pp. 5–7, 16]

Six paired seeds (17, 42, 101, 2025, 2026, 3407) share splits, excerpt selection, order, optimization, and checkpoint rules across baseline, Gaussian, CQT, and DS. MusicQA trains on 70,011 pairs from 7,779 tracks and tests on 5,040 pairs from 560 audio-disjoint tracks. Music2Emo retains official MTG-Jamendo splits and experiment-specific track splits for DEAM, EmoMusic, and PMEmo. The nominal 70/15/15 description should be read alongside explicit counts: 1,261/271/270; 495/124/125; and 536/116/115 respectively. The EmoMusic counts correspond to approximately 66.5/16.7/16.8%, an unresolved reporting discrepancy. [PDF pp. 5–7, 16; percentage arithmetic is repository analysis]

## 4. Key Results and Benchmarks

### Theory-derived tests

| Test | n | Spearman ρ (p) | Kendall τb (p) |
|---|---:|---:|---:|
| Intervals | 13 | .951 (6.36e-7) | .846 (5.20e-6) |
| Four chord exemplars | 4 | 1.000 (ordering check) | 1.000 (ordering check) |
| Extended chord voicings | 13 | .626 (.022) | .462 (.030) |
| Functional connections | 7 | .794 (.033) | .655 (.054) |
| Church modes | 7 | .893 (.0068) | .810 (.0107) |

The minor second has high DS and the fifth/octave low DS. Voicing produces local chord reversals; Dorian lies below Lydian despite the imposed mode rank. Functional connections measure relation to a C-major reference, not voice leading or learned expectation. Most target ranks are theory-derived hypotheses; there is no new listener validation. [PDF pp. 5–6, 12–14]

### Downstream results

| Endpoint | Baseline | Gaussian | CQT | DS |
|---|---:|---:|---:|---:|
| MusicQA BLEU | .2987 | .2985 | .3056 | .3074 |
| METEOR | .3761 | .3759 | .3838 | .3857 |
| ROUGE-L | .4556 | .4554 | .4643 | .4671 |
| BERTScore-R | .8952 ± .0007 | .8950 ± .0006 | .8996 ± .0006 | .9024 ± .0015 |
| Answer-token loss | .625 | .626 | .607 | .600 |
| Perplexity | 1.868 | 1.870 | 1.836 | 1.822 |
| Jamendo macro PR-AUC | .1539 | .1537 | .1564 | .1580 |
| Jamendo macro ROC-AUC | .7806 | .7801 | .7828 | .7841 |
| DEAM valence / arousal R² | .5169 / .6209 | .5164 / .6202 | .5272 / .6260 | .5355 / .6291 |
| EmoMusic valence / arousal R² | .6487 / .7598 | .6479 / .7590 | .6575 / .7642 | .6642 / .7668 |
| PMEmo valence / arousal R² | .5451 / .7926 | .5445 / .7920 | .5532 / .7970 | .5587 / .7992 |
| Mean of six V/A R² endpoints | .6473 ± .0014 | .6467 ± .0014 | .6542 ± .0016 | .6589 ± .0018 |

All are paper-reported six-seed means; ± values shown here are seed SD. Primary endpoints are MusicQA BERTScore-R and the six-endpoint mean V/A R². DS improves them by .0072/.0116 over baseline and .0028/.0047 over CQT. Every paired seed difference is positive. Holm-adjusted paired-t values are at most .0017, but the exact two-sided sign test is .03125 before and .09375 after correction over three comparisons per task. Thus the paper does not establish familywise distribution-free significance at .05. Seed variation also does not quantify every source of dataset or listener uncertainty. [PDF pp. 6–7, 19]

Three-seed exploratory MusicQA BERTScore-R falls from proposed .9015 to .8985 with global DS, .8992 with randomized frequency correspondence, .8997 with temporal shuffling, and .9004 with earlier insertion. This three-seed .9015 must not be confused with the main six-seed .9024. Music2Emo's six-seed mean falls from .6589 to .6524/.6550/.6558 for global/shuffled/early-fusion variants. These are exploratory, non-isolating mechanism checks. [PDF p. 17; tables visually checked]

Seven independently rendered loudness conditions yield a rounded Theil–Sen log-slope −.000, CI [−.014, .000], DS relative SD .94%, and relative range 2.49%. This supports near gain-invariance under the chosen normalization, not independence from perceptual loudness. Timbre and 24-TET figures are qualitative; uncontrolled envelopes/levels prevent a causal timbre ranking. [PDF pp. 15–16]

## 5. Limitations and Future Work

DS omits masking, auditory filter bandwidths, learned tonal syntax, rhythmic tension, and individual/cultural preference. The mathematical map is inspectable, but downstream answers and emotion predictions do not thereby become faithful explanations. MusicQA reference-similarity metrics are not verified musical correctness; some supplied questions can plausibly be answered from text alone. Audio-disjoint evaluation does not rule out that shortcut. There is no generation experiment, listener study, or musician-facing explanation evaluation. [PDF pp. 7, 17–19; shortcut implication is repository inference]

The MusicQA evaluator explicitly differs from the original MU-LLaMA script, and its test set is 5,040/560 rather than 4,500/500 pairs/tracks. Music2Emo also changes the original segment-augmentation protocol. Contextual comparisons in the supplement are therefore not direct reproductions. BERTScore uses English roberta-large recall without IDF/baseline rescaling; this choice must accompany the metric values. [PDF pp. 16–18]

The PDF repeatedly refers to a separately submitted Code and Data Archive containing manifests, implementation, predictions, and table scripts. None is supplied locally, no public archive URL is embedded in this PDF, and no author code was inspected. Its separate demo and natural-minor-file omission cannot be independently checked. This is an artifact-availability gap, not evidence of fabrication or a confirmed code/result mismatch.

## 6. Related Work

[[concepts/music-domain-inductive-biases]] is the primary existing synthesis anchor: DS explicitly constructs a relation that a learned representation might otherwise encode implicitly. [[concepts/dissonance-spectrum]] records the reusable mechanism and scope. [[concepts/music-theory-probing]] provides the contrasting question of whether concepts can be recovered from a frozen model. These are methodological connections, not DS experiments on the repository's symbolic generators.

## 7. Glossary

- **CQT:** constant-Q time–frequency representation with logarithmic pitch spacing.
- **Rational complexity:** log₂(pq) for a reduced ratio p/q.
- **Intrinsic DS:** target and reference use the same spectrum.
- **Cross-reference DS:** attribute target relations to an explicitly chosen reference.
- **Gated residual adapter:** learned auxiliary update added to a host representation.
- **BERTScore-R:** embedding-based recall against reference text, not factual correctness.
- **Paired seed:** conditions share a training/evaluation seed and protocol for within-seed comparison.
