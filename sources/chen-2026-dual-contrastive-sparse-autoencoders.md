---
title: "Dual-Contrastive Sparse Autoencoders Reveal Features of Musical Interpretation"
authors: Jan Chen, Manuel Cherep, Pattie Maes, Nikhil Singh
year: 2026
doi: ""
category: explainability-and-auditability
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/chen-2026-dual-contrastive-sparse-autoencoders.pdf"
pdf_filename: chen-2026-dual-contrastive-sparse-autoencoders.pdf
source_collection: openreview
source_format: pdf
extracted_date: 2026-10-16
---

## One-line Summary

Chen, Cherep, Maes, and Singh train DC-SAE, a two-branch TopK sparse autoencoder on MusicGen-Large layer-24 activations, whose dual-contrastive objectives use same-work different-recording "pivot" windows to factor the residual stream into a work-identity branch and a performance-variation branch; probes show the identity branch classifies held-out recordings of classical works at 0.856 (chance 0.020), the variation branch carries emergent performer signal without supervision, and steering along rank-1 variation features moves generations toward a target interpretation in 70% of paired contexts — a proof-of-concept workshop result with small absolute effects, evaluation-metric circularity, and no public code at extraction time.

## 1. Document Information

- **Exact title:** *Dual-Contrastive Sparse Autoencoders Reveal Features of Musical Interpretation*. [PDF p. 1]
- **Authors:** Jan Chen (TU Munich / MIT), Manuel Cherep (MIT), Pattie Maes (MIT), Nikhil Singh (Dartmouth); Chen and Cherep marked equal contribution. [PDF p. 1]
- **Source record:** OpenReview forum `xj0pDqfogb`; virtual poster at the Mechanistic Interpretability Workshop @ ICML 2026; author pages also list the paper as NeurIPS 2026. No DOI printed. The OpenReview PDF could not be fetched over this network (OpenReview blocks the egress IP); the ingested PDF is the user-supplied download `534_Dual_Contrastive_Sparse_Au (1).pdf`, whose content matches the official workshop poster (534.pdf) and the workshop-site abstract. Identity confirmed: **this is the "DC-SAE" of musical interpretation, not the "DC-SAE: Deep Compression Semantic Autoencoder" (arXiv 2609.39222) image tokenizer**. [PDF p. 1; poster PDF; mechinterpworkshop.com posters page]
- **Length and denominator:** 14 physical PDF pages (main pp. 1–4, references pp. 5–6, appendices A–M pp. 7–14). This digest checked **14/14 pages**, including the audited feature gallery (App. I), training hyperparameters (App. F), compute (App. G), release statement (App. H), intervention tables (App. K), and probe methodology (App. M).
- **Extraction method:** full PDF extracted with PyMuPDF (UTF-8); Tables 1–3, 7, 9–12 verified against the extraction. Table 2's continuation and the same-recording rows were cross-checked across page breaks.
- **Canonical integrity:** SHA-256 `25b46ee462564724eab9c1daf6ae9961e6b70ebbe08f1b6091282dbfe7c21b00`. Provenance: user-supplied copy of the OpenReview PDF; not independently re-downloadable from this network.
- **Availability boundary:** Appendix H states the code/data package is **not yet public** (intended release with Hydra configs, checkpoints, manifests). The audio demo bucket (`storage.googleapis.com/dc-sae-musicgen-listening`) was checked and returns a closed-billing-account error — the demos referenced in §4 are currently inaccessible. Reproducibility therefore cannot yet be externally verified.

This digest distinguishes author-reported claims (default), values verified against the extraction (marked), and repository interpretation.

## 2. Key Contributions

1. **DC-SAE architecture** — two parallel TopK SAE branches sharing one linear decoder over concatenated codes, trained with a dual-contrastive objective that uses coarse work-level metadata only. [PDF pp. 1, 2–3]
2. **Empirical factorization evidence** — work-identity and performance-variation branches separate by held-out probes across classical, jazz-standard, and pop-cover corpora. [PDF pp. 3–4]
3. **Interpretable interpretation features** — an audited gallery of variation-branch features (e.g., f59100 "expressivo/rubato piano", f3876 "fast jazz piano improv"). [PDF pp. 3–4, App. I]
4. **Generation-time steering proof of concept** — injecting a rank-1 variation-feature decoder direction at layer 24 shifts MusicGen continuations toward a target performer's realization of the same work. [PDF pp. 4, App. K]

