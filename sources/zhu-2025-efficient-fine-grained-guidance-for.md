---
title: "Efficient Fine-Grained Guidance for Diffusion Model Based Symbolic Music Generation"
authors: "Tingyu Zhu, Haoyu Liu, Ziyu Wang, Zhimin Jiang, and Zeyu Zheng"
year: 2025
doi: 10.48550/arXiv.2410.08435
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/zhu-2025-efficient-fine-grained-guidance-for.pdf"
pdf_filename: zhu-2025-efficient-fine-grained-guidance-for.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-21
---

# Efficient Fine-Grained Guidance for Diffusion Model Based Symbolic Music Generation

## One-line Summary

FGG adds fine-grained harmonic (required) and rhythmic (optional) piano-roll conditioning to a diffusion model and projects the predicted clean signal at every reverse step so that forbidden pitch-class/time cells cannot be sampled; on POP909 accompaniment generation it eliminates out-of-key notes (0.0% vs 2.1–3.5% for baselines), roughly doubles chord accuracy, and wins a subjective comparison on every rated dimension.

## 1. Document Information

- **Authors and affiliations:** Tingyu Zhu and Haoyu Liu (UC Berkeley), Ziyu Wang (NYU), Zhimin Jiang (Touka Technologies), Zeyu Zheng (UC Berkeley).
- **Venue and version:** ICML 2025 (PMLR 267); arXiv 2410.08435v3, 6 June 2025. 25 PDF pages: main text pp. 1–9, references pp. 10–13, appendices pp. 14–25.
- **Extraction:** full text via `pdftotext -layout`; Tables 1–4, Figures 1–3, the FGG sampling algorithm (Appendix), and §6 inspected.
- **Artifacts:** code and demo at `https://github.com/huajianduzhuo-code/FGG-music-code` and `https://huajianduzhuo-code.github.io/FGG-diffusion-music/`.
- **Anchors:** problem §1 p. 1; diffusion background §2 pp. 2–3; conditioning §3.1 pp. 3–4; reverse cross-attention/guidance §3.2 pp. 4–6; experiments §5 pp. 6–9; limitations §6 p. 9.

## 2. Key Contributions

1. **A precise formulation of the symbolic-precision problem**: unlike pixels, every piano-roll cell has a fixed time–pitch meaning, so a single wrong note is musically audible and can be constrained exactly.
2. **Fine-grained conditioning** with a harmonic piano-roll `M_cond(C)` and an optional rhythmic mask `M_cond(C, R)`, including a negative-value convention that distinguishes "no rhythmic constraint" from "silence".
3. **Hard sampling-time guidance**: at each reverse step the model's predicted clean signal is projected onto the allowed set (forbidden cells set to zero, allowed cells preserved), with a theoretical argument that this preserves the learned distribution better than post-hoc editing.
4. **Empirical evidence** that training-time conditioning plus sampling-time projection beats rule-based post-editing, inpainting, and two strong baselines on objective and subjective measures.

## 3. Methodology and Architecture

- **Representation.** Binary piano roll `M ∈ {0,1}^{L×H}`, `H=128` pitches, `L=64` sixteenth-note steps (four bars of 4/4). The diffusion model predicts a continuous `X`; the roll is `M = 1[X > 1/2]`.
- **Model.** DDPM over piano rolls, with the noise-prediction network conditioned on melody, chord, and optional rhythm channels. Classifier-free guidance is used; the paper derives the guided noise estimate and the projection step.
- **Conditioning.** `M_cond(C)` marks chord tones at each time step; `M_cond(C, R)` additionally marks a rhythmic pattern. Negative values encode "no rhythmic constraint" so that the model does not read zeros as forced silence.
- **Guidance.** The reverse step first forms the predicted `X_0`; cells that must be empty are set to zero; cells that must be present are clamped; the corrected estimate is converted back to a noise estimate and used for the usual DDPM update. This is a runtime projection, not a retrained classifier.
- **Data and task.** POP909, split 90/10; 15,761 non-overlapping four-bar segments for training; 88 pieces for evaluation. Task: generate an accompaniment given melody and chord progression. Baselines: WholeSongGen and GETMusic, both diffusion-based; ablations: inpainting, training-only control, post-hoc rounding/removal, and no control.

## 4. Key Results and Benchmarks

**Objective (Table 1, p. 8).**

| Method | Out-of-key (%) | Direct chord acc. | Chord similarity | IoU chord | IoU piano roll |
|---|---:|---:|---:|---:|---:|
| FGG | 0.0 | 0.485 | 0.767 | 0.769 | 0.281 |
| WholeSongGen | 2.1 | 0.314 | 0.611 | 0.618 | 0.107 |
| GETMusic | 3.5 | 0.153 | 0.394 | 0.412 | 0.048 |

**Ablation (Table 2, p. 9).** No control: 10.1% out-of-key, chord accuracy 0.112, chord IoU 0.378, piano-roll IoU 0.072. Training-only control: 3.7% out-of-key, 0.465 chord accuracy. Post-hoc removal: 0.0% out-of-key but chord accuracy 0.112 and chord IoU 0.378 — removing wrong notes without replacing them damages harmony. Sampling guidance is the only arm that both removes errors and preserves chord accuracy (0.485) and IoU (0.769). Inpainting is close but slightly worse on every metric (0.458 / 0.743 / 0.271).

**Subjective (Figure 3, p. 8).** FGG is preferred on creativity, harmony, melodiousness, naturalness, richness, and overall; the paper reports means and 95% CIs but not the number of participants in the main text. The evaluation is on four-bar pop accompaniment, not classical composition or repair.

**What the result means.** Hard constraints can be imposed at sampling time without retraining and without destroying local coherence, at least for pitch-class/chord constraints. The theoretical claim is distribution preservation relative to post-hoc editing; the empirical claim is that this beats rounding/removal and inpainting.

## 5. Limitations and Future Work

- **Sixteenth-note quantization.** No 10 ms expressive timing, no tempo rubato, no triple/compound metre beyond what the grid approximates; training requires beat-annotated data.
- **Pitch-class and rhythm only.** No voicing, voice-leading, texture, dynamics, articulation, or form; "harmony" is chord-tone membership, not functional harmony.
- **No probabilistic or abstract control.** The method enforces hard constraints, not soft preferences or uncertainty.
- **Data scope.** POP909 pop piano, 88 evaluation pieces, one dataset; no classical, multi-instrument, or cross-dataset test.
- **Evaluation.** Objective metrics compare to a single ground-truth accompaniment even though many valid accompaniments exist; subjective details (participant count, expertise, item sampling) are in an appendix and are not a full perceptual study.
- **Constraint authorship.** The user must supply the chord/rhythm mask; the system does not infer intent or explain why a note was forbidden.

## 6. Related Work

- DDPM, score-based diffusion, classifier-free guidance: the generative backbone.
- Image inpainting and post-conditioning (RePaint, etc.): the analogy and baseline.
- Music ControlNet, WholeSongGen, GETMusic: symbolic diffusion with control.
- Music Transformer, Pop Music Transformer, FIGARO, MuseMorphose: symbolic generation and control precedents.
- Rule-based post-editing: the practical alternative the paper argues against.

## 7. Glossary

- **FGG:** Fine-Grained Guidance.
- **DDPM:** Denoising Diffusion Probabilistic Model.
- **CFG:** Classifier-Free Guidance.
- **IoU:** Intersection over Union.
- **POP909:** a pop-song dataset with melody/chord/arrangement annotations.
- **Piano roll:** a time × pitch binary matrix.
