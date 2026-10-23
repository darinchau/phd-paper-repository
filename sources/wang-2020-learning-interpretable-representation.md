---
title: "Learning Interpretable Representation for Controllable Polyphonic Music Generation"
authors: "Ziyu Wang, Dingsu Wang, Yixiao Zhang, Gus Xia"
year: 2020
doi: 10.48550/arXiv.2008.07122
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/wang-2020-learning-interpretable-representation.pdf"
pdf_filename: wang-2020-learning-interpretable-representation.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-23
---
## One-line Summary

Wang et al. (ISMIR 2020, NYU Shanghai) factorize 8-beat (2-bar, 4/4) polyphonic piano segments into two continuous VAE latents: chord (rule-extracted 36×8 chord progression → bi-GRU, z_chd ∈ R^256) and texture (chord-invariant conv over a 128×32 piano-roll → bi-GRU, z_txt ∈ R^256, "texture" = chord arrangement + rhythmic pattern + melody contour). A PianoTree decoder reconstructs from the concatenation [z_chd; z_txt]. Swapping z_txt between pieces (inference-time only; never a training regime) yields compositional style transfer; texture sampling yields variations; a downstream Transformer predicts (z_chd, z_txt) from melody latents for accompaniment arrangement. Disentanglement is audited by latent-norm sensitivity to transposition/duration augmentations (Fig. 5) plus a listening test (Fig. 6), not by decode-and-measure interventions; no reconstruction accuracy is reported. Trained on 66K POP909 segments with 12-key transposition augmentation.

## 1. Document Information

- **Canonical source:** arXiv `2008.07122` (ISMIR 2020); official PDF preserved as `wang-2020-learning-interpretable-representation.pdf`.
- **Full-paper evidence:** full PDF read by a delegated research subagent on 2026-10-23 (NCM 4 sweep), including the public code repository; detailed digest in the wiki page `wiki/generation-and-planning/wang-2020-learning-interpretable-representation.md`.
- **Evidence policy:** paper claims, reported numbers and code-derived inferences are kept distinct; code-only findings are labelled as such.

## 2. Key Contributions

- Two inductive biases for chord/texture disentanglement: (i) a rule-based chord recognizer feeding the chord branch, (ii) an octave-wide (12-semitone kernel, stride 1) conv + 4-semitone max-pool producing a "blurry concept sketch" of the piano-roll that suppresses absolute chord identity for the texture branch (§3.1, §3.3).
- First explicit control of "compositional texture" for symbolic polyphonic generation (§1): texture swap (style transfer, Fig. 2), texture sampling (variation, Fig. 3), and melody→(chord,texture) arrangement (Fig. 4).
- Encoder-latent disentanglement audit via augmentation sensitivity: global transposition moves z_chd >> z_txt (tritone-sensitive, octave-invariant); duration halving moves z_txt only (Σ|Δz_chd| = 0) (§5.2, Fig. 5).
- Subjective evidence that swapped generations can be rated above the original human piece: best-of-5 texture transfers beat the original at p < 0.005 (36 subjects, creativity/naturalness/musicality) (§5.3, Fig. 6).

## 3. Methodology and Architecture

Four components (Fig. 1): chord encoder (36-D per-beat chord = 12 one-hot root + 12 one-hot bass + 12 multi-hot chroma, 8 beats; bi-GRU → Gaussian q(z_chd|c)); chord decoder (bi-GRU reconstructing root/bass/chroma from z_chd with CE losses — a standalone chord VAE); texture encoder (128×32 piano-roll, entries = onset durations at 1/4-beat resolution; Conv kernel 12×4 stride 1×4, 10 channels, ReLU, max-pool 4×1 stride 4×1 → 8 beat-position features → bi-GRU → q(z_txt|x)); PianoTree decoder (arXiv 2008.07118) on concat [z_chd; z_txt] ∈ R^512: GRU emits 32 frame-wise hiddens, a second GRU decodes ≤16 simultaneous note embeddings per frame, FC for pitch + GRU for duration (§3.4). Objective (Eq. 1): chord-VAE CE + PianoTree reconstruction (pitch CE + duration loss, weights (1, 0.5)) + KL(β annealed 0→0.1) — matched (x, c(x)) pairs only. Data: POP909 2/4+4/4 pieces cut into 8-beat segments (66K), song-level 90/10 split, all-12-key transposition augmentation, batch 128, 6 epochs (§5.1). Arrangement model: EC²-VAE melody pitch/rhythm latents (arXiv 1906.03626) per 2 bars → vanilla Transformer (256 hidden, 4 layers, 8 heads) predicting [z_chd, z_txt], with chord latents forced at inference (§4.3). Code: `ZZWaang/polyphonic-chord-texture-disentanglement` (inference swap/posterior/prior/slerp-interp methods verified in `model.py`; pretrained model in companion repo `ZZWaang/icm-deep-music-generation`).

