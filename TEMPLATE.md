# Using this template

1. On GitHub: **Use this template** → **Create a new repository**.
2. Enable **Issues** in the new repo (Settings → General).
3. Create issues from [.github/SUGGESTED_ISSUES.md](.github/SUGGESTED_ISSUES.md). GitHub Issues are the source of truth; agents do not use a plan doc.
4. Rename the project: replace `kalvi_library_template` and `kalvi-library-template` in `pyproject.toml`, `src/`, and any imports.
5. Set `GITHUB_TOKEN` for the GitHub MCP (Cursor Settings or env) if using Cursor.

## What's included

- **Python**: src layout, uv, pyproject.toml, Ruff (lint + format), pytest, Pylint.
- **Cursor**: Rules (project, Python), skills (run-quality-checks, release), AGENTS.md, GitHub MCP.
- **GitHub**: CI workflow (test, ruff), issue templates (Task, Bug), SUGGESTED_ISSUES.

## Make this repo a template

Settings → General → check **Template repository**.
