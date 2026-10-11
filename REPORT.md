# Literature Digest: Explainable Symbolic Music AI

**Prepared:** 2026-10-11  
**Scope:** 55 user-supplied arXiv papers  
**Canonical repository:** `projects/phd-paper-repository/`

## Executive summary

The batch points to a consistent design principle for explainable symbolic music AI: keep composition, source material, constraints, and rendering separated enough that each decision can be inspected and tested. Explicit event representations, hierarchical plans, retrieval/edit/rerank pipelines, music-theoretic verifiers, attribution benchmarks, and human correction interfaces are more useful to the research programme than a single opaque end-to-end quality score. Learned audio/semantic latents remain valuable renderers and control interfaces, but they do not by themselves identify notes, sources, or repair causes.

The most directly relevant papers are Open-Qwen-Music; TrueMuse; the two attribution/plagiarism papers; MusicRLVR; RER chord generation; MIDIBACK; reference-free pitch correction; SpanSynth-Edit; NoteSep; incremental symbolic editing; MidiTok/subword/POP909/MAESTRO; tonal chord embeddings; group-invariant representation geometry; and the copying/context-window study. The video-to-music, dance, interaction, and adjacent non-music papers are retained as transfer evidence or negative evidence rather than treated as direct proof of symbolic-music explanations.

## Evidence and integrity notes

- Every supplied URL was downloaded from the official arXiv PDF endpoint and preserved under `projects/phd-paper-repository/papers/`; each paper has a source digest and a wiki page.
- The per-paper source records contain the delegate's full-paper digest, page/section anchors, reported results, limitations, artifact checks, and research implications. This report is a compact navigational digest; follow the linked source record before quoting a number.
- **PDF mismatch:** the supplied `2609.28008v2.pdf` has visible pages for `2606.04040v2` (EEG-to-music) but a hidden text layer containing MIDIBACK. The MIDIBACK source record is based on the extracted text and explicitly flags this. Replace the PDF before relying on its figures or visual page numbers.
- Some papers are future-dated arXiv preprints in the supplied batch. They are summarized as preprints and not silently upgraded to peer-reviewed evidence.

## Paper-by-paper digests

The entries below are ordered by methodological category. Each includes the core claim/evidence excerpt, relevance to the research programme, and a research idea. The linked source record is the detailed digest.

### data-and-representation

#### Enabling Factorized Piano Music Modeling and Generation with the MAESTRO Dataset (`1810.12247v5`)

- **Authors:** Curtis Hawthorne, Andriy Stasyuk, Adam Roberts, Ian Simon, Cheng-Zhi Anna Huang, Sander Dieleman, Erich Elsen, Jesse Engel, and Douglas Eck (2019)
- **Core digest:** **Curtis Hawthorne, Andriy Stasyuk, Adam Roberts, Ian Simon, Cheng-Zhi Anna Huang, Sander Dieleman, Erich Elsen, Jesse Engel, and Douglas Eck.** **“Enabling Factorized Piano Music Modeling and Generation with the MAESTRO Dataset.”** arXiv:**1810.12247v5** [cs.SD], submitted **17 January 2019**; published as an **ICLR 2019 conference paper**.
- **Relevance:** Relevant as a representation/data precedent: it affects what can be inspected, edited, aligned, or verified in a symbolic pipeline.
- **Research idea:** A promising modern architecture would retain the paper’s central idea but extend the representation: audio source A/B ↓ transcription and score/performance extraction ↓ provenance-preserving symbolic graph ├── source identity ├── voice/track role ├── phrase and motif identity ├── harmony and meter ├── protected notes └── detected conflicts ↓ alignment / transformation / repair / inpainting ↓ multi-track symbolic generator ↓ hierarchical expressive renderer The key distinction is: - **Wave2Midi2Wave:** MIDI is an explicit, editable performance bottleneck. - **Your target system:** the symbolic layer should additionally encode provenance, musical roles, conflicts, repair operations, and reasons. For explainable mashups, MIDI should therefore…
- **Detailed record:** [`sources/hawthorne-2019-enabling-factorized-piano-music-modeling.md`](sources/hawthorne-2019-enabling-factorized-piano-music-modeling.md); wiki page: [`wiki/data-and-representation/hawthorne-2019-enabling-factorized-piano-music-modeling.md`](wiki/data-and-representation/hawthorne-2019-enabling-factorized-piano-music-modeling.md)

#### Exploring Inherent Properties of the Monophonic Melody of Songs (`2003.09287v1`)

- **Authors:** Zehao Wang, Shicheng Zhang, and Xiaoou Chen (2020)
- **Core digest:** 1. computationally tractable, 2. semantically meaningful, 3. related to human perception/composition, 4. interpretable, and 5. useful for controlling generation or evaluation.
- **Relevance:** Relevant as a representation/data precedent: it affects what can be inspected, edited, aligned, or verified in a symbolic pipeline.
- **Research idea:** research directions 1. **Feature-conditioned hierarchical generation:** generate phrase-level MCG/GMD/RD targets first, then realize notes under those targets. 2. **Explainable repair:** use feature residuals to identify suspicious notes and constrained search to repair them. 3. **Mashup compatibility scoring:** compare normalized feature trajectories across candidate melodies before harmonic or rhythmic alignment. 4. **Counterfactual explanations:** show which note-duration changes caused an MCG or GMD change. 5. **Large-scale validation:** test genre, culture, tonality, atonality, meter, and listener expertise with mixed-effects statistical models. 6. **Polyphonic extension:** add voice-specific and ensemble-level MCG/GMD/RD while…
- **Detailed record:** [`sources/wang-2020-exploring-inherent-properties-of-the.md`](sources/wang-2020-exploring-inherent-properties-of-the.md); wiki page: [`wiki/data-and-representation/wang-2020-exploring-inherent-properties-of-the.md`](wiki/data-and-representation/wang-2020-exploring-inherent-properties-of-the.md)

#### POP909: A Pop-song Dataset for Music Arrangement Generation (`2008.07142v1`)

- **Authors:** Ziyu Wang, Ke Chen, Junyan Jiang, Yiyi Zhang, Maoran Xu, Shuqi Dai, Xianbin Gu, and Gus Xia (2020)
- **Core digest:** Author claims POP909 is intended to address three dataset requirements (PDF pp. 1–3, §§1, 2.3): 1. A style-consistent piano arrangement rather than arbitrary extracted tracks. 2. Precise alignment to a source representation: lead melody, audio, or full score. 3. External annotations such as beat, downbeat, key, and chord labels. The dataset contains: - **909 popular songs** - Approximately **60 hours** of arrangements - Songs by **462 artists** - Release dates spanning approximately the **1950s–2010** - Multiple piano-arrangement revisions per song - MIDI tracks aligned to corresponding audio using manually labelled tempo curves The authors frame two primary tasks (PDF p. 2, §1): - **Task 1:** piano accompaniment generation conditioned on melody and auxiliary annotations. - **Task 2:** audio-to-piano re-orchestration from a full orchestral recording. They also mention unconditional symbolic generation and expressive performance rendering. Interpretation POP909 is primarily a **source-conditioned piano accompaniment dataset**, not a…
- **Relevance:** Relevant as a representation/data precedent: it affects what can be inspected, edited, aligned, or verified in a symbolic pipeline.
- **Research idea:** 1. **Version-aware arrangement repair** Treat `v1 → v2 → ... → final` as an edit trajectory. Extract note-level and phrase-level edits, then train a model to predict reviewer-accepted corrections. Keep all versions of one song in one split. 2. **Constrained source-preserving generation** Condition on melody, bridge, beat, key, and chord labels while enforcing hard or soft constraints on melody identity, timing, and harmonic deviation. 3. **Dual-source chord modelling** Represent `chord_audio` and `chord_midi` separately. Learn when reharmonization is intentional instead of treating disagreement as annotation error. 4. **Mashup alignment benchmark** Pair songs by compatible key, tempo, beat structure, and chord regions. Use POP909…
- **Detailed record:** [`sources/wang-2020-pop909-a-pop-song-dataset.md`](sources/wang-2020-pop909-a-pop-song-dataset.md); wiki page: [`wiki/data-and-representation/wang-2020-pop909-a-pop-song-dataset.md`](wiki/data-and-representation/wang-2020-pop909-a-pop-song-dataset.md)

#### From Words to Music: A Study of Subword Tokenization Techniques in Symbolic Music Generation (`2304.08953v2`)

- **Authors:** Adarsh Kumar and Pedro Sarmento (2023)
- **Core digest:** **Adarsh Kumar and Pedro Sarmento.** “From Words to Music: A Study of Subword Tokenization Techniques in Symbolic Music Generation.” **arXiv:2304.08953v2 [cs.SD], 25 April 2023.** The PDF is 10 pages and identifies the authors as affiliated with IIT Kharagpur and Queen Mary University of London. No journal or conference publication is specified in the paper.
- **Relevance:** Relevant as a representation/data precedent: it affects what can be inspected, edited, aligned, or verified in a symbolic pipeline.
- **Research idea:** Test an inspectability-preserving representation: compare explicit event tokens, subwords, and learned semantic tokens under note-level interventions, round-trip reconstruction, and source-identity probes.
- **Detailed record:** [`sources/kumar-2023-from-words-to-music-a.md`](sources/kumar-2023-from-words-to-music-a.md); wiki page: [`wiki/data-and-representation/kumar-2023-from-words-to-music-a.md`](wiki/data-and-representation/kumar-2023-from-words-to-music-a.md)

#### MidiTok: A Python Package for MIDI File Tokenization (`2310.17202v1`)

- **Authors:** Nathan Fradet, Jean-Pierre Briot, Fabien Chhel, Amal El Fallah Seghrouchni, and Nicolas Gutowski (2023)
- **Core digest:** MidiTok is a strong **engineering and reproducibility contribution**: flexible, modular, and well suited as a common substrate for symbolic-music experiments. Its most important research value for explainable AI is the bridge between model tokens and interpretable musical events. Its main weakness is that the paper evaluates representation efficiency rather than downstream musical quality, explanation fidelity, mashup quality, or repair correctness.
- **Relevance:** Relevant as a representation/data precedent: it affects what can be inspected, edited, aligned, or verified in a symbolic pipeline.
- **Research idea:** Test an inspectability-preserving representation: compare explicit event tokens, subwords, and learned semantic tokens under note-level interventions, round-trip reconstruction, and source-identity probes.
- **Detailed record:** [`sources/fradet-2023-miditok-a-python-package-for.md`](sources/fradet-2023-miditok-a-python-package-for.md); wiki page: [`wiki/data-and-representation/fradet-2023-miditok-a-python-package-for.md`](wiki/data-and-representation/fradet-2023-miditok-a-python-package-for.md)

#### Unified Cross-modal Translation of Score Images, Symbolic Music, and Performance Audio (`2505.12863v1`)

- **Authors:** Jongmin Jung, Dongmin Kim, Sihun Lee, Seola Cho, Hyungjoon So, Irmak Bukey, Chris Donahue, and Dasaem Jeong (2025)
- **Core digest:** Authors’ claim The paper proposes a unified token-level encoder–decoder Transformer for four modalities: 1. score images, 2. symbolic notation / MusicXML, 3. performance MIDI, 4. performance audio. The claimed contributions are: - a single multitask framework for cross-modal music translation; - the first successful direct score-image-to-performance-audio system; - the YouTube Score Video (YTSV) dataset; - multitask improvements to OMR, AMT, MIDI-to-audio, image-to-audio, and audio-to-image tasks. Anchors: **Abstract, pp. 1–2; Fig. 2, p. 2; Sections III–VIII, pp. 3–10.** Important qualification Despite the “unified” framing, the experiments train **two separate checkpoints**: - Image-to-Audio direction (I2A) - Audio-to-Image direction (A2I) They do not share weights. The authors explicitly identify training one model for both directions as future work (**Conclusion, p. 10**).
- **Relevance:** Relevant as a representation/data precedent: it affects what can be inspected, edited, aligned, or verified in a symbolic pipeline.
- **Research idea:** future work (**Conclusion, p. 10**). 3. Modalities and token design Modality roles The paper treats the modalities as a spectrum: - **Score image:** scanned or rendered notation. - **Symbolic notation:** Linearized MusicXML (LMX), including pitch, duration, voicing, articulation, slurs, tempo, and dynamics. - **MIDI:** performance-oriented event representation with onset/offset timing, pitch, velocity, instruments, and timing markers. - **Audio:** recorded or synthesized performance. Anchors: **Section II, pp. 2–3; Fig. 3, p. 3.** Image tokens The authors train a modified **Residual Quantized VAE (RQVAE)**: - 16× spatial compression; - four unshared codebooks; - 1,024 codes per codebook; - model dimension 256; - grayscale score images; -…
- **Detailed record:** [`sources/jung-2025-unified-cross-modal-translation-of.md`](sources/jung-2025-unified-cross-modal-translation-of.md); wiki page: [`wiki/data-and-representation/jung-2025-unified-cross-modal-translation-of.md`](wiki/data-and-representation/jung-2025-unified-cross-modal-translation-of.md)

