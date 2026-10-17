---
title: "Disentangling Score Content and Performance Style for Joint Piano Rendering and Transcription"
authors: Wei Zeng, Junchuan Zhao, Ye Wang
year: 2025
doi: 10.48550/arXiv.2509.23878
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/zeng-2025-disentangling-score-content-and-performance.pdf"
pdf_filename: zeng-2025-disentangling-score-content-and-performance.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-16
---

## One-line Summary

Zeng et al. train one transformer Seq2Seq system that jointly performs expressive performance rendering (EPR) and automatic performance transcription (APT) by disentangling note-level score content from a single global performance-style vector, trained with sequence-level alignment only, plus a diffusion-based Performance Style Recommendation (PSR) module that synthesizes style embeddings from score content alone; results are competitive with alignment-based baselines and the style space provably carries composer (77.5%) and performer (42.1%) identity, but the paper is a preprint with small subjective studies and no code/data release.

## 1. Document Information

- **Exact title:** *Disentangling Score Content and Performance Style for Joint Piano Rendering and Transcription*. [PDF p. 1]
- **Authors:** Wei Zeng, Junchuan Zhao, Ye Wang (National University of Singapore); Ye Wang is the corresponding author. [PDF p. 1]
- **Source record:** arXiv `2509.23878v1` (cs.SD, 28 Sep 2025), 30 physical PDF pages (main pp. 1–9, references pp. 10–11, appendices pp. 12–30). Preprint; the PDF names no venue. Third-party aggregators list it as an ICLR 2026 submission — unverified, and the PDF itself claims nothing. DOI recorded as the arXiv resolver `10.48550/arXiv.2509.23878`. [PDF p. 1; aggregator claim flagged as unverified]
- **Length and denominator:** 30 physical PDF pages. This digest checked the main body (pp. 1–9), appendix A.1–A.2 (data filtering and representation), and sampled the transcription-visualization appendices (score-typeface figures at pp. 27–30 that extract poorly by design); score-notation figures were not visually verified. **Denominator: main text and method appendices fully read; typeset-score appendices (pp. ~25–30) not visually inspected.**
- **Extraction method:** full PDF extracted with PyMuPDF (UTF-8). Tables 1–4 verified against the extraction. Appendix score figures are music glyphs and render as symbol soup in text; nothing quantitative rests on them.
- **Canonical integrity:** SHA-256 `7d1c82ed512164d16f19d237c814c8e15d70efbb878bac5c21dc788ecdbc4d3d`. Downloaded from `arxiv.org/pdf/2509.23878`.
- **Availability boundary:** demos at `jointpianist.github.io/epr-apt/`; no code, checkpoint, or dataset release is stated in the PDF. Unpaired score data is 75,913 public-domain MuseScore MusicXML files (filterable per App. A.1); unpaired performances come from YouTube piano covers transcribed with the aria-amt model.

This digest distinguishes author-reported claims (default), values verified against the extraction (marked), and repository interpretation.

## 2. Key Contributions

1. **Unified EPR + APT model** — a single transformer that renders scores to expressive performances and transcribes performances back to scores, exploiting the tasks' duality for mutual supervision; trained on paired and unpaired data with no note-level alignment. [PDF pp. 1–2, 4]
2. **Content/style disentanglement** — note-level score-content representations from both domains share a latent space, while a single global style vector (CLS token of a style encoder, KL-regularized to N(0,I)) conditions the performance decoder. [PDF pp. 4–5]
3. **PSR module** — a DDPM that samples style embeddings conditioned on a global score-content embedding, imitating a pianist choosing an interpretation from the score; enables fully automatic and diverse rendering. [PDF pp. 1–2, 5–6]

## 3. Methodology and Architecture

- **Representation:** score notes as K=7 discrete attributes, performance notes as K=4 (App. A.2); note embedding = sum of attribute embeddings. Score output uses the Beyer & Dai (2024) tokenization; performance output uses the REMI-like structured representation of Huang & Yang (2020) via MidiTok. [PDF pp. 3–4, App. A.2]
- **Four joint tasks:** EPR (`ŷ = gY(zx ⊕ zs)`, style broadcast-added to each content step), APT (`x̂ = gX(zy)`), masked score reconstruction, and masked performance reconstruction (⟨MASK⟩ token corruption); paired CE losses + unpaired reconstruction losses + KL regularization (eqs. 2–6). Content/style separation is encouraged by the objective split (content supervised by all tasks; style only enters performance decoding) rather than by an adversarial term. [PDF pp. 4–5]
- **Architecture:** five transformer components (score/performance/style encoders; score/performance decoders), each 6 layers, 8 heads, RoPE, pre-LN, SwiGLU, FFN 3072. [PDF p. 5]
- **PSR:** separate score encoder with CLS global embedding e_g; DDPM noise-prediction head conditioned on (e_g, noisy z_s, sinusoidal t); trained against style vectors extracted from the frozen joint model. [PDF pp. 5–6, eqs. 7–8]
- **Data:** ASAP, 967 curated performances, 8:1:1 split matching Beyer & Dai; unpaired 75,913 MuseScore scores (rule-filtered: 2 staves, ≥100 notes, ≥10 bars, ≤64 notes/bar, plausible time/key signatures, App. A.1) and YouTube-cover performances transcribed with a state-of-the-art audio-to-MIDI model (aria-amt); ATEPP (11,674 performances, 49 pianists, 25 composers) used only for OOD disentanglement evaluation. Era labels for the PSR analysis were parsed with GPT-4o mini. [PDF pp. 6, App. A.1]
- **Training:** 3× A5000, batch 144×256-note sequences (36 per task), 40k steps, AdamW, cosine decay with 4k warmup, peak 5e-5; PSR trained separately (batch 48, peak 1e-4). [PDF p. 6]

