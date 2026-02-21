"""Example test to verify package and pytest work."""

from kalvi_library_template import __version__


def test_version() -> None:
    """Package has a version."""
    assert __version__ == "0.1.0"
