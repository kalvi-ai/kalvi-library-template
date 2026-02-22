"""Smoke test for optional [logging] extra (structlog). Skipped when not installed."""

from __future__ import annotations

import os

import pytest


def test_logging_extra_available() -> None:
    """Optional [logging] extra: structlog can be used."""
    if os.environ.get("REQUIRE_LOGGING_EXTRA"):
        # In CI job that installs [logging], fail (do not skip) if extra is missing.
        try:
            # pylint: disable=import-error,import-outside-toplevel
            import structlog  # noqa: F401  # pyright: ignore[reportMissingImports]
        except ImportError:
            msg = (
                "[logging] extra required (REQUIRE_LOGGING_EXTRA=1) "
                "but structlog not installed"
            )
            pytest.fail(msg)
    else:
        pytest.importorskip("structlog")

    # pylint: disable=import-error,import-outside-toplevel
    import structlog  # pyright: ignore[reportMissingImports]

    logger = structlog.get_logger()
    bound = logger.bind(extra_test_key="extra_test_value")
    # Verify bound logger works (no exception); actual log output not asserted.
    bound.info("optional logging extra works")
