import pytest
from fastapi.testclient import TestClient

from src.asgi import app


@pytest.fixture(scope="function")
def client():
    with TestClient(app=app) as client:
        yield client
