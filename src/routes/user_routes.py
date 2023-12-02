from uuid import UUID

from fastapi import Depends, APIRouter, Path

from src.configs.application import get_settings
from src.dependencies.api_key import api_key
from src.dependencies.o2auth import o2auth
from src.forms.user_forms import UserCreateForm, UserUpdateForm
from src.querys.pagination import PaginateQuery
from src.querys.user_query import UserQuery
from src.services.user_service import UserService
from src.shemas.user_schema import UserSchema

router = APIRouter(prefix="/users", tags=["User"])


@router.get("", response_model=list[UserSchema], dependencies=[Depends(o2auth)])
def get_filtered(
        service_: UserService = Depends(),
        query_: UserQuery = Depends(),
        pagination_query: PaginateQuery = Depends(),
):
    return service_.get_filtered(query_, pagination_query)


@router.get("/{uuid}", response_model=UserSchema, dependencies=[Depends(o2auth)])
def get_one(
        uuid: UUID = Path(...),
        service_: UserService = Depends(),
):
    return service_.get(uuid)


@router.post("", response_model=UserSchema, dependencies=[Depends(o2auth)])
def create(
        form: UserCreateForm,
        service_: UserService = Depends(),
):
    return service_.create(form)


@router.post("/key", response_model=UserSchema, dependencies=[Depends(api_key)],
             include_in_schema=False if get_settings().API_KEY is None else True)
def create_api_key(
        form: UserCreateForm,
        service_: UserService = Depends(),
):
    return service_.create(form)


@router.patch("/{uuid}", response_model=UserSchema, dependencies=[Depends(o2auth)])
def patch(
        form: UserUpdateForm,
        uuid: UUID = Path(...),
        service_: UserService = Depends(),
):
    instance = service_.get(uuid)
    return service_.update(instance, form)


@router.delete("/{uuid}", response_model=UserSchema, dependencies=[Depends(o2auth)])
def inactivate(
        uuid: UUID = Path(...),
        service_: UserService = Depends(),
):
    instance = service_.get(uuid)
    return service_.desactivate(instance)


@router.patch("/activate/{uuid}", response_model=UserSchema, dependencies=[Depends(o2auth)])
def reactivate(
        uuid: UUID = Path(...),
        service_: UserService = Depends(),
):
    instance = service_.get(uuid)
    return service_.activate(instance)
