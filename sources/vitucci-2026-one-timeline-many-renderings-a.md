---
title: "One Timeline, Many Renderings: A Wolfram Language Paclet for Heterogeneous Musical Output"
authors: "Francesco Vitucci, Michele Lorusso, and Francesco Scagliola"
year: 2026
doi: 10.48550/arXiv.2608.24683
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/vitucci-2026-one-timeline-many-renderings-a.pdf"
pdf_filename: vitucci-2026-one-timeline-many-renderings-a.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

I inspected all five PDF pages, the extracted text, Figures 1–2, and the references. **There are no tables, appendices, or quantitative result tables.**

## 1. Document Information

- **Canonical source:** arXiv `2608.24683v1`; official PDF preserved as `vitucci-2026-one-timeline-many-renderings-a.pdf`.
- **Full-paper evidence:** delegate digest `del_mv41492s_oqyh.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### Paper identification

**Full title:** *One Timeline, Many Renderings: A Wolfram Language Paclet for heterogeneous musical output*  
**Authors:** Francesco Vitucci, Michele Lorusso, and Francesco Scagliola  
**Affiliation:** Conservatorio di Musica “N. Piccinni” di Bari  
**Version:** arXiv:2608.24683v1, 25 August 2026; 5-page PDF, classified `[cs.CL]`.

I inspected all five PDF pages, the extracted text, Figures 1–2, and the references. **There are no tables, appendices, or quantitative result tables.**

### Executive digest

The paper presents **Temporal System**, an unreleased Wolfram Language paclet for representing one algorithmic-composition timeline once and compiling it into several synchronized outputs:

- Csound score/orchestra artifacts;
- beta MusicXML 4.0 notation;
- OSC event schedules;
- Csound-based rehearsal click tracks.

Its central design is an **immutable typed event store using exact rational beat positions**. Conversion to seconds, samples, milliseconds, or frequency is deferred to individual renderers.

The contribution is primarily an **authoring and rendering architecture**, not a music-generation model, symbolic transformation algorithm, or source-preserving recomposition method.

---

### 1. Problem and motivation

#### Author claims — PDF p. 1, §1 Introduction

The paper identifies a practical problem in mixed computer-music workflows: the same composition may require a Csound score, notation, real-time control, and rehearsal click, but separately authored outputs can drift when tempo, meter, or structure changes.

The proposed solution is to make one timeline authoritative:

> “Temporal System … makes one timeline authoritative and every output derived.”

The authors distinguish their work from existing systems such as music21, Abjad, MEI/Verovio, bach, and Tidal. Their stated narrower contribution is combining:

- exact temporal representation;
- notation;
- offline Csound;
- OSC;
- click-track output;
- explicit backend-specific contracts.

#### Interpretation

This addresses **consistency between renderings**, not the harder musical problem of preserving source identity through transformation. “One timeline” is a synchronization/provenance-of-time mechanism, not yet provenance of musical material.

---

### 2. Representation and architecture

### 2.1 Temporal layer

**PDF p. 2, §2 “Anatomy of the Paclet”**

Tempo is represented as an ordered list of `{beat, BPM}` points. Each BPM applies stepwise until the next point. Compilation produces a piecewise-linear `{beat, seconds}` map with analytical inversion.

Important properties:

- Onsets and durations remain exact `Rational` values until rendering.
- Seconds and samples are computed only when a backend requires them.
- Continuous accelerando and ritardando are **not supported**.

The authors describe all functions as pure, with store operations returning new stores.

### 2.2 Semantic layer

The store is organized by type:

```text
stemData[type][id]
```

The paper claims O(1) typed access and an O(n) per-event rendering pass, but explicitly says that no large-score benchmark is claimed.

Seven implemented entity types are listed:

1. note;
2. rest;
3. trigger;
4. curve;
5. state;
6. marker;
7. annotation.

Four additional types are declared for future use:

- process;
- interval;
- trajectory;
- gesture.

A note contains:

- pitch, represented as spelling plus cents, MIDI float, or frequency;
- duration;
- dynamics;
- backend-specific rendering associations.

Meter is represented as a **state entity**. Meter is authored rather than inferred. A session configuration carries values such as `tuningA4`, defaulting to 440 Hz.

### 2.3 Rendering-contract layer

Each backend defines a contract for its rendering payload. Constructors validate the common entity shape and require `rendering[backend]` payloads to use keys belonging to that backend contract.

The paper emphasizes explicit loss policies. For example, MusicXML warns when a continuous curve is reduced to textual notation rather than silently inventing an equivalent notation.

#### Interpretation

The representation is promising for reproducible symbolic workflows because exact beat-space data survives tempo and tuning changes. However, backend-specific payloads are embedded inside the shared entities. This makes the store flexible, but it also introduces renderer-specific coupling that a future neutral interchange format would need to resolve.

---

### 3. Renderers

### 3.1 Generic dispatcher

**PDF p. 2, §3**

The paper gives the generic entry point as:

```text
renderTo[stemData, tempo, backend, config, registry]
```

Four backends are implemented.

### 3.2 Csound

**PDF pp. 3–4, §4 “The Csound Renderer”; Figure 2**

The default Csound p-field contract is:

- `p1`: instrument;
- `p2`: onset in seconds;
- `p3`: duration in seconds;
- `p4`: frequency in Hz;
- `p5`: amplitude in `[0, 1]`;
- `p6+`: entity payload fields.

The renderer is named:

```text
renderCSnd
```

Notes and triggers become `i` statements; markers become onset-ordered comments; curves become k-rate control signals. Curves can be implemented with a GEN-2 table read or generated `transeg`, depending on session configuration.

The paper gives this actual output:

```text
i "sine_osc" 0. 4. 440. 0.65 0.5
```

This represents A4, mezzo-forte, two whole notes at 120 BPM.

The orchestra registry uses stable instrument names from external `.orc` files. The authors claim that numeric renumbering is therefore unnecessary.

For parameter curves:

- `multiply` scales the note’s base value;
- `replace` discards the base value;
- later multiplicative bindings may scale replacement values.

For affected instruments, the renderer copies the instrument body and rewrites only bound p-field use sites. Other content—guards, envelopes, clamps, and oscillator logic—is reproduced.

#### Limitation

The current approach depends on copying and rewriting instrument bodies. Named software channels and voice-addressing conventions are not implemented; a channel-based adapter is future work.

### 3.3 MusicXML

**PDF pp. 2–3, §3**

The beta MusicXML backend:

- builds measures from authored meter;
- splits notes at barlines into tied fragments;
- validates measure capacity, part coverage, ties, and chords;
- emits MusicXML 4.0 partwise output;
- is described as an explicitly lossy projection;
- was checked by round-tripping through Dorico for ties, meter, and part separation.

MusicXML requires authored pitch spelling, optionally with cents. It rejects bare MIDI floats or frequencies. The utility `midiToSpelling` uses documented sharp spelling; the paper gives `58 → A#3` as an example.

