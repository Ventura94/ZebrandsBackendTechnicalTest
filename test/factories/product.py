from uuid import uuid4

import factory

from src.models import ProductModel
from test.conftest import Session


class ProductDictFactory(factory.DictFactory):
    uuid = factory.LazyFunction(uuid4)
    sku = factory.Faker("ean13")
    name = factory.Sequence(lambda n: f"Producto {n}")
    price = factory.Faker("pydecimal", left_digits=5, right_digits=2, positive=True)
    brand = factory.Faker("company")


class ProductAlchemyFactory(factory.alchemy.SQLAlchemyModelFactory):
    uuid = factory.LazyFunction(uuid4)
    sku = factory.Faker("ean13")
    name = factory.Sequence(lambda n: f"Producto {n}")
    price = factory.Faker("pydecimal", left_digits=5, right_digits=2, positive=True)
    brand = factory.Faker("company")

    class Meta:
        model = ProductModel
        sqlalchemy_session = Session
