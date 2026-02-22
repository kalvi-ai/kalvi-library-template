---
name: release
description: Prepares and publishes a release (version bump, tag, build, PyPI). Use when the user asks to release, publish to PyPI, or tag a version.
---

# Release

1. **Bump version** in `pyproject.toml` and `src/kalvi_library_template/__init__.py` (SemVer).
2. **Changelog**: Update CHANGELOG.md or release notes. If the repo was created from this template, replace the `#` placeholders at the bottom of CHANGELOG with your repo compare/tag URLs (e.g. `https://github.com/org/repo/compare/v0.1.0...HEAD`).
3. **Commit**: Stage release files explicitly (e.g. `git add pyproject.toml src/.../__init__.py CHANGELOG.md`), then `git commit -m "chore: release vX.Y.Z"`. Avoid `git add -A` so unrelated changes are not included.
4. **Tag**: `git tag vX.Y.Z`.
5. **Build**: `uv run python -m build` (produces `dist/`; `build` and `twine` are in dev deps).
6. **Upload**: `uv run twine upload dist/*` (needs PyPI token in env).
7. **Push**: `git push && git push --tags`.

Optional: GitHub release from tag; CI publish on tag if configured.
