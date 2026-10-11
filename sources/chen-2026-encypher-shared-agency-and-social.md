---
title: "Encypher: Shared Agency and Social Presence in Collaborative Music Generation for Dance Cyphers"
authors: "Zhixing Chen and Cheng-Zhi Anna Huang"
year: 2026
doi: 10.48550/arXiv.2609.18062
category: interaction-and-evaluation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/chen-2026-encypher-shared-agency-and-social.pdf"
pdf_filename: chen-2026-encypher-shared-agency-and-social.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

Encypher is a collaborative, embodied music-generation system for dance cyphers. A depth camera tracks multiple dancers; movement energy and spatial organization are aggregated into weighted text prompts and generation parameters for Google DeepMind’s LyriaRT real-time neural-audio model.

## 1. Document Information

- **Canonical source:** arXiv `2609.18062v1`; official PDF preserved as `chen-2026-encypher-shared-agency-and-social.pdf`.
- **Full-paper evidence:** delegate digest `del_mv41492r_5pk3.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Encypher digest

**Paper:** Zhixing Chen and Cheng-Zhi Anna Huang, *Encypher: Shared Agency and Social Presence in Collaborative Music Generation for Dance Cyphers*, arXiv:2609.18062v1 [cs.HC], 16 September 2026.  
**Materials inspected:** the complete 17-page PDF, extracted text, figures, Table 1, Appendix A, and the linked project page. No repository files were modified.

### Executive summary

Encypher is a collaborative, embodied music-generation system for dance cyphers. A depth camera tracks multiple dancers; movement energy and spatial organization are aggregated into weighted text prompts and generation parameters for Google DeepMind’s LyriaRT real-time neural-audio model.

The paper’s central claim is that **mapping group-level behavior rather than isolated individual gestures shifts perceived agency from “I control the music” to “the room is shaping the music.”** In a study with 11 unacquainted novice participants, collaboration received 81.8% agreement and spatial awareness 90.9%. However, the evidence is descriptive and exploratory: there was no baseline, only one study session, screen/no-screen conditions were confounded, and LyriaRT is a closed changing API.

For symbolic mashups, the most transferable ideas are:

1. aggregate multiple contributors into shared musical state;
2. treat mappings as social choreography, not merely parameter control;
3. expose causal provenance from human action to musical change;
4. combine symbolic beat/harmonic control with neural-audio richness;
5. evaluate shared agency separately from individual control.

---

### Page and section audit

| Pages | Contents |
|---|---|
| 1–2 | Abstract, motivation, contributions, system overview; Figures 1–3 |
| 3–4 | Related work on social interaction, collaborative technology, movement sonification; Table 1 |
| 5–6 | Neural motion-to-music background; Methods; first-person co-design; four-mode design space; Figure 4 |
| 6–7 | Motion sensing and deployment limits; System Design; LyriaRT architecture |
| 7–8 | Embodied collaborative steering; co-design process; Figures 5–6; study setup |
| 9–10 | Figure 7 quantitative results; qualitative themes; Figure 8–10 |
| 11–12 | Figures 8–11; museum deployment |
| 12–13 | Live performance; discussion of designing with versus for communities |
| 14–15 | Symbolic versus neural audio; limitations and future work; conclusion |
| 16–17 | References and Appendix A questionnaire/debrief protocol |

---

### 1. System and interface

### Hardware and software

The system has three primary components (**§4.1, pp. 6–7; Figure 2, p. 2**):

1. **Web interface**
   - Handles LyriaRT API calls.
   - Controls music generation.
   - Displays visualization and zone state.

2. **ZED 2i stereo depth camera**
   - Tracks multiple dancers without wearable sensors.
   - Mounted at 2.2 m, angled approximately 30° downward.
   - HD720 input, 30 fps, neural depth, RTX 4090 laptop.
   - Skeleton tracking reliably detected up to 15 people, but occlusion degraded tracking when dancers stood behind each other.
   - Multi-camera Fusion improved occlusion robustness but halved throughput.
   - The authors considered one camera adequate for the six-person study, not for larger groups (**§3.3, p. 6**).

3. **Max/MSP hub**
   - Receives motion features via OSC.
   - Filters, smooths, and quantizes movement data.
   - Communicates with the web interface and lighting controls.
   - Sends control data to an ETC Eos lighting console in the live performance.

The model is **LyriaRT**, a live codec-language model that autoregressively generates audio tokens conditioned on text/audio prompts. It generates audio in approximately **two-second chunks with ten seconds of prior audio context** (**§3.2, p. 5; §4.1, p. 7**).

### Spatial interface

The interaction space contains **six stationary circular zones**, each associated with a musical element. Participants see a projected visualization of:

- zone occupancy;
- dancer avatars or positions;
- charging/energy state;
- colored zones associated with musical elements.

The floor was physically marked with Xs in later study rounds. In the museum and performance versions, colored light increasingly replaced the screen.

### Movement-to-music mapping

#### COMAmp

The primary movement feature is **Upper Body Center of Mass Amplitude (COMAmp)**:

> “COMAmp measures how much a participant’s upper-body center of mass oscillates over a rolling two-second window.”

It is computed as the L2 norm of the standard deviations of torso X/Y world positions, producing a **0–5 scalar**, then smoothed with an exponential moving average of **α = 0.3** (**§4.2, p. 7**).

The authors chose torso sway and rocking rather than limb velocity because breakers found sharp-limb mappings unnatural and because COMAmp supports broader Hip-Hop movement vocabularies.

#### Prompt weighting

Each dancer’s COMAmp controls the weight of a text prompt representing that dancer’s assigned musical element. The weights are summed across participants:

> “the aggregate energy of the group shapes the generation in real time.”

Thus, participants do not independently control separate musical tracks in a precise sense. Their activity contributes to a shared prompt-conditioning signal.

#### Circularity, temperature, and top-K

The system counts how many of the six zones are occupied. This group-circularity measure controls LyriaRT’s temperature and top-K:

- tighter group formation → more coherent and predictable output;
- scattered formation → more randomness and variation.

The authors explicitly describe this as a feedback loop: coherent music encourages dancers to remain together, and proximity makes the music more coherent (**§4.2, pp. 7–8**).

#### Failed mappings

The authors initially tested:

- arm velocity → top-K;
- leg velocity → temperature;
- individual musical controls.

These did not produce reliable or expressive changes. Combining them created unpredictable variation that dancers described as chaotic. This led to the deliberate shift from individual control toward collective spatial organization (**§4.3, p. 8**).

BPM control was also attempted but unreliable: some genre/instrument combinations did not follow tempo constraints.

---

### 2. Co-design and interaction protocol

### Five-week co-design

The authors used autobiographical and first-person co-design methods, grounded in the first author’s dance practice and weekly sessions with the Imobilare breaking crew (**§3.1, p. 5; §4.3, pp. 7–8**).

Key design changes emerged from these sessions:

- discrete dancer-to-instrument assignments caused confusion;
- six stationary zones made participation and turn-taking more legible;
- limb-velocity control was replaced by COMAmp;
- high-dimensional parameter control was replaced by collective circularity;
- arbitrary genre combinations were replaced by curated JSON presets with compatible instrument stacks;
- latency was reframed as a “charging” mechanic: dancers build energy before music responds.

The co-design also revealed a population distinction. Established breakers already had strong social practices and expected reliable downbeats. The authors therefore shifted the formal study toward strangers and novices, for whom Encypher might function as a social bridge.

### Novice user study

**Participants:** 11 adults from an MIT introductory movement class, with minimal dance experience and no pre-existing social ties (**§5.1, p. 8**).

**Groups:**

- Group A: n=6
- Group B: n=5

**Protocol:**

1. normal class warmup;
2. groups alternated dancing inside the cypher;
3. each round lasted approximately 5–10 minutes;
4. the group that had just danced completed a paper questionnaire;
5. Group A danced an additional round;
6. a 20-minute facilitated group discussion followed.

The questionnaire used 7-point Likert items for:

- engagement;
- control;
- enjoyment;
- replay;
- social presence;
- collaboration;
- invitation;
- encouragement;
- spatial awareness.

Open-ended questions addressed body engagement, connection, spatial markers, agency, hesitation, and other observations. Researchers also tracked spot occupancy, eye contact, approach/retreat, laughter/smiling, and musical-shift timestamps (**Appendix A, pp. 16–17**).

---

### 3. Evaluation and results

### Quantitative findings

Figure 7 is a **descriptive diverging stacked bar chart**, not an inferential statistical analysis (**§5.4, pp. 9–10**).

Reported agreement rates:

| Dimension | Agreement |
|---|---:|
| Engagement | 54.5% |
| Control | 63.6% |
| Enjoyment | 72.7% |
| Replay | 63.6% |
| Social presence | 54.6% |
| Collaboration | 81.8% |
| Invitation | 63.6% |
| Encouragement | 72.7% |
| Spatial awareness | 90.9% |

Additional reported details:

- No participant disagreed on engagement or enjoyment.
- Engagement had the largest neutral share: 45.5%.
- Spatial awareness had the strongest result: 90.9% agreement and 36.4% strongly agree.
- Collaboration had 81.8% agreement and 18.2% strongly agree.
- Social presence was variable: 18.2% disagreed, including 9.1% strongly disagreeing; 27.3% were neutral or mixed.
- Control had 63.6% agreement, but no strongly-agree responses and 27.3% disagreement.

#### Interpretation

**Author claim:** Encypher shifted agency toward collective orchestration, while preserving only moderate individual control.

**My interpretation:** The data support a perceived group-level experience, but they do not establish that generative music caused it. Because there was no baseline or control condition, the effect could reflect the cypher format, shared music, novelty, the class context, or the social structure of dancing together.

### Qualitative themes

#### 1. Emergent non-verbal alignment

Participants reported mirroring movement, matching energy, and responding to visual cues:

> “The guy across from me rocked invitingly and I tried to match his movements and energy.” — P5

> “When I looked and saw others swinging, I swang [along with them].” — P8

#### 2. Shared agency as collective orchestration

Participants described the music as responding to the room rather than to a single person:

> “It felt like the music was responding to the group. When the energy was good, it felt like the music was better.” — P1

> “I feel like everyone plays a role in creating the music.” — P11

#### 3. Spatial markers as clarity and constraint

The Xs helped participants understand where to stand and what role they occupied, but some felt restricted:

> “Having marked spots kept people in more structured locations... it gave me clarity on where I could go.” — P1

> “I like moving around the space, and the need to stay on the X was quite limiting for me.” — P9

The paper also reports “social territoriality”: participants felt that people “owned” the spots they had charged.

#### 4. Screen as social mediator

The screen had a double effect:

- it offered a shared object of attention that reduced the awkwardness of approaching strangers;
- it diverted attention away from direct eye contact and interpersonal awareness.

When the screen was removed, participants initially became uncertain and drifted apart. Floor tape restored spatial legibility.

#### 5. Embodied locus of engagement

Body-map responses most frequently identified the torso, hips, and feet, consistent with the intended groove vocabulary. The authors note that hips and feet are not directly measured by COMAmp (**§5.5, p. 10; Figure 10, p. 11**).

---

### 4. Public deployments

### Museum event

The 65-minute MIT Museum event used:

- a 7 m circular installation;
- approximately 25 rotating attendees;
- groups of 5–6;
- the same camera and LyriaRT pipeline;
- a screen plus colored ceiling light.

Participants initially hesitated, but once one or two entered, others followed within approximately a minute. When the screen was disconnected, ceiling lighting preserved spatial and energetic legibility without pulling attention toward a separate display (**§6, pp. 11–12; Figure 11**).

Six participants later volunteered to demonstrate the system to an approximately 80-person event audience.

These observations support ecological feasibility, but they were not measured with questionnaires or controlled comparisons.

### Live performance

The screen-free performance took place at the MIT Music Technology Research Showcase in Tull Concert Hall on 13 May 2026, before approximately 300 people (**§7, pp. 12–13; Figure 1**).

Setup:

- six dancers;
- six zones;
- one-hour rehearsal focused on blocking rather than choreography;
- staggered entries;
- each zone assigned a compatible musical element;
- COMAmp sent via OSC/Ethernet to an ETC Eos lighting console;
- each dancer’s energy controlled the brightness of the light pool under them.

The authors observed that lighting made each dancer’s contribution legible on the body itself and restored mutual attention that the screen had displaced.

Important limitation: no audience or participant feedback was collected. The performance findings are only the first author’s observations.

---

### 5. Figures and table

- **Figure 1, p. 1:** screen-free performance with colored pools of light.
- **Figure 2, p. 2:** camera → motion features → Max/MSP → LyriaRT and lighting pipeline.
- **Figure 3, p. 2:** museum installation.
- **Table 1, p. 4:** evaluation framework: social presence, group cohesion, interaction style, interaction quality, facilitation, invitation, and encouragement.
- **Figure 4, p. 6:** classification of motion-to-music systems as structural, reactive, semantic, or textural.
- **Figure 5, p. 8:** participant warmup.
- **Figure 6, p. 8:** post-session discussion.
- **Figure 7, p. 9:** Likert-response distribution for the nine dimensions.
- **Figures 8–9, pp. 10–11:** study rounds with and without the visualization screen.
- **Figure 10, p. 11:** aggregated body-map responses.
- **Figure 11, p. 12:** strangers using Encypher at the museum.

No figure reports objective musical-quality metrics, latency measurements during the study, effect sizes, inferential tests, or model-comparison results.

---

### 6. Author claims versus interpretation

### Author claims

The authors claim that:

1. collective energy and spatial circularity shifted perceived agency from individual to group;
2. Encypher acted as a social bridge for strangers;
3. established dance communities sometimes resisted the system’s framing;
4. the screen both facilitated entry and reduced direct interpersonal attention;
5. ambient lighting progressively resolved this screen-related tension;
6. mapping design should be treated as social design.

### My interpretation

- “Shared agency” is primarily a **subjective and interactional construct** here, not an objectively measured allocation of causal control.
- The strongest contribution is not a new generation model; it is the design argument that **feature selection and aggregation encode social norms**.
- The screen/light findings are promising but not causal because screen removal, group order, and floor markings were confounded.
- The system is closer to **semantic/textural collective steering** than to reactive instrumental control.
- The paper does not evaluate explainability directly. Its observable intermediate states—energy, occupancy, circularity, prompt weights, temperature, top-K—create a strong basis for explainable interfaces, but explanation quality was not tested.

---

### 7. Artifact status and reproducibility

The paper links `https://encypher-chi.github.io/`. The project page provides:

