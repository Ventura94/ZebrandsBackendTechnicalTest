from uuid import UUID

from httpx import Client

from test.factories.user import UserAlchemyFactory, UserDictFactory


def test_get_user_filters(client: Client):
    [UserAlchemyFactory() for _ in range(10)]
    response = client.get("/v1/users")
    assert response.status_code == 200
    assert len(response.json()) == 10


def test_get_user(client: Client):
    fake_user = UserAlchemyFactory()
    response = client.get(f"/v1/users/{str(fake_user.uuid)}")
    assert response.status_code == 200
    assert fake_user.uuid == UUID(response.json()["uuid"])
    assert fake_user.name == response.json()["name"]


def test_create_user(client: Client):
    fake_user = UserDictFactory()
    del fake_user["uuid"]
    response = client.post("/v1/users", json=fake_user)
    assert response.status_code == 200
    assert response.json()
    assert fake_user["name"] == response.json()["name"]


def test_create_user_incomplete_form(client):
    fake_user = UserDictFactory()
    del fake_user["uuid"]
    del fake_user["name"]
    response = client.post("/v1/users", params=fake_user)
    assert response.status_code == 422


def test_patch_user(client: Client):
    fake_user = UserAlchemyFactory()
    response = client.patch(
        f"/v1/users/{str(fake_user.uuid)}", json={"last_name": "test_last_name"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == fake_user.name
    assert response.json()["last_name"] == "test_last_name"


def test_inactivate_users(client: Client):
    fake_user = UserAlchemyFactory()
    response = client.delete(f"/v1/users/{str(fake_user.uuid)}")
    assert response.status_code == 200
    assert response.json()["inactive"]
    assert response.json()["name"] == fake_user.name


def test_activate_users(client: Client):
    fake_user = UserAlchemyFactory(is_delete=True)
    response = client.patch(f"/v1/users/activate/{str(fake_user.uuid)}")
    assert response.status_code == 200
    assert not response.json()["inactive"]
    assert response.json()["name"] == fake_user.name
