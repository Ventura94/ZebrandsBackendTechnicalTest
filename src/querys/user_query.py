from uuid import UUID

from fastapi import Query
from pydantic import EmailStr


class UserQuery:
    def __init__(
            self,
            uuid: list[UUID] = Query(default=None),
            is_delete: list[bool] = Query(default=[False], alias="inactive"),
            name: list[str] = Query(default=None),
            last_name: list[str] = Query(default=None),
            email: list[EmailStr] = Query(default=None),

    ):
        self.uuid = uuid
        self.is_delete = is_delete
        self.name = name
        self.last_name = last_name
        self.email = email
