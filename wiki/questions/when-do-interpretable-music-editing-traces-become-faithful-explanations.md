---
title: "When Do Interpretable Music-Editing Traces Become Faithful Explanations?"
tags:
  - explainability
  - faithfulness
  - human-evaluation
  - music-editing
---

# When Do Interpretable Music-Editing Traces Become Faithful Explanations?

## Question

When can an intermediate such as a downbeat map, similarity curve, assignment matrix, confidence score, or tonal-balance target be treated as a faithful explanation of a music-editing decision rather than merely a visible trace?

## Sharper Follow-up

What combination of causal tests, musical semantics, uncertainty calibration, and human-usefulness evidence is sufficient before such a trace should guide autonomous repair or user trust?

## What the Knowledge Base Holds

[[retrieval-and-recombination/davies-2014-automashupper-automatic-creation-of-multi]] specifies a handcrafted decision that is reconstructable in principle:

- harmonic, kick/snare rhythmic, spectral-balance, and tempo terms;
- user-selected weights and transform ranges;
- internally computed winning source passage, key shift, beat mapping, and gain change;
- user-visible source assignments, parameter controls, ranked song names, and local replacement controls. [PDF pp. 3–7 / article pp. 1728–1732]

The paper does not show every internal quantity surfaced to the user or persistently logged. Nevertheless, the specified computation explains **how the formula produced the ranking** in principle. Its listening study shows why that is not yet a complete musical explanation: middle and bottom conditions are not distinguished, the overall score–enjoyment correlation is only `r = .49`, and vocal overlap, bass interaction, off-downbeat chord changes, and familiarity create failures outside the feature vocabulary. [PDF pp. 9–11 / article pp. 1734–1736]

[[retrieval-and-recombination/wu-2026-an-automated-pop-song-mashup]] exposes several kinds of intermediate state:

- deterministic downbeat anchors and timemaps;
- OpenL3 candidate utilities;
- vocal/accompaniment cosine sweeps;
- Sinkhorn assignments and row confidence;
- a 31-band vocal-relative tone-and-level condition;
- before/after restoration metrics. [PDF pp. 22–24, 32–42, 49–63, 80–89 / thesis pp. 6–8, 16–26, 33–47, 64–73]

The paper provides one strong causal clue: full mix conditioning improves pooled SI-SDR by 6.67 dB over condition dropping, while inference-only partial maps produce failures that follow their literal but malformed semantics. [PDF pp. 88–89 / thesis pp. 72–73]

Other traces remain less established. Assignment confidence is illustrated on one compatible/incompatible pair but not calibrated to listener judgment or intervention need. Ranking features predict preferences without human-readable musical reasons. The alignment maps are inspectable but not evaluated against annotated timing or perceived artifacts. Chapter 5’s use of confidence to trigger editing is explicitly future work. [PDF pp. 33–34, 40–42, 61–63, 91–95 / thesis pp. 17–18, 24–26, 45–47, 75–79]

## Tentative Answer

A music-editing trace should count as a faithful explanation only when all four conditions hold:

1. **Causal sensitivity:** controlled changes to the trace produce the predicted changes in the decision or output, while irrelevant changes do not.
2. **Semantic validity:** the trace maps to musical concepts that domain users can interpret, not only to unnamed embedding dimensions.
3. **Calibrated scope:** confidence and failure boundaries are measured on held-out music representative of intended use.
4. **Demonstrated utility:** musicians use the explanation to detect errors, choose alternatives, or repair outputs more effectively, with trust calibrated to actual reliability.

Davies satisfies formula-level reconstruction and workflow visibility but shows that an explicit score can omit important causes of listener judgment. Wu satisfies parts of causal sensitivity and workflow visibility, especially for the complete tonal-balance condition. Neither satisfies the full set for compatibility, alignment, or agent planning. The appropriate label is therefore **auditable creative editing**, not fully validated explainable AI.

## Related Pages

- [[concepts/auditable-creative-editing-pipelines]] — terminology and design criteria.
- [[overviews/automated-music-mashup-systems]] — system context.
- [[retrieval-and-recombination/davies-2014-automashupper-automatic-creation-of-multi]] — explicit Mashability and transform traces.
- [[retrieval-and-recombination/wu-2026-an-automated-pop-song-mashup]] — primary paper evidence.