The authors explicitly note that the spelling policy was not tested by the diatonic synchrony fixture.

### 3.4 OSC

**PDF pp. 3–4, §§3–4**

OSC output is a schedule-ready JSON event list in milliseconds. Curves are sampled at a configurable control rate and can be dispatched as OSC messages to a graphical patcher or a Csound instance.

The paper gives an exact example:

- two-second linear ramp;
- sampled half-open at 10 Hz;
- events from 0 through 1900 ms;
- JSON `duration_ms` is therefore 1900;
- final message has:
  - `time_ms = 1900`;
  - address `/param/amplitude`;
  - argument `[0.95]`.

The same beat-space curve and tempo map are used as in Csound, but the OSC representation streams timed parameter messages rather than binding a curve to a score p-field.

### 3.5 Click track

**PDF p. 4, §5 “A Click Track from the Same Timeline”; Figure 2**

The click backend uses only authored meter and tempo. It creates one event per beat and accents downbeats.

Session-configurable defaults include:

- beat unit: `1/4`;
- click duration: `1/16`;
- strong frequency: 1760 Hz;
- weak frequency: 1100 Hz;
- strong amplitude: 0.9;
- weak amplitude: 0.45;
- pan.

For two 4/4 bars at 120 BPM, the authors report strong downbeats at 0 and 2 seconds, with weak intervening beats.