- the paper abstract;
- photographs;
- an edited, privacy-blurred performance video;
- timestamped chapters describing the performance.

I found no linked source repository, dataset, motion traces, prompt logs, audio outputs, preset files, or analysis code in the paper or project page.

Reproducibility is limited because:

- LyriaRT is a closed API;
- its behavior may change;
- the authors did not evaluate the open-weight MagentaRT alternative;
- the precise threshold for the “charging” mechanic is not reported;
- the full preset configurations are not included;
- the source motion/video data are not released.

The artifact is therefore best classified as a **deployed research demonstrator with public documentation/video**, not a reproducible software artifact.

---

### 8. Relevance to symbolic mashups and explainable co-creation

### Directly transferable ideas

#### Group-level agency

For a symbolic mashup, avoid assigning each user a single isolated parameter. Instead aggregate:

- per-user activity;
- section or stem occupancy;
- proximity or grouping;
- synchrony;
- collective energy.

These can control arrangement-level decisions such as:

- which source enters;
- stem density;
- transition timing;
- accompaniment complexity;
- texture versus silence;
- shared versus individual musical roles.

#### Preset compatibility

Encypher’s compatible JSON presets suggest a useful mashup mechanism: maintain validated combinations of stems, keys, tempos, rhythmic densities, and transition types rather than exposing every parameter.

