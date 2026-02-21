---
name: implement-from-issue
description: Implements work from a GitHub issue (scope + acceptance criteria). Use when the user asks to implement, build, or do an issue; or to add a feature/fix from an issue.
---

# Implement from issue

**Source of truth**: The GitHub issue. Scope and acceptance criteria come from the issue.

## Steps

1. **Get scope and acceptance criteria** from the issue. If the user didn’t name an issue, ask which issue or get the requirements (summary + acceptance criteria) from the user.

2. **Plan (if non-trivial)**
   For anything beyond a tiny change (e.g. new module, refactor, multiple files), state a short plan before editing:
   - Scope: what will be changed and what will not.
   - Steps: 2–5 concrete steps (files/modules, behavior, tests).
   - Validation: how you’ll verify (tests, manual check, acceptance criteria).

3. **Implement**
   - Write or change code in `src/kalvi_library_template/` (or as the issue specifies).
   - Add or update tests in `tests/` so acceptance criteria are covered.
   - Follow project conventions (see `.cursor/rules/python.mdc` and `always.mdc`).

4. **Validate before done**
   - Run the **run-quality-checks** skill (or at minimum: `uv run pytest`, `uv run ruff check src tests`, `uv run ruff format --check src tests`).
   - Confirm behavior matches the issue’s acceptance criteria.

## Notes

- One issue = one logical change. Don’t mix unrelated work.
- If the issue is vague, ask for clarification or propose concrete acceptance criteria.
- After implementing, you can suggest closing the issue with a phrase like “Fixes #N” in the commit message (Conventional Commits: `fix: ...` or `feat: ...`).
