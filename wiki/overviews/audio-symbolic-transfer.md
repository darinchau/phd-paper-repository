---
title: "Audio–Symbolic Music Transfer"
authors: "PhD research repository"
year: 2026
doi: ""
category: ""
source_collection: "repository synthesis"
source_format: "markdown"
extracted_date: 2026-10-21
---

# Audio–Symbolic Music Transfer

**TL;DR:** Audio can supply symbolic training data at piano scale and can be aligned to symbolic representations well enough for coarse retrieval, but no paper here isolates *what* a symbolic model learns from audio, and no system gives a reliable note-level audio–symbolic space — that decomposition is the open, feasible line.

## Scope and Evidence Boundary

This page synthesises ten arXiv papers read in full on 2026-10-21, all requested as one batch: Aria-MIDI, Aria (scaling self-supervised symbolic learning), CLaMP 3, PianoBind, descriptor-injected audio–MIDI alignment, the MusicBERT representation analysis, SymPAC, FGG, YourMT3+, and spectrogram diffusion. The batch covers four mechanisms, not one literature: hard transcription, joint embedding, inverse synthesis, and representation probing. Numbers below are author-reported and anchored on the paper pages; none has been independently replicated here. The batch is piano-heavy: six of the ten papers are solo-piano or piano-first, and the two multi-instrument systems (SymPAC, YourMT3+) are the ones with the weakest public reproducibility.

## Evidence Map

| Paper | Route | Scale | Headline result | Main caveat |
|---|---|---|---|---|
| Aria-MIDI (2025) | Hard transcription | 1.19M files / ~100k h; 801k / 66.7k h after dedup | Largest public solo-piano symbolic corpus | Piano only; transcription accuracy not re-measured |
| Aria (2025) | Hard transcription + SSL | 60,473 h; 650M params | Composer probe 90.5% vs 84.5% (CLaMP 3); listening test ties Suno/human | Piano only; corpus inherits AMT errors |
| SymPAC (2024) | Hard transcription, multi-track | ~1M in-house tracks; 86M params | MOS 3.60 vs 2.74 (FIGARO); 87.2% chord control | Unreleased corpus; 1/16-bar grid; 12 triads |
| YourMT3+ (2024) | Transcription model | 10 public datasets | Slakh Multi F1 84.6 vs 75.2 (MT3) | <10% F1 on non-main pop instruments |
| CLaMP 3 (2025) | Joint embedding (text bridge) | 2.31M pairs; 8×H800 | Paired retrieval SOTA; emergent audio↔symbolic MRR 0.03–0.06 | Weak audio–symbolic alignment; global pooling |
| PianoBind (2025) | Joint embedding (piano-specific) | 900 h weak + 17 h expert | MedR 10 vs 39 (CLaMP 3) in-domain | 199/88-item tests; pop-piano only |
| Descriptor injection (2026) | Joint embedding (hand-crafted priors) | MAESTRO 13k segments; 74M params | S 73.4 → 84.0; A4 ablation −75 to −78 pp | Brittle: velocity/octave changes give S < 18% |
| MusicBERT analysis (2023) | Probing | 9.97M bars | Objective- and layer-dependent attribute decoding | Correlational; no generation/retrieval test |
| FGG (2025) | Symbolic generation control | POP909, 88 test pieces | 0.0% out-of-key; chord acc 0.485 vs 0.314 | Four-bar pop; 16th-note grid |
| Spectrogram diffusion (2022) | Inverse synthesis | 6 datasets, 16k-h inverter | Beats AR decoder; F1 0.36 = inverter ceiling | No listening test; fidelity bounded by vocoder |

## Four Routes From Audio to Symbolic

### 1. Hard transcription: audio → notes → train

Aria-MIDI and SymPAC are the two scale demonstrations. Aria establishes that solo-piano transcription is good enough to train a 650M model that matches human continuations in a listening test; SymPAC establishes that a multi-track MIR stack (transcription + beat tracking + chords + sections + tags) can train a controllable generator without any human symbolic corpus. YourMT3+ defines the quality ceiling that limits the multi-track version: strong on synthetic Slakh, below 10% F1 for non-main instruments on real pop mixes.

The unresolved issue is not "can it be done" but "what exactly is learned". Every corpus is defined by a transcriber, and no paper here measures how transcription errors propagate into generation, retrieval, or control. Aria's listening test compares against human MIDI-trained baselines only indirectly (it compares outputs, not training conditions); SymPAC compares datasets, not transcription qualities.

