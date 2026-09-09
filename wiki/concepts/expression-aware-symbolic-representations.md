---
title: "Expression-Aware Symbolic Representations"
tags: [expression-text, musicxml, symbolic-music, provenance, performance]
---

# Expression-Aware Symbolic Representations

An expression-aware representation preserves written instructions alongside notes, including their scope, timing, duration, and type. [[data-and-representation/long-2025-muspyexpress-extending-muspy-with-enhanced|MusPyExpress]] supplies a concrete implementation through score/track annotations and 28 typed classes. It distinguishes a point instruction such as a dynamic marking from a spanner such as a crescendo or slur. [MusPyExpress PDF pp. 2, 7–8]

## Four Distinct Objects

| Object | Example | Evidence or provenance needed |
|---|---|---|
| Source instruction | A printed crescendo across a passage | Score identity, annotation type, scope, onset, and span |
| Model representation | A HairPinSpanner or expression token | Parser and encoding version; handling of unsupported notation |
| Realized performance | A chosen velocity ramp | Rendering rule, parameters, timing convention, and overrides |
| Predicted annotation | A model proposes a crescendo for existing notes | Model version, uncertainty, and human acceptance or correction |

This separation is a repository framework grounded in MusPyExpress's distinct parsing, representation, realization, and tagging stages. A model-added marking should retain its inferred provenance rather than become indistinguishable from the source score. The paper's manually chosen fermata and accent multipliers are configurable performance conventions, not universal interpretations. Its released MIDI export defaults to annotation realization being disabled, and its timing conversion has unresolved expression-handling limitations documented on the paper page. [PDF pp. 4, 8; inspected expressive branch]

## Modeling and Evidence

MusPyExpress tests joint note/expression generation, expression-conditioned note generation, and expression tagging. Prefix and anticipatory interleaving expose future controls differently. The best metrical joint-prefix note perplexity is 2.64 versus a 2.80 baseline, but pitch-class entropy drops to 1.75 against a 2.68 reference. Representation richness and predictive improvement therefore do not establish holistic musical quality. Tagging's best reported total is 33.90% on the validation set, not a reliable automatic transcription of expressive intent. [PDF pp. 3–4, 10]

Compared with [[generation-and-planning/guo-2025-moonbeam-a-midi-foundation-model|Moonbeam]]'s note-level time and velocity fields, expression annotations preserve a higher-level written instruction and its span. Compared with [[generation-and-planning/wang-2025-notagen-advancing-musicality-in-symbolic|NotaGen]]'s score text, MusPyExpress emphasizes typed programmatic access and explicit conversion routes. This is a repository representation comparison; there is no shared benchmark proving one format superior. [[concepts/music-domain-inductive-biases]] explains why preserving a musical concept does not prove causal use or faithful explanation.

## Related Pages

- [[data-and-representation/long-2025-muspyexpress-extending-muspy-with-enhanced]] — defining implementation, experiments, and artifact discrepancies.
- [[concepts/music-domain-inductive-biases]] — distinguishes representation, learned bias, verification, and explanation.
- [[overviews/symbolic-music-foundation-models]] — places score annotations alongside existing generator representations.
