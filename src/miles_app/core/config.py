from functools import lru_cache

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

LOCAL_DATABASE_URL = "postgresql+psycopg://miles_app:miles_app_local@localhost:5432/miles_app"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_env: str = Field(default="local")
    app_name: str = Field(default="miles-app")
    log_level: str = Field(default="INFO")

    database_url: str = Field(default=LOCAL_DATABASE_URL)

    scraper_timeout: int = Field(default=30)
    scraper_retry_limit: int = Field(default=3)
    default_search_interval: int = Field(default=60)

    resend_api_key: str | None = Field(default=None)
    notification_from_email: str | None = Field(default=None)

    dd_api_key: str | None = Field(default=None)
    dd_site: str = Field(default="datadoghq.com")
    dd_service: str = Field(default="miles-app")
    dd_env: str = Field(default="local")
    dd_version: str = Field(default="0.1.0")

    @field_validator("database_url", mode="before")
    @classmethod
    def use_local_database_url_when_empty(cls, value: str | None) -> str:
        if value is None or not value.strip():
            return LOCAL_DATABASE_URL
        return value


@lru_cache
def get_settings() -> Settings:
    return Settings()