### 2. Joint embedding: audio and symbolic in one space

Three designs appear. CLaMP 3 uses text as a bridge and never requires paired audio–symbolic data; its emergent audio↔symbolic retrieval is 4–8× random but an order of magnitude below symbolic↔symbolic (MRR 0.03–0.06 vs 0.31–0.53). PianoBind aligns each modality to text and fuses at inference, winning on piano retrieval but not producing note-level correspondence. Descriptor injection adds hand-crafted spectral and interval features directly to a dual encoder; it raises retrieval by 8.8 points and gives clean causal evidence that the audio descriptor carries the gain, but the model collapses under transposition and velocity change.

The convergent finding: coarse, global alignment is achievable; fine-grained, robust alignment is not. CLaMP 3's own limitation — one global vector cannot represent temporal development — is the structural reason. A mashup or repair system needs to know *which notes* conflict, not just that two pieces are similar.

### 3. Inverse synthesis: symbolic → audio

Spectrogram diffusion is the cleanest statement of the inverse problem: the same MT3 note vocabulary that transcribes audio can synthesise it, and the note model reaches the spectrogram inverter's ceiling (transcription F1 0.36) while raw audio allows 0.63. This matters for the programme in two ways. First, it supplies a differentiable or at least learnable renderer for symbolic data, which is the basis of any "render → embed → compare" distillation. Second, it shows that the audio representation, not the symbolic sequence, is often the limiting factor — a caution for any claim that symbolic structure is the bottleneck.

### 4. Probing: what is in a symbolic representation

The MusicBERT analysis is the methodological template the other papers lack. Seven probes (chords, groove, instruments, tempo, velocity, duration, song clustering) show that a bar-level embedding contains different information depending on the contrastive objective and the layer; the last layer is often not the best. Aria applies linear probes at much larger scale and gets SOTA, but only for genre/form/period/composer/pianist/dataset — labels that are coarse and metadata-derived. No paper probes the distinction that matters most for "what transfers": performance/expressive information versus compositional/score-level information.

## What Actually Transfers: A Factor Decomposition

The batch supports a tentative decomposition. "Transfer" is not one thing; at least four factor groups behave differently.

| Factor group | Examples | Evidence that audio-derived data carries it | Evidence that it is separable |
|---|---|---|---|
| Expressive performance | Timing micro-variation, velocity, pedal, articulation | Aria's tokenizer keeps 10 ms timing and 12 velocity bins; listening test rewards coherent performance; MIDI-only models trained on scores lack these cues | No paper trains matched models with/without performance timing and probes the difference |
| Instrumentation / timbre | Instrument identity, orchestration, timbre | YourMT3+ and spectrogram diffusion learn instrument-conditioned tokens; PianoBind's audio branch improves retrieval | CLaMP 3 pools globally; descriptor A4 may encode room/recording as much as instrument |
| Compositional structure | Chords, metre, motifs, form, cadence | MusicBERT probes decode chords/groove; SymPAC's section/chord tokens control structure | Probes are bar-local; no cadence/phrase/voice-leading probe; Aria discards metre and key |
| Recording/style context | Genre, era, performer, room | Aria's composer/pianist probes; CLaMP 3's genre/period retrieval | Metadata labels are LLM-extracted; confounded with composer/genre imbalance |

The table is a hypothesis, not a measured decomposition. The closest measured result is the MusicBERT objective trade-off (augmentation preserves chords but destroys velocity; same-piece contrast preserves song identity but overfits), which shows that the training signal selects which factor group is invariant. The closest causal result is descriptor injection (A4 is necessary; D4 is a training regulariser), which shows that a single hand-crafted feature can dominate the learned alignment.

## Where the Evidence Is Thin

1. **No matched-corpus transfer experiment.** Nobody trains the same model on (a) human score MIDI, (b) human performance MIDI, (c) transcribed MIDI from the same performances, and (d) transcribed MIDI from different audio, then probes the same factor set. Aria compares to external models, not to a controlled corpus swap.
2. **No transcription-error dose–response.** No paper varies transcription quality (e.g., by degrading labels or using weaker transcribers) and measures downstream generation/retrieval.
3. **No multi-instrument public replication.** SymPAC's corpus is in-house; YourMT3+'s real-world performance is weak; Slakh is synthetic. "Getting past piano" currently means "get past piano on rendered or in-house data".
4. **No note-level cross-modal benchmark.** CLaMP 3 and PianoBind evaluate global retrieval; descriptor injection evaluates segment retrieval. None evaluates whether a system can point to the notes that make two recordings the same work.
5. **No score-level recovery.** Audio-to-score transcription (metre, spelling, voices, notation) is out of scope in every paper here; Aria explicitly discards metre/key, SymPAC quantises to a beat grid, and FGG assumes a supplied chord/rhythm mask.

