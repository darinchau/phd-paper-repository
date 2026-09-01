---
title: "Auditable Creative Editing Pipelines"
tags:
  - auditability
  - transparent-ai
  - mixed-initiative-systems
  - creative-editing
---

# Auditable Creative Editing Pipelines

An auditable creative editing pipeline decomposes generation or transformation into named stages whose inputs, outputs, provenance, decisions, and uncertainty can be inspected and revised without rerunning unrelated stages.

## Core Properties

1. **Named ownership:** each module has a bounded responsibility, such as alignment, selection, structural repair, or mixing.
2. **Provenance:** adopted models, explicit rules, newly trained models, and human decisions remain distinguishable.
3. **Inspectable state:** a decision leaves a durable intermediate such as a grid, score curve, assignment, constraint report, or target descriptor.
4. **Local intervention:** a user can override the intermediate and recompute only dependent stages.
5. **Alternative visibility:** rejected candidates, score margins, and uncertainty remain available rather than only the final choice.
6. **Outcome linkage:** changing an intermediate should change the output in a way consistent with its stated semantics.
7. **Evaluation at the right boundary:** each stage is tested against the quantity it claims to control, rather than only a final holistic preference score.

## Auditability Is Not Yet Explanation

A visible matrix or latent score answers **what the system selected and with what confidence**. It does not automatically answer **why the choice is musically appropriate**, whether the trace is causally faithful to the model, or whether a musician can use it effectively.

Three stronger levels should be distinguished:

- **Workflow transparency:** the stages and data flow are visible.
- **Decision auditability:** inputs, alternatives, scores, constraints, and transformations can be reconstructed.
- **Faithful semantic explanation:** the stated musical reasons are causally connected to the decision and validated for human understanding and correction.

## Evidence From Wu 2026

[[retrieval-and-recombination/wu-2026-an-automated-pop-song-mashup]] is a concrete example of the first two levels. Its downbeat grid, compatibility sweep, Sinkhorn assignment, candidate utilities, and tonal-balance condition expose useful editing state. The mix-conditioning ablation is particularly valuable: malformed partial conditions cause output failures matching their literal semantics, showing that the complete control is load-bearing. [PDF pp. 22–24, 59–63, 80–89 / thesis pp. 6–8, 43–47, 64–73]

The evidence stops short of the third level. OpenL3 and dual-encoder similarities are not mapped to chords or phrase roles; assignment confidence is not calibrated against edit need; the U-Net remains opaque; and no study measures whether explanations improve user understanding, trust calibration, or repair efficiency.

## Design Pattern for Theory-Grounded Music AI

For symbolic or classical music, the same architecture could expose:

- metrical and phrase-boundary maps;
- chord functions, cadence types, and modulation plans;
- voice-leading and range constraints;
- thematic-role and recurrence labels;
- candidate alternatives and violated-rule reports;
- a repair ledger stating which note, phrase, or section changed and why;
- confidence calibrated to the probability that a human editor will intervene.

The crucial test is counterfactual: if the stated reason changes while irrelevant state stays fixed, does the system’s decision change in the predicted way? Human evaluation should then test whether the trace enables faster, more accurate, or more confident correction without inducing over-trust.

## Related Pages

- [[retrieval-and-recombination/wu-2026-an-automated-pop-song-mashup]] — primary evidence anchor.
- [[overviews/automated-music-mashup-systems]] — application-level system map.
- [[questions/when-do-interpretable-music-editing-traces-become-faithful-explanations]] — open research question and tentative validation criteria.
