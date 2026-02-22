# Project principles

- **Scope from issues**: Implementation scope and acceptance criteria come from the GitHub issue. Do not add or assume requirements not in the issue.
- **Full quality checks before done**: Run the full check suite (tests, Ruff, Pylint, mypy, and format) before considering work complete—e.g. **run-quality-checks** or `uv run pre-commit run --all-files`. CI runs the same set.
- **One logical change per issue**: One issue = one deliverable. Do not mix unrelated work in one commit or PR.
- **Conventional Commits**: Use `feat:`, `fix:`, `docs:`, etc. Commit message is enforced by pre-commit when hooks are enabled.
- **Record decisions**: Non-obvious architectural or tooling decisions go in [docs/decisions/](decisions/README.md) as MADR-formatted ADRs.
- **Logging and observability**: Use stdlib logging only in library code; apps configure handlers. See [docs/decisions/0001-logging-in-libraries.md](decisions/0001-logging-in-libraries.md). Optional [logging] extra for structlog.

Derived libraries should replace this list with their own principles.