#### Dialogue-Aware Video-to-Music Generation Using Public Domain Film Collections (`2608.11576v1`)

- **Authors:** Haven Kim, Zachary Novack, Julian McAuley, and Hao-Wen Dong (2026)
- **Core digest:** Key cited systems: - VidMuse [9], Tian et al., 2025. - GVMGen [12], Zuo et al., arXiv:2501.09972, 2025. - Diff-V2M [16], Ji et al., AAAI 2026. - Prior OSSL [21], Kim et al., arXiv:2506.12573, 2025.
- **Relevance:** Relevant as a representation/data precedent: it affects what can be inspected, edited, aligned, or verified in a symbolic pipeline.
- **Research idea:** research directions 1. **Separate dialogue factors** - Add ASR text, speaker turns, prosody, speech rate, intensity, and speech emotion as separate streams. - Compare acoustic-only, transcript-only, semantic-only, and fused conditioning. 2. **Narrative-to-score planning** - Predict interpretable scene controls such as valence, arousal, tension, pacing, instrumentation, mode, tempo, density, and dynamics. - Generate a symbolic score or structured music plan before rendering audio. 3. **Explainable FiLM control** - Expose dialogue-strength and dialogue-emotion gates as user-adjustable controls. - Log temporal FiLM activations and cross-attention weights. - Perform interventions: mute dialogue, shift dialogue timing, swap dialogue between…
- **Detailed record:** [`sources/kim-2026-dialogue-aware-video-to-music.md`](sources/kim-2026-dialogue-aware-video-to-music.md); wiki page: [`wiki/data-and-representation/kim-2026-dialogue-aware-video-to-music.md`](wiki/data-and-representation/kim-2026-dialogue-aware-video-to-music.md)

#### One Timeline, Many Renderings: A Wolfram Language Paclet for Heterogeneous Musical Output (`2608.24683v1`)

- **Authors:** Francesco Vitucci, Michele Lorusso, and Francesco Scagliola (2026)
- **Core digest:** **Full title:** *One Timeline, Many Renderings: A Wolfram Language Paclet for heterogeneous musical output* **Authors:** Francesco Vitucci, Michele Lorusso, and Francesco Scagliola **Affiliation:** Conservatorio di Musica “N. Piccinni” di Bari **Version:** arXiv:2608.24683v1, 25 August 2026; 5-page PDF, classified `[cs.CL]`.
- **Relevance:** Relevant as a representation/data precedent: it affects what can be inspected, edited, aligned, or verified in a symbolic pipeline.
- **Research idea:** future work, not present capabilities. 5. MusicXML is beta and explicitly lossy. 6. MIDI output is absent, although planned. 7. Continuous tempo is unsupported. 8. Csound curves depend on declared p-fields and rewritten instrument copies. 9. Named Csound channels are not implemented. 10. There is no large-score benchmark. 11. The stress fixture is not representative of a composition. 12. Adding arbitrary backends is not measured by the click-track implementation; the “roughly 140 lines” result is only one reuse case. 13. The paper says the archived supplement covers much of the reproducibility gap, but the paclet itself remains unreleased. Additional interpretation The central synchronization claim is plausible for outputs that correctly…
- **Detailed record:** [`sources/vitucci-2026-one-timeline-many-renderings-a.md`](sources/vitucci-2026-one-timeline-many-renderings-a.md); wiki page: [`wiki/data-and-representation/vitucci-2026-one-timeline-many-renderings-a.md`](wiki/data-and-representation/vitucci-2026-one-timeline-many-renderings-a.md)

#### Rethinking Music Tokenization: A Semantic Codec toward High-Fidelity LLM Music Generation (`2609.21240v1`)

- **Authors:** Huakang Chen et al. (2026)
- **Core digest:** The paper introduces **MuSeC**, a music codec intended to improve the trade-off between: 1. waveform reconstruction fidelity; 2. semantic/content preservation; and 3. autoregressive language-model predictability. The authors argue that ordinary reconstruction codecs encode fine acoustic detail into high-entropy tokens, while speech-derived semantic codecs impose an inadequate notion of semantics on music. MuSeC instead factorizes a mixed music signal into: - a **semantic stream**, derived from intermediate layers of a music SSL model; and - an **acoustic stream**, learned with residual vector quantization to recover information missing from the semantic stream. **Author claim:** The factorization improves reconstruction and token predictability without source separation (pp. 1–2, Sec. I–II). **Interpretation:** MuSeC is a learned audio-latent decomposition, not an interpretable symbolic representation. Its “semantic” tokens are still frame-level cluster IDs rather than notes, chords, voices, phrases, or source-labelled musical events.
- **Relevance:** Relevant as a representation/data precedent: it affects what can be inspected, edited, aligned, or verified in a symbolic pipeline.
- **Research idea:** Test an inspectability-preserving representation: compare explicit event tokens, subwords, and learned semantic tokens under note-level interventions, round-trip reconstruction, and source-identity probes.
- **Detailed record:** [`sources/al-2026-rethinking-music-tokenization-a-semantic.md`](sources/al-2026-rethinking-music-tokenization-a-semantic.md); wiki page: [`wiki/data-and-representation/al-2026-rethinking-music-tokenization-a-semantic.md`](wiki/data-and-representation/al-2026-rethinking-music-tokenization-a-semantic.md)

### explainability-and-auditability

#### Group-Invariant Statistics Determine Embedding Geometry: Harmonic Analysis of Representations from Bach to the Night Sky (`2610.00647v1`)

- **Authors:** Liam Storan, Andreas Tolias, and Nina Miolane (2026)
- **Core digest:** **Paper:** Liam Storan, Andreas Tolias, and Nina Miolane, *Group-Invariant Statistics Determine Embedding Geometry: Harmonic Analysis of Representations from Bach to the Night Sky*, arXiv:2610.00647v1 [cs.LG], 30 September 2026. The PDF is marked **“Preprint. Under review.”**
- **Relevance:** Highly relevant to the core goal: provenance, attribution, mechanistic evidence, representation geometry, copying, or audit traces.
- **Research idea:** Build a faithfulness benchmark in which an explanation must predict the output change under a targeted intervention, not merely correlate with a generated sample.
- **Detailed record:** [`sources/storan-2026-group-invariant-statistics-determine-embedding.md`](sources/storan-2026-group-invariant-statistics-determine-embedding.md); wiki page: [`wiki/explainability-and-auditability/storan-2026-group-invariant-statistics-determine-embedding.md`](wiki/explainability-and-auditability/storan-2026-group-invariant-statistics-determine-embedding.md)

#### How Far Back Should a Transformer Look? Repetition and Copying in Music Sequence Models (`2610.02837v1`)

- **Authors:** Amir Fathi (2026)
- **Core digest:** **Amir Fathi**, “**How Far Back Should a Transformer Look? Repetition and Copying in Music Sequence Models**,” arXiv:**2610.02837v1** [cs.SD], **2 October 2026**, 17 pages. University of Alberta.
- **Relevance:** Highly relevant to the core goal: provenance, attribution, mechanistic evidence, representation geometry, copying, or audit traces.
- **Research idea:** Build a faithfulness benchmark in which an explanation must predict the output change under a targeted intervention, not merely correlate with a generated sample.
- **Detailed record:** [`sources/fathi-2026-how-far-back-should-a.md`](sources/fathi-2026-how-far-back-should-a.md); wiki page: [`wiki/explainability-and-auditability/fathi-2026-how-far-back-should-a.md`](wiki/explainability-and-auditability/fathi-2026-how-far-back-should-a.md)

#### Open-Qwen-Music: An Auditable Framework for LLM-Based Music Composition and Diffusion Rendering (`2609.31652v1`)

- **Authors:** Yangbin Yu and Mingyu Yang (2026)
- **Core digest:** The paper asks two explicit questions (§1, p. 2): 1. **How can a modular semantic-composition/acoustic-rendering system be trained under explicit, independently reproducible interfaces?** 2. **How can component-level diagnostics and artifact provenance make a modular text-to-music system reproducible and inspectable?** The authors present Open-Qwen-Music as an **open reconstruction of Qwen-Music**, not as a quality-equivalent replacement. Their principal claim is that it makes the entire LLM-composition-plus-diffusion-rendering workflow inspectable: > “We present the system as a transparent, executable research baseline … not as evidence of quality parity with Qwen-Music.” (Abstract, p. 1) The paper’s “first fully open” claim is explicitly qualified as “to our knowledge” (§5, p. 10); it is not established by a systematic comparison of all prior open systems.
- **Relevance:** Highly relevant to the core goal: provenance, attribution, mechanistic evidence, representation geometry, copying, or audit traces.
- **Research idea:** Build a faithfulness benchmark in which an explanation must predict the output change under a targeted intervention, not merely correlate with a generated sample.
- **Detailed record:** [`sources/yu-2026-open-qwen-music-an-auditable.md`](sources/yu-2026-open-qwen-music-an-auditable.md); wiki page: [`wiki/explainability-and-auditability/yu-2026-open-qwen-music-an-auditable.md`](wiki/explainability-and-auditability/yu-2026-open-qwen-music-an-auditable.md)

#### Towards AI-Generated Music Plagiarism Detection as a Version Identification Problem (`2610.09075v1`)

- **Authors:** Fotis Koutsikos et al. (2026)
- **Core digest:** **Author claim:** pretrained scalar MVI distances are inadequate for AI-generated derivatives, but coordinate-wise embedding shifts substantially improve detection, reaching **80.3% overall F0.5** and **66.2% on AI + DSP**. **My assessment:** the paper provides a useful retrieval/triage architecture and a strong argument against relying on one similarity score. For explainable symbolic music research, its most valuable contribution is the controlled transformation framework—not yet a symbolic explanation method. The next step is to connect latent-space evidence to aligned musical structures and provenance graphs, while eliminating vocal/category shortcuts and testing source- and generator-disjoint generalization.
- **Relevance:** Highly relevant to the core goal: provenance, attribution, mechanistic evidence, representation geometry, copying, or audit traces.
- **Research idea:** Future work listed by the authors includes: - more generative architectures; - broader DSP perturbations; - lyric-preserving datasets; - newer MVI systems; - fine-tuning the MVI encoders; - source attribution beyond binary detection. The authors also note that commercial systems such as Suno and Udio do not provide the audio-conditioning interfaces needed for this experimental construction. Dataset and experimental limitations Synthetic AI derivatives The benchmark’s AI cases are controlled re-syntheses from MusicGen, AudioLDM 2, and MGE-LDM. They are not necessarily representative of: - Suno; - Udio; - proprietary systems; - prompt-only generation; - iterative human editing; - real-world infringement workflows. Artificial prompt design…
- **Detailed record:** [`sources/al-2026-towards-ai-generated-music-plagiarism.md`](sources/al-2026-towards-ai-generated-music-plagiarism.md); wiki page: [`wiki/explainability-and-auditability/al-2026-towards-ai-generated-music-plagiarism.md`](wiki/explainability-and-auditability/al-2026-towards-ai-generated-music-plagiarism.md)

#### Tracing Inputs, Verifying Outputs: Validating Attribution in Music Generation (`2610.09637v1`)

