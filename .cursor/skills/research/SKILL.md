---
name: research
description: Research, web search, or deep dive; optionally write under docs/research/. Use when the user asks to research, look up docs, or write a research doc.
---

# Research skill

Use when the user asks for **research**, **web search**, **deep dive**, or **current docs** on a topic.

## When to use

- User says: "research X", "web search for Y", "deep dive on Z", "find current docs for …".
- Goal: gather and synthesize information; optionally write a doc under `docs/research/`.

## Input

- **Topic or question** (required).
- **Target** (optional): e.g. "write summary to docs/research/…" with a kebab-case filename.

## Process

1. **Gather**: Use web/search (Exa MCP when available) and/or library docs (Context7 MCP when available). Use Exa for web and code search; use Context7 for up-to-date library documentation when configured.
2. **Synthesize**: Summarize findings; cite sources. Keep output minimal and scannable.
3. **Optional write**: If the user asked for a doc, draft or update a file under `docs/research/` with a **lowercase-with-hyphens** filename (e.g. `topic-name-research.md`).
4. **Boundary**: Do not run destructive or broad edits without user direction. Prefer suggesting a filename and outline for new research docs when the user has not asked to write a file.

## MCP

- **Exa MCP**: Use for web/code search when configured (set API key in MCP config). This supports the same "deep research" flow as projects that use Brave Search MCP (gather → synthesize → optionally write to `docs/research/`).
- **Context7 MCP**: Use for up-to-date library documentation when configured (set `CONTEXT7_API_KEY` in MCP config).

## Output

- Concise summary with sources.
- If a doc was requested: one file under `docs/research/<kebab-name>.md`.
