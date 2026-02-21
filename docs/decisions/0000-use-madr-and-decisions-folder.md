# Use MADR and docs/decisions/ for ADRs

## Context and Problem Statement

We need a single place to record architecturally significant decisions (tooling, layout, patterns) so humans and agents can refer to the rationale. Without it, "why we chose X" is lost in history or chat.

## Considered Options

- No ADRs (rely on README and memory)
- Free-form decision log in a single file
- MADR in `docs/decisions/` with index

## Decision Outcome

Chosen option: **MADR in `docs/decisions/`**, because it gives a lightweight, structured format (context, decision, consequences), stable paths for linking, and an index in [README.md](README.md) for discovery. New ADRs are added as `NNNN-title-with-dashes.md`; see [MADR](https://adr.github.io/madr/).

### Consequences

- Good: One place for decisions; agents and contributors know where to look.
- Bad: Requires discipline to add an ADR when a non-obvious decision is made.
