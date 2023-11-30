from sqlalchemy import Column, String, DECIMAL

from src.models.base import LogicCreationAbstractBaseModel


class ProductModel(LogicCreationAbstractBaseModel):
    __tablename__ = "products"
    sku = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False, unique=False)
    price = Column(DECIMAL, nullable=False, unique=False)
    brand = Column(String, nullable=False, unique=False)
