---
name: refactor
description: Refactors code for clarity, style, or structure without changing behavior. Use when the user asks to refactor, clean up, or improve code in a module/file.
---

# Refactor

Use when the user asks to **refactor** (e.g. "refactor this module", "clean up X", "improve clarity of Y"). Change structure/style only; preserve behavior.

## Input

- Target: file(s), module, or area the user names (e.g. "refactor `src/.../validation.py`", "clean up the auth module").
- Optionally: an issue that describes the refactor goal (e.g. "extract component", "reduce duplication").

## Checklist (aim for; don’t change behavior)

1. **Scope** – Identify what to refactor and what to leave unchanged. No new features or bug fixes unless the user asks.
2. **Clarity** – Simplify names, split long functions, reduce nesting. Prefer clear over clever (see `.cursor/rules/python.mdc`).
3. **Duplication** – Extract repeated logic into helpers or shared code where it improves readability.
4. **Structure** – Align with existing patterns (e.g. `src/` layout, test layout). Prefer functions over deep class hierarchies.
5. **Style** – Ruff (format + lint), type hints, first-party import as `kalvi_library_template`. Run **run-quality-checks** when done.

## Process

1. If non-trivial: state a short refactor plan (what to extract/rename/split, what stays).
2. Apply edits; keep behavior identical (same inputs → same outputs).
3. Add or adjust tests only if structure change requires it (e.g. testing a new helper); do not broaden coverage beyond what’s needed for the refactor.
4. Run `uv run pytest`, `uv run ruff check src tests scripts`, `uv run ruff format src tests scripts` (or **run-quality-checks**) before done.

## Notes

- For "refactor + add feature", use **implement-from-issue** or do refactor first then implement.
- Do not change public API or behavior unless the user explicitly asks.
