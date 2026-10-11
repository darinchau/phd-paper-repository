---
title: "MusicAgent: An AI Agent for Music Understanding and Generation with Large Language Models"
authors: "Dingyao Yu, Kaitao Song, Peiling Lu, Tianyu He, Xu Tan, Wei Ye, Shikun Zhang, and Jiang Bian"
year: 2023
doi: 10.48550/arXiv.2310.11954
category: interaction-and-evaluation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/yu-2023-musicagent-an-ai-agent-for.pdf"
pdf_filename: yu-2023-musicagent-an-ai-agent-for.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

“**MusicAgent: An AI Agent for Music Understanding and Generation with Large Language Models**.” arXiv:**2310.11954v2**, [cs.CL], **25 October 2023**. Authors are affiliated with Peking University and Microsoft Research Asia. The paper identifies its code repository as:

## 1. Document Information

- **Canonical source:** arXiv `2310.11954v2`; official PDF preserved as `yu-2023-musicagent-an-ai-agent-for.pdf`.
- **Full-paper evidence:** delegate digest `del_mv4099iy_idru.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Evidence-grounded digest

### 1. Bibliography and version

**Dingyao Yu, Kaitao Song, Peiling Lu, Tianyu He, Xu Tan, Wei Ye, Shikun Zhang, and Jiang Bian.**  
“**MusicAgent: An AI Agent for Music Understanding and Generation with Large Language Models**.”  
arXiv:**2310.11954v2**, [cs.CL], **25 October 2023**. Authors are affiliated with Peking University and Microsoft Research Asia. The paper identifies its code repository as:

- `https://github.com/microsoft/muzic/tree/main/musicagent`
- Demonstration video: `https://youtu.be/tpNynjdcBqA`

The PDF contains an abstract, Sections 1–5, Appendix heading, references, and demonstration figures. There is **no separate experiments, user-study, or limitations section**.

---

### 2. Core contribution and architecture

#### Author claim

MusicAgent is presented as an LLM-controlled agent that integrates heterogeneous music tools and decomposes natural-language requests into subtasks. Its stated goals are accessibility, unified data formats, and modularity (abstract; Sections 1 and 5, PDF pp. 1–2, 6–7).

The system has four components (Figure 2, PDF p. 3):

1. **Task Planner** — LLM-based.
2. **Tool Selector** — LLM-based.
3. **Task Executor** — executes selected tools.
4. **Response Generator** — LLM-based.

The workflow is:

```text
user request
  → task decomposition
  → dependency graph / task queue
  → tool selection
  → parameterized tool execution
  → intermediate results
  → synthesized response
```

Figure 1 depicts four interaction paths:

- task planning,
- tool selection,
- task execution,
- response generation.

#### Planning

The Task Planner converts a request into structured subtasks, including:

- task type,
- input and output formats,
- dependencies between subtasks,
- an implicit dependency graph.

The paper says the planner prompt contains task descriptions, supported tasks, an information structure, and several music-task decomposition examples. User interaction history and the current request are inserted into the prompt. Semantic Kernel is used to insert task-flow text into the prompt (Section 3.2, PDF pp. 5–6).

#### Tool selection

Each tool has metadata such as:

- textual description,
- download count,
- GitHub star count,
- other user-configurable attributes.

The selector returns a tool ID and a textual reason for the selection. The paper explicitly says users can change how metadata is weighted—for example, emphasizing download count (Section 3.2, PDF p. 6).

#### Invocation and execution

When all dependencies and inputs for a subtask are ready, the backend passes the subtask to the Task Executor. The selected tool chooses required parameters from the instantiated inputs and identifies which task type it is fulfilling, because one tool may support multiple tasks (Section 3.3, PDF p. 6).

This is described procedurally rather than through a formal invocation schema. The paper gives no algorithm, typed API specification, validation protocol, or error-recovery procedure.

#### Response generation

The Response Generator collects intermediate task results and produces a coherent natural-language response. The figures show that responses may include:

- selected tools,
- reasons,
- output filenames,
- a narrative description of the execution sequence.