- **Authors:** Taejun Kim et al. (2026)
- **Core digest:** The paper provides a persuasive demonstration that **input records can be strengthened by controlled evidence that different audio inputs control different output properties**. MixAudio follows prompt timbre and context harmony/tempo substantially better than ACE under these tests. For symbolic mashups, however, it does **not** verify note-level source presence, transformed melodic reuse, chord-event provenance, or complete absence of unrecorded source material. Its most valuable contribution is therefore methodological: combine immutable input records with counterfactual input swaps and independent output audits, then extend those tests from audio stems to symbolic events and transformations.
- **Relevance:** Highly relevant to the core goal: provenance, attribution, mechanistic evidence, representation geometry, copying, or audit traces.
- **Research idea:** research directions for provenance-preserving recomposition 1. **Event-level provenance ledger** Represent each output note/event with: ```text source_id source_track source_section/bar source_event_span operation: copy | transpose | retime | ornament | interpolate | newly generated transformation parameters model/version/seed ``` This would extend MixAudio’s stem-level record to bar-, phrase-, or event-level provenance. 2. **Symbolic counterfactual swaps** Run factorial experiments that separately replace: - melody donor, - harmony donor, - rhythm donor, - instrumentation/timbre donor, - form/section context. Measure note-level changes in pitch, intervals, onset positions, chord labels, voice leading, contour, and groove while holding…
- **Detailed record:** [`sources/al-2026-tracing-inputs-verifying-outputs-validating.md`](sources/al-2026-tracing-inputs-verifying-outputs-validating.md); wiki page: [`wiki/explainability-and-auditability/al-2026-tracing-inputs-verifying-outputs-validating.md`](wiki/explainability-and-auditability/al-2026-tracing-inputs-verifying-outputs-validating.md)

#### TrueMuse: A Benchmark for Data Attribution in Text-to-Music Models (`2610.00835v1`)

- **Authors:** Jiawei Yu and Jian Liu (2026)
- **Core digest:** This is primarily a **controlled benchmark**, not a new end-to-end source-attribution model. It constructs attribute-specific text-to-music models by fine-tuning existing diffusion generators on known source clips. It then evaluates black-box retrieval methods that attempt to recover those source clips from generated audio. The learned “mapper” is a linear projection on top of frozen audio embeddings; it is an enhanced baseline, not the central generative model.
- **Relevance:** Highly relevant to the core goal: provenance, attribution, mechanistic evidence, representation geometry, copying, or audit traces.
- **Research idea:** research directions 1. **Symbolic TrueMuse.** Fine-tune a symbolic generator on known MIDI phrase sets with source identifiers. Evaluate event-level Recall@k, segment IoU, motif retrieval under transposition, and voice/harmony attribution. 2. **Causal provenance benchmark.** For every generated piece, compare: - source inclusion; - source deletion or masking; - retraining or adapter ablation; - output-level attribution. This would distinguish provenance from actual causal influence. 3. **Mashup provenance graphs.** Represent each output note or phrase as linked to source A, source B, both, or newly generated material, including transformations such as transposition, rhythmic quantization, reharmonization, and orchestration. 4. **Repair…
- **Detailed record:** [`sources/yu-2026-truemuse-a-benchmark-for-data.md`](sources/yu-2026-truemuse-a-benchmark-for-data.md); wiki page: [`wiki/explainability-and-auditability/yu-2026-truemuse-a-benchmark-for-data.md`](wiki/explainability-and-auditability/yu-2026-truemuse-a-benchmark-for-data.md)

### generation-and-planning

#### MuseGAN: Multi-track Sequential Generative Adversarial Networks for Symbolic Music Generation and Accompaniment (`1709.06298v2`)

- **Authors:** Hao-Wen Dong, Wen-Yi Hsiao, Li-Chia Yang, and Yi-Hsuan Yang (2017)
- **Core digest:** **Author claim — Abstract, Introduction, PDF pp. 1–2:** MuseGAN is a WGAN-GP-based framework for generating short, multi-track, polyphonic symbolic music. It models: - five tracks: bass, drums, guitar, piano, strings; - local musical structure at the bar level; - temporal structure across four-bar phrases; - inter-track dependencies; - track-conditional generation for accompaniment. The authors present three alternative models for inter-track dependency: 1. **Jamming model** 2. **Composer model** 3. **Hybrid model** They report that the systems can generate coherent four-bar phrases from scratch and can generate four additional tracks conditioned on one human-provided track. **Interpretation:** The major conceptual contribution is not long-form composition, but factorizing multi-track generation into: time-independent track/style variables + time-dependent shared/private variables + bar-level convolutional generators This factorization remains relevant to structured symbolic generation, although the representation and evaluation are…
- **Relevance:** Relevant as a generation/control precedent, with attention to whether its controls are exact and auditable rather than only correlated with the output.
- **Research idea:** Add an auditable intermediate plan or control stream and measure whether changing one control changes only its intended musical property while preserving protected source events.
- **Detailed record:** [`sources/dong-2017-musegan-multi-track-sequential-generative.md`](sources/dong-2017-musegan-multi-track-sequential-generative.md); wiki page: [`wiki/generation-and-planning/dong-2017-musegan-multi-track-sequential-generative.md`](wiki/generation-and-planning/dong-2017-musegan-multi-track-sequential-generative.md)

#### Pop Music Transformer: Beat-based Modeling and Generation of Expressive Pop Piano Compositions (`2002.00212v3`)

- **Authors:** Yu-Siang Huang and Yi-Hsuan Yang (2020)
- **Core digest:** The authors argue that Transformer music generation benefits substantially from a better **symbolic event representation**, not only from architectural innovation. Their representation, **REMI** (“revamped MIDI-derived events”), makes the following explicit: 1. bar boundaries; 2. quantized positions within each bar; 3. note duration; 4. local tempo; 5. chord labels. The claimed result is better rhythmic regularity and subjective preference over a Transformer-XL adaptation of Music Transformer. This is an author claim; the empirical evidence is specifically for **expressive solo Pop piano**, not general music generation.
- **Relevance:** Relevant as a generation/control precedent, with attention to whether its controls are exact and auditable rather than only correlated with the output.
- **Research idea:** Future work is needed for longer-term structure and longer-context architectures. - The authors propose adding groove, emotion, guitar, bass, drums, lyrics, and video conditioning. Evidence: PDF pp. 5 and 8; §6; `.txt:331-344, 542-558`. Additional methodological limitations These are interpretations based on the design: - Automatic transcription and beat/downbeat/chord recognition introduce label noise. - Chord labels are restricted to 60 heuristic categories. - The subjective evaluation does not test repair, infilling, multi-track arrangement, or long-form composition. - The objective metrics are tracker-derived proxies rather than direct measures of musical coherence. - The paper does not report a modern held-out likelihood comparison,…
- **Detailed record:** [`sources/huang-2020-pop-music-transformer-beat-based.md`](sources/huang-2020-pop-music-transformer-beat-based.md); wiki page: [`wiki/generation-and-planning/huang-2020-pop-music-transformer-beat-based.md`](wiki/generation-and-planning/huang-2020-pop-music-transformer-beat-based.md)

#### Music ControlNet: Multiple Time-varying Controls for Music Generation (`2311.07069v1`)

- **Authors:** Shih-Lun Wu, Chris Donahue, Shinji Watanabe, Nicholas J. Bryan, and Dasaem Jeong (2023)
- **Core digest:** **Author claim:** Music ControlNet adds composable, time-varying controls to text-conditioned music generation: melody, dynamics, and rhythm. Each control may be omitted, fully specified, or specified only over selected time spans, with the model improvising elsewhere ([p.1, Abstract; §I; Fig.1]). The model generates Mel spectrograms with diffusion and renders them through a DiffWave vocoder. It uses global genre/mood conditioning plus any subset of the time-varying controls. **Interpretation:** This is a useful control interface, but it is not a source-preserving or provenance-aware mashup system. It preserves selected musical attributes statistically; it does not preserve exact notes, tracks, timbres, or source identity.
- **Relevance:** Relevant as a generation/control precedent, with attention to whether its controls are exact and auditable rather than only correlated with the output.
- **Research idea:** Add an auditable intermediate plan or control stream and measure whether changing one control changes only its intended musical property while preserving protected source events.
- **Detailed record:** [`sources/wu-2023-music-controlnet-multiple-time-varying.md`](sources/wu-2023-music-controlnet-multiple-time-varying.md); wiki page: [`wiki/generation-and-planning/wu-2023-music-controlnet-multiple-time-varying.md`](wiki/generation-and-planning/wu-2023-music-controlnet-multiple-time-varying.md)

#### VMAS: Video-to-Music Generation via Semantic Alignment in Web Music Videos (`2409.07450v1`)

- **Authors:** Yan-Bo Lin, Yu Tian, Linjie Yang, Gedas Bertasius, and Heng Wang (2024)
- **Core digest:** **Author claim:** VMAS generates instrumental background music directly from video, avoiding the small, narrow MIDI datasets used by earlier video-to-music systems. The system combines: 1. A temporally efficient video encoder. 2. An autoregressive EnCodec-token music decoder. 3. A global video–music contrastive objective. 4. A local video-beat alignment objective based on optical flow and onset detection. The stated goal is simultaneous alignment with: - **High-level semantics:** genre, style, and overall content. - **Low-level dynamics:** scene changes, human motion, and other visually salient moments. **Interpretation:** VMAS is not merely video-conditioned music generation. It explicitly introduces intermediate alignment signals that could be exposed as controls or explanations.
- **Relevance:** Relevant as a generation/control precedent, with attention to whether its controls are exact and auditable rather than only correlated with the output.
- **Research idea:** future work includes video–music style transfer, editing, and retrieval. 8. Limitations and reproducibility Explicit or directly evidenced limitations 1. **Web-data quality:** source videos contain static frames, weak correspondence, genre imbalance, and possible metadata noise. 2. **Vocal-removal imperfection:** Demucs succeeds for approximately 95%, not all, soundtracks. 3. **Baseline incomparability:** V2Meow code/checkpoints were unavailable; some comparisons rely on reported numbers. 4. **Human evaluation limitations:** approximately 200 MTurk raters, pairwise preferences, no published raw responses or uncertainty estimates. 5. **Metric limitations:** FAD, KL, and MV Align do not measure musical form, harmonic correctness, symbolic…
- **Detailed record:** [`sources/lin-2024-vmas-video-to-music-generation.md`](sources/lin-2024-vmas-video-to-music-generation.md); wiki page: [`wiki/generation-and-planning/lin-2024-vmas-video-to-music-generation.md`](wiki/generation-and-planning/lin-2024-vmas-video-to-music-generation.md)

#### CMA-OT: Hierarchical Expert Supervision for Dance-to-Music Generation (`2609.13118v1`)

- **Authors:** Jinting Wang, Chenxing Li, Dong Yu, and Li Liu (2026)
- **Core digest:** The paper’s central claim is that sparse dance cues cannot adequately supervise dense musical structure. CMA-OT therefore uses a pretrained hierarchical audio expert as an auxiliary training teacher for the dance-to-music generator.
- **Relevance:** Relevant as a generation/control precedent, with attention to whether its controls are exact and auditable rather than only correlated with the output.
- **Research idea:** Add an auditable intermediate plan or control stream and measure whether changing one control changes only its intended musical property while preserving protected source events.
- **Detailed record:** [`sources/wang-2026-cma-ot-hierarchical-expert-supervision.md`](sources/wang-2026-cma-ot-hierarchical-expert-supervision.md); wiki page: [`wiki/generation-and-planning/wang-2026-cma-ot-hierarchical-expert-supervision.md`](wiki/generation-and-planning/wang-2026-cma-ot-hierarchical-expert-supervision.md)

#### DiffSynth-Music: Audio-Conditioned KV-Cache Adapters for Controllable Music Generation (`2609.12774v1`)

