# Using this template

1. On GitHub: **Use this template** → **Create a new repository**.
2. Enable **Issues** in the new repo (Settings → General).
3. Create issues from [.github/SUGGESTED_ISSUES.md](.github/SUGGESTED_ISSUES.md). GitHub Issues are the source of truth; agents do not use a plan doc.
4. Rename the project: replace `kalvi_library_template` and `kalvi-library-template` everywhere. **Easiest**: use the **bootstrap-from-template** skill (see [.cursor/skills/bootstrap-from-template/SKILL.md](.cursor/skills/bootstrap-from-template/SKILL.md)) and give the new library name; the agent will do the full rename and metadata update. **Manual**: follow the checklist in [docs/bootstrap-from-template.md](docs/bootstrap-from-template.md).
5. Update [LICENSE](LICENSE): set your name and year in the copyright line.
6. Set `GITHUB_TOKEN` for the GitHub MCP (Cursor Settings or env) if using Cursor.

## After creating from this template

- **Security**: In Settings → Code security and analysis, enable **Dependabot alerts** and **Secret scanning** (free for public repos). Optionally enable **Branch protection** for `main` with required status checks (CI) and PR reviews.
- **Lockfile**: Run `uv lock` after changing dependencies; commit `uv.lock` for reproducible builds. Before release, run `uv run pip-audit` to check for known vulnerabilities.

## What's included

- **Python**: src layout, uv, pyproject.toml, Ruff (lint + format), pytest, pytest-cov, coverage, Pylint, mypy, typeguard, hypothesis, bandit, pip-audit, nox, MkDocs + mkdocstrings, pre-commit, commitizen, build, twine. Optional extras: `[config]` (Pydantic/pydantic-settings), `[logging]` (structlog).
- **Cursor**: Rules (project, Python), skills (run-quality-checks, release, etc.), AGENTS.md, GitHub MCP.
- **GitHub**: CI (tests + coverage, Ruff, Pylint, mypy, bandit, pip-audit, pre-commit), issue templates (Task, Bug), pull request template, SUGGESTED_ISSUES. Community files: SECURITY.md, CODE_OF_CONDUCT.md, CHANGELOG.md, .gitattributes, .env.example.
- **Git hooks**: Run `uv run pre-commit install` and `uv run pre-commit install --hook-type commit-msg` to run checks and Conventional Commit lint on each commit.

## Making a minimal library

The template is batteries-included. For a tiny library with fewer dev tools you can slim down:

- **Dev deps**: In [pyproject.toml](pyproject.toml), remove nox, bandit, pip-audit, mkdocs, mkdocstrings from `[dependency-groups]` dev and `[project.optional-dependencies]` dev (keep pytest, ruff, pylint, mypy, pre-commit, commitizen, build, twine as needed).
- **CI**: In [.github/workflows/ci.yml](.github/workflows/ci.yml), remove the Bandit and pip-audit steps; if you removed MkDocs, remove any docs-build steps. Keep tests, coverage, Ruff, Pylint, mypy, pre-commit.
- **Optional**: Remove optional extras `[config]` and `[logging]` from pyproject if you do not need them; remove [noxfile.py](noxfile.py) if you removed nox.

See [CONTRIBUTING.md](CONTRIBUTING.md) and [README.md](README.md) for the full command list; after stripping, update those to match.

## Make this repo a template

Settings → General → check **Template repository**.
