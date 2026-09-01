# LLM Wiki — Explainable and Transparent AI for Generative Music

A personal knowledge base of papers on explainable and transparent AI for generative music, with an emphasis on symbolic classical music, explicit music-theory knowledge, auditable generation, and human evaluation, following [Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/1dd0294ef9567971c1e4348a90d69285):

```
Original PDF → sources/*.md → wiki/{category}/*.md → wiki/overviews/ + wiki/concepts/
```

Language policy: all wiki content is in English. Conversation can be in any language.

Scope and evidence policy: organize papers by their primary methodological contribution, use tags and synthesis links for secondary topics, and preserve the difference between a paper's claims, independently verified evidence, and repository inference. Local possession of a PDF does not establish redistribution rights. Until repository visibility and artifact rights are decided, do not publish or push PDFs whose redistribution status is restricted or unknown.

This file is the single source of truth for how agents work in this folder. Claude Code and Codex both read it. If `CLAUDE.md` is added, keep it as a symlink to this file (`ln -s AGENTS.md CLAUDE.md`) and keep the wording agent-neutral.

---

## Startup checklist

At the start of every session in this folder, before acting on any ingest, search, or synthesis request:

1. Re-read this file.
2. Re-read `index.md`, `logs/README.md`, and any applicable operational decisions under `agenda/llm-wiki-ops/` when they are present.
3. Do not rely on memory from a previous session for anything that moves.

---

## The rules

### The four core rules

1. No web search. Never use `WebSearch` or `WebFetch` to fill a gap. Every answer must be grounded in papers actually present here. Use them only when the user explicitly asks, for that one task.
2. Answer from the wiki first. `sources/` and `wiki/` are the only sources of truth.
3. If the wiki is insufficient, re-read the original PDF in `papers/` and extract more detail. Then update the wiki so the next question does not need the PDF.
4. If no paper exists on the topic, say so: "I don't have a paper on this — please give me the PDF." Do not improvise.

These apply to every response, overview pages included: cite only papers that exist in this wiki.

### Five more rules

5. A paper is not ingested until it is connected to the synthesis layer. See "The synthesis requirement" below.
6. No tiers, no placeholder pages. Every admitted paper meets the same standard: read from the original, with concrete methods, results, limitations, and synthesis links. Never create a page from an abstract, a metadata record, a reference-list mention, or a filename. If the original cannot support a complete page, leave the paper out and record the gap in the day's log.
7. Exhaustive means exhaustive. When the user asks for all of something, process the whole set before reporting. State the denominator and the numerator. Count extraction failures, empty text, and timeouts as unchecked, not as passing. Never sample and report as if you surveyed. Never negotiate the scope down because it is large — start, checkpoint, and finish.
8. Confidential material stays out of `wiki/`. Unpublished manuscripts, drafts under review, and embargoed work must not appear in `wiki/` at all — not as a page, not as a title, not as a tag, not as a "relevance to our manuscript" section on a published paper's page. Those notes go in `agenda/`. Published work with a DOI is ordinary wiki content.
9. PDFs only. The canonical full text of a paper is an exact PDF in `papers/`. Never save publisher HTML or a browser text snapshot as a substitute. If an exact PDF cannot be obtained, keep the paper on a missing-PDF list rather than ingesting a degraded copy.

Also: correction, erratum, and retraction notices are not papers. Titles beginning `Author Correction:`, `Publisher Correction:`, `Correction:`, `Erratum`, or `Retraction` never get a page. Match the correction word only when followed by `:` or `to`, so real papers about correcting something survive.

No publisher or venue is excluded by default. Evaluate papers on relevance, methodological quality, evidence, publication status, and correction or retraction status. If an exclusion policy is later adopted, document it in `agenda/llm-wiki-ops/` and enforce it with both a DOI-prefix sweep and a body-text scan; a preprint DOI can pass a DOI check even when the paper was published in an excluded venue.

---

## Repository structure

