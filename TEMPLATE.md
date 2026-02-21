# Using this template

1. On GitHub: **Use this template** → **Create a new repository**.
2. Enable **Issues** in the new repo (Settings → General).
3. Create issues from [.github/SUGGESTED_ISSUES.md](.github/SUGGESTED_ISSUES.md). GitHub Issues are the source of truth; agents do not use a plan doc.
4. Rename the project: replace `kalvi_library_template` and `kalvi-library-template` in `pyproject.toml`, `src/`, and any imports.
5. Update [LICENSE](LICENSE): set your name and year in the copyright line.
6. Set `GITHUB_TOKEN` for the GitHub MCP (Cursor Settings or env) if using Cursor.

## What's included

- **Python**: src layout, uv, pyproject.toml, Ruff (lint + format), pytest, Pylint, mypy, pre-commit, commitizen (commit message lint). Release deps: build, twine.
- **Cursor**: Rules (project, Python), skills (run-quality-checks, release), AGENTS.md, GitHub MCP.
- **GitHub**: CI (test, Ruff, Pylint, mypy, pre-commit), issue templates (Task, Bug), SUGGESTED_ISSUES. Commit `uv.lock` for reproducible builds.
- **Git hooks**: Run `uv run pre-commit install` and `uv run pre-commit install --hook-type commit-msg` to run checks and Conventional Commit lint on each commit.

## Make this repo a template

Settings → General → check **Template repository**.
