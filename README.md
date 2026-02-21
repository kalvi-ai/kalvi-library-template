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

From the terminal, or **Run Task** in Cursor/VS Code (`.vscode/tasks.json`):

```bash
uv run pytest
uv run ruff check src tests
uv run ruff format src tests
uv run pylint src/kalvi_library_template
uv run mypy src/kalvi_library_template
uv run pre-commit run --all-files
```

## Layout

- `src/kalvi_library_template/` – package
- `tests/` – pytest
- `examples/` – [examples/](examples/) (e.g. `hello.py`)
- [AGENTS.md](AGENTS.md) – agent guide
- [CONTRIBUTING.md](CONTRIBUTING.md) – how to contribute

## Renaming

Replace `kalvi_library_template` (package) and `kalvi-library-template` (project name) in `pyproject.toml`, `src/`, and imports.
