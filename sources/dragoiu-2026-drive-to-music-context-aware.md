---
title: "Drive-to-Music: Context-Aware Generative Audio for In-Vehicle Experiences"
authors: "Dragoiu and Nabizadeh"
year: 2026
doi: 10.48550/arXiv.2608.12615
category: generation-and-planning
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/dragoiu-2026-drive-to-music-context-aware.pdf"
pdf_filename: dragoiu-2026-drive-to-music-context-aware.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

All generative models are intended to run in the cloud. An in-vehicle service collects vehicle data, sends requests, receives generated music and media, and plays them back (§2, p. 1). Internet connectivity is therefore required.

## 1. Document Information

- **Canonical source:** arXiv `2608.12615v1`; official PDF preserved as `dragoiu-2026-drive-to-music-context-aware.pdf`.
- **Full-paper evidence:** delegate digest `del_mv415ez6_uoaw.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### Paper and contribution

**Dragoiu and Nabizadeh, “Drive-to-Music: Context-Aware Generative Audio for In-Vehicle Experiences,” arXiv:2608.12615v1, 12 Aug 2026.** Authors are from Mercedes-Benz Research & Development North America.

**Author claim:** Drive-to-Music generates personalized in-vehicle music from front-facing camera imagery plus vehicle telemetry, translating context into musical descriptors and then generated audio (Abstract; §1, p. 1).

**Assessment:** This is primarily a system-integration and model-selection paper. It does **not** introduce a new trained multimodal music architecture, symbolic composition model, or affect-recognition model. The pipeline chains existing VLM, LLM, image-generation, and audio-generation systems through textual prompts.

---

### Complete architecture

#### Inputs and deployment

The stated inputs are:

- Front-facing camera image of the road scene.
- Vehicle speed.
- Outside temperature.

The paper says future versions may add traffic, navigation, and user preferences (§4, p. 4).

All generative models are intended to run in the cloud. An in-vehicle service collects vehicle data, sends requests, receives generated music and media, and plays them back (§2, p. 1). Internet connectivity is therefore required.

#### Pipeline

Figure 1 and §2 (pp. 1–2) describe these stages:

1. **Image-description stage**
   - A VLM converts the camera image into a one-sentence scene description.
   - The prompt asks for surroundings, landmarks, vegetation, weather, and sky conditions.
   - It explicitly says to ignore people and offensive content.

2. **Music-description stage**
   - An LLM combines the scene description with speed and temperature levels.
   - It produces free-form musical descriptors involving mood, atmosphere, style, instrumentation, rhythm, and energy.

3. **Music generation**
   - The music description conditions the audio-generation model.
   - The selected model is Stable Audio 2.5.
   - The authors prioritize instrumental music and tracks of at least 90 seconds to reduce transitions (§3, p. 3).

4. **Parallel media generation**
   - Cover art is generated from the scene description.
   - A separate LLM generates a short title from the music description.

5. **Dominant-color extraction**
   - A histogram-based algorithm masks muted sky regions and low-information gray regions such as roads and buildings.
   - Remaining colors are mapped to an in-vehicle palette.
   - The selected color controls ambient vehicle lighting (§2, p. 2).
   - This is a lighting-control pathway, not a direct audio-control pathway.

6. **Safety and quality checks**
   - Music: quality scoring, loudness, true peak, sudden-jump detection, and noise-floor analysis.
   - Cover art: offensive-content screening.
   - Song title: vulgarity/disallowed-language filtering.
   - Failed outputs are regenerated (§2, p. 2).

The abstract also claims smooth transitions as context changes, but no specific transition, crossfade, continuation, or latent-conditioning algorithm is given.

---

### Prompts and controllability

Appendix B, Table 6 (p. 6), gives the exact high-level prompts:

- **Image VLM:** “describe the image by focusing on surroundings, landmarks, vegetation, weather; ignore people and offensive content in the image; limit the response to one sentence”
- **Music LLM:** “what kind of music would fit best <image description>?; take into account that the car drives at <speed level> speed and outside is <temperature level>; return only the music description, no other text”
- **Song generation:** `generate <music description>`

This intermediate text is inspectable and potentially editable, making it the main explainability surface.

**Interpretation:** Control is currently indirect and coarse. The system exposes scene, speed, temperature, mood, atmosphere, and style through prompts, but does not expose explicit tempo, key, mode, chord progression, density, form, instrumentation weights, or loudness targets. The intermediate description is also free-form, so the same context may produce inconsistent controls.

---

### Model-selection experiments

The authors report evaluating approximately ten samples per model (§3, p. 3). These are component benchmarks, not a full end-to-end driving study.

#### Table 1: image-understanding VLMs, p. 3

| Model | Capacity | Latency | CLIP score |
|---|---:|---:|---:|
| LiquidAI LFM 2.5 VL 1.6B | 1.6B | 1.2 s* | 26.43 |
| Qwen 3 VL 2B Instruct | 2B | 3.9 s* | 26.59 |
| Gemini 2.5 Flash Lite | 150B | 0.6 s | 27.25 |

`*` Local NVIDIA T4, 16 GB; Gemini was an API call.

The authors select **LiquidAI LFM 2.5 VL 1.6B**, despite Gemini having both lower latency and the highest CLIP score. The paper does not fully explain this selection.

**Assessment:** The comparison is not deployment-equivalent: local T4 inference is compared with an API call. Network latency, privacy, rate limits, and cloud variability are not reported.

#### Table 2: music-description LLMs, p. 3

| Model | Capacity | Latency | Quality |
|---|---:|---:|---:|
| LiquidAI LFM 2.5 1.2B Instruct | 1.2B | 0.7 s* | 5/5 |
| Qwen 3.5 2B | 2B | 2.4 s* | 4/5 |
| Gemini 2.5 Flash Lite | 150B | 1.2 s | 5/5 |

The quality score is based on stability and relevance on curated test cases. The authors select **LiquidAI**, which is both fastest and tied for highest quality. The same model is used for song-title generation.

#### Table 3: music-generation models, p. 3

| Model | Latency | MuQ-MuLan | TAQS |
|---|---:|---:|---:|
| ElevenLabs | 15.7 s | 0.09 | 72.22 |
| Mubert | 7.4 s | 0.29 | 91.26 |
| Stable Audio 2.5 | 6.2 s | 0.36 | 78.03 |

All values are API-call measurements.

- **MuQ-MuLan** measures prompt–audio semantic alignment.
- **TAQS** is a custom 0–100 technical score using loudness, true peak, clipping, and sudden loudness jumps.

The authors select **Stable Audio 2.5**, because it has the best semantic-alignment score and lowest latency. Mubert has substantially better TAQS, so the choice prioritizes semantic alignment and speed over technical-audio score.

#### Table 4: cover-art models, p. 4

| Model | Capacity | Latency | GenEval |
|---|---:|---:|---:|
| Stable Diffusion 3.5 Large Turbo | 8B | 1.4 s* | 0.66 |
| Qwen Image | 20B | 40.4 s* | 0.91 |
| Gemini 2.5 Flash Image | 150B | 6.5 s | 0.96 |

`*` Local NVIDIA A100, 80 GB.

The authors select **Stable Diffusion 3.5 Large Turbo** for latency, despite its lower GenEval score.

#### Latency conclusion

The paper reports component latencies but **not**:

- End-to-end latency.
- Context-update frequency.
- Network variability.
- Audio generation duration.
- Failure/retry rates.
- Compute cost.
- Playback-buffering behavior.

Therefore, “real-time” and “low latency” are feasibility claims rather than demonstrated end-to-end guarantees.

---

### Examples and qualitative evidence

Appendix A, Table 5 (p. 5), gives five examples:

1. Low speed, warm temperature, urban street → upbeat indie folk with acoustic guitar.
2. High speed, hot temperature, highway → high-energy electronic or synthwave.
3. Medium speed, warm temperature, autumn road → soft ambient acoustic music, piano, strings.
4. High speed, warm temperature, highway with truck → high-energy electronic rock.
5. Medium speed, cold temperature, snowy mountain road → soft ambient acoustic music with light electronic textures.

These examples show the intended semantic mapping, but they are not a controlled evaluation. No audio-level measurements, listener ratings, or driver outcomes are reported for these examples.

---

### Evaluation strength and limitations

#### What is supported

**Author-supported:**

- Existing models can be chained into a context-conditioned in-vehicle media pipeline.
- Model choices provide plausible latency/quality trade-offs.
- The system can generate scene descriptions, musical descriptions, audio, cover art, titles, and ambient-light colors.
- The component-level metrics indicate technically feasible operation.

#### What is not demonstrated

The paper does not report:

- A dataset or training corpus.
- Dataset size, provenance, licensing, or demographic/geographic coverage.
- A complete end-to-end benchmark.
- A baseline such as recommendation, retrieval, remixing, or fixed prompt generation.
- Ablations for image context, speed, temperature, or prompt stages.
- Human listening-study protocol, sample size, statistical tests, or ratings.
- Driver workload, distraction, attention, comfort, affect, or safety measurements.
- Whether speed actually changes musical tempo/energy reliably.
- Whether generated music remains coherent across context changes.
- Objective or human validation of “smooth transitions.”
- Error analysis for hallucinated scene descriptions or inappropriate music.

The conclusion says “limited user studies” found positive reception (§4, p. 4), but provides no participant count, procedure, measures, or numerical results. This is insufficient to evaluate the claim.

---

### Safety, control, and ethics

#### Reported safeguards

The safety stack is one of the more concrete parts of the paper:

- Technical audio checks.
- Offensive-image screening.
- Disallowed-language filtering.
- Regeneration after failed checks.

However, thresholds, classifier names, calibration procedures, retry limits, and fallback behavior are unspecified.

#### Important unaddressed risks

No dedicated ethics or safety section addresses:

- Cloud transmission of camera imagery and telemetry.
- Consent, retention, access control, or data minimization.
- Internet loss or cloud-service failure while driving.
- Driver distraction caused by overly energetic music or frequent transitions.
- Emergency-priority audio ducking or override.
- Bias in scene interpretation or cultural assumptions about “appropriate” music.
- Copyright and training-data provenance.
- Manipulative personalization or mood steering.
- User ability to reject, edit, or disable context adaptation.
- Safety of ambient-light changes during driving.

**Interpretation:** The system’s safety checks mainly screen generated artifacts. They do not establish that the adaptive behavior itself is safe for driving.

---

### Artifact and reproducibility status

The paper provides:

- Model names and approximate hardware.
- Component-selection tables.
- Prompts in Appendix B.
- Five qualitative examples.

It does **not** provide or identify:

- Source code.
- Model weights or fine-tuning checkpoints.
- A dataset.
- Evaluation scripts.
- Generated audio files or a reproducible audio benchmark.
- A public repository or supplementary artifact.
- Full prompt templates beyond the short appendix prompts.
- Safety thresholds or implementation details.

Artifact status is therefore **partial and non-reproducible at system level**. The prompt-level pipeline can be conceptually reconstructed, but exact outputs and evaluations cannot be reproduced from the paper alone.

---

### Relevance to affect- and context-conditioned music

#### Strong relevance

The paper demonstrates a useful conceptual decomposition:

\[
\text{scene/telemetry}
\rightarrow
\text{interpretable semantic description}
\rightarrow
\text{musical attributes}
\rightarrow
\text{generated audio}
\]

It is relevant to affective music research because the intermediate descriptions explicitly use terms such as:

- upbeat,
- calm,
- serene,
- lively,
- relaxed,
- high-energy,
- reflective,
- tranquil.

It is also relevant to context-aware composition because speed, temperature, weather, road type, vegetation, and urban/rural scene semantics influence the musical prompt.

#### Crucial distinction

The system does **not** measure driver affect. Its “affect” is inferred from environmental context through an LLM’s language prior. There is no validated mapping from context to valence/arousal, and no evidence that the generated music changes driver affect or behavior beneficially.

#### Relevance to explainable controllable composition

The textual intermediate representation offers:

- Inspectable context-to-music reasoning.
- Editable descriptors.
- A possible audit trail.
- Natural-language counterfactuals, such as changing “high speed” to “low speed.”

But it falls short of explainable composition because:

- The mapping is not formalized.
- Descriptors are not structured or normalized.
- No provenance links each musical attribute to a specific sensor or visual cue.
- The audio model’s internal realization is opaque.
- No symbolic score, section plan, or note-level control is exposed.
- No faithfulness test shows that changing one context signal changes only the intended musical property.

---

### Concrete research ideas

1. **Build a synchronized benchmark**
   - Pair dashcam clips, speed, acceleration, weather, route context, generated/reference music, valence/arousal labels, musical descriptors, and driver ratings.
   - Include controlled counterfactual pairs where only speed, weather, or scene changes.

2. **Replace free-form descriptions with a typed music-control schema**
   - Use validated fields such as tempo range, energy, valence, mode, instrumentation, rhythmic density, texture, loudness, and transition policy.
   - Preserve natural-language explanations alongside machine-readable controls.

3. **Test causal context faithfulness**
   - Hold the image fixed while varying speed.
   - Hold telemetry fixed while changing weather or scene.
   - Measure whether only the intended musical dimensions change using audio embeddings, tempo, energy, and listening tests.

4. **Add explainable provenance**
   - Store mappings such as `high speed → high energy/rhythmic density`.
   - Provide user-facing explanations: “High speed and multilane highway contributed to electronic, driving rhythms.”
   - Evaluate explanation faithfulness against actual generated audio.

5. **Develop safe adaptive transitions**
   - Generate overlapping 90-second segments.
   - Use crossfades or continuation models with bounded loudness and tempo changes.
   - Add emergency ducking, offline fallback, cached safe tracks, and explicit retry/time limits.

6. **Evaluate human factors in real or high-fidelity driving studies**
   - Measure workload, distraction, perceived control, affect, comfort, route confidence, and driving variability.
   - Compare generated music with retrieval, fixed playlists, and context-aware recommendation.

7. **Address privacy and deployment**
   - Perform on-device scene extraction where possible.
   - Send only structured context rather than raw camera frames.
   - Define retention, consent, encryption, and failure policies.

8. **Improve reproducibility**
   - Release prompts, schemas, benchmark contexts, anonymized audio, evaluation scripts, safety thresholds, and latency traces.
   - Report confidence intervals and failure cases, not only averages over approximately ten samples.

**Overall assessment:** Drive-to-Music is a useful prototype blueprint for multimodal, context-conditioned audio, particularly because it exposes an intermediate musical-description layer. Its main research value is architectural and methodological. Its claims about real-time operation, personalization, well-being, smooth transitions, and driving benefit remain largely unvalidated.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `generation-and-planning`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
