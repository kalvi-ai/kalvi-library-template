# Contributing

- **Work**: Tracked in **GitHub Issues**. Pick or create an issue ([.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/)).
- **Scope**: Get it from the issue. To seed issues, use [.github/SUGGESTED_ISSUES.md](.github/SUGGESTED_ISSUES.md).
- **Before submit**: Run `uv run pytest`, `uv run ruff check src tests`, `uv run ruff format src tests`. Optionally: `uv run pylint src/kalvi_library_template`, `uv run mypy src/kalvi_library_template`. Or install hooks with `uv run pre-commit install` and run `uv run pre-commit run --all-files` before pushing.
- **Agents**: [AGENTS.md](AGENTS.md).
