---
name: run-quality-checks
description: Runs tests, coverage, Ruff lint/format, Pylint, mypy, bandit, pip-audit, and pre-commit. Use when the user asks to run tests, lint, format, or verify the project is green.
---

# Run quality checks

From project root, use `uv run` so the project venv is used. Or run all checks at once: `uv run nox` (runs tests, lint, coverage, security, pre-commit).

## Tests

```bash
uv run pytest
```

## Coverage

```bash
uv run pytest --cov=src/kalvi_library_template --cov-report=term-missing --cov-fail-under=80
# or: uv run nox -s coverage
```

## Lint and format (Ruff)

```bash
uv run ruff check src tests scripts
uv run ruff format src tests scripts
```

- Fix auto-fixable: `uv run ruff check src tests scripts --fix`
- Check only (no write): `uv run ruff format --check src tests scripts`

## Pylint

```bash
uv run pylint src/kalvi_library_template scripts
```

## Mypy

```bash
uv run mypy src/kalvi_library_template scripts
```

## Security

```bash
uv run bandit -r src/kalvi_library_template
uv run pip-audit
# or: uv run nox -s security
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

Run in order: `uv run pytest` (or nox coverage) → `uv run ruff check src tests scripts` → `uv run ruff format --check src tests scripts` → `uv run pylint src/kalvi_library_template scripts` → `uv run mypy src/kalvi_library_template scripts` → `uv run bandit -r src/kalvi_library_template` → `uv run pip-audit` → `uv run pre-commit run --all-files`. Or run **`uv run nox`** to execute tests, lint, coverage, security, and pre-commit sessions; CI runs the same steps.
