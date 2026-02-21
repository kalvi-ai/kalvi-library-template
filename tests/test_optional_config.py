"""Smoke test for optional [config] extra (pydantic-settings). Skipped when extra not installed."""

from __future__ import annotations

import pytest


def test_config_extra_available() -> None:
    """Optional [config] extra: pydantic-settings can be used."""
    pytest.importorskip("pydantic_settings")
    from pydantic_settings import BaseSettings

    class Settings(BaseSettings):
        debug: bool = False

    s = Settings()
    assert s.debug is False
