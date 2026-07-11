from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # ------------------------
    # Application
    # ------------------------
    APP_NAME: str = "AMD AI Trading Copilot"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = (
        "Production-grade AI Multi-Agent Swing Trading Copilot"
    )

    FINNHUB_API_KEY: str

    # ------------------------
    # Fireworks AI
    # ------------------------
    FIREWORKS_API_KEY: str

    # ------------------------
    # Database
    # ------------------------
    DATABASE_URL: str

    # ------------------------
    # Authentication
    # ------------------------
    SECRET_KEY: str
    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    # ------------------------
    # Load .env
    # ------------------------
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()