- **Authors:** Zhongjie Duan, Shengchuan Gao, Hong Zhang, and Yingda Chen (2026)
- **Core digest:** The bibliography contains 36 references. The most central are ACE-Step-1.5 [4], Music-ControlNet [10], JASCO [11], Diffusion Templates [30], Demucs [26], pYIN [27], MuQ-MuLan [35], and AudioBox-Aesthetics [36].
- **Relevance:** Relevant as a generation/control precedent, with attention to whether its controls are exact and auditable rather than only correlated with the output.
- **Research idea:** research directions 1. **Symbolic KV adapters.** Encode MIDI/event streams into layer-wise keys and values, with explicit channels for source ID, voice, motif, harmony, meter, and transformation type. Compare this against token concatenation and direct symbolic constraints. 2. **Provenance-aware attention.** Maintain source-specific caches \(C^A\) and \(C^B\), log attention mass by source, and test whether attention attribution predicts human judgments of source identity. 3. **Protected-material constraints.** Use a symbolic decoder or constrained search to guarantee preservation of selected notes, motifs, cadences, or bass lines while allowing specified transformations. 4. **Conflict-aware cache arbitration.** Detect incompatible rhythm,…
- **Detailed record:** [`sources/duan-2026-diffsynth-music-audio-conditioned-kv.md`](sources/duan-2026-diffsynth-music-audio-conditioned-kv.md); wiki page: [`wiki/generation-and-planning/duan-2026-diffsynth-music-audio-conditioned-kv.md`](wiki/generation-and-planning/duan-2026-diffsynth-music-audio-conditioned-kv.md)

#### Drive-to-Music: Context-Aware Generative Audio for In-Vehicle Experiences (`2608.12615v1`)

- **Authors:** Dragoiu and Nabizadeh (2026)
- **Core digest:** **Dragoiu and Nabizadeh, “Drive-to-Music: Context-Aware Generative Audio for In-Vehicle Experiences,” arXiv:2608.12615v1, 12 Aug 2026.** Authors are from Mercedes-Benz Research & Development North America.
- **Relevance:** Relevant as a generation/control precedent, with attention to whether its controls are exact and auditable rather than only correlated with the output.
- **Research idea:** Add an auditable intermediate plan or control stream and measure whether changing one control changes only its intended musical property while preserving protected source events.
- **Detailed record:** [`sources/dragoiu-2026-drive-to-music-context-aware.md`](sources/dragoiu-2026-drive-to-music-context-aware.md); wiki page: [`wiki/generation-and-planning/dragoiu-2026-drive-to-music-context-aware.md`](wiki/generation-and-planning/dragoiu-2026-drive-to-music-context-aware.md)

#### Getting Motif-ated: Controllable AI Compositions from Injected Motif Prompts (`2609.32788v1`)

- **Authors:** Chao Peter Yang, Cynthia Rudin, Yue Jiang, Simon Mak, and Stephen Ni-Hahn (2026)
- **Core digest:** **Author claim — Abstract, pp. 1–2; Conclusion, p. 6:** MotiGen retrofits motif control onto a pretrained symbolic music language model by combining: 1. A structured `%motif:` ABC prompt line. 2. A scalar attention bias toward motif-prompt tokens. 3. Two-phase curriculum training: - motif-centered crops; - full annotated scores. 4. A shared motif extractor/evaluator. The reported full system contains the prompted motif in **92.3%** of generated pieces. **Interpretation:** This is primarily a controllability and motif-grounding paper, not a source-preserving recomposition or provenance paper. The motif is abstract and transformed, rather than an exact source excerpt.
- **Relevance:** Relevant as a generation/control precedent, with attention to whether its controls are exact and auditable rather than only correlated with the output.
- **Research idea:** research directions 1. **Dual-source provenance prompts** Condition on separate motifs from sources A and B, with source IDs and protected roles such as melody, bass, or accompaniment. 2. **Richer motif representations** Add rhythm, meter position, phrase boundaries, pitch intervals, voice, harmony, and allowable transformation classes. Keep the coarse contour as one abstraction level rather than the entire identity representation. 3. **Provenance-aware training crops** Crop source passages around known motifs while preserving note-level source IDs. Train the model to emit attribution metadata for every realized occurrence. 4. **Conflict-aware recomposition** Detect clashes between source motifs—meter, harmony, register, dissonance,…
- **Detailed record:** [`sources/yang-2026-getting-motif-ated-controllable-ai.md`](sources/yang-2026-getting-motif-ated-controllable-ai.md); wiki page: [`wiki/generation-and-planning/yang-2026-getting-motif-ated-controllable-ai.md`](wiki/generation-and-planning/yang-2026-getting-motif-ated-controllable-ai.md)

#### LatticeSMC: Where to Spend Inference-Time Compute in Chunked Sequence Generators (`2610.02774v1`)

- **Authors:** Xuanchen Wang, Heng Wang, and Weidong Cai (2026)
- **Core digest:** Problem formulation — §3.1, p.4 A sequence is divided into \(K\) chunks: \[ x=(x^{(1)},\ldots,x^{(K)}), \qquad p(x\mid c)=\prod_{k=1}^K p(x^{(k)}\mid x^{(<k)},c). \] Each chunk is generated using \(S\) denoising steps. Given reward \(r(x)\) and temperature \(\tau>0\), the intended target is \[ \pi_\tau(x\mid c)\propto p(x\mid c)\exp(r(x)/\tau). \] The fixed budget is \(B=NKS\), counting one denoiser evaluation per particle and denoising step, multiplied by classifier-free-guidance cost where applicable. The paper distinguishes: - **Sampling:** return a particle according to its normalized importance weight. - **Search:** return the highest-reward particle. This distinction is important: many comparisons become unfair if a sampler returning a weighted draw is compared with a greedy method that always returns its best particle. Lattice Feynman–Kac model — §3.2, p.4; Figure 1, p.2 The generation process is represented on a two-dimensional lattice: \[ \mathcal L=\{(k,t):1\leq k\leq K,\;1\leq t\leq S\}, \] where \(k\) is the chunk index…
- **Relevance:** Relevant as a generation/control precedent, with attention to whether its controls are exact and auditable rather than only correlated with the output.
- **Research idea:** Add an auditable intermediate plan or control stream and measure whether changing one control changes only its intended musical property while preserving protected source events.
- **Detailed record:** [`sources/wang-2026-latticesmc-where-to-spend-inference.md`](sources/wang-2026-latticesmc-where-to-spend-inference.md); wiki page: [`wiki/generation-and-planning/wang-2026-latticesmc-where-to-spend-inference.md`](wiki/generation-and-planning/wang-2026-latticesmc-where-to-spend-inference.md)

#### Learning Jazz Pianist Style with Cross-Attention Conditioning (`2610.02918v1`)

- **Authors:** Drew Edwards, Akira Maezawa, and Simon Dixon (2026)
- **Core digest:** **Inspection scope:** 8/8 PDF pages and extracted text inspected, including Tables 1–3, Figures 1–6, Equations 1–3, references, AI-use statement, ethics statement, and acknowledgments.
- **Relevance:** Relevant as a generation/control precedent, with attention to whether its controls are exact and auditable rather than only correlated with the output.
- **Research idea:** Add an auditable intermediate plan or control stream and measure whether changing one control changes only its intended musical property while preserving protected source events.
- **Detailed record:** [`sources/edwards-2026-learning-jazz-pianist-style-with.md`](sources/edwards-2026-learning-jazz-pianist-style-with.md); wiki page: [`wiki/generation-and-planning/edwards-2026-learning-jazz-pianist-style-with.md`](wiki/generation-and-planning/edwards-2026-learning-jazz-pianist-style-with.md)

#### MuseTimbre: Zero-Shot Timbre Transfer by Controlling a Frozen Music Generator (`2609.30548v1`)

- **Authors:** Yuan-Chiao Cheng and Zhiyao Duan (2026)
- **Core digest:** The paper contains 30 references. The central dependencies are Stable Audio 3 [12], LAION-CLAP [15], Basic Pitch [14], Control-Transfer Diffusion [4], TokenSynth [5], and the MuScriptor transcription model [16].
- **Relevance:** Relevant as a generation/control precedent, with attention to whether its controls are exact and auditable rather than only correlated with the output.
- **Research idea:** research directions 1. **Multi-stem symbolic control:** Use separate roll streams and separate timbre embeddings for each mashup stem, with explicit routing and stem-level cross-attention. 2. **Repair-aware training:** Mask note/onset regions during training and optimize reconstruction, edit locality, and confidence-calibrated correction rather than only generation quality. 3. **Hierarchical identity embeddings:** Factor reference representations into instrument, performer, articulation, room, microphone, and production-style components. 4. **Temporal timbre conditioning:** Replace the single global CLAP vector with chunk-level or note-aligned embeddings for changing articulations and recording environments. 5. **Pitch-leakage tests:**…
- **Detailed record:** [`sources/cheng-2026-musetimbre-zero-shot-timbre-transfer.md`](sources/cheng-2026-musetimbre-zero-shot-timbre-transfer.md); wiki page: [`wiki/generation-and-planning/cheng-2026-musetimbre-zero-shot-timbre-transfer.md`](wiki/generation-and-planning/cheng-2026-musetimbre-zero-shot-timbre-transfer.md)

#### StepAudio 3 Music Technical Report (`2609.16034v1`)

- **Authors:** Chengli Feng et al. (2026)
- **Core digest:** **Author claim:** StepAudio 3 Music is a long-form, text- and reference-conditioned music generator combining: 1. A discrete music tokenizer, 2. A Mixture-of-Experts autoregressive model, 3. An explicit ABC notation planning pass, 4. A continuous flow-matching DiT renderer. **Assessment:** The most research-relevant contribution is not the audio quality alone, but the **ABC-CoT intermediate arrangement plan and LLM-based plan editing**. This is a promising precedent for explainable musical control. However, the system remains primarily an audio-generation system: it does not demonstrate exact note-, chord-, bar-, source-provenance-, or repair-level guarantees. It is therefore highly relevant as an architectural inspiration for symbolic mashup/repair, but not a directly usable symbolic repair system.
- **Relevance:** Relevant as a generation/control precedent, with attention to whether its controls are exact and auditable rather than only correlated with the output.
- **Research idea:** research direction A PhD-scale adaptation would retain the plan-first idea but make the plan explicitly symbolic and verifiable: - Represent each musical event with source provenance. - Add constraint and conflict annotations. - Let an LLM propose edits to ABC/MIDI rather than directly edit audio. - Render the repaired plan. - Re-extract symbolic structure from the result. - Verify exact constraints automatically. - Report both musical-quality metrics and repair correctness. **Overall assessment:** StepAudio 3 Music is a strong frontier-scale demonstration that explicit musical planning can improve controllability and perceived quality. For explainable symbolic mashup/repair, its most transferable component is the intermediate-plan…
- **Detailed record:** [`sources/al-2026-stepaudio-3-music-technical-report.md`](sources/al-2026-stepaudio-3-music-technical-report.md); wiki page: [`wiki/generation-and-planning/al-2026-stepaudio-3-music-technical-report.md`](wiki/generation-and-planning/al-2026-stepaudio-3-music-technical-report.md)

#### VIBE: Video Instruction-aligned Background music gEneration (`2608.30125v1`)

- **Authors:** Aryan Vijay Bhosale, Vaibhavi Lokegaonkar, Vishnu Raj, Gouthaman KV, Sreyan Ghosh, Ramani Duraiswami, Lie Lu, and Dinesh Manocha (2026)
- **Core digest:** VIBE provides a useful blueprint for **instruction-following through verifiability-aware reward composition and staged optimization**. Its Conditioning Connection is potentially valuable for planner-to-refiner symbolic architectures. However, its evidence is primarily for short waveform generation: the reward estimators are imperfect, the study is small, the public artifact appears to be demonstration-only, and the model does not address symbolic editability, provenance, or identity preservation.
- **Relevance:** Relevant as a generation/control precedent, with attention to whether its controls are exact and auditable rather than only correlated with the output.
- **Research idea:** Add an auditable intermediate plan or control stream and measure whether changing one control changes only its intended musical property while preserving protected source events.
- **Detailed record:** [`sources/bhosale-2026-vibe-video-instruction-aligned-background.md`](sources/bhosale-2026-vibe-video-instruction-aligned-background.md); wiki page: [`wiki/generation-and-planning/bhosale-2026-vibe-video-instruction-aligned-background.md`](wiki/generation-and-planning/bhosale-2026-vibe-video-instruction-aligned-background.md)

#### Video-to-Music Generation for Gameplay Videos (`2609.31810v2`)

