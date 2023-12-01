from uuid import UUID

from fastapi import APIRouter, Depends, Path

from src.dependencies.o2auth import o2auth
from src.forms.product_forms import ProductCreateForm, ProductUpdateForm
from src.querys.pagination import PaginateQuery
from src.querys.product_query import ProductQuery
from src.services.product_service import ProductService
from src.shemas.product_schema import ProductSchema

router = APIRouter(prefix="/products", tags=["Product"])


@router.get("", response_model=list[ProductSchema])
def get_filtered(
    service_: ProductService = Depends(),
    query_: ProductQuery = Depends(),
    pagination_query: PaginateQuery = Depends(),
):
    return service_.get_filtered(query_, pagination_query)


@router.get("/{uuid}", response_model=ProductSchema)
def get_one(
    uuid: UUID = Path(...),
    service_: ProductService = Depends(),
):
    return service_.get(uuid)


@router.post("", response_model=ProductSchema, dependencies=[Depends(o2auth)])
def create(
    form: ProductCreateForm,
    service_: ProductService = Depends(),
):
    return service_.create(form)


@router.patch("/{uuid}", response_model=ProductSchema, dependencies=[Depends(o2auth)])
def patch(
    form: ProductUpdateForm,
    uuid: UUID = Path(...),
    service_: ProductService = Depends(),
):
    instance = service_.get(uuid)
    return service_.update(instance, form)


@router.delete("/{uuid}", response_model=ProductSchema, dependencies=[Depends(o2auth)])
def inactivate(
    uuid: UUID = Path(...),
    service_: ProductService = Depends(),
):
    instance = service_.get(uuid)
    return service_.desactivate(instance)


@router.patch(
    "/activate/{uuid}", response_model=ProductSchema, dependencies=[Depends(o2auth)]
)
def reactivate(
    uuid: UUID = Path(...),
    service_: ProductService = Depends(),
):
    instance = service_.get(uuid)
    return service_.activate(instance)
