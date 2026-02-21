# Project principles

- **Scope from issues**: Implementation scope and acceptance criteria come from the GitHub issue. Do not add or assume requirements not in the issue.
- **Tests and lint before done**: Run `uv run pytest`, `uv run ruff check src tests scripts`, `uv run ruff format src tests scripts` (or `uv run pre-commit run --all-files`) before considering work complete.
- **One logical change per issue**: One issue = one deliverable. Do not mix unrelated work in one commit or PR.
- **Conventional Commits**: Use `feat:`, `fix:`, `docs:`, etc. Commit message is enforced by pre-commit when hooks are enabled.
- **Record decisions**: Non-obvious architectural or tooling decisions go in [docs/decisions/](decisions/README.md) as MADR-formatted ADRs.

Derived libraries should replace this list with their own principles.