This provides a useful execution trace, but it is not presented as a formal provenance model.

---

### 3. Tool taxonomy and representations

#### Representations

The paper identifies three principal data formats (Section 3.1, PDF p. 5):

1. **Text** — lyrics, genre, emotion, theme, and other descriptions.
2. **Symbolic music / sheet music** — represented primarily as MIDI.
3. **Audio** — rendered or recorded music.

The introduction also mentions text, MIDI, ABC notation, and audio as formats that need to be unified (PDF p. 2).

Figure 3 organizes the system around:

- textual description,
- symbolic music,
- audio,
- mixing,
- separation.

The paper states that samples are trimmed to fit within a single audio segment, which simplifies tool cooperation but restricts long-form structure (Section 1, PDF p. 2).

#### Table 1 task inventory

| Category | Task | Input → output | Example tool |
|---|---|---|---|
| Generation | text-to-symbolic-music | text → symbolic music | MuseCoco |
| Generation | lyric-to-melody | text → symbolic music | ROC |
| Generation | singing-voice-synthesis | text → audio | HiFiSinger |
| Generation | text-to-audio | text → audio | AudioLDM |
| Generation | timbre-transfer | audio → audio | DDSP |
| Generation | accompaniment | symbolic music → symbolic music | GetMusic |
| Understanding | music-classification | audio → text | Wav2vec2 |
| Understanding | music-separation | audio → audio | Demucs |
| Understanding | lyric-recognition | audio → text | Whisper-large-zh |
| Understanding | score-transcription | audio → text | Basic-pitch |
| Auxiliary | artist/track-search | text → audio | Spotify API |
| Auxiliary | lyric-generation | text → text | ChatGPT |
| Auxiliary | web-search | text → text | Google API |

Table 1, PDF p. 4.

A notable representation ambiguity is that **score transcription is listed as audio → text**, while the surrounding prose describes transcription as enabling conversion into symbolic representation. The paper does not specify a canonical symbolic schema beyond MIDI-level representation.

---

### 4. Workflow and prompt examples

#### Figure 4: “write a song about love”

Figure 4 shows the request:

> “write a song about love”

The illustrated dependency graph contains:

```text
0. lyric-generation
        ↓
1. lyric-to-melody
        ↓
2. singing-voice-synthesis

3. accompaniment
        ↓
4. instrument-sound-synthesis
        ↓
5. audio-mixing
```

The figure shows candidate tools for lyric-to-melody, including **ROC** and **RelyMe**, with ROC selected and accompanied by a reason. The final response reports intermediate audio, including `0d63.wav` (Figure 4, PDF p. 5).

This example demonstrates dependency-aware planning, but it does not report whether the generated song was musically successful or whether the dependency graph was manually corrected.

#### Figure 5 case studies

##### Chinese-poetry song

The system reports this sequence:

1. ChatGPT generates lyrics.
2. `muzic/roc` converts lyrics to sheet music.
3. The system produces `e3a1.mid` and `e3a1.wav`.
4. DiffSinger converts the sheet music to audio, producing `486f.wav`.
5. A `basic-merge` model combines the generated audio files.
6. Final output: `726f.wav`.

The figure says files are available under `public/audios/` (Figure 5, PDF p. 9). The rendered text contains a duplicated `486f.wav` phrase around the final merge description.

##### Jay Chou retrieval and style analysis

The system:

1. Searches Spotify for Jay Chou songs.
2. Retrieves three versions of “Tracks,” named:
   - `8440.mp3`
   - `f68e.mp3`
   - `840e.mp3`
3. Applies Wav2vec2-based analysis.
4. Reports all three as pop style.

No classification accuracy or human verification is given.

##### Vocal-to-violin conversion

The system:

1. Applies Demucs to `8440.mp3`.
2. Extracts human vocals as `05aa.wav`.
3. Applies DDSP timbre transfer.
4. Produces violin-like audio `9561.wav`.

Again, this is an illustrative pipeline, not an evaluated experiment.

#### Listing 1: extensibility API

The code example shows:

```python
from agent import MusicAgent
music_agent = MusicAgent(CONFIG_PATH)

music_agent.task_map[MY_TASK].append(MY_TOOL)
music_agent.pipelines.append(MY_TOOL_CLASS)

music_agent._init_task_context()
music_agent._init_tool_context()

music_agent.update_tool_attributes(
    MY_TOOL, {"stars": ..., "likes": ...}
)

music_agent.task_context["history"] += "MY CUSTOM PROMPT"

music_agent.chat("Generate_a_song...")
```

Users can add task types, tools, pipelines, metadata, and prompts. The paper warns that adding prompts to interaction history is temporary and may be overwritten or overlap when the context limit is exceeded. Permanent prompts should be placed directly in code (Listing 1 and Section 4.1, PDF p. 6).

---

### 5. Experiments, user studies, and exact results

#### Evidence from the complete paper

The paper reports:

- **No quantitative experiments**
- **No baselines**
- **No ablation studies**
- **No dataset or test split**
- **No numerical task-success rate**
- **No latency, cost, or resource measurements**
- **No listening test**
- **No participant count or user-study protocol**
- **No annotation procedure**
- **No error analysis**
- **No reproducibility table**

The only performance statement is qualitative: the paper says MusicAgent demonstrates “excellent task decomposition performance” through in-context learning (Section 3.2, PDF p. 5). No measurement supports this statement.

The three Figure 5 examples and the Gradio interface in Figure 6 are demonstrations, not controlled case studies. The exact reported outputs are filenames and qualitative labels such as “pop”; musical quality is not evaluated.

Thus, the paper establishes an **architecture and prototype integration**, not an empirically validated music-agent benchmark.

---

### 6. Limitations and failure modes

#### Explicitly stated or directly visible

1. **Context-window risk**  
   Prompt insertion into history can overlap or be overwritten when context exceeds the limit (Section 4.1, PDF p. 6).

2. **Short-segment restriction**  
   Samples are trimmed to fit into a single audio segment (Section 1, PDF p. 2). This likely limits phrase-level and long-form musical planning.

3. **GPU-memory management rather than algorithmic efficiency**  
   Model parameters are stored on CPU and loaded onto GPU only when needed (Section 3.3, PDF p. 6).

4. **External-service dependence**  
   The demo requires an OpenAI token; tools depend on Hugging Face, GitHub, Spotify, Google, and other external software or APIs (Sections 3.1 and 4.2, PDF pp. 4, 6).

5. **Future work is unspecified**  
   The conclusion only says that more music-related functions will be integrated in the future (PDF pp. 6–7).

#### Limitations inferred from the implementation description

These are interpretations rather than explicit author claims:

- **Tool-selection reasoning is not necessarily faithful.** The LLM-generated reason may rationalize a selection after the fact. No selector audit or causal explanation test is reported.
- **Metadata can be a poor proxy for suitability.** Stars, likes, and download counts do not establish musical quality, compatibility, or reliability.
- **No formal validation layer is described.** The system does not appear to verify MIDI validity, timing consistency, harmonic compatibility, audio duration, or whether a tool actually produced the requested artifact.
- **No robust failure recovery is described.** There is no documented handling for unavailable APIs, malformed outputs, incompatible formats, tool crashes, hallucinated filenames, or incorrect task graphs.
- **No symbolic structural reasoning is implemented.** The system exposes MIDI as a format but does not describe note-level alignment, voice-leading, harmonic analysis, phrase structure, or constraint checking.
- **No provenance guarantee exists.** Intermediate filenames and narratives are useful traces, but there is no immutable mapping from output events back to source events or tools.
- **Audio and symbolic operations are not equivalent.** Audio mixing, timbre transfer, and transcription do not preserve symbolic identity or editability.

---

### 7. Relevance to an explainable symbolic mashup/repair agent

#### Useful architectural precedent

MusicAgent contributes several transferable ideas:

1. **Dependency-graph planning**  
   A mashup can be represented as explicit stages:

   ```text
   ingest A/B
   → normalize representations
   → align phrases / beats
   → detect conflicts
   → propose transformations
   → apply minimal repairs
   → render and validate
   → explain and export provenance
   ```

