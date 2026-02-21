"""Pytest configuration and shared fixtures."""

from __future__ import annotations

import pytest


@pytest.fixture
def sample_version() -> str:
    """Example fixture: provides a version string for tests."""
    return "0.1.0"
