# Contributing

- **Work**: Tracked in **GitHub Issues**. Pick or create an issue ([.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/)).
- **Scope**: Get it from the issue. To seed issues, use [.github/SUGGESTED_ISSUES.md](.github/SUGGESTED_ISSUES.md).
- **Commit messages**: Use [Conventional Commits](https://www.conventionalcommits.org/) (e.g. `feat: add X`, `fix: Y`). Enforced by the commit-msg hook if you run `uv run pre-commit install --hook-type commit-msg`.
- **Git hooks** (recommended): `uv run pre-commit install` (code checks on commit) and `uv run pre-commit install --hook-type commit-msg` (commit message lint). Then pre-commit runs automatically on each commit.
- **Before submit**: Run **`uv run nox`** (runs tests, lint, coverage, security, pre-commit), or at minimum: `uv run pytest`, `uv run ruff check src tests scripts`, `uv run ruff format src tests scripts` (or `uv run pre-commit run --all-files`). Coverage is enforced (e.g. 80%); run `uv run pytest --cov=src/kalvi_library_template --cov-fail-under=80` or `uv run nox -s coverage`.
- **Local env**: Copy [.env.example](.env.example) to `.env` for local development if needed; do not commit `.env`. See [docs/settings-pattern.md](docs/settings-pattern.md).
- **Testing**: Shared fixtures go in `tests/conftest.py`. See [docs/testing.md](docs/testing.md).
- **Markdown / docs**: Lint with [.markdownlint.yaml](.markdownlint.yaml). Use real headings (`##`, `###`) for section titles, not standalone bold. Pre-commit runs markdownlint on commit. Doc filenames under [docs/](docs/) and [docs/research/](docs/research/) use **lowercase-with-hyphens** (kebab-case); root markdown files are allowlisted (e.g. README.md, CONTRIBUTING.md). Pre-commit runs a filename check.
- **Agents**: [AGENTS.md](AGENTS.md).
