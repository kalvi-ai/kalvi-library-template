# Settings and environment configuration

This template uses **Pydantic Settings** for type-safe, environment-based configuration. Install the optional extra: `uv add ".[config]"` or `pip install package[config]`.

## Pattern

- **Do not** use `python-dotenv` or `load_dotenv()` in library code. Production should set environment variables via the platform (host, CI, container).
- For **local development**, use a `.env` file. Pydantic Settings can load it via `env_file=".env"` so you don't need to export variables manually. Copy [.env.example](../.env.example) to `.env` and never commit `.env`.

## Example

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="MYAPP_",  # optional: only read MYAPP_* vars
    )
    debug: bool = False
    log_level: str = "INFO"
```

Then in your app: `settings = Settings()` — it reads from the environment (and optionally from `.env` if present). Use `settings.debug`, `settings.log_level`, etc.

## Nested settings

For nested models, use `env_nested_delimiter` (e.g. `__`) so that `MYAPP_DB__HOST=localhost` maps to `settings.db.host`.