## 3. Methodology and Architecture

- **Setting:** frozen MusicGen-Large (3.3B params); residual-stream activations at layer 24; 30 s windows → x ∈ R^1501×2048. [PDF p. 2]
- **Cohorts:** Classical (top-100 works from a reviewed 1,500-piece Wikidata–MusicBrainz/IMSLP manifest, 101.2 h), Jazz (top-100 most-played iReal Pro standards, 75.6 h), SHS100K (top-100 cover-song families, 58.7 h). [PDF p. 2]
- **Pivot construction:** for each anchor window, same-work different-recording candidates are ranked by MERT-v1-330M cosine similarity; top-κ retained as the pivot bag. Pivots play a dual role: positives for the identity objective, negatives for the variation objective. [PDF pp. 2–3]
- **Architecture:** two TopK SAE encoders (width 32,768 each, k=50), shared decoder R^65536 → R^2048; 67.1M params per branch encoder, 134.2M decoder, 268.5M total. [PDF p. 8, Table 7]
- **Objective:** `L = L_rec + α_i L_zi + α_j L_zj`. L_zi: multi-positive MIL-NCE (temperature 0.1) pulling z_i toward same-work pivots against 64 different-work negatives. L_zj: InfoNCE with a deterministic acoustic augmentation of the same audio as the positive **and the same-work pivots as negatives** — the pivotal design choice, forcing z_j to encode recording/performance-level rather than work-level information. Reconstruction is computed only on the clean anchor. [PDF pp. 2–3, eqs. 2–9]
- **Training:** token-level; 100 stratified token positions per window; hierarchical batches (16 works × 5 performances × 4 windows); 5,000 steps with 1,000 recon-only burn-in and 1,000-step contrastive ramp; AdamW lr 1e-4; single H200 per run. [PDF pp. 8–9, Tables 7–8]
- **Evaluation probes (App. M):** raw balanced logistic regression on recording means; work identity = 50 closed classes with 5 extra held-out recordings per work (chance 0.020); same-recording = balanced pairs within the same work (chance 0.500); performer = grouped work-holdout cross-validation, performer labels loaded only at evaluation. Nuisance recipe (codec roundtrip, EQ/filtering, colored noise, hum, gain) held out from training. [PDF pp. 3, 10–14]

## 4. Key Results and Benchmarks

- **Work identity (Table 1):** z_i classifies held-out recordings at 0.856 (Classical), 0.136 (Jazz), 0.368 (SHS100K) vs vanilla SAE 0.508/0.128/0.232, MERT 0.492/0.076/0.148, CLAP 0.048/0.032/0.048. Classical separates decisively; jazz standards separate weakly (authors attribute this to the flexible realization of standards); on Jazz the concatenation [z_i;z_j] is slightly higher than z_i alone. [PDF p. 3, Table 1]
- **Feature prevalence:** in the 1–25% active-prevalence audit band, DC-SAE retains 4.85–5.65× more features than the vanilla SAE across the three corpora — the contrastive structure redistributes capacity into the interpretable band rather than only ultra-rare or ubiquitous features. [PDF p. 3, Fig. 2]
- **Same-recording robustness (Table 2):** under the held-out augmentation recipe, MERT and CLAP collapse to chance (0.500) on the same-recording probe while z_j stays at 0.670 (Classical), 0.712 (Jazz), 0.638 (SHS100K) — z_j retains realization-specific information that survives recording-condition shift, unlike the dense encoders. [PDF pp. 3–4, Table 2]
- **Emergent performer structure (Table 2):** cross-work performer probes (labels never used in training; chance 0.013–0.026): z_j 0.218 Classical; [z_i;z_j] 0.259 Jazz and 0.322 SHS100K — above MERT and CLAP on all three. The authors interpret this as emergent performer-related structure, still entangled with repertoire, arrangement, and recording context. [PDF p. 4, Table 2]
- **Steering (Table 3, App. K):** injecting the rank-1 z_j feature direction during a 10 s continuation beats a matched-random control on MERT target-margin gain in 70.0% of paired contexts (Classical 75.0%, Jazz 62.5%, SHS100K 68.8%) — the best interpretable system, though the non-interpretable raw residual reference is higher overall (73.8%). Mean margin gains are small in absolute terms (e.g., +0.00256 Classical, lift +0.00331 over random). Selection of source–target pairs and scoring both use MERT, a circularity the authors acknowledge and partially mitigate with a CLAP check (App. K). [PDF p. 4, Tables 3, 10]
- **Worked example:** Rubinstein vs Yundi Li performances of Chopin's Ballade No. 1; the Yundi target builds a louder crescendo with more elastic rubato; steering along f59100 (expressivo/rubato piano) produces a louder final span, while the best vanilla-SAE feature (f39785, slow introspective solo piano) moves generation the wrong way. [PDF p. 4]
- **Tradition-specific variation features (App. I):** Classical z_j features track phrasing/rubato/pedaling/expressive contour; Jazz features pick out lead instrument, ensemble feel, register, articulation; SHS100K features name accompaniment, vocal texture, orchestration, production style — matching the thickness of each tradition's notion of work identity. [PDF pp. 3, 9, Table 9]

