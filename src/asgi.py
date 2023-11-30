import os
from contextlib import asynccontextmanager

from alembic.command import upgrade
from alembic.config import Config
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.configs.application import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    upgrade(
        Config(os.path.join(os.path.dirname(os.path.dirname(__file__)), "alembic.ini")),
        "head",
    )
    yield


app = FastAPI(
    title=get_settings().PROJECT_NAME,
    debug=get_settings().DEBUG,
    version=get_settings().VERSION,
    docs_url=get_settings().DOCS_URL,
    openapi_url=get_settings().OPENAPI_URL,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
async def health_check():
    return {"status": "Ok", "version": get_settings().VERSION}
