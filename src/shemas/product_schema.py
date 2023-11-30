from datetime import datetime, date
from uuid import UUID

from fastapi import Form

from src.shemas.base_schema import BaseSchemas


class ProductSchema(BaseSchemas):
    uuid: UUID
    is_delete: bool = Form(serialization_alias="inactive")
    create_at: datetime | date | float
    sku: str
    name: str
    price: float
    brand: str
