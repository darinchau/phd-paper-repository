---
title: "Audio-to-symbolic Arrangement via Cross-modal Music Representation Learning"
authors: Ziyu Wang, Dejing Xu, Gus Xia, Ying Shan
year: 2022
doi: 10.48550/arXiv.2112.15110
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/wang-2022-audio-to-symbolic-arrangement-via-cross-modal.pdf"
pdf_filename: wang-2022-audio-to-symbolic-arrangement-via-cross-modal.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
---

## One-line Summary

Wang et al. learn a cross-modal audio–symbolic representation that generates a piano accompaniment score from a pop-song audio mix, using staged training to shift texture information from a corrupted score to audio so that inference needs audio only; a 26-subject study rates it above baselines on faithfulness, creativity, naturalness, and musicality.

## 1. Document Information

- **Exact title:** *Audio-to-symbolic Arrangement via Cross-modal Music Representation Learning*. [PDF p. 1]
- **Authors:** Ziyu Wang (NYU Shanghai / Tencent), Dejing Xu (Tencent), Gus Xia (NYU Shanghai), Ying Shan (Tencent). [PDF p. 1]
- **Source record:** arXiv `2112.15110v2` [cs.SD], 22 February 2022, 5 pages; ICASSP 2022 (DOI `10.1109/ICASSP43922.2022.9747884`). [PDF p. 1; OpenAlex record]
- **Length and denominator:** 5/5 pages checked, including Figures 1–3 and the evaluation section.
- **Extraction method:** `pdftotext -layout`; the qualitative figure and rating protocol were read from the text. Figure 3 is a bar chart; its exact values are not printed, so the digest reports only the significance claims.
- **Canonical integrity:** SHA-256 recorded at ingest. Downloaded from `arxiv.org/pdf/2112.15110`.
- **Availability boundary:** code and demos at `https://github.com/ZZWaang/audio2midi` (stated in the paper).

Author-reported claims are the default; repository interpretation is marked.

## 2. Key Contributions

1. **First end-to-end audio-to-symbolic arrangement model** for pop-song accompaniment, as opposed to transcription: the output is a playable piano arrangement, not a note-for-note copy. [§1]
2. **Disentangled cross-modal representation:** chord representation, audio texture, and symbolic texture in a shared latent space, decoded to MIDI. [§3, Fig. 1]
3. **Staged training that removes the symbolic crutch:** initialise as a symbolic-to-symbolic VAE, progressively corrupt the symbolic input, then fine-tune with Gaussian noise or autoregressive past bars, so that only audio is needed at inference. [§3]
4. **Human evaluation** with 26 participants on four criteria. [§4.2]

## 3. Methodology and Architecture

- **Inputs:** audio of a pop-song accompaniment under arbitrary instrumentation. **Output:** a symbolic piano arrangement in MIDI. [§1]
- **Encoders:** a chord extractor (8 × 36 chord progression), a piano transcriber pretrained on MAESTRO (onset/frame/velocity; 3 × 153 × 88), and GRU encoders for audio and symbolic texture; 192-dimensional texture spaces. [§3, Fig. 1]
- **Training stages:** (1) warm-up as a symbolic VAE; (2) pretrain with masked symbolic input and a lead-melody-removed target; (3) fine-tune with increasing corruption or autoregressive conditioning so the model depends on audio. [§3]
- **Model size:** 62M trainable parameters, including 26M in the piano transcriber. [§4.1]

## 4. Key Results and Benchmarks

- **Subjective evaluation:** 26 subjects (8 female, 18 male) rated 5-point scales for faithfulness, creativity, naturalness, and overall musicality. The proposed model is reported significantly better than all baselines on all four criteria; creativity is significantly better than human compositions (p < 0.005). [§4.2, Fig. 3]
- **Baselines:** two supervised audio-to-MIDI decoders (with and without KL loss) and a purely symbolic model. [§4.2]
- **Qualitative:** the model tracks chord changes, bass activity, and groove intensity; swapping the chord or texture latent produces the intended style transfer. [§4.2, Fig. 2]
- **Interpretation:** this is evidence that audio can supply *arrangement-level* information (texture, groove, intensity) that a lead sheet does not contain, but the claim is task-level generation quality, not a controlled measure of what the symbolic model learned.

## 5. Limitations and Future Work

- **Pop piano accompaniment only**, short excerpts (8–16 bars), one instrument family.
- **One-to-many mapping.** The paper acknowledges that one audio mix admits many valid arrangements; the evaluation does not measure diversity or distinguish stylistic choices.
- **Small human study** with a convenience sample; no inter-rater statistics beyond ANOVA confidence intervals.
- **No note-level attribution.** The model cannot say which audio evidence produced which generated note, and there is no conflict/repair evaluation.
- **Transcriber dependence.** The pretrained piano transcriber and chord extractor bound what can be recovered; errors propagate.

## 6. Related Work

- Automatic music transcription: extracts notes, but not a playable arrangement. [§1]
- Piano reduction and cover generation: rule-based or statistical, with loosely coupled analysis and generation. [§1]
- Cross-modal representation learning and disentanglement: the method's direct lineage. [§3]
- MIDI-REPA and cross-modal bootstrapping: later work using symbolic targets to improve audio generation and audio style to control symbolic generation.

## 7. Glossary

- **MIDI:** Musical Instrument Digital Interface.
- **MOS:** Mean Opinion Score (the paper uses 5-point criterion ratings rather than a single MOS).
- **VAE:** Variational Autoencoder.
