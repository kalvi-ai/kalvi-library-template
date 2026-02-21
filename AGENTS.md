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
- Lint: `uv run ruff check src tests`
- Format: `uv run ruff format src tests`
- Pylint: `uv run pylint src/kalvi_library_template`
- Type check: `uv run mypy src/kalvi_library_template`
- Pre-commit: `uv run pre-commit run --all-files`
- Commit messages: Conventional Commits (enforced if hooks enabled). Enable hooks: `uv run pre-commit install` and `uv run pre-commit install --hook-type commit-msg`

## When implementing

1. Get scope and acceptance criteria from the **GitHub issue**.
2. For non-trivial work: state a short plan (scope, steps, how to validate) before editing.
3. Implement; add or update tests.
4. Run `uv run ruff check src tests` and `uv run pytest` before done. CI also runs Pylint, mypy, and pre-commit.

## Setup

- **Rules**: `.cursor/rules/` — always (project), python (style), implementation (from-issue flow), issues (source of truth). Agent applies when relevant.
- **Skills**: `.cursor/skills/` — **implement-from-issue**, **plan**, **triage**, **review**, **commit**, **refactor** (clarity/style, no behavior change), **docs** (README, docstrings, CHANGELOG), **test** (add/extend tests only), **run-quality-checks**, **release**.
- **MCP**: `.cursor/mcp.json` (GitHub for issues). Set `GITHUB_TOKEN`. Optional for research: Exa (web/code search), Context7 (up-to-date library docs). See [docs/setup-mcp.md](docs/setup-mcp.md); do not commit API keys.
