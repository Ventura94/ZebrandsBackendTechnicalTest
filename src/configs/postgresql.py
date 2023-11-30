from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from src.configs.settings_config import SettingsConfig


class PostgresqlSettings(SettingsConfig):
    POSTGRESQL_URL: str


@lru_cache()
def get_postgresql_settings():
    return PostgresqlSettings()


class SQLAlchemyConnection:
    def __init__(self, url_connection: str, **kwargs):
        self.engine = create_engine(url_connection, **kwargs)
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def get_session(self) -> Session:
        return self.SessionLocal()


database = SQLAlchemyConnection(get_postgresql_settings().POSTGRESQL_URL)
