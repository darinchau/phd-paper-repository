---
title: "Music-Domain Inductive Biases"
tags:
  - symbolic-music
  - inductive-bias
  - representation
  - relative-attention
  - theory-grounding
  - explainability
---

# Music-Domain Inductive Biases

A music-domain inductive bias is a structural assumption that makes some musical relationships easier for a model to represent or learn. It can enter through sequence order, event fields, embeddings, attention geometry, conditioning, architectural hierarchy, or a training objective. A named musical bias is not automatically a theory constraint, and neither is automatically a faithful explanation.

## Evidence in the Current Papers

[[generation-and-planning/wang-2025-notagen-advancing-musicality-in-symbolic|NotaGen]] uses four visible biases. Interleaved ABC places simultaneous voices from one bar together; full-rest removal changes information density; bar-stream patches introduce a score-aligned representation hierarchy; and current/countdown labels provide an explicit length horizon. Its `period-composer-instrumentation` prompts and CLaMP-DPO objective then favor candidates close to a prompt-conditioned centroid of authentic reference embeddings. [NotaGen PDF pp. 2–6]

These choices are musically motivated, but their roles are not isolated. The paper does not ablate interleaving, rest removal, countdown labels, patch hierarchy, or stream continuation. CLaMP similarity is learned and latent: it may encode style and complexity, but it does not state which chord, voice-leading relation, cadence, form, or notation property caused a preference. The pipeline is reconstructable; the musical rationale is not.

[[generation-and-planning/guo-2025-moonbeam-a-midi-foundation-model|Moonbeam]] exposes a different family of biases. Each event is split into absolute onset, duration, octave, pitch class, instrument, and velocity. Continuous Fundamental Music Embeddings handle the five scalar fields, while Multidimensional Relative Attention assigns head groups to differences along named attribute axes. Timed chord controls share the same absolute-onset coordinate as generated events. [Moonbeam PDF pp. 3–7, 15–18]

Moonbeam's complete design reaches perplexity `2.423`, versus `2.512` with standard attention and `2.512` with a rotation that mixes all attributes in every head. This whole-module ablation supports the usefulness of the selected design on one split. It does not show that each head group uses its assigned dimension causally, that the representation is equivariant under musical transformations, or that attention explains a generated event. [Moonbeam PDF pp. 7–8]

## Four Levels That Should Not Be Collapsed

1. **Music-shaped representation:** notes, voices, bars, onset, duration, pitch, instrument, and velocity are explicit rather than hidden inside arbitrary tokens.
2. **Architectural inductive bias:** model connectivity or geometry privileges a relation, such as simultaneous bar content or relative pitch/onset differences.
3. **Constraint or verifier:** an explicit predicate checks a scoped claim, such as voice range, metrical duration, cadence type, or parallel-motion rule, with documented exceptions.
4. **Faithful explanation:** the surfaced reason is causally connected to the decision and helps a person predict, diagnose, or repair model behavior.

NotaGen and Moonbeam provide strong examples of levels 1–2. NotaGen's bar-alignment error is one narrow level-3 check for duration, not a general notation or theory verifier. Neither paper establishes level 4.

## Validation Contract

A proposed music-domain bias should be tested at the level of the claim it makes:

- **Component ablation:** remove or permute each named dimension while matching parameter and training budgets.
- **Transformation tests:** measure predicted invariance or equivariance under transposition, tempo scaling, metrical displacement, velocity shift, instrumentation change, or notation-preserving rewrites.
- **Out-of-distribution tests:** include unseen values, composers, works, ensembles, meters, keys, and lengths without pretraining leakage.
- **Counterfactual intervention:** change the proposed musical reason while controlling irrelevant state and test whether the output changes in the predicted direction.
- **Conflict and exception handling:** record when learned preference, explicit theory rules, playability, notation, and user intent disagree.
- **Human utility:** test whether the surfaced structure improves prediction, diagnosis, repair, trust calibration, or creative control—not merely whether listeners prefer the final output.

For classical symbolic generation, the next step is not to replace learned biases with brittle universal rules. It is to keep representation, learned preference, explicit constraints, legitimate stylistic exceptions, and human overrides separate enough that their contributions and failures can be inspected.

## Related Pages

- [[overviews/symbolic-music-foundation-models]] — comparative evidence across the two ingested symbolic pretraining systems.
- [[generation-and-planning/wang-2025-notagen-advancing-musicality-in-symbolic]] — interleaved ABC, bar-count planning, hierarchical patches, and learned-evaluator feedback.
- [[generation-and-planning/guo-2025-moonbeam-a-midi-foundation-model]] — continuous attribute embeddings and dimension-specific relative attention.
- [[concepts/auditable-creative-editing-pipelines]] — separates inspectable workflow state from faithful semantic explanation.
