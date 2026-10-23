---
title: "Music SketchNet: Controllable Music Generation via Factorized Representations of Pitch and Rhythm"
authors: "Ke Chen, Cheng-i Wang, Taylor Berg-Kirkpatrick, Shlomo Dubnov"
year: 2020
doi: 10.48550/arXiv.2008.01291
source: chen-2020-music-sketchnet-controllable-music-generation.md
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/chen-2020-music-sketchnet-controllable-music-generation.pdf"
pdf_filename: chen-2020-music-sketchnet-controllable-music-generation.pdf
pdf_source_url: "https://arxiv.org/pdf/2008.01291v1"
code_url: "https://github.com/RetroCirce/Music-SketchNet"
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-23
tags: [factorized-latents, vae, pitch-rhythm-disentanglement, controllable-generation, music-inpainting, monophonic, irish-folk, cross-piece-swap, code-analysis, code-public]
---

# Music SketchNet: Controllable Music Generation via Factorized Representations of Pitch and Rhythm

## Summary

Music SketchNet (ISMIR 2020) is the closest in-domain precedent for factorized attribute streams in symbolic music: a monophonic Irish-folk measure is split at the *input* into a rhythm-free pitch-contour token sequence and a pitch-blind onset/hold rhythm sequence, each with its own GRU encoder producing a continuous 128-d Gaussian latent, and a learned hierarchical beat/tick decoder merges the concatenation. On top of SketchVAE sit a per-stream latent inpainter and a transformer "connector" that integrates user sketches via random unmasking. Its "virtual control experiment" (Table 3) is an early cross-piece single-factor swap: injecting sample B's rhythm into sample A yields 97.3% rhythm agreement but only 18.9% pitch agreement with B (pitch sketch: 88.1% / 84.8%). For this knowledge base it anchors the pitch-vs-rhythm factorization axis — but it is monophonic, uses continuous VAE latents (no codebooks), trains its merge only on same-measure factor pairs, and its swap test never verifies the untouched factor, which is precisely the dissociation gap our stream-swap audit fills.

## Key Contributions

- SketchVAE: factorized inference network — separate pitch and rhythm encoders over separately tokenized input streams, z = [z_pitch (128-d); z_rhythm (128-d)] continuous Gaussian (§2.2, Figure 4; `SketchVAE/sketchvae.py`).
- SketchInpainter: stacked bidirectional GRUs over past/future measure latents per stream, autoregressively predicting missing-measure latents (§2.3, Figure 5).
- SketchConnector: transformer encoder over the measure-latent sequence, trained with random unmasking (rate 0.3) to accept partial user sketches (§2.4, Figure 6).
- Virtual control experiment: quantitative cross-piece factor-swap test of user control (§3.4, Table 3) — the paper's main evidence that factor interventions steer only their attribute (partially).

## Methodology and Architecture

**Score encoding and factorization (§2.2.1, Figure 3).** Monophonic MIDI, each measure cut to 24 frames (4 beats × 6 ticks; eighth-note-triplet-safe grid); tokens 0–127 = onset pitch, 128 = hold, 129 = rest. The encoded measure x is split into x_pitch (all note-onset values, padded with a padding token to 24) and x_rhythm (every onset replaced by the same token "O", holds kept as "_"; a 3-way one-hot per code, `r_input_dims=3`). So the pitch encoder sees a rhythm-free ordered pitch sequence (its length = number of notes; note count leaks implicitly), and the rhythm encoder sees onset/hold only, blind to pitch. Factorization is by input construction — no adversarial, MI, or bottleneck constraint.

**Encoders (§2.2.2, Figure 4; code).** Two independent 2-layer bidirectional GRUs (hidden 512), each → linear μ and log σ² → Normal; z_pitch, z_rhythm ∈ R^128 each (|z| = 256, "half for the pitch contour, and the other half for the rhythm", §3.2.1). Latents are continuous; no quantization, codebooks, or RVQ anywhere.

**Merge / decoder (§2.2.3, Figure 4; `final_decoder`).** z = torch.cat(z_pitch, z_rhythm) → Linear(256→512) + SELU → initial hidden state of a beat GRU unrolling n = 4 beats → per-beat Linear+SELU → tick GRUs generating 6 ticks each autoregressively over the 130-token vocabulary, with decaying teacher forcing (`decay=1000`). This concatenation-into-learned-hierarchy is the merge; it is a trained fusion of the two stream vectors, but it is trained **only on (z_pitch, z_rhythm) pairs from the same measure of the same piece** (standard reconstruction). Cross-piece pairing never enters SketchVAE training.

**Inpainter and connector (§§2.3–2.4, Figures 5–6).** Separate past/future pitch and rhythm bidirectional GRUs encode context; per-stream generation GRUs predict missing measure latents (stage I, frozen VAE). The connector embeds [past; predicted-missing; future] measure latents with positional encoding and refines them with multihead self-attention; during training, predicted missing latents are randomly replaced by the ground-truth latents at rate 0.3 (independently for the pitch and rhythm halves in code) — ground truth again from the same piece. Inference with a user sketch hard-overwrites the sketched positions with the sketch's encoder latents **after** the connector output (`sketchnet.py`, `sketch_generation`: `ys[:, d, :zp_dims] = cond_output`) — the user constraint is imposed structurally, not purely emergent (code-verified; not stated in the paper).

