"""Example test to verify package and pytest work."""

import re

import kalvi_library_template
from kalvi_library_template import __version__


def test_package_importable() -> None:
    """Package can be imported and exposes public API."""
    assert hasattr(kalvi_library_template, "__version__")
    assert isinstance(kalvi_library_template.__version__, str)
    assert len(kalvi_library_template.__version__) > 0


def test_version() -> None:
    """Package has a version."""
    assert __version__ == "0.1.0"


def test_version_format() -> None:
    """Version string matches semver-like X.Y.Z."""
    assert re.match(r"^\d+\.\d+\.\d+", __version__), "version should be X.Y.Z"
