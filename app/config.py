from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    # ===== Phase 1: base configuration =====
    env: str = Field(default="development")
    api_key: str | None = Field(default=None)
    log_level: str = Field(default="INFO")

    # ===== Placeholders for later phases =====
    source_system: str | None = Field(default=None)
    openrouter_key: str | None = Field(default=None)
    mcp_server_url: str | None = Field(default=None)

    # ===== Future keys already present in .env (safe to keep) =====
    gdrive_shared_drive_id: str | None = Field(default=None)
    gdrive_service_account_json_path: str | None = Field(default=None)
    openrouter_model: str | None = Field(default=None)

    # Accept unknown keys gracefully
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
