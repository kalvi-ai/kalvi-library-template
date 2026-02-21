---
name: project-review
description: Assesses the whole project against a dynamic rubric (structure, docs, tests, CI, principles, deps, security). Use when the user asks to review the project, project health, audit the repo, or how healthy the project is.
---

# Project-level review

Use when the user asks to **review the project**, **project health**, **audit the repo**, **project review**, or **how healthy is this project**. Produces a rubrics table and summary only—no edits. Does not run pytest/Ruff/mypy by default; does not review staged or recent code (use **review** for that).

## Input

- **Scope** (optional): **full** (default) — all criteria below; **quick** — subset: structure, tests present, principles documented, CI present, no obvious secrets.
- **Consult best practices** (optional): If the user says e.g. "review project and check against current best practices" or "review and validate with best practices":
  - Run a **research** step: use web search (Exa MCP when available) or research skill to look up current best practices (e.g. OWASP/OpenSSF for security and deps, documentation/testing rubrics, reviewer guidance).
  - Use findings to validate or extend the rubric for this run (e.g. add a short "Best practices" section or adjust criteria).
  - **Optional write**: If useful, draft or update a doc under `docs/research/` (e.g. `project-review-best-practices.md`) with a concise summary of sources and criteria used, so future runs can refer to it. Use a kebab-case filename.

## Building the rubric

1. **Project-derived criteria**: Read [pyproject.toml](pyproject.toml), [AGENTS.md](AGENTS.md), [docs/principles.md](docs/principles.md), and [docs/decisions/](docs/decisions/) (if present). Derive criteria from them, e.g.:
   - Issues as source of truth; tests/lint before done; one change per issue; Conventional Commits; decisions recorded in docs/decisions.
2. **Built-in criteria** (Python library template): Structure (src layout, package vs tests), dependencies (minimal, lockfile/pinned where appropriate), CI (e.g. GitHub Actions), docs (README, docstrings, principles/decisions), testing (tests present and in expected location), security (no committed secrets, dependency hygiene), code quality (Ruff/config present, type hints/mypy configured).
3. **Optional extension**: If `docs/project-review-rubric.md` exists, merge its criteria into the rubric (project-specific or extra dimensions).

For **quick** scope, use only: structure, tests present, principles documented, CI present, no obvious secrets.

## Process

1. **Build rubric**: Assemble criteria from project config + principles + built-in list (+ optional docs/project-review-rubric.md). If user asked for **consult best practices**, run research/web, validate or extend rubric, and optionally write to `docs/research/`.
2. **Assess**: For each criterion, **read only** (inspect files, configs). Do not run the full test/lint suite unless the user asks.
3. **Output**: Emit the rubrics table (markdown), summary, and optional reminder.

## Rubric table format

For each criterion, report:

| Criterion | Status | Evidence | Suggestion |
|-----------|--------|----------|------------|
| … | Pass / Partial / Fail | One-line evidence | Optional one-line |

Status: **Pass** (met), **Partial** (partially met), **Fail** (not met or not found).

## Output

- **Rubrics table**: Markdown table as above for all criteria (full or quick scope).
- **Summary**: One-line overall (e.g. "Pass with 2 partial") and 1–3 top recommendations.
- **Optional reminder**: "Run **run-quality-checks** for tests/lint; use **review** for change-level review."

If you ran **consult best practices**, add a short "Best practices" note (sources and any criteria added or validated).

## Out of scope

- Does not run pytest, Ruff, mypy, or pre-commit by default (user runs **run-quality-checks**).
- Does not review staged or recent code changes (user uses **review**).
- Does not apply edits; assessment and suggestions only.
