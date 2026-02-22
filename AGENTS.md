# Agent guide (Cursor)

**GitHub Issues** are the source of truth. Scope and acceptance criteria come from issues.

## What this is

Python library template: src layout, uv, Ruff, pytest. Cursor-only agent setup for complex projects. Rename to your project.

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
| Agentic workflow | [docs/agentic-workflow.md](docs/agentic-workflow.md) — canonical loop (R→P→E→V) and skill chain; use this for the finalized flow. |
| Research/background | [docs/research/](docs/research/) |

## Commands

- **All checks**: `uv run nox` (tests, lint, coverage, security, pre-commit).
- Tests: `uv run pytest` (with coverage: `uv run pytest --cov=src/kalvi_library_template --cov-fail-under=80` or `uv run nox -s coverage`).
- Lint: `uv run ruff check src tests scripts`
- Format: `uv run ruff format src tests scripts`
- Pylint: `uv run pylint src/kalvi_library_template scripts`
- Type check: `uv run mypy src/kalvi_library_template scripts`
- Security: `uv run bandit -r src/kalvi_library_template`, `uv run pip-audit` (or `uv run nox -s security`).
- Docs: `uv run mkdocs build` (or `uv run nox -s docs`).
- Pre-commit: `uv run pre-commit run --all-files`
- Commit messages: Conventional Commits (enforced if hooks enabled). Enable hooks: `uv run pre-commit install` and `uv run pre-commit install --hook-type commit-msg`

## When implementing

Follow the canonical loop: [Agentic workflow](docs/agentic-workflow.md) (Research → Plan → Execute → Validate). In short:

1. Get scope and acceptance criteria from the **GitHub issue**.
2. For non-trivial work: state a short plan (scope, steps, how to validate) before editing.
3. Implement; add or update tests.
4. Before done: run **run-quality-checks** (or `uv run pre-commit run --all-files`) so tests, Ruff, Pylint, mypy, and format all pass. CI runs the same set.

## Setup (Cursor)

- **Rules**: [.cursor/rules/](.cursor/rules/) — activation and globs; project context is this file (AGENTS.md).
- **Skills**: [.cursor/skills/](.cursor/skills/) — use **implement-from-issue**, **plan**, **triage**, **review**, **project-review**, **commit**, **refactor**, **docs**, **test**, **run-quality-checks**, **release**, **debug**, **dependency-update**, **maintain**, **bootstrap-from-template**.
- **Commands**: [.cursor/commands/](.cursor/commands/) — slash commands (e.g. `/code-review`, `/run-quality-checks`) for repeatable workflows.
- **Hooks**: [.cursor/hooks.json](.cursor/hooks.json) — lifecycle hooks (e.g. format after edit). See [docs/cursor-setup.md](docs/cursor-setup.md).
- **MCP**: [.cursor/mcp.json](.cursor/mcp.json). GitHub (issues), Exa (research), Context7 (docs). Set `GITHUB_TOKEN`. Optional: Exa, Context7. See [docs/setup-mcp.md](docs/setup-mcp.md); do not commit API keys. In Cursor Settings → Tools, disable duplicate or unused MCP servers to avoid token bloat.
- **Indexing**: [.cursorignore](.cursorignore) — excludes paths from codebase indexing (faster index). Edit in Settings → Indexing & Docs if needed.
- **Subagents**: Use Cursor’s built-in subagents for parallel work; add custom subagents only when you need specific tool access or prompts. See [docs/cursor-setup.md](docs/cursor-setup.md).
