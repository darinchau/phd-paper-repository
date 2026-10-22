# Cross-Modal Supervision and Transfer

## Scope and Evidence Boundary

This page asks a general question that the audio↔symbolic programme depends on: **when does adding a second modality improve what a model learns in the first?** It covers twelve imported papers: seven general cross-modal results (vision–audio, RGB–depth, vision–language) and five music-specific systems. It is not a survey of multimodal learning; it is the evidence needed to judge whether "audio teaches symbolic" is a plausible premise and where the gain should appear.

The page distinguishes three settings that are often conflated:

1. **Joint training, joint inference** — both modalities are present at test time (Look, Listen and Learn).
2. **Privileged training, single-modality inference** — the extra modality is used only as a teacher or side information (SoundNet, modality hallucination, modality distillation).
3. **Conditioning at inference** — an external modality embedding steers a frozen generator (cross-modal bootstrapping, SMART).

Only setting 2 is the direct template for a symbolic model that must run without audio at inference.

## Evidence Map

| Paper | Setting | What the second modality supplies | Result |
|---|---|---|---|
| SoundNet (Aytar et al. 2016) | Privileged teacher | Visual object/scene semantics | DCASE 88% vs 78% prior; ESC-50 74.2% vs 64.5% |
| Look, Listen and Learn (Arandjelović & Zisserman 2017) | Joint, self-supervised | Audio–visual correspondence | ESC-50 79.3% vs 74.2% SoundNet; ImageNet 32.3% |
| Multimodality Helps Unimodality (Lin et al. 2023) | Joint encoder, unimodal probe | Text/audio as extra few-shot examples | 1-shot cross-modal beats most prior 2-shot methods |
| What Makes Multi-modal Learning Better (Huang et al. 2021) | Theory | Better estimate of a shared latent | Multimodal population risk < subset risk, under assumptions |
| Greedy multimodal learning (Wu et al. 2022) | Diagnosis | — | One modality can dominate; multimodal can lose to unimodal |
| Modality hallucination (Hoffman et al. 2016) | Privileged training, RGB inference | Depth mid-level features | Beats RGB-only and RGB-ensemble on NYUDv2 |
| Modality distillation (Garcia et al. 2018) | Privileged training, RGB inference | Depth features via a hallucination stream | State-of-the-art RGB-only NTU RGB+D |
| MIDI-REPA (Yu et al. 2026) | Symbolic → audio | AMT piano rolls as an alignment target | Rank 1 ATTM Borda; FAD 0.497, CLAP 0.315 |
| SMART (Jonason et al. 2025) | Audio reward, symbolic output | Audio aesthetic score | +1.22 listener rating points; diversity collapse under over-optimisation |
| Audio-to-symbolic arrangement (Wang et al. 2022) | Audio → symbolic generation | Chord, texture, groove | Beats baselines on four listening criteria |
| Cross-modal bootstrapping (Zhao et al. 2026) | Audio style → symbolic generation | Groove, dynamics, texture | Better style coherence and musicality than piano-cover baselines |
| MusicFM (Won et al. 2024) | Audio-only SSL | — (control/teacher candidate) | Beat F1 0.868; competitive with MERT |

## The Principle

The consistent finding is conditional, not universal: **the second modality helps when it carries information the first modality lacks for the target task.**

- Vision helps sound because scenes and objects predict what a sound is (SoundNet).
- Audio helps vision because co-occurrence is free supervision and sounding objects are visually distinctive (Look, Listen and Learn).
- Depth helps RGB because geometry is not fully recoverable from appearance (hallucination, distillation).
- Text helps images because class names and descriptions add semantic evidence (Multimodality Helps Unimodality).
- Symbolic scores help audio generation because melody, rhythm, and harmony are compact and sparse, while audio must also model timbre and production (MIDI-REPA).

When the extra modality is redundant, or when optimisation lets one branch dominate, the gain disappears or reverses (Wu et al. 2022). The theory explains the positive case: more modalities give a better estimate of a shared latent cause (Huang et al. 2021), but that assumes the modalities really are generated from a shared latent and that the model can estimate it.

## What This Predicts for Audio → Symbolic

MIDI already contains notes, onset times, durations, velocities, and instrument programs. Audio adds information that MIDI does not encode:

- timbre and spectral blend;
- masking and roughness when instruments overlap;
- perceived loudness balance and production;
- performance nuance that survives rendering but is flattened in symbolic tokens.

It does **not** add new information about pitch class, metre, or chord labels. Therefore the prediction is sharp:

- **Structure probes should stay flat** when audio supervision is added; a large gain there would be suspicious or evidence of a leak.
- **Perceptual/acoustic probes should move** if the teacher is valid and the student does not take a shortcut.
- **A null on everything** is informative only after checking utilisation: the student may have ignored the teacher (Wu et al. 2022), or the teacher may encode instrument identity rather than the target property.

