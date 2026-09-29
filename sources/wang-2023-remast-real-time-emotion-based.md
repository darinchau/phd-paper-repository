---
title: "REMAST: Real-time Emotion-based Music Arrangement with Soft Transition"
authors: Zihao Wang, Le Ma, Chen Zhang, Bo Han, Yunfei Xu, Yikai Wang, Xinyi Chen, Haorong Hong, Wenbo Liu, Xinda Wu, and Kejun Zhang
year: 2023
doi: 10.48550/arXiv.2305.08029
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/wang-2023-remast-real-time-emotion-based.pdf"
pdf_filename: wang-2023-remast-real-time-emotion-based.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-09-29
---

## One-line Summary

REMAST is a symbolic, emotion-controlled music arrangement system that conditions each new segment on both the current target emotion and the emotion recognized from the previously generated segment, aiming to trade a small amount of responsiveness for smoother transitions while preserving a known melody.

## 1. Document Information

- **Official source:** [arXiv:2305.08029v3](https://arxiv.org/abs/2305.08029v3), updated 27 July 2024.
- **Task:** real-time emotion-based arrangement, not unconstrained composition. The user selects a melody; the system generates melody details and harmony for successive four-bar segments.
- **Primary category:** `generation-and-planning`. The central contribution is a controllable symbolic generation and arrangement architecture. Its secondary contributions concern music-domain inductive biases, semi-supervised learning, and subjective evaluation.
- **Representation:** four-bar symbolic segments with melody sampled at sixteenth-note resolution, a quarter-note downsampled melody, harmony sampled at quarter-note resolution, and valence-arousal emotion labels where available.
- **Reported compute:** PyTorch; training for 50 epochs on an NVIDIA Tesla A100. The paper reports four-bar generation latency on CPU, Apple M1, and RTX 3080 Ti.
- **Evidence boundary:** Results below are reported by the paper. Interpretive claims about source identity, explanation, and therapeutic effectiveness are repository-level assessments, not claims established by the authors.

## 2. Key Contributions

1. **Previous-output emotion feedback.** REMAST recognizes the emotion of the previous generated segment and fuses it with the current target emotion. This differs from simply averaging successive target inputs and is intended to keep the trajectory moving toward the target while reducing adjacent emotional discontinuities.
2. **Four explicit emotion-related music features.** Harmonic Color, Rhythm Pattern, Contour Factor, and Form Factor provide structured inputs to the emotion recognizer.
3. **Downsampling arrangement pipeline.** A coarse beat-level melody is used to reconstruct full-resolution melody and harmony. Sampling granularity therefore becomes a control over preservation of the input melody versus freedom to fit the target emotion.
4. **Semi-supervised learning.** The model first uses emotion-labelled data and then exploits unlabelled symbolic music with recognized emotion as a training signal, while blending manual and recognized labels.
5. **Combined objective and subjective evaluation.** The authors measure local tonal/chord coherence, similarity, and valence-arousal fit, and conduct listener studies covering coherence, transition softness, similarity, and emotion fit.

## 3. Methodology and Architecture

### 3.1 Overall pipeline

REMAST has two phases. An emotion-recognition model receives music content and the four theory features and predicts a fine-grained valence-arousal sequence for a four-bar segment. A Transformer generation model receives the current input melody plus a fused emotion condition and outputs melody and harmony. A texture-generation procedure then converts harmony into multi-track accompaniment.

The recognizer uses two sets of MLPs, separate embeddings for music content and theory features, a 512-unit hidden layer, and ReLU activation. The generator is a Transformer with four encoder and four decoder layers, embedding size 512, feed-forward size 1024, two attention heads, dropout 0.1, maximum input length 64, and maximum output length 256.

### 3.2 Emotion fusion

The paper compares three fusion methods:

- **Median Emotion:** the midpoint of the previous recognized music emotion and current target emotion in valence-arousal space.
- **Emotion Concat:** concatenation of the two emotion vectors followed by dimensionality reduction.
- **Features Concat:** concatenation of the current target emotion with music/content features from the previous segment, followed by dimensionality reduction.

The authors select Features Concat as the final configuration. Their geometric argument is that the previous *generated* emotion supplies the actual state of the music, whereas the previous target may not have been achieved. This reduces the chance that the trajectory changes in the wrong direction when target inputs change.

### 3.3 Music-theory features

- **Harmonic Color:** a relative harmonic-distance measure based on positions of chord notes on the circle of fifths. It is intended to describe harmonic freshness relative to a reference chord.
- **Contour Factor:** pitch extrema, melodic and chord trends, and concave/convex contour properties over four bars, represented in melody and chord dimensions.
- **Form Factor:** binary or interval-valued judgments for melody repetition, chord repetition, tonal transformation, register/zone transformation, and rhythmic difference. A rolling cache retains up to 80 bars of information.
- **Rhythm Pattern:** successive pitch durations extracted from MIDI before downsampling, preserving rhythmic information that would otherwise be lost.

These features are domain-informed descriptors, not hard generation constraints or proofs that a particular musical feature caused a listener judgment.

### 3.4 Downsampling arrangement

The original melody is sampled every quarter note to form a coarse representation. The model generates a higher-resolution melody and harmony from this representation under emotion control, analogous to filling in detail after image super-resolution. Coarser input preserves less literal source detail and gives the generator more freedom to change the emotional expression; finer input should preserve more similarity.

The paper compares this with a no-downsampling pipeline that constructs positive samples using noise masking, duration stretching/contraction, key transposition, and register transposition.

### 3.5 Semi-supervised learning

Training first uses labelled examples with recognition and generation cross-entropy losses. It then uses unlabelled examples: the recognizer supplies an emotion estimate that conditions generation, and the generation loss updates both models. The effective emotion target is defined as:

\[
E_{mo}=(1-\alpha)E_{mo}^{label}+\alpha E_{mo}^{recog},
\quad \alpha=N_{cur}/N_{total}.
\]

This is intended both to use more symbolic music and to reduce the effect of subjective manual annotation.

### 3.6 Data processing

The authors merge eleven open datasets: seven labelled emotion datasets and four unlabelled symbolic datasets. Audio is transcribed to MIDI where necessary; emotion labels are aligned with musical content and BPM. Only 4/4 and 2/4 pieces are retained, clips shorter than four bars are removed, and poor transcriptions are screened out.

The final representation contains 18,201 labelled and 15,591 unlabelled four-bar pieces. Discrete emotions are mapped into a continuous valence-arousal space using Russell’s circumplex model. Dataset-specific ranges are normalized, and the three-dimensional Soundtracks labels are reduced to two dimensions.

### 3.7 Evaluation protocol

The data split is 80% training, 10% test, and 10% validation. The test input consists of 180 popular-song melody sequences, each 60 bars long, paired with fine-grained dynamic emotion sequences.

Objective metrics include:

- **PCC:** change in pitch-consonance score between adjacent segments.
- **CEC:** change in chord-histogram entropy.
- **MCTC:** change in melody-chord tonal distance.
- **Overall coherence:** a fixed-value transform of the three coherence measures, where lower raw differences imply higher reported overall coherence.
- **Similarity:** pitch similarity to the original.
- **Real-time fit:** inverse Euclidean distance between generated and target valence-arousal values.

The baselines are adapted versions of Transformer-GANs-Muhamed, mLSTM-Ferreira, and Music Transformer-Sulun. Thirty participants (15 music professionals and 15 amateurs) rate coherence, transition softness, similarity, and real-time emotion fit.

## 4. Key Results and Benchmarks

### 4.1 Comparison with baselines

Reported objective results are:

| Method | PCC ↓ | CEC ↓ | MCTC ↓ | Overall coherence ↑ | Similarity ↑ | Real-time fit ↑ |
|---|---:|---:|---:|---:|---:|---:|
| TG-Muhamed | 3.62 ± 0.29 | 7.51 ± 0.66 | 1.77 ± 0.13 | 1.10 ± 0.72 | 6.67 ± 0.03 | **2.08 ± 0.71** |
| mL-Ferreira | 3.12 ± 0.13 | 5.09 ± 0.29 | 1.35 ± 0.07 | 4.44 ± 0.32 | 6.91 ± 0.01 | 1.58 ± 0.82 |
| MT-Sulun | 3.38 ± 0.27 | 4.57 ± 0.30 | 1.73 ± 0.16 | 4.32 ± 0.42 | 6.11 ± 0.04 | 1.67 ± 0.08 |
| **REMAST** | **3.04 ± 0.19** | **3.71 ± 0.31** | **1.04 ± 0.09** | **6.21 ± 0.37** | **7.60 ± 0.59** | 2.02 ± 0.74 |

REMAST is best on the three coherence submetrics, transformed overall coherence, and pitch similarity. TG-Muhamed is slightly better on objective valence-arousal fit. Thus the evidence supports a better reported trade-off, not universal dominance on every objective.

Subjective mean scores are:

| Method | Coherence | Softness | Similarity | Real-time fit | Overall |
|---|---:|---:|---:|---:|---:|
| TG-Muhamed | 3.34 | 3.03 | 3.31 | 3.07 | 12.76 |
| mL-Ferreira | 3.86 | 3.31 | 3.76 | 3.10 | 14.03 |
| MT-Sulun | 2.66 | 2.66 | 2.93 | 2.55 | 10.79 |
| **REMAST** | **4.00** | **3.79** | **3.90** | **3.66** | **15.34** |

The authors report statistically significant differences for all subjective metrics with `p < 0.03`; the paper gives limited information about counterbalancing, blinding, effect sizes, or confidence intervals.

### 4.2 Pipeline and fusion ablation

The best combination is downsampling plus Features Concat. It achieves objective coherence 6.21, similarity 7.60, and fit 2.02. Median Emotion gives slightly better subjective softness but lower fit, illustrating the central smoothness–responsiveness trade-off. Without downsampling, objective fit improves in some settings but coherence and similarity decline.

### 4.3 Music-feature ablations

Removing any one of Harmonic Color, Rhythm Pattern, Contour Factor, or Form Factor degrades reported coherence and similarity. Removing semi-supervised learning produces especially poor subjective overall quality, although its objective emotion fit remains relatively high. Bar-level granularity also loses emotional detail compared with beat-level processing.

In the separate emotion-recognition validation, the full model reports average RMSE 0.39, compared with 0.41–0.42 for the four feature ablations. The cross-dataset results are worst for C-WCMED, which the authors attribute to its Western/Chinese classical genre gap.

### 4.4 Latency

For a four-bar, approximately eight-second segment at 120 BPM, generation takes 2.881 ± 0.037 seconds on an Intel Xeon CPU, 2.341 ± 0.083 seconds on Apple M1, and 1.015 ± 0.151 seconds on an RTX 3080 Ti. This is below the segment duration, but the reported timing is generation latency rather than a complete end-to-end measurement including all preprocessing, recognition, rendering, and playback buffering.

### 4.5 Anxiety-relief application

A therapist-designed emotion trajectory is used in a comparison with original songs and real-time recommendation. The reported anxiety-relief scores are 21.60 for REMAST, 12.37 for original songs, and 4.70 for recommendation, with `p < 0.1`. The paper reports that nearly 60% of participants had decreased anxiety after REMAST and that the remaining increases were small.

This is an application result, not a clinical efficacy demonstration: the paper gives limited information about randomization, intervention duration, power, blinding, ethics, and clinical controls.

## 5. Limitations and Future Work

### Limitations

1. **Arrangement rather than streaming composition.** The entire input melody is known after selection. The system adapts arrangement to emotion; it does not yet infer and generate music from a continuously arriving musical stream.
2. **Emotion-label heterogeneity.** Labels from different datasets are mapped into a common valence-arousal space, and some audio is transcribed into MIDI. Both steps may introduce systematic annotation or transcription errors.
3. **Accumulated recognition error.** The method depends on recognizing each previous generated segment. The paper does not provide a detailed stress test of feedback errors or long-horizon drift.
4. **Smoothing can reduce responsiveness.** Median fusion gives smoother transitions but may lag behind a sharp target change. The work selects one operating point rather than reporting a Pareto frontier across identity/similarity, coherence, and target fit.
5. **Similarity is narrow.** Pitch similarity does not establish preservation of motif identity, rhythmic identity, phrase function, formal structure, or listener recognition.
6. **Objective coherence is local.** PCC, CEC, and MCTC measure adjacent-segment changes and may reward conservative smoothing without guaranteeing long-range form, cadence quality, voice-leading, or musical interest.
7. **Evaluation transparency.** The paper does not fully specify source-level separation, baseline tuning, listener order/randomization, or whether the popular-song test material is disjoint from training at the work level.
8. **Therapy claims are preliminary.** The anxiety experiment is encouraging but uses a weak significance threshold and should not be interpreted as evidence of clinical effectiveness.

### Future work stated by the authors

The authors propose incorporating EEG data for real-time emotional resonance and releasing an interactive public website.

### Repository interpretation

REMAST is valuable as a feedback-conditioned arrangement baseline. For explainable symbolic music AI, its four features and fusion state are inspectable inputs, but they are not faithful explanations unless interventions show that changing a stated feature causes the predicted musical change. For symbolic mashups, the same architecture could condition a segment on the preceding segment’s actual harmony, texture, tension, and source-provenance state, but additional measures would be needed for identity and contribution from each source.

## 6. Related Work

- Muhamed et al., **Symbolic Music Generation with Transformer-GANs**, provide the adapted conditional-generation baseline.
- Ferreira and Whitehead, **Learning to Generate Music with Sentiment**, provide the sentiment-conditioned baseline.
- Sulun, Davies, and Viana, **Symbolic Music Generation Conditioned on Continuous-Valued Emotions**, provide the continuous-emotion baseline.
- MuseMorphose is discussed as a fine-grained symbolic style-transfer system, while RL-Duet and SongDriver provide related real-time music-generation context.
- The paper draws on Russell’s circumplex model for valence-arousal representation and on music-theory descriptors for harmony, rhythm, contour, and form.

## 7. Glossary

- **Emotion-based arrangement:** transforming an existing musical input to express a target emotion while retaining some similarity.
- **Valence–arousal (V-A):** a two-dimensional representation of affect, here used as a continuous emotion condition.
- **Harmonic Color:** the paper’s circle-of-fifths-based relative harmonic freshness feature.
- **Contour Factor:** a feature describing pitch extrema, trends, and melodic/chord shape.
- **Form Factor:** cached structural judgments about repetition, transposition, register, and rhythmic variation.
- **Downsampling arrangement:** generating detailed melody and harmony from a coarser representation of the original melody.
- **Soft transition:** a gradual change between emotional states that avoids abrupt perceptual discontinuity.
- **PCC / CEC / MCTC:** local coherence measures for pitch consonance, chord entropy, and melody-chord tonal distance.
