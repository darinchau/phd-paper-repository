---
title: "MusicAgent: An AI Agent for Music Understanding and Generation with Large Language Models"
authors: "Dingyao Yu, Kaitao Song, Peiling Lu, Tianyu He, Xu Tan, Wei Ye, Shikun Zhang, and Jiang Bian"
year: 2023
doi: 10.48550/arXiv.2310.11954
category: interaction-and-evaluation
source: yu-2023-musicagent-an-ai-agent-for.md
pdf_path: "C:/Users/User/Documents/Repository/phd-research/projects/phd-paper-repository/papers/yu-2023-musicagent-an-ai-agent-for.pdf"
pdf_filename: yu-2023-musicagent-an-ai-agent-for.pdf
source_collection: arxiv
source_format: pdf
extracted_date: 2026-10-11
tags: []
---
## Summary

“**MusicAgent: An AI Agent for Music Understanding and Generation with Large Language Models**.” arXiv:**2310.11954v2**, [cs.CL], **25 October 2023**. Authors are affiliated with Peking University and Microsoft Research Asia. The paper identifies its code repository as:

## Key Contributions

Core contribution and architecture

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

The selector returns a tool ID and a textual reason for the selection.

The complete evidence-grounded digest is in [`sources/yu-2023-musicagent-an-ai-agent-for.md`](../../sources/yu-2023-musicagent-an-ai-agent-for.md).

## Methodology and Architecture

Read the linked source digest for the paper's full method, equations, implementation details, and page/section anchors.

## Results

The linked source digest preserves the paper-reported results and their evidence boundaries; this page does not claim an independent reproduction.

## Related Papers

- [[overviews/2026-symbolic-music-literature-map]] — primary synthesis anchor for this batch; the overview places this paper beside related representation, generation, evaluation, and auditability work.
