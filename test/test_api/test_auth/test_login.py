from httpx import Client

from test.factories.user import UserAlchemyFactory


def test_login_user(client: Client):
    fake_user = UserAlchemyFactory()
    response = client.post(f"/v1/auth/login", data={"username": fake_user.email, "password": "password"}, )
    assert response.status_code == 200
    assert response.json()


def test_login_user_invalid(client: Client):
    fake_user = UserAlchemyFactory()
    response = client.post(f"/v1/auth/login", data={"username": fake_user.email, "password": "invalid_password"}, )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Incorrect Authentication Credentials'}
