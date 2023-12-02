from fastapi import Form
from pydantic import BaseModel


class ProductCreateForm(BaseModel):
    name: str = Form(...)
    sku: str = Form(...)
    price: float = Form(...)
    brand: str = Form(...)


class ProductUpdateForm(BaseModel):
    name: str = Form(default=None)
    sku: str = Form(default=None)
    price: float = Form(default=None)
    brand: str = Form(default=None)