```
phd-paper-repository/
├── AGENTS.md               # This file; CLAUDE.md, if used, is a symlink to it
├── index.md                # Generated catalog: categories, page counts, synthesis coverage
├── indexes/                # Generated per-category page listings
├── logs/                   # Daily work logs — the narrative record
│   ├── {YYYY-MM-DD}-{agent}-{host}.md
│   ├── README.md           #   generated folder guide and topic index
│   └── reports/            #   audit reports written for a person to read
├── scripts/                # Extraction, validation, index and log builders
├── papers/                 # Original PDFs, canonical storage (copy, never symlink)
├── papers-supplementary/   # Publisher supplements + manifests
├── sources/                # PDF summaries, English
├── wiki/                   # Knowledge layer, English; Obsidian vault root
│   ├── {category}/
│   ├── concepts/
│   ├── overviews/
│   └── questions/
├── agenda/                 # Project execution notes, plans, handoffs, unpublished work
└── materials/              # Non-paper reference material
```

### The three synthesis layers

- `overviews/` — encyclopedic topic pages. Declarative noun-phrase titles. Never a question title.
- `concepts/` — stable definitions, methods, mechanisms. Written once, pointed at by many paper pages.
- `questions/` — paper-anchored research questions. The title is a question; the body has `## Question`, `## Sharper follow-up`, `## What the knowledge base holds`, `## Tentative answer`.

A question-form synthesis page belongs in `questions/`, never in `overviews/`.

### `agenda/`

`agenda/{project-or-context}/` holds work-facing notes: execution plans, handoff documents, analysis backlogs, decision records, meeting follow-ups, training material, and notes on unpublished manuscripts. No schema requirements.

A handoff document includes: why the method or paper is needed and what it enables, the analyses to run, the expected results, a decision section stating when to continue or pause or stop if results are weak, and the concrete deliverables. No agent-workflow notes, no personal absolute paths, no relative-date titles.

Put durable decisions about how this wiki operates in `agenda/llm-wiki-ops/` as short ADR-style notes.

### `materials/`

Non-paper reference material, with no filename convention, no category, and no PDF frontmatter requirement: journal scope and author-guideline snapshots, writing-style profiles, lecture notes, curated meeting notes, professional-activity records.

Do not link `materials/` from `wiki/`, `sources/`, or `index.md`. It is outside the paper knowledge graph by design. Keep raw audio and raw transcripts outside this repository entirely; only curated notes come in.

---

## File naming convention

All three tiers (PDF, source, wiki) share one stem:

```
{first-author-lastname}-{year}-{first-5-title-tokens}.{ext}
```

- Tokens, not words. Lowercase the title, then take runs of alphanumerics. Every non-alphanumeric character is a separator: `self-report` is two tokens. Digits count.
- Year is 4 digits. Consortium papers use the consortium name.
- Let the ingest script generate the stem. Do not hand-build it.
- Do not bulk-rename legacy stems to match a newer rule — every wikilink and index entry would have to follow. Fix only the cases where one paper's three tiers disagree with each other.

Example: `wu-2026-an-automated-pop-song-mashup`

---

## Categories

Start with these six method- or contribution-based domain categories. Split one only when it passes roughly 500 files. For a borderline paper, use its primary methodological contribution as the category and represent cross-cutting topics with tags and synthesis links.

| Category | Includes |
|---|---|
| `data-and-representation` | Corpus construction, licensing and provenance, deduplication, symbolic or audio encodings, tokenization, and score representations; excludes papers whose main contribution is a model architecture using an established representation. |
| `generation-and-planning` | Generative architectures, pretraining, long-context modeling, hierarchical planning, infilling, and diffusion; excludes papers centered on explicit theory constraints or explanations. |
| `theory-and-constraints` | Formal music-theory rules, computational analysis, neuro-symbolic guidance, constraint satisfaction, verification, and repair; excludes descriptive musicology without a computational method and generic generation evaluated only with theory-derived metrics. |
| `explainability-and-auditability` | Faithful decision traces, causal or mechanistic interpretability, evidence-grounded explanations, attribution, provenance, uncertainty, and auditability; excludes controllability without an explanation or faithfulness claim. |
| `retrieval-and-recombination` | Music similarity, compatibility scoring, retrieval, alignment, mashups, source-preserving transformation, and recombination; excludes unconstrained generation from scratch. |
| `interaction-and-evaluation` | Co-creative interfaces, controllable editing, MIDI question answering, human studies, perceptual or behavioral evaluation, creativity and coherence metrics, and explanation utility; excludes routine evaluation that is secondary to another paper's main method. |
| `concepts` | Methods, mechanisms, reusable definitions. |
| `overviews` | Encyclopedic synthesis pages. |
| `questions` | Paper-anchored research-question pages. |
| `other` | Cross-cutting work whose primary methodological contribution does not fit a domain category; document why no specific category applies. |

