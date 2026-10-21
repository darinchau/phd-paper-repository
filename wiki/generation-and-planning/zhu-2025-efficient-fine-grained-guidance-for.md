---
title: "Efficient Fine-Grained Guidance for Diffusion Model Based Symbolic Music Generation"
authors: "Tingyu Zhu, Haoyu Liu, Ziyu Wang, Zhimin Jiang, and Zeyu Zheng"
year: 2025
doi: 10.48550/arXiv.2410.08435
source: zhu-2025-efficient-fine-grained-guidance-for.md
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/zhu-2025-efficient-fine-grained-guidance-for.pdf"
pdf_filename: zhu-2025-efficient-fine-grained-guidance-for.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
tags: [diffusion, symbolic-music, piano-roll, harmonic-control, constrained-sampling, pop909, accompaniment]
---

# Efficient Fine-Grained Guidance for Diffusion Model Based Symbolic Music Generation

## Summary

FGG makes harmonic control exact rather than approximate. The model is trained with a chord piano-roll condition (plus an optional rhythm mask), and at every reverse diffusion step the predicted clean piano roll is projected onto the allowed time–pitch cells before the next update. On POP909 accompaniment generation this yields 0.0% out-of-key notes, chord accuracy 0.485 versus 0.314/0.153 for WholeSongGen/GETMusic, and a piano-roll IoU of 0.281 versus 0.107/0.048. The ablation is the useful part: removing wrong notes after sampling also reaches 0% out-of-key but collapses chord accuracy to 0.112, so the gain comes from replacing forbidden notes with harmonically valid ones during denoising, not from deletion.

## Key Contributions

- A precise statement of why symbolic diffusion needs cell-level constraints: each piano-roll position has fixed musical meaning, unlike a pixel.
- Fine-grained conditioning with separate harmonic and rhythmic masks and a negative-value convention for absent rhythm.
- A sampling-time projection with a distribution-preservation argument, competitive with inpainting and cheaper than adding a mask channel.
- Strong objective and subjective gains over two diffusion baselines, plus a clean ablation separating training control, sampling control, and post-hoc editing.

## Methodology and Architecture

Piano roll `M ∈ {0,1}^{64×128}` (four bars, sixteenth notes). A DDPM predicts the clean roll; classifier-free guidance is used. Conditioning marks chord tones per step and, optionally, a rhythmic pattern. At each reverse step the predicted `X_0` is projected: forbidden cells → 0, required cells → clamped, then converted back to a noise estimate for the standard update. Data: POP909, 15,761 four-bar segments, 88 evaluation pieces; task: melody + chord → accompaniment. Baselines: WholeSongGen, GETMusic; ablations: inpainting, training-only control, post-hoc rounding/removal, no control.

## Results

| Method | Out-of-key % | Chord acc. | Chord sim. | IoU chord | IoU roll | Anchor |
|---|---:|---:|---:|---:|---:|---|
| FGG | 0.0 | 0.485 | 0.767 | 0.769 | 0.281 | Table 1, p. 8 |
| WholeSongGen | 2.1 | 0.314 | 0.611 | 0.618 | 0.107 | Table 1, p. 8 |
| GETMusic | 3.5 | 0.153 | 0.394 | 0.412 | 0.048 | Table 1, p. 8 |
| Training-only control | 3.7 | 0.465 | 0.763 | 0.757 | 0.277 | Table 2, p. 9 |
| Post-hoc removal | 0.0 | 0.112 | 0.378 | 0.378 | 0.072 | Table 2, p. 9 |
| No control | 10.1 | 0.112 | — | 0.378 | 0.072 | Table 2, p. 9 |

Subjective ratings favour FGG on creativity, harmony, melodiousness, naturalness, richness, and overall. The evaluation is four-bar pop accompaniment with a fixed sixteenth-note grid; it does not test classical style, long-form structure, voice leading, or expressive timing.

## Related Papers

- [[overviews/audio-symbolic-transfer]] — control and constraint technology that could make audio-derived symbolic data usable for composition/repair, not just retrieval.
- [[generation-and-planning/chen-2024-sympac-scalable-symbolic-music]] — the autoregressive/FSM counterpart: exact constraints via grammar, rather than diffusion projection.
- [[theory-and-constraints/liu-2026-do-language-models-need-music]] — verifier-based rewards for multi-constraint symbolic generation.
- [[generation-and-planning/wu-2023-music-controlnet-multiple-time-varying]] — time-varying control for audio diffusion.
- [[generation-and-planning/guo-2025-moonbeam-a-midi-foundation-model]] — chord/metadata-conditioned symbolic generation.
