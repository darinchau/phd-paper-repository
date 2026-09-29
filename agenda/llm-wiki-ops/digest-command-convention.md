# Digest command convention

## Decision

When the user says **“digest”** in a future request, interpret it as an instruction to ingest the named paper into `phd-paper-repository` according to `AGENTS.md`: obtain and preserve the canonical PDF, write the source digest, write the connected wiki page, update the synthesis layer and generated indexes, validate the records, and record the work in the daily log.

Do **not** summarize the digest back in the chat unless the user separately asks for a summary or a report. The normal chat response should only confirm the repository paths, validation status, and any blocker or unresolved evidence limitation.

## Rationale

The repository is the durable paper knowledge base. Repeating a complete digest in chat creates a second, non-canonical copy and makes the command ambiguous.

## Scope

This convention applies to future uses of “digest” referring to a paper. A request that explicitly asks for both a repository digest and a chat summary overrides the no-summary default for that request only.
