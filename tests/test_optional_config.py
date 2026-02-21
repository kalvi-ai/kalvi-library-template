"""Smoke test for optional [config] extra (pydantic-settings). Skipped when extra not installed."""

from __future__ import annotations

import os

import pytest


def test_config_extra_available() -> None:
    """Optional [config] extra: pydantic-settings can be used."""
    if os.environ.get("REQUIRE_CONFIG_EXTRA"):
        # In CI job that installs [config], fail (do not skip) if extra is missing.
        try:
            import pydantic_settings  # noqa: F401
        except ImportError:
            pytest.fail(
                "[config] extra was required (REQUIRE_CONFIG_EXTRA=1) but pydantic_settings is not installed"
            )
    else:
        pytest.importorskip("pydantic_settings")

    from pydantic_settings import BaseSettings

    class Settings(BaseSettings):
        debug: bool = False

    s = Settings()
    assert s.debug is False
