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

## Related Pages

- [[explainability-and-auditability/pocwiardowski-2026-mi-midi-mechanistic-interpretability-of]] — symbolic probes, lenses, patching, and bidirectional steering.

- [[explainability-and-auditability/wei-2024-do-music-generation-models-encode]] — primary evidence, full results, and implementation discrepancies.
- [[concepts/music-domain-inductive-biases]] — structural priors and the different evidence needed for constraints or faithful explanations.
- [[concepts/auditable-creative-editing-pipelines]] — moves from reconstructable state to intervention-tested decision explanations.
