from enum import StrEnum
from uuid import UUID, uuid4

from fastapi import Response, Request
from pydantic import BaseModel


class SameSiteEnum(StrEnum):
    lax = "lax"
    strict = "strict"
    none = "none"


class CookieParameters(BaseModel):
    max_age: int = None
    path: str = "/"
    domain: str | None = None
    secure: bool = False
    httponly: bool = True
    samesite: SameSiteEnum = SameSiteEnum.lax


class AnonymousUserCookieDependency:
    def __init__(
        self, cookie_key: str, cookie_params: CookieParameters = CookieParameters()
    ):
        self.cookie_key = cookie_key
        self.cookie_params = cookie_params

    def __call__(self, request: Request, response: Response):
        cookie_value = request.cookies.get(self.cookie_key)
        if cookie_value:
            return UUID(cookie_value)
        return self.attach_to_response(response)

    def attach_to_response(self, response: Response):
        user_id = str(uuid4())
        response.set_cookie(
            key=self.cookie_key, value=user_id, **dict(self.cookie_params)
        )
        return user_id
