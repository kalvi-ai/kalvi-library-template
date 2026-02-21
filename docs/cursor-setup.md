# Cursor setup

This template configures Cursor as the single AI agent. All paths and features below are under `.cursor/` or the repo root.

## Overview

| Feature | Path | Purpose |
|---------|------|---------|
| **Rules** | [.cursor/rules/](.cursor/rules/) | Scoped rules (activation, globs); see [AGENTS.md](../AGENTS.md) for project context. |
| **Skills** | [.cursor/skills/](.cursor/skills/) | Procedural skills (implement-from-issue, plan, review, project-review, etc.). |
| **Commands** | [.cursor/commands/](.cursor/commands/) | Slash commands (e.g. `/code-review`, `/run-quality-checks`) for repeatable workflows. |
| **Hooks** | [.cursor/hooks.json](.cursor/hooks.json) | Lifecycle hooks (e.g. format after file edit). |
| **MCP** | [.cursor/mcp.json](.cursor/mcp.json) | Tools (GitHub, Exa, Context7). See [setup-mcp.md](setup-mcp.md). |
| **Indexing** | [.cursorignore](../.cursorignore) | Excludes paths from codebase indexing for a faster, leaner index. |

## Hooks

Hooks run custom scripts at specific points during the agent’s execution. Config: `.cursor/hooks.json` (project) or `~/.cursor/hooks.json` (global).

**Included:** `afterFileEdit` runs `scripts/cursor-after-file-edit.py`, which runs `uv run ruff format` on the edited file(s) so agent edits stay formatted.

**Other hooks** (see [Cursor docs](https://cursor.com/docs/agent/third-party-hooks)): `beforeSubmitPrompt`, `beforeReadFile`, `beforeShellExecution`, `beforeMCPExecution`, `stop`. Scripts receive JSON on stdin; exit 0 to allow, exit 2 to block (where applicable). Add more entries in `hooks.json` and scripts as needed.

## Commands

Type `/` in Cursor chat to see slash commands. Each command is a Markdown file in `.cursor/commands/` with the prompt text. Add files like `my-workflow.md` for new `/my-workflow` commands.

## Subagents

Cursor provides built-in subagents for parallel work (e.g. one runs tests, one writes docs). Use them when a task benefits from focused, parallel execution. Add **custom subagents** in Cursor Settings only when you need specific tool access or a dedicated system prompt.

## Indexing and Docs

- **Codebase indexing**: Cursor indexes the repo for semantic search. [.cursorignore](../.cursorignore) excludes venv, caches, and build output so indexing stays fast. Edit in Settings → Indexing & Docs → “Ignore Files in .cursorignore”.
- **Docs**: Add external documentation URLs in Settings → Indexing & Docs → Add Doc when you want the agent to use specific external docs (e.g. framework references). Indexing is URL-based.
