from fastapi import APIRouter, Depends
from passlib.context import CryptContext
from sqlalchemy.exc import NoResultFound

from src.exceptions.authentication_failed import AuthenticationFailed
from src.forms.login_form import LoginForm
from src.services.user_service import UserService
from src.shemas.o2auth_schema import AccessTokenSchema

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=AccessTokenSchema)
def login(
    service: UserService = Depends(),
    form_data: LoginForm = Depends(),
):
    try:
        auth_user = service.get_by_email(form_data.username)
    except NoResultFound:
        raise AuthenticationFailed
    if not CryptContext(schemes=["bcrypt"], deprecated="auto").verify(
        form_data.password, auth_user.password
    ):
        raise AuthenticationFailed
    return auth_user
