from datetime import datetime, timedelta, UTC

from jose import jwt
from pydantic import EmailStr, Field, field_validator

from src.configs.application import get_settings
from src.shemas.base_schema import BaseSchemas


def access_token_expire():
    return datetime.now(UTC) + timedelta(
        minutes=get_settings().ACCESS_TOKEN_EXPIRE_MINUTES
    )


class AccessTokenSchema(BaseSchemas):
    name: str
    last_name: str | None
    email: EmailStr
    access_token_expire: datetime = Field(default_factory=access_token_expire)
    access_token: str | None = Field(default=None, validate_default=True)
    token_type: str = Field(default="bearer")

    @field_validator("access_token", mode="before")
    def set_access_token(cls, v, values):
        token_data = {
            "iss": "zebrands.mx",
            "sub": values.data["email"],
            "aud": get_settings().TOKEN_AUD,
            "nbf": datetime.now(UTC),
            "exp": values.data["access_token_expire"],
        }
        return jwt.encode(token_data, get_settings().SECRET_KEY)