The implementation is described as roughly 140 lines and reuses `serializeCSnd` unchanged.

---

### 4. Figures

### Figure 1 — PDF p. 2, §2

Figure 1 is a `drawTimeline` visualization of a stress fixture, not a representative composition. It shows:

- 16 sine-oscillator notes, including cent offsets;
- 8 click hits;
- 4 triggers;
- 6 overlapping amplitude/pan curves;
- section markers;
- meter changes:
  - 4/4 opening;
  - 5/8 rotation;
  - 7/8 expansion;
  - 3/4 coda.

The authors explicitly characterize it as:

> “A stress fixture exercising many entity types at once, not a representative composition.”

### Figure 2 — PDF p. 3, §4

Figure 2 shows the shared pipeline:

```text
entity store + tempo map
        ↓
renderCSnd / renderClickTrack
        ↓
score and orchestra primitives
        ↓
serializeCSnd
        ↓
.csd + generated code + included .orc
```

It illustrates that Csound and click output share serialization while source instruments remain external and curve bindings create generated copies.

---

### 5. Synchrony demonstration

**PDF p. 4, §6 “Keeping the Projections Synchronous”**

The paper reports a single synchrony fixture:

- two 4/4 bars followed by 3/4;
- tempo changes from 120 to 90 BPM;
- rendered to Csound, click, OSC, and beta MusicXML.

For the third-bar downbeat, the reported outputs are:

- Csound: `p2 = 4.0 s`;
- OSC: `time_ms = 4000`;
- click: strong click at 4.0 s;
- MusicXML: bar 3, beat 1.

When the second tempo segment is changed from 90 to 60 BPM, the paper reports that later onsets change consistently in the time-domain backends. Its example is:

```text
beat 9/4: 4.667 s → 5.0 s
```

MusicXML changes only the second tempo mark, from 90 to 60 BPM; initial tempo and written note durations remain unchanged because notation stays in beat space.

#### Evidence qualification

The authors state that shared rational onsets and a shared compiled tempo map prevent drift. The evidence presented is a fixture-level demonstration, not a formal proof or broad stress test. No error tolerances, randomized tests, large scores, or independent backend comparison metrics are reported.

---

### 6. Experiments and reported results

This is an implementation report rather than a conventional empirical music-AI paper.

#### Reported evidence

**PDF p. 2, §2**

- Every fixture in the Csound suite reportedly compiled without error and was auditioned.
- A Zenodo supplement reportedly archives:
  - the generating notebook;
  - Csound, OSC, MusicXML, and click outputs;
  - audio;
  - the tempo-edit synchrony demonstration.

**PDF pp. 3–4, §§3–6**

- Exact Csound serialization example.
- Exact OSC sampling example.
- Click-track example.
- Cross-renderer synchrony example.
- MusicXML round-trip checking through Dorico.

#### Not reported

The paper contains no:

- dataset;
- learned model;
- training procedure;
- quantitative benchmark;
- baseline comparison;
- listening study;
- user study;
- timing-error statistics;
- scalability measurements;
- ablation study;
- formal test of source preservation;
- evaluation of musical quality, coherence, novelty, or playability.

The authors themselves say no large-score benchmark is claimed.

---

### 7. Limitations

### Explicit author-stated limitations

**PDF pp. 1, 4, §7**

