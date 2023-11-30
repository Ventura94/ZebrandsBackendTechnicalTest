from uuid import UUID

from fastapi import Query


class ProductQuery:
    def __init__(
        self,
        uuid: list[UUID] = Query(default=None),
        is_delete: list[bool] = Query(default=[False], alias="inactive"),
        name: list[str] = Query(default=None),
        sku: list[str] = Query(default=None),
        price: list[float] = Query(default=None),
        brand: list[str] = Query(default=None),
    ):
        self.uuid = uuid
        self.is_delete = is_delete
        self.name = name
        self.sku = sku
        self.price = price
        self.brand = brand
