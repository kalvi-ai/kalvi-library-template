#!/usr/bin/env python3
# pylint: disable=invalid-name  # script name for Cursor hook
"""Cursor afterFileEdit hook: run ruff format on edited file(s).

Reads JSON payload from stdin (file_path or paths). Runs `uv run ruff format`
on the given path(s). Exit 0 so the hook does not block the agent.
"""

from __future__ import annotations

import contextlib
import json
import subprocess
import sys


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        return 0
    paths = []
    for key in ("file_path", "filePath"):
        if key in payload and payload[key]:
            paths.append(payload[key])
            break
    if "paths" in payload:
        paths.extend(payload["paths"])
    paths = [p for p in paths if p and (p.endswith(".py") or "/" in p)]
    if not paths:
        return 0
    with contextlib.suppress(subprocess.TimeoutExpired, FileNotFoundError):
        subprocess.run(
            ["uv", "run", "ruff", "format", "--", *paths],
            check=False,
            capture_output=True,
            timeout=30,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
