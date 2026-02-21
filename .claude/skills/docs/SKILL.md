---
name: docs
description: Updates documentation for a change (README, docstrings, CHANGELOG, or other docs). Use when the user asks to update docs, add docstrings, or document a feature/fix.
---

# Update documentation

Use when the user asks to **update docs** (e.g. "update docs for this change", "add docstrings to X", "document the new API", "update README/CHANGELOG").

## Input

- What changed: the user describes the change or points to code/diff (e.g. new function, new module, config change).
- Where to document: README, docstrings, CHANGELOG, `docs/`, or "wherever needed".

## What to update (as relevant)

1. **Docstrings** – Public modules, classes, and functions in `src/kalvi_library_template/`: summary, args, returns, raises (Google or NumPy style; project may prefer one). Keep in sync with `.cursor/rules/python.mdc` (type hints; mypy strict).
2. **README.md** – Install/usage if the change affects how users run or configure the project; new commands or options; layout if new top-level paths.
3. **CHANGELOG.md** – If present: add an entry under Unreleased (or next version) with the change; use Conventional Commits style (feat/fix/docs).
4. **Other docs** – `docs/`, AGENTS.md, CONTRIBUTING.md, or skill/rule files only if the user explicitly asks (e.g. "document this in AGENTS.md").

## Process

1. Identify which of the above apply from the user’s request and the code/diff.
2. Edit docstrings and/or markdown; keep tone consistent with existing docs.
3. Do not change code behavior; only add or edit documentation.
4. If you touch markdown, pre-commit (markdownlint, etc.) will apply on commit; no need to run full **run-quality-checks** unless you also changed code.

## Notes

- For "implement feature and document it", use **implement-from-issue** and include docs in the same pass, or use this skill after implementation.
- Prefer concise, accurate docs over long prose.
