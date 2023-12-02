from functools import lru_cache

from fastapi_mail import ConnectionConfig
from pydantic import EmailStr

from src.configs.settings_config import SettingsConfig


class Mail(SettingsConfig):
    MAIL_USERNAME: EmailStr
    MAIL_PASSWORD: str
    MAIL_FROM: EmailStr
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_TLS: bool
    MAIL_SSL: bool


@lru_cache()
def get_mail_settings():
    return Mail()


email_config = ConnectionConfig(
    MAIL_USERNAME=get_mail_settings().MAIL_USERNAME,
    MAIL_PASSWORD=get_mail_settings().MAIL_PASSWORD,
    MAIL_FROM=get_mail_settings().MAIL_FROM,
    MAIL_PORT=get_mail_settings().MAIL_PORT,
    MAIL_SERVER=get_mail_settings().MAIL_SERVER,
    MAIL_STARTTLS=get_mail_settings().MAIL_TLS,
    MAIL_SSL_TLS=get_mail_settings().MAIL_SSL
)
