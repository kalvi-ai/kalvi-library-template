---
name: run-quality-checks
description: Runs tests, Ruff lint/format, and optional Pylint. Use when the user asks to run tests, lint, format, or verify the project is green.
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

## Pylint (optional)

```bash
uv run pylint src/kalvi_library_template
```

## Full check

Run in order: `uv run pytest` → `uv run ruff check src tests` → `uv run ruff format --check src tests`. Optionally add Pylint.
