---
title: "Music-Theory Probing"
tags: [music-theory, interpretability, representation-probing, evaluation-validity, causal-faithfulness]
---

# Music-Theory Probing

Music-theory probing trains a supervised predictor on a fixed model representation to test whether a named musical property can be recovered. In [[explainability-and-auditability/wei-2024-do-music-generation-models-encode|Wei et al.'s SynTheory study]], those properties are pitch class, interval, mode, chord quality, progression template, meter, and tempo. A probe's success establishes accessibility to that probe under its evaluation protocol; it does not by itself establish that the generator uses the property to decide what to produce. [Wei et al. PDF pp. 4–6]

## Three Distinct Claims

| Claim | Evidence required | What SynTheory supplies |
|---|---|---|
| Information is recoverable | Predict labels on a defensibly held-out set from fixed representations | High reported linear/MLP-probe results, with unresolved implementation validity concerns |
| The generator uses the concept causally | Intervene on the proposed representation and measure the predicted output change | No such intervention experiment |
| The explanation helps a musician | Test prediction, diagnosis, repair, or calibrated reliance with users | No explanation-utility study |

These are repository distinctions grounded in the study's actual experimental scope. High probing scores cannot substitute for the latter two experiments.

## What a Controlled Dataset Controls

SynTheory crosses tonal labels with 92 timbres and uses synthetic construction to reduce contextual entanglement. This makes labels and stimulus construction inspectable. It does not guarantee that a model learns an abstract rule: pitch/timbre cues, register, template identity, rendering artifacts, and temporal summaries can still support a predictor. Random row splits differ from instrument-, root-, or soundfont-disjoint tests. [Wei et al. PDF pp. 3–5; shortcut and generalization distinctions are repository inference]

The strong handcrafted baselines matter: aggregate features score .936 on the paper's mixed-metric mean, versus .950 for MusicGen Small. Simple concept classification therefore does not uniquely diagnose foundation-model musical reasoning. Both values remain paper-reported; the released evaluation path uses validation-dependent preprocessing, overlaps two tempo values between training and holdout, and does not demonstrate independent test scoring. The paper page records pinned code evidence. The effect on the scores and rankings is unknown. [Wei et al. PDF p. 6 and inspected implementation]

## Evaluation Contract

For future use, the repository recommends fitting preprocessing on training data only and freezing it for validation/test; splitting nuisance factors and unique BPM values according to the generalization claim; selecting layers/hyperparameters on validation; and evaluating selected configurations once on untouched test data. Report per-task metrics and repeated-run uncertainty rather than relying on an average of accuracy and R².

Then test interventions that change the target concept while preserving irrelevant properties. For a symbolic generator, pitch/onset fields or bar hierarchy can define candidate targets, but applying SynTheory-style probes to [[generation-and-planning/guo-2025-moonbeam-a-midi-foundation-model|Moonbeam]] or [[generation-and-planning/wang-2025-notagen-advancing-musicality-in-symbolic|NotaGen]] is a proposed experiment, not a result already held by this repository.

## From Recoverability to Symbolic Intervention

[[explainability-and-auditability/pocwiardowski-2026-mi-midi-mechanistic-interpretability-of|MI-MIDI]] strengthens this evidence base by probing both full symbolic generations and SynTheory MIDI, then testing prompt patching and activation steering in text2midi and MIDI-LLM. Its reported train-fold-only scaling and sequence-grouped cross-validation address specific protocol risks, but post-hoc best-layer selection, heuristic labels, and histogram controls still limit what high accuracy establishes. It is a separate study, not a repair or reproduction of Wei et al.'s audio results. [MI-MIDI PDF pp. 3–6]

The study supplies the intervention evidence absent from SynTheory: piano/violin prompt transfer and bidirectional register/polyphony changes. Its tuned lenses also show that poor early-layer readout through the final vocabulary projection can reflect a basis mismatch rather than missing information. The general three-claim distinction above remains unchanged: neither intervention success nor a readable concept establishes a faithful note-level explanation or utility for musicians. [MI-MIDI PDF pp. 7–12]

For steering, reverse the direction as well as changing its magnitude. MI-MIDI separates antisymmetric response from symmetric drift and uses a note-count stability guard. Its specificity score concerns reversal symmetry of a selected proxy; it does not establish disentanglement from all other musical attributes. Its linked demo uses different source-layer/injection configurations from the main selected results, so the showcase cannot serve as an independent reproduction of those tables. [MI-MIDI PDF pp. 9–12 and pinned demo mapping on the paper page]

[[explainability-and-auditability/chen-2026-dual-contrastive-sparse-autoencoders|DC-SAE]] carries the same ladder to the audio side with corpus structure instead of synthetic control: work-identity probes on held-out recordings establish recoverability, and its rank-1 feature-direction steering — beating a matched-random control in 70% of aligned-pair contexts while the raw residual reference reaches 73.8% — is the intervention step, with absolute margins small and the MERT selection-scoring circularity acknowledged. Musician-utility remains untested there as well. [DC-SAE PDF pp. 3–4, App. K]

## Symbolic Harmony: Localisation and Steering Together

[[explainability-and-auditability/silberschein-2026-harmonic-representations-in-symbolic|Silberschein et al. (2026)]] run the same ladder on tonal harmony in Aria, a LLaMA-based symbolic transformer, and are unusual in making all three evidence types converge on one claim. A single-pitch counterfactual (V → v) drops tonic resolutions in major-source chorales from 87.5% to 51.4%; layer-wise activation patching places the causal effect from layer 6 onward; linear probes recover mode at 82.1% around layers 8–9 (chance 50%) but key identity only from layer 10, reaching 65.5% by layer 15 (chance 5.6%); and probe-derived directions added at inference turn tonic resolutions into relative-minor (32% to vi at α = 0.15) or parallel-minor (57% to i at α = 0.1) ones. Structural errors stay at or below 2.9% and out-of-range notes at 0%. [Silberschein et al. PDF pp. 3–6, Figs. 2–5, Table 1]

Two limits keep this below the third claim. The outcome metric is the first generated pitch class, not the harmony of the whole continuation; quality is measured with FMD, Roman-numeral entropy and structural-error rates rather than listeners; and α is tuned per condition. The representational finding is stronger than the control result: a relative-grouped probe (9 classes by shared key signature) reaches 83.4% against 65.5% for the full 18-class key probe and 65.3% for a parallel-grouped probe, and the confusion matrices show relative-pair errors dominating. The model's geometry, not just its accuracy, mirrors the music-theory distinction. [Silberschein et al. PDF pp. 5–7, Figs. 6–7]

## Related Pages

- [[explainability-and-auditability/pocwiardowski-2026-mi-midi-mechanistic-interpretability-of]] — symbolic probes, lenses, patching, and bidirectional steering.
- [[explainability-and-auditability/chen-2026-dual-contrastive-sparse-autoencoders]] — audio-side probing plus single-feature steering on MusicGen, structured by work identity.
- [[concepts/work-identity-versus-performance-variation]] — the factorization question that DC-SAE's branches instantiate.

- [[explainability-and-auditability/wei-2024-do-music-generation-models-encode]] — primary evidence, full results, and implementation discrepancies.
- [[explainability-and-auditability/silberschein-2026-harmonic-representations-in-symbolic]] — symbolic-harmony case where patching, probing and steering agree on middle-to-late layers.
- [[concepts/music-domain-inductive-biases]] — structural priors and the different evidence needed for constraints or faithful explanations.
- [[concepts/auditable-creative-editing-pipelines]] — moves from reconstructable state to intervention-tested decision explanations.