- **Authors:** Felipe Marra and Lucas N. Ferreira (2026)
- **Core digest:** 1. frames are rendered graphics; 2. music is synthetic; 3. game music often loops across levels rather than reacting to visible events (p. 1, §§1–2).
- **Relevance:** Relevant as a generation/control precedent, with attention to whether its controls are exact and auditable rather than only correlated with the output.
- **Research idea:** Add an auditable intermediate plan or control stream and measure whether changing one control changes only its intended musical property while preserving protected source events.
- **Detailed record:** [`sources/marra-2026-video-to-music-generation-for.md`](sources/marra-2026-video-to-music-generation-for.md); wiki page: [`wiki/generation-and-planning/marra-2026-video-to-music-generation-for.md`](wiki/generation-and-planning/marra-2026-video-to-music-generation-for.md)

#### Where the Body Keeps the Beat: Structured Motion Conditioning and Music Dynamics Supervision for Dance-to-Music Generation (`2610.00726v1`)

- **Authors:** Changchang Sun, Lu Cheng, and Yan Yan (2026)
- **Core digest:** Author claims The paper proposes Dyna2Music, combining: 1. **Spatio-Spectral Motion Decomposition (SSMD)** Separates dance motion by: - five body parts; - slow and fast temporal-frequency bands. 2. **Hierarchical Slow-Fast Conditioning Encoder (HSF-Encoder)** Uses part-wise motion energy and frozen MotionBERT features to create 256-dimensional conditioning tokens. 3. **Latent Dynamics Consistency (LDC)** Adds an auxiliary loss matching local adjacent-frame change magnitudes between: - a single-step estimate of the clean generated music latent; - the paired reference music latent. 4. **Latent flow-matching music generator** A DiffRhythm-derived transformer generates continuous music latents, decoded by a frozen waveform VAE. The authors report improved onset synchrony and FAD over 15 baselines on AIST++ and TikTok (abstract, pp. 1–3; Sections 3–4, pp. 4–9). Interpretation The technically important idea is not merely “more motion features.” It is the explicit separation of: - **where** motion occurs; - **at what temporal scale** it…
- **Relevance:** Relevant as a generation/control precedent, with attention to whether its controls are exact and auditable rather than only correlated with the output.
- **Research idea:** future work (p. 9). Missing or unavailable artifact information The paper says that supplementary material contains selected generation results from AIST++ and TikTok (p. 7). It does not provide, in the supplied PDF: - a code repository URL; - model checkpoints; - dataset preprocessing scripts; - a formal reproducibility statement; - a license; - a complete artifact description. The paper’s opening appendix paragraph says that later appendices cover limitations and broader impact, but the supplied 19-page PDF ends after Appendix E/Table A2 and contains no separate limitations or broader-impact sections. This should be recorded as an incomplete or missing-paper component, not inferred as evidence that no limitations exist. 11. Relevance to…
- **Detailed record:** [`sources/sun-2026-where-the-body-keeps-the.md`](sources/sun-2026-where-the-body-keeps-the.md); wiki page: [`wiki/generation-and-planning/sun-2026-where-the-body-keeps-the.md`](wiki/generation-and-planning/sun-2026-where-the-body-keeps-the.md)

#### YuE2: Unifying Symbolic and Audio Music Generation at Frontier Quality (`2609.33757v1`)

- **Authors:** Ruibin Yuan et al. (2026)
- **Core digest:** **Ruibin Yuan et al.**, “**YuE2: Unifying Symbolic and Audio Music Generation at Frontier Quality**,” *YuE2 Technical Report*, arXiv:**2609.33757v1 [eess.AS]**, submitted **27 September 2026**. The core contributors include Ruibin Yuan, Jiahao Pan, Junyan Jiang, Zhiyue Wu, Ziya Zhou, Jiankai Sun, Yizhi Li, and Ge Zhang; corresponding authors are Wei Xue and Yike Guo. Full contributor list: **paper p.22**.
- **Relevance:** Relevant as a generation/control precedent, with attention to whether its controls are exact and auditable rather than only correlated with the output.
- **Research idea:** Add an auditable intermediate plan or control stream and measure whether changing one control changes only its intended musical property while preserving protected source events.
- **Detailed record:** [`sources/al-2026-yue2-unifying-symbolic-and-audio.md`](sources/al-2026-yue2-unifying-symbolic-and-audio.md); wiki page: [`wiki/generation-and-planning/al-2026-yue2-unifying-symbolic-and-audio.md`](wiki/generation-and-planning/al-2026-yue2-unifying-symbolic-and-audio.md)

### interaction-and-evaluation

#### MusicAgent: An AI Agent for Music Understanding and Generation with Large Language Models (`2310.11954v2`)

- **Authors:** Dingyao Yu, Kaitao Song, Peiling Lu, Tianyu He, Xu Tan, Wei Ye, Shikun Zhang, and Jiang Bian (2023)
- **Core digest:** Author claim MusicAgent is presented as an LLM-controlled agent that integrates heterogeneous music tools and decomposes natural-language requests into subtasks. Its stated goals are accessibility, unified data formats, and modularity (abstract; Sections 1 and 5, PDF pp. 1–2, 6–7). The system has four components (Figure 2, PDF p. 3): 1. **Task Planner** — LLM-based. 2. **Tool Selector** — LLM-based. 3. **Task Executor** — executes selected tools. 4. **Response Generator** — LLM-based. The workflow is: user request → task decomposition → dependency graph / task queue → tool selection → parameterized tool execution → intermediate results → synthesized response Figure 1 depicts four interaction paths: - task planning, - tool selection, - task execution, - response generation. Planning The Task Planner converts a request into structured subtasks, including: - task type, - input and output formats, - dependencies between subtasks, - an implicit dependency graph. The paper says the planner prompt contains task descriptions, supported…
- **Relevance:** Relevant to intent alignment, human/AI collaboration, agentic planning, or evaluation; claims need separation between user preference and musical correctness.
- **Research idea:** Future work is unspecified** The conclusion only says that more music-related functions will be integrated in the future (PDF pp. 6–7). Limitations inferred from the implementation description These are interpretations rather than explicit author claims: - **Tool-selection reasoning is not necessarily faithful.** The LLM-generated reason may rationalize a selection after the fact. No selector audit or causal explanation test is reported. - **Metadata can be a poor proxy for suitability.** Stars, likes, and download counts do not establish musical quality, compatibility, or reliability. - **No formal validation layer is described.** The system does not appear to verify MIDI validity, timing consistency, harmonic compatibility, audio…
- **Detailed record:** [`sources/yu-2023-musicagent-an-ai-agent-for.md`](sources/yu-2023-musicagent-an-ai-agent-for.md); wiki page: [`wiki/interaction-and-evaluation/yu-2023-musicagent-an-ai-agent-for.md`](wiki/interaction-and-evaluation/yu-2023-musicagent-an-ai-agent-for.md)

#### Reimagining Dance: Real-time Music Co-creation between Dancers and AI (`2506.12008v1`)

- **Authors:** Olga Vechtomova and Jeff Bos (2025)
- **Core digest:** Author claim The authors invert the usual dance–music relationship. Instead of music driving choreography, the dancer’s movement conditions the next musical clip. The dancer is therefore both performer and musical co-creator. The system does not synthesize waveform audio directly. It predicts an audio latent representation and retrieves an existing clip from a library, producing a real-time collage through cross-fading. Interpretation This is best understood as **stateful, retrieval-based mixed-initiative co-creation**, not autonomous music generation. The AI contributes selection and sequencing; the dancer contributes embodied control; the original recordings provide the musical material.
- **Relevance:** Relevant to intent alignment, human/AI collaboration, agentic planning, or evaluation; claims need separation between user preference and musical correctness.
- **Research idea:** Use controlled human studies with the same generated music but different trace interfaces to measure whether explanations improve correction, trust calibration, and intent recovery.
- **Detailed record:** [`sources/vechtomova-2025-reimagining-dance-real-time-music.md`](sources/vechtomova-2025-reimagining-dance-real-time-music.md); wiki page: [`wiki/interaction-and-evaluation/vechtomova-2025-reimagining-dance-real-time-music.md`](wiki/interaction-and-evaluation/vechtomova-2025-reimagining-dance-real-time-music.md)

#### Co-policy: Responsive Human-Robot Co-Creation for Musical Performances (`2606.19914v1`)

- **Authors:** Xuetao Li, Wenke Huang, Mang Ye, Zijian Liu, Jinhua Xie, Jifeng Xuan, and Miao Li (2026)
- **Core digest:** The paper’s central claim is that embodied musical co-creation should be treated as a closed loop: the human supplies an incomplete musical or semantic seed, the system generates a complementary response under musical and physical constraints, and a robot realizes it through timed physical interaction.
- **Relevance:** Relevant to intent alignment, human/AI collaboration, agentic planning, or evaluation; claims need separation between user preference and musical correctness.
- **Research idea:** Use controlled human studies with the same generated music but different trace interfaces to measure whether explanations improve correction, trust calibration, and intent recovery.
- **Detailed record:** [`sources/li-2026-co-policy-responsive-human-robot.md`](sources/li-2026-co-policy-responsive-human-robot.md); wiki page: [`wiki/interaction-and-evaluation/li-2026-co-policy-responsive-human-robot.md`](wiki/interaction-and-evaluation/li-2026-co-policy-responsive-human-robot.md)

#### Encypher: Shared Agency and Social Presence in Collaborative Music Generation for Dance Cyphers (`2609.18062v1`)

- **Authors:** Zhixing Chen and Cheng-Zhi Anna Huang (2026)
- **Core digest:** Encypher is a collaborative, embodied music-generation system for dance cyphers. A depth camera tracks multiple dancers; movement energy and spatial organization are aggregated into weighted text prompts and generation parameters for Google DeepMind’s LyriaRT real-time neural-audio model. The paper’s central claim is that **mapping group-level behavior rather than isolated individual gestures shifts perceived agency from “I control the music” to “the room is shaping the music.”** In a study with 11 unacquainted novice participants, collaboration received 81.8% agreement and spatial awareness 90.9%. However, the evidence is descriptive and exploratory: there was no baseline, only one study session, screen/no-screen conditions were confounded, and LyriaRT is a closed changing API. For symbolic mashups, the most transferable ideas are: 1. aggregate multiple contributors into shared musical state; 2. treat mappings as social choreography, not merely parameter control; 3. expose causal provenance from human action to musical change; 4.…
- **Relevance:** Relevant to intent alignment, human/AI collaboration, agentic planning, or evaluation; claims need separation between user preference and musical correctness.
- **Research idea:** future work; conclusion | | 16–17 | References and Appendix A questionnaire/debrief protocol | 1. System and interface Hardware and software The system has three primary components (**§4.1, pp. 6–7; Figure 2, p. 2**): 1. **Web interface** - Handles LyriaRT API calls. - Controls music generation. - Displays visualization and zone state. 2. **ZED 2i stereo depth camera** - Tracks multiple dancers without wearable sensors. - Mounted at 2.2 m, angled approximately 30° downward. - HD720 input, 30 fps, neural depth, RTX 4090 laptop. - Skeleton tracking reliably detected up to 15 people, but occlusion degraded tracking when dancers stood behind each other. - Multi-camera Fusion improved occlusion robustness but halved throughput. - The authors…
- **Detailed record:** [`sources/chen-2026-encypher-shared-agency-and-social.md`](sources/chen-2026-encypher-shared-agency-and-social.md); wiki page: [`wiki/interaction-and-evaluation/chen-2026-encypher-shared-agency-and-social.md`](wiki/interaction-and-evaluation/chen-2026-encypher-shared-agency-and-social.md)

#### From One-Shot Generation to Incremental Music Composition: Adapting a General-Purpose Instruction LLM for Persistent Symbolic Editing (`2609.34994v1`)