Classify by method, not topic: a theory-constrained generator goes to `theory-and-constraints`, not `generation-and-planning`, when its primary contribution is the constraint method. Write and preserve exclusions — asking what to deliberately leave out is what keeps categories from blurring.

---

## Adding a paper

### Step 0 — locate the PDF

If the user did not give a path, look in the current user's `Downloads` directory. Identify each file from its first page (title, authors, DOI). If a mapping is ambiguous, ask instead of guessing. Never move, delete, or overwrite files in the user's directories.

### Step 1 — copy to `papers/` and extract text

Copy, never symlink. `pdf_path` is always an absolute path inside `papers/`; `pdf_filename` matches its basename. Never put an external path in `pdf_path`.

Default extractor is [opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf): it reconstructs two-column paragraphs as continuous prose, separates figure captions, tidies references, and strips page furniture, where simpler extractors interleave figure-panel scaffolding into the body. It needs Java. Wrap it in a helper that discovers a working Python 3.12 and Java on the current machine, applies a timeout, and falls back to `pypdf` then `pdftotext`.

```bash
pdfinfo "/path/to/paper.pdf" | grep Pages          # check length first
bash scripts/extract_pdf_text.sh "/path/to/paper.pdf" 1-25 400000
```

The arguments are a page range and a character cap. A small character cap truncates the paper mid-Methods and still reports success. Be generous with the cap and widen the range for long PDFs.

For music-object or relation extraction rather than summarization, PyMuPDF is the better tool when its layout behavior has been validated for the paper: it keeps columns pure, needs no Java, and is much faster.

Clean the raw output with a bounded contract — list exactly what may be removed (page furniture, running headers, line-break hyphenation, empty pseudo-tables) and remove nothing else.

Record the provenance. Mandatory on every new or re-extracted record:

```yaml
source_format: pdf
text_extractor: opendataloader-pdf-{version}
text_extracted_date: YYYY-MM-DD
```

Never ingest without naming the tool. Update these fields on re-extraction, and note the re-extraction in the day's log rather than in the page body. Do not invent values for legacy records that lack them.

### Step 2 — write `sources/{stem}.md`

```yaml
---
title: "Paper Title"
authors: Author List
year: YYYY
doi: DOI
category: {category-slug}
pdf_path: /absolute/path/to/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: publisher-or-repository-collection
source_format: pdf
text_extractor: opendataloader-pdf-{version}
text_extracted_date: YYYY-MM-DD
---

## One-line Summary
## 1. Document Information
## 2. Key Contributions
## 3. Methodology and Architecture
## 4. Key Results and Benchmarks
## 5. Limitations and Future Work
## 6. Related Work
## 7. Glossary
```

Replace `{category-slug}` with exactly one domain category from the table above. Use tags and synthesis links for secondary contributions.

That section list is the whole schema. Do not add a section holding the raw extraction dump — the canonical full text is the PDF, and copying it in drags publisher boilerplate into the search index.

`source_collection` names a stable source class such as a publisher or repository collection. Processing metadata is forbidden in paper frontmatter: no `tier`, no `curation_level`, no batch or run names, no agent names, no dated batch identifiers, no status tags. Batch processing is an execution strategy and must be invisible in the knowledge layer; run provenance belongs in the log.

