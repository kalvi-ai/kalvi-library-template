Run the project quality checks and report results.

1. Run: `uv run pytest`
2. Run: `uv run ruff check src tests scripts`
3. Run: `uv run ruff format --check src tests scripts`
4. Optionally: `uv run pylint src/kalvi_library_template scripts` and `uv run mypy src/kalvi_library_template scripts`
5. Or run everything with: `uv run pre-commit run --all-files`

Summarize pass/fail for each step. If anything fails, list the first few errors or suggest running the command locally for full output.
