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

Install hooks to run on commit: `uv run pre-commit install`

## Full check

Run in order: `uv run pytest` → `uv run ruff check src tests` → `uv run ruff format --check src tests` → `uv run pylint src/kalvi_library_template` → `uv run mypy src/kalvi_library_template` → `uv run pre-commit run --all-files`. Or just `uv run pre-commit run --all-files` (which runs Ruff); CI runs all of the above.
