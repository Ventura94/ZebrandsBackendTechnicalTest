FROM python:3.12 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.12

WORKDIR /zebrands_projects

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONOPTIMIZE=TRUE

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

COPY ./src /zebrands_projects/src

COPY ./alembic.ini /zebrands_projects/alembic.ini

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.asgi:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]