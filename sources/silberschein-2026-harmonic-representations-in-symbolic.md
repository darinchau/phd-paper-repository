---
title: "Harmonic Representations in Symbolic Music Transformers are Localized and Controllable"
authors: Adi Silberschein, Megan Wei, Tamar Rott Shaham
year: 2026
doi: 10.48550/arXiv.2610.15957
category: explainability-and-auditability
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/silberschein-2026-harmonic-representations-in-symbolic.pdf"
pdf_filename: silberschein-2026-harmonic-representations-in-symbolic.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-31
---

## One-line Summary

In Aria, a symbolic music transformer, lowering a single note at a cadence changes where the music resolves; patching experiments show the causal effect appearing only from the middle layers, probes recover mode before key, and adding a probe-derived direction at inference turns a tonic resolution into a relative- or parallel-minor one without breaking the music.

## 1. Document Information

- **Canonical citation:** Adi Silberschein, Megan Wei, and Tamar Rott Shaham, “Harmonic Representations in Symbolic Music Transformers are Localized and Controllable,” arXiv:2610.15957v1 [cs.SD; cs.LG], 11 October 2026, 9 PDF pages. The arXiv comment states “Accepted at ISMIR 2026 (27th International Society for Music Information Retrieval Conference)”; the PDF itself carries no proceedings header, so venue status rests on that arXiv metadata.
- **Affiliations:** Weizmann Institute of Science; Brown University; MIT CSAIL. [PDF p. 1]
- **DOI:** `10.48550/arXiv.2610.15957` (arXiv DOI).
- **Artifacts:** the paper points to `https://adisilber.github.io/harmonic-interp/` for samples, code and data. [PDF p. 1]
- **Canonical integrity:** SHA-256 `cf6ed289b8ebbf0c6a222679ae1cb639b6a885864e11b86c5a21090cc5cfa93c`.
- **Rights boundary:** arXiv preprint; the batch digest records “CC BY 4.0” as the citation note, which this record does not verify as a redistribution licence. Retained locally as research evidence only.
- **Primary category:** `explainability-and-auditability`. The contribution is a mechanistic-interpretability account of one model plus a training-free control method, not a new generator or dataset.
- **Evidence levels:** numbers below were re-read from Figures 2–6 and Table 1. The earlier batch digest swapped two FMD values (the unsteered baseline is 80.27 and relative-minor steering is 85.42) and gave the mode-steering strength as unspecified; this record corrects both. The paper also declares LLM assistance for text polishing and coding agents for experimental code, with authors responsible for all claims. [PDF p. 7]

## 2. Key Contributions

### A one-note counterfactual that changes harmony

Cadences are found with music21, the chorale is truncated after the dominant, and the chordal third of V is lowered by a semitone, turning V into v. Everything else in the context is identical, so any change in resolution is attributable to that one pitch. The construction yields 184 major-source and 91 minor-source prompt pairs, continued with three seeds each (552 and 273 generation pairs). [PDF p. 3, Fig. 1]

### Causal localisation of harmonic computation

Interchange intervention (activation patching) at each layer measures how much the model's resolution shifts toward the counterfactual when the intervened residual-stream activation is swapped in. Layers 0–5 have little effect; the effect rises from layer 6 and keeps growing, which places harmonic computation in the middle-to-late network rather than at the input. [PDF pp. 3–4, Fig. 3]

### Mode before key

Linear probes on the residual stream (3,176 samples, last token of each bar) show mode peaking at 82.1% around layers 8–9 against 50% chance, while key identity (18 classes, 5.6% chance) stays low until layer 10 and reaches 65.5% by layer 15. The authors read this as a hierarchy: tonal category first, specific tonal centre later. [PDF p. 4, Fig. 4]

### Probe-derived steering, and a representational explanation for its asymmetry

Adding a scaled probe-weight difference to the residual stream redirects resolutions. Parallel-minor steering works at a single layer with a smaller α than relative-minor steering, and the probes explain why: a relative-grouped probe (9 classes by shared key signature) reaches 83.4%, above the 18-class key probe (65.5%) and a parallel-grouped probe (65.3%), and confusion matrices show relative-pair errors dominating. The model's geometry mirrors music theory's distinction between relative and parallel keys. [PDF pp. 5–6, Figs. 5–7]

## 3. Methodology and Architecture

- **Model and data.** Aria, a LLaMA-based autoregressive symbolic transformer, evaluated on Bach chorales with no fine-tuning. [PDF p. 2]
- **Intervention.** Patching the last token's residual-stream activation before generation, one layer at a time, from the minorised run into the original; the outcome metric is interchange intervention accuracy (IIA), the share of generations whose first pitch class belongs only to the counterfactual chord. [PDF pp. 2–3]
- **Probing.** Linear probes for mode (2 classes) and key (18 observed of 2 × 12), trained per layer on the original split. [PDF p. 4]
- **Steering.** Direction v_ℓ = ‖h_ℓ‖ · (w_c1 − w_c2)/‖w_c1 − w_c2‖, added to the residual stream at selected layers and all token positions (or last-bar positions for mode), scaled by α; α is scanned and the strongest harmonic effect reported. [PDF p. 4, eq. 3–4]
- **Quality battery.** Sequence-level structural errors and pitch repetition; note-level out-of-range notes and durations; Fréchet Music Distance (FMD) against Bach chorales; Roman-numeral entropy and top-1 dominance over the first 16 sixteenth-note slots. [PDF pp. 4–5, Table 1]

