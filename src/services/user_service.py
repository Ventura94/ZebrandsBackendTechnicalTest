from fastapi import Depends
from pydantic import EmailStr
from sqlalchemy.orm import Session

from src.dependencies.db_session import get_db
from src.models import UserModel
from src.services.base_service import BaseService


class UserService(BaseService):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(UserModel, session)

    def get_by_email(self, email: EmailStr, is_delete: bool = False) -> UserModel:
        return (
            self.session.query(self.model)
            .where(self.model.email == email, self.model.is_delete == is_delete)
            .one()
        )
