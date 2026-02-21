#!/usr/bin/env python3
# pylint: disable=invalid-name  # script name check-doc-filenames.py is kebab-case by choice
"""Check that doc markdown filenames follow the convention.

- Root: only allowlisted names (README.md, CONTRIBUTING.md, etc.).
- docs/ and docs/research/: lowercase with hyphens (kebab-case);
  README.md allowed in subdirs.
- Excluded: .cursor/skills/*/SKILL.md, .github/SUGGESTED_ISSUES.md.

Exit 1 and print violating paths if any.
"""

from __future__ import annotations

import re
import subprocess
import sys

ROOT_ALLOWLIST = frozenset(
    {
        "README.md",
        "CONTRIBUTING.md",
        "AGENTS.md",
        "AGENTIC-WORKFLOW.md",
        "TEMPLATE.md",
        "CHANGELOG.md",
        "LICENSE",
    }
)

# kebab-case .md: one or more [a-z0-9] segments joined by hyphens
KEBAB_MD = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.md$")


def get_tracked_md_files() -> list[str]:
    """Return list of tracked .md file paths (relative to repo root)."""
    result = subprocess.run(
        ["git", "ls-files", "*.md", "LICENSE"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return []
    return [p for p in result.stdout.strip().splitlines() if p.strip()]


def is_exempt(path: str) -> bool:
    """Paths that are exempt from doc filename rules."""
    return path == ".github/SUGGESTED_ISSUES.md" or (
        path.startswith(".cursor/skills/") and path.endswith("/SKILL.md")
    )


def check_path(path: str) -> str | None:
    """Return error message if path violates convention, else None."""
    if is_exempt(path):
        return None

    parts = path.split("/")
    name = parts[-1]
    error: str | None = None
    under_docs = parts[0] == "docs"

    if len(parts) == 1:
        if name not in ROOT_ALLOWLIST:
            error = (
                "root: only allowlisted names allowed "
                "(e.g. README.md, CONTRIBUTING.md); "
                f"got {path!r}"
            )
    elif under_docs and name != "README.md" and not KEBAB_MD.match(name):
        error = (
            f"docs: filenames must be lowercase-with-hyphens (kebab-case) or "
            f"README.md; got {path!r}"
        )
    # Other .md under repo (e.g. .cursor, .github) — no constraint from this script

    return error


def main() -> int:
    files = get_tracked_md_files()
    errors: list[str] = []
    for path in files:
        err = check_path(path)
        if err:
            errors.append(err)
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
