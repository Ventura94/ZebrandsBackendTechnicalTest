from uuid import uuid4

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.models.base import UUIDAbstractBaseModel


class AnonymousProductTraceModel(UUIDAbstractBaseModel):
    __tablename__ = "anonymous_products_trace"
    anonymous_user_uuid = Column(UUID(as_uuid=True), default=uuid4, nullable=False)
    ip_address = Column(String, nullable=False, default="Unknown")
    operating_system = Column(String, nullable=False, default="Unknown")
    explorer = Column(String, nullable=False, default="Unknown")
    device = Column(String, nullable=False, default="Unknown")
    product_uuid = Column(UUID, ForeignKey("products.uuid"))
    product = relationship(
        "ProductModel", back_populates="anonymous_products_trace", cascade="all,delete"
    )
