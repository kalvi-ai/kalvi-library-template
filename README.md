# kalvi-library-template

Python library template: src layout, uv, Ruff, pytest, and Cursor agent setup. **GitHub Issues** are the source of truth.

Use **Use this template** on GitHub to create a new repo, then see [TEMPLATE.md](TEMPLATE.md).

## Setup

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)

```bash
uv sync --group dev
```

**Enable git hooks** (optional but recommended): run code checks and commit message lint on every commit:

```bash
uv run pre-commit install
uv run pre-commit install --hook-type commit-msg
```

Commit messages must follow [Conventional Commits](https://www.conventionalcommits.org/) (e.g. `feat: add X`, `fix: Y`). Config: `[tool.commitizen]` in `pyproject.toml`.

## Commands

Run all checks: **`uv run nox`** (tests, lint, coverage, security, pre-commit).

From the terminal, or **Run Task** in Cursor/VS Code (`.vscode/tasks.json`):

```bash
uv run pytest
uv run pytest --cov=src/kalvi_library_template --cov-report=term-missing --cov-fail-under=80
uv run ruff check src tests scripts
uv run ruff format src tests scripts
uv run pylint src/kalvi_library_template scripts
uv run mypy src/kalvi_library_template scripts
uv run bandit -r src/kalvi_library_template
uv run pip-audit
uv run mkdocs build
uv run pre-commit run --all-files
```

## Layout

- `src/kalvi_library_template/` – package
- `tests/` – pytest
- `examples/` – [examples/](examples/) (e.g. `hello.py`)
- [AGENTS.md](AGENTS.md) – Cursor agent guide (commands, paths, skills, MCP). See [docs/cursor-setup.md](docs/cursor-setup.md) for rules, hooks, commands, indexing.
- [AGENTIC-WORKFLOW.md](AGENTIC-WORKFLOW.md) – agentic flow research and recommendation
- [CONTRIBUTING.md](CONTRIBUTING.md) – how to contribute

## Documentation

- [docs/](docs/) – overview, how-to, reference. Build with `uv run mkdocs build` (or `uv run nox -s docs`).
- [docs/principles.md](docs/principles.md) – project principles
- [docs/decisions/](docs/decisions/) – architecture decision records (ADRs)
- [docs/settings-pattern.md](docs/settings-pattern.md) – Pydantic Settings and env config (optional extra `[config]`)
- [docs/testing.md](docs/testing.md) – testing guide (fixtures, coverage, markers)
- [docs/specs/](docs/specs/) – formal specifications (optional; scope usually from [GitHub Issues](.github/ISSUE_TEMPLATE/))
- [docs/research/](docs/research/) – background and research
- [docs/cursor-setup.md](docs/cursor-setup.md) – Cursor rules, skills, commands, hooks, MCP, indexing
- [docs/setup-mcp.md](docs/setup-mcp.md) – MCP servers (GitHub, Exa, Context7)

Pre-commit enforces: YAML/JSON/TOML syntax, yamllint, actionlint (workflows), markdownlint, typos, Ruff, commit message (Conventional Commits). Configs: `.editorconfig`, `.markdownlint.yaml`, `.yamllint.yaml`.

## Renaming

Replace `kalvi_library_template` (package) and `kalvi-library-template` (project name) in `pyproject.toml`, `src/`, and imports.
