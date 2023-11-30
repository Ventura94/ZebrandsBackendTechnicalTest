from functools import lru_cache

from src.configs.settings_config import SettingsConfig
from src.version import __version__


class Application(SettingsConfig):
    DEBUG: bool = True
    PROJECT_NAME: str = "ZebrandsBackendTechnicalTest"
    VERSION: str = __version__
    DOCS_URL: str = "docs"
    OPENAPI_URL: str = "/openapi.json"


@lru_cache()
def get_settings():
    return Application()
