---
title: "Symbolic Music Foundation Models"
tags:
  - symbolic-music
  - foundation-models
  - classical-music-generation
  - midi
  - abc-notation
  - controllable-generation
  - auditability
---

# Symbolic Music Foundation Models

The current repository contains two 2025 arXiv preprints that test large-scale pretraining for symbolic music from different starting points. [[generation-and-planning/wang-2025-notagen-advancing-musicality-in-symbolic|NotaGen]] is a 516M-parameter ABC sheet generator followed by curated classical fine-tuning and learned-evaluator preference optimization. [[generation-and-planning/guo-2025-moonbeam-a-midi-foundation-model|Moonbeam]] is a 309M/839M-parameter autoregressive MIDI family adapted to classification and chord/metadata-conditioned generation. Their corpus units, representations, tasks, and evaluations differ, so the useful comparison is architectural and evidential rather than a model leaderboard.

## Evidence Map

| Dimension | NotaGen | Moonbeam | Evidence boundary |
|---|---|---|---|
| Symbolic medium | Interleaved ABC score text with headers, voices, notation, and current/countdown bar labels | Compound MIDI events with absolute onset, duration, octave, pitch class, instrument, and velocity | ABC preserves score spelling/layout; Moonbeam preserves limited expressive timing/velocity but drops controllers and metadata |
| Core architecture | 20-layer patch decoder plus six-layer character decoder, 516M parameters | LLaMA-style causal decoder with MRA and sequential GRU attribute decoder, 309M or 839M | Neither paper isolates model size from representation and corpus effects |
| Pretraining | 1.6M internally curated ABC sheets, augmented across 15 keys | 19 listed datasets, 81.58K hours and 18.06B attribute tokens for Medium | The units are incomparable; both lack a complete deduplicated work-level manifest |
| Adaptation | 8,948 classical sheets, then three CLaMP-DPO iterations | LoRA classification and conditional-generation heads over a frozen base | NotaGen's references reuse fine-tuning material; Moonbeam does not identify the generation checkpoint scale |
| Control | Period–composer–instrumentation prompts and a bar-count horizon | Timed chord controls plus 12 metadata fields in a shared absolute-onset space | Neither verifies harmony, voice leading, cadence, phrase, or form constraints |
| Human evidence | 92 music-college participants; at least 35 valid responses per test group | 20 music experts rating ten paired examples each | NotaGen reports no inferential tests; Moonbeam does not state the Wilcoxon analysis unit |
| Transparency | Prompt, reference set, evaluator score, preference quantile, and policy iteration can be logged | Event fields, relative-attention head groups, conditioning routes, and dataset-license rows are named | Both are structurally auditable; neither provides faithful note-level explanations |

## Representation and Context

NotaGen builds musical simultaneity into text order. Voices belonging to one bar are interleaved, full-rest bars are omitted, and `[r:current/countdown]` labels expose position and intended remaining length. A patch-level decoder models larger character blocks before a character decoder realizes notation. When a context fills, the header and latter half of the generated body seed continuation. This is an explicit length and representation hierarchy, but the paper does not ablate interleaving, rest removal, countdown labels, continuation, or patching, and it does not test long-form structure directly. [NotaGen PDF pp. 2–5]

Moonbeam instead factorizes every MIDI event. Fixed continuous embeddings represent five scalar attributes, a lookup represents instrument identity, and Multidimensional Relative Attention assigns head groups to onset, duration, octave, pitch class, onset-for-instrument, and velocity differences. Transformer inputs use absolute onset while the generated event begins with a categorical time shift. This makes relative timing inspectable in the architecture and supports future-aware control alignment, but the 1,024-event context remains finite and categorical generation retains time/duration limits. [Moonbeam PDF pp. 3–7, 15–17]

These are different inductive biases. NotaGen makes bar/voice organization local in the sequence and gives generation an explicit remaining-length signal. Moonbeam makes event attributes and their pairwise differences explicit. Neither representation contains a verified harmonic function, cadence role, voice-leading obligation, thematic identity, or formal plan. [[concepts/music-domain-inductive-biases]] records the distinction between a useful music-shaped prior and an explanation or rule guarantee.

## Data and Adaptation

NotaGen's broad pretraining corpus is not auditable from the PDF: it is described as 1.6M internal-use ABC sheets without a work manifest, license map, split, or duplicate analysis. Its classical fine-tuning set is more legible by aggregate source, but 6,436 of 8,948 sheets—about 71.9%—are again internal. The model then generates about 100 pieces for each eligible prompt, sends the top and bottom CLaMP 2 similarity deciles to DPO-Positive, and repeats the process three times. CLaMP 2 therefore supplies both preference construction and the headline Average CLaMP 2 Score. [NotaGen PDF pp. 3–6]

