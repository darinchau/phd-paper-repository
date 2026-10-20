---
title: "MuseTok: Symbolic Music Tokenization for Generation and Semantic Understanding"
authors: "Jingyue Huang, Zachary Novack, Phillip Long, Yupeng Hou, Ke Chen, Taylor Berg-Kirkpatrick, and Julian McAuley"
year: 2025
doi: 10.48550/arXiv.2510.16273
source: huang-2025-musetok-symbolic-music-tokenization-for.md
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/huang-2025-musetok-symbolic-music-tokenization-for.pdf"
pdf_filename: huang-2025-musetok-symbolic-music-tokenization-for.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-20
tags: [residual-vq, rq-vae, discrete-latents, bar-level-tokens, remi-plus, symbolic-piano, code-analysis, released-checkpoint]
---

# MuseTok: Symbolic Music Tokenization for Generation and Semantic Understanding

## Summary

MuseTok is a bar-wise residual vector-quantized autoencoder (RQ-VAE) for symbolic piano scores in REMI+ events. Each bar becomes `D` codes from non-shared codebooks; the decoder reconstructs events autoregressively from the summed code embedding. The released Large model (D=16, K=2048) reconstructs at 99.58 / 93.71 / 82.68% event accuracy on monophonic / chorale / polyphonic test material. It drives a two-stage generator that beats REMI+ and AMT on objective continuation similarity but loses on rated Pitch and Harmony. It also gives correlational, Small-model-only evidence that the first codebook is largely transposition-invariant (rhythm and contour) and deeper codebooks carry absolute pitch. For this knowledge base it is the closest existing symbolic-music instance of a residual code ladder, with public weights and training code.

## Key Contributions

- RQ-VAE over bar-level REMI+ segments with SimVQ, rotation trick and EMA codebooks; ablations show both tricks matter for utility and accuracy (Table 1).
- Two-stage generation: a 152M code-sequence Transformer plus the frozen decoder. Codes are flattened and predicted serially, not coarse-to-fine.
- Code embeddings as features for melody, 133-class chord and emotion classification (best on chord and emotion, worst on melody).
- Codebook analysis: texture-specific code sets, time-signature separation growing with depth, pitch-shift similarity above 0.7 at d=1 and dropping with depth.

## Methodology and Architecture

A 12-layer Transformer encoder maps each bar to `z_b`; residual quantization picks `c_b^1 … c_b^D` (Eqs. 1–3); the decoder conditions every event of bar `b` on `Σ_d r_b^d` (Eq. 4). Loss = event cross-entropy + cumulative commitment loss across depths (Eq. 5). Trained on 195,187 piano sequences from PDMX plus six smaller datasets, with ±6-semitone transposition augmentation, ~45k steps on one A6000. Performance attributes (tempo, velocity) are removed and onsets snapped to score positions.

## Results

| | Mono. Acc | Chorale Acc | Poly. Acc | Util |
|---|---|---|---|---|
| VAE upper bound | 96.70 | 83.59 | 82.21 | – |
| MuseTok-Small (D=8) | 97.76 | 80.85 | 62.92 | 99.58% |
| MuseTok-Large (D=16) | 99.58 | 93.71 | 82.68 | 98.96% |

Continuation: sim_chr 95.19 and sim_grv 88.77 (best), but Pitch 3.698 vs REMI 4.099 and Harmony 3.604 vs 3.927 on a 192-rating-per-cell Likert test without intervals. Understanding: chord 49.87% (RNN 38.03), emotion 78.95% (MusicBERT 77.78), melody 81.92% (MIDI-BERT 90.97).

Evidence boundaries: the level analysis uses the unreleased Small model and is correlational (code frequency and embedding cosine, no swap or ablation). The decoder is trained only on full-depth sums, so prefix decodes are off-distribution. A local CPU check on one synthetic pattern gave event accuracy rising from 0.19 at depth 1 to 1.00 at depth 12. The released checkpoint is Large; reusing it needs a `miditoolkit` compatibility shim and score-quantised input.

## Related Papers

- [[concepts/hierarchical-latent-reasoning]] — MuseTok is the symbolic-music residual code ladder against which the NCM-style resolution-hierarchy claims can be tested; its level reading is correlational and needs the causal checks listed there.
- [[overviews/2026-symbolic-music-literature-map]] — data and representation entry.
- [[other/kumbong-2026-ncm-next-concept-modeling-fast]] — text analogue: multiscale residual VQ generated level-parallel coarse-to-fine, with coarse-code fixing and mixing probes.
- [[data-and-representation/fradet-2023-miditok-a-python-package-for]] — event-level tokenization tooling MuseTok sits on top of conceptually.