#### Explainable interaction

An explainable symbolic mashup interface could log and display:

```text
Participant A: high torso energy
Participant B: low energy
Group circularity: 5/6 zones
Result: increase bass + percussion weights
Transition: source B enters at next phrase boundary
Reason: collective energy threshold crossed
```

This would expose the causal chain:

**movement → extracted feature → aggregate state → symbolic decision → audible result**

Encypher already has the intermediate variables needed for this kind of provenance, but does not surface them as explanations or test whether users understand them.

### Important differences from symbolic mashups

Neural audio gives Encypher timbral richness but loses:

- exact note-level control;
- reliable meter and downbeat alignment;
- deterministic repetition;
- explicit harmonic compatibility;
- easy source attribution.

For mashups, a hybrid architecture is likely stronger:

- symbolic engine for beat grid, phrase boundaries, harmonic legality, and source/stem identity;
- neural audio or learned texture model for fills, transitions, timbral variation, and expressive surface detail.

---

### 9. Concrete research ideas

1. **Collective symbolic mashup controller**  
   Compare individual control, averaged group control, summed group control, and consensus-based control for the same mashup task. Measure perceived shared agency, individual agency, musical coherence, and turn-taking.

2. **Live provenance/explanation interface**  
   Show current motion features, group aggregate, selected stems, prompt/weight changes, and the counterfactual result if one participant’s input were removed. Test explanation fidelity and user trust.

