# SynTheory Artifact Review and Result-Validity Caveats

Reviewed on 2026-09-06. **Current decision: ingest with explicit result-validity caveats, following the user's instruction to continue and record the discrepancies.** The initial ingestion hold is superseded by that task-specific instruction. The released evaluation implementation has a validation-preprocessing problem and does not strictly implement the paper's unseen-tempo split. Their numerical impact on the published results is unknown. This operational report supports the [admitted paper page](../../wiki/explainability-and-auditability/wei-2024-do-music-generation-models-encode.md) and [complete source digest](../../sources/wei-2024-do-music-generation-models-encode.md).

## Paper and Evidence Identity

- **Paper:** Megan Wei, Michael Freeman, Chris Donahue, and Chen Sun, *Do Music Generation Models Encode Music Theory?* (ISMIR 2024), supplied as arXiv `2410.00872v1`.
- **Exact input:** [root-level PDF](../../../2410.00872v1.pdf), eight physical pages. Page 1 identifies the conference and carries a CC BY 4.0 notice.
- **PDF SHA-256:** `9f25a57800d48876f6f801561387771906ffe6480e983e3966fd35ae37b8ce05`.
- **Author-linked implementation:** [brown-palm/syntheory](https://github.com/brown-palm/syntheory), inspected at commit `4f222359e750ec55425c12809c1a0358b74fce49`. Findings below concern this revision, not an assumed historical experiment revision.
- **Other paper-linked artifacts:** [Hugging Face dataset](https://huggingface.co/datasets/meganwei/syntheory) and [project website](https://brown-palm.github.io/music-theory/). Both pages were inspected; audio assets were not downloaded or listened to. The dataset card labels the release MIT. This does not independently verify every soundfont or asset's rights.
- **Extraction:** Citra 5.0.0, `rust-read-pdf-v1`, returned all eight pages as full text, but collapsed word spacing and interleaved columns. Poppler/MiKTeX layout extraction supplemented that reading. Its process emitted a log-permission failure even though it wrote readable output; it is not recorded as a clean command success. The rendered Table 2 was inspected visually.

## Why This Paper Matters

The paper proposes SynTheory, a synthetic MIDI/audio benchmark of tempo, meter, pitch class, intervals, modes, chord quality, and chord progressions. It trains probes on frozen Jukebox and MusicGen representations and compares their scores with handcrafted acoustic features. This could supply a diagnostic step between semantically named music representations and claims about musical knowledge. However, recoverability by a probe does not establish causal use during generation, successful concept editing, or useful explanations for musicians. [PDF pp. 1–6]

The paper reports mean scores of `0.984` for Jukebox, `0.950` for MusicGen Small, `0.914` for Medium, `0.929` for Large, and `0.936` for aggregate handcrafted features. These are averages mixing six classification accuracies with tempo regression R², not overall classification accuracy. Table 2 was visually checked, but the experiments were not reproduced. The table explicitly describes validation-based selection; it should not be relabeled as independently verified test performance. [PDF p. 6, Table 2]

## Confirmed Implementation Findings

### 1. Validation features enter normalization before the first training update

The released training path creates an unfitted `StandardScaler`, initializes `step = 0`, and performs early-stopping evaluation at step zero. That evaluation calls `self.eval("valid")`. Inside `eval_logits`, an unfitted scaler triggers `partial_fit(X)`, where `X` is the validation feature matrix. Subsequent training batches continue updating the same scaler. This is feature-distribution leakage into preprocessing, not a demonstrated leak of validation labels into gradient updates.

Evidence: [probe/probes.py, training and evaluation](https://github.com/brown-palm/syntheory/blob/4f222359e750ec55425c12809c1a0358b74fce49/probe/probes.py#L340), especially lines 341–377, 429, and 450–455; [default early-stopping configuration](https://github.com/brown-palm/syntheory/blob/4f222359e750ec55425c12809c1a0358b74fce49/probe/probe_config.py#L100).

Verification executed the actual `eval_logits` function extracted with Python AST, using explicit scaler and torch test doubles. Before any model inference, its calls were:

```text
transform(VALIDATION_FEATURES)
partial_fit(VALIDATION_FEATURES)
transform(VALIDATION_FEATURES)
```

This verifies the branch and data ownership. It is not a numerical scikit-learn test or an end-to-end training run. The paper does not disclose this validation-dependent normalization. It affects the evaluation procedure underpinning the central comparisons and prompted the initial hold; its effect size and direction remain unmeasured and must remain explicit when citing the results.

### 2. The unseen-tempo split shares two BPM values with training

The paper says training uses the middle 70% of BPM values, while validation/test use the extremes to assess unseen-BPM generalization. [PDF p. 4, Section 4.1]

The code instead sorts all sample rows and slices at 15% and 85% of the row count. With 161 BPM values and 25 samples per value, those cuts fall inside the groups for **74 BPM and 186 BPM**. Therefore both values occur in training and in the combined validation/test pool.

Evidence: [split code](https://github.com/brown-palm/syntheory/blob/4f222359e750ec55425c12809c1a0358b74fce49/probe/probes.py#L192) and [tempo generator](https://github.com/brown-palm/syntheory/blob/4f222359e750ec55425c12809c1a0358b74fce49/dataset/synthetic/tempos.py).

An independent standard-library reproduction of those exact row boundaries returned:

```text
total rows: 4025
lower cut: 603; upper cut: 3421
training rows: 2818; combined holdout rows: 1207
shared BPM values: [74, 186]
```

This is a bounded discrepancy: it does not mean every held-out tempo is seen during training. It does mean that the released split is not strictly BPM-disjoint as described.

### 3. The released runner does not demonstrate independent test scoring

`start()` calls `load_data()` and `train()`, then returns. The experiment's internal evaluation calls use `"valid"`; `save_metrics()` also evaluates `"valid"`. The supplied runner does not call `eval("test")`, despite creating a test split.

Evidence: [probe/main.py](https://github.com/brown-palm/syntheory/blob/4f222359e750ec55425c12809c1a0358b74fce49/probe/main.py) and [metric persistence](https://github.com/brown-palm/syntheory/blob/4f222359e750ec55425c12809c1a0358b74fce49/probe/probes.py#L578). AST inspection found the two experiment-level evaluation calls at lines 377 and 580, both targeting validation.

This is a reproducibility gap, not proof that the authors never evaluated a test set elsewhere. Table 2's caption already refers to validation-based selection. An unreleased analysis or a different experiment revision may explain the final numbers; neither was available in the inspected release.

## Additional Bounded Differences

- The chord-progression generator defaults to two beats per chord at 120 BPM, whereas the paper describes quarter-note chord playback. See [generator lines 75–98 and 159](https://github.com/brown-palm/syntheory/blob/4f222359e750ec55425c12809c1a0358b74fce49/dataset/synthetic/chord_progressions.py#L75). This changes stimulus timing; published audio was not analyzed to determine which version it follows.
- Sweep configurations declare `goal: minimize` for accuracy/R², although those metrics should increase. The search is a grid and the training loop itself maximizes its early-stopping score, so this metadata alone does **not** establish that Table 2 selected the worst models. See [sweep definitions](https://github.com/brown-palm/syntheory/blob/4f222359e750ec55425c12809c1a0358b74fce49/probe/probe_config.py#L34).

## Decision and Conditions for Stronger Result Claims

The applicable [AGENTS.md artifact rule](../../../AGENTS.md) says: “If there are significant discrepancies between what is reported in the paper and what is actually done in code, or if the difference affects a major result in the paper, this difference should be recorded and reported. You should not continue on digesting this paper.”

The initial review applied that rule and paused admission. The user subsequently explicitly instructed continued ingestion with the discrepancy recorded because it might affect result validity. That task-specific authorization takes precedence for this paper; it is not a general change to AGENTS.md. The PDF is now copied into canonical storage, and complete source/wiki pages and reciprocal concept links are present. The original root file remains unchanged. Synthesis adds the probing method while preserving all validity concerns; it does not treat the numerical ranking as independently verified.

To strengthen confidence in the results, obtain the exact experiment revision and run/export provenance, then establish whether it used the released preprocessing and splits. If so, fit preprocessing on training data only, freeze it for evaluation, split tempo by unique BPM, select probes/layers on validation, and score the selected configurations once on an untouched test set. Compare corrected per-task scores and model rankings with Table 2. If the findings remain stable, record that additional evidence; if they materially change, revise the result interpretation and linked synthesis claims.

Concrete deliverables needed: a revision/run mapping, exact split manifests, a corrected evaluation configuration, per-task results with uncertainty, and clarification of chord-progression timing. No author contact or expensive model rerun was performed in this review.