**Data (§3.1).** Irish/Scottish folk (Sturm et al. 2016), 4/4 only, ~16,000 train / 2,000 test melodies; inpainting setting 6 past + 4 missing + 6 future measures (§3.3.1). Monophonic throughout; polyphony is explicitly out of scope.

## Results

| | Irish-Test loss↓ / pAcc↑ / rAcc↑ | Irish-Test-R | Irish-Test-NR |
|---|---|---|---|
| Music InpaintNet | 0.662 / 0.511 / 0.972 | 0.312 / 0.636 / 0.975 | 0.997 / 0.354 / 0.959 |
| SketchNet (full) | **0.516 / 0.651 / 0.985** | **0.206 / 0.799 / 0.991** | **0.783 / 0.461 / 0.977** |

(Table 1; bootstrap over 10k resamples: all pairwise accuracy differences p < 0.05 except InpaintNet vs SketchVAE+InpaintRNN, p = 0.402.)

- Reconstruction (§3.2.1): SketchVAE 98.8%, MeasureVAE 98.7%, EC²-VAE 99.0% at |z| = 256 — near-ceiling on 24-frame monophonic measures.
- Listening test (Table 2; 106 subjects, 318 ratings, non-repetition subset, 1–5 scale): SketchNet 3.04 / 3.29 / 3.26 (complexity / structure / musicality) vs InpaintNet 2.98 / 3.01 / 3.09 vs original 3.22 / 3.47 / 3.56; significant gains on structure and musicality, not complexity (p = 0.364).
- Virtual control experiment (§3.4, Table 3; 3,000 (A,B) pairs from Irish-Test; B's factor injected as sketch into A's missing position; pitch agreement via longest-common-subsequence, footnote 2): rhythm sketch → 97.3% rhythm agreement / 18.9% pitch agreement with B; pitch sketch → 88.1% pitch / 84.8% rhythm agreement with B.

Evidence boundaries: the swap test measures agreement with the sketch source B only — it never measures whether the untouched factor stays close to A's original, so it is asymmetric-guidance evidence, not a "only the corresponding attribute moved" dissociation audit. No chance baseline is reported; rhythm accuracy is dominated by hold tokens, so 0.848 / 0.985-style values need a null model before being read as disentanglement (analysis, not the authors' claim). Inference-time control partly relies on the hard latent overwrite in code. All numbers are monophonic, measure-granularity, 4/4 Irish folk only.

### Limitations and Follow-up

Authors' admitted limits (§4): only pitch and rhythm factors; polyphonic latent representation is "a pressing issue" left as future work. Follow-up: first author's UCSD dissertation "Controllable Monophonic Music Generation via Latent Variable Disentanglement" (2021, eScholarship) extends the line but stays monophonic; Ke Chen + Dubnov later co-authored Multitrack Music Transformer (arXiv 2207.06983), polyphonic but not factorized-sketch. (Search-level evidence, not full-read.) ~27 citations per DataCite/OpenAlex metadata (2026-10-23). Code: `github.com/RetroCirce/Music-SketchNet` (CC0, full notebook pipeline, trained-parameter backups downloadable).

### Delta vs Our Project (NCM factorized harmony/rhythm streams)

SketchNet occupies: separate per-attribute encoders over symbolic music, a learned concat-into-decoder merge, optional partial user specification, and a cross-piece single-factor swap with numbers (Table 3) — on exactly the pitch-vs-rhythm axis. It does **not** occupy any of our four design points: (1) streams are continuous VAE Gaussians, not RVQ-quantized codebooks; (2) monophonic pitch *contour* over Irish folk, not *harmony* (chords) over polyphonic piano; (3) the merge is trained only on same-measure factor pairs — cross-piece stream pairing happens only at inference, never in training, so its decoder was never audited for stream-recombination competence; (4) its swap audit checks that the swapped factor follows the source but never that the untouched factor stays with the original — the exact criterion our dissociation gate (one factor moves, the other must not) adds. Position it in the novelty sweep as the closest conceptual ancestor, and cite Table 3 as precedent for — and evidence of the incompleteness of — intervention-style control evaluation.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — generation-and-planning entry.
- [[data-and-representation/huang-2025-musetok-symbolic-music-tokenization-for]] — the opposite pole: one residual code ladder with correlational level-reading, vs SketchNet's two hand-split continuous streams with a (partial) interventional test.
- [[generation-and-planning/zeng-2025-disentangling-score-content-and-performance]] — disentangled piano latents, content vs performance style.
- [[generation-and-planning/zhu-2025-efficient-fine-grained-guidance-for]] — separate harmonic/rhythmic constraint masks in diffusion guidance.
- [[generation-and-planning/wu-2023-music-controlnet-multiple-time-varying]] — control-interface precedent.
