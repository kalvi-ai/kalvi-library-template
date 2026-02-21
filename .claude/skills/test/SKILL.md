---
name: test
description: Adds or extends tests for existing code (no new features). Use when the user asks to add tests, improve coverage, or test a specific function/module.
---

# Add or extend tests

Use when the user asks to **add tests** (e.g. "add tests for X", "improve coverage for Y", "test this function"). Implement tests only; do not add new features or change production behavior.

## Input

- Target: module, function, class, or file (e.g. "add tests for `validation.py`", "test `parse_config`").
- Optionally: an issue that specifies scenarios or edge cases to cover.

## Process

1. **Locate** – Identify the code under test in `src/kalvi_library_template/` and the corresponding test file in `tests/` (e.g. `tests/test_validation.py`). Create the test file if it doesn’t exist.
2. **Scenarios** – Cover happy path, edge cases (empty input, boundaries, invalid input), and error paths (exceptions) where relevant.
3. **Style** – pytest; `pythonpath` includes `src` (see `pyproject.toml`). Use type hints; follow `.cursor/rules/python.mdc`. Use fixtures if they already exist in `conftest.py`.
4. **Run** – Execute `uv run pytest` for the touched tests (or all). Run `uv run ruff check src tests scripts` and `uv run ruff format src tests scripts` (or **run-quality-checks**) before done.

## Notes

- One test file per module under test (e.g. `src/.../validation.py` → `tests/test_validation.py`). Mirror package layout under `tests/` if the package has subpackages.
- Do not change production code except to make it testable (e.g. no new features or refactors unless the user asks). For "implement feature and add tests", use **implement-from-issue** instead.
- Prefer small, focused tests; avoid unnecessary duplication.
