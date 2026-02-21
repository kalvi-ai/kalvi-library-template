# Linters and formatters: research and recommendation

What you already have vs what's commonly added for a Python library template (pre-commit, CI, config files, docs).

**Status:** The recommended additions below are **implemented** in this repo (pre-commit hooks, configs, EditorConfig, typos). CI runs `pre-commit run --all-files` so all checks are enforced on push/PR.

---

## Already in this template

| Kind      | Tool       | Role                  | Where                    |
| --------- | ---------- | --------------------- | ------------------------ |
| Python    | Ruff       | Lint + format         | pre-commit, CI          |
| Python    | Pylint     | Lint                  | CI, optional local       |
| Python    | mypy       | Type check            | CI                       |
| Commit msg| Commitizen | Conventional Commits  | pre-commit (commit-msg)  |

---

## Recommended additions (by file type)

### 1. Markdown (`.md`)

- **Tool**: **markdownlint** (e.g. [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli) or [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) via pre-commit).
- **Why**: You have many `.md` files (README, AGENTS.md, skills, docs). Markdownlint enforces consistent structure, list style, line length, and heading hierarchy.
- **Config**: `.markdownlint.yaml` or `.markdownlint.json` (e.g. line-length, rule disable where needed).
- **Enforce**: pre-commit hook + optional CI step.

### 2. YAML (`.yml` / `.yaml`)

- **Tool**: **yamllint** ([adrienverge/yamllint](https://github.com/adrienverge/yamllint)).
- **Why**: Used for `.github/workflows/ci.yml`, `.github/ISSUE_TEMPLATE/*.yml`, `.pre-commit-config.yaml`. Catches syntax errors and style (indent, line length, document start).
- **Lightweight alternative**: pre-commit-hooks' **check-yaml** (syntax only, no style).
- **Recommendation**: Prefer **yamllint** for style + syntax; add a `.yamllint.yaml` (e.g. extend `default`, relax line-length for workflow files if needed).
- **Enforce**: pre-commit + optional CI.

### 3. TOML (e.g. `pyproject.toml`)

- **Tool**: **check-toml** from [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks) (validates TOML syntax).
- **Why**: One place that must be valid is `pyproject.toml`; no need for a separate TOML formatter for a single file.
- **Enforce**: pre-commit (and optionally CI via same pre-commit config).

### 4. JSON (e.g. `.vscode/tasks.json`, `.cursor/mcp.json`)

- **Tool**: **check-json** from pre-commit-hooks (validates JSON syntax).
- **Why**: Prevents invalid JSON in config files.
- **Enforce**: pre-commit (and optionally CI).

### 5. Generic file hygiene (pre-commit-hooks)

Widely used and low-friction:

- **trailing-whitespace** – remove trailing spaces.
- **end-of-file-fixer** – ensure newline at EOF.
- **check-added-large-files** – block huge accidental commits (e.g. max 500KB).
- **check-merge-conflict** – block commit with `<<<<<<<` etc.
- **detect-private-key** – block committed private keys.

All from [pre-commit/pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks).

### 6. Optional but useful

- **EditorConfig** (`.editorconfig`): Indent size, line endings, trim trailing whitespace across editors. Complements linters; no runtime in CI.
- **typos** ([crate-ci/typos](https://github.com/crate-ci/typos)): Spell/typo check in code and docs; can run in pre-commit.
- **actionlint** ([rhysd/actionlint](https://github.com/rhysd/actionlint)): Lint GitHub Actions workflows specifically (stricter than yamllint for Actions). Add if you want strict workflow validation.

---

## Suggested priority

| Priority | What                                                                         | Effort | Impact                                      |
| -------- | ---------------------------------------------------------------------------- | ------ | ------------------------------------------- |
| **1**    | pre-commit-hooks (check-yaml, check-json, check-toml, trailing-whitespace…)  | Low    | Syntax + hygiene on all config/docs         |
| **2**    | markdownlint + config                                                        | Low    | Consistent markdown in README, AGENTS.md…   |
| **3**    | yamllint + config                                                            | Low    | Valid, consistent YAML (workflows, etc.)    |
| **4**    | .editorconfig                                                                | Low    | Consistent editor behavior                  |
| **5**    | typos (optional)                                                             | Low    | Fewer typos in prose and strings            |
| **6**    | actionlint (optional)                                                        | Low    | Stricter GitHub Actions checks              |

---

## Summary

- **Implemented in this template**: Python (Ruff, Pylint, mypy), commit messages (Commitizen), pre-commit-hooks (check-yaml, check-json, check-toml, trailing-whitespace, end-of-file-fixer, check-merge-conflict, detect-private-key, check-added-large-files), yamllint (`.yamllint.yaml`), actionlint (GitHub Actions workflows in `.github/workflows/`), markdownlint (`.markdownlint.yaml`), EditorConfig (`.editorconfig`), typos.
- **Enforcement**: pre-commit runs all of the above; CI runs `pre-commit run --all-files`.

References: [pre-commit hooks](https://pre-commit.com/hooks.html), [yamllint](https://yamllint.readthedocs.io/), [markdownlint](https://github.com/DavidAnson/markdownlint-cli2), [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks).
