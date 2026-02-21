---
name: review
description: Reviews staged or recent code changes against the issue and project standards. Use when the user asks to review changes, review before commit, or review the diff for an issue.
---

# Review changes

Use when the user asks to **review** their changes (e.g. "review my changes", "review before commit", "review the diff for #5"). Output a short, structured review only—no edits.

## Input

- Staged diff, or the changes for a given issue, or "recent" implementation (user specifies).
- Optionally: issue number or link so acceptance criteria can be checked.

## Review checklist

Work through and report briefly on each that applies:

1. **Issue alignment** – Do the changes match the issue’s scope and acceptance criteria? Anything missing or out of scope?
2. **Architecture / design** – Do changes fit existing structure (e.g. `src/` vs `tests/`), module roles, and patterns?
3. **Code quality** – Style (Ruff, type hints), naming, minimal change, no obvious duplication or dead code.
4. **Tests** – Are acceptance criteria covered by tests? Any obvious edge cases or missing tests?
5. **Docs / comments** – Are docstrings, README, or other docs updated if the change affects behavior or API?

## Output

- **Pass / concerns** – One line: "Pass" or "Concerns" (and how many).
- **Findings** – Bullet list: each finding with file/area and a concrete suggestion. Order by importance (blocking vs nice-to-have).
- **Optional** – One-line reminder to run **run-quality-checks** (or at least `uv run pytest` and `uv run ruff check src tests`) before commit.

Do not run linters or tests yourself unless the user asks; focus on reading the diff and code. Do not apply edits; only suggest.
