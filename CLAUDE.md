

<!-- Source: .ruler/AGENTS.md -->

# Agent guide

**GitHub Issues** are the source of truth. Scope and acceptance criteria come from issues.

## What this is

Python library template: src layout, uv, Ruff, pytest. Rename to your project.

## Key paths

| Purpose   | Path                               |
| --------- | ---------------------------------- |
| Config    | [pyproject.toml](pyproject.toml)   |
| Package   | [src/kalvi_library_template/](src/kalvi_library_template/) |
| Tests     | [tests/](tests/)                   |
| Templates | [.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/) |
| Principles | [docs/principles.md](docs/principles.md) |
| Decisions | [docs/decisions/](docs/decisions/) |
| Specs (optional) | [docs/specs/](docs/specs/) |
| Research/background | [docs/research/](docs/research/) |

## Commands

- Tests: `uv run pytest`
- Lint: `uv run ruff check src tests scripts`
- Format: `uv run ruff format src tests scripts`
- Pylint: `uv run pylint src/kalvi_library_template scripts`
- Type check: `uv run mypy src/kalvi_library_template scripts`
- Pre-commit: `uv run pre-commit run --all-files`
- Commit messages: Conventional Commits (enforced if hooks enabled). Enable hooks: `uv run pre-commit install` and `uv run pre-commit install --hook-type commit-msg`

## When implementing

1. Get scope and acceptance criteria from the **GitHub issue**.
2. For non-trivial work: state a short plan (scope, steps, how to validate) before editing.
3. Implement; add or update tests.
4. Run `uv run ruff check src tests scripts` and `uv run pytest` before done. CI also runs Pylint, mypy, and pre-commit.

## Setup

- **Rules**: `.cursor/rules/` — Cursor activation and globs; project context in this file (AGENTS.md). Agent applies when relevant.
- **Skills**: Canonical skills in `.ruler/skills/`; Ruler propagates to Cursor (`.cursor/skills/`), Claude (`.claude/skills/`), Gemini (`.gemini/skills/`), Codex (`.codex/skills/`). Use **implement-from-issue**, **plan**, **triage**, **review**, **commit**, **refactor**, **docs**, **test**, **run-quality-checks**, **release**.
- **MCP**: Defined in `.ruler/ruler.toml`; Ruler propagates to `.cursor/mcp.json`, `.zed/settings.json`, etc. GitHub (issues), Exa (research), Context7 (docs). Set `GITHUB_TOKEN`. Optional: Exa, Context7. See [docs/setup-mcp.md](docs/setup-mcp.md); do not commit API keys.
- **Codex**: Set `CODEX_HOME="$(pwd)/.codex"` so Codex uses project MCP and config.
