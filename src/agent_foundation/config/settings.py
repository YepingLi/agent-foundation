from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="AF_",
        env_file=".env",
        extra="ignore",
    )

    llm_provider: str = "gemini"
    llm_model: str | None = None
    rag_provider: str | None = None
    log_level: str = "INFO"


def load_settings() -> AppSettings:
    return AppSettings()
