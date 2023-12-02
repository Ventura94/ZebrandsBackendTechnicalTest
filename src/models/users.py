from sqlalchemy import (
    Column,
    String,
)

from src.models.base import LogicCreationAbstractBaseModel


class UserModel(LogicCreationAbstractBaseModel):
    __tablename__ = "users"
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