## Cross-Modal Evidence Outside This Batch

A companion synthesis ([[overviews/cross-modal-supervision-transfer]]) covers the general cross-modal literature and five music systems added on 2026-10-22. Three points sharpen the picture:

- **The general principle is conditional.** A second modality helps when it carries information the first lacks; when it is redundant, gains vanish, and one branch can dominate so that multimodal training loses to unimodal training ([[other/wu-2022-characterizing-and-overcoming-the-greedy]]).
- **The strongest music result runs in the reverse direction.** MIDI-REPA aligns AMT-derived piano rolls into a text-to-music DiT and ranks first on the ATTM benchmark at 14.2 A100-equivalent GPU-hours; a noisy Basic Pitch teacher is worse than no alignment ([[generation-and-planning/yu-2026-midi-repa-improving-text-to-music]]). This shows symbolic supervision improving audio generation, not audio supervision improving a symbolic representation.
- **Audio→symbolic systems exist at task level, not at representation level.** Audio-to-symbolic arrangement ([[generation-and-planning/wang-2022-audio-to-symbolic-arrangement-via-cross-modal]]) and cross-modal bootstrapping ([[generation-and-planning/zhao-2026-learning-music-style-for-piano]]) use audio to produce symbolic output, and SMART ([[generation-and-planning/jonason-2025-smart-tuning-a-symbolic-music]]) uses an audio reward to tune a symbolic generator. None measures what the symbolic model internalised, and none provides note-level attribution.

Consequence: the "no matched-corpus transfer experiment" and "no note-level benchmark" gaps below still stand. The defensible version of the premise is narrower than "what does audio teach symbolic models": it is **what audio adds that MIDI lacks, measured on a perceptual target**.

## Implications for the Mashup/Repair Programme

- **Audio-derived data is a performance prior, not a score prior.** It is well suited to learning expressive rendering, timbre, and performer style; it is poorly suited to learning notation-level voice leading, spelling, or cadence unless those are added as explicit labels.
- **A global audio embedding is not enough for compatibility or repair.** CLaMP 3's and PianoBind's global vectors can retrieve candidates, but they cannot localise a conflict or justify a note-level repair. A usable system needs bar/note-level alignment or an attribution mechanism.
- **Rendered audio is the clean control.** If the question is "what does audio add to a symbolic model", rendering symbolic data to audio gives an exact pairing and removes the transcriber from the causal chain. Slakh is the public multi-instrument option; MAESTRO is the piano option. The synthesis paper shows the renderer's ceiling, which must be reported.
- **Transcription noise may be useful augmentation — or a confound.** No paper separates these. A dose–response study is cheap relative to training a new corpus and would directly inform whether to invest in better transcription or in noise-robust training.
- **Control technology is ready.** FGG and SymPAC show that hard harmonic/structural constraints can be enforced at sampling time. If audio-derived data supplies the material, these methods supply the inspectable control surface a mashup/repair system needs.

## Feasibility Ranking for a New Line

| Candidate | Data cost | Compute cost | Novelty risk | Fit to programme | Verdict |
|---|---|---|---|---|---|
| **Transfer decomposition** (matched corpora × probe suite) | Low: existing MAESTRO/Aria-MIDI/ASAP-style data | Low–medium: small probes, few training runs | Low–medium: MusicBERT probes exist, but not the corpus-swap design | High: directly answers "what transfers", feeds mashup/repair feature choice | **Best first step** |
| **Rendered-audio distillation** (Slakh/MAESTRO → MERT → symbolic encoder) | Medium: Slakh subset, MAESTRO | Medium: MERT inference + small contrastive training | Medium: CLaMP 3/descriptor work is adjacent; exact rendered-pair setup is less covered | High: gives audio-grounded symbolic embeddings and an explainability hook | **Strong second step / merge with first** |
| **Transcription-noise dose–response** | Low: reuse Aria-MIDI + MAESTRO | Low: CPU/one GPU for small models | Low: nobody in this batch does it | High: tells you whether to chase transcription quality | **Cheap add-on** |
| **Multi-instrument transcription corpus** | High: audio rights, MIR stack, storage | High: GPU-days to weeks | High: SymPAC occupies the in-house version; public version is hard | Medium: necessary for "past piano" but not a first project | **Defer** |
| **Note-level audio–symbolic benchmark** | Medium: paired renditions | Low–medium: annotation/alignment | High: could be a contribution, but evaluation design is the hard part | High: enables compatibility/repair claims | **Good paper-sized project after a pilot** |

