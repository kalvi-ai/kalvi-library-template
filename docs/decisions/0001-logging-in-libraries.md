# Logging in libraries: stdlib only, app configures

## Context and Problem Statement

Libraries need to emit log events for debugging and observability, but must not take over logging configuration. The consuming application should control handlers, levels, and format (e.g. JSON in production, pretty console in dev).

## Decision Outcome

Chosen option: **Use only the standard library `logging` module in library code. Do not call `logging.basicConfig()` or install handlers.**

- In this library: use `logging.getLogger(__name__)` and log via that logger. Do not configure logging globally.
- Applications that use this library: call `logging.basicConfig()` or `logging.config.dictConfig()` (or use a framework) to set handlers and levels.
- For structured (key-value) logging: the template provides an optional extra `[logging]` with **structlog**. Applications that want structured logs can install `package[logging]` and use structlog; see the structlog example in the docs.

### Consequences

- Good: Library works with any application logging setup; no hidden configuration; Twelve-Factor friendly (apps log to stdout, platform handles aggregation).
- Good: Apps can opt in to structlog via the `[logging]` extra and the documented example.
