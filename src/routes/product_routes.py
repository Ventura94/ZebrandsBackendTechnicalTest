from uuid import UUID

from fastapi import APIRouter, Depends, Path

from src.dependencies.is_o2auth_authenticate import is_o2auth_authenticate
from src.dependencies.o2auth import o2auth
from src.dependencies.product_change_notification import ProductChangeNotificationBackground
from src.dependencies.register_product_trace import AnonymousProductTraceBackground
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
        is_authenticated=Depends(is_o2auth_authenticate),
        product_trace: AnonymousProductTraceBackground = Depends(),
        service_: ProductService = Depends(),
):
    product = service_.get(uuid)
    if not is_authenticated:
        product_trace.trace_product_in_background(product.uuid)
    return product


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
        change_notification: ProductChangeNotificationBackground = Depends()
):
    instance = service_.get(uuid)
    instance = service_.update(instance, form)
    changes_text = ', '.join(f'{key}: {value}' for key, value in form.model_dump(exclude_none=True).items())
    change_notification.notificate_in_background(
        message=f"Product {instance.name} changed regarding {changes_text}")
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
