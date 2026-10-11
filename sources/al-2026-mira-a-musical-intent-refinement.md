---
title: "MIRA: A Musical Intent Refinement Agent for Aligning Text-to-Music Generation with User Intent"
authors: "Zhilin Wang et al."
year: 2026
doi: 10.48550/arXiv.2610.10355
category: interaction-and-evaluation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/al-2026-mira-a-musical-intent-refinement.pdf"
pdf_filename: al-2026-mira-a-musical-intent-refinement.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

Affiliations: Shandong University; University of Science and Technology of China; Central Conservatory of Music; Kunlun Tech Co. Ltd.; Shanghai Jiao Tong University.

## 1. Document Information

- **Canonical source:** arXiv `2610.10355v1`; official PDF preserved as `al-2026-mira-a-musical-intent-refinement.pdf`.
- **Full-paper evidence:** delegate digest `del_mv3zfqmo_id6g.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Detailed digest

### 1. Bibliography and version

**Zhilin Wang, Xuzheng He, Yu Cheng, Yang Yang, and Zekai Liu.**  
**“MIRA: A Musical Intent Refinement Agent for Aligning Text-to-Music Generation with User Intent.”**  
arXiv: **2610.10355v1 [cs.SD]**, **7 October 2026**, 26 pages.  
Project page: <https://mirareview.github.io/>

Affiliations: Shandong University; University of Science and Technology of China; Central Conservatory of Music; Kunlun Tech Co. Ltd.; Shanghai Jiao Tong University.

This digest covers the complete PDF, including the main text, references, Tables 1–8, Figures 1–4, prompt templates, and ethical appendix. The supplied extraction is also available at `/tmp/paper-digest/2610.10355v1.txt`.

---

### 2. Paper thesis

#### Authors’ claim

The paper argues that text-to-music evaluation should not rely primarily on global text–audio similarity or holistic quality scores. A request may contain:

- explicit requirements;
- implicit requirements inferred from an artist, song, scene, or use case;
- multiple musical dimensions that can independently succeed or fail.

The authors formulate alignment as satisfaction of a **request-specific rubric**, introduce the **MuRA-Bench** benchmark, and propose **MIRA**, a test-time agent that searches over prompt revisions using generated-audio verification.

#### My interpretation

The central contribution is not a new music generator. It is an **external control-and-evaluation loop**:

> natural-language request → structured intent specification → generation → requirement-level verification → prompt revision/search → selected output.

This is potentially important for explainable systems because the optimization target is decomposed into auditable requirements rather than hidden inside one scalar reward.

---

### 3. MuRA-Bench

### 3.1 Dataset composition

**Anchor:** §3.1, Appendix A.1, PDF pp. 3 and 15; extracted text approximately lines 157–186 and 872–901.

MuRA-Bench contains:

- **100 controlled requests**;
- derived from anonymized intent seeds collected on the **Mureka** platform;
- **68 instrumental** and **32 vocal** requests;
- **1,566 rubric items**:
  - 996 base items;
  - 570 completion items;
- 6–31 items per request;
- mean: **15.66** items;
- median: **14.5** items.

The benchmark includes:

- partially specified requests;
- reference-based requests;
- hybrid requests;
- requests with multiple simultaneous constraints.

Raw user logs are not released. The paper states that the curated benchmark was released with platform permission, but the PDF does not provide the actual dataset contents or release mechanism beyond the project-page reference.

### 3.2 Rubric structure

For a request \(x\), the gold rubric is:

\[
R(x)=B(x)\cup C(x)
\]

where:

- \(B(x)\): requirements directly supported by the prompt;
- \(C(x)\): musical traits completed from references, use cases, and context.

The seven dimensions are:

| Dimension | Items |
|---|---:|
| Style | 135 |
| Instrumentation/vocal | 303 |
| Mood | 218 |
| Rhythm | 257 |
| Harmony/melody | 114 |
| Structure/energy | 199 |
| Production/texture | 340 |
| **Total** | **1,566** |

The dimensions are organizational categories, not a fixed checklist. Requests may contain only a subset.

### 3.3 Annotation and expert revision

An instruction-following LLM first drafts:

- base requirements;
- completion requirements;
- dimension assignments.

Three music experts independently revise disjoint subsets using shared guidelines. They check:

1. Explicit constraints, including omitted negative constraints.
2. Whether interpretation is actually needed.
3. Contextual support for completion items.
4. Atomicity and audibility.
5. Dimension assignment.
6. Usability and whether completion is appropriate.

Named artists, songs, and albums are converted into generalized musical traits rather than direct imitation targets.

#### Important methodological limitation

Because experts worked on **disjoint subsets**, the paper does not report inter-rater reliability for rubric construction. The rubric is therefore expert-curated, but not necessarily a consensus ground truth.

### 3.4 Example rubric

**Anchor:** Appendix A.3, PDF p. 15.

Prompt: upbeat combat music for a 2D RPG in an open plains biome, with flutes, wind textures, and African drums.

Base items include:

- upbeat combat music;
- open-plains atmosphere;
- flute parts;
- wind textures;
- African drum rhythms;
- energizing battle-ready mood.

Completion items include:

- open-air spaciousness;
- buoyant loopable battle structure;
- flute–drum call and response;
- no long cinematic introduction;
- bright major-key tonality;
- progressively intensifying drum patterns.

This example illustrates the paper’s distinction between “what the user explicitly said” and “what the context plausibly requires.”

---

### 4. Rubric-level evaluation

### 4.1 Automatic verifier

**Anchor:** §3.2, Appendix C, PDF pp. 3–4 and 18.

Each rubric item becomes a binary audio question:

> “Does the audio clearly satisfy this requirement?”

MusicFlamingo receives the audio and requirement and produces yes/no answer logits. The soft satisfaction score is:

\[
q_i(a)=
\frac{\exp(z_i^{yes})}
{\exp(z_i^{yes})+\exp(z_i^{no})}.
\]

The paper uses the probability rather than thresholding each item.

For a rubric subset \(S\), scoring first averages items within each audio and then averages audios equally. This prevents requests with more items from receiving disproportionate weight.

Reported metrics:

- **Overall**: all rubric items;
- **Base**: explicit requirements;
- **Completion**: inferred/completed requirements;
- **D-Macro**: equally weighted average over the seven musical dimensions.

Overall does **not** simply average Base and Completion.

### 4.2 Expert agreement study

**Anchor:** Table 1, §5, Appendix B, PDF pp. 6, 16–17.

The study used:

- 100 clips;
- 25 requests;
- 1,536 clip-item ratings;
- three experts;
- one expert rating per target;
- hidden system identities and automatic scores.

Experts used a 20-point fulfillment scale:

- 1–4: not fulfilled;
- 5–8: slightly fulfilled;
- 9–12: partially fulfilled;
- 13–16: mostly fulfilled;
- 17–20: fully fulfilled.

Normalized human score:

\[
h=(r-1)/19.
\]

#### Table 1: agreement with experts

| Evaluator | Item SRCC | Item Kendall | Item LCC | Clip SRCC | Clip Kendall | Pair accuracy |
|---|---:|---:|---:|---:|---:|---:|
| MusicFlamingo AQA | .690 | .532 | .817 | .823 | .646 | 79.59% |
| Qwen3-Omni-30B-A3B | .509 | .375 | .632 | .631 | .480 | 74.15% |
| Qwen2.5-Omni-7B | .469 | .344 | .599 | .643 | .465 | 72.79% |
| MOSS-Music-8B | .502 | .371 | .591 | .593 | .429 | 62.59% |
| AnyAudio-Judge-7B | .462 | .335 | .561 | .556 | .393 | 68.03% |
| MusicFlamingo prompting | .552 | .460 | .732 | .743 | .567 | 72.79% |
| MusicFlamingo cascade | .436 | .350 | .563 | .608 | .434 | 57.82% |
| CLAPScore | .245 | .175 | .361 | .331 | .223 | 62.59% |

#### Authors’ claim

MusicFlamingo with AQA scoring is the strongest evaluator on all six reported agreement measures and is therefore used for MIRA search and candidate selection.

#### Interpretation

This supports requirement-specific audio questioning over:

- broad CLAP similarity;
- a caption-then-text-judge pipeline;
- direct five-point prompting.

However, MusicFlamingo is both the primary search verifier and the principal evaluator. That creates a possible evaluator-selection bias, partially addressed—but not eliminated—by the MOSS-Music and Qwen3-Omni cross-evaluation.

---

### 5. MIRA algorithm

### 5.1 Overall architecture

**Anchor:** §4, Figure 2, PDF pp. 4–6; Appendix D and E, pp. 19–25.

MIRA operates outside the generator and treats it as a black box \(G\).

Each search-tree node stores:

\[
n_v=(p_v,a_v,o_v,M_v)
\]

where:

- \(p_v\): complete generation prompt;
- \(a_v\): generated audio;
- \(o_v\): rubric-level verifier observations;
- \(M_v\): branch-specific memory.

The three design principles are:

1. Externalize intent into verifiable rubrics.
2. Use tree search to balance exploration and exploitation.
3. Preserve branch-specific feedback rather than retaining only the best score.

### 5.2 Tool-grounded online rubric

Before generation, MIRA may invoke tools for:

- music-reference lookup;
- scene-to-music lookup;
- track-audio evidence.

The original request is retained as an immutable intent anchor.

Tool evidence passes a deterministic gate requiring:

- nonempty claim;
- nonempty support;
- `usable_for_prompt = true`;
- confidence ≥ **0.45**;
- no blocked copy/imitate language;
- at least one accepted evidence card.

Reference information is converted to generalized musical properties.

The online rubric is:

\[
R(x,E)=\{r_1,\ldots,r_m\}.
\]

It is fixed before search and is not the expert gold rubric. The gold rubric is used only for offline evaluation.

### 5.3 Candidate verification

For node \(v\):

\[
q_{v,i}=P_{\mathrm{MF}}(\text{yes}\mid a_v,r_i)
\]

and:

\[
s_v=\frac{1}{m}\sum_i q_{v,i}.
\]

Items with:

\[
q_{v,i}<\tau,\qquad \tau=0.60
\]

are treated as weak and may receive targeted feedback. The threshold is used for repair prioritization, not for binarizing the ranking score.

### 5.4 Search and frontier selection

At each layer, the planner proposes complete replacement prompts, not small appended repair notes.

The frontier retains:

1. the highest aggregate-score candidate;
2. a complementary candidate with the strongest average score over its lowest-scoring quarter of rubric items;
3. remaining slots filled by aggregate score.

This is intended to avoid optimizing only the mean while ignoring severe failures.

For \(B=9\), the nominal allocation is:

- 1 initial generation;
- 3 exploratory generations;
- up to 4 children from two selected parents;
- 1 final action from the strongest candidate.

For \(B=3\):

- 1 initial generation;
- 2 exploratory generations.

Budget counts generated candidates, including the initial one. It does not count:

- planner calls;
- retrieval calls;
- verifier questions;
- elapsed time.

### 5.5 Tree-structured feedback memory

For each child \(v\) and parent \(p(v)\):

\[
\Delta^{par}_{v,i}=q_{v,i}-q_{p(v),i}.
\]

MIRA also computes a contrast with other candidates at the same layer:

\[
\Delta^{cmp}_{v,i}
=
q_{v,i}
-
\frac{1}{|N_l(v)|}\sum_{u\in N_l(v)}q_{u,i}.
\]

Changes with magnitude at most:

\[
\epsilon=0.03
\]

are treated as stable. Larger positive or negative changes are recorded as improvements or regressions.

Memory records:

- passed requirements to preserve;
- unresolved requirements;
- successful repair phrases;
- persistent failures;
- parent–child improvements;
- regressions;
- sibling advantages and weaknesses;
- “preserve next” and “repair next” lists.

Memory is branch-specific and reset between requests.

### 5.6 Prompt constraints

The candidate prompt:

- must be a standalone replacement;
- must preserve the original request and locked requirements;
- must be under **110 words**;
- may not introduce unrequested artists or references;
- may not introduce new duration, BPM, key, timestamps, Hz/kHz, dB, bar counts, or exact mix numbers;
- preserves lyrics unless a small lyric change is required.

Kimi 2.6 is run with temperature **0.6** and thinking disabled.

MusicFlamingo answer-token scoring aggregates unique token IDs for variants of `yes` and `no`, including leading-space forms, then applies a log-sum-exp normalization.

---

### 6. Generators and baselines

### 6.1 Open-source refinement backends

- ACE-Step v1.5 Turbo;
- SongGeneration2 Large;
- YuE2-3B.

Each is evaluated with:

- direct generation;
- MIRA \(B=3\);
- MIRA \(B=9\).

Generation and verification use one NVIDIA A800 per backend.

### 6.2 Planning and verification

- Planner: Kimi 2.6.
- Primary verifier: MusicFlamingo.
- Cross-evaluators: MOSS-Music-8B-Instruct and Qwen3-Omni-30B-A3B.

### 6.3 Commercial direct-prompting baselines

- MiniMax music-2.6;
- MiniMax music-3.0;
- Mureka V9;
- Mureka V9.5;
- StepAudio 3 Music;
- Suno v4;
- Suno v4.5;
- Suno v5;
- Suno v5.5;
- Suno v6.

These were accessed through official APIs and evaluated with direct prompting.

---

### 7. Main results

**Anchor:** Table 2, Figure 3, PDF pp. 7–8.

All Table 2 scores are multiplied by 100. Columns are:

`Overall / D-Macro / Base / Completion / Style / I-V / Mood / Rhythm / H-M / S-E / P-T`

### 7.1 Open-source systems

| Backend | Setting | Overall | D-Macro | Base | Comp. |
|---|---|---:|---:|---:|---:|
| ACE-Step | Direct | 67.6 | 67.2 | 69.6 | 66.1 |
| ACE-Step | MIRA B=3 | 74.2 (+6.6) | 74.1 (+6.9) | 77.1 (+7.5) | 71.1 (+5.0) |
| ACE-Step | MIRA B=9 | 76.3 (+8.7) | 75.6 (+8.4) | 79.1 (+9.5) | 73.4 (+7.3) |
| SongGeneration2 | Direct | 60.5 | 59.2 | 62.9 | 58.3 |
| SongGeneration2 | MIRA B=3 | 66.2 (+5.7) | 64.9 (+5.7) | 68.9 (+6.0) | 63.2 (+4.9) |
| SongGeneration2 | MIRA B=9 | 72.0 (+11.5) | 70.8 (+11.6) | 75.3 (+12.4) | 68.4 (+10.1) |
| YuE2-3B | Direct | 76.5 | 75.8 | 79.2 | 73.3 |
| YuE2-3B | MIRA B=3 | 80.5 (+4.0) | 79.9 (+4.1) | 83.1 (+3.9) | 77.6 (+4.3) |
| YuE2-3B | MIRA B=9 | 82.1 (+5.6) | 81.3 (+5.5) | 85.0 (+5.8) | 78.4 (+5.1) |

Per-dimension examples:

- ACE-Step B=9: Style 75.4, I/V 69.1, Mood 83.0, Rhythm 77.2, H/M 72.8, S/E 74.6, P/T 77.0.
- SongGeneration2 B=9: Style 75.1, I/V 63.5, Mood 77.2, Rhythm 74.6, H/M 59.8, S/E 72.1, P/T 73.4.
- YuE2 B=9: Style 82.8, I/V 77.7, Mood 87.7, Rhythm 81.9, H/M 75.8, S/E 81.0, P/T 81.9.

#### Authors’ headline claims

Relative Overall improvements at \(B=9\):

- ACE-Step: **12.9% relative**;
- SongGeneration2: **19.0% relative**;
- YuE2-3B: **7.3% relative**.

YuE2-3B + MIRA reaches **82.1**, compared with **81.9** for Suno v5.5, the strongest commercial baseline on the primary evaluator.

ACE-Step + MIRA reaches **76.3**, compared with **75.9** for MiniMax music-2.6.

#### Interpretation

The largest relative gain occurs for SongGeneration2, whose direct baseline is weakest. This is consistent with MIRA helping generators whose native prompt alignment is poorer, although the paper does not test that hypothesis directly.

The gains are not uniform across musical dimensions. Harmony/melody remains relatively weak for SongGeneration2, suggesting that prompt refinement cannot fully compensate for backend limitations.

### 7.2 Commercial systems

| System | Overall | D-Macro | Base | Comp. |
|---|---:|---:|---:|---:|
| MiniMax 2.6 | 75.9 | 75.4 | 78.2 | 74.0 |
| MiniMax 3.0 | 77.0 | 75.6 | 79.8 | 74.8 |
| Mureka V9 | 80.6 | 80.0 | 84.0 | 77.2 |
| Mureka V9.5 | 81.2 | 80.6 | 83.8 | 78.9 |
| StepAudio 3 | 79.6 | 79.3 | 82.6 | 76.5 |
| Suno v4 | 73.6 | 72.8 | 75.8 | 72.9 |
| Suno v4.5 | 76.8 | 76.0 | 80.0 | 73.2 |
| Suno v5 | 79.7 | 79.0 | 83.1 | 76.0 |
| Suno v5.5 | 81.9 | 80.9 | 85.3 | 77.7 |
| Suno v6 | 81.8 | 81.5 | 85.8 | 77.6 |

Suno’s Overall scores increase from 73.6 in v4 to 81.9 in v5.5, then slightly decrease to 81.8 in v6.

### 7.3 Human system-level evaluation

**Anchor:** Figure 3, Appendix B.3, PDF pp. 8 and 17.

The study used:

- all 100 requests;
- 400 clips;
- four systems per request:
  - direct ACE-Step;
  - ACE-Step + MIRA B=9;
  - MiniMax music-3.0;
  - Suno v5.5;
- one expert rating per clip and intent dimension;
- five-point scales for overall, explicit, and inferred intent.

Means:

| System | Overall | Explicit | Inferred/completed |
|---|---:|---:|---:|
| ACE-Step direct | 3.84 | 3.89 | 4.01 |
| ACE-Step + MIRA B=9 | 4.04 | 4.07 | 4.23 |
| MiniMax 3.0 | 3.99 | 4.02 | 4.11 |
| Suno v5.5 | 4.26 | 4.24 | 4.31 |

MIRA improves ACE-Step in all three human-rated dimensions and exceeds MiniMax 3.0, while remaining below Suno v5.5.

The confidence intervals are shown in the figure, but exact interval endpoints are not tabulated.

---

### 8. Ablations and equal-budget comparison

**Anchor:** Table 3 and Figure 4, PDF p. 8.

The ablation uses a fixed subset of 20 requests and ACE-Step/YuE2 only.

### 8.1 Table 3

#### ACE-Step

| Configuration | Overall | D-Macro | Base | Comp. |
|---|---:|---:|---:|---:|
| Direct | .759 | .756 | .803 | .710 |
| Best-of-9 | .800 | .795 | .874 | .719 |
| Tools + Best-of-9 | .815 | .807 | .871 | .748 |
| Tools + Adaptive search | .826 | .814 | .862 | .781 |
| Full MIRA | **.836** | **.826** | **.880** | **.782** |

#### YuE2-3B

| Configuration | Overall | D-Macro | Base | Comp. |
|---|---:|---:|---:|---:|
| Direct | .816 | .811 | .868 | .752 |
| Best-of-9 | .848 | .850 | .910 | .775 |
| Tools + Best-of-9 | .860 | .852 | .911 | .800 |
| Tools + Adaptive search | .867 | .863 | .913 | .808 |
| Full MIRA | **.872** | **.868** | .911 | **.821** |

#### Authors’ interpretation

- Tool grounding chiefly improves Completion.
- Adaptive search improves Overall, D-Macro, and Completion.
- Structured memory produces the best Overall and D-Macro.

#### Equal-budget comparison

Figure 4 compares independent Best-of-9 sampling with MIRA using nine generations:

| Backend | Best-of-9 Overall | MIRA Overall | Best-of-9 D-Macro | MIRA D-Macro |
|---|---:|---:|---:|---:|
| ACE-Step | 80.0 | 83.6 | 79.5 | 82.6 |
| YuE2-3B | 84.8 | 87.2 | 85.0 | 86.8 |

The plotted improvements are approximately:

- ACE-Step Overall: **+3.6 points**;
- YuE2 Overall: **about +2.4 points**.

This is the most direct evidence that MIRA is not merely benefiting from having nine samples.

---

### 9. Cross-evaluator results

**Anchor:** Appendix D.4, Table 8, PDF pp. 20–21.

MIRA was still selected using MusicFlamingo, but outputs were rescored by MOSS-Music and Qwen3-Omni.

### MOSS-Music Overall / D-Macro / Base / Completion

| Backend | Direct | MIRA B=3 | MIRA B=9 |
|---|---|---|---|
| ACE-Step | 64.7 / 65.6 / 66.5 / 63.8 | 71.2 / 71.5 / 73.1 / 68.1 | 71.9 / 72.7 / 73.1 / 69.8 |
| SongGeneration2 | 62.9 / 63.1 / 65.0 / 60.5 | 66.0 / 66.4 / 68.6 / 62.2 | 69.8 / 69.5 / 71.8 / 67.0 |
| YuE2-3B | 73.9 / 73.7 / 76.3 / 71.3 | 77.5 / 77.7 / 79.8 / 76.0 | 78.4 / 78.1 / 80.7 / 76.8 |

### Qwen3-Omni Overall / D-Macro / Base / Completion

| Backend | Direct | MIRA B=3 | MIRA B=9 |
|---|---|---|---|
| ACE-Step | 59.5 / 60.0 / 62.4 / 57.1 | 65.7 / 67.4 / 69.8 / 62.9 | 67.1 / 68.2 / 70.1 / 64.7 |
| SongGeneration2 | 53.0 / 53.1 / 55.0 / 51.8 | 56.5 / 57.2 / 59.5 / 53.8 | 64.3 / 64.4 / 67.9 / 61.6 |
| YuE2-3B | 66.8 / 68.2 / 70.7 / 62.7 | 69.0 / 70.1 / 71.5 / 66.8 | 70.6 / 71.5 / 74.2 / 67.5 |

Both alternative evaluators preserve the direction of the MIRA improvement.

#### Caveat

The paper itself notes that Qwen3-Omni has lower agreement with human ratings than MusicFlamingo. The proposed explanation—that a general-purpose model is less sensitive to fine-grained musical properties—is explicitly described as an untested possibility.

---

### 10. Limitations and risks

### Explicitly acknowledged by the authors

**Anchor:** §6 and Appendix F, PDF pp. 9 and 26.

1. **Interpretive and cultural bias.**  
   Three experts and the models may encode particular musical conventions. The benchmark measures alignment with its rubrics, not universal musical quality.

2. **Intent is not uniquely determined.**  
   References and scenarios may admit multiple legitimate musical interpretations.

3. **Copyright and originality are outside the metric.**  
   Generalizing artist references reduces direct imitation, but alignment scores do not establish originality or copyright safety.

4. **Human studies focus only on fulfillment.**  
   General quality and listener preference are explicitly outside scope.

### Additional methodological risks

#### Benchmark scope

The benchmark is small and sourced from one commercial platform. It may not represent:

- professional composer workflows;
- classical music;
- instrumental arrangement;
- symbolic editing;
- mashups;
- repair;
- culturally diverse interpretations;
- users outside Mureka’s platform ecology.

#### Rubric ground truth

Expert revisions are valuable, but:

- experts work on disjoint subsets;
- no inter-rater reliability is reported for rubric construction;
- completion items necessarily involve interpretation;
- a single “gold” rubric may suppress valid alternative readings.

#### Evaluator dependence

MusicFlamingo is used to:

1. guide search;
2. rank candidates;
3. select the final candidate.

The same family of judgments is then central to the primary benchmark score. This can favor outputs that satisfy MusicFlamingo’s representation of musical requirements.

#### Compute and cost accounting

The budget counts generated candidates but excludes:

- planner calls;
- retrieval calls;
- verifier queries;
- wall-clock time.

Thus \(B=9\) is not a complete measure of inference cost.

#### Reproducibility gaps

The PDF specifies:

- models;
- thresholds;
- prompt constraints;
- seeds for some systems;
- hardware;
- major search allocation.

But it does not provide full operational detail about:

- retrieval-tool implementations and knowledge sources;
- exact API settings for commercial models;
- runtime and verifier-query counts;
- statistical tests over repeated runs;
- confidence intervals for automatic benchmark scores;
- complete public artifacts.

Commercial models are also subject to API version drift.

#### Search/backend limitations

ACE-Step and YuE retain fixed generation seeds within adaptive search, whereas SongGeneration2 uses native stochastic generation. This makes backend comparisons nonuniform.

MIRA modifies prompts, not latent states, parameters, note events, or audio directly. It may therefore fail when the generator cannot realize a requested change through text.

#### No direct causal explanation test

The traces record motivations and observed score changes, but the paper does not systematically test whether explanations are faithful. A prompt edit may be described as repairing rhythm while actually changing instrumentation or overall style.

---

### 11. Relevance to explainable controllable symbolic music

### Strongly transferable ideas

#### 11.1 Rubrics as explicit intent contracts

For symbolic music, rubric items could be exact predicates such as:

- melody identity preserved;
- source A contributes the principal motif;
- source B contributes bass/harmony;
- meter remains 4/4;
- cadence occurs at phrase boundary;
- no parallel fifths;
- voice-leading leap below a threshold;
- target density range;
- motif appears at least twice;
- original source notes are untouched.

This is more auditable than a single “musicality” score.

#### 11.2 Requirement-level diagnostics

MIRA’s Base/Completion split maps naturally to:

- explicit user constraints;
- inferred compositional intent.

For mashups:

- explicit: “combine melody A with accompaniment B”;
- inferred: preserve source identity, avoid harmonic collision, create a coherent transition.

For repair:

- explicit: “preserve melody and key”;
- inferred: repair the clash with minimal disruption and retain phrase/cadence structure.

#### 11.3 Search over transformations, not only prompts

A symbolic MIRA variant could search over structured operations:

- transposition;
- time stretching;
- rhythmic quantization;
- chord substitution;
- voice reassignment;
- phrase deletion/insertion;
- orchestration change;
- motif transformation;
- bridge generation;
- cadence repair.

The tree memory could preserve which operations improved one requirement while damaging another.

#### 11.4 Provenance-preserving explanations

Appendix D.5 specifies traces containing:

- original and revised prompts;
- seeds;
- node and round identifiers;
- actions;
- verifier feedback;
- resolved and regressed requirements;
- tool calls;
- evidence cards.

For symbolic music, these can become a provenance graph linking:

> source note/phrase → detected conflict → candidate operation → affected constraint → resulting score change.

That is closely aligned with the repository’s goal of conflict-aware, provenance-preserving repair.

### Important difference

MIRA currently verifies generated **audio**. Audio-language verification cannot reliably establish:

- exact note identity;
- source provenance;
- minimality of repair;
- voice-leading legality;
- whether a motif was copied, transformed, or lost;
- exact harmonic function.

Symbolic research should therefore replace or supplement MusicFlamingo with deterministic and learned symbolic verifiers.

---

### 12. Concrete research ideas

### 12.1 MuRA-SymBench

Create a symbolic analogue with:

- user requests;
- paired source pieces;
- explicit and inferred requirements;
- expert-revised rubrics;
- exact symbolic predicates;
- human ratings for coherence, identity, novelty, and playability.

Use separate rubrics for overlay, transition, recomposition, and repair.

### 12.2 Provenance-preserving MIRA for mashups

Search jointly over:

- alignment;
- transformation;
- orchestration;
- harmony;
- phrase structure.

Add immutable source anchors and require every output event to have provenance:

- source A;
- source B;
- generated;
- transformed from A/B.

Evaluate source identity separately from compatibility and novelty.

### 12.3 Conflict-aware symbolic repair

Represent rubric failures as a conflict graph:

- incompatible pitch classes;
- rhythmic collision;
- voice-crossing;
- phrase-boundary mismatch;
- cadence disruption;
- density overload.

Search minimal repairs under protected-note constraints. Return:

- repaired score;
- conflict classification;
- changed notes;
- preserved notes;
- rejected alternatives;
- counterfactual explanations.

### 12.4 Faithfulness evaluation for explanations

Adapt MIRA’s traces into a causal test:

1. The agent claims an operation repaired rhythm.
2. Remove or undo that operation.
3. Re-evaluate the affected rubric.
4. Check whether the claimed improvement disappears.

This distinguishes a useful explanation from a post-hoc narrative.

### 12.5 Multi-objective frontier instead of one score

MIRA’s lower-tail criterion is promising, but symbolic mashups should retain a Pareto frontier over:

- compatibility;
- source identity;
- structural coherence;
- novelty;
- playability;
- repair minimality;
- explanation faithfulness.

Do not collapse these permanently into one weighted score.

### 12.6 Active verifier budgeting

Generation is expensive. Use a cascade:

1. cheap deterministic symbolic checks;
2. learned symbolic models;
3. audio rendering and perceptual verification;
4. human adjudication for ambiguous cases.

Allocate the search budget to candidates with high uncertainty or high potential Pareto improvement.

### 12.7 Expert disagreement as data

Instead of forcing one completed rubric, store:

- multiple plausible interpretations;
- expert confidence;
- disagreement;
- culturally dependent alternatives.

Evaluate whether a system satisfies the request under several legitimate rubrics.

---

### Bottom line

#### Authors’ demonstrated result

MIRA improves rubric-level intent alignment across three open-source text-to-music generators, at both \(B=3\) and \(B=9\), and outperforms equal-budget independent sampling on a 20-request ablation subset.

#### My assessment

The strongest transferable contribution is the combination of:

- explicit intent decomposition;
- requirement-level verification;
- budgeted search;
- lower-tail-aware candidate selection;
- branch-specific memory;
- inspectable traces.

For symbolic mashup and repair, the main research opportunity is to replace opaque audio-level verification with **exact, provenance-aware symbolic predicates** and to test explanation faithfulness causally.

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
