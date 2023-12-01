from uuid import uuid4

import factory
from passlib.context import CryptContext

from src.models import UserModel
from test.conftest import Session


class UserDictFactory(factory.DictFactory):
    uuid = factory.LazyFunction(uuid4)
    name = factory.Faker("name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = CryptContext(schemes=["bcrypt"], deprecated="auto").hash("password")


class UserAlchemyFactory(factory.alchemy.SQLAlchemyModelFactory):
    uuid = factory.LazyFunction(uuid4)
    name = factory.Faker("name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = CryptContext(schemes=["bcrypt"], deprecated="auto").hash("password")

    class Meta:
        model = UserModel
        sqlalchemy_session = Session
