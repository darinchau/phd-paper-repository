---
title: "MidiTok: A Python Package for MIDI File Tokenization"
authors: "Nathan Fradet, Jean-Pierre Briot, Fabien Chhel, Amal El Fallah Seghrouchni, and Nicolas Gutowski"
year: 2023
doi: 10.48550/arXiv.2310.17202
category: data-and-representation
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/fradet-2023-miditok-a-python-package-for.pdf"
pdf_filename: fradet-2023-miditok-a-python-package-for.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
---
## One-line Summary

MidiTok is an open-source Python library that converts MIDI into token sequences suitable for Transformer-style symbolic-music models. Its central contribution is not a new model, dataset, or tokenization algorithm; it is a **unified, configurable implementation of many existing tokenization schemes**, plus preprocessing, BPE, augmentation, dataset utilities, and model-hub integration.

## 1. Document Information

- **Canonical source:** arXiv `2310.17202v1`; official PDF preserved as `fradet-2023-miditok-a-python-package-for.pdf`.
- **Full-paper evidence:** delegate digest `del_mv42y90g_ae6y.out` was produced from the supplied PDF and extracted text; the detailed digest is retained under **Key Contributions** below.
- **Evidence policy:** numerical results, author claims, artifact claims, and repository inferences remain distinguished in the embedded digest. The report must not treat an abstract or reference-list mention as a full-paper reading.

## 2. Key Contributions

### Full-paper digest

### MidiTok digest