## 4. Key Results and Benchmarks

- **APT (Table 1, ASAP):** roughly matches the end-to-end SOTA (Beyer & Dai) — slightly worse pitch edit distance (Ep 3.08 vs 2.73) but better onset/offset deviation (16.26/27.30 vs 17.48/32.92) and best-in-table ScoreSimilarity missing-note (9.48), staff (51.75), stem (9.43), and spelling (6.24) errors. Aligned-supervision systems (Liu et al., Shibata et al.) retain lower pitch errors. [PDF p. 6, Table 1]
- **EPR objective (Table 2):** with ground-truth target styles, Ours-Target has the best duration/velocity KL (1.16/0.98) and MAE (0.55/9.21); velocity variance 120.19 (Ours-Target) and 199.51 (Ours-PSR) bracket the human 179.04, while DExter's larger 326.33 is attributed by the authors to unstable dynamics, not expressiveness. [PDF p. 7, Table 2]
- **EPR accuracy (Table 3):** Ours-PSR achieves the best alignment rate (92.27%) and lowest insertion rate (3.77%); Ours-Target has the worst missing rate (4.32%). [PDF p. 7, Table 3]
- **Subjective (Fig. 2):** 11 music-trained participants, 5 pieces (Bach, Rachmaninoff, Schubert, Scriabin, Ravel), 5-point Likert on dynamics/tempo/style/overall. Ours-Target is highest on every attribute, Ours-PSR follows and beats both baselines; strongest on Bach and Scriabin. [PDF pp. 6–7, Fig. 2]
- **Disentanglement probes (Table 4, ATEPP):** style→composer 77.46% vs content→composer 29.99%; style→performer 42.07% vs content→performer 9.94%. The style vector carries both composer and performer identity; the residual composer information in content is attributed to composer-specific structural fingerprints. The dominant composer signal in style is interpreted as pianists aligning expression with the composer's conventions. [PDF pp. 8–9, Table 4]
- **Style transfer (Fig. 5, subjective, 3 samples):** transferring a reference style (Target) gives the highest style-similarity ratings in samples 1 and 3 without quality loss; interpolated styles (Mean) rate consistently high, indicating a smooth style space. [PDF p. 9]
- **PSR validity (Fig. 4):** on 5,003 ATEPP performances, 2D projections of PSR-generated style vectors cluster by historical era (Baroque/Classical/Romantic/Modern) with centroids matching those of style vectors extracted from real performances. [PDF p. 9]

## 5. Limitations and Future Work

- Alignment-free training costs some APT pitch accuracy versus note-aligned baselines; the authors frame this as a flexibility trade-off for ornaments/trills rather than a win. [PDF pp. 6–7]
- Performer information is recovered from style at only 42.07% and remains entangled with repertoire and arrangement; the paper does not claim performer-level style transfer. [PDF pp. 8–9]
- Subjective studies are small (11 raters; 3 style-transfer samples); no statistical tests or confidence intervals are reported for Figures 2 and 5. [PDF pp. 6–9]
- Paired training data is ASAP-only (≈960 performances); unpaired web sources are unverified quality; era labels depend on GPT-4o-mini parsing. [PDF pp. 6, 9]
- No code or checkpoint release stated; the paper is a preprint with no peer-reviewed venue at extraction time. [PDF p. 1]
- Repository inference: the disentanglement evidence is correlational (probe accuracy); no intervention test (e.g., swapping style vectors and measuring perceptible style change with controlled raters) isolates the causal role of z_s beyond the 3-sample transfer demo.

## 6. Related Work

Builds on Beyer & Dai (2024) for alignment-free Seq2Seq piano transcription, VirtuosoNet and DExter as EPR baselines, Zhang & Dixon (2023) for unsupervised content/style separation from performances, and the ASR/TTS joint-modeling tradition. Cites Borovik & Viro (2023) (ScorePerformer) as an alignment-dependent control system. [PDF pp. 2–3]

## 7. Glossary

- **EPR / APT:** expressive performance rendering (score → expressive performance MIDI) and automatic (performance) transcription (expressive MIDI → score).
- **PSR:** Performance Style Recommendation — the DDPM module that samples a style embedding from score content.
- **Content representation (z_x, z_y):** note-level latent sequence capturing pitch/rhythm structure, shared across score and performance domains.
- **Style representation (z_s):** single global latent vector summarizing a performance's expressive character, KL-regularized toward N(0,I).
- **DDPM:** denoising diffusion probabilistic model used to generate style embeddings.
- **MUSTER / ScoreSimilarity:** APT evaluation suites covering rhythmic alignment and notation-level errors.
- **ATEPP:** Aligned Topic (sic) — a large transcribed expressive piano performance dataset with performer/composer labels, used here only for evaluation.