The two interests named by the owner — "getting past piano" and "what actually transfers" — are not separate projects. The cheapest way to pursue both is a **rendered multi-instrument transfer study**: use Slakh (exact MIDI/audio pairs, many instruments), render or use its stems, distil an audio foundation model into a symbolic encoder, and evaluate a factor-decomposed probe suite (instrument, dynamics, articulation, genre, composer/work, metre, chord). That design gets multi-instrument coverage without a transcription pipeline, and it measures transfer rather than assuming it. A piano-only version on MAESTRO/Aria-MIDI is the fallback if Slakh's size or licences are a problem.

## Acronyms

- **AMT:** Automatic Music Transcription.
- **CKA:** Centered Kernel Alignment.
- **CLaMP:** Contrastive Language–Music Pretraining.
- **FAD:** Fréchet Audio Distance.
- **FGG:** Fine-Grained Guidance.
- **FSM:** Finite State Machine.
- **GAN:** Generative Adversarial Network.
- **LLM:** Large Language Model.
- **MERT:** Music Understanding Model with Large-Scale Self-Supervised Training.
- **MIDI:** Musical Instrument Digital Interface.
- **MIR:** Music Information Retrieval.
- **MIR data:** here, the outputs of transcription/beat/chord/section/tagging models.
- **MoE:** Mixture of Experts.
- **MOS:** Mean Opinion Score.
- **MRR:** Mean Reciprocal Rank.
- **MT3:** Multi-Task Multitrack Music Transcription.
- **NT-Xent:** Normalized Temperature-scaled Cross-Entropy loss.
- **REMI+:** multi-track Revamped MIDI encoding.
- **SSL:** Self-Supervised Learning.
- **SOTA:** State of the Art.
- **VICReg:** Variance–Invariance–Covariance Regularization.

## Related Pages

- [[overviews/cross-modal-supervision-transfer]] — general evidence on when a second modality improves the first.
- [[generation-and-planning/yu-2026-midi-repa-improving-text-to-music]] — symbolic supervision of audio generation.
- [[generation-and-planning/jonason-2025-smart-tuning-a-symbolic-music]] — audio reward for symbolic generation.
- [[generation-and-planning/wang-2022-audio-to-symbolic-arrangement-via-cross-modal]] — audio-to-symbolic arrangement.
- [[generation-and-planning/zhao-2026-learning-music-style-for-piano]] — audio style for symbolic arrangement.
- [[data-and-representation/won-2024-a-foundation-model-for-music]] — audio-only foundation model and teacher candidate.
- [[concepts/transcription-as-supervision]] — the label chain and its failure modes.
- [[concepts/audio-symbolic-modality-gap]] — why alignment is hard even with pairs.
- [[concepts/music-theory-probing]] — probe design and construct validity.
- [[data-and-representation/bradshaw-2025-aria-midi-a-dataset-of]] — the corpus.
- [[data-and-representation/bradshaw-2025-scaling-self-supervised-representation]] — the strongest downstream evidence.
- [[data-and-representation/chang-2024-yourmt3-multi-instrument-music-transcription]] — the multi-instrument ceiling.
- [[generation-and-planning/chen-2024-sympac-scalable-symbolic-music]] — multi-track generation from MIR outputs.
- [[generation-and-planning/hawthorne-2022-multi-instrument-music-synthesis-with]] — inverse synthesis and its ceiling.
- [[generation-and-planning/zhu-2025-efficient-fine-grained-guidance-for]] — hard symbolic control.
- [[retrieval-and-recombination/wu-2025-clamp-3-universal-music]] — text-bridged alignment.
- [[retrieval-and-recombination/bang-2025-pianobind-a-multimodal-joint]] — piano-specific alignment.
- [[retrieval-and-recombination/fernandez-mendez-2026-descriptor-injected-cross-modal-learning]] — descriptor injection.
- [[explainability-and-auditability/han-2023-systematic-analysis-of-music]] — probing methodology.
- [[overviews/symbolic-music-foundation-models]] — the generation-side foundation-model context.
