from fastapi import Query

from pydantic import BaseModel


class PaginateQuery(BaseModel):
    offset: int = Query(default=0)
    limit: int = Query(default=10)
