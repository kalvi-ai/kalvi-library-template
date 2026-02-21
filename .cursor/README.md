# Cursor agent setup

**GitHub Issues** are the source of truth. Agents do not use a plan doc.

## Rules (`.cursor/rules/`)

- `always.mdc` – Project context, tooling, GitHub Issues.
- `python.mdc` – Python/Ruff when editing `**/*.py`.

Activation: agent-decides (or change in Cursor Settings → Rules).

## Skills (`.cursor/skills/`)

- `run-quality-checks` – pytest, Ruff, Pylint.
- `release` – version, tag, build, PyPI.

## AGENTS.md

Project root; source of truth, key paths, commands.

## MCP (`.cursor/mcp.json`)

GitHub server for issues. Set `GITHUB_TOKEN` in env or Cursor MCP settings.