Moonbeam Medium names 19 sources and tabulates duration, attribute-token counts, and license labels. That is better provenance visibility, yet three sources dominate the corpus, four license cells are blank, several licenses restrict commercial use, and versions, hashes, work-level deduplication, and mixture weights are absent. Moonbeam adapts the base with LoRA for four classification datasets and with added condition paths for CoMMU generation. PiJAMA is present in pretraining while PiJAMA30 is a downstream benchmark without a documented exclusion boundary. [Moonbeam PDF pp. 6–9, 14–18]

The comparison supports a programme-level requirement: corpus size should never substitute for work identity, provenance, rights, duplicate families, or composer/work-disjoint evaluation. The two papers make valuable large-scale systems possible, but neither lets a reader reconstruct exactly which musical works train and test the reported claims.

## What the Evaluations Establish

For NotaGen, CLaMP-DPO raises the score it directly optimizes across NotaGen, MuPT, and MET. It also generally raises coarse period/instrumentation classifier agreement and shifts descriptive A/B votes toward post-training outputs. The trade-offs matter: MuPT's bar-alignment error worsens from `0.824%` to `4.676%`, secondary metrics sometimes peak before the final iteration, and human ground truth still defeats NotaGen `50.0%` to `41.7%` with `8.3%` no preference. No confidence interval, effect size, participant/item model, or significance test is reported. [NotaGen PDF pp. 6–7]

For Moonbeam, the full Small model has lower reported perplexity than standard attention, an all-attribute rotation, an MLP sub-decoder, and a nominal no-FME condition. Medium leads accuracy and macro-F1 on three of four classification datasets. In conditional generation, the REMI-like baseline is better on objective pitch, velocity, and timing control, while Moonbeam receives higher expert ratings for chord fit, metadata fit, coherence, and enjoyment. This is evidence that the selected objective controls and holistic preference are not interchangeable. The participant-level statistical structure, decoding-budget equality, and generation checkpoint scale remain unclear. [Moonbeam PDF pp. 7–9]

Together, the papers support four bounded conclusions:

1. Large heterogeneous symbolic pretraining can support useful downstream music tasks in both ABC and MIDI settings.
2. Music-shaped representations and adaptation objectives can improve reported predictive, control, or preference outcomes.
3. A proxy can improve while another musically relevant property degrades; one scalar is not a complete definition of musical quality.
4. Semantically named fields, stages, and controls improve auditability without establishing causal explanation or theory compliance.

They do not establish held-out composer/work generation, long-form formal coherence, explicit common-practice rule satisfaction, memorization safety, independent reward validity, calibrated control confidence, or explanation utility.

## Research Direction

A theory-grounded successor could combine the strongest inspectable elements from both systems while adding evidence neither paper provides:

- a work- and composer-disjoint, rights-audited corpus manifest with duplicate-family tracking;
- score-level simultaneity and notation when the task requires readable classical parts, plus expressive event timing where performance control matters;
- explicit form, harmony, cadence, voice-leading, range, texture, and notation constraints with scoped exceptions;
- a learned aesthetic or stylistic critic kept separate from named rule checks;
- a decision ledger recording prompts, references, candidates, rule outcomes, uncertainty, chosen/rejected reasons, and model versions;
- causal tests showing that changing a stated musical reason changes the model decision as predicted;
- human studies that separate quality, style fit, correctness, explanation usefulness, repair efficiency, trust calibration, and creative agency.

[[concepts/hierarchical-latent-reasoning]] adds a tentative architectural hypothesis: slow latent computation could plan form while fast computation realizes notes. HRM does not validate that transfer, so any music system must compare the latent hierarchy against explicit plans, constraints, and intervention-tested traces rather than import a brain analogy as evidence.

## Claim Delta

NotaGen **strengthens** the case that learned-evaluator post-training can move both evaluator-aligned metrics and observed A/B votes across several symbolic encodings. It **narrows** that claim because the evaluator is also the main objective metric, human references still win, and notation validity can degrade.

Moonbeam **strengthens** the case for continuous, semantically factorized music attributes and dimension-specific relative attention in a pretrained MIDI system. It **narrows** transparency claims to architectural auditability: whole-module ablations do not prove that each named dimension causally carries its intended musical relation.

Neither paper contradicts or replaces the repository's existing mashup claims; they establish a new symbolic-generation synthesis route.

## Related Pages

- [[generation-and-planning/wang-2025-notagen-advancing-musicality-in-symbolic]] — ABC generation, classical fine-tuning, CLaMP-DPO, and human-reference comparison.
- [[generation-and-planning/guo-2025-moonbeam-a-midi-foundation-model]] — expressive MIDI representation, MRA, downstream adaptation, and expert evaluation.
- [[concepts/music-domain-inductive-biases]] — how music structure can enter representation, attention, and training without becoming an explanation automatically.
- [[concepts/hierarchical-latent-reasoning]] — slow/fast latent computation and the evidence needed before applying it to long-form music.
