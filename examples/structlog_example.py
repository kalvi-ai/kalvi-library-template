"""Example: using structlog for structured logging (install with [logging] extra).

Run: uv run python examples/structlog_example.py
(requires: uv sync --extra logging, or install -e ".[logging]")
"""

from __future__ import annotations

import logging

# Optional: integrate structlog with stdlib logging so library loggers benefit.
try:
    import structlog

    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.dev.ConsoleRenderer(),
        ],
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )
except ImportError:
    pass  # structlog not installed; use stdlib logging only


def main() -> None:
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    logging.basicConfig(level=logging.INFO)
    log.info("Hello from structlog example", extra={"key": "value"})


if __name__ == "__main__":
    main()
