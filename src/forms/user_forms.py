from fastapi import Form
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr, field_validator


class UserCreateForm(BaseModel):
    name: str = Form(...)
    last_name: str = Form(...)
    email: EmailStr = Form(...)
    password: str = Form(...)

    @field_validator("password", mode="after")
    def set_encode_password(cls, v, values):
        return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(v)


class UserUpdateForm(BaseModel):
    name: str = Form(default=None)
    last_name: str = Form(default=None)
    email: EmailStr = Form(default=None)
    password: str = Form(default=None)

    @field_validator("password", mode="after")
    def set_encode_password(cls, v, values):
        if v is not None:
            return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(v)
