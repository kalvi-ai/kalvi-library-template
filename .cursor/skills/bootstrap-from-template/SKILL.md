---
name: bootstrap-from-template
description: Sets up a new library from this template. Use when the user has created a repo from this template and provides the new library name (and optionally description, author, repo URL); the agent renames the project/package everywhere and updates metadata.
---

# Bootstrap new library from template

When the user bases a **new library** on this template and gives **enough context** (at least the new library name; optionally description, author, GitHub repo URL), perform a **full rename and metadata update** so the repo is ready for the new library. Do not run this in the original template repo if the goal is to keep the template unchanged.

## Input from user

- **Required**: New library/project name (e.g. `my-auth-lib`, `My Auth Library`, or `my_auth_lib`). Use it to derive:
  - **project_name**: PyPI-style, lowercase, hyphens for word separation (e.g. `my-auth-lib`, `my-auth-library`).
  - **package_name**: Import-style, lowercase, underscores (e.g. `my_auth_lib`, `my_auth_library`). If the user gives a name with underscores, use it as package_name and derive project_name by replacing underscores with hyphens.
- **Optional**: One-line description (for `pyproject.toml` and README); author/copyright holder (for LICENSE); GitHub repo URL or `org/repo` (for CHANGELOG links, SECURITY.md, mkdocs `site_url`, README link).

If anything required is missing, ask the user before proceeding.

## Steps

### 1. Derive names

- **project_name**: Used in `pyproject.toml` `name`, URLs, `site_name`, README title. Must be lowercase; spaces and underscores become hyphens.
- **package_name**: Used in `src/<package_name>/`, imports, Ruff `known-first-party`, coverage paths, docs API. Must be a valid Python identifier (lowercase, underscores only).

### 2. Rename package directory

- Rename `src/kalvi_library_template` to `src/<package_name>` (create new directory, move `__init__.py` and any other modules, remove old directory; or use `git mv` if available).

### 3. Replace in all files

Replace **every** occurrence in the repo (excluding `.git/`, `.venv/`, and binary files):

- `kalvi_library_template` → `<package_name>`
- `kalvi-library-template` → `<project_name>`

**Files that must be updated** (check each):

| Location | What to change |
|----------|----------------|
| `pyproject.toml` | `name`, `[tool.hatch.build.targets.wheel]` packages, `[tool.ruff.lint.isort]` known-first-party, `[tool.commitizen]` version_files, `[tool.coverage.run]` source |
| `src/<package_name>/__init__.py` | (already in new path; no string replace needed for package name inside file if it only has `__version__`) |
| `docs/api/kalvi_library_template.md` | Rename file to `docs/api/<package_name>.md`; replace title and `::: module` with `<package_name>` |
| `docs/index.md` | Title, API link (`api/<package_name>.md`), README link (if repo URL known) |
| `docs/testing.md` | Import example and coverage path |
| `mkdocs.yml` | `site_name`, `site_url` (if repo URL known), `nav` API entry to `<package_name>.md` |
| `README.md` | Title, description (if provided), all command paths and package path, "Replace..." note (update or remove) |
| `TEMPLATE.md` | Step 4: replace with "Already done if you used the bootstrap-from-template skill" or a short "This repo was created from the template" note so the new repo does not imply the rename is still to do |
| `AGENTS.md` | Package path in table and in every command example |
| `CONTRIBUTING.md` | Coverage path in commands |
| `CHANGELOG.md` | `[Unreleased]` and version links: replace `kalvi-library-template` with `org/repo` or project name in URL if repo given |
| `SECURITY.md` | Repo path in advisory link |
| `LICENSE` | Copyright holder and year (if author provided) |
| `noxfile.py` | `pylint` path, `mypy` path, `--cov=` path, `bandit` path |
| `.github/workflows/ci.yml` | `--cov=src/<package_name>`, `pylint src/<package_name>`, `mypy src/<package_name>`, `bandit -r src/<package_name>` |
| `.cursor/skills/release/SKILL.md` | Path to `__init__.py` |
| `.cursor/skills/run-quality-checks/SKILL.md` | All `pytest --cov`, `pylint`, `mypy`, `bandit` paths |
| `.cursor/skills/refactor/SKILL.md` | First-party package name and path |
| `.cursor/skills/test/SKILL.md` | Package path |
| `.cursor/skills/docs/SKILL.md` | Package path |
| `.cursor/skills/implement-from-issue/SKILL.md` | Package path |
| `.cursor/rules/implementation.mdc` | Package path and first-party name |
| `.cursor/rules/python.mdc` | known-first-party package name |
| `.cursor/commands/run-quality-checks.md` | pylint/mypy paths |
| `.vscode/tasks.json` | pylint and mypy `command` entries to `src/<package_name>` (often missed; check both tasks). |
| `examples/hello.py` | Import and any print message |
| `tests/test_example.py` | Import |
| `tests/__init__.py` | Comment |
| `.github/SUGGESTED_ISSUES.md` | Rename step: can say "Already done if you used the bootstrap-from-template skill" or keep generic |

If the user provided a **description**, set it in `pyproject.toml` `description` and optionally in the first line or paragraph of `README.md`. If they provided **repo URL** (e.g. `https://github.com/org/repo` or `org/repo`), use it for `mkdocs.yml` `site_url`, `CHANGELOG.md` compare/tag links, `SECURITY.md`, and README repo link.

### 3b. Template wording cleanup (after renames)

Several docs and skills still say "this template" or refer to the template repo; update them so the new project reads as the actual library.

| File | What to change |
|------|----------------|
| `SECURITY.md` | Replace "this template" / "the template" with "this project" / "the project" (or equivalent). |
| `docs/cursor-setup.md` | Same. |
| `README.md` | Same; also remove or reword any "Replace…" note that still refers to the template. |
| `docs/research/linters-formatters.md` | Same. |
| `docs/decisions/0001-logging-in-libraries.md` | Same. |
| `docs/settings-pattern.md` | Same. |
| `AGENTIC-WORKFLOW.md` | Same. |
| `.cursor/skills/project-review/SKILL.md` | Same. |
| `TEMPLATE.md` | Already updated in Step 3; ensure no remaining "this template" or "rename" wording that implies the repo is still the template. |

Optional: run a search for `template` (and `kalvi.library.template` if any remain) in `.md`, `.mdc`, `.yml` and fix any leftover "this template" or old package references.

### 4. Regenerate lockfile and verify

- Run `uv lock` so the lockfile reflects the new project name.
- Run **run-quality-checks** (or at least `uv run pytest` and `uv run ruff check src tests scripts`) to confirm nothing is broken.

### 5. Summarize and suggest commit

- List what was renamed and updated (project name, package name, key files).
- Suggest the user review the diff and commit, e.g. `chore: bootstrap from template as <project_name>`.

## Boundaries

- **Do not** run in the original template repository if the intent is to keep the template as-is (e.g. user said "in the template repo, add a skill...").
- **Do** run when the user says they created a new repo from this template and want to set up/rename for their library.
- If the repo is already partially renamed (e.g. package name changed but some files still have the old name), you can still run: treat the **current** package/project name as the "old" name and replace with the user's desired new name (idempotent only if they ask to rename again to the same name).

## Reference

- Full file list for renames and replacements: see **docs/bootstrap-from-template.md** (if present) or the table in Step 3 above.
- Manual alternative: [TEMPLATE.md](TEMPLATE.md) step 4 and LICENSE/security steps.
