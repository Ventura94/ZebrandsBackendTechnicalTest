from contextlib import contextmanager

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import orm

from src.asgi import app
from src.configs.postgresql import database

Session = orm.scoped_session(orm.sessionmaker())


@contextmanager
def sqlaclhemy_session():
    Session.configure(bind=database.engine)
    session = Session()
    try:
        yield session
    finally:
        session.rollback()
        Session.remove()


@pytest.fixture(scope="function")
def client():
    with TestClient(app=app) as client:
        yield client
