from contextlib import contextmanager

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import orm

from src.asgi import app
from src.configs.postgresql import database
from src.dependencies.db_session import get_db
from src.dependencies.o2auth import o2auth
from test.dependencies.get_db import get_db_override
from test.dependencies.o2auth import o2auth_override

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
    with sqlaclhemy_session() as session:
        app.dependency_overrides[o2auth] = o2auth_override
        app.dependency_overrides[get_db] = get_db_override(session)
        with TestClient(app=app) as client:
            yield client