## 5. Limitations and Future Work

- Workshop-scale evidence; the authors themselves frame steering as a "proof of concept" with small absolute effects, and note the evaluation circularity (MERT used both to select aligned pairs and to score movement). [PDF pp. 4, App. K]
- The account is model-internal to MusicGen: it shows how MusicGen organizes these corpora, not a general claim about musical interpretation; work labels carry tradition-specific assumptions (score-bound works vs standards vs covers), and the weak Jazz separation is a live instance of that fragility. [PDF pp. 3–4]
- Performer signal is emergent but entangled with repertoire and recording context; no performer-labeled training or controlled performer-transfer test. [PDF p. 4, Table 2]
- Code, checkpoints, and the audio dashboard are not yet public (App. H); the demo bucket is currently dead (closed billing account), so the "listen along" evidence is unverifiable at extraction time. [PDF App. H; live check 2026-10-16]
- Repository inference: probing accuracy establishes information recoverability, not causal use; the steering test is the paper's intervention evidence, but with a single rank-1 feature, a 10 s continuation, and an effect size that must be compared against the residual baseline. The three-claim ladder (recoverable / causal / useful) from [[concepts/music-theory-probing]] applies directly.

## 6. Related Work

Directly extends Singh, Cherep & Maes (ICLR 2026, "Discovering and Steering Interpretable Concepts in Large Generative Music Models"), which recovers flat SAE dictionaries from MusicGen; DC-SAE restructures that dictionary around the work/interpretation distinction. Also engages Wei et al. 2024 (SynTheory probing), Ma & Xia / Ma et al. (music-LLM probing), cover-song version identification (SHS100K, Discogs-VI), and content/style disentanglement including Zeng et al. 2025 (score-grounded piano performance), which it cites explicitly. [PDF pp. 1–2, App. A]

## 7. Glossary

- **SAE (sparse autoencoder):** overcomplete dictionary-learning autoencoder reconstructing a model's activations with a sparse bottleneck, used to surface monosemantic features.
- **TopK SAE:** SAE variant keeping exactly k active dictionary features per code.
- **Pivot window:** a window from a different recording of the same work, used positively for the identity branch and negatively for the variation branch.
- **MIL-NCE:** multi-positive noise-contrastive estimation pooling similarity over a bag of positives.
- **z_i / z_j:** the work-identity and performance-variation branch codes.
- **Residual stream:** the transformer's per-token read-write activation channel; here MusicGen layer 24.
- **MERT / CLAP:** frozen dense music-audio encoders used as baselines and (MERT) for pivot ranking and steering scores.
- **Target-margin gain:** increase in similarity of a steered continuation to the target performance relative to the source, measured by MERT cosine similarity.