**Paper:** Nathan Fradet, Jean-Pierre Briot, Fabien Chhel, Amal El Fallah Seghrouchni, Nicolas Gutowski, “MidiTok: A Python package for MIDI file tokenization,” arXiv:2310.17202v1, 26 October 2023.  
**Artifact inspected:** full 9-page PDF and extracted text. The paper links to [github.com/Natooz/MidiTok](https://github.com/Natooz/MidiTok).

### 1. Main contribution

MidiTok is an open-source Python library that converts MIDI into token sequences suitable for Transformer-style symbolic-music models. Its central contribution is not a new model, dataset, or tokenization algorithm; it is a **unified, configurable implementation of many existing tokenization schemes**, plus preprocessing, BPE, augmentation, dataset utilities, and model-hub integration.

The paper addresses a genuine reproducibility problem: many symbolic-music papers introduce token formats without releasing convenient implementations. MidiTok aims to make tokenization interchangeable and reproducible across generation, transcription, modeling, and MIR tasks (§1, p.1).

The paper reports that MidiTok had already been used in research and production-oriented tooling, including Qosmo’s Neutone DAW plugin (§6, p.7).

---

### 2. Package architecture and workflow

#### Configuration-driven design

A tokenizer is created from a `TokenizerConfig` containing:

- pitch range;
- beat/time resolution;
- number of velocity bins;
- enabled optional information such as tempo, rests, chords, programs, sustain pedal, pitch bend, and time signatures;
- special tokens;
- single-stream versus per-track operation.

The tokenizer derives its vocabulary from this configuration and can save/load the configuration as JSON (§3, p.3).

The implementation is organized around shared abstractions:

- `Event`: token type, value, time, and optional description;
- `TokSequence`: tokens, integer IDs, events, or BPE bytes;
- a common `MusicTokenizer` base class;
- tokenizer-specific subclasses for REMI, TSD, CPWord, MIDILike, MuMIDI, Octuple, MMM, Structured, and related schemes.

The v2-era source exposes these through `miditok/classes.py` and `miditok/midi_tokenizer.py`; the package root imports `Event`, `TokenizerConfig`, `TokSequence`, `MusicTokenizer`, `TokTrainingIterator`, augmentation utilities, and the tokenization classes.

#### Processing pipeline

The paper’s workflow is (§3, p.3):

1. **Preprocess MIDI**
   - merge tracks when using one token stream;
   - remove out-of-range pitches;
   - quantize onset, offset, velocity, tempo, and time-signature values;
   - remove duplicate notes/events and empty tracks;
   - optionally merge tracks with the same program.
2. Gather global events such as tempo and time signature.
3. Gather track events such as notes and chords.
4. Either:
   - concatenate all events into one time-sorted stream, or
   - create one stream per track.
5. Add/deduce time events.
6. Return token strings and integer IDs.

The package divides events into:

- **global tokens:** tempo, time signature;
- **track tokens:** notes, chords, programs, pedal, pitch bend;
- **time tokens:** Bar, Position, TimeShift, Duration, or Rest.

The authors state that detokenization reconstructs the **preprocessed** MIDI exactly, not necessarily the original unquantized MIDI (§3, p.3).

---

### 3. Implemented tokenization schemes

#### MIDILike

Represents MIDI-like events directly:

- `NoteOn`;
- `NoteOff`;
- `Velocity`;
- `TimeShift`.

It preserves explicit onset and offset events but generally produces longer sequences (§4, p.4).

#### REMI

Represents notes using:

- `Pitch`;
- `Velocity`;
- `Duration`.

Time is represented with:

- `Bar`;
- `Position`.

REMI also supports optional chord and tempo information. MidiTok implements REMI+ functionality under the REMI tokenizer, including programs/instruments and time signatures (§4, pp.4–5).

#### Structured

Similar to MIDILike but imposes a fixed succession:

`Pitch → Velocity → Duration → TimeShift`

This gives stronger structural regularity than unconstrained event ordering (§4, p.4).

#### TSD

“TimeShift & Duration.” It is close to MIDILike but represents note lengths explicitly with `Duration` rather than relying on `NoteOff` events (§4, p.4).

#### Compound Word / CPWord

Groups several note attributes into a compound representation. Pitch, velocity, and duration embeddings are pooled into one representation, reducing the number of Transformer time steps while requiring multiple output heads (§4, p.4).

#### Octuple

Uses multiple vocabularies for note attributes such as:

- bar;
- position;
- pitch;
- duration;
- velocity;
- program and related attributes.

Each note becomes one pooled representation, so sequence length approaches the number of notes rather than the number of individual attribute tokens (§4, p.4).

#### MuMIDI

A multivocabulary representation related to Compound Word that also represents programs/instruments and uses bar/position information (§4, p.4).

#### MMM

Designed for multitrack music inpainting. MidiTok implements it using duration tokens (§4, p.4; Table 1, p.5).

---

### 4. Optional musical information

MidiTok lets users add tokens for (§5.1, p.5):

- **Chord:** harmony inferred from following notes;
- **Programs:** instruments;
- **Sustain pedal;**
- **Pitch bend;**
- **Tempo;**
- **Time signature;**
- **Rest:** silent time intervals.

This is particularly important for explainability: the representation can expose harmony, instrumentation, timing, and silence as separate semantic events rather than hiding everything inside a note ID.

The paper cites prior work reporting better human-preferred generation when tempo and chord tokens are included, but MidiTok itself does not provide a new controlled quality experiment for those choices (§5.1, p.5).

---

### 5. BPE implementation

MidiTok applies Byte Pair Encoding to the base symbolic vocabulary (§5.2, p.6).

Process:

1. each base token is mapped to a unique byte;
2. frequent consecutive byte sequences are learned from a MIDI corpus;
3. frequent sequences become new composite tokens;
4. the resulting tokenizer must be saved with the model.

BPE is implemented using Hugging Face’s Rust-backed `tokenizers` library. The paper presents BPE as an alternative to multi-vocabulary schemes:

- it preserves a single token stream;
- avoids multiple input/output modules;
- avoids combining several losses;
- can reduce Transformer sequence length substantially.

The trade-off is greater tokenization and detokenization overhead and reduced semantic transparency of composite tokens.

---

### 6. Quantitative benchmark results

Table 2 (§5.2, p.5) reports average vocabulary size, tokens per beat, and tokenization/detokenization times on the **MAESTRO** dataset.

#### TSD and REMI

| Strategy | Vocabulary | Tokens/beat | Tokenization time (s) | Detokenization time (s) |
|---|---:|---:|---:|---:|
| TSD, no BPE | 149 | 18.5 | 0.174 | 0.031 |
| REMI, no BPE | 162 | 19.1 | 0.151 | 0.039 |
| TSD, BPE 1k | 1k | 9.3 (**−49.5%**) | 0.187 | 0.053 |
| REMI, BPE 1k | 1k | 10.4 (**−45.3%**) | 0.163 | 0.063 |
| TSD, BPE 5k | 5k | 7.0 (**−62.2%**) | 0.181 | 0.053 |
| REMI, BPE 5k | 5k | 8.5 (**−55.2%**) | 0.165 | 0.064 |
| TSD, BPE 10k | 10k | 6.3 (**−66.0%**) | 0.183 | 0.052 |
| REMI, BPE 10k | 10k | 7.7 (**−59.7%**) | 0.164 | 0.065 |
| TSD, BPE 20k | 20k | 5.8 (**−68.9%**) | 0.184 | 0.052 |
| REMI, BPE 20k | 20k | 6.9 (**−63.9%**) | 0.163 | 0.063 |

#### Multivocabulary schemes

| Strategy | Tokens/beat | Tokenization time (s) | Detokenization time (s) |
|---|---:|---:|---:|
| CPWord | 8.6 (**−54.8%**) | 0.169 | 0.034 |
| Octuple | 5.2 (**−72.6%**) | 0.118 | 0.035 |

CPWord and Octuple are grouped with REMI in the paper because they represent time with Bar and Position tokens.

#### Interpretation

The strongest reported compression is:

- **Octuple:** 5.2 tokens/beat, −72.6%;
- **TSD with 20k BPE:** 5.8 tokens/beat, −68.9%;
- **REMI with 20k BPE:** 6.9 tokens/beat, −63.9%.

However, BPE increases preprocessing cost. For example, TSD tokenization rises from **0.174 s** to **0.184 s**, and detokenization from **0.031 s** to **0.052 s** at 20k BPE.

These are **representation-speed benchmarks**, not end-to-end model-quality results. The paper does not report perplexity, likelihood, generation quality, repair accuracy, or human preference comparisons between MidiTok configurations.

---

### 7. Other artifact features

#### Hugging Face Hub

MidiTok integrates with `huggingface_hub.ModelHubMixin` and exposes:

- `save_pretrained`;
- `load_pretrained`;
- `push_to_hub`.

The goal is to ensure that a trained model’s tokenizer configuration is shared alongside the model (§5.3, p.6).

#### Data augmentation

Augmentation operates at MIDI or token level, including:

- velocity changes;
- duration changes;
- octave pitch shifts.

The authors argue that augmentation helps models learn melody and harmony rather than corpus-specific token succession patterns (§5.4, p.6).

#### Dataset and collation utilities

The paper describes:

- `DatasetTok`: loads tokenized or MIDI data into RAM and splits sequences;
- `DatasetJsonIO`: streams token JSON files from disk;
- a data collator that pads sequences, adds BOS/EOS, shifts labels, and supports left padding for autoregressive generation;
- utilities for splitting long sequences.

Important limitation: `DatasetJsonIO` cannot split sequences while loading; splitting must occur beforehand (§5.5, p.7).

#### MIDI utilities

Additional utilities include:

- chord extraction;
- overlapping-note fixes;
- track merging by program or program category;
- bar counting;
- note deduplication (§5.6, p.7).

---

### 8. Code, license, and artifact status

#### Paper-era status

As of September 2023, the paper reports:

- more than **450 GitHub stars**;
- more than **50 forks**;
- approximately **100 daily repository visits**;
- approximately **900 PyPI downloads per week**;
- approximately **75,000 total downloads** since the first release (§6, p.7).

The paper describes MidiTok as fully implemented and open source (§8, p.7).

#### Repository status

The public repository is:

`https://github.com/Natooz/MidiTok`

The repository’s `LICENSE` is MIT. The package metadata and documentation expose a reusable Python package rather than merely a research prototype. The artifact is therefore primarily:

- source code;
- configuration serialization;
- documentation;
- tests/utilities;
- PyPI distribution;
- Hugging Face interoperability.

There is no new trained model, dataset, or benchmark corpus released as the paper’s central artifact. The MAESTRO benchmark is used for timing/sequence-length measurements, not introduced by the authors.

---

### 9. Limitations and caveats

1. **Lossy quantization.**  
   MIDI timing, velocity, duration, tempo, and pitch are discretized. Exact round-trip claims apply to the preprocessed MIDI, not the original file (§2.1, §3).

2. **Limited evaluation scope.**  
   The quantitative benchmark uses MAESTRO, principally piano performance data. Results may not transfer to dense multitrack, expressive orchestral, electronic, or mashup MIDI.

3. **No downstream quality evaluation.**  
   Table 2 measures sequence efficiency and runtime, not musical quality, repair correctness, interpretability, or task performance.

4. **BPE is corpus-dependent.**  
   A BPE vocabulary learned on one corpus may create opaque or poorly transferable units on another. The tokenizer must remain coupled to the model.

5. **Interpretability–compression trade-off.**  
   Octuple, CPWord, and BPE reduce sequence length, but compound representations make individual predictions less directly interpretable.

6. **Incomplete MIDI semantic coverage.**  
   The paper discusses MIDI categories including lyrics, key signatures, control changes, and pitch bend, but the documented optional-token set does not represent every MIDI event type. This matters for expressive-performance preservation and repair.

7. **No explicit repair constraints.**  
   Utilities fix some malformed MIDI conditions, but the package does not itself guarantee voice-leading, harmonic, rhythmic, or instrument-consistency constraints.

8. **Memory trade-offs.**  
   In-memory datasets are convenient but may become impractical for large corpora; JSON streaming requires preprocessing and pre-splitting.

9. **Potential data-augmentation leakage.**  
   Pitch, velocity, and duration transformations can change musical identity or create unrealistic examples if applied without genre- or instrument-aware constraints.

10. **Ethics and provenance.**  
    The ethics statement acknowledges risks of copying or altering artists’ work, but the paper does not provide a detailed copyright/provenance protocol for training MIDI corpora (§Ethics Statement, p.8).

---

### Relevance to explainable symbolic music AI

### Explainability strengths

MidiTok is unusually useful for explainable symbolic models because:

- tokens correspond to recognizable musical concepts;
- `Event` objects retain token type, value, time, and descriptions;
- explicit `Pitch`, `Duration`, `Velocity`, `Bar`, `Position`, `Chord`, `Program`, and `Tempo` tokens support semantic attribution;
- one can map a model prediction back to a precise note attribute or temporal event;
- tokenization configurations are serializable, making explanations reproducible.

A model can therefore explain a prediction as:

> “The next note was assigned pitch 67 because the current chord token is G major, the position is beat 3, and the preceding program is piano.”

### Explainability weaknesses

- BPE tokens may span several notes or heterogeneous events.
- CPWord/Octuple pooling moves semantic reasoning into embedding composition.
- Quantization hides microtiming and fine velocity differences.
- A token-level explanation may not correspond cleanly to a perceptual musical event.
- Multi-track ordering and global-event placement can affect explanations even when the sounding music is similar.

A practical explainability system should preserve both:

1. the compressed model token; and  
2. a provenance graph pointing back to original MIDI events, tracks, timestamps, and preprocessing operations.

---

### Relevance to mashup systems

MidiTok provides useful infrastructure for mashups:

- one-stream or per-track representations;
- program/instrument tokens;
- chord, tempo, and time-signature tokens;
- track merging by program;
- pitch-shift augmentation;
- explicit bar/position alignment.

A mashup model could use separate track streams for source songs, then align them through shared Bar/Position/Tempo representations. Programs and chord tokens provide interpretable controls for deciding which instruments or harmonic regions to preserve.

Important risks:

- quantization can destroy subtle groove alignment;
- independent source tempos may be normalized incorrectly;
- BPE may encode source-specific phrases rather than transferable musical units;
- naïve track merging can create collisions between instruments, programs, or note ranges.

---

### Relevance to symbolic repair

MidiTok is especially relevant to repair because it exposes the structure of common MIDI defects:

- missing `NoteOn`/`NoteOff`;
- incorrect duration;
- duplicated notes;
- overlapping notes;
- timing gaps;
- inconsistent program or track assignments;
- malformed rests or tempo events.

MMM’s explicit connection to multitrack inpainting is particularly relevant (§4, p.4).

However, the paper does not evaluate repair. A repair model would need additional constraints for:

- valid note pairing;
- nonnegative and bounded durations;
- instrument consistency;
- polyphonic overlap policy;
- harmonic plausibility;
- preservation of expressive timing;
- minimal-edit behavior.

---

### Concrete research ideas

1. **Tokenization-aware repair benchmark**  
   Create synthetic corruptions—deleted notes, shifted onsets, wrong durations, duplicated events, missing programs—and compare MIDILike, TSD, REMI, CPWord, Octuple, and MMM on exact repair and perceptual metrics.

2. **Provenance-preserving explainable tokenizer**  
   Extend `TokSequence` with original MIDI event IDs, track IDs, source timestamps, quantization deltas, and preprocessing decisions. Report explanations in original musical coordinates rather than only token IDs.

3. **Protected-semantic BPE**  
   Learn BPE while forbidding merges across boundaries such as:
   - bar boundaries;
   - chord changes;
   - instrument/program changes;
   - note onset versus duration fields.  
   Measure whether this preserves interpretability while retaining the sequence-length gains in Table 2.

4. **Mashup alignment model**  
   Use REMI/REMI+ with explicit tempo, time signature, program, and chord tokens. Train a model to align two source MIDI streams and produce explanations for:
   - tempo normalization;
   - key/harmony compatibility;
   - instrument selection;
   - conflict resolution.

5. **Counterfactual explanation through augmentation**  
   Use controlled octave, velocity, and duration transformations to test whether model explanations track meaningful musical invariances rather than token-frequency artifacts.

6. **Round-trip fidelity benchmark**  
   Quantify the difference between original MIDI and detokenized MIDI across:
   - timing;
   - velocity;
   - duration;
   - pedal;
   - pitch bend;
   - tempo;
   - control changes.  
   This would directly expose what is lost by each configuration.

7. **Hybrid event/attribute representation**  
   Use explicit interpretable tokens for rare or semantically important events, while applying BPE only to repetitive note patterns. Compare repair accuracy and explanation quality against pure BPE and pure REMI.

8. **Constraint-guided decoding**  
   Combine MidiTok’s token-type structure with a decoder that masks invalid transitions, e.g. impossible duration ordering, unmatched note-offs, invalid program changes, or structurally inconsistent multitrack events.

### Bottom line

MidiTok is a strong **engineering and reproducibility contribution**: flexible, modular, and well suited as a common substrate for symbolic-music experiments. Its most important research value for explainable AI is the bridge between model tokens and interpretable musical events. Its main weakness is that the paper evaluates representation efficiency rather than downstream musical quality, explanation fidelity, mashup quality, or repair correctness.

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