This is exactly the design constraint that the AGT line adopts: a predicted-null structure battery, a perceptual target, and instrument-only plus shuffled controls.

## Music-Specific Evidence

- **Symbolic → audio is established.** MIDI-REPA shows that AMT-derived piano rolls improve a text-to-music DiT, and that noisy AMT targets (Basic Pitch) can hurt. The direction works when the symbolic target is accurate.
- **Audio → symbolic exists at task level.** Audio-to-symbolic arrangement and cross-modal bootstrapping both use audio to produce symbolic output. Bootstrapping is the stronger analogy to AGT because the audio supplies style/groove that the lead sheet lacks, and the gain is measured on style coherence. But both systems require the audio at inference (as input or reference), so they do not show that a symbolic model has internalised audio-side knowledge.
- **Audio reward can tune symbolic generation** (SMART), but the evidence is output-level, the sample is small, and the proxy is known to be gameable.
- **No paper in this set tests whether audio supervision makes a symbolic representation better at anything, with controls for instrument identity and transcription noise.** Aria's symbolic model, trained on transcriptions but evaluated as a symbolic model, beats the aligned CLaMP 3 symbolic tower on composer probing; that is consistent with "audio alignment has not yet taught symbolic structure beyond scale" but is not a controlled test.

## Boundary Conditions and Failure Modes

1. **Redundancy.** If the target modality already contains the information, extra supervision adds optimisation cost without new signal.
2. **Shortcut learning.** A symbolic student can read the instrument program token or the note density instead of the intended acoustic property. Instrument-only and shuffled-pair controls are mandatory.
3. **Teacher validity.** An audio encoder may encode instrument and production identity more strongly than blend or clash. The teacher must be validated against perceptual judgements before distillation.
4. **Teacher noise.** MIDI-REPA's Basic Pitch result shows that a noisy symbolic teacher can be worse than no teacher. The same applies in reverse to AMT-derived audio targets.
5. **Optimisation imbalance.** One branch can dominate; utilisation must be measured, not assumed.
6. **Task–modality alignment.** Hallucination and distillation work when the privileged modality is spatially or temporally aligned with the target (depth↔RGB). Audio and symbolic tokens are only loosely aligned; a frame-wise feature-mimicry loss is therefore inappropriate, and a distributional or contrastive objective is the natural choice.

## Implications for the AGT Line

- The premise is literature-supported **only for properties that MIDI lacks**; it is not supported for structure. AGT's perceptual target (clash/blend) is the correct place to look.
- The methodological template is privileged training with single-modality inference (Hoffman; Garcia), not joint fusion (Look, Listen and Learn) and not inference-time conditioning (bootstrapping).
- The closest prior art is MIDI-REPA (reverse direction, audio generation) and SMART (audio reward on rendered symbolic output). Neither performs note-level attribution or validates the teacher against perceptual clash.
- The novelty claim should be narrow: **audio→symbolic distillation of a perceptual property, with a validated teacher and intervention-checked note attribution**, not "audio supervision helps symbolic models" in general.

## Acronyms

- **AMT:** Automatic Music Transcription.
- **ATTM:** Academic Text-To-Music Challenge.
- **CLAP:** Contrastive Language–Audio Pretraining.
- **DiT:** Diffusion Transformer.
- **FAD:** Fréchet Audio Distance.
- **MIDI:** Musical Instrument Digital Interface.
- **MIR:** Music Information Retrieval.
- **SSL:** Self-Supervised Learning.

## Related Pages

- [[overviews/audio-symbolic-transfer]] — the music-specific evidence map and the four audio→symbolic routes.
- [[data-and-representation/aytar-2016-soundnet-learning-sound-representations-from]] — vision-teacher → audio-student.
- [[data-and-representation/arandjelovic-2017-look-listen-and-learn]] — bidirectional audio–visual correspondence.
- [[data-and-representation/won-2024-a-foundation-model-for-music]] — audio-only foundation model and teacher candidate.
- [[other/lin-2023-multimodality-helps-unimodality-cross-modal]] — cross-modal examples improve unimodal classifiers.
- [[other/huang-2021-what-makes-multi-modal-learning-better]] — the population-risk argument.
- [[other/wu-2022-characterizing-and-overcoming-the-greedy]] — modality imbalance and the need for utilisation controls.
- [[other/hoffman-2016-learning-with-side-information-through]] — side information via hallucination.
- [[other/garcia-2018-modality-distillation-with-multiple-stream]] — privileged-modality distillation.
- [[generation-and-planning/yu-2026-midi-repa-improving-text-to-music]] — symbolic → audio alignment.
- [[generation-and-planning/jonason-2025-smart-tuning-a-symbolic-music]] — audio reward for symbolic generation.
- [[generation-and-planning/wang-2022-audio-to-symbolic-arrangement-via-cross-modal]] — audio → symbolic arrangement.
- [[generation-and-planning/zhao-2026-learning-music-style-for-piano]] — audio style → symbolic generation.
