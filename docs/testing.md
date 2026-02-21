# Testing

Tests live in `tests/` and use **pytest**. The project is configured so `pythonpath` includes `src`, so you can `import kalvi_library_template` in tests.

## Running tests

```bash
uv run pytest
uv run pytest --cov=src/kalvi_library_template   # with coverage
uv run nox -s coverage   # coverage with fail-under
```

## Fixtures and conftest

- Put **shared fixtures** in `tests/conftest.py`. Pytest discovers them automatically and injects them into test functions by name.
- Use **dependency injection**: declare fixtures as function parameters. Use `scope="session"` or `scope="module"` when a fixture is expensive and can be shared.
- Built-in fixtures: `tmp_path`, `monkeypatch`, `capsys`, `caplog` are useful for isolation and capturing output.

## Markers (optional)

For larger projects you can add custom markers in `pyproject.toml` and use them to separate unit from integration tests:

```toml
[tool.pytest.ini_options]
markers = [
    "unit: unit tests (fast, no I/O).",
    "integration: integration tests (may use network or DB).",
]
```

Then: `@pytest.mark.unit`, `@pytest.mark.integration`, and run with `-m unit` or `-m integration`.

## Coverage

Coverage is configured in `pyproject.toml` under `[tool.coverage.*]`. Minimum coverage is enforced (e.g. 80%) in CI and when running `uv run nox -s coverage`.