### Step 3 — write `wiki/{category}/{stem}.md`

```yaml
---
title: "Exact English Title"
authors: Author list
year: YYYY
doi: DOI
source: {stem}.md
category: {category-slug}
pdf_path: /absolute/path/to/papers/{stem}.pdf
pdf_filename: {stem}.pdf
source_collection: publisher-or-repository-collection
source_format: pdf
text_extractor: opendataloader-pdf-{version}
text_extracted_date: YYYY-MM-DD
tags: []
---

## Summary
## Key Contributions
## Methodology and Architecture
## Results
## Related Papers
- [[overviews/some-page]] — relationship
```

Replace `{category-slug}` with exactly one domain category from the table above. Use tags and synthesis links for secondary contributions.

### Step 4 — connect to the synthesis layer

Mandatory. See the next section.

### Step 5 — log it, then rebuild the indexes

Append one entry to the day's log file with a topic slug in the heading, then regenerate the catalog and the log index:

```bash
python scripts/build_hierarchical_index.py --all --apply
python scripts/build_logs_index.py --apply
```

Do not put ingest narrative into `index.md`.

---

## The synthesis requirement

A source and wiki pair with no link into `overviews/` or `concepts/` is a synthesis-orphan. It behaves like a RAG cache entry, not a wiki, and defeats the purpose of the system. Every ingest, routine ones included, must end with:

1. At least one bidirectional link between the new page and the single most relevant existing overview or concept page — `Related Papers` on the paper, `Related Pages` on the synthesis page. One-way links are invisible from the side that would use them.
2. One sentence in that synthesis page's body placing the paper in context. Not just a bullet in a list. If the paper only restates what the page already says, a link is enough, but say so in the log.
3. A supersede check: does the paper strengthen, narrow, contradict, or replace an existing claim? If it contradicts or replaces one, append a `supersede` entry to the day's log.
4. If no overview or concept covers the topic, record the gap in the day's log instead of skipping silently. Create the anchor when the topic is clearly recurring.

Audit the drift with a read-only script that lists orphans. That list is the backlog.

### High-impact mode

When a paper can change an active argument, review, benchmark interpretation, or project decision:

- Process one paper, or a very small set, at a time.
- Read the relevant existing synthesis pages before writing.
- Update the overview and concept page bodies, not just the links.
- Create the concept anchor if one is missing.
- State the claim delta explicitly: strengthen, narrow, contradict, replace, or unchanged.
- If the paper's conclusion lives in a figure (heatmap direction, effect-size plot, architecture diagram), render that figure to PNG and read it as an image rather than trusting text extraction.
- If the right emphasis is unclear, ask for a short interpretation checkpoint rather than burying the decision inside a batch.

---

## Batch ingest

Batch size never changes who writes the pages: the active agent in the current conversation reads each paper and writes each source and wiki page. Do not spawn another model CLI or model API from an ingest script. Local scripts do deterministic extraction, metadata checks, validation and repair, logging, and index rebuilds — nothing else.

1. Fix the total count first. Identify title, authors, DOI, and document type from a one-page extraction.
2. Check for duplicates by DOI across all of `sources/` and `wiki/`.
3. Filter out correction notices and excluded venues, then copy the survivors into `papers/` under the naming convention.
4. Extract full text and write complete, original-grounded source and wiki pairs.
5. Add synthesis links and context sentences for every paper, and run the supersede check.
6. Run the closing sweeps and the validator. Extraction failures, empty text, and timeouts count as unchecked, not as passing.
7. Report so that completed plus excluded plus unchecked equals the starting count, and append it to the day's log.
8. Rebuild the generated Markdown catalogs. Leave routine BM25 freshness to the next scheduled local rebuild; run an immediate rebuild only when the user needs the new pages to be searchable now.

Closing sweeps must return zero matches before the batch is done — a title-based filter in step 3 leaks, because a preprint DOI passes a publisher-DOI check even when the paper was published in an excluded venue. Scan the body text as well as the DOI.

