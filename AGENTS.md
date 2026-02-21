# Agent guide

**GitHub Issues** are the source of truth. Scope and acceptance criteria come from issues.

## What this is

Python library template: src layout, uv, Ruff, pytest. Rename to your project.

## Key paths

| Purpose   | Path                          |
|----------|-------------------------------|
| Config   | [pyproject.toml](pyproject.toml) |
| Package  | [src/kalvi_library_template/](src/kalvi_library_template/) |
| Tests    | [tests/](tests/)              |
| Templates| [.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/) |

## Commands

- Tests: `uv run pytest`
- Lint: `uv run ruff check src tests`
- Format: `uv run ruff format src tests`
- Pylint: `uv run pylint src/kalvi_library_template`

## When implementing

1. Get scope and acceptance criteria from the **GitHub issue**.
2. Implement; add or update tests.
3. Run `uv run ruff check src tests` and `uv run pytest` before done.

## Setup

- **Rules**: `.cursor/rules/` (project, Python). Agent applies when relevant.
- **Skills**: `.cursor/skills/` (run-quality-checks, release).
- **MCP**: `.cursor/mcp.json` (GitHub). Set `GITHUB_TOKEN`.
