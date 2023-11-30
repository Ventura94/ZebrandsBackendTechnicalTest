from fastapi import Request, status
from sqlalchemy.exc import NoResultFound
from starlette.responses import JSONResponse


async def no_result_found_exception_handler(request: Request, exc: NoResultFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Not Found"},
    )
