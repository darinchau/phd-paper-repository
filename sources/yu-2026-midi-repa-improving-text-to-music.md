---
title: "MIDI-REPA: Improving Text-to-Music Generation with Symbolic Representation Alignment"
authors: Song-Ze Yu, Fang-Duo Tsai, Yi-Hsuan Yang
year: 2026
doi: 10.48550/arXiv.2610.20967
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/yu-2026-midi-repa-improving-text-to-music.pdf"
pdf_filename: yu-2026-midi-repa-improving-text-to-music.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-22
---

## One-line Summary

MIDI-REPA aligns the intermediate layers of a 122M flow-matching text-to-music DiT to AMT-derived piano rolls, showing that symbolic supervision improves audio generation and that early-layer alignment across the full flow trajectory works best, at 14.2 A100-equivalent GPU-hours.

## 1. Document Information

- **Exact title:** *MIDI-REPA: Improving Text-to-Music Generation with Symbolic Representation Alignment*. [PDF p. 1]
- **Authors:** Song-Ze Yu (National Taiwan University), Fang-Duo Tsai (NTU / UC San Diego), Yi-Hsuan Yang (NTU). [PDF p. 1]
- **Source record:** arXiv `2610.20967v1` [cs.SD], 14 October 2026, 5 pages, submitted to ICASSP 2027. DOI recorded as the arXiv resolver. [PDF p. 1; arXiv metadata]
- **Length and denominator:** 5/5 pages checked, including Tables 1–5 and Figures 1–2. No appendix.
- **Extraction method:** `pdftotext -layout`; table values cross-checked against the extracted text.
- **Canonical integrity:** SHA-256 recorded in the registry log at ingest. Downloaded from `arxiv.org/pdf/2610.20967`.
- **Availability boundary:** code, JamendoMIDI pipeline, and audio samples advertised at `https://midi-repa.vaclis.net`. No listening test is reported.

Author-reported claims are the default below; repository interpretation is marked.

## 2. Key Contributions

1. **Symbolic representation alignment for audio generation.** An auxiliary cosine-similarity loss pulls a DiT hidden state toward a time-aligned symbolic target, on top of the flow-matching objective; λ = 0.5. [§2.1, Eq. 1]
2. **A design study of what, where, and when to align.** Compares AMT teachers (Basic Pitch, MuScriptor), target representations (merged piano roll vs 7-instrument cube), DiT layers (L0–L11), and flow-timestep intervals. [§3]
3. **JamendoMIDI.** AMT applied to 55,701 vocal-removed Jamendo tracks; 51,077 usable, 49,034 used for training (3,161 hours). [§2.2.3]
4. **Efficiency claim.** Competitive or better ATTM objective scores with a 122M backbone at 14.2 A100-equivalent GPU-hours, versus 190.3 for the baseline. [Table 4]

## 3. Methodology and Architecture

- **Backbone:** FluxAudio-S, the 122M official baseline of the 2026 ICME Academic Text-to-Music Challenge; T5 + CLAP conditioning; 12 MMDiT blocks (four joint audio/text, eight fused); frozen SAME-L audio autoencoder; 10 s audio → 108 frames × 256 channels. [§2.2.1]
- **Symbolic target:** AMT output converted to binary time-pitch; MuScriptor merged roll (108 × 88) or a 7-family instrument cube (108 × 88 × 7). Basic Pitch is the instrument-agnostic alternative. [§2.2.2]
- **Alignment:** a one-layer temporal convolution projects hidden state `h_{t,l}` to the symbolic space; loss is negative cosine similarity on frames with symbolic activity; total loss `L_flow + λ L_REPA`. Training only; no symbolic input at inference. [§2.1]
- **Training:** AdamW, batch 128, 300k updates, lr 1e-4, 1k warm-up, EMA; 25 Euler steps and CFG 4.5 at sampling. [§2.2.3]

## 4. Key Results and Benchmarks

- **Teacher choice (Table 1, SDD):** MuScriptor merged roll gives FAD 0.5040 / CLAP 0.2603, versus baseline 0.5275 / 0.2220; the 7-family cube gives 0.5117 / 0.2665. **Basic Pitch roll is worse than no alignment on FAD (0.5363)**, showing that noisy symbolic supervision can hurt. [Table 1]
- **Layer choice (Table 3):** alignment improves CLAP at every tested block and FAD everywhere except L0; L2 is best overall (FAD 0.4947, CLAP 0.2686); deeper layers are weaker. [Table 3]
- **Timestep interval (Table 5):** aligning over the full trajectory is best; restricting to late or early windows loses either FAD or CLAP. [Table 5]
- **ATTM benchmark (Table 4, 80 in-domain prompts):** rank 1 by Borda over 17 official systems plus the baseline; FAD 0.497, CLAP 0.315, CCS 0.829; 14.2 A100-equivalent GPU-hours. The baseline scores FAD 0.495, CLAP 0.295, CCS 0.804 at 190.3 A100-equivalent hours. [Table 4]
- **Interpretation:** the gain is not a uniform metric win (FAD is essentially tied with the baseline), but prompt adherence (CLAP) and the composite CCS improve at a fraction of the compute; the authors' headline is efficiency plus symbolic supervision, not audio-quality dominance.

## 5. Limitations and Future Work

- **One direction only (symbolic → audio).** The paper does not ask what audio supervision teaches a symbolic model; it uses symbolic content to regularise an audio generator.
- **AMT-derived teacher.** The symbolic target inherits transcription errors; the Basic Pitch result shows this matters. The 7-family instrument mapping is coarse.
- **Objective metrics only.** No listening test; FAD and CLAP are known imperfect proxies. The benchmark is 80 in-domain prompts from one challenge setup.
- **Task scope.** Instrumental text-to-music, 10 s windows, one 122M backbone; no long-form or symbolic-output evaluation.

## 6. Related Work

- REPA and iREPA: representation alignment as a training signal for generative models. [§1, §2.1]
- MERT, CLAP, MuQ: audio-encoder alignment targets; the paper argues these align to learned audio representations rather than structured musical content. [§1]
- MusicFM, MERT, CLaMP 3: audio and cross-modal music encoders in this repository.
- SMART (Jonason et al. 2025): the mirror intervention, where a rendered-audio reward tunes a symbolic generator.

## 7. Glossary

- **AMT:** Automatic Music Transcription.
- **ATTM:** Academic Text-To-Music Challenge.
- **CFG:** Classifier-Free Guidance.
- **CLAP:** Contrastive Language–Audio Pretraining.
- **DiT:** Diffusion Transformer.
- **FAD:** Fréchet Audio Distance.
- **MIDI:** Musical Instrument Digital Interface.
- **REPA:** Representation Alignment for generative models.
- **SDD:** Song Describer Dataset.
