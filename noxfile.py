"""Nox sessions: run all checks via uv. Requires uv and a synced project (uv sync --group dev)."""

from __future__ import annotations

import nox


@nox.session(name="tests")
def tests(session: nox.Session) -> None:
    """Run pytest."""
    session.run("uv", "run", "pytest", external=True)


@nox.session(name="lint")
def lint(session: nox.Session) -> None:
    """Run Ruff, Pylint, and mypy."""
    session.run("uv", "run", "ruff", "check", "src", "tests", "scripts", external=True)
    session.run(
        "uv",
        "run",
        "ruff",
        "format",
        "--check",
        "src",
        "tests",
        "scripts",
        external=True,
    )
    session.run(
        "uv", "run", "pylint", "src/kalvi_library_template", "scripts", external=True
    )
    session.run(
        "uv", "run", "mypy", "src/kalvi_library_template", "scripts", external=True
    )


@nox.session(name="coverage")
def coverage(session: nox.Session) -> None:
    """Run pytest with coverage report (fail under configured minimum)."""
    session.run(
        "uv",
        "run",
        "pytest",
        "--cov=src/kalvi_library_template",
        "--cov-report=term-missing",
        "--cov-fail-under=80",
        external=True,
    )


@nox.session(name="security")
def security(session: nox.Session) -> None:
    """Run bandit and pip-audit."""
    session.run(
        "uv",
        "run",
        "bandit",
        "-r",
        "src/kalvi_library_template",
        external=True,
    )
    session.run("uv", "run", "pip-audit", external=True)


@nox.session(name="docs")
def docs(session: nox.Session) -> None:
    """Build MkDocs documentation."""
    session.run("uv", "run", "mkdocs", "build", external=True)


@nox.session(name="pre-commit")
def pre_commit(session: nox.Session) -> None:
    """Run pre-commit on all files."""
    session.run("uv", "run", "pre-commit", "run", "--all-files", external=True)
