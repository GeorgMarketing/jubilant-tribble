from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
from .utils import normalize_link


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=("bot/.env", ".env", "bot/env"), env_prefix="", case_sensitive=False)

    BOT_TOKEN: str
    MANAGER_URL: str
    CHAT_LINK_DEFAULT: str
    CHAT_LINK_USDT: str
    CORE_REG_URL: str
    DB_PATH: str = "bot/storage.db"
    LOG_LEVEL: str = "INFO"

    # webhook settings
    WEBHOOK_URL: str | None = None  # Полный https URL или None
    WEBHOOK_PATH: str = "/webhook"
    WEBHOOK_SECRET: str = "change_me_secret"
    WEBAPP_HOST: str = "0.0.0.0"
    WEBAPP_PORT: int = 8080


_raw = Settings()
_raw.MANAGER_URL = normalize_link(_raw.MANAGER_URL)
_raw.CHAT_LINK_DEFAULT = normalize_link(_raw.CHAT_LINK_DEFAULT)
_raw.CHAT_LINK_USDT = normalize_link(_raw.CHAT_LINK_USDT)
_raw.CORE_REG_URL = normalize_link(_raw.CORE_REG_URL)
settings = _raw