---

## What the extractor gets wrong

Every one of these reports success:

- Glyphs substituted rather than dropped, especially Greek letters in proper nouns.
- Minus signs lost. Undetectable from the text alone. If a sign matters, look at the PDF.
- Table columns reordered or merged, binding numbers to the wrong label.
- Figure reading order scrambled, binding values to the wrong axis label. Color is never extracted at all.
- The body silently emptied on some font runs. Corruption is per font run, not per file — a spot check on one page proves nothing about another.
- Tables that are images: invisible even to a missing-content check.
- Zero-width spaces triggering false alarms in completeness checks.
- Superscripts flattened. A layout failure, so font tools do not warn.
- Another paper appended to the end of the PDF, silently merged into one.

Two working rules: check which tool actually produced the text, because a failing extractor may fall back silently; and never run a corruption-repair substitution table in reverse, which corrupts clean text at scale and is far harder to detect than the original problem.

---

## Logs

There are no commit messages here, so the log is the only narrative record of what changed and why. One Markdown file per day, per agent, per machine:

```
logs/{YYYY-MM-DD}-{agent}-{host}.md
```

`{agent}` is `claude` or `codex`. `{host}` distinguishes machines that share this folder — resolve it by running a command, never from memory. Several files may coexist for one day; never write into another agent's or machine's file.

Frontmatter, then the title, then append-only entries, oldest first:

```markdown
---
date: YYYY-MM-DD
agent: codex
host: {resolved-hostname}
model: {model-name}
---

# YYYY-MM-DD — Codex work log ({resolved-hostname})
```

Entry headings carry a kind and a topic slug so one campaign can be followed across days, agents, and machines:

```
## [YYYY-MM-DD] ingest | {topic} | Paper or batch title
## [YYYY-MM-DD] maintenance | {topic} | Task
## [YYYY-MM-DD] query-to-wiki | {topic} | Result page
## [YYYY-MM-DD] semantic-lint | {topic} | Scope
## [YYYY-MM-DD] supersede | {topic} | Claim or page
```

A topic slug is lowercase letters, digits, and hyphens. Read the existing topic table before inventing one — a near-duplicate slug splits a campaign in two and neither half looks incomplete.

Directly under the heading, add whichever index lines apply, then a blank line, then the narrative. Write only what the entry actually did:

- `targets:` records or paths this entry changed
- `scripts:` scripts this entry ran
- `report:` the report page this entry produced
- `model:` only when it differs from the file's frontmatter

Generate `logs/README.md` from the headings; never hand-edit it. Keep reports in `logs/reports/` — a dated report sitting beside dated daily logs gets read back as a log.

---

## Query-to-wiki

When a question produces a reusable comparison, analysis, decision framework, or handoff-quality synthesis, file it back instead of leaving it in chat:

- `wiki/overviews/` — research-facing literature synthesis.
- `wiki/concepts/` — stable definitions, methods, mechanisms.
- `wiki/questions/` — an open question with the evidence currently available.
- `agenda/{project-or-context}/` — execution plans, handoffs, operational notes.

Save only durable outputs a future reader would search for, not every casual answer.

---

## Search and health checks

- `rg` for exact strings across `wiki/`, `sources/`, `agenda/`, `scripts/`.
- Once the wiki passes roughly 500 pages, use a pinned, memory-mapped `bm25s` index built directly from `wiki/**/*.md` as the default candidate generator. QMD or another vector index is an optional semantic fallback, not an upstream dependency of the default index.
- Exclude `wiki/questions/` from retrieval results by default. Search evidence-bearing paper, overview, and concept pages instead of returning the query-shaped page derived from the same question.
- Use a complete English research question as the BM25 query. For a non-English question against an English corpus, preserve the original question and supply a complete English rewrite; do not reduce it to three keywords.
- Retrieval scores identify candidates only. Read the page and, when necessary, its source summary or canonical PDF before making a claim. Abstain when the retrieved text does not explicitly support the requested relationship.
- Run the validator before and after any large ingest or reorganization. It should check YAML frontmatter, PDF path existence, source-to-wiki references, broken wikilinks, category drift, duplicate titles, forbidden ingest metadata, empty required sections, and placeholder prose.

