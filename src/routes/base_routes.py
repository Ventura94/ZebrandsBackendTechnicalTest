from enum import Enum
from uuid import UUID

from fastapi import APIRouter, Depends, Path

from src.shemas.base_schema import BaseSchemas
from src.querys.pagination import PaginateQuery
from src.services.base_service import BaseService


def create_router(
    schema: type[BaseSchemas],
    service: type[BaseService],
    query,
    create_form,
    update_form,
    prefix: str = "",
    tags: list[str | Enum] | None = None,
):
    router = APIRouter(prefix=prefix, tags=tags)

    @router.get("", response_model=list[schema])
    def get_filtered(
        service_: service = Depends(),
        query_: query = Depends(),
        pagination_query: PaginateQuery = Depends(),
    ):
        return service_.get_filtered(query_, pagination_query)

    @router.get("/{uuid}", response_model=schema)
    def get_one(
        uuid: UUID = Path(...),
        service_: service = Depends(),
    ):
        return service_.get(uuid)

    @router.post("", response_model=schema)
    def create(
        form: create_form,
        service_: service = Depends(),
    ):
        return service_.create(form)

    @router.patch("/{uuid}", response_model=schema)
    def patch(
        form: update_form,
        uuid: UUID = Path(...),
        service_: service = Depends(),
    ):
        instance = service_.get(uuid)
        return service_.update(instance, form)

    @router.delete("/{uuid}", response_model=schema)
    def inactivate(
        uuid: UUID = Path(...),
        service_: service = Depends(),
    ):
        instance = service_.get(uuid)
        return service_.desactivate(instance)

    @router.patch("/activate/{uuid}", response_model=schema)
    def reactivate(
        uuid: UUID = Path(...),
        service_: service = Depends(),
    ):
        instance = service_.get(uuid)
        return service_.activate(instance)

    return router
