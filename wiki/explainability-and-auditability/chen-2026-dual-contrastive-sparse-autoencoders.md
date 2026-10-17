---
title: "Dual-Contrastive Sparse Autoencoders Reveal Features of Musical Interpretation"
authors: Jan Chen, Manuel Cherep, Pattie Maes, Nikhil Singh
year: 2026
doi: ""
source: chen-2026-dual-contrastive-sparse-autoencoders.md
category: explainability-and-auditability
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/chen-2026-dual-contrastive-sparse-autoencoders.pdf"
pdf_filename: chen-2026-dual-contrastive-sparse-autoencoders.pdf
source_collection: openreview
source_format: pdf
extracted_date: 2026-10-16
tags: [sparse-autoencoders, mechanistic-interpretability, MusicGen, disentanglement, probing, steering, work-identity, performance-variation, performer-identity, workshop-paper]
---

## Summary

DC-SAE asks the musicological question — which features of a performance belong to the *work* and which to its *interpretation* — as a representation-factorization problem on a frozen generative music transformer. Two parallel TopK sparse autoencoders (width 32,768 each, k=50, shared decoder; 268.5M parameters) are trained on MusicGen-Large layer-24 activations with a dual-contrastive objective whose pivot sets are **same-work different-recording windows**: those pivots are positives for the work-identity branch z_i (against different-work negatives) and negatives for the performance-variation branch z_j (whose positive is an augmented view of the same recording). One metadata source — the work id — thus supplies both directions of disentangling pressure. Across classical, jazz-standard, and pop-cover corpora, probes show z_i classifies held-out recordings of classical works at 0.856 (chance 0.020) where a vanilla SAE reaches 0.508 and MERT 0.492; z_j retains same-recording and (emergent, unsupervised) performer information that survives a held-out recording-condition shift; and steering along a rank-1 z_j feature direction moves 10 s MusicGen continuations toward a target performer's realization of the same work in 70% of paired contexts. [PDF pp. 1–4]

## Key Contributions

- **DC-SAE architecture and objective:** two-branch TopK SAE with shared decoder; `L = L_rec + α_i L_zi + α_j L_zj` with MIL-NCE identity and InfoNCE variation terms (τ=0.1); pivots ranked by MERT similarity. [PDF pp. 2–3, eqs. 1–9]
- **Factorization evidence:** held-out work-classification, augmented same-recording, and cross-work performer probes across three traditions. [PDF pp. 3–4, Tables 1–2, App. M]
- **Audited interpretation features:** e.g., f59100 "expressivo/rubato piano (Romantic-leaning, especially Chopin)", f3876 "fast jazz piano improv", f48506 "cinematic orchestral/choral" — with tradition-specific content matching the thickness of each tradition's work-identity notion. [PDF pp. 3, 9, Table 9]
- **Steering proof of concept:** rank-1 z_j direction injection at layer 24; beats matched-random on MERT target-margin gain in 70.0% of paired contexts; the non-interpretable residual reference is 73.8%, so a single named feature recovers most of the available movement. [PDF p. 4, Table 3, App. K]

## Methodology and Architecture

Cohorts: top-100 classical works (Wikidata–MusicBrainz/IMSLP manifest, 101.2 h), top-100 jazz standards (iReal Pro, 75.6 h), top-100 SHS100K cover families (58.7 h). MusicGen-Large activations (30 s windows, R^1501×2048); 100 stratified token positions per window; hierarchical batches 16 works × 5 performances × 4 windows; 5,000 steps (1,000 recon burn-in, 1,000 contrastive ramp) on one H200. Performer labels are loaded only at evaluation. [PDF pp. 2, 8–9, Tables 7–8]

## Results

| Probe (chance) | Classical | Jazz | SHS100K |
|---|---:|---:|---:|
| Work ID, z_i (0.020) | **0.856** | 0.136 | 0.368 |
| Work ID, vanilla SAE | 0.508 | 0.128 | 0.232 |
| Work ID, MERT | 0.492 | 0.076 | 0.148 |
| Same-recording aug., z_j (0.500) | 0.670 | 0.712 | 0.638 |
| Same-recording aug., MERT | 0.501 | 0.513 | 0.502 |
| Cross-work performer, z_j (0.013–0.026) | 0.218 | 0.257 ([z_i;z_j]) | 0.253 ([z_i;z_j]) |

DC-SAE also places 4.85–5.65× more features in the 1–25% prevalence audit band than the vanilla SAE. Limitations acknowledged by the authors: small absolute steering effects; MERT used both for pair selection and scoring (mitigated by a CLAP check); jazz-standard identity separates weakly because standards are realized flexibly; performer structure is entangled with repertoire; the account is MusicGen-internal. Code is not yet public (App. H) and the audio demo bucket was dead at extraction time. [PDF pp. 3–4, Tables 1–3, Apps. H, K]

## Related Papers

- [[concepts/work-identity-versus-performance-variation]] — defining synthesis anchor for the work/interpretation distinction across generative and interpretability approaches.
- [[concepts/music-theory-probing]] — the recoverable/causal/useful evidence ladder applied to this paper: probing rows are recoverability; steering is its intervention evidence.
- [[explainability-and-auditability/pocwiardowski-2026-mi-midi-mechanistic-interpretability-of]] — symbolic-side probing and bidirectional steering; DC-SAE is the audio-side, corpus-structured counterpart.
- [[generation-and-planning/zeng-2025-disentangling-score-content-and-performance]] — the same content/interpretation split trained into a symbolic EPR system; cited by DC-SAE.
- [[explainability-and-auditability/wei-2024-do-music-generation-models-encode]] — probing precedents on MusicGen features with handcrafted-baseline caveats.
- [[overviews/2026-symbolic-music-literature-map]] — batch synthesis anchor.
