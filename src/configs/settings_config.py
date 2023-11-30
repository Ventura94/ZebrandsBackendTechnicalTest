from pydantic_settings import SettingsConfigDict, BaseSettings


class SettingsConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )
