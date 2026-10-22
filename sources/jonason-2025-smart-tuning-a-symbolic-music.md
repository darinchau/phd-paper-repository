---
title: "SMART: Tuning a symbolic music generation system with an audio domain aesthetic reward"
authors: Nicolas Jonason, Luca Casini, Bob L. T. Sturm
year: 2025
doi: 10.48550/arXiv.2504.16839
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/jonason-2025-smart-tuning-a-symbolic-music.pdf"
pdf_filename: jonason-2025-smart-tuning-a-symbolic-music.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
---

## One-line Summary

SMART fine-tunes a piano MIDI generator with GRPO using Meta Audiobox Aesthetics scores of rendered audio as the reward, raising listener ratings by about 1.22 points on a 10-point scale in a 14-participant pilot while aggressive optimisation collapses output diversity.

## 1. Document Information

- **Exact title:** *SMART: Tuning a symbolic music generation system with an audio domain aesthetic reward*. [PDF p. 1]
- **Authors:** Nicolas Jonason, Luca Casini, Bob L. T. Sturm (KTH Royal Institute of Technology); Jonason and Casini equal contribution. [PDF p. 1]
- **Source record:** arXiv `2504.16839v1` [cs.SD], 23 April 2025, 11 pages. Preprint; no venue printed. DOI recorded as the arXiv resolver. [PDF p. 1]
- **Length and denominator:** 11/11 pages checked, including the main text, Figures 3–7, Tables 1–4, and the appendix soundfont list.
- **Extraction method:** `pdftotext -layout`; ratings and test statistics cross-checked against the text.
- **Canonical integrity:** SHA-256 recorded at ingest. Downloaded from `arxiv.org/pdf/2504.16839`.
- **Availability boundary:** demo page linked in the abstract; no code or checkpoint release is stated.

Author-reported claims are the default; repository interpretation is marked.

## 2. Key Contributions

1. **Audio-reward tuning for symbolic music.** Renders MIDI generations to audio, scores them with an audio aesthetic model, and optimises the symbolic generator with Group Relative Policy Optimisation (GRPO). [§3]
2. **Behavioural characterisation.** Reports shifts in note count, polyphony, empty-beat rate, pitch range, and velocity distribution after tuning. [§5.1]
3. **Preliminary human evidence.** A 14-participant listening study finds a significant positive effect (p = 0.002; +1.22 rating points). [§4]
4. **Over-optimisation warning.** Longer optimisation raises the proxy reward while visibly collapsing diversity. [§5.2, Fig. 6]

## 3. Methodology and Architecture

- **Base model:** a piano MIDI model trained from scratch on a large MIDI corpus; the reference policy is the frozen base model. [§3.1]
- **Reward:** Meta Audiobox Aesthetics (MAA) ratings of audio rendered from each sampled MIDI, using a fixed soundfont (Yamaha; soundfont comparison in Table 2). [§3.3]
- **Optimisation:** GRPO; 200 steps for the main condition, β = 0.04; a 1000-step, β = 0.0 condition probes over-optimisation. [§3.2, §5.2]
- **Evaluation:** 1000 procedurally prompted generations for feature statistics; MAA ratings; a 14-participant listening study with 407 usable ratings, analysed with a linear mixed-effects model. [§4, §5]

## 4. Key Results and Benchmarks

- **Listener ratings:** SMART outputs are rated higher than base outputs; the mixed-effects model gives p = 0.002 and an average increase of about 1.22 points. This is a small convenience-sample pilot, not a population estimate. [§4]
- **Feature shifts:** more notes, higher polyphony, zero empty beats, wider pitch range and velocity set, lower mean velocity; listeners describe fewer pauses and more dynamics. [§5.1]
- **Proxy validity warning:** post-tuning MAA scores often exceed MAA scores of real piano performances, which the authors read as evidence that MAA is an imperfect proxy rather than that the model surpasses humans. [§5.1, Table 1]
- **Diversity collapse:** 1000-step optimisation increases MAA reward while average piano rolls become visibly repetitive. [§5.2, Fig. 6]
- **Interpretation:** an audio-domain signal can steer symbolic generation, but the paper measures output aesthetics, not what the symbolic model internally learned, and provides no attribution of which notes caused the reward.

## 5. Limitations and Future Work

- **Proxy reward, not perception.** MAA predicts average aesthetic ratings; it ignores listener dependence and can be gamed.
- **Small human study.** 14 participants, 407 ratings, convenience sample; no expert stratification.
- **Piano only, short generations.** No multi-instrument or long-form test.
- **No representation analysis.** The intervention changes outputs, not necessarily the model's symbolic knowledge; there is no probe, no note-level attribution, and no test of whether the effect transfers beyond the reward model's biases.
- **Diversity–reward trade-off.** The paper documents collapse but does not propose a mitigation beyond stopping earlier.

## 6. Related Work

- MusicRL (Cideron et al. 2024): RL from human preference comparisons for audio generation.
- NotaGen: symbolic RL fine-tuning with a CLaMP 3 embedding-distance reward.
- RaveForce: audio-rendered rewards for symbolic agents, an earlier precedent.
- MIDI-REPA (Yu et al. 2026): the reverse intervention, aligning audio-generation layers to symbolic targets.

## 7. Glossary

- **GRPO:** Group Relative Policy Optimisation.
- **MAA:** Meta Audiobox Aesthetics.
- **MIDI:** Musical Instrument Digital Interface.
- **RL:** Reinforcement Learning.
