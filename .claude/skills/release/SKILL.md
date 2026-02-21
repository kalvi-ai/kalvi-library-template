---
name: release
description: Prepares and publishes a release (version bump, tag, build, PyPI). Use when the user asks to release, publish to PyPI, or tag a version.
---

# Release

1. **Bump version** in `pyproject.toml` and `src/kalvi_library_template/__init__.py` (SemVer).
2. **Changelog**: Update CHANGELOG.md or release notes.
3. **Validate**: Run **run-quality-checks** (or at least `uv run pytest` and `uv run ruff check src tests scripts`) so the tree is green before committing.
4. **Commit**: `git add -A && git commit -m "chore: release vX.Y.Z"`.
5. **Tag**: `git tag vX.Y.Z`.
6. **Build**: `uv run python -m build` (produces `dist/`; `build` and `twine` are in dev deps).
7. **Upload**: `uv run twine upload dist/*` (needs PyPI token in env).
8. **Push**: `git push && git push --tags`.

Optional: GitHub release from tag; CI publish on tag if configured.