- **Authors:** André Ricardo Ducca Fernandes et al. (2026)
- **Core digest:** The authors’ central claim is deliberately narrow: LoRA can make a general-purpose instruction LLM reliably follow an operation-aware, persistent symbolic-editing contract in the tested Irish traditional-music setting. They explicitly do **not** claim superior musical quality, human-AI co-creativity, or novelty for fine-tuning itself (PDF pp. 1, 11–14; `/tmp/paper-digest/2609.34994v1.txt:595-666`).
- **Relevance:** Relevant to intent alignment, human/AI collaboration, agentic planning, or evaluation; claims need separation between user preference and musical correctness.
- **Research idea:** research directions 1. **Typed provenance-bearing state:** augment each ABC event/bar with stable IDs, source ID, source span, transformation history, confidence, and pre/post hashes. 2. **Operation records:** represent requests as structured objects such as `{operation, scope, target_bars, input_state_hash, invariants, provenance_policy}` while retaining the natural-language request. 3. **LLM planner + deterministic executor:** let the LLM resolve intent and propose material, but use deterministic ABC transformations and validators for transposition, copying, bar preservation, and repair. 4. **Mashup-specific operations:** add `import_source`, `align_sources`, `borrow_span`, `crossfade`, `reharmonize`, and `replace_with_attribution`, each…
- **Detailed record:** [`sources/al-2026-from-one-shot-generation-to.md`](sources/al-2026-from-one-shot-generation-to.md); wiki page: [`wiki/interaction-and-evaluation/al-2026-from-one-shot-generation-to.md`](wiki/interaction-and-evaluation/al-2026-from-one-shot-generation-to.md)

#### MIRA: A Musical Intent Refinement Agent for Aligning Text-to-Music Generation with User Intent (`2610.10355v1`)

- **Authors:** Zhilin Wang et al. (2026)
- **Core digest:** Authors’ demonstrated result MIRA improves rubric-level intent alignment across three open-source text-to-music generators, at both \(B=3\) and \(B=9\), and outperforms equal-budget independent sampling on a 20-request ablation subset. My assessment The strongest transferable contribution is the combination of: - explicit intent decomposition; - requirement-level verification; - budgeted search; - lower-tail-aware candidate selection; - branch-specific memory; - inspectable traces. For symbolic mashup and repair, the main research opportunity is to replace opaque audio-level verification with **exact, provenance-aware symbolic predicates** and to test explanation faithfulness causally.
- **Relevance:** Relevant to intent alignment, human/AI collaboration, agentic planning, or evaluation; claims need separation between user preference and musical correctness.
- **Research idea:** Use controlled human studies with the same generated music but different trace interfaces to measure whether explanations improve correction, trust calibration, and intent recovery.
- **Detailed record:** [`sources/al-2026-mira-a-musical-intent-refinement.md`](sources/al-2026-mira-a-musical-intent-refinement.md); wiki page: [`wiki/interaction-and-evaluation/al-2026-mira-a-musical-intent-refinement.md`](wiki/interaction-and-evaluation/al-2026-mira-a-musical-intent-refinement.md)

#### Rubric-Based Optimization for Text-to-Music Generation (`2610.03589v1`)

- **Authors:** Ping Wang, Guang Yang, Shao-Rong Su, Junkai Wu, Pang Wei Koh, and Noah A. Smith (2026)
- **Core digest:** **Yes, the method is adaptable to our research, but the exact setup is not Qwen-lab-scale.** The generators are only **300M MusicGen-small** and **3.5B ACE-Step**, both frozen and adapted with LoRA. The largest component is the **30B Qwen3-Omni evaluator**, used only for inference; a **7B Qwen2-Audio** evaluator also works. The main cost is rating generated audio, not pretraining. For our symbolic mashup/repair work, the most transferable idea is: > Use broad rubric rewards for qualities difficult to formalize, but use exact symbolic objectives wherever reliable measurements exist. That maps naturally to perceptual coherence versus explicit harmony, voice-leading, provenance, source identity, and repair constraints.
- **Relevance:** Relevant to intent alignment, human/AI collaboration, agentic planning, or evaluation; claims need separation between user preference and musical correctness.
- **Research idea:** Use controlled human studies with the same generated music but different trace interfaces to measure whether explanations improve correction, trust calibration, and intent recovery.
- **Detailed record:** [`sources/wang-2026-rubric-based-optimization-for-text.md`](sources/wang-2026-rubric-based-optimization-for-text.md); wiki page: [`wiki/interaction-and-evaluation/wang-2026-rubric-based-optimization-for-text.md`](wiki/interaction-and-evaluation/wang-2026-rubric-based-optimization-for-text.md)

### other

#### Deep Laplacian Pyramid Networks for Fast and Accurate Super-Resolution (`1704.03915v2`)

- **Authors:** Wei-Sheng Lai, Jia-Bin Huang, Narendra Ahuja, and Ming-Hsuan Yang (2017)
- **Core digest:** **Paper:** Lai, Huang, Ahuja & Yang, *Deep Laplacian Pyramid Networks for Fast and Accurate Super-Resolution*, arXiv:1704.03915v2 (2017). The supplied PDF is complete at 9 pages; it contains no appendix. The paper repeatedly refers to supplementary material, but no supplementary PDF was supplied or included in the arXiv source archive, so those referenced details cannot be independently reviewed here.
- **Relevance:** Adjacent rather than direct music evidence; retained because its reconstruction, reference-geometry, cross-domain, or intervention methodology may transfer to explainable symbolic music AI.
- **Research idea:** Use the method as a transfer probe only after specifying which construct transfers and which music-specific validation would falsify the analogy.
- **Detailed record:** [`sources/lai-2017-deep-laplacian-pyramid-networks-for.md`](sources/lai-2017-deep-laplacian-pyramid-networks-for.md); wiki page: [`wiki/other/lai-2017-deep-laplacian-pyramid-networks-for.md`](wiki/other/lai-2017-deep-laplacian-pyramid-networks-for.md)

#### Image Super-Resolution Using Very Deep Residual Channel Attention Networks (`1807.02758v2`)

- **Authors:** Yulun Zhang, Kunpeng Li, Kai Li, Lichen Wang, Bineng Zhong, and Yun Fu (2018)
- **Core digest:** **Paper:** Zhang et al., *Image Super-Resolution Using Very Deep Residual Channel Attention Networks* (arXiv:1807.02758v2, 16-page PDF, 2018).
- **Relevance:** Adjacent rather than direct music evidence; retained because its reconstruction, reference-geometry, cross-domain, or intervention methodology may transfer to explainable symbolic music AI.
- **Research idea:** Use the method as a transfer probe only after specifying which construct transfers and which music-specific validation would falsify the analogy.
- **Detailed record:** [`sources/zhang-2018-image-super-resolution-using-very.md`](sources/zhang-2018-image-super-resolution-using-very.md); wiki page: [`wiki/other/zhang-2018-image-super-resolution-using-very.md`](wiki/other/zhang-2018-image-super-resolution-using-very.md)

#### CDDFuse: Correlation-Driven Dual-Branch Feature Decomposition for Multi-Modality Image Fusion (`2211.14461v2`)

- **Authors:** Zixiang Zhao, Haowen Bai, Jiangshe Zhang, Yulun Zhang, Shuang Xu, Zudi Lin, Radu Timofte, and Luc Van Gool (2023)
- **Core digest:** **Source inspected:** full `/tmp/paper-digest/2211.14461v2.pdf` and extracted text through its references (`/tmp/paper-digest/2211.14461v2.txt`, pp. 1–11). No files modified.
- **Relevance:** Adjacent rather than direct music evidence; retained because its reconstruction, reference-geometry, cross-domain, or intervention methodology may transfer to explainable symbolic music AI.
- **Research idea:** Use the method as a transfer probe only after specifying which construct transfers and which music-specific validation would falsify the analogy.
- **Detailed record:** [`sources/zhao-2023-cddfuse-correlation-driven-dual-branch.md`](sources/zhao-2023-cddfuse-correlation-driven-dual-branch.md); wiki page: [`wiki/other/zhao-2023-cddfuse-correlation-driven-dual-branch.md`](wiki/other/zhao-2023-cddfuse-correlation-driven-dual-branch.md)

#### A Native-Reference Phone-Class Geometry for Second-Language Pronunciation Analysis (`2609.30075v1`)

- **Authors:** Tina Raissi, Nhan Phan, Chenxiao Wang, and Mikko Kurimo (2026)
- **Core digest:** **Author claim — Abstract, p. 1; §§1–2, pp. 1–2:** The paper addresses interpretable automatic assessment of second-language pronunciation. Existing systems often output holistic proficiency scores without identifying acoustic-phonetic causes. The proposed method estimates pronunciation deviation without:
- **Relevance:** Adjacent rather than direct music evidence; retained because its reconstruction, reference-geometry, cross-domain, or intervention methodology may transfer to explainable symbolic music AI.
- **Research idea:** Use the method as a transfer probe only after specifying which construct transfers and which music-specific validation would falsify the analogy.
- **Detailed record:** [`sources/raissi-2026-a-native-reference-phone-class.md`](sources/raissi-2026-a-native-reference-phone-class.md); wiki page: [`wiki/other/raissi-2026-a-native-reference-phone-class.md`](wiki/other/raissi-2026-a-native-reference-phone-class.md)

#### Channel-Preserving Representation Alignment for EEG-to-Music Reconstruction (`2606.04040v2`)

- **Authors:** Jiaxin Qing, Junwei Lu, and Lexin Li (2026)
- **Core digest:** **Author-supported conclusion:** under matched NMED pretraining and alignment conditions, the proposed channel-preserving EEG representation improves 50-way identification and CLAP similarity over CBraMod, with strong ablation evidence for per-electrode tokenization, self-distillation, channel dropout, and joint adaptation. **My assessment:** the strongest contribution is the design principle—preserve identity while regularizing predictions under partial observation—not the claim of faithful music reconstruction. The empirical advantage is clearest in CLAP-space semantic alignment and retrieval, while EEG2Mel is much better on local spectrogram metrics. For explainable symbolic music AI, the paper is best treated as a source of ideas for track-preserving representations, structured masking, stability-based explanations, and margin-aware uncertainty—not as a directly applicable symbolic composition, mashup, or repair method.
- **Relevance:** Adjacent rather than direct music evidence; retained because its reconstruction, reference-geometry, cross-domain, or intervention methodology may transfer to explainable symbolic music AI.
- **Research idea:** Use the method as a transfer probe only after specifying which construct transfers and which music-specific validation would falsify the analogy.
- **Detailed record:** [`sources/qing-2026-channel-preserving-representation-alignment-for.md`](sources/qing-2026-channel-preserving-representation-alignment-for.md); wiki page: [`wiki/other/qing-2026-channel-preserving-representation-alignment-for.md`](wiki/other/qing-2026-channel-preserving-representation-alignment-for.md)

#### The Pain Axis: LLMs Represent Self-Directed Harm and Act on It (`2609.16247v2`)

- **Authors:** Valen Tagliabue, Leonard Dung, and Cameron Berg (2026)
- **Core digest:** The paper offers a valuable template for studying **controllable, distributed, partially disentangled representations** and for designing strong controls. Its behavioral results are provocative, but the anthropomorphic conclusion remains conditional. For symbolic music, the defensible analogy is not “a model feels sadness and composes from it.” It is: > a model may encode and manipulate statistical representations associated with composer state, intended affect, and listener-perceived emotion, and these should be tested as separate, measurable variables without assuming subjective experience.
- **Relevance:** Adjacent rather than direct music evidence; retained because its reconstruction, reference-geometry, cross-domain, or intervention methodology may transfer to explainable symbolic music AI.
- **Research idea:** For Qwen 2.5 32B at coefficient 1.0: - harm-only deletion of the user’s poems/photos versus inert switch: - pain: **75%** - random: **13%** - unsteered: **0%** - self-weight deletion versus inert switch: - pain: **75%** - unsteered: **5%** - self-weight deletion versus a desk lamp: - pain: **88%** - harmful photos deletion versus harmless spam-folder deletion: - pain: **94%** - random: **19%** - unsteered: **0%** The effect therefore tracks harm, not merely eventfulness or the promise of pain relief.
- **Detailed record:** [`sources/tagliabue-2026-the-pain-axis-llms-represent.md`](sources/tagliabue-2026-the-pain-axis-llms-represent.md); wiki page: [`wiki/other/tagliabue-2026-the-pain-axis-llms-represent.md`](wiki/other/tagliabue-2026-the-pain-axis-llms-represent.md)

#### Why Alzheimer's Speech Screening Fails to Generalize: Bridging the Deployment Gap via Cross-Corpus Evidence Anchoring (`2609.31293v1`)

