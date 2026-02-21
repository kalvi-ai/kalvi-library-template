---
name: run-quality-checks
description: Runs tests, Ruff lint/format, Pylint, mypy, and pre-commit. Use when the user asks to run tests, lint, format, or verify the project is green.
---

# Run quality checks

From project root, use `uv run` so the project venv is used.

## Tests

```bash
uv run pytest
```

## Lint and format (Ruff)

```bash
uv run ruff check src tests
uv run ruff format src tests
```

- Fix auto-fixable: `uv run ruff check src tests --fix`
- Check only (no write): `uv run ruff format --check src tests`

## Pylint

```bash
uv run pylint src/kalvi_library_template
```

## Mypy

```bash
uv run mypy src/kalvi_library_template
```

## Pre-commit (all hooks)

```bash
uv run pre-commit run --all-files
```

Pre-commit runs: check-yaml, check-json, check-toml, trailing-whitespace, end-of-file-fixer, check-merge-conflict, detect-private-key, check-added-large-files, yamllint, actionlint (`.github/workflows/`), markdownlint-cli2, typos, Ruff (check + format), and (on commit) commitizen. Configs: `.yamllint.yaml`, `.markdownlint.yaml`.

Enable git hooks (code checks + commit message lint on every commit):

```bash
uv run pre-commit install
uv run pre-commit install --hook-type commit-msg
```

Commit messages must follow Conventional Commits (e.g. `feat: add X`). Use task **enable git hooks** or the commands above.

## Full check

Run in order: `uv run pytest` → `uv run ruff check src tests` → `uv run ruff format --check src tests` → `uv run pylint src/kalvi_library_template` → `uv run mypy src/kalvi_library_template` → `uv run pre-commit run --all-files`. Or just `uv run pre-commit run --all-files` (runs YAML/JSON/TOML/Markdown/typos + Ruff); CI runs the same.
