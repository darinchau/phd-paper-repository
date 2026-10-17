---
title: "Disentangling Score Content and Performance Style for Joint Piano Rendering and Transcription"
authors: Wei Zeng, Junchuan Zhao, Ye Wang
year: 2025
doi: 10.48550/arXiv.2509.23878
source: zeng-2025-disentangling-score-content-and-performance.md
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/zeng-2025-disentangling-score-content-and-performance.pdf"
pdf_filename: zeng-2025-disentangling-score-content-and-performance.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-16
tags: [expressive-performance-rendering, piano-transcription, content-style-disentanglement, seq2seq, diffusion, style-transfer, alignment-free, probing, ATEPP, ASAP]
---

## Summary

Zeng et al. unify expressive performance rendering (EPR) and automatic performance transcription (APT) — inverse tasks normally studied separately — in one transformer Seq2Seq system. The model separates a note-level score-content latent (shared across score and performance domains) from a single global performance-style vector, and trains on paired and unpaired data using only sequence-level alignment: no note-level score–performance alignment is required. A separately trained diffusion module (PSR) samples style embeddings from score content alone, so a score can be rendered expressively with no user-chosen style. [PDF pp. 1–6]

## Key Contributions

- **Joint EPR+APT model:** four tasks trained together — EPR, APT, masked score reconstruction, masked performance reconstruction — with KL regularization of the style vector toward N(0,I). Content and style are separated by the objective split (content supervised by all tasks; style only conditions performance decoding), not by adversarial training. [PDF pp. 4–5, eqs. 2–6]
- **Alignment-free EPR:** the Seq2Seq formulation removes the note-aligned data dependency of VirtuosoNet/DExter/ScorePerformer-style systems, at a modest APT pitch-accuracy cost. [PDF pp. 2–4, 6–7]
- **PSR module:** a DDPM that generates diverse, stylistically plausible style embeddings conditioned on a global score-content embedding, validated by era-cluster structure matching real-performance style embeddings on 5,003 ATEPP pieces. [PDF pp. 5–6, 9]

## Methodology and Architecture

Five 6-layer transformer components (score/performance/style encoders; score/performance decoders; RoPE, pre-LN, SwiGLU). Style is a CLS-token global vector broadcast-added to content steps in the performance decoder. Training data: ASAP (967 performances, 8:1:1 split matching Beyer & Dai), 75,913 rule-filtered MuseScore scores, and YouTube covers transcribed with aria-amt; ATEPP held out for disentanglement evaluation. 3× A5000, 40k steps. [PDF pp. 4–6, App. A]

## Results

- **APT:** matches the alignment-free SOTA (Beyer & Dai) — slightly worse pitch edit distance (3.08 vs 2.73), better onset/offset deviation, best ScoreSimilarity missing/staff/stem/spelling errors. [Table 1]
- **EPR:** with target styles, best duration/velocity KL (1.16/0.98) and MAE; PSR styles give the best alignment rate (92.27%) and a velocity variance (199.51) close to human (179.04). Subjectively (11 music-trained raters, 5 pieces) Ours-Target rates highest on dynamics/tempo/style/overall, Ours-PSR beats both baselines. [Tables 2–3, Fig. 2]
- **Disentanglement probes (ATEPP):** style→composer 77.46% vs content→composer 29.99%; style→performer 42.07% vs content→performer 9.94%. Style carries composer more than performer — interpreted as pianists aligning expression with composer conventions. Style transfer (3 samples, subjective) succeeds without quality loss, and style-space interpolation rates consistently well. [Table 4, Figs. 3–5]

The disentanglement evidence is probe-based (correlational); the causal test is limited to the 3-sample subjective style-transfer demo. Small rater pools, ASAP-only paired data, preprint status, and no stated code release bound these claims. [PDF pp. 6–9]

## Related Papers

- [[concepts/work-identity-versus-performance-variation]] — defining synthesis anchor: this paper's content/style split is the score-grounded, generative counterpart of Chen et al.'s representation-level factorization.
- [[explainability-and-auditability/chen-2026-dual-contrastive-sparse-autoencoders]] — same content/interpretation distinction recovered from a frozen generator's internals rather than built into an encoder.
- [[generation-and-planning/borovik-2025-symupe-affective-and-controllable]] — concurrent EPR model requiring note-aligned data and text/emotion control; Zeng et al. cite ScorePerformer (same first author lineage) as alignment-dependent.
- [[data-and-representation/jung-2025-unified-cross-modal-translation-of]] — unified multi-task translation across score/performance modalities.
- [[overviews/2026-symbolic-music-literature-map]] — batch synthesis anchor.
