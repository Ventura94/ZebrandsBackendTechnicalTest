from uuid import UUID

from httpx import Client

from test.factories.product import ProductAlchemyFactory, ProductDictFactory


def test_get_product_filters(client: Client):
    [ProductAlchemyFactory() for _ in range(10)]
    response = client.get(f"/v1/products")
    assert response.status_code == 200
    assert len(response.json()) == 10


def test_get_product(client: Client):
    fake_product = ProductAlchemyFactory()
    response = client.get(f"/v1/products/{str(fake_product.uuid)}")
    assert response.status_code == 200
    assert fake_product.uuid == UUID(response.json()["uuid"])
    assert fake_product.name == response.json()["name"]


def test_create_product(client: Client):
    fake_product = ProductDictFactory()
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
    fake_product = ProductDictFactory()
    del fake_product["uuid"]
    del fake_product["name"]
    response = client.post("/v1/products", params=fake_product)
    assert response.status_code == 422


def test_patch_product(client: Client):
    fake_product = ProductAlchemyFactory()
    response = client.patch(
        f"/v1/products/{str(fake_product.uuid)}", json={"brand": "test_brand"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == fake_product.name
    assert response.json()["sku"] == fake_product.sku
    assert response.json()["price"] == float(fake_product.price)
    assert response.json()["brand"] == "test_brand"


def test_inactivate_products(client: Client):
    fake_product = ProductAlchemyFactory()
    response = client.delete(f"/v1/products/{str(fake_product.uuid)}")
    assert response.status_code == 200
    assert response.json()["inactive"]
    assert response.json()["name"] == fake_product.name
    assert response.json()["sku"] == fake_product.sku
    assert response.json()["price"] == float(fake_product.price)
    assert response.json()["brand"] == fake_product.brand


def test_activate_products(client: Client):
    fake_product = ProductAlchemyFactory(is_delete=True)
    response = client.patch(f"/v1/products/activate/{str(fake_product.uuid)}")
    assert response.status_code == 200
    assert not response.json()["inactive"]
    assert response.json()["name"] == fake_product.name
    assert response.json()["sku"] == fake_product.sku
    assert response.json()["price"] == float(fake_product.price)
    assert response.json()["brand"] == fake_product.brand
