from functools import lru_cache

from src.configs.settings_config import SettingsConfig
from src.version import __version__


class Application(SettingsConfig):
    DEBUG: bool = True
    PROJECT_NAME: str = "ZebrandsBackendTechnicalTest"
    VERSION: str = __version__
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    TOKEN_AUD: str = "https://zebrands.alicfornia.com"
    API_KEY: str | None = None


@lru_cache()
def get_settings():
    return Application()