## 4. Key Results and Benchmarks

| Evaluation | Type | Outcome |
|---|---|---|
| Fig. 5a: Σ\|Δz\| under F_i transposition | latent sensitivity | z_chd >> z_txt for small i; z_chd tritone-max/octave-min; z_txt grows with i (residual pitch leak) |
| Fig. 5b: P_i beat-wise ±1 semitone / R_i half durations | latent sensitivity | P_i: Δz_chd > Δz_txt; R_i: Δz_chd = 0, only z_txt moves |
| Fig. 2 style transfer | qualitative scores | texture-swap outputs follow source chords + donor texture (labels inferred from output, footnote 2) |
| Fig. 6 listening test (n=36, 10×6 versions) | subjective 5-pt | best-of-5 transfers > original, p < 0.005; 2nd-largest ≈ original (p > 0.05, creativity/musicality); mean transfer < original |

Evidence boundaries: no note-level or chord-level reconstruction accuracy is reported for the fused model (training losses only). The disentanglement test measures encoder-latent L1 shifts under input augmentation — no experiment decodes swapped latents and measures that only the matching attribute changed; chord preservation after texture swap is shown only as score figures and quality ratings. Released `train.py` instantiates `PtvaeEncoder` (non-conv) for the texture stream with `TextureEncoder` commented out, and GRU hiddens are 1024 in code vs 256/512 in the paper (§5.1); README admits the repo is "selected files... may be incomplete". Both z's are continuous Gaussians; nothing is quantized.

## 5. Limitations and Future Work

Occupies: in-domain precedent for two factorized streams over polyphonic symbolic piano (harmonic content vs everything-else) merged by a decoder and demonstrated by cross-piece latent swaps; a swap application (style transfer) and a latent-sensitivity audit. Does not occupy: (1) discretization — no VQ/codebooks, no LM-ready discrete codes, no RVQ depth structure; (2) train-time cross-piece merge — Eq. 1 trains only on matched (x, c(x)); swap is pure off-distribution inference (`model.py swap()`), so merge generalization is never optimized or measured; (3) interventional dissociation gate — no "swap one stream, decode, and verify only the corresponding attribute moved" test with objective metrics on decoded output; (4) rhythm isolation — texture conflates rhythm, melody contour and voicing, so the chord/rhythm axis is coarser than harmony-vs-rhythm, and harmony is a rule-based 8-beat chord grid rather than learned codes; (5) reconstruction fidelity gate — no reconstruction number exists to compare against a noop floor (cf. MuseTok's 0.924 noop acc@16 baseline). Positioning for the factorized-streams pivot: this is the closest in-domain ancestor to cite and partially replicate; our novelty rests on quantized streams, a fusion decoder trained on cross-piece pairings, and pre-registered decode-and-measure dissociation gates.

## 6. Related Work

- [[generation-and-planning/wang-2022-audio-to-symbolic-arrangement-via-cross-modal]] — same-group ICLR 2022 follow-up (arXiv 2112.15110): adds audio-texture branch and a shared 192-D continuous texture space; still no quantization.
- [[data-and-representation/wang-2020-pop909-a-pop-song-dataset]] — the training corpus (same lab, same year).
- [[data-and-representation/huang-2025-musetok-symbolic-music-tokenization-for]] — the other side of our pivot's design space: single-stream RVQ codes, correlational level analysis, no factorization.
- [[overviews/2026-symbolic-music-literature-map]] — placement in the 2026 symbolic-music landscape.
- PianoTree VAE (arXiv 2008.07118) supplies the decoder; Deep Music Analogy (arXiv 1906.03626) supplies the melody EC²-VAE and the monophonic pitch/rhythm predecessor; AccoMontage (arXiv 2108.11213, ISMIR 2021) turns the chord-manipulation pathway into phrase-retrieval arrangement; whole-song cascaded diffusion (Wang, Min & Xia, ICLR 2024, arXiv 2405.09901) scales the hierarchy to full songs — all keep the factors continuous (follow-ups verified from metadata/abstracts, not full texts).

## 7. Glossary

- **VAE:** variational autoencoder.
- **GRU:** gated recurrent unit.
- **RVQ / RQ-VAE:** residual vector quantization (variational autoencoder) — contrasted with this paper's continuous latents.
