from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    Column,
    DateTime,
    Boolean,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class UUIDAbstractBaseModel(Base):
    __abstract__ = True
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4, nullable=False)


class LogicCreationAbstractBaseModel(UUIDAbstractBaseModel):
    __abstract__ = True
    create_at = Column(DateTime, default=datetime.now, nullable=False)
    is_delete = Column(Boolean, default=False, nullable=False)
    delete_at = Column(DateTime, nullable=True)
