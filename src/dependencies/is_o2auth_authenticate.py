from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from src.dependencies.o2auth import o2auth

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/v1/auth/login", description="authorization", auto_error=False
)


def is_o2auth_authenticate(token: str = Depends(oauth2_scheme)) -> bool:
    if token:
        o2auth(token)  # I check the validity of the token
        return True
    return False
