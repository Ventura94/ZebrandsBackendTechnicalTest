from fastapi import Depends
from sqlalchemy.orm import Session

from src.dependencies.db_session import get_db
from src.models import ProductModel
from src.services.base_service import BaseService


class ProductService(BaseService):
    def __init__(self, session: Session = Depends(get_db)):
        super().__init__(ProductModel, session)