3. **Controlled screen versus ambient-light study**  
   Counterbalance screen, floor markers, ceiling light, and no-feedback conditions. Measure gaze, eye contact, approach/retreat, turn-taking, social-presence ratings, and group cohesion.

4. **Synchrony as a musical control signal**  
   Compare beat-level phase coherence, torso-sway correlation, and foot-timing synchrony. Test whether rewarding synchrony increases social bonding or undesirably suppresses individual expression.

5. **Beat-conditioned neural/symbolic hybrid**  
   Use a symbolic beat scaffold to guarantee downbeat alignment while a neural model generates texture. Compare against pure LyriaRT-like generation on danceability, controllability, and perceived agency.

6. **Expert-versus-novice cultural transfer**  
   Re-design movement features with breaking, waacking, locking, contemporary dance, and non-dance participants. Measure whether the system supports the intended community or turns movement into instrumental control.

7. **Baseline study**  
   Compare Encypher-like collective generation with a fixed playlist, live DJ, symbolic mashup system, and unresponsive music. This is necessary to attribute shared-agency effects specifically to generative adaptation.

8. **Reproducible artifact package**  
   Release anonymized motion traces, feature extraction code, presets, prompt logs, transition decisions, and a deterministic symbolic backend. This would preserve the social-design contribution even if the original neural API changes.

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
