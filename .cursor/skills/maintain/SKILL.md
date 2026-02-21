---
name: maintain
description: Keep the library and docs in good shape: sync documentation, CHANGELOG, dependency hygiene, and optional project-review. Use when the user asks to maintain the library, update docs, or keep things up to date.
---

# Maintain library and documentation

Use when the user asks to **maintain the library**, **keep docs in sync**, **update documentation**, **changelog**, or **library hygiene**. Covers documentation, CHANGELOG, dependency hygiene, and optional health checks.

## Input

- **Focus** (optional): e.g. “docs only,” “deps only,” “full maintenance,” or “get ready for release.”

## Steps

1. **Documentation**
   - **README**: Ensure setup, commands, and links match the project (e.g. nox, coverage, optional extras, docs build). Fix broken or outdated sections.
   - **Docstrings**: For public API in `src/`, ensure new or changed code has clear docstrings; update existing ones if behavior changed.
   - **docs/** and **MkDocs**: Update or add pages under `docs/` (e.g. settings-pattern, testing, decisions) if the code or workflow changed. Run `uv run mkdocs build` to confirm the site builds.
   - **AGENTS.md / CONTRIBUTING**: If commands, skills, or workflows changed, update these so agents and contributors see the current flow.

2. **CHANGELOG**
   - Open [CHANGELOG.md](CHANGELOG.md). Under **Unreleased**, add entries for any user-facing changes not yet listed (from recent commits or the current work). Use Keep a Changelog categories: Added, Changed, Deprecated, Removed, Fixed, Security.
   - If preparing a release, ensure the version section and date are updated when the release is cut (see **release** skill).

3. **Dependency and security hygiene**
   - Run `uv run pip-audit`; if there are known vulnerabilities, use **dependency-update** to upgrade affected packages (or document why not).
   - Optionally run `uv lock --upgrade` and then full **run-quality-checks** to catch deprecations or breakages; apply **dependency-update** flow if doing upgrades.

4. **Optional: project health**
   - If the user wants a broader check, run **project-review** (structure, tests, CI, principles, security, docs) and address any high-priority suggestions.

## Output

- Summarize what was updated (docs, CHANGELOG, deps, or “no changes needed”).
- If you made edits, suggest a commit (e.g. `docs: sync README and docs with current commands` or `chore: update CHANGELOG and run pip-audit`). Use **commit** skill for approval if the user wants to commit.

## Boundaries

- Do not bump version or publish; use **release** for that.
- Prefer small, focused commits (e.g. “docs” vs “deps” vs “changelog”) unless the user asked for one combined maintenance commit.
