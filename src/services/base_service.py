from datetime import datetime
from uuid import UUID

from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from src.dependencies.db_session import get_db
from src.models.base import LogicCreationAbstractBaseModel
from src.querys.pagination import PaginateQuery


class BaseService:
    def __init__(
        self,
        model: LogicCreationAbstractBaseModel | type[LogicCreationAbstractBaseModel],
        session: Session = Depends(get_db),
    ):
        self.session = session
        self.model = model

    def get(self, uuid: UUID) -> LogicCreationAbstractBaseModel:
        return self.session.query(self.model).where(self.model.uuid == uuid).one()

    def get_filtered(
        self, model_query: object, paginate: PaginateQuery
    ) -> LogicCreationAbstractBaseModel:
        query = self.session.query(self.model)
        query = query.where(self.model.is_delete == False)  # noqa = 712
        for attr, value in model_query.__dict__.items():
            if value is not None:
                query = query.where(getattr(self.model, attr).in_(value))
        return query.limit(paginate.limit).offset(paginate.offset).all()

    def create(self, form_data: BaseModel) -> LogicCreationAbstractBaseModel:
        new_instance = self.model(**form_data.model_dump())
        self.session.add(new_instance)
        self.session.flush()
        self.session.refresh(new_instance)
        return new_instance

    def update(
        self, model: LogicCreationAbstractBaseModel, form_data: BaseModel
    ) -> LogicCreationAbstractBaseModel:
        for field, value in form_data.model_dump(exclude_none=True).items():
            setattr(model, field, value)
        self.session.flush()
        self.session.refresh(model)
        return model

    def desactivate(
        self, model: LogicCreationAbstractBaseModel
    ) -> LogicCreationAbstractBaseModel:
        model.is_delete = True
        model.delete_at = datetime.now()
        self.session.flush()
        self.session.refresh(model)
        return model

    def activate(self, model: LogicCreationAbstractBaseModel):
        model.is_delete = False
        model.delete_at = None
        self.session.flush()
        self.session.refresh(model)
        return model
