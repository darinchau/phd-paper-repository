# 2026-10-16 — SyMuPe, Zeng et al. joint EPR/APT, and DC-SAE ingestion

## Scope and completion

User-requested digest of three papers, ingested per the digest command convention. All three were identified and verified before ingestion:

1. **SyMuPe** (arXiv 2511.03425v1, ACM MM '25, DOI 10.1145/3746027.3755871) — Borovik, Gavrilev, Viro.
2. **Zeng et al.** (arXiv 2509.23878v1, preprint) — "Disentangling Score Content and Performance Style for Joint Piano Rendering and Transcription".
3. **DC-SAE** — identity question resolved: OpenReview `xj0pDqfogb` is **"Dual-Contrastive Sparse Autoencoders Reveal Features of Musical Interpretation"** (Jan Chen*, Manuel Cherep*, Pattie Maes, Nikhil Singh; Mechanistic Interpretability Workshop @ ICML 2026 virtual poster; listed as NeurIPS 2026 on author pages). It is **not** the identically abbreviated "DC-SAE: Deep Compression Semantic Autoencoder" (arXiv 2609.39222, an image tokenizer). Verified via the official workshop poster PDF (mechinterpworkshop.com/poster-pdfs/534.pdf), the workshop virtual-posters page abstract, and the authors' homepages (chen-jan.github.io, sahaslab.com).

- PDF provenance: SyMuPe and Zeng downloaded from arXiv; DC-SAE supplied by the user at the phd-research root (OpenReview blocks this network's egress IP: direct fetch, Jina, CORS proxies, and archive routes all failed). Canonical copies in `papers/`; SHA-256 in each source record. The user's root copy was left untouched.
- All pages of all three PDFs read from PyMuPDF extraction (SyMuPe 16/16; Zeng 30/30 with the typeset-score appendices not visually inspected — nothing quantitative rests on them; DC-SAE 14/14 including appendices A–M).
- DC-SAE artifact check: the paper's audio-demo bucket (`storage.googleapis.com/dc-sae-musicgen-listening`) returns a closed-billing-account error — the "listen along" evidence is currently inaccessible; code is not yet public per App. H. Recorded in the source record.

## Records

- `papers/borovik-2025-symupe-affective-and-controllable.pdf` + `sources/` + `wiki/generation-and-planning/`
- `papers/zeng-2025-disentangling-score-content-and-performance.pdf` + `sources/` + `wiki/generation-and-planning/`
- `papers/chen-2026-dual-contrastive-sparse-autoencoders.pdf` + `sources/` + `wiki/explainability-and-auditability/`
- **New concept anchor** `wiki/concepts/work-identity-versus-performance-variation.md`: the work/interpretation factorization question, instantiated by Zeng (trained into an EPR system) and Chen (recovered from MusicGen internals), with Borovik as the non-factorizing control. This was recorded as a gap candidate in the 2026-10-14 MATCHA log's style; the topic now clearly recurs (two primary papers plus MusPyExpress/MuseTimbre/Storan adjacency), so the anchor was created.
- `wiki/overviews/2026-symbolic-music-literature-map.md` updated: three category entries, three Related Papers entries, and body sentences in "Generation, control, and editing" and "Explainability, attribution, and verification".
- Reciprocal synthesis links + body sentences added to `wiki/concepts/music-theory-probing.md` (DC-SAE as the audio-side probing→steering instance of the three-claim ladder) and `wiki/concepts/expression-aware-symbolic-representations.md` (PianoFlow's real-valued score/performance feature pair without typed expression instructions).

Category decisions: SyMuPe and Zeng → `generation-and-planning` (primary contributions are generative frameworks for performance rendering; disentanglement in Zeng serves generation/control, with no faithfulness or explanation claim). DC-SAE → `explainability-and-auditability` (interpretability method with probing and steering evidence on a frozen generator).

## Supersede check

No contradictions. Deltas: (1) DC-SAE **strengthens** the music-theory-probing concept's claim that probing needs an intervention companion — it supplies one, with honestly small margins and acknowledged metric circularity. (2) Zeng et al. **narrows** nothing but adds the first wiki evidence that a global performance-style vector recovers composer identity (77.5%) far above performer identity (42.1%), consistent with DC-SAE's entanglement findings — two independent methods, same asymmetry. (3) Borovik et al. **strengthens** the existing caution that objective distribution metrics (KL) dissociate from perceptual quality, from within the EPR task itself.

## Synthesis gaps noted

- No wiki page yet covers expressive performance rendering (EPR) as a task family: ScorePerformer, VirtuosoNet, DExter, PianoFlow, Zeng et al., Edwards et al. are now all present or cited. Anchor candidate for a future session; the new work-identity concept carries the interim load.
- DC-SAE's evaluation circularity (MERT for both pair selection and steering scores) is a concrete instance of a general evaluation-validity problem that deserves its own treatment if more steering papers arrive.

## Validation and status

- `validate_paper_records.py`: 72 source records, 72 paper pages, 11 synthesis pages — 0 errors, 0 warnings.
- `audit_synthesis_orphans.py`: 0/72 orphans.
- `build_indexes.py --date 2026-10-16` run after ingestion; `index.md`, both touched category indexes, and `logs/README.md` regenerated.
- Evidence limitations preserved: SyMuPe's proprietary 74.6% corpus share and non-expert listener pool; Zeng's preprint status, 11-rater studies, and correlational disentanglement evidence; DC-SAE's workshop scale, dead demo bucket, unreleased code, and MERT circularity.