Two validator findings need the right fix. A section containing only an instruction to consult the original, and a page describing its own processing status, both mean the record was never properly built: re-ingest it from the PDF or drop it. Deleting the offending line is the wrong fix — it leaves an empty section that reads as a complete one and is invisible to every text check afterward.

### Retrieval index policy

Pin the runtime (`bm25s==0.3.10`, `PyStemmer==3.1.0`) and expose one sanctioned interface:

```bash
# One-time on each machine: runtime, first index, local scheduled rebuild
bash scripts/setup_llm_wiki_retrieval.sh

# Default search
bash scripts/search_llm_wiki.sh "full English research question" --json

# Non-English question against an English corpus
bash scripts/search_llm_wiki.sh "original question" \
  --english-query "complete English research-question rewrite" --json

# Immediate freshness only
bash scripts/reindex_bm25s.sh
```

Rules:

1. Every machine keeps its runtime, index versions, build lock, and success stamp outside the synced repository. Never put a live retrieval index or lock in cloud storage.
2. A scheduled rebuild reads the current `wiki/**/*.md` tree but writes only machine-local state, so every machine may run its own job independently. Do not rebuild after every ingest.
3. Build a complete version first; validate the document count, deterministic corpus hash, memory-mapped load, and a non-question smoke query; then atomically switch `current`. Retain the previous complete version for rollback. Never edit index files in place.
4. Semantic fallback processes must be serialized locally and must treat an unexpectedly empty result as a health failure. Do not run concurrent vector or hybrid processes against a backend known to initialize shared accelerator state.
5. Use semantic fallback for ambiguous lexical retrieval, source/agenda collection navigation, or decomposed multi-document questions. It does not control BM25 freshness.

---

## Wikilinks and Obsidian

The Obsidian vault root is `wiki/`, not the repository root. Every `[[...]]` target is vault-root-relative with no `wiki/` prefix:

- Correct: `[[overviews/some-page]]`, `[[concepts/some-method]]`
- Wrong: `[[wiki/overviews/some-page]]`

Inside a `wiki/`-rooted vault, the prefixed form resolves to `wiki/wiki/...`, which does not exist, and Obsidian creates an empty ghost page there every time the link is opened. Link-checking scripts accept both forms, so they will not catch a reintroduced prefix — keep it out by hand.

Do not create an `.obsidian/` directory at the repository root. Its presence is what makes a tool assume the wrong vault root; the only vault config lives at `wiki/.obsidian/`.

---

## Housekeeping

- No scratch folders inside this repository. Temporary artifacts, text dumps, conversion output, and debug files go to the current user's temporary directory. Delete tool caches that appear.
- Supplements never go in `papers/`, which holds exactly one canonical PDF per paper. They go in `papers-supplementary/` with a manifest recording what each opaque publisher filename actually contains. Do not keep peer-review files, decision letters, or blank checklists — but do keep an author-written reporting summary, which often holds the power analysis, exclusion criteria, blinding, software versions, and demographics found nowhere else. Stop the extraction page range before it so its blank boilerplate never reaches a page.
- Never use `path` as a shell variable name. In zsh it is a special array tied to `PATH`, and assigning to it can break command lookup mid-script. The same goes for `HOME`, `IFS`, `SHELL`, `PWD`, and `RANDOM`.
- If you use git, keep the `.git` directory outside any cloud-synced folder. A sync conflict on the git index can stage hundreds of healthy files as deletions.

---

## Design principles

- Four tiers: raw PDF (immutable), `sources/`, `wiki/{category}/`, synthesis layer.
- English only in wiki content, for writing and retrieval.
- Obsidian compatible: `[[wikilinks]]`, plain Markdown.
- Consistent YAML in every paper record, extraction provenance included.
- No web search, no placeholders, no unconnected pages.

When in doubt, follow rule 1.