## 4. Key Results and Benchmarks

**The intervention moves resolution** [PDF p. 3, Fig. 2]: in major-source chorales, tonic resolutions drop from 87.5% to 51.4% under the minorised dominant, with mass moving to vi and others; in minor-source chorales, resolutions to i fall from about 60%.

**Causal localisation** [PDF pp. 3–4, Fig. 3]: IIA stays low for layers 0–5, rises from layer 6, and grows through later layers, with 95% confidence bands.

**Probes** [PDF p. 4, Fig. 4]: mode peaks at 82.1% around layers 8–9 (chance 50%); key reaches 65.5% by layer 15 (chance 5.6%).

**Steering** [PDF p. 5, Fig. 5]: from an 81% baseline of tonic resolutions, a relative-minor direction at α = 0.15 shifts 32% of cases to vi; a parallel-minor direction at α = 0.1 shifts 57% to i; mode steering at α = 0.25 reduces tonic resolutions (110 → 58 cases) but spreads the remainder diffusely and works best when applied only at the last bar positions.

**Quality is preserved** [PDF p. 6, Table 1]: structural-token errors are 0.0% unsteered, 2.9% relative and 0.0% parallel; out-of-range notes 0.0% throughout; mean generated duration ≈3.7 s; FMD 80.27 unsteered, 85.42 relative, 106.65 parallel (the FMD between Bach chorales and Bach fugues is 195.97, which the authors use as scale); Roman-numeral entropy 1.26 → 1.40 → 1.50 bits; top-1 dominance 59.0% → 55.3% → 49.6%.

**Geometry** [PDF pp. 5–6, Figs. 6–7]: relative-grouped probe 83.4%, full key probe 65.5%, parallel-grouped 65.3%; single-layer (layer 12) parallel steering shifts 76 of 118 test cases to the target with FMD 102.05.

## 5. Limitations and Future Work

- **One model, one corpus.** Aria on Bach chorales; the authors state that whether the findings hold for less conventional or more chromatic material is open. [PDF p. 6]
- **A narrow outcome metric.** IIA looks only at the first generated pitch class, not the harmony of the whole continuation.
- **Modest sample sizes.** 184 and 91 prompt pairs, with some probe classes imbalanced, as the paper notes. [PDF p. 4, Fig. 4 caption]
- **Quality is metric-based.** FMD, entropy and structural-error rates stand in for a listening study; no human evaluation is reported.
- **Tuned intervention strength.** α is chosen per condition and differs between relative and parallel steering, so “one controllable direction” is a family of directions with condition-specific scaling.
- **Control, not explanation of a piece.** The experiment shows the model can be steered; it does not show that the directions are stable across contexts or usable as a musician-facing explanation.
- **Declared tool use.** Text polishing used LLMs and experimental code used AI coding agents, with authorship responsibility retained. [PDF p. 7]

## 6. Related Work

- **A template for the repository's explanation standard.** The minimal counterfactual, patching, probing and steering sequence is the strongest published example of the three-claim ladder in [[concepts/music-theory-probing]]: recoverable, causally used, and useful to a person. Only the first two are established here.
- **Comparison with symbolic probing work.** [[explainability-and-auditability/pocwiardowski-2026-mi-midi-mechanistic-interpretability-of]] probes text2midi and MIDI-LLM with prompt patching and steering; Aria's mode/key hierarchy is a second model family and corpus for those questions.
- **Audio-side counterpart.** [[explainability-and-auditability/chen-2026-dual-contrastive-sparse-autoencoders]] runs the same recoverability-then-intervention ladder on audio latents with matched random controls.
- **Theory-grounded representation work.** [[theory-and-constraints/ebrahimzadeh-2026-emergent-tonal-structure-in-learned]] asks what tonal structure emerges in learned representations, and [[theory-and-constraints/mcleod-2020-a-modular-system-for]] supplies the modular harmonic analysis that such probes operationalise.
- **Auditability framing.** [[concepts/auditable-creative-editing-pipelines]] separates workflow transparency, decision auditability, and faithful explanation; steering evidence belongs to the second level plus a partial third.

## 7. Glossary

- **α:** steering strength multiplier.
- **FMD:** Fréchet Music Distance.
- **IIA:** Interchange Intervention Accuracy, here the share of generations whose first pitch class belongs only to the counterfactual chord.
- **ISMIR:** International Society for Music Information Retrieval.
- **LLaMA:** the transformer family Aria is built on.
- **RN:** Roman numeral (chord label).
- **V–I / V–i:** dominant-to-major-tonic and dominant-to-minor-tonic cadences.
- **vi / i:** submediant (relative-minor tonic) and minor tonic.
