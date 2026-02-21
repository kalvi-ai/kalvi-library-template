---
name: dependency-update
description: Upgrade one or all dependencies with uv, run checks, and propose a commit. Use when the user asks to update, upgrade, or bump dependencies (or apply a Dependabot-style change).
---

# Dependency update

Use when the user asks to **update dependency X**, **upgrade dev deps**, **bump packages**, or **apply this Dependabot PR**. Keep the change scoped to dependencies and verify the project stays green.

## Input

- **Scope**: One package (e.g. `pytest`), optional extras (e.g. `[config]`), or “all” / “dev” for `uv lock --upgrade`.
- **Constraint** (optional): e.g. “only patch versions” or “pytest to latest 7.x.”

## Steps

1. **Update lockfile**
   - **Single package**: `uv lock --upgrade-package <name>` (e.g. `uv lock --upgrade-package pytest`).
   - **All packages**: `uv lock --upgrade`.
   - If the user gave a constraint, run the appropriate command and ensure the resolved version matches (e.g. check `uv.lock` or run `uv tree`).

2. **Sync and run checks**
   - `uv sync --group dev` (or `uv sync` if updating runtime deps).
   - Run **run-quality-checks** (or at minimum `uv run pytest` and `uv run ruff check src tests scripts`). Fix any new failures (e.g. deprecations, type errors) before proposing a commit.

3. **Propose commit**
   - Type: `chore` or `chore(deps)`.
   - Subject: e.g. `chore(deps): upgrade pytest to X.Y.Z` or `chore(deps): upgrade dev dependencies`.
   - Body (optional): list major version bumps or breaking changes if relevant. If this closes an issue (e.g. Dependabot), add “Fixes #N.”
   - Remind: commit only after user approval; stage `pyproject.toml` and `uv.lock` (and any changed files). Use **commit** skill for approval flow if desired.

## Notes

- Prefer upgrading one or a few packages at a time so regressions are easy to attribute. For “upgrade everything,” run checks and scan the diff for major bumps.
- If `pip-audit` is in the project, run it after the upgrade to confirm no new known vulnerabilities.
