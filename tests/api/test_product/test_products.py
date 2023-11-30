from uuid import UUID

from httpx import Client

from src.asgi import app
from src.dependencies.db_session import get_db
from tests.conftest import sqlaclhemy_session
from tests.dependencies.get_db import get_db_override
from tests.factories.product import ProductAlchemyFactory, ProductDictFactory


def test_get_product_filters(client: Client):
    with sqlaclhemy_session() as session:
        app.dependency_overrides[get_db] = get_db_override(session)
        [ProductAlchemyFactory() for _ in range(10)]
        response = client.get(f"/v1/products")
        assert response.status_code == 200
        assert len(response.json()) == 10


def test_get_product(client: Client):
    with sqlaclhemy_session() as session:
        app.dependency_overrides[get_db] = get_db_override(session)
        fake_product = ProductAlchemyFactory()
        response = client.get(f"/v1/products/{str(fake_product.uuid)}")
        assert response.status_code == 200
        assert fake_product.uuid == UUID(response.json()["uuid"])
        assert fake_product.name == response.json()["name"]


def test_create_product(client: Client):
    with sqlaclhemy_session() as session:
        fake_product = ProductDictFactory()
        app.dependency_overrides[get_db] = get_db_override(session)
        fake_product["price"] = float(fake_product["price"])
        del fake_product["uuid"]
        response = client.post(f"/v1/products", json=fake_product)
        assert response.status_code == 200
        assert response.json()
        assert fake_product["name"] == response.json()["name"]
        assert fake_product["sku"] == response.json()["sku"]
        assert fake_product["price"] == response.json()["price"]
        assert fake_product["brand"] == response.json()["brand"]


def test_create_product_incomplete_form(client):
    with sqlaclhemy_session() as session:
        fake_product = ProductDictFactory()
        app.dependency_overrides[get_db] = get_db_override(session)
        del fake_product["uuid"]
        del fake_product["name"]
        response = client.post("/v1/products", params=fake_product)
        assert response.status_code == 422


def test_patch_product(client: Client):
    with sqlaclhemy_session() as session:
        fake_product = ProductAlchemyFactory()
        app.dependency_overrides[get_db] = get_db_override(session)
        response = client.patch(
            f"/v1/products/{str(fake_product.uuid)}", json={"brand": "test_brand"}
        )
        print(response.json())
        assert response.status_code == 200
        assert response.json()["name"] == fake_product.name
        assert response.json()["sku"] == fake_product.sku
        assert response.json()["price"] == float(fake_product.price)
        assert response.json()["brand"] == "test_brand"


def test_inactivate_products(client: Client):
    with sqlaclhemy_session() as session:
        fake_product = ProductAlchemyFactory()
        app.dependency_overrides[get_db] = get_db_override(session)
        response = client.delete(f"/v1/products/{str(fake_product.uuid)}")
        assert response.status_code == 200
        assert response.json()["inactive"]
        assert response.json()["name"] == fake_product.name
        assert response.json()["sku"] == fake_product.sku
        assert response.json()["price"] == float(fake_product.price)
        assert response.json()["brand"] == fake_product.brand


def test_activate_products(client: Client):
    with sqlaclhemy_session() as session:
        fake_product = ProductAlchemyFactory(is_delete=True)
        app.dependency_overrides[get_db] = get_db_override(session)
        response = client.patch(f"/v1/products/activate/{str(fake_product.uuid)}")
        print(response.json())
        assert response.status_code == 200
        assert not response.json()["inactive"]
        assert response.json()["name"] == fake_product.name
        assert response.json()["sku"] == fake_product.sku
        assert response.json()["price"] == float(fake_product.price)
        assert response.json()["brand"] == fake_product.brand
