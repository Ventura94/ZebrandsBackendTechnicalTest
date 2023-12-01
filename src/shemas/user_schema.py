from datetime import datetime, date
from uuid import UUID

from fastapi import Form
from pydantic import EmailStr

from src.shemas.base_schema import BaseSchemas


class UserSchema(BaseSchemas):
    uuid: UUID
    is_delete: bool = Form(serialization_alias="inactive")
    create_at: datetime | date | float
    name: str
    last_name: str
    email: EmailStr