2. **Typed tool contracts**  
   Its input/output orientation suggests a stronger symbolic interface in which every tool declares schemas, preconditions, postconditions, and failure states.

3. **Modular orchestration**  
   The separation between planner, selector, executor, and response generator is appropriate for combining symbolic analysis, search, optimization, rendering, and explanation tools.

4. **Intermediate-result visibility**  
   Figure 6’s display of intermediate results could become an inspectable repair trace rather than merely a conversational answer.

#### Important gap for mashup and repair

MusicAgent does **not** solve the central research problem of conflict-aware symbolic recomposition:

- no pairwise source alignment,
- no source-contribution tracking,
- no conflict classification,
- no responsible-note or responsible-voice identification,
- no protected source material,
- no minimal repair search,
- no counterfactual alternatives,
- no explanation-faithfulness evaluation.

Its closest relevant operation is **symbolic accompaniment** and its demonstrations include audio mixing. Neither constitutes provenance-preserving symbolic mashup or repair.

#### Provenance interpretation

The agent’s textual explanations describe a sequence such as:

> ChatGPT generated lyrics → ROC generated sheet music → DiffSinger generated audio → basic-merge combined audio.

This is **workflow provenance**, not **musical provenance**. It identifies tools and files, but not:

- which notes originated in source A or B,
- which notes were transformed,
- which musical constraints caused a repair,
- which output notes are newly generated,
- whether source identity was preserved.

---

### 8. Concrete research ideas

1. **Provenance-aware symbolic intermediate representation**

   Represent every event with fields such as:

   ```text
   source_id, source_event_id, onset, duration, pitch,
   voice, measure, role, transformation_history, protected
   ```

   Every transformation should emit a provenance edge rather than only a new MIDI file.

2. **Conflict-aware planner**

   Extend the task graph with explicit conflict nodes:

   ```text
   harmonic clash
   rhythmic incompatibility
   meter mismatch
   voice crossing
   range/playability violation
   phrase/cadence conflict
   ```

   The planner should identify evidence before proposing repair.

3. **Minimal repair operators**

   Implement deterministic, auditable operations such as:

   - transposition,
   - onset displacement,
   - duration adjustment,
   - octave relocation,
   - voice reassignment,
   - chord substitution,
   - omission or controlled replacement,
   - bridge or transition insertion.

   Optimize musical improvement against edit cost and source-identity loss.

4. **Protected-material constraints**

   Let users mark melody, bass, rhythm, motif, phrase, or source-specific notes as protected, then test whether a proposed repair violates those constraints.

5. **Faithful explanations**

   Require explanations to cite:

   - the exact conflicting events,
   - the computed musical rule or evidence,
   - the applied operation,
   - the resulting changes,
   - rejected alternatives,
   - a counterfactual showing what happens without repair.

   The LLM should verbalize a structured record rather than invent the record.

6. **Benchmark and metrics**

   Build paired symbolic excerpts with annotated conflicts and acceptable repairs. Evaluate separately:

   - compatibility,
   - source identity,
   - structural coherence,
   - novelty,
   - playability,
   - edit minimality,
   - provenance completeness,
   - explanation faithfulness.

7. **Agent ablations**

   Compare:

   - LLM planner versus hand-designed planner,
   - metadata-based versus music-quality-based tool selection,
   - free-form explanations versus structured provenance,
   - unconstrained versus protected-source repair,
   - single-shot repair versus search over alternatives.

8. **Reproducible execution logs**

   Record model/API versions, prompts, tool versions, hashes of all inputs and outputs, random seeds, selected parameters, validation results, and failures. This directly addresses the reproducibility omissions in MusicAgent.

### Bottom line

MusicAgent is a useful early architectural reference for **LLM-mediated orchestration of heterogeneous music tools**. Its strongest ideas are dependency-graph planning, tool metadata, modular plugins, and visible intermediate results. However, the paper provides **no empirical validation** and does not address symbolic mashup/repair’s central requirements: conflict diagnosis, minimal repair, source identity, note-level provenance, or faithful explanation.

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