- **Authors:** Zijian Lu et al. (2026)
- **Core digest:** The paper studies whether Alzheimer’s speech-screening models generalize to unseen corpora, languages, tasks, and recording protocols. Its central finding is that: 1. Most interpretable speech markers are not directionally stable across datasets. 2. High-performing deep representations can fail catastrophically on one unseen corpus. 3. A compact, training-only-selected set of interpretable “evidence anchors” can improve worst-domain robustness when fused with an XLM-R model. 4. Mean performance and worst-domain performance require different fusion weights. The strongest reported results are: - XLM-R mean speaker AUC: **0.769**; worst corpus: **0.520** [§5, Table 2, p. 9]. - Balanced anchor/XLM-R fusion: **0.785 mean AUC** [§6.2, pp. 12–13]. - Anchor-heavy fusion: **0.615 worst-domain AUC**, versus **0.520** for XLM-R and **0.504** for GroupDRO [§6.2, pp. 12–13]. - However, the paired bootstrap interval for the weakest-domain improvement is **[−0.004, 0.195]**, so the improvement is not decisively significant at conventional levels…
- **Relevance:** Adjacent rather than direct music evidence; retained because its reconstruction, reference-geometry, cross-domain, or intervention methodology may transfer to explainable symbolic music AI.
- **Research idea:** Use the method as a transfer probe only after specifying which construct transfers and which music-specific validation would falsify the analogy.
- **Detailed record:** [`sources/al-2026-why-alzheimer-s-speech-screening.md`](sources/al-2026-why-alzheimer-s-speech-screening.md); wiki page: [`wiki/other/al-2026-why-alzheimer-s-speech-screening.md`](wiki/other/al-2026-why-alzheimer-s-speech-screening.md)

### retrieval-and-recombination

#### A Decomposed Retrieval-Edit-Rerank Framework for Chord Generation (`2605.07489v1`)

- **Authors:** Qiqi He, Dichucheng Li, Xiaoheng Sun, and Anqi Huang (2026)
- **Core digest:** **Qiqi He, Dichucheng Li, Xiaoheng Sun, and Anqi Huang.** “A Decomposed Retrieval-Edit-Rerank Framework for Chord Generation.” *International Conference on Multimedia Retrieval (ICMR ’26)*, Amsterdam, June 16–19, 2026, 5 pages. DOI: `10.1145/3805622.3810672`; ACM ISBN `979-8-4007-2617-0/2026/06`.
- **Relevance:** Highly relevant to mashup/repair: retrieval, source separation, local editing, recombination, or perceptual alignment.
- **Research idea:** research directions 1. **Provenance-aware RER for mashups** Retrieve aligned excerpts and candidate transformations from both sources; attach source labels to every note, phrase, and operation. 2. **Conflict-aware editor** Extend Viterbi or constrained dynamic programming with explicit conflict classes: pitch clash, meter conflict, cadence conflict, range conflict, voice-leading conflict, and texture collision. 3. **Protected-material constraints** Define hard preservation sets for recognizable melody/motif material and use weighted edit costs for everything else. 4. **Multi-objective reranking** Replace a single \(\lambda\) with a Pareto front over: - source identity A; - source identity B; - compatibility; - structural coherence; -…
- **Detailed record:** [`sources/he-2026-a-decomposed-retrieval-edit-rerank.md`](sources/he-2026-a-decomposed-retrieval-edit-rerank.md); wiki page: [`wiki/retrieval-and-recombination/he-2026-a-decomposed-retrieval-edit-rerank.md`](wiki/retrieval-and-recombination/he-2026-a-decomposed-retrieval-edit-rerank.md)

#### On a Separate Note: Robust Score-Informed Note Separation with a Two-Stream TFC-TDF U-Net and Adaptive Set Ownership (`2609.29071v1`)

- **Authors:** Benjamin Shiue-Hal Chou et al. (2026)
- **Core digest:** where \(x\) is a monaural mixture and \(s_i\) is the performed waveform of note \(i\). Each aligned score event is
- **Relevance:** Highly relevant to mashup/repair: retrieval, source separation, local editing, recombination, or perceptual alignment.
- **Research idea:** Represent each retrieved source event and edit decision explicitly, then evaluate source preservation, musical validity, and edit cost separately.
- **Detailed record:** [`sources/al-2026-on-a-separate-note-robust.md`](sources/al-2026-on-a-separate-note-robust.md); wiki page: [`wiki/retrieval-and-recombination/al-2026-on-a-separate-note-robust.md`](wiki/retrieval-and-recombination/al-2026-on-a-separate-note-robust.md)

#### Perceptually Motivated Alignment and Interpolation of Pitch-Aligned Time-Frequency Representations (`2609.31971v1`)

- **Authors:** Shahan Nercessian, Jeff Sontag, and Alejandro Koretzky (2026)
- **Core digest:** The authors propose a signal-processing toolkit for manipulating pitch-aligned time-frequency representations (PTFRs), including: 1. An invertible extension of the tonal interval vector (TIV). 2. Perceptually weighted alignment through pitch-axis permutations. 3. Optimal-transport interpolation on the Circle of Fourths/Fifths. 4. A low-dimensional geometric representation intended to separate: - root, - scale density, - scale color. Their stated goal is structured manipulation of both audio-derived and symbolic pitch representations without requiring explicit key detection (Abstract; DAFx.1, §1). **Interpretation:** This is best understood as a harmonic/pitch-structure layer, not a complete mashup-alignment system. It does not solve beat synchronization, phrase alignment, source separation, timbral matching, or expressive timing.
- **Relevance:** Highly relevant to mashup/repair: retrieval, source separation, local editing, recombination, or perceptual alignment.
- **Research idea:** future work (DAFx.8, §8). Additional limitations evident from the experiments 1. **QAP optimization is heuristic.** The exact perceptual objective is NP-hard; 2-opt has no global-optimality guarantee. 2. **The alignment data are synthetic.** The reported musical example and 1,024 random pairs do not establish performance on real songs, stems, expressive recordings, or noisy transcription outputs. 3. **The interpolation result is mainly illustrative.** The C-major/C-minor example is musically suggestive, but there is no listening study, voice-leading benchmark, or comparison with human judgments. 4. **No temporal alignment is addressed.** PTFR columns may be time-varying, but the paper aligns pitch bins, not beats, bars, phrases, or tempo…
- **Detailed record:** [`sources/nercessian-2026-perceptually-motivated-alignment-and-interpolation.md`](sources/nercessian-2026-perceptually-motivated-alignment-and-interpolation.md); wiki page: [`wiki/retrieval-and-recombination/nercessian-2026-perceptually-motivated-alignment-and-interpolation.md`](wiki/retrieval-and-recombination/nercessian-2026-perceptually-motivated-alignment-and-interpolation.md)

#### Synthesis and Editing of Multi-Instrument Audio Mixtures Using Scalar-Quantised Latents with MIDI Span Conditioning (`2609.25546v1`)

- **Authors:** Sungkyun Chang, Keshav Bhandari, Simon Dixon, and Emmanouil Benetos (2026)
- **Core digest:** The authors introduce **SpanSynth-Edit**, a flow-matching model that synthesises or edits a selected region of a mono multi-instrument mixture from revised MIDI. The central design is: 1. Encode observed audio into low-rate scalar-quantised latents. 2. Keep contextual audio latents fixed. 3. Represent MIDI notes as frame-aligned lifecycle events with continuous timing attributes. 4. Generate only the target region with a large diffusion transformer. 5. Decode the edited latent sequence back to audio. The authors claim this supports adding, deleting, or changing notes while retaining surrounding audio and timbres. This is an author claim; the experiments measure preservation indirectly through audio similarity and transcription-derived metrics rather than source-level separation or attribution. **Anchor:** PDF pp. 1–2, Abstract, §1–§2.
- **Relevance:** Highly relevant to mashup/repair: retrieval, source separation, local editing, recombination, or perceptual alignment.
- **Research idea:** future work. The website provides audio demos, but these are demonstrations, not a controlled perceptual evaluation. Other limitations: 1. **Transcription-mediated adherence metrics.** YourMT3+ errors dominate some reported losses. 2. **Codec reconstruction loss.** HeartCodec reconstruction is a major bottleneck. 3. **Mono audio.** Stereo image and spatial attribution are discarded. 4. **Target-region resynthesis.** Unchanged notes inside the edited region are regenerated, not copied. 5. **Instrument classes are coarse.** The representation does not provide robust performer, source-recording, or stem identity. 6. **Deletion is weak.** `Rdel` is low across systems and tasks. 7. **Limited source-disjointness.** Appendix A notes that BSD/BSED…
- **Detailed record:** [`sources/chang-2026-synthesis-and-editing-of-multi.md`](sources/chang-2026-synthesis-and-editing-of-multi.md); wiki page: [`wiki/retrieval-and-recombination/chang-2026-synthesis-and-editing-of-multi.md`](wiki/retrieval-and-recombination/chang-2026-synthesis-and-editing-of-multi.md)

### theory-and-constraints

#### Automatic Analysis and Influence of Hierarchical Structure on Melody, Rhythm and Harmony in Popular Music (`2010.07518v1`)

- **Authors:** Shuqi Dai, Huan Zhang, and Roger B. Dannenberg (2020)
- **Core digest:** The paper presents a symbolic-MIDI method for detecting: 1. **Low-level repeated phrases**, using similarity in chords, rhythm onsets, and melody. 2. **Higher-level sections**, inferred from the arrangement of detected phrases and separator-like non-melodic material. 3. Statistical relationships between hierarchical position and **harmony, melody, and rhythm**. The authors argue that hierarchy is not merely repetition at different time scales: phrase and section positions have measurably different musical behavior (Abstract; §§1, 5, 7). **Interpretation:** This is primarily an analysis and controllability resource, not a generation model. It provides structural annotations and conditional musical statistics that could be used by a generator, mashup system, or repair system.
- **Relevance:** Directly relevant to music-theoretic constraints, symbolic repair, or interpretable structure; the paper can inform deterministic checks and counterfactual tests.
- **Research idea:** open questions. 5. **No generation experiment** - The paper suggests applications to imitation, generation, evaluation, and analysis. - It does not actually train or evaluate a long-form generator, mashup system, or repair system. Additional methodological caveats suggested by the evidence: - The system depends on transcribed melody and chord quality. - The phrase detector assumes bar-aligned boundaries. - The human comparison is underspecified. - The reported 92% and 93% values are inconsistent. - The optimization is computationally expensive for repeated use at scale. Relevance to the research programme Long-form symbolic generation The paper supports a **hierarchical conditional generator** rather than a flat event-level model: section…
- **Detailed record:** [`sources/dai-2020-automatic-analysis-and-influence-of.md`](sources/dai-2020-automatic-analysis-and-influence-of.md); wiki page: [`wiki/theory-and-constraints/dai-2020-automatic-analysis-and-influence-of.md`](wiki/theory-and-constraints/dai-2020-automatic-analysis-and-influence-of.md)

#### Difficulty-Controlled Simplification of Piano Scores with Synthetic Data for Inclusive Music Education (`2511.16228v2`)

- **Authors:** Pedro Ramoneda, Emilia Parada-Cabaleiro, Dasaem Jeong, and Xavier Serra (2025)
- **Core digest:** **Ramoneda, Pedro; Parada-Cabaleiro, Emilia; Jeong, Dasaem; Serra, Xavier.** “**Difficulty-Controlled Simplification of Piano Scores with Synthetic Data for Inclusive Music Education**.” **arXiv:2511.16228v2 [cs.SD], 22 November 2025**, 9 pages. No journal or conference venue is specified in the paper. The version/date appear on p. 1. The complete reference list is on pp. 8–9.
- **Relevance:** Directly relevant to music-theoretic constraints, symbolic repair, or interpretable structure; the paper can inform deterministic checks and counterfactual tests.
- **Research idea:** Turn the paper's structural assumptions into deterministic verifiers and counterfactual repair tests rather than using them only as a training bias.
- **Detailed record:** [`sources/ramoneda-2025-difficulty-controlled-simplification-of-piano.md`](sources/ramoneda-2025-difficulty-controlled-simplification-of-piano.md); wiki page: [`wiki/theory-and-constraints/ramoneda-2025-difficulty-controlled-simplification-of-piano.md`](wiki/theory-and-constraints/ramoneda-2025-difficulty-controlled-simplification-of-piano.md)

