---
title: "Work Identity versus Performance Variation"
tags: [disentanglement, content-style, work-identity, performance-variation, probing, steering, expressive-performance]
---

# Work Identity versus Performance Variation

Which aspects of a musical performance belong to the *work* (the score, the tune, the identity-preserving content) and which belong to its *interpretation* (timing, dynamics, articulation, performer, production) is a long-standing musicological distinction. In this knowledge base it names a concrete modeling question: can a system's representations be **factored** so that one factor carries work identity and another carries performance variation, and what evidence supports such a factorization? Two 2025–2026 papers make the split their primary contribution from opposite directions.

| Paper | Where the split lives | Supervision | Factorization evidence | Intervention evidence |
|---|---|---|---|---|
| [[generation-and-planning/zeng-2025-disentangling-score-content-and-performance]] (Zeng et al. 2025) | Trained into an EPR/APT Seq2Seq system: note-level content latent z_c + single global style vector z_s | Paired/unpaired data, sequence-level alignment only; no work labels beyond the pair structure | Style→composer 77.5% vs content→composer 30.0%; style→performer 42.1% vs 9.9% (ATEPP probes) | 3-sample subjective style-transfer demo; PSR diffusion samples styles from content alone |
| [[explainability-and-auditability/chen-2026-dual-contrastive-sparse-autoencoders]] (Chen et al. 2026) | Recovered from a frozen MusicGen's residual stream by a two-branch contrastive SAE | Work ids only (performer labels evaluation-only) | z_i work-ID probe 0.856 classical (chance 0.020); z_j same-recording 0.670–0.712 under held-out augmentation; emergent performer probes | Rank-1 z_j feature steering beats matched-random in 70% of aligned-pair contexts |

Three observations generalize across both:

1. **Composer signal is easier than performer signal, and leaks into style.** Zeng et al.'s style vector classifies composer (77.5%) far above performer (42.1%); Chen et al.'s variation branch carries performer information but "entangled with repertoire, arrangement, and recording context." Both papers attribute part of this to real musicians aligning their interpretation with the composer's conventions — the entanglement is in the data-generating process, not only the model.
2. **The boundary is tradition-dependent.** Chen et al.'s classical cohort separates decisively while jazz standards barely do (work-ID z_i 0.856 vs 0.136): a "work" with a thick score-bound identity factorizes; a standard realized flexibly does not. Any claim of a universal content/style split must say which notion of work identity it assumes.
3. **Recoverability is not causal use.** Both factorizations rest primarily on probes. Zeng et al. demonstrate transfer with a 3-sample subjective test; Chen et al. add a single-feature steering intervention with small absolute margins and an acknowledged selection-scoring circularity. Neither yet shows a controlled perceptual test that swapping exactly one factor changes exactly the intended perceptual attribute — the intervention standard from [[concepts/music-theory-probing]].

[[generation-and-planning/borovik-2025-symupe-affective-and-controllable]] (PianoFlow) treats the same expressive dimension without factorizing it: it conditions rendering on emotion/text embeddings while preserving the score by construction (the score is the input), leaving the work/interpretation boundary implicit in the data rather than explicit in the architecture.

For source attribution and mashup research, this concept marks what a "source" is: a work-level factor, a performance-level factor, or a recording artifact. [[explainability-and-auditability/storan-2026-group-invariant-statistics-determine-embedding]] shows how embedding geometry encodes such invariances more generally, and [[concepts/expression-aware-symbolic-representations]] keeps the written-instruction layer distinct from realized performance features.

## Related Pages

- [[generation-and-planning/zeng-2025-disentangling-score-content-and-performance]] — trained content/style split in a symbolic EPR/APT system.
- [[explainability-and-auditability/chen-2026-dual-contrastive-sparse-autoencoders]] — recovered identity/variation split from MusicGen internals.
- [[generation-and-planning/borovik-2025-symupe-affective-and-controllable]] — expressive rendering with text/emotion control, no factorization claim.
- [[concepts/music-theory-probing]] — evidence ladder (recoverable / causal / useful) for factorization claims.
- [[concepts/expression-aware-symbolic-representations]] — written expression instructions vs realized performance features.
