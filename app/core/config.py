# app/core/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",   # load from .env
        extra="ignore"     # <-- accept extra env vars
    )


# Create the settings instance
settings = Settings()  # type: ignore
