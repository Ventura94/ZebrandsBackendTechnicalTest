from uuid import UUID

from fastapi import Depends, APIRouter, Path

from src.dependencies.o2auth import o2auth
from src.forms.user_forms import UserCreateForm, UserUpdateForm
from src.querys.pagination import PaginateQuery
from src.querys.user_query import UserQuery
from src.services.user_service import UserService
from src.shemas.user_schema import UserSchema

router = APIRouter(prefix="/users", tags=["User"], dependencies=[Depends(o2auth)])


@router.get("", response_model=list[UserSchema])
def get_filtered(
    service_: UserService = Depends(),
    query_: UserQuery = Depends(),
    pagination_query: PaginateQuery = Depends(),
):
    return service_.get_filtered(query_, pagination_query)


@router.get("/{uuid}", response_model=UserSchema)
def get_one(
    uuid: UUID = Path(...),
    service_: UserService = Depends(),
):
    return service_.get(uuid)


@router.post("", response_model=UserSchema)
def create(
    form: UserCreateForm,
    service_: UserService = Depends(),
):
    return service_.create(form)


@router.patch("/{uuid}", response_model=UserSchema)
def patch(
    form: UserUpdateForm,
    uuid: UUID = Path(...),
    service_: UserService = Depends(),
):
    instance = service_.get(uuid)
    return service_.update(instance, form)


@router.delete("/{uuid}", response_model=UserSchema)
def inactivate(
    uuid: UUID = Path(...),
    service_: UserService = Depends(),
):
    instance = service_.get(uuid)
    return service_.desactivate(instance)


@router.patch("/activate/{uuid}", response_model=UserSchema)
def reactivate(
    uuid: UUID = Path(...),
    service_: UserService = Depends(),
):
    instance = service_.get(uuid)
    return service_.activate(instance)