1. The paclet is unreleased.
2. Authoring requires proprietary Wolfram software.
3. The free Wolfram Engine is licensed for development and non-commercial use.
4. A language-neutral store serialization and Python/Julia core are future work, not present capabilities.
5. MusicXML is beta and explicitly lossy.
6. MIDI output is absent, although planned.
7. Continuous tempo is unsupported.
8. Csound curves depend on declared p-fields and rewritten instrument copies.
9. Named Csound channels are not implemented.
10. There is no large-score benchmark.
11. The stress fixture is not representative of a composition.
12. Adding arbitrary backends is not measured by the click-track implementation; the “roughly 140 lines” result is only one reuse case.
13. The paper says the archived supplement covers much of the reproducibility gap, but the paclet itself remains unreleased.

### Additional interpretation

The central synchronization claim is plausible for outputs that correctly consume the same store and tempo map, but the paper demonstrates it only with hand-designed fixtures. It does not establish robustness under malformed events, complex tuplets, polymeter, expressive tempo, large orchestral scores, or contradictory backend contracts.

---

### 8. Relevance to symbolic music source-preserving transformations

### Directly useful

**Interpretation grounded in the architecture**

The paper offers several components that could support a source-preserving symbolic transformation system:

- exact rational beat positions avoid repeated floating-point timing changes;
- immutable stores make transformations naturally functional and reproducible;
- typed entities support notes, rests, meter, curves, markers, and annotations;
- stable entity IDs and explicit rendering associations could help track transformed material;
- late tempo and tuning conversion allows rendering changes without rewriting source events;
- multiple synchronized outputs are useful for inspecting a transformation as notation, synthesis, control data, and rehearsal audio.

These properties could support a mashup or repair pipeline in which transformed notes retain stable source references.

### Important gap

The paper does **not** implement source-preserving transformation in the research sense. It does not provide:

- source-A/source-B provenance;
- protected source material;
- transformation operators;
- alignment between sources;
- conflict detection;
- minimal repair;
- rationale graphs;
- identity-preservation metrics;
- counterfactual alternatives;
- listener or musician evaluation.

Its “preservation” concerns primarily **temporal consistency across renderings**, not preservation of melody, rhythm, voice, style, or source identity.

MusicXML’s explicitly lossy projection also means that the same semantic entity may not survive identically in every output. Curves may become textual directions, and pitch representations may be rejected or respelled.

---

### 9. Relevance to general music generation

The work is relevant as **generation infrastructure**, not as a generative model.

#### Potential value

A symbolic generator could emit Temporal System entities and then obtain synchronized:

- notation;
- Csound audio;
- OSC performance control;
- rehearsal click.

The exact beat-space representation is particularly useful for evaluating whether generated material remains stable when tempo, meter, or tuning changes.

#### What it does not address

It does not learn musical distributions, generate motifs, model style, infer harmony, optimize musical objectives, or evaluate listener preference. It is best understood as a backend/rendering layer that could sit after a symbolic composition or AI generation system.

### Overall assessment

The paper’s defensible contribution is a compact architecture for **single-source, exact-time, multi-backend musical rendering**. Its strongest evidence is the concrete fixture outputs and synchrony demonstration. Its weakest areas are reproducibility before paclet release, absence of scalability and quantitative evaluation, proprietary authoring, and the lack of any mechanism for musical provenance or source identity.

For the repository’s research goal, it is most valuable as a possible **representation and rendering substrate** for provenance-preserving symbolic mashup or repair—not as evidence that source-preserving transformation or explainable music generation has been solved.

## 3. Methodology and Architecture

The methodology and architecture are preserved in the embedded full-paper digest above, including its original page/section anchors.

## 4. Key Results and Benchmarks

Reported results and benchmark denominators are preserved in the embedded digest above; no unverified reproduction is implied by this record.

## 5. Limitations and Future Work

The evidence limitations, artifact status, and future-work claims are preserved in the embedded digest above. See the batch report for relevance to the explainable symbolic music AI programme.

## 6. Related Work

- [[overviews/2026-symbolic-music-literature-map]] — batch literature map and bidirectional synthesis anchor.

## 7. Glossary

- **Primary category:** `data-and-representation`. Domain-specific terms are defined in the embedded digest and cross-paper synthesis.
