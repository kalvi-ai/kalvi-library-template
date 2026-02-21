# Contributing

- **Work**: Tracked in **GitHub Issues**. Pick or create an issue ([.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/)).
- **Scope**: Get it from the issue. To seed issues, use [.github/SUGGESTED_ISSUES.md](.github/SUGGESTED_ISSUES.md).
- **Commit messages**: Use [Conventional Commits](https://www.conventionalcommits.org/) (e.g. `feat: add X`, `fix: Y`). Enforced by the commit-msg hook if you run `uv run pre-commit install --hook-type commit-msg`.
- **Git hooks** (recommended): `uv run pre-commit install` (code checks on commit) and `uv run pre-commit install --hook-type commit-msg` (commit message lint). Then pre-commit runs automatically on each commit.
- **Before submit**: Run `uv run pytest`, `uv run ruff check src tests`, `uv run ruff format src tests` (or `uv run pre-commit run --all-files`). Optionally: Pylint, mypy.
- **Markdown / docs**: Lint with [.markdownlint.yaml](.markdownlint.yaml). Use real headings (`##`, `###`) for section titles, not standalone bold. Pre-commit runs markdownlint on commit. Doc filenames under [docs/](docs/) and [docs/research/](docs/research/) use **lowercase-with-hyphens** (kebab-case); root markdown files are allowlisted (e.g. README.md, CONTRIBUTING.md). Pre-commit runs a filename check.
- **Agents**: [AGENTS.md](AGENTS.md).
