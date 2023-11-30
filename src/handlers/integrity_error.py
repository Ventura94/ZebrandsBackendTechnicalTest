import re

from fastapi import Request, status
from sqlalchemy.exc import IntegrityError
from starlette.responses import JSONResponse


async def integrity_exception_handler(request: Request, exc: IntegrityError):
    detail = re.search(r"DETAIL:(.*)", exc.args[0])
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": f"{detail.group(1)}"},
    )
