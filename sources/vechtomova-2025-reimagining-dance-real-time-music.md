---
title: "Reimagining Dance: Real-time Music Co-creation between Dancers and AI"
authors: "Olga Vechtomova and Jeff Bos"
year: 2025
doi: 10.48550/arXiv.2506.12008
category: interaction-and-evaluation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/vechtomova-2025-reimagining-dance-real-time-music.pdf"
pdf_filename: vechtomova-2025-reimagining-dance-real-time-music.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

I reviewed all five PDF pages, the extracted text, Figures 1–3, and the linked supplementary plots referenced in the paper’s footnote.

## 1. Document Information

- **Canonical source:** arXiv `2506.12008v1`; official PDF preserved as `vechtomova-2025-reimagining-dance-real-time-music.pdf`.
- **Full-paper evidence:** delegate digest `del_mv40f079_dc50.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### Bibliography and version

**Olga Vechtomova and Jeff Bos**, “**Reimagining Dance: Real-time Music Co-creation between Dancers and AI**,” arXiv:**2506.12008v1** [cs.SD], **13 June 2025**. Affiliations: University of Waterloo and WordSynth Inc. The supplied PDF is five pages. A linked presentation identifies the work with **ICCC 2025**, but the supplied manuscript is the arXiv v1 version.

I reviewed all five PDF pages, the extracted text, Figures 1–3, and the linked supplementary plots referenced in the paper’s footnote.

---

### Page and section map

| Page | Main content |
|---|---|
| **p. 1** | Abstract; Introduction; Figure 1 system diagram; Related Work |
| **p. 2** | Related Work; Theoretical Foundations; System Architecture; audio and movement representation; Figure 2 |
| **p. 3** | Cross-Modal Generation; Retrieval Module; Real-time Inference; Dataset; Figure 3; Pilot Study |
| **p. 4** | Pilot Study; feature extraction; statistical methods; quantitative results; qualitative results; Conclusion |
| **p. 5** | Conclusion continuation; References |

The paper has headings but no numbered sections.

---

### Core contribution

#### Author claim

The authors invert the usual dance–music relationship. Instead of music driving choreography, the dancer’s movement conditions the next musical clip. The dancer is therefore both performer and musical co-creator.

The system does not synthesize waveform audio directly. It predicts an audio latent representation and retrieves an existing clip from a library, producing a real-time collage through cross-fading.

#### Interpretation

This is best understood as **stateful, retrieval-based mixed-initiative co-creation**, not autonomous music generation. The AI contributes selection and sequencing; the dancer contributes embodied control; the original recordings provide the musical material.

---

### Architecture and interaction loop

**Figure 1, p. 1; “System Architecture,” p. 2; “Real-time Inference,” p. 3**

1. **Movement capture**
   - Webcam input.
   - TensorFlow **MoveNet Thunder** extracts five landmarks:
     - head
     - left wrist
     - right wrist
     - left ankle
     - right ankle

2. **Movement encoding**
   - Each 3.5-second motion sequence becomes a color-coded trajectory image.
   - Input size: **256 × 256 × 3**.
   - A movement VAE maps it to a **128-dimensional latent vector**.

3. **Audio encoding**
   - Audio is represented as spectrograms of 3.5-second clips.
   - Audio VAE input: **224 × 224 × 1**.
   - Five convolutional encoder layers with ReLU; decoder uses transposed convolutions.
   - Audio latent dimension: **128**.

4. **Cross-modal generation**
   - Inputs:
     - current movement latent
     - previous audio clip latent
   - A GAN generator predicts the latent vector for the next audio clip.
   - The authors tested concatenation, multiplication, gated layers, FiLM, and cross-attention.
   - They report that **pointwise addition** worked best.
   - This is followed by a multilayer network with **256-unit hidden dimensions**, LayerNorm, and LeakyReLU.

5. **Clip retrieval**
   - The predicted latent is compared with encoded library clips using **cosine similarity**.
   - The highest-similarity clip is selected.
   - Direct decoding is avoided because the authors report that it produced lower audio quality.

6. **Playback**
   - The selected clip is cross-faded with the current audio.
   - The previous/current audio state is fed back into the generator.
   - The selected audio becomes the next state.

7. **Human curation**
   - The dancer can curate the source library, thereby controlling the available sonic palette and style.

#### Important architectural implication

The system is effectively a one-step recurrent process:

\[
\text{next clip} =
\operatorname{argmax}_{c \in \mathcal{L}}
\operatorname{cosine}
\left(
G(z_\text{movement}, z_\text{previous audio}), z_c
\right)
\]

The paper does not specify whether the retrieval library is identical to the 50K audio-VAE training set.

---

### Dataset and clip library

**“Dataset,” p. 3**

#### Training data

- **18,000 aligned 3.5-second video–audio recordings**
  - 17,000 from the **AIST Dance Video Database**
  - 1,000 from the authors’ own recordings or material supplied by professional dance collaborators
- Audio VAE:
  - **50,000 audio clips**
  - Authors’ studio recordings
  - Multiple genres, tempos, and instrumentation

#### Pilot data

- Three participants:
  - **P1:** more than 10 years of ballet
  - **P2:** 2–3 years of ballet/jazz
  - **P3:** no formal dance training
- Each performed improvisational movement for up to 30 minutes.
- More than **70 minutes** of video and system-generated audio were collected.

#### Library semantics

The clips are pre-recorded audio fragments rather than symbolic musical units. The paper does not report:

- exact library size used at inference;
- clip overlap or segmentation stride;
- tempo/key/chord metadata;
- genre labels;
- duplicate handling;
- licensing or release status.

---

### Figure 3 examples

**“Cross-Modal Generation,” p. 3; Figure 3**

The four panels show previous audio, movement, predicted audio, and top retrieved match.

The authors use two controlled comparisons:

- With identical previous audio but different movements:
  - minimal movement leads to an ambient result;
  - energetic break-dancing leads to a rhythmic result.
- With movement held constant but previous audio changed:
  - the predicted clip also changes.

#### Interpretation

The figure demonstrates sensitivity to both modalities, but it is a qualitative visualization rather than a controlled quantitative ablation. It does not establish how often the retrieved clip agrees with a human judgment of musical appropriateness.

---

### Motion/audio feature analysis

**“Video and Audio Features” and “Statistical Analysis,” pp. 3–4**

#### Motion features

Performances were segmented into **10-second clips**. MoveNet landmarks were normalized to **[-1, 1]**.

Movement energy was computed from Euclidean displacement between corresponding landmark positions in consecutive frames. The authors calculated:

- mean energy;
- minimum energy;
- maximum energy;
- standard deviation of energy.

#### Audio features

They extracted **47 audio features** using Librosa and Essentia, including:

- MFCCs;
- spectral contrast;
- spectral flux;
- chroma;
- psychoacoustic measures.

The paper highlights:

- `mfcc_1`, interpreted as related to overall spectral shape/timbre;
- `mfcc_7`;
- `spec_contrast_6`;
- spectral flux.

#### Statistical methods

The authors applied:

- Pearson correlation;
- separate PCA for movement and audio features;
- CCA;
- PLS regression in both directions;
- Random Forest regression and feature importance;
- coefficient of determination, \(R^2\), for predictive models.

---

### Exact reported results

#### Pearson correlation

- Minimum movement energy had the strongest and most consistent associations.
- `mfcc_1` correlated negatively with minimum movement energy:

\[
r = -0.45,\quad p < 0.001
\]

- `spec_contrast_6` and `mfcc_7` showed positive correlations with minimum movement energy.

The authors interpret lower minimum movement energy as associated with smoother spectral shapes.

#### PCA

The paper reports that:

- movement-energy measures loaded strongly on the first few components;
- audio variance was dominated by MFCC and spectral features.

The linked supplementary plot labels the first two video components as **0.66** and **0.28**.

#### CCA

The paper reports moderate canonical correlations. The first canonical pair linked high movement-energy standard deviation with spectral complexity and dissonance.

The linked supplementary plot gives the first canonical correlation as:

\[
r = 0.619
\]

#### PLS regression

Audio features predicted movement energy only modestly:

- best audio-to-motion result: **\(R^2 = 0.103\)** for minimum movement energy.

Motion features predicted some audio properties more strongly:

- predicting `mfcc_1`: **\(R^2 = 0.202\)**
- predicting `mfcc_7`: **\(R^2 = 0.162\)**

#### Random Forest feature importance

The features repeatedly identified as important predictors of movement-energy statistics were:

- `mfcc_1`
- `mfcc_7`
- `spec_contrast_6`
- spectral flux

#### Causal caution

These correlations are measured on **system-generated audio**, which is produced from movement. Therefore, they demonstrate coupling in the implemented system, but they do not independently establish a natural or causal dance-to-music relationship.

---

### Qualitative evaluation

**“Qualitative results,” p. 4**

The authors report that dancers experienced:

- a fluid exchange of initiative;
- system influence on movement choices;
- exploration of new movements to elicit different musical responses;
- deliberate attempts to redirect the musical atmosphere, such as energetic movement during ambient passages.

The system generally required **5–10 seconds** to adapt to substantial changes in dance energy. The authors intentionally designed this delay to preserve musical continuity and suggest that it could be customized by genre.

During fatigue, reduced movement intensity naturally caused transitions from rhythmic music toward ambient soundscapes. The authors propose exercise and training as an additional application.

---

### Limitations and reproducibility

These are either explicit in the paper or omissions visible in the supplied manuscript.

#### Explicit or acknowledged limitations

- The study is a **pilot with only three participants**.
- The authors describe it as establishing technical foundations.
- A larger study with a professional dance company is planned.
- The 5–10-second adaptation delay limits immediate responsiveness, although the authors frame it as musically intentional.

#### Reproducibility gaps

The paper does not provide:

- train/validation/test splits;
- participant-level or dancer-independent evaluation;
- optimizer, learning rate, loss functions, epochs, or batch sizes;
- GAN discriminator architecture;
- pose-estimation frame rate;
- audio sample rate or spectrogram parameters;
- clip overlap/stride;
- cross-fade duration;
- inference latency or hardware;
- reference-library composition;
- raw data or trained models;
- exact sample counts for the 10-second pilot windows;
- confidence intervals or multiple-comparison correction;
- baseline systems or ablations;
- formal participant questionnaires or audience evaluation.

The linked supplementary material provides plots and presentation material, including the \(r=0.619\) CCA result, but not a complete reproducible implementation package.

---

### Relevance to responsive symbolic mashup

#### Directly reusable design patterns

1. **Latent retrieval instead of unconstrained generation**
   - For symbolic mashup, retrieve bar-aligned MIDI or MusicXML phrases rather than decoding arbitrary notes.

2. **Previous musical state as context**
   - The previous clip conditions the next selection, supporting continuity and controlled evolution.

3. **Human-curated source library**
   - A performer or composer can constrain the system to approved motifs, stems, harmonic regions, or stylistic palettes.

4. **Cross-fading as a simple continuity mechanism**
   - In symbolic music, this could become beat-synchronous switching, overlap-add, reharmonization, or voice-leading-aware transition.

5. **Movement as an interpretable control channel**
   - Energy, stillness, trajectory spread, and limb-specific motion can control density, instrumentation, register, rhythmic activity, or harmonic tension.

#### Major difference

The paper operates on audio spectrograms and does not explicitly represent:

- notes;
- beats or bars;
- tempo;
- key;
- chord progression;
- voice leading;
- phrase boundaries;
- symbolic provenance.

For symbolic mashup, these constraints are essential.

---

### Concrete research ideas

1. **Symbolic version of the architecture**
   - Encode bar-aligned MIDI phrases.
   - Predict the next phrase embedding from dancer motion plus recent musical context.
   - Retrieve candidates subject to tempo, key, chord, and phrase-boundary constraints.

2. **Explainable retrieval**
   - Log movement features, previous-clip features, candidate cosine scores, harmonic compatibility, and the reason a clip won.
   - Provide counterfactuals: “more stillness would have selected ambient clip B.”

3. **Richer musical state**
   - Replace only the previous clip with a context window containing recent clips, beat phase, tempo, key, harmonic tension, density, and novelty.

4. **Controlled causal evaluation**
   - Use scripted motion conditions—stillness, acceleration, arm extension, torso rotation—and randomize the available library.
   - Compare movement-only, previous-audio-only, and combined models.

5. **Adaptive latency**
   - Learn a responsiveness/coherence trade-off instead of fixing the 5–10-second adaptation window.
   - Use rapid transitions for improvisation and slower transitions for phrase-level composition.

6. **Human-AI co-authorship study**
   - Measure perceived agency, responsiveness, surprise, coherence, trust, and willingness to reuse the resulting material.
   - Include trained dancers, musicians, and non-experts.

7. **Provenance-preserving mashup**
   - Track the original composer, source clip, transformations, and selection rationale.
   - Treat the output as an auditable real-time collage rather than opaque generation.

**Bottom line:** the paper’s strongest contribution is its interaction design—movement and prior music jointly drive retrieval from a curated library. Its statistical evidence is promising but exploratory, and its approach requires substantial symbolic, structural, and evaluation extensions before it can support rigorous responsive mashup research.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `interaction-and-evaluation`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
