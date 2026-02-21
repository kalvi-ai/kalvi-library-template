# Cursor agent setup

**GitHub Issues** are the source of truth. Implement from issues; plan then execute for non-trivial work.

## Rules (`.cursor/rules/`)

- `always.mdc` – Project context, tooling, skills list.
- `python.mdc` – Python/Ruff when editing `**/*.py`.
- `implementation.mdc` – When implementing: issue = scope, plan if non-trivial, tests, quality checks before done.
- `issues.mdc` – How to use issues (acceptance criteria, templates).
- `markdown.mdc` – When editing `.md`: follow .markdownlint.yaml, use headings for section titles.

Activation: agent-decides (or change in Cursor Settings → Rules).

## Skills (`.cursor/skills/`)

- `implement-from-issue` – Implement from a GitHub issue (scope → plan if needed → code + tests → quality checks).
- `plan` – Produce a short plan (scope, steps, validation) without editing code.
- `triage` – Triage an issue: classify (task/bug/question), check completeness, suggest labels and next step (ready / needs clarification / needs more info).
- `review` – Review staged or recent changes against the issue and project standards (checklist; suggest only, no edits).
- `commit` – Suggest a Conventional Commit message from the diff; remind to run pre-commit (suggest only, no git commands).
- `refactor` – Refactor code for clarity/style/structure without changing behavior; small plan then edit then quality checks.
- `docs` – Update documentation (README, docstrings, CHANGELOG, or other docs) for a given change.
- `test` – Add or extend tests for existing code (no new features); target module/function; run pytest and Ruff when done.
- `run-quality-checks` – pytest, Ruff, Pylint, mypy, pre-commit.
- `release` – version, tag, build, PyPI.

## AGENTS.md

Project root; source of truth, key paths, commands.

## MCP (`.cursor/mcp.json`)

GitHub server for issues. Set `GITHUB_TOKEN` in env or Cursor MCP settings.