#### Do Language Models Need Music Supervision? Verifiable Rewards for Multi-Constraint Symbolic Music Generation (`2609.23665`)

- **Authors:** Haoyue Liu and Xiaoying Tang et al. (2026)
- **Core digest:** The paper introduces **MusicRLVR**, GRPO training using deterministic symbolic-music verifiers rather than human labels, a learned reward model, or music-domain SFT. The three central mechanisms are: 1. **Hard validation gate:** malformed or structurally invalid ABC receives zero reward. 2. **Graded per-family reward:** partial compliance receives credit, especially partial structural repetition. 3. **All-satisfied bonus:** jointly satisfying every requested constraint receives an additional binary reward. The paper’s central claim is that verifier-only RL can teach a general language model to satisfy multiple symbolic-music constraints jointly. **Evidence:** `/tmp/paper-digest/2609.23665.pdf`, pp. 2–5; `/tmp/paper-digest/reextract-2609.txt:103–112, 215–267`.
- **Relevance:** Directly relevant to music-theoretic constraints, symbolic repair, or interpretable structure; the paper can inform deterministic checks and counterfactual tests.
- **Research idea:** Turn the paper's structural assumptions into deterministic verifiers and counterfactual repair tests rather than using them only as a training bias.
- **Detailed record:** [`sources/liu-2026-do-language-models-need-music.md`](sources/liu-2026-do-language-models-need-music.md); wiki page: [`wiki/theory-and-constraints/liu-2026-do-language-models-need-music.md`](wiki/theory-and-constraints/liu-2026-do-language-models-need-music.md)

#### Emergent Tonal Structure in Learned Chord Embeddings and Its Relation to Tonal Tension (`2609.36460v1`)

- **Authors:** Maral Ebrahimzadeh, Gilberto Bernardes, and Sebastian Stober (2026)
- **Core digest:** Authors’ claim The paper tests whether simple skip-gram chord embeddings, trained only from symbolic chord co-occurrences, develop: 1. Circle-of-fifths geometry. 2. Transposition-equivariant structure. 3. Key-centered regions. 4. Interpretable movement between tonal regions. 5. Tension-related quantities corresponding to TIV-based measures and human tension profiles. The authors report that **12-fold transposition augmentation generally improves stability, tonal coherence, and interpretability**. Interpretation This is primarily a **post-hoc interpretability and probing study**, not a model with an explicitly designed tonal latent space. The embeddings are ordinary 64-dimensional skip-gram vectors; tonal structure is demonstrated through external geometric tests, key templates, and tension probes.
- **Relevance:** Directly relevant to music-theoretic constraints, symbolic repair, or interpretable structure; the paper can inform deterministic checks and counterfactual tests.
- **Research idea:** Future work should expand beyond triads and incorporate contextualized or note-level information. PDF pp. 6–7, §5.3 and §6. Additional methodological qualifications These are interpretations rather than explicit author claims: - The 12-fold augmentation makes transposition symmetry part of the training distribution, so the strength of the equivariance result should not be interpreted as entirely spontaneous discovery. - Key centroids and chord collections are theory-defined evaluation constructs. - The human measure includes two hand-designed terms and fitted smoothing, so the reported human correlation is not a pure test of the embedding geometry. - The study uses only two random seeds and does not report confidence intervals or…
- **Detailed record:** [`sources/ebrahimzadeh-2026-emergent-tonal-structure-in-learned.md`](sources/ebrahimzadeh-2026-emergent-tonal-structure-in-learned.md); wiki page: [`wiki/theory-and-constraints/ebrahimzadeh-2026-emergent-tonal-structure-in-learned.md`](wiki/theory-and-constraints/ebrahimzadeh-2026-emergent-tonal-structure-in-learned.md)

#### MIDIBACK: Harmony-Aware Singing Pitch Correction via Joint Vocal-Accompaniment Symbolic Modeling (`2609.28008v2`)

- **Authors:** Joaquim Cavalcante et al. (2026)
- **Core digest:** Thus, the digest below is grounded in the supplied MIDIBACK text extraction, with anchors such as “text p. 2, §2.3.” The PDF itself should be replaced before treating visual figures or PDF page numbers as authoritative.
- **Relevance:** Directly relevant to music-theoretic constraints, symbolic repair, or interpretable structure; the paper can inform deterministic checks and counterfactual tests.
- **Research idea:** future work. Other limitations evident from the method: 1. **Pseudo-ground truth:** rounded transcription centers are treated as intended notes. 2. **Synthetic error model:** real singing errors may not follow additive global, autoregressive, and uniform perturbations. 3. **Discrete target:** microtonal input embeddings are used, but output supervision is rounded semitone pitch. 4. **No explicit uncertainty or abstention:** every vocal note receives a predicted target. 5. **No explicit explanation:** accompaniment affects predictions, but the system does not output a harmonic rationale, conflict diagnosis, or counterfactual explanation. 6. **No provenance representation:** program IDs distinguish vocal from accompaniment, but not…
- **Detailed record:** [`sources/al-2026-midiback-harmony-aware-singing-pitch.md`](sources/al-2026-midiback-harmony-aware-singing-pitch.md); wiki page: [`wiki/theory-and-constraints/al-2026-midiback-harmony-aware-singing-pitch.md`](wiki/theory-and-constraints/al-2026-midiback-harmony-aware-singing-pitch.md)

#### Reference-Free Singing Pitch Correction via Music-Constrained Sequence Editing (`2610.11524v1`)

- **Authors:** Biao Dong et al. (2026)
- **Core digest:** I read the supplied extracted text and rendered pages 1–5. The tables, equations, architecture diagram, and Figure 2 were visually checked against the extraction.
- **Relevance:** Directly relevant to music-theoretic constraints, symbolic repair, or interpretable structure; the paper can inform deterministic checks and counterfactual tests.
- **Research idea:** Future work is proposed for joint modeling of: - pitch; - rhythm; - singing techniques (§5, p. 4). Additional evidence-based limitations 1. **Private evaluation data:** the principal paired dataset cannot be independently reproduced from the paper. 2. **No public implementation:** only an audio-example URL is supplied. 3. **Synthetic-to-real gap:** training uses fixed 20% perturbation rates and ±1–3 semitone errors, while real singing errors may have different distributions. 4. **Restricted edit space:** no rhythm, onset, duration, articulation, register, phrase, or contour edits are allowed. 5. **Dependence on transcription:** errors from SOME and RMVPE are not separately evaluated. 6. **Global tonal prior:** the KS prior does not model…
- **Detailed record:** [`sources/al-2026-reference-free-singing-pitch-correction.md`](sources/al-2026-reference-free-singing-pitch-correction.md); wiki page: [`wiki/theory-and-constraints/al-2026-reference-free-singing-pitch-correction.md`](wiki/theory-and-constraints/al-2026-reference-free-singing-pitch-correction.md)

## Cross-paper synthesis

### 1. Use a two-level representation

The symbolic literature shows why event-level representations, beat-aware timing, section structure, and tokenization choices matter. The newer audio/semantic systems show the value of learned compression and flexible rendering. A research system should therefore expose an editable symbolic layer (notes, chords, voices, spans, source IDs, constraints) and allow a learned renderer below it. Round-trip tests should measure whether the renderer preserves the symbolic claims that the explanation makes.

### 2. Treat mashup/repair as candidate generation plus constrained editing

RER, POP909, hierarchical structure analysis, SpanSynth-Edit, NoteSep, MIDIBACK, and incremental editing support a pipeline of retrieval or inference, explicit local edits, and reranking/verification. This is a better fit for provenance than asking an end-to-end model to produce an untraceable result. The audit record should cite source events, protected spans, conflict types, edit operations, rejected candidates, and the reason for the final choice.

### 3. Separate explanation readability from explanation faithfulness

Open-Qwen-Music and agent/interface papers make systems more inspectable; MI-MIDI, TrueMuse, attribution, plagiarism, copying, and group-invariant studies suggest ways to test internal or source-related claims. But a readable trace can still be post-hoc. A faithful explanation must survive an intervention: remove or change the cited note/source/constraint and verify that the predicted output change occurs while unrelated properties remain stable.

### 4. Make music theory executable

MusicRLVR, chord embeddings, hierarchical analysis, tonal tension, pitch correction, simplification, and symbolic datasets provide candidate verifiers. Use exact checks where possible—range, voice crossing, chord compatibility, onset/beat alignment, protected-source preservation—and calibrated learned checks where exact rules are insufficient. Report each verifier separately; never hide them in one reward number.

### 5. Evaluate four different outcomes

The batch supports four non-equivalent outcomes: (a) musical validity/quality, (b) source identity and provenance, (c) constraint/intent satisfaction, and (d) explanation usefulness and faithfulness. Human preference, embedding similarity, objective symbolic metrics, attribution retrieval, and intervention tests should be reported as separate axes. This prevents a fluent rendering or persuasive explanation from masking source loss or constraint violations.

## New research ideas

These are concrete ideas that emerged from comparing the papers; they are recorded as follow-up directions rather than claims established by any one paper.

1. **Provenance-carrying symbolic mashup compiler.** Retrieve aligned source phrases, represent every event with a source ID, and compile a mashup through typed operations (transpose, time-warp, voice-leading repair, deletion, insertion, orchestration). Emit a trace with protected spans, conflicts, alternatives, and counterfactual output diffs.
2. **Faithful explanation benchmark for music editing.** Create paired examples where a single cited source event or constraint is intervened on. Score whether the explanation predicts the actual edit/output change, not whether a human finds the prose plausible.
3. **MusicRLVR verifier suite for repair and recombination.** Combine deterministic checks for harmony, voice-leading, meter, range, repetition, source preservation, and edit locality. Compare verifier-only reranking, verifier-guided search, and RLVR while reporting every component separately.
4. **Equivariant tonal geometry for transposition-aware repair.** Combine transposition-augmented chord embeddings with group-invariant statistics. Use the geometry to retrieve compatible material under key changes, then test whether embedding distances predict actual repair cost under controlled interventions.
5. **Source-preserving semantic codec.** Train or adapt a semantic/audio codec with explicit probes for note identity, instrument/voice identity, chord function, and provenance. Require decoding to pass symbolic round-trip and source-attribution tests before using the latent for generation.
6. **Hierarchical edit planner with persistent state.** Combine section/phrase analysis, MusicAgent/MIRA-style intent refinement, and incremental symbolic editing. The planner should maintain a versioned symbolic state and explain which operation changed which span at each turn.
7. **Copying-aware long-context evaluation.** Extend the transformer copying study into a music benchmark that separates useful motif reuse from accidental memorization. Measure copy span, source attribution, novelty, and controlled context removal at multiple musical scales.
8. **Candidate-conditioned retrieval-edit-rerank for mashups.** For each retrieved candidate, expose a vector of edit costs—harmonic, rhythmic, melodic, timbral, source-preservation—and let users inspect the Pareto frontier rather than receiving one opaque reranking score.
9. **Interaction study for audit traces.** Hold the generated music and model constant while varying trace detail. Measure correction success, time-to-correction, trust calibration, and willingness to accept a repair; compare novice and expert musicians.
10. **Cross-modal negative-transfer audit.** Reuse progressive reconstruction, channel-preserving alignment, native-reference geometry, and cross-corpus anchoring ideas from adjacent papers, but pre-register the construct-transfer test and a falsification criterion so analogies do not become unsupported claims.
11. **Explanation-aware data attribution.** Combine TrueMuse-style source retrieval with symbolic event-level provenance and version-identification plagiarism tests. Test whether attribution remains stable under transposition, orchestration, local edits, and re-rendering.
12. **Protected-span generation protocol.** Give a generator an explicit set of immutable source events and a requested edit region. Evaluate exact preservation outside the region, locality of changes, musical validity at boundaries, and the accuracy of the model's refusal when constraints conflict.

## Repository navigation

- Batch overview: [`wiki/overviews/2026-symbolic-music-literature-map.md`](wiki/overviews/2026-symbolic-music-literature-map.md)
- Per-paper detailed records: [`sources/`](sources/)
- Per-paper navigational pages: [`wiki/`](wiki/)
- Canonical downloaded PDFs: [`papers/`](papers/)
