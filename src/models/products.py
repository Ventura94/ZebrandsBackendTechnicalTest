from sqlalchemy import Column, String, DECIMAL
from sqlalchemy.orm import relationship

from src.models.base import LogicCreationAbstractBaseModel


class ProductModel(LogicCreationAbstractBaseModel):
    __tablename__ = "products"
    sku = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False, unique=False)
    price = Column(DECIMAL, nullable=False, unique=False)
    brand = Column(String, nullable=False, unique=False)
    anonymous_products_trace = relationship(
        "AnonymousProductTraceModel", back_populates="product", cascade="all,delete"
    )
